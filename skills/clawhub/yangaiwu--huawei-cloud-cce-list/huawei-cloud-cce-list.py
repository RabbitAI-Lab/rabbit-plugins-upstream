#!/usr/bin/env python3
"""查询华为云CCE集群列表 — huaweicloudsdk-cce 实现"""

import argparse
import os
import sys
from typing import Tuple

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions.exceptions import (
    ClientRequestException,
    ServerResponseException,
    ConnectionException,
    RequestTimeoutException,
    SdkException,
)
from huaweicloudsdkcce.v3 import CceClient, ListClustersRequest
from huaweicloudsdkcce.v3.region.cce_region import CceRegion


_EXIT_OK = 0
_EXIT_AUTH_ERR = 3
_EXIT_API_ERR = 4
_EXIT_NET_ERR = 5
_EXIT_UNKNOWN = 6


def _load_credentials() -> Tuple[str, str]:
    ak, sk = "", ""
    for k, v in os.environ.items():
        u = k.upper()
        if not (u.startswith("HUAWEI") or u.startswith("HW") or u.startswith("HWC")):
            continue
        if "ACCESS_KEY" in u or u.endswith("_AK") or u == "AK":
            ak = v or ak
        if "SECRET_KEY" in u or u.endswith("_SK") or u == "SK":
            sk = v or sk
    if not ak or not sk:
        print("错误：未找到 AK/SK 环境变量。请设置 HUAWEICLOUD_SDK_AK / HUAWEICLOUD_SDK_SK", file=sys.stderr)
        sys.exit(_EXIT_AUTH_ERR)
    return ak, sk


def build_client(region: str) -> CceClient:
    ak, sk = _load_credentials()
    creds = BasicCredentials(ak, sk)
    try:
        region_obj = CceRegion.value_of(region)
    except KeyError:
        print(f"错误：不支持的区域 '{region}'", file=sys.stderr)
        sys.exit(_EXIT_API_ERR)
    return CceClient.new_builder() \
        .with_credentials(creds) \
        .with_region(region_obj) \
        .build()


def query_clusters(client: CceClient) -> list:
    request = ListClustersRequest()
    response = client.list_clusters(request)
    return response.items if response.items else []


def format_table(clusters: list) -> str:
    if not clusters:
        return "未找到任何 CCE 集群"

    rows = []
    for c in clusters:
        name = c.metadata.name if c.metadata and c.metadata.name else "-"
        phase = c.status.phase if c.status and c.status.phase else "-"
        version = c.spec.version if c.spec and c.spec.version else "-"
        platform = c.spec.platform_version if c.spec and c.spec.platform_version else "-"
        rows.append((name, phase, version, platform))

    headers = ("名称", "状态", "集群版本", "平台版本")
    col_widths = [len(h) for h in headers]
    for r in rows:
        for i in range(4):
            col_widths[i] = max(col_widths[i], len(r[i]))

    sep = "+-" + "-+-".join("-" * w for w in col_widths) + "-+"
    header = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"
    lines = [sep, header, sep]
    for r in rows:
        line = "| " + " | ".join(r[i].ljust(col_widths[i]) for i in range(4)) + " |"
        lines.append(line)
    lines.append(sep)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="查询华为云CCE集群列表")
    parser.add_argument("--region", default="cn-north-4", help="区域代码，如 cn-north-4")
    args = parser.parse_args()

    try:
        client = build_client(args.region)
        clusters = query_clusters(client)
        print(format_table(clusters))
    except ClientRequestException as e:
        print(f"认证或权限错误 ({e.status_code}): {e.error_msg}", file=sys.stderr)
        if e.status_code == 401:
            print("提示：请检查 AK/SK 是否正确", file=sys.stderr)
        elif e.status_code == 403:
            print("提示：IAM 用户缺少 cce:cluster:list 权限", file=sys.stderr)
        sys.exit(_EXIT_AUTH_ERR) if e.status_code in (401, 403) else sys.exit(_EXIT_API_ERR)
    except ConnectionException:
        print("网络连接失败：无法连接到华为云API", file=sys.stderr)
        print("提示：请检查网络连通性和代理设置", file=sys.stderr)
        sys.exit(_EXIT_NET_ERR)
    except RequestTimeoutException:
        print("请求超时：华为云API 30秒内未响应", file=sys.stderr)
        sys.exit(_EXIT_NET_ERR)
    except ServerResponseException as e:
        print(f"服务器错误 ({e.status_code}): {e.error_msg}", file=sys.stderr)
        sys.exit(_EXIT_API_ERR)
    except SdkException as e:
        print(f"SDK 调用异常: {e}", file=sys.stderr)
        sys.exit(_EXIT_UNKNOWN)
    except Exception as e:
        print(f"未知错误: {e}", file=sys.stderr)
        sys.exit(_EXIT_UNKNOWN)


if __name__ == "__main__":
    main()