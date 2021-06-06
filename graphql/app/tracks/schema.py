import graphene
from graphene_django import DjangoObjectType
from  .models  import Track

class TrackType(DjangoObjectType):
    class Meta:
        models = Track
        
class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)
    
    def resolve_tracks(self, info):
        return TrackType.objects.all()