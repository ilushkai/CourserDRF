from rest_framework import serializers

allowed_links = ['https://www.youtube.com']

def validator_banned_links(value):
    if value.lower()[:23] not in allowed_links or not None:
        raise serializers.ValidationError('Это не те ссылки')
