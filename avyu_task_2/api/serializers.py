from rest_framework import serializers

from api import models


class CardsSerializer(serializers.ModelSerializer):
    # поля: серия, номер, дата выпуска, дата окончания активности, статус
    date_expiration = serializers.DateTimeField(read_only=True,)

    class Meta:
        fields = (
            'series',
            'number',
            'date_release',
            'date_expiration',
            'status'
        )
        model = models.Card

    # def create(self, validated_data):
        # request = self.context.get('request')
        # ingredients = validated_data.pop('ingredients')
        # tags = validated_data.pop('tags')
        # recipe = models.Recipe.objects.create(
        #     **validated_data,
        #     author=request.user)
        # recipe.tags.set(tags)
        # self.create_recipe_ingredients(recipe, ingredients)
        # return recipe
