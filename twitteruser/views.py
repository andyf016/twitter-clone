from django.shortcuts import render

# Create your views here.
"""
    @classmethod
    def follow(cls, current_user, following):
        following, created = cls.objects.get_or_create(
            current_user=current_user
        )
        following.owner.add(following)
"""