#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hcs-ecs-servers — 查询华为云 ECS（弹性云服务器）实例列表。

能力:
  A. list-servers — 查询 ECS 实例列表（名称/ID/状态/IP/规格）
  B. capability-list — 列出本 skill 所有能力项

认证: AK/SK 签名（SDK-HMAC-SHA256），通过环境变量或 .project-info/ JSON 配置解析
退出码: 0=成功; 2=参数错误; 3=缺少配置（AK/SK）; 4=API 调用失败
"""

import argparse
import json
import os
import sys


# ---------------------------------------------------------------------------
# Credentials（动态扫描，不依赖固定环境变量名）
# ---------------------------------------------------------------------------

def _load_credentials():
    """动态扫描环境变量和项目知识获取 AK/SK，不依赖固定变量名。

    优先级:
    1. 项目知识 — 递归扫描 .project-info/ 下所有 JSON 文件（secrets.HUAWEI_AK / secrets.HUAWEI_SK）
    2. 环境变量 — 扫描 HUAWEI/HW/HWC 开头 + 含 ACCESS_KEY/_AK/SECRET_KEY/_SK 的变量
    """
    ak, sk = '', ''

    # 1. 项目知识优先
    ak, sk = _load_from_project_knowledge(ak, sk)

    # 2. 环境变量回退：项目知识缺失时从环境变量补充
    for k, v in os.environ.items():
        u = k.upper()
        if not (u.startswith('HUAWEI') or u.startswith('HW') or u.startswith('HWC')):
            continue
        if 'ACCESS_KEY' in u or u.endswith('_AK') or u == 'AK':
            ak = v or ak
        if 'SECRET_KEY' in u or u.endswith('_SK') or u == 'SK':
            sk = v or sk

    return ak, sk


def _load_from_project_knowledge(ak, sk):
    """从 .project-info/ 目录递归查找 JSON 配置文件，读取 secrets.HUAWEI_AK / secrets.HUAWEI_SK。"""
    import glob
    for pattern in ['.project-info/**/*.json',
                    '../.project-info/**/*.json',
                    '../../.project-info/**/*.json']:
        for filepath in glob.glob(pattern, recursive=True):
            try:
                with open(filepath) as f:
                    data = json.load(f)
                secrets = data.get('secrets', {})
                for key, val in secrets.items():
                    u = key.upper()
                    if 'ACCESS_KEY' in u or u.endswith('_AK') or u == 'AK':
                        if val:
                            ak = val or ak
                    if 'SECRET_KEY' in u or u.endswith('_SK') or u == 'SK':
                        if val:
                            sk = val or sk
            except Exception:
                continue
    return ak, sk


def _require_credentials():
    """获取 AK/SK，缺失时退出码 3。"""
    ak, sk = _load_credentials()
    if not ak or not sk:
        missing = []
        if not ak:
            missing.append('AK')
        if not sk:
            missing.append('SK')
        print("错误：缺少华为云凭据（%s）。请通过环境变量（HUAWEI_AK/HUAWEI_SK）"
              "或 .project-info/ JSON 配置文件设置。" % '/'.join(missing), file=sys.stderr)
        sys.exit(3)
    return ak, sk


# ---------------------------------------------------------------------------
# Huawei Cloud API client（AK/SK 签名 + requests 调用）
# ---------------------------------------------------------------------------

_DEFAULT_REGION = 'cn-north-4'


def _get_project_id(ak, sk, region):
    """通过 IAM API 获取指定区域的 project_id。

    GET /v3/projects?name={region}
    签名方式: SDK-HMAC-SHA256
    """
    try:
        from huaweicloudsdkcore.auth.credentials import BasicCredentials
        from huaweicloudsdkcore.signer.signer import Signer
        from huaweicloudsdkcore.sdk_request import SdkRequest
    except ImportError:
        print("错误：缺少 huaweicloudsdkcore 库，请安装: pip install huaweicloudsdkcore",
              file=sys.stderr)
        sys.exit(3)

    import requests

    credentials = BasicCredentials(ak=ak, sk=sk)
    signer = Signer(credentials)

    host = 'iam.myhuaweicloud.com'
    resource_path = '/v3/projects'
    query_params = [('name', region)]

    sdk_req = SdkRequest(
        method='GET',
        schema='https',
        host=host,
        resource_path=resource_path,
        uri=resource_path,
        query_params=query_params,
        header_params={'Content-Type': 'application/json'},
        body='',
    )
    signer.sign(sdk_req)

    url = 'https://%s%s' % (host, sdk_req.uri)
    resp = None
    try:
        resp = requests.get(url, headers=sdk_req.header_params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        projects = data.get('projects', [])
        if projects:
            return projects[0].get('id')
        print("错误：无法获取区域 %s 的 project_id（IAM 返回空列表）" % region, file=sys.stderr)
        sys.exit(4)
    except requests.exceptions.HTTPError as e:
        status = resp.status_code if resp is not None else 'N/A'
        print("错误：IAM API 调用失败 %s: %s" % (status, e), file=sys.stderr)
        sys.exit(4)
    except requests.exceptions.RequestException as e:
        print("错误：网络请求失败: %s" % e, file=sys.stderr)
        sys.exit(4)
    except ValueError:
        print("错误：IAM API 返回非 JSON 格式", file=sys.stderr)
        sys.exit(4)


def _ecs_api_request(ak, sk, region, query_params):
    """调用华为云 ECS API 查询实例列表。

    GET /v1/{project_id}/cloudservers/detail
    签名方式: SDK-HMAC-SHA256
    """
    try:
        from huaweicloudsdkcore.auth.credentials import BasicCredentials
        from huaweicloudsdkcore.signer.signer import Signer
        from huaweicloudsdkcore.sdk_request import SdkRequest
    except ImportError:
        print("错误：缺少 huaweicloudsdkcore 库，请安装: pip install huaweicloudsdkcore",
              file=sys.stderr)
        sys.exit(3)

    import requests

    project_id = _get_project_id(ak, sk, region)

    credentials = BasicCredentials(ak=ak, sk=sk)
    signer = Signer(credentials)

    host = 'ecs.%s.myhuaweicloud.com' % region
    resource_path = '/v1/%s/cloudservers/detail' % project_id

    sdk_req = SdkRequest(
        method='GET',
        schema='https',
        host=host,
        resource_path=resource_path,
        uri=resource_path,
        query_params=query_params,
        header_params={'Content-Type': 'application/json'},
        body='',
    )
    signer.sign(sdk_req)

    url = 'https://%s%s' % (host, sdk_req.uri)
    resp = None
    try:
        resp = requests.get(url, headers=sdk_req.header_params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.HTTPError as e:
        status = resp.status_code if resp is not None else 'N/A'
        print("错误：ECS API 调用失败 %s: %s" % (status, e), file=sys.stderr)
        sys.exit(4)
    except requests.exceptions.RequestException as e:
        print("错误：网络请求失败: %s" % e, file=sys.stderr)
        sys.exit(4)
    except ValueError:
        print("错误：ECS API 返回非 JSON 格式", file=sys.stderr)
        sys.exit(4)


# ---------------------------------------------------------------------------
# Subcommand implementations
# ---------------------------------------------------------------------------

def _extract_server_info(server):
    """从 API 返回的 server 对象中提取关键字段。"""
    name = server.get('name', '')
    sid = server.get('id', '')
    status = server.get('status', '')
    created = server.get('created', '')

    # Flavor
    flavor = server.get('flavor', {})
    flavor_id = flavor.get('id', '') if isinstance(flavor, dict) else ''

    # Addresses — extract private and public IPs
    private_ip = ''
    public_ip = ''
    addresses = server.get('addresses', {})
    if isinstance(addresses, dict):
        for net_name, addr_list in addresses.items():
            if not isinstance(addr_list, list):
                continue
            for addr in addr_list:
                if not isinstance(addr, dict):
                    continue
                ip_addr = addr.get('addr', '')
                ip_type = addr.get('OS-EXT-IPS:type', '')
                version = addr.get('version', 4)
                if version == 4 and ip_addr:
                    if ip_type == 'fixed' or ip_type == 'private' or not ip_type:
                        if not private_ip:
                            private_ip = ip_addr
                    elif ip_type == 'floating' or ip_type == 'public':
                        if not public_ip:
                            public_ip = ip_addr

    # Availability zone
    az = ''
    os_az = server.get('OS-EXT-AZ:availability_zone', '')
    if os_az:
        az = os_az

    return {
        'name': name,
        'id': sid,
        'status': status,
        'flavor': flavor_id,
        'private_ip': private_ip,
        'public_ip': public_ip,
        'availability_zone': az,
        'created': created,
    }


def cmd_list_servers(args):
    """能力 A：查询 ECS 实例列表。"""
    ak, sk = _require_credentials()
    region = args.region or _DEFAULT_REGION

    query_params = []
    if args.limit is not None:
        query_params.append(('limit', str(args.limit)))
    if args.offset is not None:
        query_params.append(('offset', str(args.offset)))
    if args.status:
        query_params.append(('status', args.status))

    data = _ecs_api_request(ak, sk, region, query_params)

    count = data.get('count', 0)
    raw_servers = data.get('servers', [])
    servers = [_extract_server_info(s) for s in raw_servers]

    result = {
        'count': count,
        'region': region,
        'servers': servers,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        _print_table(result)

    return result


def _print_table(result):
    """以表格格式输出 ECS 实例列表。"""
    count = result.get('count', 0)
    region = result.get('region', '')
    servers = result.get('servers', [])

    print("区域: %s  |  实例总数: %d" % (region, count))
    print()

    if not servers:
        print("（该区域无 ECS 实例）")
        return

    # Table header
    header = "%-20s %-36s %-10s %-16s %-18s %-16s" % (
        "实例名称", "实例ID", "状态", "规格", "私有IP", "公网IP")
    print(header)
    print("-" * len(header))

    for s in servers:
        name = s['name'][:20] if s['name'] else ''
        sid = s['id'][:36] if s['id'] else ''
        status = s['status'][:10] if s['status'] else ''
        flavor = s['flavor'][:16] if s['flavor'] else ''
        priv = s['private_ip'][:18] if s['private_ip'] else '-'
        pub = s['public_ip'][:16] if s['public_ip'] else '-'
        print("%-20s %-36s %-10s %-16s %-18s %-16s" % (name, sid, status, flavor, priv, pub))


# ---------------------------------------------------------------------------
# Capability list
# ---------------------------------------------------------------------------

def cmd_capability_list(args):
    """能力 B：列出本 skill 所有能力项。"""
    result = {
        'capability': 'capability-list',
        'skill': 'hcs-ecs-servers',
        'version': '0.1.0',
        'auth_type': 'ak_sk',
        'capabilities': [
            {'name': 'list-servers', 'description': '查询华为云 ECS 实例列表',
             'command': 'list-servers [--region REGION] [--status STATUS] [--limit N] [--offset N] [--json]'},
            {'name': 'capability-list', 'description': '列出本 skill 所有能力项',
             'command': 'capability-list'},
        ],
    }
    return result


# ---------------------------------------------------------------------------
# Main entry
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog='hcs-ecs-servers',
        description='查询华为云 ECS（弹性云服务器）实例列表')

    sub = parser.add_subparsers(dest='command', help='能力命令')

    # === list-servers ===
    p_ls = sub.add_parser('list-servers', help='查询 ECS 实例列表')
    p_ls.add_argument('--region', default=None,
                      help='华为云区域（默认 cn-north-4）')
    p_ls.add_argument('--status', default=None,
                      help='实例状态筛选（ACTIVE/SHUTOFF/ERROR/BUILD/REBOOT 等）')
    p_ls.add_argument('--limit', type=int, default=None,
                      help='每页最大返回数（API 默认 25，最大 1000）')
    p_ls.add_argument('--offset', type=int, default=None,
                      help='页码偏移（从 1 开始）')
    p_ls.add_argument('--json', action='store_true',
                      help='输出 JSON 格式（默认表格格式）')

    # === capability-list ===
    p_cl = sub.add_parser('capability-list', help='列出本 skill 所有能力项')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(2)

    dispatch = {
        'list-servers': cmd_list_servers,
        'capability-list': cmd_capability_list,
    }

    handler = dispatch.get(args.command)
    if handler is None:
        print("错误：未知命令 %s" % args.command, file=sys.stderr)
        sys.exit(2)

    try:
        if args.command == 'capability-list':
            payload = handler(args)
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            handler(args)
    except SystemExit:
        raise
    except Exception as exc:
        print("错误：%s" % exc, file=sys.stderr)
        sys.exit(4)


if __name__ == '__main__':
    main()
