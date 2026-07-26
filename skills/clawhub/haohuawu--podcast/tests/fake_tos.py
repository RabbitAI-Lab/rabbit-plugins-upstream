"""In-memory stand-in for the `tos` SDK — the single TOS mock for the whole suite.

Injected by conftest.py as ``sys.modules["tos"]`` BEFORE any script imports it,
so ``tos_uploader`` / ``update_metadata`` / ``generate_podcast`` all transparently
talk to one shared in-memory bucket. Tests reset it via the ``tos_bucket`` fixture.

Design rules (mirrors the real SDK's surface actually used by the scripts):
  - client.put_object(bucket, key=..., content=..., content_type=..., cache_control=...)
  - client.get_object(bucket, key=...) -> object with .read() -> bytes
  - missing key raises tos.exceptions.TosServerError with .status_code == 404
"""

import types


class TosServerError(Exception):
    def __init__(self, status_code: int = 500, message: str = ""):
        super().__init__(message or f"TosServerError({status_code})")
        self.status_code = status_code


class _GetResult:
    def __init__(self, data: bytes):
        self._data = data

    def read(self) -> bytes:
        return self._data


class FakeTosClient:
    """All instances share one bucket so separate TOSUploader() objects see the same state."""

    store: dict = {}        # key -> bytes
    meta: dict = {}         # key -> {"content_type": ..., "cache_control": ...}
    put_log: list = []      # keys in put order (write-order assertions)

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def reset(cls):
        cls.store.clear()
        cls.meta.clear()
        cls.put_log.clear()

    def put_object(self, bucket=None, key=None, content=None, content_type=None,
                   cache_control=None, **kwargs):
        data = content.read() if hasattr(content, "read") else content
        if isinstance(data, str):
            data = data.encode("utf-8")
        FakeTosClient.store[key] = bytes(data)
        FakeTosClient.meta[key] = {"content_type": content_type, "cache_control": cache_control}
        FakeTosClient.put_log.append(key)

    def get_object(self, bucket, key=None):
        if key not in FakeTosClient.store:
            raise TosServerError(404, f"NoSuchKey: {key}")
        return _GetResult(FakeTosClient.store[key])


def as_module() -> types.ModuleType:
    mod = types.ModuleType("tos")
    mod.TosClientV2 = FakeTosClient
    exceptions = types.ModuleType("tos.exceptions")
    exceptions.TosServerError = TosServerError
    mod.exceptions = exceptions
    return mod
