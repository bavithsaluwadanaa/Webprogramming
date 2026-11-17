import csv
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from rugby.models import Player, PlayerPosition, Position, RugbyTeam

class Command(BaseCommand):
    help = "Load rugby players and positions from rugby/data/players.csv"

    def handle(self, *args, **options):
        file_path = Path(__file__).resolve().parents[2] / "data" / "players.csv"
        if not file_path.exists():
            raise CommandError(f"CSV not found: {file_path}")
        with file_path.open(newline="", encoding="utf-8-sig") as source:
            for row in csv.DictReader(source):
                position, _ = Position.objects.get_or_create(name=row["position"], defaults={"specialist": row["specialist"].lower() == "true"})
                team, _ = RugbyTeam.objects.get_or_create(name=row["team"], defaults={"home_ground": row["home_ground"]})
                player, _ = Player.objects.get_or_create(first_name=row["first_name"], last_name=row["last_name"], defaults={"team": team})
                PlayerPosition.objects.get_or_create(player=player, position=position, defaults={"approved_for_specialist_role": row["approved"].lower() == "true"})
        self.stdout.write(self.style.SUCCESS("Rugby sample data loaded."))
