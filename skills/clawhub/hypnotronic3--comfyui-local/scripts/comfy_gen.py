#!/usr/bin/env python3
"""
comfy_gen.py — Secure ComfyUI image generation script.

Security design:
- Server address from COMFYUI_SERVER_ADDRESS env var ONLY (no CLI override)
- Workflows allowlisted to skill's workflows/ directory only
- Path traversal and absolute paths rejected
- All data passed as JSON over HTTP — no shell interpolation
- No arbitrary file reads

Usage:
    python3 comfy_gen.py --prompt "a mountain lake" [--workflow NAME] [--width W] [--height H] [--negative "blurry, low quality"]
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path, PurePosixPath

# ─── Configuration ───────────────────────────────────────────────────────────

# Server address: environment variable ONLY. No CLI override.
SERVER_ADDRESS = os.environ.get("COMFYUI_SERVER_ADDRESS", "").rstrip("/")

# Script directory (for resolving workflows and output)
SCRIPT_DIR = Path(__file__).parent.resolve()
SKILL_DIR = SCRIPT_DIR.parent
WORKFLOWS_DIR = SKILL_DIR / "workflows"
OUTPUT_DIR = SKILL_DIR / "output"

# ─── Security: validate workflow name ────────────────────────────────────────

def validate_workflow_name(name: str) -> Path:
    """Validate a workflow name and return the safe path.
    
    Rejects:
    - Names containing path separators (/ \\)
    - Names containing .. (path traversal)
    - Absolute paths
    - Names that resolve outside the workflows directory
    
    Returns:
        Path object to the workflow file within WORKFLOWS_DIR
    """
    # Reject any path separator or traversal
    if "/" in name or "\\" in name or ".." in name:
        print(f"ERROR: Invalid workflow name '{name}'. Only simple filenames are allowed (no paths, no '..').", file=sys.stderr)
        sys.exit(1)
    
    # Add .json extension if missing
    if not name.endswith(".json"):
        name = name + ".json"
    
    # Resolve and verify it's within the workflows directory
    workflow_path = (WORKFLOWS_DIR / name).resolve()
    
    if not str(workflow_path).startswith(str(WORKFLOWS_DIR.resolve())):
        print(f"ERROR: Workflow '{name}' resolves outside the workflows directory.", file=sys.stderr)
        sys.exit(1)
    
    if not workflow_path.exists():
        # List available workflows
        available = [f.stem for f in WORKFLOWS_DIR.glob("*.json")] if WORKFLOWS_DIR.exists() else []
        avail_str = ", ".join(available) if available else "(none found)"
        print(f"ERROR: Workflow '{name}' not found. Available: {avail_str}", file=sys.stderr)
        sys.exit(1)
    
    return workflow_path


def validate_server_url(url: str) -> str:
    """Validate that the server URL looks like a local network address.
    
    Rejects URLs that point to arbitrary external servers.
    Allows: localhost, 127.x.x.x, 10.x.x.x, 172.16-31.x.x, 192.168.x.x
    """
    from urllib.parse import urlparse
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    
    # Allow localhost
    if hostname in ("localhost", "127.0.0.1"):
        return url
    
    # Allow private IP ranges
    import ipaddress
    try:
        ip = ipaddress.ip_address(hostname)
        if ip.is_private:
            return url
    except ValueError:
        pass
    
    # Allow hostnames ending in .local (mDNS)
    if hostname.endswith(".local"):
        return url
    
    print(f"ERROR: Server address '{url}' is not a local/private network address. "
          f"COMFYUI_SERVER_ADDRESS must point to a local network address (localhost, 192.168.x.x, 10.x.x.x, etc.).",
          file=sys.stderr)
    sys.exit(1)


# ─── ComfyUI API ──────────────────────────────────────────────────────────────

def queue_prompt(server: str, workflow: dict) -> str:
    """Send a workflow to ComfyUI and return the prompt ID."""
    data = json.dumps({"prompt": workflow}).encode("utf-8")
    req = urllib.request.Request(
        f"{server}/prompt",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            response = json.loads(resp.read().decode("utf-8"))
            return response["prompt_id"]
    except urllib.error.URLError as e:
        print(f"ERROR: Cannot connect to ComfyUI at {server}: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyError:
        print(f"ERROR: Unexpected response from ComfyUI: {response}", file=sys.stderr)
        sys.exit(1)


def wait_for_completion(server: str, prompt_id: str, timeout: int = 300) -> dict:
    """Poll ComfyUI history until the prompt completes or times out."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            with urllib.request.urlopen(f"{server}/history/{prompt_id}", timeout=10) as resp:
                history = json.loads(resp.read().decode("utf-8"))
        except urllib.error.URLError:
            time.sleep(2)
            continue
        
        if prompt_id in history:
            return history[prompt_id]
        time.sleep(1)
    
    print(f"ERROR: Timed out waiting for ComfyUI prompt {prompt_id} after {timeout}s", file=sys.stderr)
    sys.exit(1)


def download_image(server: str, filename: str, subfolder: str, folder_type: str) -> Path:
    """Download a generated image from ComfyUI."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    params = urllib.parse.urlencode({
        "filename": filename,
        "subfolder": subfolder,
        "type": folder_type,
    })
    url = f"{server}/view?{params}"
    image_path = OUTPUT_DIR / filename
    
    try:
        urllib.request.urlretrieve(url, str(image_path))
    except urllib.error.URLError as e:
        print(f"ERROR: Cannot download image: {e}", file=sys.stderr)
        sys.exit(1)
    
    return image_path


# ─── Workflow injection ────────────────────────────────────────────────────────

def inject_prompt(workflow: dict, prompt: str, negative: str, seed: int, width: int, height: int) -> dict:
    """Inject prompt, negative prompt, seed, and dimensions into a workflow.
    
    Finds CLIPTextEncode nodes for prompt injection, KSampler nodes for seed,
    and EmptyLatentImage nodes for dimensions.
    """
    import copy
    workflow = copy.deepcopy(workflow)
    
    prompt_injected = False
    negative_injected = False
    
    for node_id, node in workflow.items():
        class_type = node.get("class_type", "")
        inputs = node.get("inputs", {})
        
        # Inject positive prompt into first CLIPTextEncode
        if class_type == "CLIPTextEncode" and not prompt_injected:
            inputs["text"] = prompt
            prompt_injected = True
        
        # Inject negative prompt into second CLIPTextEncode
        elif class_type == "CLIPTextEncode" and prompt_injected and not negative_injected:
            inputs["text"] = negative
            negative_injected = True
        
        # Inject seed into KSampler
        if "seed" in inputs:
            inputs["seed"] = seed
        
        # Inject dimensions into EmptyLatentImage
        if class_type == "EmptyLatentImage":
            if width is not None:
                inputs["width"] = width
            if height is not None:
                inputs["height"] = height
    
    return workflow


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    if not SERVER_ADDRESS:
        print("ERROR: COMFYUI_SERVER_ADDRESS environment variable is not set.", file=sys.stderr)
        print("Set it to your ComfyUI server address, e.g.:", file=sys.stderr)
        print("  export COMFYUI_SERVER_ADDRESS=http://127.0.0.1:8188", file=sys.stderr)
        print("  export COMFYUI_SERVER_ADDRESS=http://192.168.1.10:8188", file=sys.stderr)
        sys.exit(1)
    
    # Validate server URL is local/private
    validate_server_url(SERVER_ADDRESS)
    
    parser = argparse.ArgumentParser(
        description="Generate images using a local ComfyUI instance (secure version)."
    )
    parser.add_argument("--prompt", "-p", required=True, help="Image generation prompt")
    parser.add_argument("--negative", "-n", default="text, watermark, low quality, blurry, distorted",
                        help="Negative prompt (default: standard quality filters)")
    parser.add_argument("--workflow", "-w", default=None,
                        help="Workflow name (filename in workflows/ directory, without .json)")
    parser.add_argument("--width", type=int, default=None, help="Image width (overrides workflow default)")
    parser.add_argument("--height", type=int, default=None, help="Image height (overrides workflow default)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed (default: time-based)")
    parser.add_argument("--timeout", type=int, default=300, help="Timeout in seconds (default: 300)")
    
    args = parser.parse_args()
    seed = args.seed or int(time.time())
    
    # Load workflow
    if args.workflow:
        workflow_path = validate_workflow_name(args.workflow)
        with open(workflow_path, "r", encoding="utf-8") as f:
            workflow = json.load(f)
    else:
        # Use default simple workflow
        workflow = {
            "3": {
                "inputs": {
                    "seed": seed,
                    "steps": 20,
                    "cfg": 7,
                    "sampler_name": "euler",
                    "scheduler": "normal",
                    "denoise": 1,
                    "model": ["4", 0],
                    "positive": ["6", 0],
                    "negative": ["7", 0],
                    "latent_image": ["5", 0]
                },
                "class_type": "KSampler"
            },
            "4": {
                "inputs": {
                    "ckpt_name": "model.safetensors"
                },
                "class_type": "CheckpointLoaderSimple"
            },
            "5": {
                "inputs": {
                    "width": args.width or 1024,
                    "height": args.height or 1024,
                    "batch_size": 1
                },
                "class_type": "EmptyLatentImage"
            },
            "6": {
                "inputs": {
                    "text": args.prompt,
                    "clip": ["4", 1]
                },
                "class_type": "CLIPTextEncode"
            },
            "7": {
                "inputs": {
                    "text": args.negative,
                    "clip": ["4", 1]
                },
                "class_type": "CLIPTextEncode"
            },
            "8": {
                "inputs": {
                    "samples": ["3", 0],
                    "vae": ["4", 2]
                },
                "class_type": "VAEDecode"
            },
            "9": {
                "inputs": {
                    "filename_prefix": "OpenClaw",
                    "images": ["8", 0]
                },
                "class_type": "SaveImage"
            }
        }
    
    # Inject prompt into workflow
    workflow = inject_prompt(workflow, args.prompt, args.negative, seed, args.width, args.height)
    
    # Queue the prompt
    print(f"Generating image: '{args.prompt[:60]}{'...' if len(args.prompt) > 60 else ''}'")
    print(f"Server: {SERVER_ADDRESS}")
    print(f"Seed: {seed}")
    prompt_id = queue_prompt(SERVER_ADDRESS, workflow)
    print(f"Queued: {prompt_id}")
    
    # Wait for completion
    result = wait_for_completion(SERVER_ADDRESS, prompt_id, timeout=args.timeout)
    
    # Download images
    outputs = result.get("outputs", {})
    saved_paths = []
    for node_id, node_output in outputs.items():
        if "images" in node_output:
            for image_data in node_output["images"]:
                image_path = download_image(
                    SERVER_ADDRESS,
                    image_data["filename"],
                    image_data.get("subfolder", ""),
                    image_data.get("type", "output"),
                )
                saved_paths.append(image_path)
    
    if saved_paths:
        for path in saved_paths:
            print(f"MEDIA:{path}")
        print(f"Generated {len(saved_paths)} image(s)")
    else:
        print("ERROR: No images in output", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
