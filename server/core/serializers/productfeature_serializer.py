from rest_framework import serializers
from core.models import Productfeatures


class ProductFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productfeatures
        fields = ['text', 'ordernumber', ]
