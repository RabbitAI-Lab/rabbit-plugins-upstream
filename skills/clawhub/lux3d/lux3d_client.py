"""
Lux3D client for image-to-3D and text-to-3D generation.
Supports both China (CN) and International API endpoints.
"""

import argparse
import base64
import io
import os
import sys
import time
import urllib.parse

import requests
from PIL import Image


# API endpoints
CN_HOST = "https://api.aholo3d.cn"
CN_PREFIX = ""
INTERNATIONAL_HOST = "https://api.aholo3d.com"
INTERNATIONAL_PREFIX = "/global"

# Default to international endpoint
DEFAULT_REGION = "international"

REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 2
DEFAULT_POLL_ATTEMPTS = 60
DEFAULT_POLL_INTERVAL = 15
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
SUPPORTED_STYLES = {
    "photorealistic",
    "cartoon",
    "anime",
    "hand_painted",
    "cyberpunk",
    "fantasy",
    "glass",
}

SUPPORTED_VERSIONS = {
    "v1.0-pro",
    "v2.0-preview",
    "v3.0-standard",
    "G1",
}

SUPPORTED_FORMATS = {
    "zip",
    "glb",
    "usdz",
    "obj_zip",
    "fbx_zip",
    "ply",
}

# v2.0-preview / v3.0-standard custom face count range; G1 uses the same
# public faceCount field with a higher default.
FACE_COUNT_MIN = 10000
FACE_COUNT_MAX = 500000


def get_api_key():
    """Read the API key from the environment each time it is needed."""
    return os.environ.get("LUX3D_API_KEY", "").strip()


def validate_api_key():
    """Validate the configured API key and return it."""
    api_key = get_api_key()
    if not api_key or api_key in {"your_lux3d_api_key", "your_invitation_code_here"}:
        raise ValueError(
            "[ERROR] API key not configured.\n"
            "Please set LUX3D_API_KEY to your Lux3D API key."
        )
    return api_key


def validate_image_path(image_path):
    """Validate that an image path exists and is readable."""
    if not image_path:
        raise ValueError("Image path cannot be empty")
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    if not os.path.isfile(image_path):
        raise ValueError(f"Path is not a file: {image_path}")
    try:
        with open(image_path, "rb") as file_obj:
            file_obj.read(1)
    except PermissionError as exc:
        raise PermissionError(f"Permission denied reading: {image_path}") from exc


def validate_output_path(output_path):
    """Validate that the output path can be written."""
    output_dir = os.path.dirname(output_path) or "."
    if not os.path.isdir(output_dir):
        raise ValueError(f"Output directory does not exist: {output_dir}")

    test_path = os.path.join(output_dir, ".lux3d_write_test")
    try:
        with open(test_path, "w", encoding="utf-8") as file_obj:
            file_obj.write("ok")
    except OSError as exc:
        raise PermissionError(f"Cannot write to directory: {output_dir}") from exc
    finally:
        if os.path.exists(test_path):
            os.remove(test_path)


def validate_prompt(prompt):
    """Validate the text prompt for text-to-3D generation."""
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    return prompt.strip()


def validate_style(style):
    """Validate the requested text-to-3D style. Returns default if not provided."""
    if style is None:
        return "photorealistic"
    if style not in SUPPORTED_STYLES:
        supported = ", ".join(sorted(SUPPORTED_STYLES))
        raise ValueError(f"Unsupported style '{style}'. Supported styles: {supported}")
    return style


def validate_version(version):
    """Validate the Lux3D version parameter."""
    if version not in SUPPORTED_VERSIONS:
        supported = ", ".join(sorted(SUPPORTED_VERSIONS))
        raise ValueError(f"Unsupported version '{version}'. Supported versions: {supported}")
    return version


def validate_face_count(faceCount):
    """Validate the target face count.

    Takes effect for Mesh only, not 3DGS, in v2.0-preview / v3.0-standard and G1. For v1.0-pro the
    server ignores this parameter and uses its own default. Valid range is
    [FACE_COUNT_MIN, FACE_COUNT_MAX]. When omitted, the server applies the
    version-specific default: 60000 for v2.0-preview / v3.0-standard and
    200000 for G1.
    """
    if faceCount is None:
        return None
    if not isinstance(faceCount, int) or isinstance(faceCount, bool):
        raise ValueError(f"faceCount must be an integer, got {type(faceCount).__name__}")
    if faceCount < FACE_COUNT_MIN or faceCount > FACE_COUNT_MAX:
        raise ValueError(
            f"faceCount {faceCount} is out of range [{FACE_COUNT_MIN}, {FACE_COUNT_MAX}]"
        )
    return faceCount


def normalize_output_formats(outputFormat):
    """Normalize a legacy string or the new list-form outputFormat."""
    if outputFormat is None:
        return None
    if isinstance(outputFormat, str):
        formats = [outputFormat]
    elif isinstance(outputFormat, (list, tuple, set)):
        formats = list(outputFormat)
    else:
        raise ValueError("outputFormat must be a string or a list of strings")
    normalized = []
    for requested_format in formats:
        validated_format = validate_format(requested_format)
        if validated_format not in normalized:
            normalized.append(validated_format)
    return normalized


def validate_format(outputFormat):
    """Validate the output format parameter."""
    if outputFormat not in SUPPORTED_FORMATS:
        supported = ", ".join(sorted(SUPPORTED_FORMATS))
        raise ValueError(f"Unsupported format '{outputFormat}'. Supported formats: {supported}")
    return outputFormat


def validate_version_format(version, outputFormat):
    """Validate that the requested output format is supported by the version."""
    formats = normalize_output_formats(outputFormat)
    if not formats:
        return
    effective_version = version or "v3.0-standard"
    if effective_version == "v1.0-pro" and any(item != "zip" for item in formats):
        raise ValueError("v1.0-pro supports only outputFormat=['zip']")
    if effective_version == "G1" and any(item not in {"zip", "glb", "ply"} for item in formats):
        raise ValueError("G1 supports only outputFormat values: zip, glb, ply")
    if effective_version != "G1" and "ply" in formats:
        raise ValueError("ply output is supported only by G1")


def output_extension(outputFormat):
    """Return the filesystem extension for a requested output format."""
    formats = normalize_output_formats(outputFormat)
    if not formats or len(formats) != 1:
        return "zip"
    outputFormat = formats[0]
    if outputFormat in {"obj_zip", "fbx_zip"}:
        return "zip"
    return outputFormat


def get_export_flags(outputFormat):
    """Build the unified list-form outputFormat request field."""
    formats = normalize_output_formats(outputFormat)
    return {"outputFormat": formats} if formats else {}


def default_download_format(outputFormat):
    """Select the format downloaded from a single or multi-format result."""
    formats = normalize_output_formats(outputFormat)
    return formats[0] if formats and len(formats) == 1 else "zip"


def validate_mesh_url(meshUrl):
    """Validate the mesh URL for material transfer."""
    if not meshUrl or not meshUrl.strip():
        raise ValueError("Mesh URL cannot be empty")
    normalized_url = meshUrl.strip()
    parsed_url = urllib.parse.urlparse(normalized_url)
    if parsed_url.scheme.lower() not in {"http", "https"} or not parsed_url.netloc:
        raise ValueError("Mesh URL must be an absolute HTTP or HTTPS URL")
    if not urllib.parse.unquote(parsed_url.path).lower().endswith(".glb"):
        raise ValueError("Mesh URL path must point to a .glb file")
    return normalized_url


def get_base_url(region=None):
    """
    Get the base URL for the specified region.
    
    Args:
        region: 'cn' for China, 'international' for global. 
                If None, uses LUX3D_BASE_URL env var or LUX3D_REGION env var or default.
    
    Returns:
        The base URL for the API endpoint.
    """
    # First check if LUX3D_BASE_URL is explicitly set
    env_base_url = os.environ.get("LUX3D_BASE_URL", "").strip()
    if env_base_url:
        return env_base_url.rstrip("/")
    
    # Determine region
    if region is None:
        region = os.environ.get("LUX3D_REGION", DEFAULT_REGION).strip().lower()
    
    if region in ("cn", "china", "domestic"):
        return CN_HOST + CN_PREFIX
    elif region in ("international", "global", "intl"):
        return INTERNATIONAL_HOST + INTERNATIONAL_PREFIX
    else:
        # Default to international for unknown regions
        return INTERNATIONAL_HOST + INTERNATIONAL_PREFIX


def normalize_base_url(base_url, region=None):
    """Normalize the configured base URL to a documented Lux3D API root."""
    if base_url:
        normalized = base_url.rstrip("/")
    else:
        normalized = get_base_url(region)
    
    # Handle case where user specifies the host without prefix
    if normalized == INTERNATIONAL_HOST:
        return normalized + INTERNATIONAL_PREFIX
    if normalized == CN_HOST:
        return normalized + CN_PREFIX
    
    return normalized


def get_auth_headers():
    """Get authorization headers using the API key."""
    api_key = validate_api_key()
    return {
        "Content-Type": "application/json",
        "Authorization": api_key,
    }


def secure_request(method, url, headers=None, data=None, timeout=None, retries=None, stream=False):
    """Perform an HTTP request with bounded retries."""
    request_headers = headers or {"Content-Type": "application/json"}
    timeout = timeout or REQUEST_TIMEOUT
    retries = retries or MAX_RETRIES
    last_error = None

    for attempt in range(retries):
        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=request_headers,
                json=data,
                timeout=timeout,
                stream=stream,
            )
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout as exc:
            last_error = f"Request timeout (attempt {attempt + 1}/{retries})"
            if attempt == retries - 1:
                break
            time.sleep(RETRY_DELAY)
        except requests.exceptions.RequestException as exc:
            last_error = f"Request failed: {exc}"
            if attempt == retries - 1:
                break
            time.sleep(RETRY_DELAY)

    raise Exception(f"Request failed after {retries} attempts: {last_error}")


def image_to_data_url(image_path):
    """Convert an image file to a data URL while preserving PNG transparency."""
    validate_image_path(image_path)
    image = Image.open(image_path)
    buffer = io.BytesIO()
    has_alpha = image.mode in ("RGBA", "LA") or "transparency" in image.info
    if image.format == "PNG" or has_alpha:
        image.save(buffer, format="PNG")
        mime_type = "image/png"
    else:
        if image.mode != "RGB":
            image = image.convert("RGB")
        image.save(buffer, format="JPEG", quality=85)
        mime_type = "image/jpeg"
    image_bytes = buffer.getvalue()
    encoded = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def ensure_success(result):
    """Validate the Lux3D API response format used in the documentation."""
    code = result.get("c")
    if code not in (None, "", 0, "0"):
        message = result.get("m") or "unknown error"
        raise Exception(f"API error: {message} (code={code})")

    legacy_code = result.get("code")
    if code is None and legacy_code not in (None, "", 0, "0"):
        message = result.get("message") or "unknown error"
        raise Exception(f"API error: {message} (code={legacy_code})")

    return result


def submit_task(path, payload, base_url=None, region=None):
    """Submit a Lux3D generation task and return its taskid."""
    url = normalize_base_url(base_url, region) + path
    headers = get_auth_headers()
    response = secure_request("POST", url, headers=headers, data=payload)

    try:
        result = response.json()
    except ValueError as exc:
        raise Exception(f"Invalid JSON response: {response.text}") from exc

    ensure_success(result)
    task_id = result.get("d")
    if task_id in (None, ""):
        raise Exception(f"Missing task id in response: {result}")
    return str(task_id)


def create_task(
    image_path,
    base_url=None,
    region=None,
    lux3dBizType=None,
    version=None,
    faceCount=None,
    outputFormat=None,
    imagePaths=None,
    enablePbr=None,
    textureSize=None,
):
    """Submit an image-to-3D task.

    Args:
        imagePaths: Optional additional local image paths for G1 multi-view.
        faceCount: Optional Mesh face count. Does not affect 3DGS. Takes effect for
            v2.0-preview / v3.0-standard / G1; v1.0-pro ignores this parameter.
        enablePbr: G1 texture/PBR switch. Defaults to true for G1.
        textureSize: G1 texture size. Defaults to 1000 for G1.
    """
    version = validate_version(version) if version is not None else None
    additional_paths = [imagePaths] if isinstance(imagePaths, str) else list(imagePaths or [])
    paths = [image_path] + additional_paths
    paths = list(dict.fromkeys(path for path in paths if path))
    if not paths:
        raise ValueError("At least one image path is required")
    if len(paths) > 1 and version != "G1":
        raise ValueError("Multiple image paths are supported only by G1")
    if len(paths) > 32:
        raise ValueError("G1 supports at most 32 image paths")
    encoded_images = [image_to_data_url(path) for path in paths]
    payload = {"imgs": encoded_images} if len(encoded_images) > 1 else {"img": encoded_images[0]}
    if lux3dBizType is not None:
        payload["lux3dBizType"] = lux3dBizType
    if version is not None:
        payload["version"] = version
    validate_version_format(version, outputFormat)
    if faceCount is not None:
        payload["faceCount"] = validate_face_count(faceCount)
    payload.update(get_export_flags(outputFormat))
    if enablePbr is not None:
        if version != "G1":
            raise ValueError("enablePbr is supported only by G1")
        payload["enablePbr"] = bool(enablePbr)
    if textureSize is not None:
        if version != "G1":
            raise ValueError("textureSize is supported only by G1")
        if not isinstance(textureSize, int) or isinstance(textureSize, bool) or textureSize <= 0:
            raise ValueError("textureSize must be a positive integer")
        payload["textureSize"] = textureSize
    return submit_task("/lux3d/v1/generate/img-to-3d/task/create", payload, base_url=base_url, region=region)


def create_text_to_3d_task(
    prompt,
    style=None,
    image_path=None,
    base_url=None,
    region=None,
    lux3dBizType=None,
    version=None,
    faceCount=None,
    outputFormat=None,
    enablePbr=None,
    textureSize=None,
):
    """Submit a text-to-3D task with an optional reference image.

    Args:
        faceCount: Optional Mesh face count. Does not affect 3DGS. Takes effect for
            v2.0-preview / v3.0-standard / G1; v1.0-pro ignores this parameter.
        enablePbr: G1 texture/PBR switch. Defaults to true for G1.
        textureSize: G1 texture size. Defaults to 1000 for G1.
    """
    payload = {
        "prompt": validate_prompt(prompt),
    }
    if style is not None:
        payload["style"] = validate_style(style)
    if image_path:
        payload["img"] = image_to_data_url(image_path)
    if lux3dBizType is not None:
        payload["lux3dBizType"] = lux3dBizType
    if version is not None:
        payload["version"] = validate_version(version)
    validate_version_format(version, outputFormat)
    if faceCount is not None:
        payload["faceCount"] = validate_face_count(faceCount)
    payload.update(get_export_flags(outputFormat))
    if enablePbr is not None:
        if version != "G1":
            raise ValueError("enablePbr is supported only by G1")
        payload["enablePbr"] = bool(enablePbr)
    if textureSize is not None:
        if version != "G1":
            raise ValueError("textureSize is supported only by G1")
        if not isinstance(textureSize, int) or isinstance(textureSize, bool) or textureSize <= 0:
            raise ValueError("textureSize must be a positive integer")
        payload["textureSize"] = textureSize
    return submit_task("/lux3d/v1/generate/text-to-3d/task/create", payload, base_url=base_url, region=region)


def create_material_transfer_task(
    image_path,
    meshUrl,
    base_url=None,
    region=None,
    version=None,
    outputFormat=None,
):
    """Submit a material transfer task to regenerate materials for an existing model."""
    payload = {
        "img": image_to_data_url(image_path),
        "meshUrl": validate_mesh_url(meshUrl),
    }
    if version is not None:
        payload["version"] = validate_version(version)
        if version == "G1":
            raise ValueError("Material transfer is not supported by G1")
    validate_version_format(version, outputFormat)
    payload.update(get_export_flags(outputFormat))
    return submit_task("/lux3d/v1/generate/material-transfer/task/create", payload, base_url=base_url, region=region)


def query_task_status(task_id, base_url=None, region=None, max_attempts=DEFAULT_POLL_ATTEMPTS, interval=DEFAULT_POLL_INTERVAL):
    """Poll a Lux3D task until completion and return the download URLs.
    
    Returns:
        A dictionary mapping format names to download URLs, e.g.
        {'zip': '...', 'glb': '...', 'usdz': '...', 'obj_zip': '...', 'fbx_zip': '...', 'ply': '...'}
        Or a single URL string for backward compatibility with older API versions.
    """
    for _ in range(max_attempts):
        url = normalize_base_url(base_url, region) + "/lux3d/v1/generate/task/get?taskid=" + urllib.parse.quote(str(task_id))
        headers = get_auth_headers()
        response = secure_request("GET", url, headers=headers)

        try:
            result = response.json()
        except ValueError as exc:
            raise Exception(f"Invalid JSON response: {response.text}") from exc

        ensure_success(result)
        task_data = result.get("d") or {}
        status = task_data.get("status")

        if status == 3:
            outputs = task_data.get("outputs") or []
            
            # Parse multiple outputs with different formats based on URL
            format_urls = {}
            for output in outputs:
                content = output.get("content", "").strip()
                if not content or content.upper() == "NOT_REQUESTED":
                    continue

                # Extract format from URL filename. Check obj/fbx zip before generic zip.
                content_lower = content.lower()
                if "_obj.zip" in content_lower:
                    format_urls["obj_zip"] = content
                elif "_fbx.zip" in content_lower:
                    format_urls["fbx_zip"] = content
                elif ".glb" in content_lower:
                    format_urls["glb"] = content
                elif ".usdz" in content_lower:
                    format_urls["usdz"] = content
                elif ".ply" in content_lower:
                    format_urls["ply"] = content
                elif ".zip" in content_lower:
                    format_urls["zip"] = content
            
            # If we found multiple formats, return the dictionary
            if format_urls:
                return format_urls
            
            # Fallback: return the first output URL for backward compatibility
            for output in outputs:
                content = output.get("content", "").strip()
                if content and content.upper() != "NOT_REQUESTED":
                    return content
            
            raise Exception(f"Task succeeded without output content: {result}")
        if status == 4:
            raise Exception(f"Task execution failed: {result}")

        time.sleep(interval)

    raise Exception("Task timeout")


def download_model(model_url, output_path, outputFormat=None):
    """
    Download the generated model file to the target path.
    
    Args:
        model_url: Can be either:
                   - A string URL (backward compatibility with single format API)
                   - A dictionary mapping format names to URLs (new multi-format API)
        output_path: The path to save the downloaded file.
        outputFormat: Optional single output format. Defaults to 'zip' when
                       model_url is a dictionary.
    
    Returns:
        The size of the downloaded file in bytes.
    """
    validate_output_path(output_path)
    
    # Handle multi-format API response (dict)
    if isinstance(model_url, dict):
        outputFormat = default_download_format(outputFormat)

        outputFormat = validate_format(outputFormat)
        if outputFormat not in model_url:
            available_formats = ", ".join(sorted(model_url.keys()))
            raise ValueError(f"Format '{outputFormat}' not available. Available formats: {available_formats}")
        
        url_to_download = model_url[outputFormat]
    
    # Handle single format API response (string)
    else:
        url_to_download = model_url
        if outputFormat is not None:
            validate_format(default_download_format(outputFormat))
    
    response = secure_request("GET", url_to_download, headers={}, stream=True)
    total_size = 0
    with open(output_path, "wb") as file_obj:
        for chunk in response.iter_content(chunk_size=DOWNLOAD_CHUNK_SIZE):
            if chunk:
                file_obj.write(chunk)
                total_size += len(chunk)
    response.close()
    return total_size


def download_requested_models(model_url, output_path, outputFormat=None):
    """Download every requested format and return ``[(path, size), ...]``."""
    formats = normalize_output_formats(outputFormat)
    if not formats or len(formats) == 1:
        selected_format = formats[0] if formats else None
        size = download_model(model_url, output_path, outputFormat=selected_format)
        return [(output_path, size)]
    if not isinstance(model_url, dict):
        raise ValueError("Multiple output formats require multiple artifact URLs")

    output_base, _ = os.path.splitext(output_path)
    downloads = []
    for selected_format in formats:
        extension = output_extension(selected_format)
        selected_path = f"{output_base}_{selected_format}.{extension}"
        size = download_model(model_url, selected_path, outputFormat=selected_format)
        downloads.append((selected_path, size))
    return downloads


def generate_3d_model(
    image_path,
    output_path=None,
    base_url=None,
    region=None,
    lux3dBizType=None,
    version=None,
    faceCount=None,
    outputFormat=None,
    max_attempts=DEFAULT_POLL_ATTEMPTS,
    interval=DEFAULT_POLL_INTERVAL,
    imagePaths=None,
    enablePbr=None,
    textureSize=None,
):
    """Run the full image-to-3D workflow."""
    validate_api_key()

    print("=== Submitting image-to-3D task ===")
    task_id = create_task(
        image_path,
        base_url=base_url,
        region=region,
        lux3dBizType=lux3dBizType,
        version=version,
        faceCount=faceCount,
        outputFormat=outputFormat,
        imagePaths=imagePaths,
        enablePbr=enablePbr,
        textureSize=textureSize,
    )
    print(f"Task ID: {task_id}")

    print("\n=== Querying task result ===")
    model_url = query_task_status(
        task_id,
        base_url=base_url,
        region=region,
        max_attempts=max_attempts,
        interval=interval,
    )
    print(f"Model URL: {model_url}")

    # Determine output filename based on format
    if output_path:
        output_name = output_path
    else:
        ext = output_extension(outputFormat)
        output_name = image_path.rsplit(".", 1)[0] + f"_3d.{ext}"
    
    print("\n=== Downloading model ===")
    downloads = download_requested_models(model_url, output_name, outputFormat=outputFormat)
    for downloaded_path, size in downloads:
        print(f"Downloaded: {downloaded_path} ({size} bytes)")
    return downloads[0][0] if len(downloads) == 1 else [item[0] for item in downloads]


def generate_text_to_3d(
    prompt,
    output_path=None,
    style=None,
    image_path=None,
    base_url=None,
    region=None,
    lux3dBizType=None,
    version=None,
    faceCount=None,
    outputFormat=None,
    max_attempts=DEFAULT_POLL_ATTEMPTS,
    interval=DEFAULT_POLL_INTERVAL,
    enablePbr=None,
    textureSize=None,
):
    """Run the full text-to-3D workflow."""
    validate_api_key()

    print("=== Submitting text-to-3D task ===")
    task_id = create_text_to_3d_task(
        prompt,
        style=style,
        image_path=image_path,
        base_url=base_url,
        region=region,
        lux3dBizType=lux3dBizType,
        version=version,
        faceCount=faceCount,
        outputFormat=outputFormat,
        enablePbr=enablePbr,
        textureSize=textureSize,
    )
    print(f"Task ID: {task_id}")

    print("\n=== Querying task result ===")
    model_url = query_task_status(
        task_id,
        base_url=base_url,
        region=region,
        max_attempts=max_attempts,
        interval=interval,
    )
    print(f"Model URL: {model_url}")

    # Determine output filename based on format
    if output_path:
        output_name = output_path
    else:
        ext = output_extension(outputFormat)
        output_name = f"lux3d_text_to_3d.{ext}"
    
    print("\n=== Downloading model ===")
    downloads = download_requested_models(model_url, output_name, outputFormat=outputFormat)
    for downloaded_path, size in downloads:
        print(f"Downloaded: {downloaded_path} ({size} bytes)")
    return downloads[0][0] if len(downloads) == 1 else [item[0] for item in downloads]


def generate_material_transfer(
    image_path,
    meshUrl,
    output_path=None,
    base_url=None,
    region=None,
    version=None,
    outputFormat=None,
    max_attempts=DEFAULT_POLL_ATTEMPTS,
    interval=DEFAULT_POLL_INTERVAL,
):
    """Run the full material transfer workflow."""
    validate_api_key()

    print("=== Submitting material transfer task ===")
    task_id = create_material_transfer_task(
        image_path,
        meshUrl,
        base_url=base_url,
        region=region,
        version=version,
        outputFormat=outputFormat,
    )
    print(f"Task ID: {task_id}")

    print("\n=== Querying task result ===")
    model_url = query_task_status(
        task_id,
        base_url=base_url,
        region=region,
        max_attempts=max_attempts,
        interval=interval,
    )
    print(f"Model URL: {model_url}")

    # Determine output filename based on format
    if output_path:
        output_name = output_path
    else:
        ext = output_extension(outputFormat)
        output_name = f"lux3d_material_transfer.{ext}"
    
    print("\n=== Downloading model ===")
    downloads = download_requested_models(model_url, output_name, outputFormat=outputFormat)
    for downloaded_path, size in downloads:
        print(f"Downloaded: {downloaded_path} ({size} bytes)")
    return downloads[0][0] if len(downloads) == 1 else [item[0] for item in downloads]


def build_parser():
    """Build the CLI parser."""
    parser = argparse.ArgumentParser(
        description="Lux3D client for image-to-3D and text-to-3D generation. "
                    "Supports both China (CN) and International API endpoints."
    )
    parser.add_argument(
        "--region", "-r",
        choices=["cn", "international"],
        default=None,
        help="API region: 'cn' for China (api.aholo3d.cn), 'international' for global (api.aholo3d.com/global). "
             "Can also be set via LUX3D_REGION environment variable. Default: international"
    )
    parser.add_argument(
        "--base-url",
        default=None,
        help="Override API base URL. Can also be set via LUX3D_BASE_URL environment variable."
    )
    subparsers = parser.add_subparsers(dest="command")

    image_parser = subparsers.add_parser("image", help="Generate a 3D model from an image.")
    image_parser.add_argument("image_path", help="Input image path")
    image_parser.add_argument("output_path", nargs="?", help="Output file path")
    image_parser.add_argument("--biz-type", dest="lux3dBizType", help="Optional business type")
    image_parser.add_argument("--version", default=None, help="Lux3D version: v3.0-standard (default), v2.0-preview, v1.0-pro or G1")
    image_parser.add_argument("--face-count", dest="faceCount", type=int, default=None,
                              help=f"Mesh face count only (not 3DGS), effective for v2.0-preview / v3.0-standard / G1. Range: [{FACE_COUNT_MIN}, {FACE_COUNT_MAX}]")
    image_parser.add_argument("--format", dest="outputFormat", action="append", choices=["zip", "glb", "usdz", "obj_zip", "fbx_zip", "ply"], default=None,
                              help="Output format; repeat for a list. G1 supports zip, glb and ply.")
    image_parser.add_argument("--image-view", dest="imageViews", action="append", default=None,
                              help="Additional local image path for G1 multi-view input; repeat up to 31 times.")
    image_parser.add_argument("--enable-pbr", dest="enablePbr", action="store_true", default=None,
                              help="Enable G1 textured/PBR mesh output.")
    image_parser.add_argument("--no-pbr", dest="enablePbr", action="store_false",
                              help="Disable G1 textured/PBR mesh output and return a white mesh.")
    image_parser.add_argument("--texture-size", dest="textureSize", type=int, default=None,
                              help="G1 texture size; defaults to 1000.")
    image_parser.add_argument("--max-attempts", type=int, default=DEFAULT_POLL_ATTEMPTS)
    image_parser.add_argument("--interval", type=int, default=DEFAULT_POLL_INTERVAL)

    text_parser = subparsers.add_parser("text", help="Generate a 3D model from text.")
    text_parser.add_argument("prompt", help="Text prompt")
    text_parser.add_argument("output_path", nargs="?", help="Output file path")
    text_parser.add_argument("--style", default=None, help="Generation style (default: photorealistic)")
    text_parser.add_argument("--image", dest="image_path", help="Optional reference image path")
    text_parser.add_argument("--biz-type", dest="lux3dBizType", help="Optional business type")
    text_parser.add_argument("--version", default=None, help="Lux3D version: v3.0-standard (default), v2.0-preview, v1.0-pro or G1")
    text_parser.add_argument("--face-count", dest="faceCount", type=int, default=None,
                              help=f"Mesh face count only (not 3DGS), effective for v2.0-preview / v3.0-standard / G1. Range: [{FACE_COUNT_MIN}, {FACE_COUNT_MAX}]")
    text_parser.add_argument("--format", dest="outputFormat", action="append", choices=["zip", "glb", "usdz", "obj_zip", "fbx_zip", "ply"], default=None,
                              help="Output format; repeat for a list. G1 supports zip, glb and ply.")
    text_parser.add_argument("--enable-pbr", dest="enablePbr", action="store_true", default=None,
                              help="Enable G1 textured/PBR mesh output.")
    text_parser.add_argument("--no-pbr", dest="enablePbr", action="store_false",
                              help="Disable G1 textured/PBR mesh output and return a white mesh.")
    text_parser.add_argument("--texture-size", dest="textureSize", type=int, default=None,
                              help="G1 texture size; defaults to 1000.")
    text_parser.add_argument("--max-attempts", type=int, default=DEFAULT_POLL_ATTEMPTS)
    text_parser.add_argument("--interval", type=int, default=DEFAULT_POLL_INTERVAL)

    material_parser = subparsers.add_parser("material", help="Regenerate materials for an existing 3D model.")
    material_parser.add_argument("image_path", help="Reference image path for material")
    material_parser.add_argument("output_path", nargs="?", help="Output file path")
    material_parser.add_argument("--mesh-url", dest="meshUrl", required=True,
                                 help="URL of the GLB model file")
    material_parser.add_argument("--version", default=None, help="Lux3D version: v3.0-standard (default), v2.0-preview or v1.0-pro")
    material_parser.add_argument("--format", dest="outputFormat", action="append", choices=["zip", "glb", "usdz", "obj_zip", "fbx_zip"], default=None,
                               help="Output format; repeat for a list.")
    material_parser.add_argument("--max-attempts", type=int, default=DEFAULT_POLL_ATTEMPTS)
    material_parser.add_argument("--interval", type=int, default=DEFAULT_POLL_INTERVAL)

    return parser


def main():
    """CLI entrypoint."""
    parser = build_parser()
    commands = ("image", "text", "material")
    has_legacy_input = (len(sys.argv) >= 2
                        and not sys.argv[1].startswith("-")
                        and sys.argv[1] not in commands)
    is_legacy_call = has_legacy_input and (len(sys.argv) == 2 or (
            len(sys.argv) >= 3 and sys.argv[2] not in commands))
    if is_legacy_call:
        # Historical form: python lux3d_client.py input.jpg [output.zip]
        default_args = parser.parse_args([])
        image_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) >= 3 else None
        result = generate_3d_model(
            image_path,
            output_path=output_path,
            region=default_args.region,
            base_url=default_args.base_url,
        )
        print(f"\n[SUCCESS] Model saved to: {result}")
        return

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        raise SystemExit(1)

    if args.command == "image":
        result = generate_3d_model(
            args.image_path,
            output_path=args.output_path,
            base_url=args.base_url,
            region=args.region,
            lux3dBizType=args.lux3dBizType,
            version=args.version,
            faceCount=args.faceCount,
            outputFormat=args.outputFormat,
            imagePaths=args.imageViews,
            enablePbr=args.enablePbr,
            textureSize=args.textureSize,
            max_attempts=args.max_attempts,
            interval=args.interval,
        )
        print(f"\n[SUCCESS] Model saved to: {result}")
        return

    if args.command == "text":
        result = generate_text_to_3d(
            args.prompt,
            output_path=args.output_path,
            style=args.style,
            image_path=args.image_path,
            base_url=args.base_url,
            region=args.region,
            lux3dBizType=args.lux3dBizType,
            version=args.version,
            faceCount=args.faceCount,
            outputFormat=args.outputFormat,
            enablePbr=args.enablePbr,
            textureSize=args.textureSize,
            max_attempts=args.max_attempts,
            interval=args.interval,
        )
        print(f"\n[SUCCESS] Model saved to: {result}")
        return

    if args.command == "material":
        result = generate_material_transfer(
            args.image_path,
            meshUrl=args.meshUrl,
            output_path=args.output_path,
            base_url=args.base_url,
            region=args.region,
            version=args.version,
            outputFormat=args.outputFormat,
            max_attempts=args.max_attempts,
            interval=args.interval,
        )
        print(f"\n[SUCCESS] Model saved to: {result}")
        return

    parser.print_help()
    raise SystemExit(1)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"\n[ERROR] {exc}")
        raise SystemExit(1)
    except Exception as exc:
        print(f"\n[ERROR] {exc}")
        raise SystemExit(1)
