#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""查询华为云 ECS 云服务器实例列表。

能力:
  A. 列出账号下（region/project 范围）全部 ECS 实例，可选按名称/状态/可用区过滤。
  B. 按实例名称模糊匹配查询。
  C. 按实例状态过滤（ACTIVE / SHUTOFF / ERROR 等）。

认证:
  读取环境变量 HWCLOUD_AK / HWCLOUD_SK（真实验证必填，不硬编码密钥）。
  可选 HWCLOUD_PROJECT_ID（缺省由 AK/SK 解析默认项目）。

用法:
  python3 hcs-ecs-servers.py list [--region cn-north-4] [--project-id <id>]
                                   [--name <名称>] [--status <状态>]
                                   [--format json|md] [--mock]
  python3 hcs-ecs-servers.py list --mock --region cn-north-4 --format json

退出码: 0=成功; 2=参数错误; 3=缺少认证(未设置 HWCLOUD_AK/HWCLOUD_SK); 4=API 调用失败
"""

import argparse
import json
import os
import sys


MOCK_DATA = {
    "servers": [
        {"id": "i-0aaa1111bbbb2222cccc", "name": "web-server-01",
         "status": "ACTIVE", "os_ext_a_zavailability_zone": "cn-north-4a",
         "flavor": {"id": "s6.large.2", "name": "s6.large.2", "vcpus": "2", "ram": "4096", "disk": "0"},
         "addresses": {"vpc-prod": [
             {"addr": "192.168.1.10", "version": "4", "type": "fixed"},
             {"addr": "100.64.1.10", "version": "4", "type": "floating"},
         ]},
         "created": "2024-01-15T08:30:00Z", "updated": "2024-06-01T12:00:00Z"},
        {"id": "i-3333444455556666aaaa", "name": "db-server-01",
         "status": "ACTIVE", "os_ext_a_zavailability_zone": "cn-north-4b",
         "flavor": {"id": "s6.xlarge.4", "name": "s6.xlarge.4", "vcpus": "4", "ram": "16384", "disk": "0"},
         "addresses": {"vpc-prod": [
             {"addr": "192.168.1.20", "version": "4", "type": "fixed"},
         ]},
         "created": "2024-02-20T10:00:00Z", "updated": "2024-06-02T15:30:00Z"},
        {"id": "i-7777888899990000bbbb", "name": "test-server-01",
         "status": "SHUTOFF", "os_ext_a_zavailability_zone": "cn-north-4a",
         "flavor": {"id": "s6.medium.2", "name": "s6.medium.2", "vcpus": "1", "ram": "2048", "disk": "0"},
         "addresses": {"vpc-dev": [
             {"addr": "192.168.2.30", "version": "4", "type": "fixed"},
         ]},
         "created": "2024-03-10T14:20:00Z", "updated": "2024-05-15T09:00:00Z"},
    ],
}


def _attr(obj, name, default=None):
    """兼容 SDK 对象（属性访问）与普通 dict。"""
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _norm_addresses(addresses):
    """将 addresses（dict 或 SDK 对象）标准化为 IP 列表。

    华为云 ECS addresses 结构: {network_name: [{addr, version, OS-EXT-IPS:type}, ...]}
    输出: [{addr, version, type}, ...]
    """
    if not addresses:
        return []
    if isinstance(addresses, dict):
        result = []
        for _net, addrs in addresses.items():
            if not addrs:
                continue
            for a in addrs:
                if isinstance(a, dict):
                    result.append({
                        "addr": a.get("addr"),
                        "version": a.get("version"),
                        "type": a.get("type") or a.get("OS-EXT-IPS:type"),
                    })
                else:
                    result.append({
                        "addr": _attr(a, "addr"),
                        "version": _attr(a, "version"),
                        "type": _attr(a, "os_ext_ip_stype"),
                    })
        return result
    # SDK 对象: dict-like with values
    result = []
    try:
        for _net, addrs in addresses.items():
            if not addrs:
                continue
            for a in addrs:
                result.append({
                    "addr": _attr(a, "addr"),
                    "version": _attr(a, "version"),
                    "type": _attr(a, "os_ext_ip_stype"),
                })
    except Exception:
        pass
    return result


def _norm_flavor(flavor):
    """将 flavor（dict 或 SDK ServerFlavor 对象）标准化。"""
    if not flavor:
        return {"id": None, "name": None, "vcpus": None, "ram": None, "disk": None}
    return {
        "id": _attr(flavor, "id"),
        "name": _attr(flavor, "name"),
        "vcpus": _attr(flavor, "vcpus"),
        "ram": _attr(flavor, "ram"),
        "disk": _attr(flavor, "disk"),
    }


def _norm_server(s):
    """将 ServerDetail（dict 或 SDK 对象）标准化为输出 dict。"""
    return {
        "id": _attr(s, "id"),
        "name": _attr(s, "name"),
        "status": _attr(s, "status"),
        "availability_zone": _attr(s, "os_ext_a_zavailability_zone"),
        "flavor": _norm_flavor(_attr(s, "flavor")),
        "addresses": _norm_addresses(_attr(s, "addresses")),
        "created": _attr(s, "created"),
        "updated": _attr(s, "updated"),
    }


def _build_client(region_id, project_id):
    from huaweicloudsdkcore.auth.credentials import BasicCredentials
    from huaweicloudsdkcore.region.region import Region
    from huaweicloudsdkecs.v2 import EcsClient

    ak = os.environ.get("HWCLOUD_AK")
    sk = os.environ.get("HWCLOUD_SK")
    if not ak or not sk:
        print("错误：缺少认证，请设置环境变量 HWCLOUD_AK / HWCLOUD_SK", file=sys.stderr)
        sys.exit(3)
    creds = BasicCredentials(ak, sk)
    if project_id:
        creds = creds.with_project_id(project_id)
    region = Region(region_id, "https://ecs.{}.myhuaweicloud.com".format(region_id))
    return EcsClient.new_builder().with_credentials(creds).with_region(region).build()


def _fetch_servers(client, name=None, status=None):
    """分页拉取账号下（region/project 范围）全部 ECS 实例。"""
    from huaweicloudsdkecs.v2 import ListServersDetailsRequest

    servers, marker = [], None
    while True:
        req = ListServersDetailsRequest(limit=1000)
        if name:
            req.name = name
        if status:
            req.status = status
        if marker:
            req.marker = marker
        resp = client.list_servers_details(req)
        items = _attr(resp, "servers", []) or []
        servers.extend(items)
        if len(items) < 1000:
            break
        last = items[-1] if items else None
        marker = _attr(last, "id") if last else None
        if not marker:
            break
    return servers


def capability_list(client, args):
    """能力 A：列出 ECS 实例（可按名称/状态过滤）。"""
    if args.mock:
        servers = MOCK_DATA["servers"]
        if args.name:
            servers = [s for s in servers if args.name in (_attr(s, "name") or "")]
        if args.status:
            servers = [s for s in servers if _attr(s, "status") == args.status]
    else:
        servers = _fetch_servers(client, name=args.name, status=args.status)

    items = [_norm_server(s) for s in servers]
    items.sort(key=lambda x: (x["name"] or "", x["id"] or ""))
    payload = {
        "capability": "list",
        "region": args.region,
        "project_id": args.project_id,
        "filter_name": args.name,
        "filter_status": args.status,
        "count": len(items),
        "servers": items,
    }
    return payload


def render_md(payload):
    lines = ["## ECS 实例列表（区域: {}）".format(payload["region"])]
    if payload.get("filter_name"):
        lines.append("按名称过滤: {}".format(payload["filter_name"]))
    if payload.get("filter_status"):
        lines.append("按状态过滤: {}".format(payload["filter_status"]))
    lines.append("实例数量: {}".format(payload["count"]))
    lines.append("")
    lines.append("| 实例名称 | 实例ID | 状态 | 可用区 | 实例类型 | IP地址 |")
    lines.append("|---|---|---|---|---|---|")
    for s in payload["servers"]:
        addrs = ", ".join(
            "{}({})".format(a["addr"], a["type"] or "fixed")
            for a in s["addresses"] if a.get("addr")
        )
        flavor_name = (s["flavor"] or {}).get("name") or ""
        lines.append("| {} | {} | {} | {} | {} | {} |".format(
            s["name"], s["id"], s["status"], s["availability_zone"], flavor_name, addrs))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        prog="hcs-ecs-servers",
        description="查询华为云 ECS 云服务器实例列表（含 mock 无凭证模式）")

    def add_common_args(p):
        p.add_argument("--region", default="cn-north-4", help="区域，默认 cn-north-4（北京四）")
        p.add_argument("--project-id", default=None, help="项目 ID（默认由 AK/SK 解析）")
        p.add_argument("--format", choices=["json", "md"], default="json", help="输出格式，默认 json")
        p.add_argument("--mock", action="store_true", help="使用内置 mock 数据（无需凭证）")

    add_common_args(parser)
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="列出账号下全部 ECS 实例")
    p_list.add_argument("--name", default=None, help="按实例名称模糊过滤")
    p_list.add_argument("--status", default=None,
                        help="按状态过滤（ACTIVE/SHUTOFF/ERROR 等）")
    add_common_args(p_list)

    args = parser.parse_args()

    try:
        if args.mock:
            print("提示：使用 mock 数据验证（未访问真实华为云）。", file=sys.stderr)
            client = None
        else:
            client = _build_client(args.region, args.project_id)

        if args.command == "list":
            payload = capability_list(client, args)
        else:
            parser.error("未知命令: {}".format(args.command))

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
