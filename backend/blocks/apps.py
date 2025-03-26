from django.apps import AppConfig


class BlocksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blockchain.blocks'  # Must match your Python import path
    label = 'blocks_app'
