---
name: lux3d
description: "Use Lux3D to generate 3D models from images or text, or perform material repaint. Trigger when the user asks for image to 3D, text to 3D, prompt to 3D, create a 3D model from a description, create a 3D model from a description plus a reference image, or regenerate materials for an existing 3D model. Supports v1.0-pro, v2.0-preview, and v3.0-standard (default, with colored transparent material support, custom face count, and five-format output). For international users."
---

## What This Skill Does

Lux3D generates 3D assets through three documented asynchronous workflows:

- **Image to 3D**: submit an input image, poll the task, then download the ZIP result.
- **Text to 3D**: submit a prompt plus style, optionally with a reference image, poll the task, then download the ZIP result.
- **Material Repaint**: submit a reference image and a model URL, poll the task, then download the regenerated model result.

All workflows require `LUX3D_API_KEY`, which is the API key obtained from https://labs.aholo3d.com/api-keys.

## API Endpoint

- **International Endpoint**: `https://api.aholo3d.com/global`

## Concurrency Limits

Lux3D limits the number of generation tasks that can be in progress at the same time based on the account plan. Image-to-3D, text-to-3D, and material repaint tasks share the same account-level concurrency quota.

| Account Type | Maximum Concurrent In-progress Tasks |
| --- | :--: |
| Free account | 1 |
| Pro account | 2 |

If a task creation endpoint returns `GENERATION_CONCURRENCY_LIMIT_EXCEEDED`, the account has reached its concurrency limit. No new task is created and no credits are consumed. Wait for an existing task to finish before retrying, or upgrade the account for higher concurrency.

## Setup

### Apply for an API Key

- Register at: https://labs.aholo3d.com/api-keys

### Set Environment Variables

**Required:**

```bash
export LUX3D_API_KEY="your_api_key"
```

**Optional - Override Base URL:**

```bash
export LUX3D_BASE_URL="https://api.aholo3d.com/global"
```

**Optional - Specify Region:**

```bash
export LUX3D_REGION="international"
```

## Python Usage

### Image to 3D

```python
from skill.lux3d_client import generate_3d_model

result = generate_3d_model("path/to/input.jpg", version="v2.0-preview")
print(result)
```

Specify target face count (effective for v2.0-preview / v3.0-standard, range [10000, 500000], default 60000):

```python
result = generate_3d_model("path/to/input.jpg", version="v3.0-standard", face_count=100000)
print(result)
```

Or explicitly specify international region:

```python
result = generate_3d_model("path/to/input.jpg", region="international", version="v2.0-preview")
print(result)
```

### Text to 3D

```python
from skill.lux3d_client import generate_text_to_3d

result = generate_text_to_3d(
    "Generate a high-quality 3D wooden chair",
    style="photorealistic",
    version="v2.0-preview",
)
print(result)
```

Specify target face count (effective for v2.0-preview / v3.0-standard):

```python
result = generate_text_to_3d(
    "Generate a high-quality 3D wooden chair",
    style="photorealistic",
    version="v3.0-standard",
    face_count=100000,
)
print(result)
```

### Text plus Reference Image

```python
from skill.lux3d_client import generate_text_to_3d

result = generate_text_to_3d(
    "Generate a premium ceramic vase with a glossy glaze",
    style="glass",
    image_path="path/to/reference.png",
    version="v2.0-preview",
)
print(result)
```

### Low-level Task APIs

```python
from skill.lux3d_client import (
    create_task,
    create_text_to_3d_task,
    create_material_transfer_task,
    query_task_status,
    download_model,
)

image_task_id = create_task("path/to/input.jpg")
text_task_id = create_text_to_3d_task(
    "Generate a stylized toy robot",
    style="cartoon",
    image_path="path/to/reference.png",
)
material_task_id = create_material_transfer_task(
    "path/to/reference.png",
    mesh_url="https://example.com/model.glb",
)

image_model_url = query_task_status(image_task_id)
text_model_url = query_task_status(text_task_id)
material_model_url = query_task_status(material_task_id)

download_model(image_model_url, "image_to_3d.zip")
download_model(text_model_url, "text_to_3d.zip")
download_model(material_model_url, "material_transfer.zip")
```

### Material Repaint

```python
from skill.lux3d_client import generate_material_transfer

result = generate_material_transfer(
    "path/to/reference.png",
    mesh_url="https://example.com/model.glb",
    version="v2.0-preview",
)
print(result)
```

## Command Line Usage

### Region Selection

Use `--region` or `-r` to select the international endpoint (default):

```bash
python lux3d_client.py --region international image input.jpg output.zip
```

Or simply omit the region flag (international is default):

```bash
python lux3d_client.py image input.jpg output.zip
```

### Image to 3D

```bash
# Historical form (default region)
python lux3d_client.py input.jpg output.zip --version v3.0-standard

# Explicit command
python lux3d_client.py image input.jpg output.zip --version v3.0-standard
```

### Text to 3D

```bash
python lux3d_client.py text "Generate a high-quality 3D wooden chair" output.zip --style photorealistic --version v3.0-standard
```

### Text to 3D with Reference Image

```bash
python lux3d_client.py text "Generate a futuristic desk lamp" output.zip --style cyberpunk --image ref.png --version v3.0-standard
```

### Material Repaint

```bash
python lux3d_client.py material reference.png output.zip --mesh-url https://example.com/model.glb --version v3.0-standard
```

## Text-to-3D Styles

Supported styles:

| Style | Description |
|-------|-------------|
| `photorealistic` | Photorealistic quality |
| `cartoon` | Cartoon style |
| `anime` | Anime style |
| `hand_painted` | Hand-painted style |
| `cyberpunk` | Cyberpunk theme |
| `fantasy` | Fantasy style |
| `glass` | Glass material |

## Lux3D Version

You can specify the Lux3D version via the `version` parameter:

| Version | Description | Output Format |
|---------|-------------|---------------|
| `v3.0-standard` | **Default version**, adds colored transparent material support, reduces color deviation in generated models, improves material quality, preserves text and texture details, and adds custom face count support; supports five-format output | .zip + .glb + .usdz + _obj.zip + _fbx.zip |
| `v2.0-preview` | 2.0 model architecture with enhanced text and texture detail preservation, no transparent material support | .zip + .glb + .usdz |
| `v1.0-pro` | First-generation model with complete PBR material properties, supports transparent material generation | ZIP result |

**Important**: If the `version` parameter is not provided in the request, the system will default to `v3.0-standard`.
**Custom face count**: The `faceCount` parameter for image-to-3D / text-to-3D is supported by `v2.0-preview` / `v3.0-standard`; `v1.0-pro` ignores this parameter.

All generation APIs (image-to-3D, text-to-3D, material repaint) support the `version` parameter.

### Specify Version in Python

```python
# Image to 3D with version
result = generate_3d_model("path/to/input.jpg", version="v3.0-standard")

# Text to 3D with version
result = generate_text_to_3d(
    "Generate a high-quality 3D wooden chair",
    style="photorealistic",
    version="v3.0-standard",
)

# Material repaint with version
result = generate_material_transfer(
    "path/to/reference.png",
    mesh_url="https://example.com/model.glb",
    version="v3.0-standard",
)
```

### Specify Version in Command Line

```bash
# Image to 3D with version
python lux3d_client.py image input.jpg output.zip --version v3.0-standard

# Text to 3D with version
python lux3d_client.py text "Generate a high-quality 3D wooden chair" output.zip --style photorealistic --version v3.0-standard

# Material repaint with version
python lux3d_client.py material reference.png output.zip --mesh-url https://example.com/model.glb --version v3.0-standard
```

## Output

### v3.0-standard Multi-format Output

The `v3.0-standard` version supports five model format outputs. You can choose the appropriate format based on your use case:

| Format | Description | Use Case |
|--------|-------------|----------|
| **.zip** | Packaged result containing GLB model and separate PBR texture assets | Material editing or custom rendering pipelines |
| **.glb** | GLB model with embedded materials | Web rendering, Unity/Unreal engine import, most 3D software |
| **.usdz** | Apple AR native format | iOS/macOS AR Quick Look, ARKit applications |
| **_obj.zip** | OBJ + MTL + BaseColor textures packed in a ZIP | Common 3D software and DCC tools |
| **_fbx.zip** | FBX model and .fbm textures directory packed in a ZIP | Maya, 3ds Max, Blender, and other mainstream DCC software |

### Download Different Formats

After task completion, you can append parameters to the result URL to get different formats:

```python
# Get ZIP format (default)
zip_url = result['data']['url'] + '?format=zip'

# Get GLB format
glb_url = result['data']['url'] + '?format=glb'

# Get USDZ format
usdz_url = result['data']['url'] + '?format=usdz'

# Get OBJ zip format
obj_url = result['data']['url'] + '?format=obj_zip'

# Get FBX zip format
fbx_url = result['data']['url'] + '?format=fbx_zip'

# Download the corresponding format
download_model(glb_url, "model.glb")
```

**Note**: v3.0-standard returns 5 output slots in `outputs[]` in order, corresponding to .zip / .glb / .usdz / _obj.zip / _fbx.zip. zip and glb always return URLs; usdz / obj_zip / fbx_zip return URLs only when the corresponding optional export is requested, otherwise the slot returns `NOT_REQUESTED`. The default download is `outputs[0]` (the .zip packaged result). To switch to a different format, append the corresponding `?format=` parameter as shown. URL construction is consistent with v2.0-preview.

### v2.0-preview Multi-format Output

The `v2.0-preview` version supports three model format outputs:

| Format | Description | Use Case |
|--------|-------------|----------|
| **.zip** | Packaged result containing GLB model and separate PBR texture assets | Material editing or custom rendering pipelines |
| **.glb** | GLB model with embedded materials | Web rendering, Unity/Unreal engine import, most 3D software |
| **.usdz** | Apple AR native format | iOS/macOS AR Quick Look, ARKit applications |

### v1.0-pro Output

The `v1.0-pro` version returns a single ZIP result containing:
- A GLB model file
- Complete PBR texture assets (with transparent material support)

### Result Validity

All format download links are valid for **2 hours**, please download promptly.

## Notes

- Authentication uses `Authorization` header: `Authorization: <apiKey>`
- Image-to-3D, text-to-3D, and material repaint use different create endpoints
- All three workflows share the same task query endpoint
- `prompt` and `style` are required for text-to-3D
- `img` is optional for text-to-3D and should be a full data URL after encoding
- Material repaint requires `img` (reference image) and `meshUrl` (model GLB file URL) parameters

## Requirements

```bash
pip install Pillow requests
```

## References

- Lux3D Website: https://lux3d.aholo3d.com/
- API Key Application: https://labs.aholo3d.com/api-keys
- API contact: lux3d@qunhemail.com
