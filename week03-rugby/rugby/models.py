from django.core.exceptions import ValidationError
from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=80, unique=True)
    specialist = models.BooleanField(default=False, help_text="Only players approved for this specialist role should be assigned.")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class RugbyTeam(models.Model):
    name = models.CharField(max_length=100, unique=True)
    home_ground = models.CharField(max_length=120, blank=True)
    founded_year = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField(null=True, blank=True)
    team = models.ForeignKey(RugbyTeam, on_delete=models.SET_NULL, null=True, blank=True, related_name="players")
    positions = models.ManyToManyField(Position, through="PlayerPosition", related_name="players", blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class PlayerPosition(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    approved_for_specialist_role = models.BooleanField(default=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["player", "position"], name="unique_player_position")]

    def clean(self):
        if self.position_id and self.position.specialist and not self.approved_for_specialist_role:
            raise ValidationError({"approved_for_specialist_role": "Confirm the player's specialist-role approval before assigning this position."})

    def __str__(self):
        return f"{self.player} — {self.position}"
