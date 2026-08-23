#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tencent Cloud COS helper with least-privilege guards.

Required environment:
  COS_SECRET_ID, COS_SECRET_KEY, COS_REGION, COS_BUCKET

Optional environment:
  COS_ALLOWED_PREFIX  object-key prefix allowlist
  COS_LOCAL_ROOT      local filesystem root for upload/download paths
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from qcloud_cos import CosConfig, CosS3Client
from qcloud_cos.cos_exception import CosServiceError

MAX_LIST_ITEMS = 200
DEFAULT_LIST_ITEMS = 50
MAX_PART_SIZE_MB = 32
MAX_THREADS = 8
KEY_RE = re.compile(r"^[A-Za-z0-9._/=+\-@]+$")
KEY_MAX_LEN = 850


def _require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise ValueError(f"Missing required environment variable {name}")
    return value


def get_cos_client() -> CosS3Client:
    secret_id = _require_env("COS_SECRET_ID")
    secret_key = _require_env("COS_SECRET_KEY")
    region = os.environ.get("COS_REGION", "ap-beijing").strip() or "ap-beijing"
    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
    return CosS3Client(config)


def configured_bucket() -> str:
    return _require_env("COS_BUCKET")


def monthly_prefix() -> str:
    now = datetime.now()
    return f"{now.year}/{now.month:02d}/"


def _check_allowed_prefix(key: str) -> None:
    allowed = os.environ.get("COS_ALLOWED_PREFIX", "").strip().lstrip("/")
    if allowed and not key.startswith(allowed):
        raise ValueError(f"Object key is outside COS_ALLOWED_PREFIX={allowed!r}")


def validate_object_key(cos_key: str) -> str:
    key = (cos_key or "").strip().lstrip("/")
    if not key:
        raise ValueError("Object key is empty")
    if len(key) > KEY_MAX_LEN:
        raise ValueError("Object key exceeds 850 bytes")
    if ".." in key.split("/"):
        raise ValueError("Object key must not contain '..' segments")
    if not KEY_RE.match(key):
        raise ValueError("Object key contains unsupported characters")
    _check_allowed_prefix(key)
    return key


def validate_list_prefix(prefix: str) -> str:
    value = (prefix or "").strip().lstrip("/")
    if not value:
        raise ValueError("list requires --prefix; listing an entire bucket is not allowed")
    sample = value if not value.endswith("/") else f"{value}placeholder"
    validate_object_key(sample)
    _check_allowed_prefix(value)
    return value


def resolve_local_path(path: str, *, must_exist: bool) -> Path:
    raw = Path(path).expanduser()
    if not raw.is_absolute():
        raw = Path.cwd() / raw
    target = raw.resolve()
    if must_exist and not target.is_file():
        raise FileNotFoundError(f"Local file not found: {target}")

    root_value = os.environ.get("COS_LOCAL_ROOT", "").strip()
    if root_value:
        root = Path(root_value).expanduser().resolve()
        try:
            target.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"Local path is outside COS_LOCAL_ROOT={root}") from exc
    return target


def object_exists(client: CosS3Client, bucket: str, cos_key: str) -> bool:
    try:
        client.head_object(Bucket=bucket, Key=cos_key)
        return True
    except CosServiceError as exc:
        status = getattr(exc, "get_status_code", lambda: None)()
        error_code = str(getattr(exc, "get_error_code", lambda: "")() or "")
        if status in (404, "404") or error_code in {"NoSuchKey", "NoSuchResource"}:
            return False
        raise


def resolve_upload_key(local_file: Path, cos_key: str | None) -> str:
    if cos_key is None or not str(cos_key).strip():
        return validate_object_key(f"{monthly_prefix()}{local_file.name}")
    raw = str(cos_key).strip()
    if raw.endswith("/"):
        raw = f"{raw}{local_file.name}"
    return validate_object_key(raw)


def upload_file(
    local_file_path: str,
    cos_key: str | None = None,
    *,
    overwrite: bool = False,
    advanced: bool = False,
    part_size: int = 1,
    max_threads: int = 4,
) -> dict:
    local_file = resolve_local_path(local_file_path, must_exist=True)
    key = resolve_upload_key(local_file, cos_key)
    bucket = configured_bucket()
    client = get_cos_client()

    if object_exists(client, bucket, key) and not overwrite:
        raise ValueError(
            f"Remote object already exists: {key}. Re-run with --overwrite after user approval."
        )

    print(f"upload local={local_file}")
    print(f"bucket={bucket}")
    print(f"key={key}")

    if advanced:
        part_size = max(1, min(int(part_size), MAX_PART_SIZE_MB))
        max_threads = max(1, min(int(max_threads), MAX_THREADS))
        response = client.upload_file(
            Bucket=bucket,
            LocalFilePath=str(local_file),
            Key=key,
            PartSize=part_size,
            MAXThread=max_threads,
        )
    else:
        with open(local_file, "br") as fp:
            response = client.put_object(
                Bucket=bucket,
                Body=fp,
                Key=key,
                EnableMD5=True,
            )

    print(f"upload ok etag={response.get('ETag', 'N/A')}")
    return response


def download_file(
    cos_key: str,
    local_file_path: str,
    *,
    overwrite: bool = False,
) -> None:
    key = validate_object_key(cos_key)
    dest = resolve_local_path(local_file_path, must_exist=False)
    if dest.exists() and not overwrite:
        raise ValueError(
            f"Local file already exists: {dest}. Re-run with --overwrite after user approval."
        )
    dest.parent.mkdir(parents=True, exist_ok=True)

    bucket = configured_bucket()
    client = get_cos_client()
    print(f"download key={key}")
    print(f"bucket={bucket}")
    print(f"local={dest}")

    response = client.get_object(Bucket=bucket, Key=key)
    tmp = dest.with_name(dest.name + ".cos-partial")
    try:
        body = response["Body"]
        raw_stream = body.get_raw_stream() if hasattr(body, "get_raw_stream") else None
        if raw_stream is not None:
            with open(tmp, "bw") as out:
                while True:
                    chunk = raw_stream.read(1024 * 1024)
                    if not chunk:
                        break
                    out.write(chunk)
        else:
            body.get_stream_to_file(str(tmp))
        os.replace(tmp, dest)
    finally:
        if tmp.exists() and tmp != dest:
            tmp.unlink()
    print("download ok")


def list_objects(prefix: str, max_items: int = DEFAULT_LIST_ITEMS) -> dict:
    prefix = validate_list_prefix(prefix)

    max_items = max(1, min(int(max_items), MAX_LIST_ITEMS))
    bucket = configured_bucket()
    client = get_cos_client()
    print(f"list bucket={bucket} prefix={prefix} max={max_items}")

    response = client.list_objects(Bucket=bucket, Prefix=prefix, MaxKeys=max_items)
    contents = response.get("Contents") or []
    if not contents:
        print("no objects")
        return response
    print(f"found {len(contents)} object(s):")
    for obj in contents:
        print(f"  - {obj.get('Key')} ({obj.get('Size', 'N/A')} bytes, {obj.get('LastModified', 'N/A')})")
    return response


def delete_object(cos_key: str, confirm: str) -> dict:
    key = validate_object_key(cos_key)
    if (confirm or "").strip() != key:
        raise ValueError("--confirm must exactly match the object key")

    bucket = configured_bucket()
    client = get_cos_client()
    print(f"delete key={key} bucket={bucket}")
    response = client.delete_object(Bucket=bucket, Key=key)
    print("delete ok")
    return response


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Tencent COS ops with confirmation guards")
    sub = parser.add_subparsers(dest="command")

    upload = sub.add_parser("upload", help="Upload one local file")
    upload.add_argument("local_file")
    upload.add_argument("--key", "-k", help="Exact object key, or a prefix ending with /")
    upload.add_argument("--overwrite", action="store_true", help="Replace an existing remote object")
    upload.add_argument("--advanced", "-a", action="store_true")
    upload.add_argument("--part-size", "-p", type=int, default=1)
    upload.add_argument("--threads", "-t", type=int, default=4)

    download = sub.add_parser("download", help="Download one object")
    download.add_argument("cos_key")
    download.add_argument("local_file")
    download.add_argument("--overwrite", action="store_true", help="Replace an existing local file")

    listing = sub.add_parser("list", help="List objects under a prefix")
    listing.add_argument("--prefix", "-p", required=True)
    listing.add_argument("--max", "-m", type=int, default=DEFAULT_LIST_ITEMS)

    delete = sub.add_parser("delete", help="Delete one object")
    delete.add_argument("cos_key")
    delete.add_argument(
        "--confirm",
        required=True,
        help="Must equal the object key; refuses the delete otherwise",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "upload":
            upload_file(
                args.local_file,
                cos_key=args.key,
                overwrite=args.overwrite,
                advanced=args.advanced,
                part_size=args.part_size,
                max_threads=args.threads,
            )
        elif args.command == "download":
            download_file(args.cos_key, args.local_file, overwrite=args.overwrite)
        elif args.command == "list":
            list_objects(prefix=args.prefix, max_items=args.max)
        elif args.command == "delete":
            delete_object(args.cos_key, confirm=args.confirm)
        else:
            parser.print_help()
            return 1
    except (ValueError, FileNotFoundError, CosServiceError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
