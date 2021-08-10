from django.db.models import fields
from django.http import response
from django.shortcuts import render
# import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import csv
from rest_framework import serializers
from .models import KPIModel
from datetime import datetime
from django.db.models import Q
from django.db.models import Count, F


class KPIModelSerializer(serializers.ModelSerializer):

    sprint_start_date = serializers.DateField(format=None, input_formats=['%d-%m-%y %H:%M',])
    sprint_end_date = serializers.DateField(format=None, input_formats=['%d-%m-%y %H:%M',])
    last_status_change_date = serializers.DateField(format=None, input_formats=['%d-%m-%y %H:%M',])

    class Meta:
        model = KPIModel
        fields = '__all__'


class KPIModelView(APIView):

    serializer_class = KPIModelSerializer

    def post(self, request):
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return Response({'error':'please upload a csv file format'}, status=status.HTTP_400_BAD_REQUEST)

        var_decode = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(var_decode)

        serializer = self.serializer_class(data=list(reader), many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class RetrieveStoryPointsData(APIView):

    def get(self, request):
        query_data = KPIModel.objects.filter(Q(work_item_type__iexact='User Story', tags__icontains="MMPV2.1") & 
        ~Q(current_status__iexact='Removed'))
        total_sum = 0
        closed_status_poinst = 0

        for data in query_data:
            if not data.story_points == '':
                total_sum = total_sum + int(data.story_points)
            if data.current_status == 'Closed':
                closed_status_poinst = closed_status_poinst + int(data.story_points)

        per_cal = (closed_status_poinst/total_sum)*100
        return Response({'Percentage':per_cal}, status=status.HTTP_200_OK)


class RetrieveIncomeandFixedPointsData(APIView):

    def get(self, request):
        query_data = KPIModel.objects

        incoming_defects = 0
        fixed_defects = 0

        for data in query_data.filter(work_item_type='Bug'):
            if data.creation_date > data.sprint_start_date and data.creation_date <= data.sprint_end_date:
                incoming_defects = incoming_defects + 1
        grouped_data = KPIModel.objects.values('sprint_name').filter(current_status__iexact='Closed').annotate(fixed_defects=Count('id'))

        return Response({'incoming_defects':incoming_defects, 'fixed_defects':grouped_data}, status=200)


