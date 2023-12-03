from django.db import models

class BookingAgent(models.Model):
    agent_id = models.IntegerField(primary_key=True)
    agent_name = models.CharField(max_length=50)
    agent_email = models.EmailField(max_length=100)
    agent_phone = models.CharField(max_length=20)

# Define other models (Airports, Passengers, FlightSchedule, Payments, TravelClassCapacity, FlightCoast) similarly
