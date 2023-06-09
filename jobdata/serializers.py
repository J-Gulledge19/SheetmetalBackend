from .models import Job, Download
from rest_framework import serializers

# class WeightSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Weight
#         fields = '__all__'
        
class DownloadSerializer(serializers.ModelSerializer):
    # weight = WeightSerializer(many = False)
    class Meta:
        model = Download
        fields = '__all__'
    # def create(self, validated_data):
    #     print(validated_data)
    #     weight_data = validated_data.pop('weight')
    #     print(weight_data)
    #     download = Download.objects.create(**validated_data)
    #     Weight.objects.create(dl=download, **weight_data)
    #     return download
        
class JobSerializer(serializers.ModelSerializer):
    downloads = DownloadSerializer(many = True, read_only=True)
    class Meta:
        model = Job
        fields = '__all__'