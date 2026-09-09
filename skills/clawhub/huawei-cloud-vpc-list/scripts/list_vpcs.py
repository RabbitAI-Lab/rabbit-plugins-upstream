#!/usr/bin/env python3
"""
huawei-cloud-vpc-list — 查询华为云 VPC 列表（SDK 模式，支持全量分页聚合）

用法:
  python3 scripts/list_vpcs.py --project_id <project_id> [--region cn-north-4] [--limit 100]
  python3 scripts/list_vpcs.py --project_id <project_id> --enterprise_project_id 0

环境变量:
  HUAWEI_ACCESS_KEY / HUAWEI_SECRET_KEY  或  HW_AK / HW_SK 等
"""

import argparse
import json
import os
import sys
import traceback


def load_credentials():
    """动态扫描环境变量获取 AK/SK，不依赖固定变量名。"""
    ak, sk = "", ""
    for k, v in os.environ.items():
        u = k.upper()
        if not (u.startswith("HUAWEI") or u.startswith("HW") or u.startswith("HWC")):
            continue
        if "ACCESS_KEY" in u or u.endswith("_AK") or u == "AK":
            ak = v or ak
        if "SECRET_KEY" in u or u.endswith("_SK") or u == "SK":
            sk = v or sk
    return ak, sk


def build_client(ak, sk, project_id, region, security_token=""):
    """构建 VPC v3 SDK 客户端。"""
    try:
        from huaweicloudsdkcore.auth.credentials import BasicCredentials
        from huaweicloudsdkcore.http.http_config import HttpConfig
        from huaweicloudsdkvpc.v3 import VpcClient
        from huaweicloudsdkvpc.v3.region.vpc_region import VpcRegion
    except ImportError:
        print("错误: 缺少 huaweicloudsdkvpc 包。请执行: pip install huaweicloudsdkvpc", file=sys.stderr)
        sys.exit(4)

    http_config = HttpConfig.get_default_config()
    http_config.ignore_ssl_verification = False
    http_config.timeout = 30

    creds = BasicCredentials(ak, sk, project_id)
    if security_token:
        creds = creds.with_security_token(security_token)

    client = VpcClient.new_builder() \
        .with_http_config(http_config) \
        .with_credentials(creds) \
        .with_region(VpcRegion.value_of(region)) \
        .build()
    return client


def list_vpcs(client, region, marker="", limit=2000, filters=None):
    """执行单次 ListVpcs 查询。"""
    from huaweicloudsdkvpc.v3.model import ListVpcsRequest

    request = ListVpcsRequest()
    request.limit = limit
    if marker:
        request.marker = marker

    if filters:
        if filters.get("id"):
            request.id = filters["id"]
        if filters.get("name"):
            request.name = filters["name"]
        if filters.get("cidr"):
            request.cidr = filters["cidr"]
        if filters.get("description"):
            request.description = filters["description"]
        if filters.get("enterprise_project_id"):
            request.enterprise_project_id = filters["enterprise_project_id"]

    response = client.list_vpcs(request)
    return response


def aggregate_all_vpcs(client, region, filters=None):
    """全量聚合所有分页 VPC，返回 (vpcs_list, total_count)。"""
    all_vpcs = []
    marker = ""
    page_num = 0
    max_pages = 50  # 安全上限，防止死循环

    while page_num < max_pages:
        page_num += 1
        response = list_vpcs(client, region, marker=marker, limit=2000, filters=filters)
        vpcs = response.vpcs
        if not vpcs:
            break

        # 检测重复：如果本页第一条与上页最后一条 id 相同，说明 marker 未生效，终止
        if marker and all_vpcs and getattr(vpcs[0], "id", None) == getattr(all_vpcs[-1], "id", None):
            break

        all_vpcs.extend(vpcs)

        # 获取 next_marker
        page_info = getattr(response, "page_info", None)
        next_marker = getattr(page_info, "next_marker", None) if page_info else ""
        if not next_marker:
            break
        marker = next_marker

    return all_vpcs, len(all_vpcs)


def render_json(vpcs, total_count):
    """输出 JSON 格式结果。"""
    result = {
        "total_count": total_count,
        "vpcs": []
    }
    for v in vpcs:
        result["vpcs"].append({
            "id": getattr(v, "id", ""),
            "name": getattr(v, "name", ""),
            "description": getattr(v, "description", ""),
            "cidr": getattr(v, "cidr", ""),
            "status": getattr(v, "status", ""),
            "enterprise_project_id": getattr(v, "enterprise_project_id", ""),
            "routes": [
                {
                    "destination": getattr(r, "destination", ""),
                    "nexthop": getattr(r, "nexthop", ""),
                }
                for r in (getattr(v, "routes", []) or [])
            ] if hasattr(v, "routes") else [],
            "created_at": getattr(v, "created_at", ""),
            "updated_at": getattr(v, "updated_at", ""),
            "tags": [
                {
                    "key": getattr(t, "key", ""),
                    "value": getattr(t, "value", ""),
                }
                for t in (getattr(v, "tags", []) or [])
            ] if hasattr(v, "tags") else [],
        })
    print(json.dumps(result, indent=2, ensure_ascii=False))


def render_text(vpcs, total_count):
    """输出纯文本表格格式。"""
    if not vpcs:
        print("没有找到 VPC")
        return

    header = (
        f"{'ID':<40} {'名称':<24} {'CIDR':<20} {'状态':<12} "
        f"{'企业项目ID':<20} {'描述':<30}"
    )
    print(header)
    print("-" * len(header))
    for v in vpcs:
        print(
            f"{getattr(v, 'id', ''):<40} "
            f"{getattr(v, 'name', ''):<24} "
            f"{getattr(v, 'cidr', ''):<20} "
            f"{getattr(v, 'status', ''):<12} "
            f"{getattr(v, 'enterprise_project_id', ''):<20} "
            f"{getattr(v, 'description', '')[:28]:<30}"
        )

    print(f"\n共 {total_count} 条 VPC")


def main():
    parser = argparse.ArgumentParser(
        description="查询华为云 VPC 列表（支持全量分页聚合）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "环境变量:\n"
            "  支持 HUAWEI_ACCESS_KEY / HUAWEI_SECRET_KEY, HW_AK / HW_SK 等\n"
            "示例:\n"
            "  python3 scripts/list_vpcs.py --project_id <id> --region cn-north-4\n"
            "  python3 scripts/list_vpcs.py --project_id <id> --enterprise_project_id 0\n"
        ),
    )
    parser.add_argument("--project_id", type=str, required=True, help="华为云项目 ID")
    parser.add_argument("--region", type=str, default="cn-north-4", help="区域（默认 cn-north-4）")
    parser.add_argument("--limit", type=int, default=2000, help="每页最大条数（默认 2000，最大2000）")
    parser.add_argument("--marker", type=str, help="分页标记（从上次响应的 next_marker 获取）")
    parser.add_argument("--id", type=str, nargs="+", dest="filter_id", help="VPC ID 过滤")
    parser.add_argument("--name", type=str, nargs="+", dest="filter_name", help="VPC 名称过滤")
    parser.add_argument("--cidr", type=str, nargs="+", dest="filter_cidr", help="CIDR 过滤")
    parser.add_argument("--description", type=str, nargs="+", dest="filter_description", help="描述过滤")
    parser.add_argument("--enterprise_project_id", type=str, help="企业项目 ID 过滤")
    parser.add_argument("--output", type=str, choices=["json", "text"], default="json", help="输出格式（默认 json）")
    args = parser.parse_args()

    # 加载凭据
    ak, sk = load_credentials()
    if not ak or not sk:
        print(
            "错误: 未找到华为云 AK/SK 环境变量。请设置 HUAWEI_ACCESS_KEY / HUAWEI_SECRET_KEY 等。",
            file=sys.stderr,
        )
        sys.exit(3)

    # 构建客户端
    security_token = ""
    for k, v in os.environ.items():
        u = k.upper()
        if "SECURITY_TOKEN" in u or u.endswith("_ST") or u == "SECURITY_TOKEN":
            security_token = v or security_token

    client = build_client(ak, sk, args.project_id, args.region, security_token)
    if not client:
        sys.exit(1)

    # 构建过滤器
    filters = {}
    if args.filter_id:
        filters["id"] = args.filter_id
    if args.filter_name:
        filters["name"] = args.filter_name
    if args.filter_cidr:
        filters["cidr"] = args.filter_cidr
    if args.filter_description:
        filters["description"] = args.filter_description
    if args.enterprise_project_id:
        filters["enterprise_project_id"] = args.enterprise_project_id

    try:
        # 全量分页聚合
        vpcs, total_count = aggregate_all_vpcs(client, args.region, filters=filters)

        if not vpcs:
            print(f"没有找到 VPC（区域: {args.region}）")
            sys.exit(0)

        # 如果有 marker 参数，在聚合结果中做本地分页
        if args.marker:
            start_idx = 0
            for i, v in enumerate(vpcs):
                if getattr(v, "id", "") == args.marker:
                    start_idx = i + 1
                    break
            vpcs = vpcs[start_idx:]

        # 按 limit 截取
        display_vpcs = vpcs[:args.limit] if args.limit else vpcs

        if args.output == "json":
            render_json(display_vpcs, total_count)
        else:
            render_text(display_vpcs, total_count)

    except Exception as e:
        print(f"错误: VPC 列表查询失败 — {e}", file=sys.stderr)
        if os.environ.get("DEBUG"):
            traceback.print_exc(file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()