from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index for email
        db.users.create_index([('email', 1)], unique=True)

        # Sample data
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'marvel'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': 'marvel'},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'marvel'},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': 'dc'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'dc'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'dc'},
        ]
        teams = [
            {'name': 'marvel', 'members': ['ironman@marvel.com', 'cap@marvel.com', 'spiderman@marvel.com']},
            {'name': 'dc', 'members': ['superman@dc.com', 'batman@dc.com', 'wonderwoman@dc.com']},
        ]
        activities = [
            {'user_email': 'ironman@marvel.com', 'activity': 'run', 'duration': 30},
            {'user_email': 'superman@dc.com', 'activity': 'fly', 'duration': 60},
        ]
        leaderboard = [
            {'team': 'marvel', 'points': 100},
            {'team': 'dc', 'points': 120},
        ]
        workouts = [
            {'name': 'Push Ups', 'difficulty': 'easy'},
            {'name': 'Flight', 'difficulty': 'superhero'},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
