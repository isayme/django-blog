import os
from django.utils.encoding import filepath_to_uri
from django.utils.six.moves.urllib.parse import urljoin

from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.conf import settings

from qiniu import Auth, BucketManager, put_data

class QiniuStorage(Storage):
    def __init__(self):
        self.ak = os.environ.get('QINIU_ACCESS_KEY', getattr(settings, 'QINIU_ACCESS_KEY', None))
        self.sk = os.environ.get('QINIU_SECRET_KEY', getattr(settings, 'QINIU_SECRET_KEY', None))
        self.bn = os.environ.get('QINIU_BUCKET_NAME', getattr(settings, 'QINIU_BUCKET_NAME', None))
        self.base_url = os.environ.get('QINIU_BUCKET_DOMAIN', getattr(settings, 'QINIU_BUCKET_DOMAIN', None))

        self.auth = Auth(self.ak, self.sk)

    def _open(self, name, mode='wb'):
        return ContentFile(name, mode)

    def _clean_name(self, name):
        return name[2:]

    def _save(self, name, content):
        name = self._clean_name(name)

        if hasattr(content, 'chunks'):
            data = ''.join(chunk for chunk in content.chunks())
        else:
            data = content.read()

        token = self.auth.upload_token(self.bn, name)

        ret, info = put_data(token, name, data)

        return name

    def delete(self, name):
        bucket = BucketManager(self.auth)
        bucket.delete(self.bn, name)

    def size(self, name):
        name = self._clean_name(name)

        bucket = BucketManager(self.auth)
        ret, info = bucket.stat(self.bn, name)
        return ret and ret['fsize']

    def exists(self, name):
        name = self._clean_name(name)

        bucket = BucketManager(self.auth)
        ret, info = bucket.stat(self.bn, name)
        return ret and ret['hash']

    def url(self, name):
        return urljoin(self.base_url, filepath_to_uri(name))
