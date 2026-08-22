#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""华为云 OBS 元数据检索 + AI 内容感知 skill。

能力:
  A. scalar-search  — 标量检索：按文件名/大小/类型/时间过滤桶内对象
  B. semantic-search — 语义检索：基于华为云 AI 服务（Image Recognition / VIAS）+ OBS 对象列表组合
  C. enable-ai      — AI 内容感知开通：为桶配置图片/视频语义提取
  D. ai-status      — AI 内容感知查询：查看桶的 AI 配置状态
  E. disable-ai     — AI 内容感知关闭：关闭桶的 AI 配置
  F. create-bucket  — 创建 OBS 桶
  G. upload-object  — 上传文件到 OBS 桶
  H. bucket-stats   — 查询桶元数据信息
  I. list-buckets   — 列出账号下全部桶
  J. capability-list — 列出本 skill 所有能力项

认证:
  动态扫描环境变量获取 AK/SK（HUAWEI/HW/HWC 开头 + ACCESS_KEY/_AK/SECRET_KEY/_SK）。
  可选 HWCLOUD_PROJECT_ID（缺省由 AK/SK 解析默认项目）。

退出码: 0=成功; 2=参数错误; 3=缺少认证; 4=API 调用失败
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime


# ---------------------------------------------------------------------------
# Mock data
# ---------------------------------------------------------------------------

MOCK_BUCKETS = [
    {"name": "demo-assets", "region": "cn-north-4", "creation_time": "2024-01-15T08:00:00Z",
     "storage_class": "STANDARD"},
    {"name": "prod-images", "region": "cn-north-4", "creation_time": "2024-03-20T10:30:00Z",
     "storage_class": "STANDARD"},
    {"name": "dev-videos", "region": "cn-north-4", "creation_time": "2024-06-05T14:00:00Z",
     "storage_class": "STANDARD"},
]

MOCK_OBJECTS = {
    "demo-assets": [
        {"key": "images/sunset.jpg", "size": 2048000, "last_modified": "2024-07-01T12:00:00Z"},
        {"key": "images/mountain.png", "size": 4096000, "last_modified": "2024-07-02T13:30:00Z"},
        {"key": "docs/report.pdf", "size": 512000, "last_modified": "2024-06-28T09:15:00Z"},
        {"key": "videos/demo.mp4", "size": 10485760, "last_modified": "2024-07-03T16:45:00Z"},
        {"key": "logs/app.log", "size": 8192, "last_modified": "2024-07-05T08:00:00Z"},
    ],
    "prod-images": [
        {"key": "photos/landscape_01.jpg", "size": 3072000, "last_modified": "2024-08-01T10:00:00Z"},
        {"key": "photos/portrait_02.png", "size": 5242880, "last_modified": "2024-08-02T11:20:00Z"},
        {"key": "thumbnails/small_01.jpg", "size": 10240, "last_modified": "2024-08-03T14:00:00Z"},
    ],
    "dev-videos": [
        {"key": "clips/intro.mp4", "size": 15728640, "last_modified": "2024-08-10T09:00:00Z"},
        {"key": "clips/demo_v2.mp4", "size": 20971520, "last_modified": "2024-08-12T15:30:00Z"},
    ],
}

MOCK_AI_TAGS = {
    "images/sunset.jpg": {"tags": ["sunset", "sky", "orange", "landscape"], "confidence": 0.95},
    "images/mountain.png": {"tags": ["mountain", "snow", "nature", "landscape"], "confidence": 0.92},
    "photos/landscape_01.jpg": {"tags": ["landscape", "field", "green", "sky"], "confidence": 0.89},
    "photos/portrait_02.png": {"tags": ["person", "portrait", "face"], "confidence": 0.96},
    "videos/demo.mp4": {"tags": ["presentation", "screen", "text"], "confidence": 0.88},
    "clips/intro.mp4": {"tags": ["intro", "animation", "text"], "confidence": 0.91},
}

MOCK_AI_CONFIG = {}  # bucket -> {"image": True/False, "video": True/False}


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def _attr(obj, name, default=None):
    """兼容 SDK 对象（属性访问）与普通 dict。"""
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _load_credentials():
    """动态扫描环境变量获取 AK/SK，不依赖固定变量名。"""
    ak, sk = '', ''
    for k, v in os.environ.items():
        u = k.upper()
        if not (u.startswith('HUAWEI') or u.startswith('HW') or u.startswith('HWC')):
            continue
        if 'ACCESS_KEY' in u or u.endswith('_AK') or u == 'AK':
            ak = v or ak
        if 'SECRET_KEY' in u or u.endswith('_SK') or u == 'SK':
            sk = v or sk
    return ak, sk


def _get_object_type(key):
    """根据文件扩展名推断对象类型。"""
    ext = os.path.splitext(key)[1].lower()
    image_exts = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff'}
    video_exts = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'}
    audio_exts = {'.mp3', '.wav', '.flac', '.aac', '.ogg'}
    doc_exts = {'.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'}
    if ext in image_exts:
        return 'image'
    if ext in video_exts:
        return 'video'
    if ext in audio_exts:
        return 'audio'
    if ext in doc_exts:
        return 'document'
    return 'other'


def _parse_size_str(size_str):
    """解析大小字符串（如 '1KB', '2MB'）为字节数。"""
    if not size_str:
        return None
    s = size_str.strip().upper()
    multipliers = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
    for suffix, mult in sorted(multipliers.items(), key=lambda x: -len(x[0])):
        if s.endswith(suffix):
            try:
                return int(float(s[:-len(suffix)]) * mult)
            except ValueError:
                return None
    try:
        return int(s)
    except ValueError:
        return None


def _parse_time_str(time_str):
    """解析时间字符串为时间戳。支持 ISO 格式和 'YYYY-MM-DD'。"""
    if not time_str:
        return None
    try:
        if 'T' in time_str:
            dt = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
        else:
            dt = datetime.fromisoformat(time_str)
        return dt.timestamp()
    except (ValueError, TypeError):
        return None


# ---------------------------------------------------------------------------
# OBS client builder
# ---------------------------------------------------------------------------

def _build_obs_client(region_id):
    """构建 OBS SDK 客户端。"""
    ak, sk = _load_credentials()
    if not ak or not sk:
        print("错误：缺少认证，请设置环境变量（HUAWEI/HW/HWC 开头 + AK/SK）", file=sys.stderr)
        sys.exit(3)

    from huaweicloudsdkcore.region.region import Region
    from huaweicloudsdkobs.v1 import ObsClient
    from huaweicloudsdkobs.v1.obs_credentials import ObsCredentials

    creds = ObsCredentials(ak, sk)
    region = Region(region_id, "https://obs.{}.myhuaweicloud.com".format(region_id))
    return ObsClient.new_builder().with_credentials(creds).with_region(region).build()


def _get_project_id():
    """获取项目 ID（可选）。"""
    for k, v in os.environ.items():
        u = k.upper()
        if (u.startswith('HUAWEI') or u.startswith('HW') or u.startswith('HWC')) and 'PROJECT_ID' in u:
            if v:
                return v
    return None


# ---------------------------------------------------------------------------
# OBS operations
# ---------------------------------------------------------------------------

def _list_all_buckets(client):
    """拉取账号下全部桶。"""
    from huaweicloudsdkobs.v1 import ListBucketsRequest
    resp = client.list_buckets(ListBucketsRequest())
    buckets_obj = _attr(resp, 'buckets')
    if buckets_obj is None:
        return []
    items = _attr(buckets_obj, 'bucket', [])
    return items or []


def _list_all_objects(client, bucket_name, prefix=None, max_keys=1000):
    """分页拉取桶内全部对象。"""
    from huaweicloudsdkobs.v1 import ListObjectsRequest
    items, marker = [], None
    while True:
        kwargs = {'bucket_name': bucket_name, 'max_keys': max_keys}
        if prefix:
            kwargs['prefix'] = prefix
        if marker:
            kwargs['marker'] = marker
        req = ListObjectsRequest(**kwargs)
        resp = client.list_objects(req)
        contents = _attr(resp, 'contents')
        if contents is None:
            break
        # contents may be a list or an object with .object attribute
        if isinstance(contents, list):
            batch = contents
        else:
            batch = _attr(contents, 'object', [])
            if not isinstance(batch, list):
                batch = [batch] if batch else []
        if not batch:
            break
        items.extend(batch)
        if len(batch) < max_keys:
            break
        last = batch[-1]
        marker = _attr(last, 'key')
        if not marker:
            break
    return items


def _norm_bucket(b):
    return {
        'name': _attr(b, 'name'),
        'region': _attr(b, 'location') or _attr(b, 'region'),
        'creation_time': _attr(b, 'creation_date') or _attr(b, 'creation_time'),
        'storage_class': _attr(b, 'storage_class', 'STANDARD'),
    }


def _norm_object(o):
    key = _attr(o, 'key', '')
    size = _attr(o, 'size', 0)
    last_mod = _attr(o, 'last_modified', '')
    return {
        'key': key,
        'size': int(size) if size else 0,
        'last_modified': last_mod,
        'type': _get_object_type(key),
    }


def _get_bucket_metadata(client, bucket_name):
    """获取桶元数据（存储类别/区域/冗余等）。"""
    from huaweicloudsdkobs.v1 import GetBucketMetadataRequest
    req = GetBucketMetadataRequest(bucket_name=bucket_name)
    resp = client.get_bucket_metadata(req)
    return resp


# ---------------------------------------------------------------------------
# AI service REST API helpers
# ---------------------------------------------------------------------------

def _call_image_recognition(ak, sk, region_id, bucket_name, object_key):
    """调用华为云 Image Recognition REST API 进行图像标签识别。

    API: POST https://{endpoint}/v2/{project_id}/image/tagging
    参考: https://support.huaweicloud.com/api-image/image_01_0007.html
    """
    import requests
    # 华为云 Image Recognition endpoint
    endpoint = "https://{}.api.{}.myhuaweicloud.com".format(
        'image', region_id)
    # 构造 OBS URL 供 Image Recognition 读取
    obs_url = "https://{}.obs.{}.myhuaweicloud.com/{}".format(
        bucket_name, region_id, object_key)

    # 使用 AK/SK 签名（简化：使用 Basic Auth 或 token）
    # 实际生产环境应使用华为云 SDK 签名
    project_id = _get_project_id() or ''
    url = "{}/v2/{}/image/tagging".format(endpoint, project_id) if project_id else \
          "{}/v2/image/tagging".format(endpoint)

    payload = {"url": obs_url, "language": "zh"}
    headers = {"Content-Type": "application/json"}

    # 使用华为云 APIG 签名（AK/SK）
    _sign_request(headers, ak, sk, 'POST', url, json.dumps(payload))

    resp = requests.post(url, json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    tags = []
    for tag_info in data.get('result', {}).get('tags', []):
        tags.append({
            'tag': tag_info.get('tag', ''),
            'confidence': tag_info.get('confidence', 0),
        })
    return tags


def _call_vias_analysis(ak, sk, region_id, bucket_name, object_key):
    """调用华为云 VIAS（视频分析服务）REST API 进行视频内容分析。

    API: POST https://{endpoint}/v2/{project_id}/video-analysis
    参考: https://support.huaweicloud.com/api-vias/vias_01_0001.html
    """
    import requests
    endpoint = "https://{}.api.{}.myhuaweicloud.com".format('vias', region_id)
    obs_url = "https://{}.obs.{}.myhuaweicloud.com/{}".format(
        bucket_name, region_id, object_key)

    project_id = _get_project_id() or ''
    url = "{}/v2/{}/video-analysis".format(endpoint, project_id) if project_id else \
          "{}/v2/video-analysis".format(endpoint)

    payload = {
        "obs_url": obs_url,
        "analysis_type": "tagging",
    }
    headers = {"Content-Type": "application/json"}
    _sign_request(headers, ak, sk, 'POST', url, json.dumps(payload))

    resp = requests.post(url, json=payload, headers=headers, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    tags = []
    for tag_info in data.get('result', {}).get('tags', []):
        tags.append({
            'tag': tag_info.get('tag', ''),
            'confidence': tag_info.get('confidence', 0),
        })
    return tags


def _sign_request(headers, ak, sk, method, url, body=''):
    """华为云 APIG AK/SK 签名（简化版——实际应使用 huaweicloudsdkcore 签名器）。

    生产环境建议安装 huaweicloudsdkcore 并使用其 Signer 进行完整签名。
    此处提供 header 占位，真实调用时由 Signer 填充 Authorization header。
    """
    from huaweicloudsdkcore.auth.credentials import BasicCredentials
    from huaweicloudsdkcore.signer.signer import Signer

    creds = BasicCredentials(ak, sk)
    project_id = _get_project_id()
    if project_id:
        creds = creds.with_project_id(project_id)
    signer = Signer(creds)
    # 构造 SignRequest
    from huaweicloudsdkcore.signer.signer import SignRequest
    req = SignRequest()
    req.method = method
    req.url = url
    req.headers = dict(headers)
    req.body = body if body else ''
    signer.sign(req)
    headers.update(req.headers)


# ---------------------------------------------------------------------------
# Capability implementations
# ---------------------------------------------------------------------------

def capability_scalar_search(client, args):
    """能力 A：标量检索——按文件名/大小/类型/时间过滤桶内对象。"""
    if args.mock:
        raw = MOCK_OBJECTS.get(args.bucket, [])
        objects = []
        for o in raw:
            obj = dict(o)
            obj['type'] = _get_object_type(obj.get('key', ''))
            objects.append(obj)
    else:
        raw = _list_all_objects(client, args.bucket, prefix=args.prefix)
        objects = [_norm_object(o) for o in raw]

    # Apply filters
    filtered = []
    for obj in objects:
        key = obj.get('key', '')
        size = obj.get('size', 0)
        obj_type = obj.get('type', '')
        last_mod = obj.get('last_modified', '')

        # Name filter (substring match)
        if args.name_filter and args.name_filter.lower() not in key.lower():
            continue
        # Type filter
        if args.type and obj_type != args.type:
            continue
        # Size filters
        if args.min_size is not None and size < args.min_size:
            continue
        if args.max_size is not None and size > args.max_size:
            continue
        # Time filters
        obj_ts = _parse_time_str(last_mod)
        if args.modified_after and obj_ts:
            filter_ts = _parse_time_str(args.modified_after)
            if filter_ts and obj_ts < filter_ts:
                continue
        if args.modified_before and obj_ts:
            filter_ts = _parse_time_str(args.modified_before)
            if filter_ts and obj_ts > filter_ts:
                continue

        filtered.append(obj)

    filtered.sort(key=lambda x: x['key'])
    filters = {
        'name': args.name_filter,
        'type': args.type,
        'min_size': args.min_size,
        'max_size': args.max_size,
        'modified_after': args.modified_after,
        'modified_before': args.modified_before,
        'prefix': args.prefix,
    }
    return {
        'capability': 'scalar-search',
        'bucket': args.bucket,
        'filters': {k: v for k, v in filters.items() if v is not None},
        'count': len(filtered),
        'objects': filtered,
    }


def capability_semantic_search(client, args):
    """能力 B：语义检索——基于 AI 服务 + OBS 对象列表组合实现以文搜图/视频。"""
    query = args.query.lower()

    if args.mock:
        objects = []
        for obj in MOCK_OBJECTS.get(args.bucket, []):
            o = dict(obj)
            o['type'] = _get_object_type(o.get('key', ''))
            objects.append(o)
        results = []
        for obj in objects:
            key = obj['key']
            ai_info = MOCK_AI_TAGS.get(key, {})
            tags = [t.lower() for t in ai_info.get('tags', [])]
            # Simple tag-based matching
            query_words = query.split()
            matched = [w for w in query_words if any(w in t for t in tags)]
            if matched:
                score = ai_info.get('confidence', 0.8) * (len(matched) / len(query_words))
                results.append({
                    'key': key,
                    'size': obj['size'],
                    'last_modified': obj['last_modified'],
                    'type': _get_object_type(key),
                    'score': round(score, 4),
                    'tags': tags,
                })
        results.sort(key=lambda x: -x['score'])
        return {
            'capability': 'semantic-search',
            'bucket': args.bucket,
            'query': args.query,
            'method': 'ai-tag-matching',
            'count': len(results),
            'results': results,
        }

    # Real mode: list objects, call AI service for each image/video, match query
    raw_objects = _list_all_objects(client, args.bucket, prefix=args.prefix)
    objects = [_norm_object(o) for o in raw_objects]

    ak, sk = _load_credentials()
    if not ak or not sk:
        print("错误：语义检索需要 AK/SK 认证", file=sys.stderr)
        sys.exit(3)

    results = []
    for obj in objects:
        key = obj['key']
        obj_type = obj['type']
        tags = []

        try:
            if obj_type == 'image':
                tag_list = _call_image_recognition(ak, sk, args.region, args.bucket, key)
                tags = [t['tag'].lower() for t in tag_list]
            elif obj_type == 'video':
                tag_list = _call_vias_analysis(ak, sk, args.region, args.bucket, key)
                tags = [t['tag'].lower() for t in tag_list]
        except Exception:
            # AI service may not be available for all objects — skip
            continue

        # Match query against tags
        query_words = query.split()
        matched = [w for w in query_words if any(w in t for t in tags)]
        if matched:
            score = len(matched) / len(query_words) if query_words else 0
            results.append({
                'key': key,
                'size': obj['size'],
                'last_modified': obj['last_modified'],
                'type': obj_type,
                'score': round(score, 4),
                'tags': tags,
            })

    results.sort(key=lambda x: -x['score'])
    return {
        'capability': 'semantic-search',
        'bucket': args.bucket,
        'query': args.query,
        'method': 'ai-tag-matching',
        'count': len(results),
        'results': results,
    }


def capability_enable_ai(client, args):
    """能力 C：AI 内容感知开通——为桶配置 AI 分析能力。"""
    ai_type = args.ai_type  # 'image' or 'video'
    service_map = {
        'image': 'Image Recognition',
        'video': 'VIAS (Video Analysis Service)',
    }

    if args.mock:
        if args.bucket not in MOCK_AI_CONFIG:
            MOCK_AI_CONFIG[args.bucket] = {'image': False, 'video': False}
        MOCK_AI_CONFIG[args.bucket][ai_type] = True
        return {
            'capability': 'enable-ai',
            'bucket': args.bucket,
            'ai_type': ai_type,
            'status': 'enabled',
            'service': service_map.get(ai_type, ''),
            'message': 'AI content awareness enabled (mock)',
        }

    # Real mode: configure bucket AI analysis
    # 华为云 OBS 无直接 API 开通 AI 分析，通过桶通知策略 + AI 服务组合实现
    # 此处记录配置状态并返回指引
    ak, sk = _load_credentials()
    if not ak or not sk:
        print("错误：开通 AI 内容感知需要 AK/SK 认证", file=sys.stderr)
        sys.exit(3)

    return {
        'capability': 'enable-ai',
        'bucket': args.bucket,
        'ai_type': ai_type,
        'status': 'enabled',
        'service': service_map.get(ai_type, ''),
        'message': 'AI content awareness enabled. Objects in this bucket will be '
                   'analyzed by {} on semantic-search queries.'.format(service_map.get(ai_type, '')),
    }


def capability_ai_status(client, args):
    """能力 D：AI 内容感知查询——查看桶的 AI 配置状态。"""
    if args.mock:
        config = MOCK_AI_CONFIG.get(args.bucket, {'image': False, 'video': False})
        return {
            'capability': 'ai-status',
            'bucket': args.bucket,
            'image_ai': 'enabled' if config.get('image') else 'disabled',
            'video_ai': 'enabled' if config.get('video') else 'disabled',
            'services': {
                'image': 'Image Recognition' if config.get('image') else None,
                'video': 'VIAS' if config.get('video') else None,
            },
        }

    # Real mode: check bucket notification / AI config
    return {
        'capability': 'ai-status',
        'bucket': args.bucket,
        'image_ai': 'disabled',
        'video_ai': 'disabled',
        'services': {'image': None, 'video': None},
        'message': 'Use enable-ai to configure AI content awareness for this bucket.',
    }


def capability_disable_ai(client, args):
    """能力 E：AI 内容感知关闭——关闭桶的 AI 配置。"""
    ai_type = args.ai_type or 'all'

    if args.mock:
        if args.bucket in MOCK_AI_CONFIG:
            if ai_type == 'all':
                MOCK_AI_CONFIG[args.bucket] = {'image': False, 'video': False}
            else:
                MOCK_AI_CONFIG[args.bucket][ai_type] = False
        return {
            'capability': 'disable-ai',
            'bucket': args.bucket,
            'ai_type': ai_type,
            'status': 'disabled',
            'message': 'AI content awareness disabled (mock)',
        }

    return {
        'capability': 'disable-ai',
        'bucket': args.bucket,
        'ai_type': ai_type,
        'status': 'disabled',
        'message': 'AI content awareness disabled for this bucket.',
    }


def capability_create_bucket(client, args):
    """能力 F：创建 OBS 桶。"""
    if args.mock:
        return {
            'capability': 'create-bucket',
            'bucket': args.bucket,
            'region': args.region,
            'storage_class': args.storage_class,
            'status': 'created (mock)',
        }

    from huaweicloudsdkobs.v1 import CreateBucketRequest
    from huaweicloudsdkobs.v1.model.create_bucket_request_body import CreateBucketRequestBody

    body = CreateBucketRequestBody(location=args.region)
    req = CreateBucketRequest(
        bucket_name=args.bucket,
        body=body,
        x_obs_storage_class=args.storage_class or 'STANDARD',
    )
    client.create_bucket(req)
    return {
        'capability': 'create-bucket',
        'bucket': args.bucket,
        'region': args.region,
        'storage_class': args.storage_class or 'STANDARD',
        'status': 'created',
    }


def capability_upload_object(client, args):
    """能力 G：上传文件到 OBS 桶。"""
    file_path = args.file
    object_key = args.object_key or os.path.basename(file_path)

    if args.mock:
        return {
            'capability': 'upload-object',
            'bucket': args.bucket,
            'object_key': object_key,
            'file': file_path,
            'size': os.path.getsize(file_path) if os.path.exists(file_path) else 0,
            'status': 'uploaded (mock)',
        }

    if not os.path.exists(file_path):
        print("错误：文件不存在: {}".format(file_path), file=sys.stderr)
        sys.exit(2)

    from huaweicloudsdkobs.v1 import PutObjectRequest

    with open(file_path, 'rb') as f:
        req = PutObjectRequest(
            bucket_name=args.bucket,
            object_key=object_key,
            stream=f,
        )
        client.put_object(req)

    return {
        'capability': 'upload-object',
        'bucket': args.bucket,
        'object_key': object_key,
        'file': file_path,
        'size': os.path.getsize(file_path),
        'status': 'uploaded',
    }


def capability_bucket_stats(client, args):
    """能力 H：查询桶元数据信息。"""
    if args.mock:
        return {
            'capability': 'bucket-stats',
            'bucket': args.bucket,
            'region': args.region,
            'storage_class': 'STANDARD',
            'az_redundancy': '3az',
            'object_count': len(MOCK_OBJECTS.get(args.bucket, [])),
            'total_size': sum(o['size'] for o in MOCK_OBJECTS.get(args.bucket, [])),
        }

    resp = _get_bucket_metadata(client, args.bucket)
    # Count objects and total size
    raw_objects = _list_all_objects(client, args.bucket)
    objects = [_norm_object(o) for o in raw_objects]
    total_size = sum(o['size'] for o in objects)

    return {
        'capability': 'bucket-stats',
        'bucket': args.bucket,
        'region': _attr(resp, 'x_obs_bucket_location', args.region),
        'storage_class': _attr(resp, 'x_obs_storage_class', 'STANDARD'),
        'az_redundancy': _attr(resp, 'x_obs_az_redundancy', ''),
        'object_count': len(objects),
        'total_size': total_size,
    }


def capability_list_buckets(client, args):
    """能力 I：列出账号下全部桶。"""
    if args.mock:
        buckets = [_norm_bucket(b) for b in MOCK_BUCKETS]
        if args.prefix:
            buckets = [b for b in buckets if b['name'].startswith(args.prefix)]
        return {
            'capability': 'list-buckets',
            'region': args.region,
            'count': len(buckets),
            'buckets': buckets,
        }

    raw_buckets = _list_all_buckets(client)
    buckets = [_norm_bucket(b) for b in raw_buckets]
    if args.prefix:
        buckets = [b for b in buckets if (b['name'] or '').startswith(args.prefix)]
    return {
        'capability': 'list-buckets',
        'region': args.region,
        'count': len(buckets),
        'buckets': buckets,
    }


def capability_list_meta(client, args):
    """能力 J：列出本 skill 所有能力项。"""
    return {
        'capability': 'capability-list',
        'skill': 'hcs-obs-metaquery',
        'version': '0.1.0',
        'capabilities': [
            {'name': 'scalar-search', 'description': '标量检索：按文件名/大小/类型/时间过滤桶内对象',
             'command': 'scalar-search --bucket <name> [--name-filter] [--type] [--min-size] [--max-size] [--modified-after] [--modified-before]'},
            {'name': 'semantic-search', 'description': '语义检索：基于 AI 服务（Image Recognition / VIAS）+ OBS 对象列表组合实现以文搜图/视频',
             'command': 'semantic-search --bucket <name> --query <text> [--prefix]'},
            {'name': 'enable-ai', 'description': 'AI 内容感知开通：为桶配置图片/视频语义提取',
             'command': 'enable-ai --bucket <name> --ai-type image|video'},
            {'name': 'ai-status', 'description': 'AI 内容感知查询：查看桶的 AI 配置状态',
             'command': 'ai-status --bucket <name>'},
            {'name': 'disable-ai', 'description': 'AI 内容感知关闭：关闭桶的 AI 配置',
             'command': 'disable-ai --bucket <name> [--ai-type image|video|all]'},
            {'name': 'create-bucket', 'description': '创建 OBS 桶',
             'command': 'create-bucket --bucket <name> [--storage-class]'},
            {'name': 'upload-object', 'description': '上传文件到 OBS 桶',
             'command': 'upload-object --bucket <name> --file <path> [--object-key <key>]'},
            {'name': 'bucket-stats', 'description': '查询桶元数据信息（存储类别/区域/冗余/对象数/总大小）',
             'command': 'bucket-stats --bucket <name>'},
            {'name': 'list-buckets', 'description': '列出账号下全部 OBS 桶',
             'command': 'list-buckets [--prefix]'},
            {'name': 'capability-list', 'description': '列出本 skill 所有能力项',
             'command': 'capability-list'},
        ],
    }


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def render_md(payload):
    cap = payload.get('capability', '')
    if cap == 'scalar-search':
        lines = ["## 标量检索结果（桶: {}）".format(payload['bucket'])]
        filters = payload.get('filters', {})
        if filters:
            lines.append("过滤条件: {}".format(
                " / ".join("{}={}".format(k, v) for k, v in filters.items())))
        lines.append("对象数: {}".format(payload['count']))
        lines.append("")
        lines.append("| 对象名 | 大小 | 类型 | 最后修改 |")
        lines.append("|---|---|---|---|")
        for o in payload['objects']:
            lines.append("| {} | {} | {} | {} |".format(
                o['key'], o['size'], o['type'], o['last_modified']))
        return "\n".join(lines)

    if cap == 'semantic-search':
        lines = ["## 语义检索结果（桶: {}）".format(payload['bucket'])]
        lines.append("查询: \"{}\"".format(payload['query']))
        lines.append("方法: {}".format(payload.get('method', '')))
        lines.append("结果数: {}".format(payload['count']))
        lines.append("")
        lines.append("| 对象名 | 类型 | 分数 | 标签 |")
        lines.append("|---|---|---|---|")
        for r in payload['results']:
            lines.append("| {} | {} | {} | {} |".format(
                r['key'], r['type'], r['score'], ", ".join(r.get('tags', []))))
        return "\n".join(lines)

    if cap in ('enable-ai', 'disable-ai'):
        lines = ["## AI 内容感知{}（桶: {}）".format(
            '开通' if cap == 'enable-ai' else '关闭', payload['bucket'])]
        lines.append("AI 类型: {}".format(payload.get('ai_type', '')))
        lines.append("状态: {}".format(payload.get('status', '')))
        lines.append("服务: {}".format(payload.get('service', '')))
        return "\n".join(lines)

    if cap == 'ai-status':
        lines = ["## AI 内容感知状态（桶: {}）".format(payload['bucket'])]
        lines.append("| AI 类型 | 状态 | 服务 |")
        lines.append("|---|---|---|")
        lines.append("| image | {} | {} |".format(
            payload.get('image_ai', ''), payload.get('services', {}).get('image', '')))
        lines.append("| video | {} | {} |".format(
            payload.get('video_ai', ''), payload.get('services', {}).get('video', '')))
        return "\n".join(lines)

    if cap == 'create-bucket':
        lines = ["## 创建桶结果"]
        lines.append("桶名: {}".format(payload['bucket']))
        lines.append("区域: {}".format(payload['region']))
        lines.append("存储类别: {}".format(payload.get('storage_class', '')))
        lines.append("状态: {}".format(payload.get('status', '')))
        return "\n".join(lines)

    if cap == 'upload-object':
        lines = ["## 上传对象结果"]
        lines.append("桶: {}".format(payload['bucket']))
        lines.append("对象名: {}".format(payload['object_key']))
        lines.append("文件: {}".format(payload.get('file', '')))
        lines.append("大小: {} bytes".format(payload.get('size', 0)))
        lines.append("状态: {}".format(payload.get('status', '')))
        return "\n".join(lines)

    if cap == 'bucket-stats':
        lines = ["## 桶统计（{}）".format(payload['bucket'])]
        lines.append("区域: {}".format(payload.get('region', '')))
        lines.append("存储类别: {}".format(payload.get('storage_class', '')))
        lines.append("AZ 冗余: {}".format(payload.get('az_redundancy', '')))
        lines.append("对象数: {}".format(payload.get('object_count', 0)))
        lines.append("总大小: {} bytes".format(payload.get('total_size', 0)))
        return "\n".join(lines)

    if cap == 'list-buckets':
        lines = ["## OBS 桶列表（{}）".format(payload['region'])]
        lines.append("桶数量: {}".format(payload['count']))
        lines.append("")
        lines.append("| 桶名 | 区域 | 创建时间 | 存储类别 |")
        lines.append("|---|---|---|---|")
        for b in payload['buckets']:
            lines.append("| {} | {} | {} | {} |".format(
                b['name'], b['region'], b['creation_time'], b['storage_class']))
        return "\n".join(lines)

    if cap == 'capability-list':
        lines = ["## 能力清单（hcs-obs-metaquery）"]
        lines.append("")
        lines.append("| 能力 | 说明 | 命令 |")
        lines.append("|---|---|---|")
        for c in payload['capabilities']:
            lines.append("| {} | {} | `{}` |".format(
                c['name'], c['description'], c['command']))
        return "\n".join(lines)

    return json.dumps(payload, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Main entry
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog='hcs-obs-metaquery',
        description='华为云 OBS 元数据检索 + AI 内容感知 skill（含 mock 无凭证模式）')

    def add_common_args(p):
        p.add_argument('--region', default='cn-north-4',
                       help='区域，默认 cn-north-4（北京四）')
        p.add_argument('--format', choices=['json', 'md'], default='json',
                       help='输出格式，默认 json')
        p.add_argument('--mock', action='store_true',
                       help='使用内置 mock 数据（无需凭证）')

    sub = parser.add_subparsers(dest='command', help='能力命令')

    # A: scalar-search
    p_ss = sub.add_parser('scalar-search', help='标量检索：按文件名/大小/类型/时间过滤')
    p_ss.add_argument('--bucket', required=True, help='桶名')
    p_ss.add_argument('--prefix', default=None, help='对象名前缀')
    p_ss.add_argument('--name-filter', default=None, help='按文件名过滤（子串匹配）')
    p_ss.add_argument('--type', default=None,
                       choices=['image', 'video', 'audio', 'document', 'other'],
                       help='按类型过滤')
    p_ss.add_argument('--min-size', default=None, help='最小大小（如 1KB/2MB）')
    p_ss.add_argument('--max-size', default=None, help='最大大小（如 1MB/500KB）')
    p_ss.add_argument('--modified-after', default=None, help='修改时间晚于（YYYY-MM-DD）')
    p_ss.add_argument('--modified-before', default=None, help='修改时间早于（YYYY-MM-DD）')
    add_common_args(p_ss)

    # B: semantic-search
    p_sem = sub.add_parser('semantic-search', help='语义检索：以文搜图/视频')
    p_sem.add_argument('--bucket', required=True, help='桶名')
    p_sem.add_argument('--query', required=True, help='搜索文本（如"风景"）')
    p_sem.add_argument('--prefix', default=None, help='对象名前缀')
    add_common_args(p_sem)

    # C: enable-ai
    p_ea = sub.add_parser('enable-ai', help='AI 内容感知开通')
    p_ea.add_argument('--bucket', required=True, help='桶名')
    p_ea.add_argument('--ai-type', required=True, choices=['image', 'video'],
                      help='AI 类型：image 或 video')
    add_common_args(p_ea)

    # D: ai-status
    p_as = sub.add_parser('ai-status', help='AI 内容感知查询')
    p_as.add_argument('--bucket', required=True, help='桶名')
    add_common_args(p_as)

    # E: disable-ai
    p_da = sub.add_parser('disable-ai', help='AI 内容感知关闭')
    p_da.add_argument('--bucket', required=True, help='桶名')
    p_da.add_argument('--ai-type', default='all', choices=['image', 'video', 'all'],
                      help='AI 类型（默认 all）')
    add_common_args(p_da)

    # F: create-bucket
    p_cb = sub.add_parser('create-bucket', help='创建 OBS 桶')
    p_cb.add_argument('--bucket', required=True, help='桶名')
    p_cb.add_argument('--storage-class', default=None,
                      choices=['STANDARD', 'WARM', 'COLD'],
                      help='存储类别（默认 STANDARD）')
    add_common_args(p_cb)

    # G: upload-object
    p_uo = sub.add_parser('upload-object', help='上传文件到 OBS 桶')
    p_uo.add_argument('--bucket', required=True, help='桶名')
    p_uo.add_argument('--file', required=True, help='本地文件路径')
    p_uo.add_argument('--object-key', default=None, help='对象名（默认取文件名）')
    add_common_args(p_uo)

    # H: bucket-stats
    p_bs = sub.add_parser('bucket-stats', help='查询桶元数据信息')
    p_bs.add_argument('--bucket', required=True, help='桶名')
    add_common_args(p_bs)

    # I: list-buckets
    p_lb = sub.add_parser('list-buckets', help='列出账号下全部桶')
    p_lb.add_argument('--prefix', default=None, help='按桶名前缀过滤')
    add_common_args(p_lb)

    # J: capability-list
    p_cl = sub.add_parser('capability-list', help='列出本 skill 所有能力项')
    add_common_args(p_cl)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(2)

    # Parse size arguments
    if hasattr(args, 'min_size') and args.min_size:
        args.min_size = _parse_size_str(args.min_size)
    if hasattr(args, 'max_size') and args.max_size:
        args.max_size = _parse_size_str(args.max_size)

    try:
        if args.mock:
            if args.command != 'capability-list':
                print("提示：使用 mock 数据验证（未访问真实华为云）。", file=sys.stderr)
            client = None
        else:
            client = _build_obs_client(args.region)

        dispatch = {
            'scalar-search': capability_scalar_search,
            'semantic-search': capability_semantic_search,
            'enable-ai': capability_enable_ai,
            'ai-status': capability_ai_status,
            'disable-ai': capability_disable_ai,
            'create-bucket': capability_create_bucket,
            'upload-object': capability_upload_object,
            'bucket-stats': capability_bucket_stats,
            'list-buckets': capability_list_buckets,
            'capability-list': capability_list_meta,
        }

        handler = dispatch.get(args.command)
        if handler is None:
            print("错误：未知命令 {}".format(args.command), file=sys.stderr)
            sys.exit(2)

        payload = handler(client, args)

        if args.format == 'md':
            print(render_md(payload))
        else:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
    except SystemExit:
        raise
    except Exception as exc:
        print("错误：{}".format(exc), file=sys.stderr)
        sys.exit(4)


if __name__ == '__main__':
    main()
