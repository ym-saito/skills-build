from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='marvel')
        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='marvel', members=['test@example.com'])
        self.assertEqual(team.name, 'marvel')
        self.assertEqual(team.members, ['test@example.com'])

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_email='test@example.com', activity='run', duration=10)
        self.assertEqual(activity.user_email, 'test@example.com')
        self.assertEqual(activity.activity, 'run')
        self.assertEqual(activity.duration, 10)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='marvel', points=50)
        self.assertEqual(lb.team, 'marvel')
        self.assertEqual(lb.points, 50)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Push Ups', difficulty='easy')
        self.assertEqual(workout.name, 'Push Ups')
        self.assertEqual(workout.difficulty, 'easy')
