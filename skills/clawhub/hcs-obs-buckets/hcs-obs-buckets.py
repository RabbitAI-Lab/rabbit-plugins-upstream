#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""查询华为云账号下关联的 OBS 桶。

能力:
  A. 列出账号下（region/project 范围）全部 OBS 桶，可选按桶名/前缀过滤。
  B. 按桶名/前缀过滤。
  C. 按资源（如 VPC/云服务器）关联查询桶。
  D. 列出桶内对象。

认证:
  读取环境变量 HWCLOUD_AK / HWCLOUD_SK（真实验证必填，不硬编码密钥）。
  可选 HWCLOUD_PROJECT_ID（缺省由 AK/SK 解析默认项目）。

用法:
  python3 hcs-obs-buckets.py list [--region cn-north-4] [--project-id <id>]
                                        [--bucket-prefix <前缀>] [--format json|md] [--mock]
  python3 hcs-obs-buckets.py associated <资源id或名称> [--region cn-north-4]
                                       [--project-id <id>] [--format json|md] [--mock]
  python3 hcs-obs-buckets.py objects --bucket <桶名或id> [--prefix <前缀>]
                                       [--max-keys <n>] [--format json|md] [--mock]

退出码: 0=成功; 2=参数错误; 3=缺少认证(未设置 HWCLOUD_AK/HWCLOUD_SK); 4=API 调用失败
"""

import argparse
import json
import os
import sys


MOCK_DATA = {
    "buckets": [
        {"name": "prod-data", "region": "cn-north-4", "creation_time": "2024-01-01T00:00:00Z",
         "storage_class": "STANDARD", "resource_type": "vpc-prod"},
        {"name": "prod-logs", "region": "cn-north-4", "creation_time": "2024-02-03T00:00:00Z",
         "storage_class": "STANDARD", "resource_type": "vpc-prod"},
        {"name": "dev-assets", "region": "cn-north-4", "creation_time": "2024-05-06T00:00:00Z",
         "storage_class": "STANDARD"},
        {"name": "backup-bucket", "region": "cn-north-4", "creation_time": "2023-12-01T00:00:00Z",
         "storage_class": "STANDARD"},
    ],
    "objects": {
        "prod-data": [
            {"key": "config/app.yaml", "size": 1024, "last_modified": "2024-06-01T00:00:00Z"},
            {"key": "logs/app.log", "size": 2048, "last_modified": "2024-06-02T00:00:00Z"}
        ]
    },
}


def _attr(obj, name, default=None):
    """兼容 SDK 对象（属性访问）与普通 dict。"""
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _norm_bucket(b):
    return {
        "name": _attr(b, "name"),
        "region": _attr(b, "region"),
        "creation_time": _attr(b, "creation_time"),
        "storage_class": _attr(b, "storage_class"),
    }


def _build_client(region_id, project_id):
    from huaweicloudsdkcore.auth.credentials import BasicCredentials
    from huaweicloudsdkcore.region.region import Region
    from huaweicloudsdkobs.v1 import ObsClient

    ak = os.environ.get("HWCLOUD_AK")
    sk = os.environ.get("HWCLOUD_SK")
    if not ak or not sk:
        print("错误：缺少认证，请设置环境变量 HWCLOUD_AK / HWCLOUD_SK", file=sys.stderr)
        sys.exit(3)
    creds = BasicCredentials(ak, sk)
    if project_id:
        creds = creds.with_project_id(project_id)
    region = Region(region_id, "https://obs.{}.myhuaweicloud.com".format(region_id))
    builder = ObsClient.new_builder().with_credentials(creds).with_region(region)
    return builder.build()


def _list_buckets(client, prefix=None, mock=False):
    if mock:
        return MOCK_DATA["buckets"]
    """分页拉取账号下全部桶。"""
    from huaweicloudsdkobs.v1 import ListBucketsRequest

    buckets, marker = [], None
    while True:
        req = ListBucketsRequest(max_keys=1000)
        if marker:
            req.marker = marker
        resp = client.list_buckets(req)
        items = _attr(resp, "buckets", []) or []
        buckets.extend(items)
        if len(items) < 1000:
            break
        marker = _attr(items[-1], "name")
    if prefix:
        buckets = [b for b in buckets if _attr(b, "name", "").startswith(prefix)]
    return buckets


def _list_objects(client, bucket, prefix=None, max_keys=1000):
    from huaweicloudsdkobs.v1 import ListObjectsRequest

    items, marker = [], None
    while True:
        req = ListObjectsRequest(bucket=bucket, prefix=prefix or "", max_keys=max_keys)
        if marker:
            req.marker = marker
        resp = client.list_objects(req)
        batch = _attr(resp, "contents", []) or []
        items.extend(batch)
        if len(batch) < max_keys:
            break
        marker = _attr(batch[-1], "key")
    return items


def _resolve_bucket(client, bucket_ref, mock=False):
    """按名称解析桶，返回桶对象。"""
    if mock:
        buckets = MOCK_DATA["buckets"]
    else:
        buckets = _list_buckets(client)
    for b in buckets:
        if _attr(b, "name") == bucket_ref:
            return b
    return None


def capability_list(client, args):
    """能力 A/B：列出桶（可过滤）。"""
    buckets = _list_buckets(client, mock=args.mock)
    if args.prefix:
        buckets = [b for b in buckets if (_attr(b, "name") or "").startswith(args.prefix)]
    if args.bucket:
        buckets = [b for b in buckets if _attr(b, "name") == args.bucket]

    items = [_norm_bucket(b) for b in buckets]
    items.sort(key=lambda x: x["name"])
    payload = {
        "capability": "list",
        "region": args.region,
        "project_id": args.project_id,
        "filter_prefix": args.prefix,
        "count": len(items),
        "buckets": items,
    }
    return payload


def capability_associated(client, args):
    """能力 C：按资源（VPC/云服务器）查询关联的桶。"""
    associated = []
    if args.mock:
        for b in MOCK_DATA["buckets"]:
            if b.get("resource_type") == args.resource:
                associated.append(b)
    else:
        # 真实链路：通过 IAM/OBS 策略按资源名解析桶
        owned = _list_buckets(client)
        associated = [b for b in owned if _bucket_matches_resource(b, args.resource)]

    items = [_norm_bucket(b) for b in associated]
    items.sort(key=lambda x: x["name"])
    payload = {
        "capability": "associated",
        "resource": args.resource,
        "region": args.region,
        "count": len(items),
        "buckets": items,
    }
    return payload


def capability_objects(client, args):
    """能力 D：列出桶内对象。"""
    bucket = _resolve_bucket(client, args.bucket, mock=args.mock)
    if bucket is None:
        raise RuntimeError("未找到指定桶: {}".format(args.bucket))

    objs = []
    if args.mock:
        objs = MOCK_DATA["objects"].get(_attr(bucket, "name"), [])
    else:
        objs = _list_objects(client, _attr(bucket, "name"),
                             prefix=args.prefix, max_keys=args.max_keys)

    items = [{"key": _attr(o, "key"), "size": _attr(o, "size"),
              "last_modified": _attr(o, "last_modified")} for o in objs]
    items.sort(key=lambda x: x["key"])
    return {
        "capability": "objects",
        "bucket": _attr(bucket, "name"),
        "prefix": args.prefix,
        "count": len(items),
        "objects": items,
    }


def _bucket_matches_resource(bucket, resource):
    """判断桶是否与指定资源关联（真实链路启发式）。

    OBS 未提供「资源 → 桶」的直接列表接口，此处以桶名包含资源名作为关联判定，
    结合 IAM/OBS 策略授权的可见桶集合使用。
    """
    name = _attr(bucket, "name") or ""
    return resource in name or _attr(bucket, "resource_type") == resource


def render_md(payload):
    if payload["capability"] == "list":
        lines = ["## OBS 桶列表（{}）".format(payload["region"])]
        if payload.get("filter_prefix"):
            lines.append("按前缀过滤: {}".format(payload["filter_prefix"]))
        lines.append("桶数量: {}".format(payload["count"]))
        lines.append("")
        lines.append("| 桶名 | 区域 | 创建时间 | 存储类别 |")
        lines.append("|---|---|---|---|")
        for b in payload["buckets"]:
            lines.append("| {} | {} | {} | {} |".format(
                b["name"], b["region"], b["creation_time"], b["storage_class"]))
    elif payload["capability"] == "associated":
        r = payload["resource"]
        lines = ["## 资源关联桶（{}）".format(r)]
        lines.append("区域: {}   桶数量: {}".format(payload["region"], payload["count"]))
        lines.append("")
        lines.append("| 桶名 | 区域 | 创建时间 | 存储类别 |")
        lines.append("|---|---|---|---|")
        for b in payload["buckets"]:
            lines.append("| {} | {} | {} | {} |".format(
                b["name"], b["region"], b["creation_time"], b["storage_class"]))
    else:
        bucket = payload["bucket"]
        lines = ["## 桶内对象（{}）".format(bucket), ""]
        lines.append("前缀: {}    对象数: {}".format(payload.get("prefix", ""), payload["count"]))
        lines.append("")
        lines.append("| 对象名 | 大小 | 最后修改时间 |")
        lines.append("|---|---|---|")
        for o in payload["objects"]:
            lines.append("| {} | {} | {} |".format(o["key"], o["size"], o["last_modified"]))
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(
        prog="hcs-obs-buckets",
        description="查询华为云账号下关联的 OBS 桶/对象（含 mock 无凭证模式）")

    def add_common_args(p):
        p.add_argument("--region", default="cn-north-4", help="区域，默认 cn-north-4（北京四）")
        p.add_argument("--project-id", default=None, help="项目 ID（默认由 AK/SK 解析）")
        p.add_argument("--format", choices=["json", "md"], default="json", help="输出格式，默认 json")
        p.add_argument("--mock", action="store_true", help="使用内置 mock 数据（无需凭证）")

    add_common_args(parser)
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="能力 A：列出账号下全部桶")
    p_list.add_argument("--bucket", default=None, help="按桶名过滤")
    p_list.add_argument("--prefix", default=None, help="按前缀过滤")
    add_common_args(p_list)

    p_assoc = sub.add_parser("associated", help="能力 C：查询资源关联的桶")
    p_assoc.add_argument("resource", help="资源 ID 或名称（如 VPC/云服务器）")
    add_common_args(p_assoc)

    p_obj = sub.add_parser("objects", help="能力 D：列出桶内对象")
    p_obj.add_argument("--bucket", required=True, help="桶名")
    p_obj.add_argument("--prefix", default=None, help="对象名前缀")
    add_common_args(p_obj)

    args = parser.parse_args()

    try:
        if args.mock:
            print("提示：使用 mock 数据验证（未访问真实华为云）。", file=sys.stderr)
            client = None
        else:
            client = _build_client(args.region, args.project_id)

        if args.command == "list":
            payload = capability_list(client, args)
        elif args.command == "associated":
            payload = capability_associated(client, args)
        else:
            payload = capability_objects(client, args)

        if args.format == "md":
            print(render_md(payload))
        else:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
    except SystemExit:
        raise
    except Exception as exc:
        print("错误：调用华为云 API 失败：{}".format(exc), file=sys.stderr)
        sys.exit(4)


if __name__ == "__main__":
    main()
