from rest_framework import mixins, viewsets


class GetFollowMixin(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    pass
