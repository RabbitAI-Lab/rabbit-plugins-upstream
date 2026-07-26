#!/usr/bin/env python3
"""火山引擎 TOS 对象存储上传客户端（导入即为了上传，依赖 tos SDK）。

RSS feed 的生成在 rss_feed.py（纯标准库），与上传解耦。
"""

import os
from typing import Optional

import tos


class TOSUploader:
    """火山引擎 TOS 上传客户端。凭证走环境变量，bucket/region 由调用方传入（来自 config.json）。"""

    def __init__(
        self,
        bucket: Optional[str] = None,
        region: Optional[str] = None,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
    ):
        self.access_key = access_key or os.environ.get("TOS_ACCESS_KEY")
        self.secret_key = secret_key or os.environ.get("TOS_SECRET_KEY")
        bucket = bucket or os.environ.get("TOS_BUCKET")
        region = region or os.environ.get("TOS_REGION")
        if not self.access_key or not self.secret_key:
            raise ValueError("缺少 TOS_ACCESS_KEY 或 TOS_SECRET_KEY 环境变量")
        if not bucket or not region:
            raise ValueError("缺少 TOS_BUCKET 或 TOS_REGION 环境变量")

        self.bucket = bucket
        self.region = region
        self.endpoint = f"https://tos-{region}.volces.com"
        self.client = tos.TosClientV2(
            self.access_key, self.secret_key, self.endpoint, region=region
        )

    @property
    def base_url(self) -> str:
        return f"https://{self.bucket}.tos-{self.region}.volces.com"

    def upload_file(self, local_path: str, key: str, content_type: Optional[str] = None) -> str:
        with open(local_path, "rb") as f:
            self.client.put_object(self.bucket, key=key, content=f, content_type=content_type)
        return f"{self.base_url}/{key}"

    def upload_text(self, text: str, key: str,
                    content_type: str = "text/plain; charset=utf-8",
                    cache_control: Optional[str] = None) -> str:
        # 默认值保持中性；feed/json/markdown 由调用方显式指定（见 podcast_store 的 *_CT 常量）
        kwargs = {
            "bucket": self.bucket,
            "key": key,
            "content": text.encode("utf-8"),
            "content_type": content_type,
        }
        if cache_control:
            kwargs["cache_control"] = cache_control
        self.client.put_object(**kwargs)
        return f"{self.base_url}/{key}"

    def download_text(self, key: str) -> Optional[str]:
        """读取对象文本内容；对象不存在返回 None（其余错误照常抛出）"""
        try:
            return self.client.get_object(self.bucket, key=key).read().decode("utf-8")
        except tos.exceptions.TosServerError as e:
            if e.status_code == 404:
                return None
            raise
