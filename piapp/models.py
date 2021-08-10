from django.db import models
from django.db.models.base import ModelState, ModelStateFieldsCacheDescriptor
from django.db.models.fields import URLField


class KPIModel(models.Model):
    '''
        type_id	
        creation_date	
        current_status	
        story_points	
        sprint_name	
        sprint_start_date	
        sprint_end_date	
        tags	
        scrum_team_name	
        severity	
        last_status_change_date	
        release_id	
        reason	
        value_area	
        effort	
        work_item_type
    '''

    status_choices = (
        ('Closed', 'Closed'),
        ('Active', 'Active'),
        ('Design', 'Design'),
        ('Removed', 'Removed'),
    )
    type_id = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    current_status = models.CharField(max_length=50)
    story_points = models.CharField(max_length=10, blank=True, null=True)
    sprint_name = models.CharField(max_length=120)
    sprint_start_date = models.DateTimeField()
    sprint_end_date = models.DateTimeField()
    tags = models.CharField(max_length=120, null=True, blank=True)
    scrum_team_name = models.CharField(max_length=120, null=True, blank=True)
    severity = models.CharField(max_length=120, null=True, blank=True)
    last_status_change_date = models.DateTimeField()
    release_id = models.CharField(max_length=10)
    reason = models.CharField(max_length=50)
    value_area = models.CharField(max_length=60, null=True, blank=True)
    effort = models.CharField(max_length=10, null=True, blank=True)
    work_item_type = models.CharField(max_length=50, blank=True, null=True)