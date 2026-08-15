#!/usr/bin/env python3
"""上传图片并调用极鲸云 SHEIN 图搜同款接口。"""

import argparse
import base64
import binascii
import json
import mimetypes
import os
import re
import sys
import uuid
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlencode, urlparse
from urllib.request import Request, url2pathname, urlopen

from geekbi_auth import ActionRequired, authenticated_json_request
from shein_search_common import (
    DEFAULT_BASE_URL,
    parse_int,
    parse_pairs,
    validate_page,
    validate_range_pairs,
    validate_search_response,
    validate_sort,
)


ENDPOINT = "/api/v1/shein/goods/ai-image-search"
MAX_IMAGE_SIZE = 10 * 1024 * 1024
BASE_PARAMS = {
    "keyword",
    "blockKeyword",
    "matchMode",
    "catIds",
    "siteId",
    "hostingMode",
    "page",
    "size",
    "sort",
    "order",
}
NUMERIC_RANGE_PARAMS = {
    "sold",
    "totalSold",
    "daySold",
    "weekSold",
    "monthSold",
    "daySoldRate",
    "weekSoldRate",
    "monthSoldRate",
    "sales",
    "totalSales",
    "daySales",
    "weekSales",
    "monthSales",
    "daySalesRate",
    "weekSalesRate",
    "monthSalesRate",
    "mallSold",
    "similarNum",
    "price",
    "supplyPrice",
    "goodsScore",
    "reviewNum",
}
INTEGER_RANGE_PARAMS = {
    "sold",
    "totalSold",
    "daySold",
    "weekSold",
    "monthSold",
    "mallSold",
    "similarNum",
    "reviewNum",
}
NONNEGATIVE_RANGE_PARAMS = {
    "similarNum",
    "sold",
    "totalSold",
    "daySold",
    "weekSold",
    "monthSold",
    "sales",
    "totalSales",
    "daySales",
    "weekSales",
    "monthSales",
    "mallSold",
    "price",
    "supplyPrice",
    "goodsScore",
    "reviewNum",
}
DATE_RANGE_PARAMS = {"onSaleTime", "mallOpenTime"}
ALLOWED_PARAMS = BASE_PARAMS | {
    f"{field}{suffix}"
    for field in NUMERIC_RANGE_PARAMS | DATE_RANGE_PARAMS
    for suffix in ("Min", "Max")
}
SORT_FIELDS = {
    "sold",
    "totalSold",
    "daySold",
    "weekSold",
    "monthSold",
    "totalSoldRate",
    "daySoldRate",
    "weekSoldRate",
    "monthSoldRate",
    "sales",
    "totalSales",
    "daySales",
    "weekSales",
    "monthSales",
    "totalSalesRate",
    "daySalesRate",
    "weekSalesRate",
    "monthSalesRate",
    "minPrice",
    "maxPrice",
    "supplyPrice",
    "minSupplyPrice",
    "medianSupplyPrice",
    "maxSupplyPrice",
    "goodsScore",
    "reviewNum",
    "similarNum",
    "similarNumUpdateTime",
    "onSaleTime",
    "mallSold",
    "mallOpenTime",
    "createTime",
    "updateTime",
}
ALLOWED_IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/gif",
    "image/webp",
    "image/bmp",
    "image/tiff",
    "image/avif",
    "image/heic",
    "image/heif",
}


def parse_params(raw_params):
    params, values, repeated = parse_pairs(
        raw_params,
        ALLOWED_PARAMS,
        repeated_params={"catIds"},
    )
    if len(values.get("keyword", "")) > 300:
        raise ValueError("商品关键词不能超过 300 个字符")
    if len(values.get("blockKeyword", "")) > 300:
        raise ValueError("排除关键词不能超过 300 个字符")
    if "matchMode" in values:
        parse_int("匹配模式", values["matchMode"], minimum=1, maximum=2)
    if "siteId" in values:
        parse_int("站点 ID", values["siteId"], minimum=1)
    if "hostingMode" in values:
        parse_int("托管模式", values["hostingMode"], minimum=0, maximum=2)
    for value in repeated["catIds"]:
        parse_int("类目 ID", value, minimum=1)
    validate_page(values)
    validate_sort(values, SORT_FIELDS)
    validate_range_pairs(
        values,
        NUMERIC_RANGE_PARAMS,
        DATE_RANGE_PARAMS,
        INTEGER_RANGE_PARAMS,
        NONNEGATIVE_RANGE_PARAMS,
    )
    return params


def validate_response(payload):
    return validate_search_response(payload, "图搜查询失败")


def _clean_content_type(content_type):
    if not content_type:
        return None
    return content_type.split(";", 1)[0].strip().lower()


def _detect_content_type(data):
    if data.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return "image/gif"
    if len(data) >= 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp"
    if data.startswith(b"BM"):
        return "image/bmp"
    if data.startswith((b"II*\x00", b"MM\x00*")):
        return "image/tiff"
    if len(data) >= 12 and data[4:8] == b"ftyp":
        brand = data[8:12]
        if brand in {b"avif", b"avis"}:
            return "image/avif"
        if brand in {b"heic", b"heix", b"hevc", b"hevx", b"mif1", b"msf1"}:
            return "image/heic"
    return None


def _extension(content_type):
    return {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/bmp": ".bmp",
        "image/tiff": ".tiff",
        "image/avif": ".avif",
        "image/heic": ".heic",
        "image/heif": ".heic",
    }.get(content_type)


def _validate_image(data, declared_content_type=None):
    if not data:
        raise ValueError("图片内容为空")
    if len(data) > MAX_IMAGE_SIZE:
        raise ValueError("图片大小不能超过10M")
    detected = _detect_content_type(data)
    declared = _clean_content_type(declared_content_type)
    if detected in ALLOWED_IMAGE_TYPES:
        return detected
    if declared in ALLOWED_IMAGE_TYPES:
        return declared
    raise ValueError("无法识别图片格式，请使用支持的位图文件")


def _read_limited(response):
    data = response.read(MAX_IMAGE_SIZE + 1)
    if len(data) > MAX_IMAGE_SIZE:
        raise ValueError("图片大小不能超过10M")
    return data


def _read_data_uri(source):
    match = re.fullmatch(r"data:([^;,]+)?(?:;charset=[^;,]+)?;base64,(.+)", source, re.DOTALL)
    if not match:
        raise ValueError("图片 Data URI 格式不正确")
    try:
        data = base64.b64decode(match.group(2), validate=True)
    except (ValueError, binascii.Error) as error:
        raise ValueError("图片 Base64 内容无效") from error
    content_type = _validate_image(data, match.group(1))
    return data, content_type, "image" + _extension(content_type)


def _read_base64(source):
    try:
        data = base64.b64decode(source.removeprefix("base64:"), validate=True)
    except (ValueError, binascii.Error) as error:
        raise ValueError("图片 Base64 内容无效") from error
    content_type = _validate_image(data)
    return data, content_type, "image" + _extension(content_type)


def _read_remote_image(source, timeout):
    request = Request(source, headers={"User-Agent": "GeekBI-SHEIN-Image-Search-Skill"})
    with urlopen(request, timeout=timeout) as response:
        data = _read_limited(response)
        content_type = _validate_image(data, response.headers.get_content_type())
        path_name = Path(unquote(urlparse(response.geturl()).path)).name
        filename = path_name or "image" + _extension(content_type)
        return data, content_type, filename


def _read_local_image(source):
    parsed = urlparse(source)
    if parsed.scheme == "file":
        uri_path = unquote(parsed.path)
        if parsed.netloc and parsed.netloc != "localhost":
            uri_path = f"//{parsed.netloc}{uri_path}"
        uri_path = url2pathname(uri_path)
        if os.name == "nt" and re.match(r"^/[A-Za-z]:", uri_path):
            uri_path = uri_path[1:]
        path = Path(uri_path)
    else:
        path = Path(source)
    if not path.is_file():
        raise ValueError(f"找不到图片文件: {path}")
    if path.stat().st_size > MAX_IMAGE_SIZE:
        raise ValueError("图片大小不能超过10M")
    data = path.read_bytes()
    guessed_type, _ = mimetypes.guess_type(path.name)
    content_type = _validate_image(data, guessed_type)
    return data, content_type, path.name


def read_image_source(source, timeout):
    if source == "-":
        data = sys.stdin.buffer.read(MAX_IMAGE_SIZE + 1)
        content_type = _validate_image(data)
        return data, content_type, "image" + _extension(content_type)
    if source.startswith("data:"):
        return _read_data_uri(source)
    if source.startswith("base64:"):
        return _read_base64(source)
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        return _read_remote_image(source, timeout)
    if parsed.scheme not in {"", "file"}:
        raise ValueError("图片地址只支持本地文件、file、http 或 https")
    return _read_local_image(source)


def build_url(base_url, params):
    url = f"{base_url.rstrip('/')}{ENDPOINT}"
    query = urlencode(params)
    return f"{url}?{query}" if query else url


def build_multipart(data, content_type, filename):
    boundary = "----GeekBIBoundary" + uuid.uuid4().hex
    safe_filename = re.sub(r"[^A-Za-z0-9._-]", "_", Path(filename).name)
    if not safe_filename:
        safe_filename = "image" + _extension(content_type)
    header = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{safe_filename}"\r\n'
        f"Content-Type: {content_type}\r\n\r\n"
    ).encode("utf-8")
    body = header + data + f"\r\n--{boundary}--\r\n".encode("ascii")
    return body, f"multipart/form-data; boundary={boundary}"


def main():
    parser = argparse.ArgumentParser(description="用图片查询 SHEIN 同款商品并输出 JSON")
    parser.add_argument(
        "--image",
        required=True,
        help="本地路径、file/http/https 地址、Data URI、base64:内容，或 - 从标准输入读取",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"极鲸云服务地址，默认 {DEFAULT_BASE_URL}",
    )
    parser.add_argument(
        "--param",
        action="append",
        default=[],
        help="商品筛选参数，格式为 key=value；列表字段可重复传入",
    )
    parser.add_argument("--timeout", type=float, default=60, help="请求超时秒数")
    args = parser.parse_args()

    try:
        params = parse_params(args.param)
        data, content_type, filename = read_image_source(args.image, args.timeout)
        body, multipart_content_type = build_multipart(data, content_type, filename)
        payload = authenticated_json_request(
            build_url(args.base_url, params),
            args.base_url,
            args.timeout,
            method="POST",
            body=body,
            headers={"Content-Type": multipart_content_type},
        )
        payload = validate_response(payload)
    except ActionRequired as error:
        print(json.dumps(error.public_payload(), ensure_ascii=False, indent=2))
        return 2
    except (ValueError, OSError, HTTPError, URLError, TimeoutError) as error:
        print(
            json.dumps({"error": True, "msg": str(error)}, ensure_ascii=False),
            file=sys.stderr,
        )
        return 1

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
