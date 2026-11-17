from django.contrib import admin
from .models import Player, PlayerPosition, Position, RugbyTeam

class PlayerPositionInline(admin.TabularInline):
    model = PlayerPosition
    extra = 1

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")
    inlines = (PlayerPositionInline,)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "specialist")
    list_filter = ("specialist",)
    search_fields = ("name",)

@admin.register(RugbyTeam)
class RugbyTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "home_ground", "founded_year")
    search_fields = ("name",)
