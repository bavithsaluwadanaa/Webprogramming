from datetime import date
from django.core.management.base import BaseCommand
from directory.models import Module, Student

class Command(BaseCommand):
    help = "Create a small set of sample modules and students"
    def handle(self, *args, **options):
        modules = [Module.objects.get_or_create(code=code, defaults={"name": name})[0] for code, name in [("MOD002619", "Web Programming"), ("MOD002691", "Final Project"), ("MOD003212", "Introduction to Programming")]]
        people = [("Amara", "Perera", 21, "amara@example.edu"), ("Kavindu", "Silva", 22, "kavindu@example.edu"), ("Nethmi", "Fernando", 20, "nethmi@example.edu"), ("Dilan", "Jayasinghe", 23, "dilan@example.edu"), ("Sajani", "Wijesinghe", 21, "sajani@example.edu"), ("Ravi", "Perera", 24, "ravi@example.edu"), ("Mala", "Fernando", 20, "mala@example.edu"), ("Ishan", "Silva", 22, "ishan@example.edu"), ("Tharu", "Gunasekara", 19, "tharu@example.edu"), ("Dinuka", "Senanayake", 21, "dinuka@example.edu"), ("Anjali", "Perera", 20, "anjali@example.edu")]
        for index, (first, last, age, email) in enumerate(people):
            student, _ = Student.objects.get_or_create(email=email, defaults={"first_name": first, "last_name": last, "age": age, "enrolment_date": date(2025, 9, 15)})
            student.modules.add(modules[index % len(modules)], modules[0])
        self.stdout.write(self.style.SUCCESS("Sample directory loaded."))
