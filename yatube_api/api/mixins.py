from rest_framework import mixins, viewsets


class GetPostFollowMixin(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    pass
