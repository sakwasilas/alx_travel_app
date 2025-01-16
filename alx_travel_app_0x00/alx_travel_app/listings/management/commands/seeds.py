from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        listings = [
            {"title": "Beachside Villa", "description": "A lovely villa by the beach.", "price": 250.00},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains.", "price": 150.00},
            {"title": "City Apartment", "description": "Modern apartment in the city center.", "price": 300.00},
        ]

        for listing_data in listings:
            listing, created = Listing.objects.get_or_create(**listing_data)
            if created:
                self.stdout.write(f"Created listing: {listing.title}")
            else:
                self.stdout.write(f"Listing already exists: {listing.title}")