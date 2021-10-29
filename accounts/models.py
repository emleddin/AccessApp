from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    NO_DISABILITY = 'ND'
    NO_AID = 'NA'
    WHEELCHAIR = 'WHEEL'
    CANE = 'CANE'
    WALKER = 'WALKER'
    CRUTCHES = 'CRUTCHES'
    SCOOTER = 'SCOOTER'
    GUIDE_DOG ='GUIDE'
    MOBILITY_TYPE = [
        (NO_DISABILITY, 'No mobility disability'),
        (NO_AID, 'No primary mobility aid'),
        (WHEELCHAIR, 'Wheelchair'),
        (CANE, 'Cane'),
        (WALKER, 'Walker'),
        (CRUTCHES, 'Crutches'),
        (SCOOTER, 'Scooter'),
        (GUIDE_DOG, 'Guide Dog')
    ]

    student_id = models.PositiveIntegerField(null=True, blank=False)
    mobility_type = models.CharField(
        max_length=10,
        choices=MOBILITY_TYPE,
        blank=False
    )
