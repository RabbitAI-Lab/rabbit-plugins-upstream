#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.28.0",
# ]
# ///
"""
aoment-image-video CLI

Agent API Key authenticated image and video generation powered by Aoment AI.
The client calls the dedicated skill API endpoints only.
"""

import argparse
import base64
import json
import mimetypes
import os
import re
import sys

import requests

API_BASE = "https://www.aoment.com"

DEFAULT_IMAGE_MODEL = "image-n2-fast"
DEFAULT_VIDEO_MODEL = "video-v1-fast"
DEFAULT_RECOGNITION_MODEL = "image-recognition-g2"
SUPPORTED_VIDEO_MODELS = {"video-v1-fast", "video-seedance-2"}

IMAGE_TIMEOUT = 660
VIDEO_TIMEOUT = 1380


def _auth_headers(api_key: str) -> dict:
    return {"Authorization": f"Bearer {api_key}"}


def _json_or_error(response: requests.Response) -> dict:
    try:
        result = response.json()
    except ValueError:
        return {"success": False, "error": response.text or f"HTTP {response.status_code}"}

    if not response.ok and result.get("success") is not False:
        result["success"] = False
        result.setdefault("error", f"HTTP {response.status_code}")
    return result


def _decode_base64_image(value: str) -> bytes:
    if "," in value and value.split(",", 1)[0].startswith("data:image/"):
        value = value.split(",", 1)[1]
    return base64.b64decode(value)


def _image_file_tuple(source: str, fallback_name: str) -> tuple[str, bytes, str]:
    if os.path.exists(source):
        with open(source, "rb") as file:
            content = file.read()
        content_type = mimetypes.guess_type(source)[0] or "image/png"
        return os.path.basename(source) or fallback_name, content, content_type

    image_bytes = _decode_base64_image(source)
    return fallback_name, image_bytes, "image/png"


def _media_file_tuple(source: str, fallback_name: str, fallback_type: str) -> tuple[str, bytes, str]:
    if os.path.exists(source):
        with open(source, "rb") as file:
            content = file.read()
        content_type = mimetypes.guess_type(source)[0] or fallback_type
        return os.path.basename(source) or fallback_name, content, content_type

    media_bytes = base64.b64decode(source)
    return fallback_name, media_bytes, fallback_type


def generate_text_to_image(api_base: str, args: argparse.Namespace) -> dict:
    url = f"{api_base}/api/skills/aoment-image-video/text-to-image"
    payload = {
        "prompt": args.prompt,
        "aspectRatio": args.aspect_ratio,
        "imageSize": args.image_size,
        "model": args.model or DEFAULT_IMAGE_MODEL,
    }

    response = requests.post(
        url, json=payload, headers=_auth_headers(args.api_key), timeout=IMAGE_TIMEOUT
    )
    result = _json_or_error(response)

    if not result.get("success"):
        return {"success": False, "error": result.get("error", "text-to-image failed")}

    return {
        "success": True,
        "tool_type": "text-to-image",
        "data": {"image_url": result.get("imageUrl")},
    }


def generate_image_to_image(api_base: str, args: argparse.Namespace) -> dict:
    url = f"{api_base}/api/skills/aoment-image-video/image-to-image"

    ref_list = args.reference_image
    if not ref_list:
        return {"success": False, "error": "image-to-image requires --reference-image"}

    data = {
        "prompt": args.prompt,
        "aspectRatio": args.aspect_ratio,
        "imageSize": args.image_size,
        "model": args.model or DEFAULT_IMAGE_MODEL,
    }
    files = {}

    reference_image = ref_list[0]
    if reference_image.startswith("http"):
        data["image"] = reference_image
    else:
        try:
            image_bytes = base64.b64decode(reference_image)
        except Exception as exc:
            return {"success": False, "error": f"invalid reference image base64: {exc}"}
        files["image"] = ("reference.png", image_bytes, "image/png")

    response = requests.post(
        url,
        data=data,
        files=files or None,
        headers=_auth_headers(args.api_key),
        timeout=IMAGE_TIMEOUT,
    )
    result = _json_or_error(response)

    if not result.get("success"):
        return {"success": False, "error": result.get("error", "image-to-image failed")}

    return {
        "success": True,
        "tool_type": "image-to-image",
        "data": {"image_url": result.get("imageUrl")},
    }


def generate_video(api_base: str, args: argparse.Namespace) -> dict:
    model = args.model or DEFAULT_VIDEO_MODEL
    if model not in SUPPORTED_VIDEO_MODELS:
        return {"success": False, "error": "unsupported_model"}

    endpoint = "video-seedance-2" if model == "video-seedance-2" else "video-v1-fast"
    url = f"{api_base}/api/skills/aoment-image-video/{endpoint}"
    duration = args.duration if args.duration is not None else (-1 if model == "video-seedance-2" else 8)

    data = {
        "prompt": args.prompt,
        "aspectRatio": args.aspect_ratio,
        "resolution": args.resolution,
        "duration": str(duration),
    }
    if model == "video-v1-fast":
        data["v1Orientation"] = args.orientation
        data["v1Resolution"] = args.resolution
    elif model == "video-seedance-2":
        data["seedanceReferenceMode"] = args.seedance_reference_mode

    files_list = []

    for index, ref in enumerate(args.reference_image or []):
        if ref.startswith("http"):
            data[f"referenceImageUrl_{index}"] = ref
        else:
            try:
                image_bytes = base64.b64decode(ref)
            except Exception as exc:
                return {"success": False, "error": f"invalid reference image base64: {exc}"}
            files_list.append(
                ("referenceImage", (f"reference-{index}.png", image_bytes, "image/png"))
            )

    for index, ref in enumerate(args.reference_video or []):
        if ref.startswith("http"):
            data[f"referenceVideoUrl_{index}"] = ref
        else:
            try:
                files_list.append(
                    ("referenceVideo", _media_file_tuple(ref, f"reference-video-{index}.mp4", "video/mp4"))
                )
            except Exception as exc:
                return {"success": False, "error": f"invalid reference video input: {exc}"}

    for index, ref in enumerate(args.reference_audio or []):
        if ref.startswith("http"):
            return {"success": False, "error": "reference audio URLs are not supported yet; use a local path or base64 data"}
        try:
            files_list.append(
                ("referenceAudio", _media_file_tuple(ref, f"reference-audio-{index}.mp3", "audio/mpeg"))
            )
        except Exception as exc:
            return {"success": False, "error": f"invalid reference audio input: {exc}"}

    response = requests.post(
        url,
        data=data,
        files=files_list or None,
        headers=_auth_headers(args.api_key),
        timeout=VIDEO_TIMEOUT,
    )
    result = _json_or_error(response)

    if not result.get("success"):
        return {"success": False, "error": result.get("error", "video generation failed")}

    return {
        "success": True,
        "tool_type": "video-generation",
        "data": {"video_url": result.get("videoUrl")},
    }


def recognize_image(api_base: str, args: argparse.Namespace) -> dict:
    url = f"{api_base}/api/skills/aoment-image-video/image-recognition"
    image_sources = (args.image or []) + (args.reference_image or [])
    if not image_sources:
        return {"success": False, "error": "image-recognition requires --image"}

    data = {
        "prompt": args.prompt,
        "model": args.model or DEFAULT_RECOGNITION_MODEL,
    }
    files_list = []

    for index, source in enumerate(image_sources):
        if source.startswith("http"):
            data[f"imageUrl_{index}"] = source
            continue

        try:
            files_list.append(
                ("images", _image_file_tuple(source, f"recognition-{index}.png"))
            )
        except Exception as exc:
            return {"success": False, "error": f"invalid image input: {exc}"}

    response = requests.post(
        url,
        data=data,
        files=files_list or None,
        headers=_auth_headers(args.api_key),
        timeout=IMAGE_TIMEOUT,
    )
    result = _json_or_error(response)

    if not result.get("success"):
        return {"success": False, "error": result.get("error", "image recognition failed")}

    return {
        "success": True,
        "tool_type": "image-recognition",
        "data": {"result_text": result.get("resultText")},
    }


def _read_local_version() -> str | None:
    try:
        skill_md = os.path.join(os.path.dirname(__file__), "..", "SKILL.md")
        with open(skill_md, "r", encoding="utf-8") as file:
            content = file.read()
        match = re.search(r"^version:\s*(.+)$", content, re.MULTILINE)
        return match.group(1).strip() if match else None
    except Exception:
        return None


def _compare_versions(local: str, remote: str) -> int:
    def parse(version: str) -> tuple:
        return tuple(int(part) for part in version.split("."))

    try:
        local_parts, remote_parts = parse(local), parse(remote)
        return (local_parts > remote_parts) - (local_parts < remote_parts)
    except Exception:
        return 0


def _check_version(api_base: str) -> None:
    local_version = _read_local_version()
    if not local_version:
        return

    try:
        response = requests.get(f"{api_base}/api/skills/aoment-image-video/version", timeout=5)
        data = response.json()
        if not data.get("success"):
            return
        remote_version = data.get("data", {}).get("version")
        if remote_version and _compare_versions(local_version, remote_version) < 0:
            json.dump(
                {
                    "success": False,
                    "error": "update_required",
                    "current_version": local_version,
                    "latest_version": remote_version,
                    "message": (
                        f"Skill version is outdated (current {local_version}, "
                        f"latest {remote_version}). Download the latest package and retry."
                    ),
                },
                sys.stdout,
                ensure_ascii=False,
                indent=2,
            )
            print()
            sys.exit(1)
    except Exception:
        return


def main():
    parser = argparse.ArgumentParser(description="aoment-image-video generation CLI")
    parser.add_argument("--api-key", "-k", required=True, help="Agent API Key")
    parser.add_argument(
        "--tool-type",
        "-t",
        required=True,
        choices=["text-to-image", "image-to-image", "video-generation", "image-recognition"],
        help="Tool type",
    )
    parser.add_argument("--prompt", "-p", default="", help="Prompt")
    parser.add_argument(
        "--model",
        default=None,
        help=(
            "Model ID. Image default: image-n2-fast. Video default: video-v1-fast. "
            "Recognition default: image-recognition-g2. Image models: image-n2-fast, image-n2, "
            "image-n1-fast, image-n1, image-o2, image-o2-pro. Video models: video-v1-fast, "
            "video-seedance-2. Recognition models: image-recognition-g1, image-recognition-g2."
        ),
    )
    parser.add_argument("--aspect-ratio", default="auto", help="Image/video aspect ratio")
    parser.add_argument("--image-size", default="1K", help="Image size: 1K, 2K, or 4K")
    parser.add_argument(
        "--reference-image",
        action="append",
        default=None,
        help="Reference image as Base64 data or URL. Can be specified multiple times for video or recognition.",
    )
    parser.add_argument(
        "--reference-video",
        action="append",
        default=None,
        help="Reference video as local path, Base64 data, or URL. Only supported by video-seedance-2.",
    )
    parser.add_argument(
        "--reference-audio",
        action="append",
        default=None,
        help="Reference audio as local path or Base64 data. Only supported by video-seedance-2.",
    )
    parser.add_argument(
        "--image",
        "-i",
        action="append",
        default=None,
        help="Image for recognition as a local path, URL, or Base64 data. Can be specified multiple times.",
    )
    parser.add_argument(
        "--orientation",
        default="portrait",
        choices=["portrait", "landscape"],
        help="Video orientation",
    )
    parser.add_argument(
        "--resolution",
        default="720p",
        choices=["480p", "720p", "1080p", "4k"],
        help="Video resolution",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=None,
        choices=[-1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        help="Video duration. video-v1-fast: 4, 6, or 8 seconds; video-seedance-2: 4-15 seconds or -1",
    )
    parser.add_argument(
        "--seedance-reference-mode",
        default="multimodal",
        choices=["multimodal", "first_frame", "first_last_frame"],
        help="Seedance 2.0 reference mode",
    )
    args = parser.parse_args()

    _check_version(API_BASE)

    if not args.prompt:
        has_video_reference = bool(args.reference_image or args.reference_video or args.reference_audio)
        requested_video_model = args.model or DEFAULT_VIDEO_MODEL
        if args.tool_type != "video-generation" or requested_video_model != "video-seedance-2" or not has_video_reference:
            json.dump(
                {"success": False, "error": "prompt is required"},
                sys.stdout,
                ensure_ascii=False,
                indent=2,
            )
            print()
            sys.exit(1)

    try:
        if args.tool_type == "text-to-image":
            result = generate_text_to_image(API_BASE, args)
        elif args.tool_type == "image-to-image":
            result = generate_image_to_image(API_BASE, args)
        elif args.tool_type == "image-recognition":
            result = recognize_image(API_BASE, args)
        else:
            result = generate_video(API_BASE, args)
    except requests.exceptions.Timeout:
        result = {"success": False, "error": f"request timed out for {args.tool_type}"}
    except requests.exceptions.RequestException as exc:
        result = {"success": False, "error": f"network request failed: {exc}"}
    except Exception as exc:
        result = {"success": False, "error": f"internal error: {exc}"}

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
