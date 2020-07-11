from .base import *

# 개발기간에는 배포환경도 임시로 디버그 호스트 모두 허용
# 완성 후에는 변경해야함

DEBUG = True

ALLOWED_HOSTS = ['*']