from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    #Use Signals file to the ready method to create profile for user when its signed up
    def ready(self):
        import users.signals