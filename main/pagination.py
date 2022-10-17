from rest_framework.pagination import LimitOffsetPagination

class LimitPagination(LimitOffsetPagination):
    default_limit = 10