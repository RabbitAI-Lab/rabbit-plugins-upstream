#!/usr/bin/env python3
"""
image_with_comfyui.py - Call a ComfyUI server for T2I / I2I / I2V media generation.

Modes:
    t2i      Text-to-Image (Z-Image or SD3.5 Medium via --model)
    i2i      Image-to-Image / edit (Qwen Image Edit)
    wan2.2   Image-to-Video (Wan2.2)
    i2m      Image-to-3D-Mesh (Pixal3D / Trellis2, default -> GLB; the source
             image feeds straight in, then generates the mesh and zips it)
    hyi2m    Image-to-3D-Mesh (Hunyuan 3D v2.1 -> GLB; extracts the main
             character first via i2i or rembg, then generates the mesh,
             scales the GLB x3000 for delivery, and zips it)
    test     Quick health check

Usage:
    python3 image_with_comfyui.py t2i --prompt "..." [--aspect 1:1] [--model z-image]
    python3 image_with_comfyui.py t2i --prompt "..." --model sd35
    python3 image_with_comfyui.py i2i --prompt "..." --image image.jpg
    python3 image_with_comfyui.py wan2.2 --prompt "..." --image image.jpg
    python3 image_with_comfyui.py i2m --image character.jpg [--scale 1]
    python3 image_with_comfyui.py hyi2m --image character.jpg [--extract i2i|rembg|none] [--scale 3000]
    python3 image_with_comfyui.py test

Configuration:
    Reads config from this SKILL's config.json (relative to this script).
    The endpoint is user-defined: COMFYUI_URL env var, or comfyui_url in
    config.json (bundled default http://127.0.0.1:8188). If no ComfyUI server
    is reachable, the script exits with configuration instructions.
    Environment overrides:
      COMFYUI_URL            endpoint (non-local hosts print a warning)
      COMFYUI_TIMEOUT        global generation timeout in seconds
      COMFYUI_POLL_INTERVAL  polling interval in seconds
      COMFYUI_OUTPUT_DIR     output directory

Data flow:
    Prompts and workflow JSON are sent to the configured endpoint; i2i/i2v
    additionally upload the full source image. Generated media is written
    to the output directory (config output_dir / COMFYUI_OUTPUT_DIR).
"""

import argparse
import base64
import io
import json
import os
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
import http.client
import mimetypes
from email.encoders import encode_base64
from io import BytesIO
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_CONFIG = SCRIPT_DIR / "config.json"

# Workspace / config directory detection.
#
# The agent's OpenClaw workspace is provided by the runtime via the
# OPENCLAW_WORKSPACE_DIR environment variable (the gateway sets that exact
# name for every agent turn). The old code read "OPENCLAW_WORKSPACE" (no
# trailing _DIR) -- a variable that never existed -- so the fallback to the
# upward filesystem scan always ran and could land output in the wrong
# workspace. We match the real env name and fall back to the OpenClaw
# config-dir resolution instead of guessing by walking parent directories.
import os

def resolve_config_dir(env: "dict | None" = None, homedir: "str | None" = None) -> Path:
    """Replicate OpenClaw's config-dir resolution (resolveConfigDir).

    Precedence (matching the OpenClaw source):
      1. OPENCLAW_STATE_DIR      -> use this as the base directory
      2. OPENCLAW_CONFIG_PATH    -> directory containing that config file
      3. otherwise               -> <home>/.openclaw
    """
    if env is None:
        env = os.environ
    if homedir is None:
        homedir = os.path.expanduser("~")
    override = (env.get("OPENCLAW_STATE_DIR") or "").strip()
    if override:
        return Path(override).expanduser().resolve()
    config_path = (env.get("OPENCLAW_CONFIG_PATH") or "").strip()
    if config_path:
        return Path(config_path).expanduser().resolve().parent
    return Path(homedir).expanduser().resolve() / ".openclaw"

def find_workspace_dir(env: "dict | None" = None) -> Path:
    """Find the agent's OpenClaw workspace directory.

    1. Honour OPENCLAW_WORKSPACE_DIR when the runtime provides it -- this is
       the agent's real workspace on a normal gateway turn.
    2. Otherwise fall back to the resolved config dir, so output lands under
       <config-dir>/media/comfyui (e.g. ~/.openclaw/media/comfyui) instead of
       scanning the filesystem and possibly hitting the wrong workspace.
    """
    if env is None:
        env = os.environ
    ws = (env.get("OPENCLAW_WORKSPACE_DIR") or "").strip()
    if ws:
        return Path(ws).expanduser().resolve()
    return resolve_config_dir(env)

WORKSPACE_DIR = find_workspace_dir()

def _apply_timeout_override(cfg: dict, timeout: int) -> None:
    """Apply a global generation timeout override to every model entry."""
    cfg["timeout_seconds"] = timeout
    for section in ("image", "video"):
        for model in cfg.get(section, {}).values():
            if isinstance(model, dict):
                model["timeout_seconds"] = timeout


def _endpoint_disclosure(cfg: dict) -> None:
    """Disclose data flow when the endpoint is non-local.

    Prints a one-time warning (stderr) if comfyui_url points at a
    non-local host, so users are aware prompts and (for i2i/i2v) full
    source images will be transmitted there.
    """
    url = cfg.get("comfyui_url", "")
    try:
        parsed = urllib.parse.urlparse(url)
    except ValueError:
        return
    host = (parsed.hostname or "").lower()
    if host in ("127.0.0.1", "localhost", "local", "0.0.0.0", "::1"):
        return
    scheme = (parsed.scheme or "http").upper()
    print(
        f"⚠️  Non-local ComfyUI endpoint: {url} — prompts and (for i2i/i2v) full "
        f"source images will be sent to this host via {scheme}. "
        "Only point COMFYUI_URL at a server you control.",
        file=sys.stderr,
    )


def load_config() -> dict:
    """Load config from config.json, then apply env overrides."""
    config_path = SCRIPT_DIR / "config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    env_url = os.environ.get("COMFYUI_URL")
    if env_url:
        cfg["comfyui_url"] = env_url
    env_poll = os.environ.get("COMFYUI_POLL_INTERVAL")
    if env_poll:
        cfg["poll_interval_seconds"] = int(env_poll)
    env_timeout = os.environ.get("COMFYUI_TIMEOUT")
    if env_timeout:
        _apply_timeout_override(cfg, int(env_timeout))
    env_out = os.environ.get("COMFYUI_OUTPUT_DIR")
    if env_out:
        cfg["output_dir"] = env_out
    env_keep = os.environ.get("COMFYUI_KEEP_MODELS_RESIDENT")
    if env_keep is not None:
        cfg["keep_models_resident"] = env_keep.strip().lower() in ("1", "true", "yes", "on")
    # ComfyUI API key (Bearer auth). Env wins over config.json when both set.
    env_key = os.environ.get("COMFYUI_APIKEY")
    if env_key is not None:
        cfg["comfyui_api_key"] = env_key.strip()
    cfg.setdefault("comfyui_api_key", "")
    _endpoint_disclosure(cfg)
    return cfg

def _endpoint_setup_help(cfg: dict, err: Exception) -> None:
    """Explain how to point this skill at a reachable ComfyUI server."""
    source = "COMFYUI_URL env var" if os.environ.get("COMFYUI_URL") else "comfyui_url in config.json"
    print(f"❌ Cannot reach the ComfyUI server at {cfg['comfyui_url']} (endpoint from {source})",
          file=sys.stderr)
    print(f"   Connection error: {err}", file=sys.stderr)
    print("   To configure this skill:", file=sys.stderr)
    print("     1. Start a ComfyUI server (see README.md → 'Qwen-Image 2.1 ComfyUI Setup'", file=sys.stderr)
    print("        and 'Models & Custom Nodes')", file=sys.stderr)
    print("     2. Point the skill at it: export COMFYUI_URL=http://host:port", file=sys.stderr)
    print("        or edit \"comfyui_url\" in the skill's config.json", file=sys.stderr)
    print("     3. Verify: python3 image_with_comfyui.py test", file=sys.stderr)

def ensure_comfyui_reachable(cfg: dict) -> None:
    """Fail fast with setup instructions when no ComfyUI server answers.

    Runs before any generation work: if the user-defined endpoint (env var or
    config.json) is unreachable, nothing useful would happen, so stop and
    point the user at the configuration docs instead of a raw timeout error.
    """
    url = cfg["comfyui_url"].rstrip("/") + "/history"
    try:
        req = urllib.request.Request(url, method="GET", headers=auth_headers(cfg))
        with urllib.request.urlopen(req, timeout=5):
            pass
    except Exception as e:
        _endpoint_setup_help(cfg, e)
        sys.exit(1)

# ---------------------------------------------------------------------------
# Helper: get model config from nested structure
# ---------------------------------------------------------------------------

def get_model_cfg(cfg: dict, model_id: str) -> dict:
    """Get config for a specific model by ID.
    
    model_id examples: 'z-image', 'sd35', 'qwen_imageedit', 'wan2.2_i2v'
    """
    # Search in image/t2i
    if "image" in cfg and "t2i" in cfg["image"]:
        if model_id in cfg["image"]["t2i"]:
            return cfg["image"]["t2i"][model_id]
    # Search in image/i2i
    if "image" in cfg and "i2i" in cfg["image"]:
        if model_id in cfg["image"]["i2i"]:
            return cfg["image"]["i2i"][model_id]
    # Search in mesh (i2m)
    if "mesh" in cfg and model_id in cfg["mesh"]:
        return cfg["mesh"][model_id]
    # Search in video
    if "video" in cfg and model_id in cfg["video"]:
        return cfg["video"][model_id]
    raise KeyError(f"Model '{model_id}' not found in config")

def get_workflow_path(cfg: dict, model_id: str) -> str:
    return get_model_cfg(cfg, model_id)["workflow_path"]

def get_output_subdir(cfg: dict, model_id: str, default: str = "images") -> str:
    return get_model_cfg(cfg, model_id).get("output_subdir", default)

# ---------------------------------------------------------------------------
# Node package mapping — maps class_type → (package_name, github_url)
# Note: install_command is NOT executed by this script.
# Users must manually run git clone in their ComfyUI/custom_nodes directory.
# ComfyUI may be on a remote server not reachable from this agent.
# ---------------------------------------------------------------------------

NODE_PACKAGE_MAP: dict[str, tuple[str, str]] = {
    # Impact Pack (most common)
    "ImpactPack.IA2PlusPatch": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "ImpactKSamplerBasicPipe": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "ImpactKSamplerAdvancedBasicPipe": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "ImpactSimpleDetectorSEGS": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "ImpactSegsAndMask": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "ImpactSAM2VideoDetectorSEGS": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "BasicPipeToDetailerPipe": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "SAMLoader": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "ImpactIPAdapterApplySEGS": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "ImpactControlNetApplySEGS": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "UltralyticsDetectorProvider": ("ComfyUI-Impact-Subpack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "ImpactWildcardEncode": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "ImpactWildcardProcessor": ("ComfyUI-Impact-Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),

    # Video Helper Suite
    "VHS_VideoCombine": ("ComfyUI-VideoHelperSuite", "https://github.com/Fannovel16/ComfyUI-VideoHelperSuite"),
    "VHS_LoadVideo": ("ComfyUI-VideoHelperSuite", "https://github.com/Fannovel16/ComfyUI-VideoHelperSuite"),
    "VHS_LoadVideoPath": ("ComfyUI-VideoHelperSuite", "https://github.com/Fannovel16/ComfyUI-VideoHelperSuite"),
    "VHS_LoadVideoFFmpeg": ("ComfyUI-VideoHelperSuite", "https://github.com/Fannovel16/ComfyUI-VideoHelperSuite"),

    # Frame Interpolation (RIFE)
    "RIFE VFI": ("ComfyUI-Frame-Interpolation", "https://github.com/Fannovel16/ComfyUI-Frame-Interpolation"),
    "RIFE_VFI_Opt": ("ComfyUI-Frame-Interpolation", "https://github.com/Fannovel16/ComfyUI-Frame-Interpolation"),
    "RIFE_VFI_Advanced": ("ComfyUI-Frame-Interpolation", "https://github.com/Fannovel16/ComfyUI-Frame-Interpolation"),
    "AMT VFI": ("ComfyUI-Frame-Interpolation", "https://github.com/Fannovel16/ComfyUI-Frame-Interpolation"),
    "IFRNet VFI": ("ComfyUI-Frame-Interpolation", "https://github.com/Fannovel16/ComfyUI-Frame-Interpolation"),
    "FILM VFI": ("ComfyUI-Frame-Interpolation", "https://github.com/Fannovel16/ComfyUI-Frame-Interpolation"),
    "GMFSS Fortuna VFI": ("ComfyUI-Frame-Interpolation", "https://github.com/Fannovel16/ComfyUI-Frame-Interpolation"),

    # WAS Node Suite
    "BLIP Analyze Image": ("WASms_Node_Suite_For_ComfyUI", "https://github.com/WASasquatch/was-node-suite-comfyui"),
    "BLIP Model Loader": ("WASms_Node_Suite_For_ComfyUI", "https://github.com/WASasquatch/was-node-suite-comfyui"),
    "Blend Latents": ("WASms_Node_Suite_For_ComfyUI", "https://github.com/WASasquatch/was-node-suite-comfyui"),

    # rgthree
    "Any Switch (rgthree)": ("rgthree-comfy", "https://github.com/rgthree/rgthree-comfy"),
    "Context (rgthree)": ("rgthree-comfy", "https://github.com/rgthree/rgthree-comfy"),
    "Image Comparer (rgthree)": ("rgthree-comfy", "https://github.com/rgthree/rgthree-comfy"),

    # mtb
    "Add To Playlist (mtb)": ("comfy-mtb", "https://github.com/melMass/comfy_mtb"),

    # easy-use
    "dynamicThresholdingFull": ("ComfyUI-easy-use", "https://github.com/easymatic/ComfyUI-easy-use"),

    # kjnodes
    "AppendInstanceDiffusionTracking": ("comfyui-kjnodes", "https://github.com/kijai/ComfyUI-KJNodes"),
    "ImageResizeKJ": ("comfyui-kjnodes", "https://github.com/kijai/ComfyUI-KJNodes"),
    "ApplyRifleXRoPE_WanVideo": ("comfyui-kjnodes", "https://github.com/kijai/ComfyUI-KJNodes"),

    # Crystools
    "Get resolution [Crystools]": ("ComfyUI-Crystools", "https://github.com/crystian/ComfyUI-Crystools"),

    # GGUF
    "CLIPLoaderGGUF": ("ComfyUI-GGUF", "https://github.com/city96/ComfyUI-GGUF"),
    "UnetLoaderGGUF": ("ComfyUI-GGUF", "https://github.com/city96/ComfyUI-GGUF"),

    # wanvideo custom nodes
    "WanImageToVideo": ("wanvideo-comfyui", "https://github.com/kijai/ComfyUI-WanVideoWrapper"),
    "WanMoeKamplerAdvanced": ("wanvideo-comfyui", "https://github.com/kijai/ComfyUI-WanVideoWrapper"),

    # ControlNet
    "ControlNetLoader": ("ComfyUI-ControlNet-Live2D", "https://github.com/coqui-ai/ComfyUI-ControlNet-Live2D"),
    "ControlNetApply": ("ComfyUI-ControlNet", "https://github.com/comfyanonymous/ComfyUI_controlnet_aux"),
    "ControlNetApplyAdvanced": ("ComfyUI-ControlNet", "https://github.com/comfyanonymous/ComfyUI_controlnet_aux"),

    # Hunyuan 3D v2.1 (hyi2m) — core ComfyUI >= 0.37 nodes, not a custom package.
    # Mapped here only so the missing-node detector has a hint; the hyi2m path
    # special-cases these via CORE_3D_NODES below.
    "ImageOnlyCheckpointLoader": ("ComfyUI (core node)", "https://github.com/comfyanonymous/ComfyUI"),
    "ModelSamplingAuraFlow": ("ComfyUI (core node)", "https://github.com/comfyanonymous/ComfyUI"),
    "EmptyLatentHunyuan3Dv2": ("ComfyUI (core node)", "https://github.com/comfyanonymous/ComfyUI"),
    "Hunyuan3Dv2Conditioning": ("ComfyUI (core node)", "https://github.com/comfyanonymous/ComfyUI"),
    "VAEDecodeHunyuan3D": ("ComfyUI (core node)", "https://github.com/comfyanonymous/ComfyUI"),
    "VoxelToMesh": ("ComfyUI (core node)", "https://github.com/comfyanonymous/ComfyUI"),
    "SaveGLB": ("ComfyUI (core node)", "https://github.com/comfyanonymous/ComfyUI"),
}

# Core ComfyUI nodes required by the i2m (image -> 3D mesh) workflow. When one
# is missing the fix is "update ComfyUI", not "clone a custom package" — the
# missing-node detector reports that instead of a git-clone hint.
CORE_3D_NODES = {
    "ImageOnlyCheckpointLoader",
    "ModelSamplingAuraFlow",
    "EmptyLatentHunyuan3Dv2",
    "Hunyuan3Dv2Conditioning",
    "VAEDecodeHunyuan3D",
    "VoxelToMesh",
    "SaveGLB",
}

# ---------------------------------------------------------------------------
# ComfyUI API helpers
# ---------------------------------------------------------------------------

def api_url(cfg: dict, path: str) -> str:
    base = cfg["comfyui_url"].rstrip("/")
    return f"{base}{path}"


def auth_headers(cfg: dict) -> dict:
    """Return the API-auth header dict for ComfyUI API calls.

    Reads the API key from cfg['comfyui_api_key'] (populated from the
    COMFYUI_APIKEY env var or config.json 'comfyui_api_key').
    Returns {'Authorization': 'Bearer <key>'} when a key is configured,
    otherwise {} so requests behave exactly as before (no auth).
    """
    key = (cfg.get("comfyui_api_key") or "").strip()
    if not key:
        return {}
    return {"Authorization": f"Bearer {key}"}


def _merge_headers(*dicts: dict) -> dict:
    """Merge header dicts left-to-right (later keys override earlier ones)."""
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged

def fetch_object_info(cfg: dict) -> dict:
    """Fetch ComfyUI /object_info to get available node types and models."""
    req = urllib.request.Request(
        api_url(cfg, "/object_info"),
        method="GET",
        headers=auth_headers(cfg),
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())

def find_node_package(class_type: str) -> tuple[str, str, str] | None:
    """Look up a node class in the package map. Supports partial matching."""
    if class_type in NODE_PACKAGE_MAP:
        return NODE_PACKAGE_MAP[class_type]
    # Try partial match: normalize and search
    ct_lower = class_type.lower().replace(" ", "").replace("_", "")
    for known, info in NODE_PACKAGE_MAP.items():
        known_norm = known.lower().replace(" ", "").replace("_", "")
        if known_norm in ct_lower or ct_lower in known_norm:
            return info
    return None

def get_available_models(obj_info: dict) -> dict:
    """Extract model file lists from object_info.
    
    Returns dict: {loader_type: {param_name: [model_names]}}
    """
    models = {}
    for node_name, node_info in obj_info.items():
        inp = node_info.get("input", {})
        for param, spec in {**inp.get("required", {}), **inp.get("optional", {})}.items():
            if isinstance(spec, list) and len(spec) > 0 and isinstance(spec[0], list):
                if node_name not in models:
                    models[node_name] = {}
                models[node_name][param] = spec[0]
    return models

def find_model_substitute(requested_model: str, available_models: dict) -> tuple[str, str, str] | None:
    """Find a substitute model for a missing model.
    
    Returns (loader_node, param, substitute_model) or None.
    
    Substitution rules:
    - sd3.5_medium → sd3.5_large
    - WAN2.2 High → WAN2.2 Low (or vice versa)
    - Any exact match in available models
    """
    base_name = requested_model.replace(".safetensors", "")
    
    # Filter: only keep string values (ComfyUI API includes non-string validation values)
    str_lists = {}
    for loader, params in available_models.items():
        str_lists[loader] = {
            k: [v for v in vs if isinstance(v, str)]
            for k, vs in params.items()
            if any(isinstance(x, str) for x in vs)
        }
    
    # Rule 1: sd3.5_medium → sd3.5_large
    if "sd3.5_medium" in base_name or "sd3_medium" in base_name:
        for loader, params in str_lists.items():
            for param, model_list in params.items():
                for m in model_list:
                    if "sd3.5_large" in m or "sd3_large" in m:
                        return (loader, param, m)
                    if "sd3_medium" in m and requested_model != m:
                        return (loader, param, m)
    
    # Rule 2: WAN2.2 High/Low substitution
    if "wan" in base_name.lower() or "WAN" in base_name:
        for loader, params in str_lists.items():
            for param, model_list in params.items():
                has_high = any("High" in m or "high" in m for m in model_list)
                has_low = any("Low" in m or "low" in m for m in model_list)
                if has_high and has_low:
                    if "High" in base_name or "high" in base_name:
                        for m in model_list:
                            if "Low" in m or "low" in m:
                                return (loader, param, m)
                    elif "Low" in base_name or "low" in base_name:
                        for m in model_list:
                            if "High" in m or "high" in m:
                                return (loader, param, m)
                    else:
                        for m in model_list:
                            if "High" in m or "high" in m:
                                return (loader, param, m)
    
    # Rule 3: Any exact match
    for loader, params in str_lists.items():
        for param, model_list in params.items():
            if requested_model in model_list:
                return (loader, param, requested_model)
    
    # Rule 4: Fuzzy match - find any model with similar base name
    for loader, params in str_lists.items():
        for param, model_list in params.items():
            for m in model_list:
                m_base = m.replace(".safetensors", "")
                shared_parts = set(base_name.split("_")) & set(m_base.split("_"))
                if len(shared_parts) >= 2 and m != requested_model:
                    return (loader, param, m)
    
    return None

def update_workflow_model(workflow: dict, loader_node: str, param: str, substitute_model: str) -> dict:
    """Create a modified workflow copy with the substitute model."""
    import copy
    modified = copy.deepcopy(workflow)
    for node_id, node_data in modified.items():
        ct = node_data.get("class_type", "")
        # Find the loader node by class_type
        if ct == loader_node:
            if param in node_data.get("inputs", {}):
                modified[node_id]["inputs"][param] = substitute_model
    return modified


def bypass_node(workflow: dict, missing_node_id: str) -> dict:
    """Create a bypass workflow: remove missing_node_id and redirect upstream → downstream.

    Usage: when ComfyUI reports a missing node but it's a utility/bridging node
    like UnloadAllModels, we can safely skip it by rerouting the signal path.
    """
    import copy
    modified = copy.deepcopy(workflow)
    missing_id = str(missing_node_id)

    # 1. Collect downstream connections — who receives FROM this node
    downstream: dict[str, list[tuple[str, str]]] = {}  # {downstream_node_id: [(upstream_param, port)]}
    for nid, nd in modified.items():
        for k, v in nd.get("inputs", {}).items():
            if isinstance(v, list) and len(v) >= 2 and v[0] == missing_id:
                downstream.setdefault(nid, []).append((k, str(v[1])))

    if not downstream:
        # No downstream — just remove the node, nothing to redirect to
        modified.pop(missing_id, None)
        return modified

    # 2. Find the upstream source — what feeds INTO this node
    # The missing node's own inputs reference its upstream, e.g. {'value': ['43', 0]}
    # means node 43 is the upstream source.
    upstream_nids: list[str] = []
    missing_node = modified.get(missing_id, {})
    for k, v in missing_node.get("inputs", {}).items():
        if isinstance(v, list) and len(v) >= 2:
            src_nid = str(v[0])
            if src_nid != missing_id:  # avoid self-reference
                upstream_nids.append(src_nid)

    if not upstream_nids:
        # No upstream — orphan node, just remove it
        modified.pop(missing_id, None)
        return modified

    up_nid = str(upstream_nids[0])
    up_port = 0

    # 3. Collect connections to update, then apply (avoid mutation during iteration)
    updates: list[tuple[str, str, list]] = []
    for down_nid, connections in downstream.items():
        for param, port in connections:
            if down_nid in modified and param in modified[down_nid].get("inputs", {}):
                updates.append((down_nid, param, [up_nid, up_port]))

    for dn, p, val in updates:
        modified[dn]["inputs"][p] = val

    # 5. Remove the missing node
    modified.pop(missing_id, None)
    return modified

def send_prompt(cfg: dict, workflow: dict, timeout: int = 30) -> str:
    """Send workflow to ComfyUI with error handling for missing nodes and models."""
    data = json.dumps({"prompt": workflow}).encode("utf-8")
    req = urllib.request.Request(
        api_url(cfg, "/prompt"),
        data=data,
        headers=_merge_headers(auth_headers(cfg), {"Content-Type": "application/json"}),
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        result = json.loads(resp.read().decode())
    return result.get("prompt_id", result.get("error", "unknown"))

def send_prompt_with_errors(cfg: dict, workflow: dict, timeout: int = 30, retry_count: int = 0, max_retries: int = 1, skip_autosubstitute: bool = False) -> tuple[str | None, str | None, list[str]]:
    """Send workflow to ComfyUI with automatic error handling.

    Args:
        skip_autosubstitute: When True, the `value_not_in_list` automatic model
            substitution branch is skipped so the caller can decide how to react
            (e.g. descend the runtime fallback chain instead of silently swapping
            the model). Defaults to False (keep the existing auto-substitute behavior).

    Returns: (prompt_id_or_None, error_message_or_None, warning_messages)
    """
    warnings = []
    
    # Send prompt and capture raw result
    data = json.dumps({"prompt": workflow}).encode("utf-8")
    req = urllib.request.Request(
        api_url(cfg, "/prompt"),
        data=data,
        headers=_merge_headers(auth_headers(cfg), {"Content-Type": "application/json"}),
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            result = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        result = json.loads(e.read().decode())
    
    # Check for missing node type error
    error_type = result.get("error", {}).get("type", "")
    if error_type == "missing_node_type":
        class_type = result.get("error", {}).get("extra_info", {}).get("class_type", "Unknown")
        node_id = result.get("error", {}).get("extra_info", {}).get("node_id", "")

        # UnloadAllModels: bypass it (utility node, not needed for generation)
        if class_type == "UnloadAllModels":
            warnings.append(
                f"⚠️ Workflow missing node: `UnloadAllModels` (memory cleanup, non-critical)\n"
                f"🔄 Auto-bypassed — generation continues"
            )
            bypassed = bypass_node(workflow, node_id)
            b_pid, b_err, b_warns = send_prompt_with_errors(cfg, bypassed, timeout, retry_count + 1, max_retries, skip_autosubstitute)
            return b_pid, b_err, warnings + b_warns

        if class_type in CORE_3D_NODES:
            warnings.append(
                f"⚠️ Missing node: `{class_type}`\n"
                f"📦 ComfyUI **core** node (no custom package) — used by the i2m (3D) mode\n"
                f"ℹ️ Update the ComfyUI server to >= 0.37.0 (core Hunyuan 3D v2.1 support) and restart"
            )
            return None, f"missing_node: {class_type}", warnings

        pkg_info = find_node_package(class_type)
        if pkg_info:
            pkg_name, github_url = pkg_info
            warnings.append(
                f"⚠️ Missing node: `{class_type}`\n"
                f"📦 Package: {pkg_name}\n"
                f"🔗 GitHub: {github_url}\n"
                f"ℹ️ Install manually: cd ComfyUI/custom_nodes && git clone {github_url}"
            )
        else:
            warnings.append(f"⚠️ Missing node: `{class_type}` (unknown package, search GitHub)")
        return None, f"missing_node: {class_type}", warnings
    
    # Check for model validation errors
    node_errors = result.get("node_errors", {})
    for node_id, node_err in node_errors.items():
        err_details = node_err.get("errors", [{}])[0] if node_err.get("errors") else {}
        err_type = err_details.get("type", "")
        if err_type == "value_not_in_list":
            # Find the requested model from the node's current inputs
            requested = None
            loader_node = None
            param_name = None
            for nid, nd in workflow.items():
                if str(nid) == str(node_id) and nd.get("class_type", "") in ["CheckpointLoaderSimple", "UNETLoader", "CLIPLoader"]:
                    for param, val in nd.get("inputs", {}).items():
                        if isinstance(val, str) and val.endswith(".safetensors"):
                            requested = val
                            param_name = param
                            loader_node = nd.get("class_type", "")
            
            if requested and loader_node and not skip_autosubstitute:
                obj_info = fetch_object_info(cfg)
                available = get_available_models(obj_info)
                sub = find_model_substitute(requested, available)
                if sub:
                    sub_loader, sub_param, substitute_model = sub
                    warnings.append(
                        f"⚠️ Model missing: `{requested}`\n"
                        f"🔄 Substituted: `{substitute_model}`\n"
                        f"📦 Loader: {sub_loader}.{sub_param}"
                    )
                    new_workflow = update_workflow_model(workflow, loader_node, param_name, substitute_model)
                    sub_pid, sub_err, sub_warns = send_prompt_with_errors(cfg, new_workflow, timeout, retry_count + 1, max_retries, skip_autosubstitute)
                    return sub_pid, sub_err, warnings + sub_warns

            # With substitute disabled (or no usable substitute), hand the raw
            # prompt_id/None back to the caller. For the runtime fallback chain a
            # None here (missing node/file) is treated as a config problem and is
            # NOT retried at a different tier — see error-handling.md §4.
    
    prompt_id = result.get("prompt_id")
    error_msg = result.get("error", {}).get("message", "") if "error" in result else ""
    return prompt_id, error_msg if error_msg else None, warnings

def wait_for_completion(cfg: dict, prompt_id: str, timeout: int = 120) -> dict:
    start = time.time()
    poll_interval = cfg.get("poll_interval_seconds", 3)
    while time.time() - start < timeout:
        try:
            req = urllib.request.Request(
                api_url(cfg, f"/history/{prompt_id}"),
                method="GET",
                headers=auth_headers(cfg),
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                history = json.loads(resp.read().decode())
        except urllib.error.URLError:
            time.sleep(poll_interval)
            continue
        status = history.get(prompt_id, {}).get("status", {})
        status_str = status.get("status_str", "")
        if status_str == "error":
            # ComfyUI reported an error — return immediately so caller
            # can inspect the error messages instead of waiting for timeout.
            return history
        if status.get("completed"):
            return history
        time.sleep(poll_interval)
    raise TimeoutError(f"Generation timed out after {timeout}s (prompt_id={prompt_id})")

def sanitize_filename(filename: str, output_dir: Path) -> str | None:
    """Sanitize a filename from a remote ComfyUI server.

    Prevents path traversal attacks (e.g. `../../../etc/passwd`) by:
    1. Stripping all directory components — only the bare basename is kept
    2. Rejecting empty names, `..`, `.`, or names containing path separators
    3. Verifying the final resolved path stays within output_dir

    Returns the sanitized filename, or None if the filename is unsafe.
    """
    if not filename or not isinstance(filename, str):
        print(f"⚠️ sanitize_filename: empty or non-string filename", file=sys.stderr)
        return None

    # Strip all directory components — only keep the bare filename
    basename = Path(filename).name

    # Reject empty, dot, or dot-dot
    if not basename or basename in (".", ".."):
        print(f"⚠️ sanitize_filename: rejected suspicious name ({basename!r} from {filename!r})", file=sys.stderr)
        return None

    # Reject names with embedded path separators (cross-platform)
    if "/" in basename or "\\" in basename:
        print(f"⚠️ sanitize_filename: path separator in filename ({filename!r})", file=sys.stderr)
        return None

    # Reconstruct candidate path and verify it stays within output_dir
    candidate = (output_dir / basename).resolve()
    if not str(candidate).startswith(str(output_dir.resolve())):
        print(f"⚠️ sanitize_filename: path traversal detected ({filename!r} resolves outside output_dir)", file=sys.stderr)
        return None

    return basename


def get_output_images(history: dict, prompt_id: str, output_dir: Path = None) -> list[dict]:
    """Extract only the final output images from a single prompt_id result.
    Filters out type='temp' intermediate images and sanitizes filenames
    to prevent path traversal from a potentially compromised ComfyUI server.
    """
    images = []
    for node_id, node_result in history.get(prompt_id, {}).get("outputs", {}).items():
        for img in node_result.get("images", []):
            # Only include final output images, skip temp/intermediate
            if img.get("type") == "output":
                safe_name = sanitize_filename(img.get("filename", ""), output_dir)
                if safe_name is None:
                    print(f"⚠️ Skipping unsafe image filename from ComfyUI", file=sys.stderr)
                    continue
                images.append({
                    "filename": safe_name,
                    "subfolder": img.get("subfolder", ""),
                    "type": img.get("type", "output"),
                })
    return images

def image_b64_from_comfyui(cfg: dict, img: dict) -> str:
    params = urllib.parse.urlencode({
        "filename": img["filename"],
        "subfolder": img.get("subfolder", ""),
        "type": img.get("type", "output"),
    })
    req = urllib.request.Request(
        f"{api_url(cfg, '/view')}?{params}",
        method="GET",
        headers=auth_headers(cfg),
    )
    with urllib.request.urlopen(req, timeout=cfg.get("timeout_seconds", 30)) as resp:
        return base64.b64encode(resp.read()).decode("utf-8")

# ---------------------------------------------------------------------------
# Workflow manipulation
# ---------------------------------------------------------------------------

ASPECT_RATIOS = {
    "1:1": (1024, 1024),
    "4:3": (1280, 960),
    "3:4": (960, 1280),
    "16:9": (1280, 720),
    "9:16": (720, 1280),
    "3:2": (1536, 1024),
    "2:3": (1024, 1536),
}

# Qwen-Image 2.1: skill aspect keys -> ResolutionSelector preset names
QWEN21_ASPECT_PRESETS = {
    "1:1": "1:1 (Square)",
    "2:3": "2:3 (Portrait Photo)",
    "3:2": "3:2 (Photo)",
    "3:4": "3:4 (Portrait Standard)",
    "4:3": "4:3 (Standard)",
    "9:16": "9:16 (Portrait Widescreen)",
    "16:9": "16:9 (Widescreen)",
}
QWEN21_MAX_IMAGES = 16

# Runtime fallback chains — see references/error-handling.md §4.
# If a tier fails at RUNTIME (timeout / server sampling error / no output images),
# the next tier is tried. Config problems (missing model file / missing node =>
# prompt_id is None) are NOT retried at other tiers.
FALLBACK_TIERS: dict[str, list[str]] = {
    "t2i": ["qwen21t", "qwen21", "z-image", "sd35"],
    "i2i": ["qwen21t", "qwen21", "qwen_imageedit"],
}


def get_qwen21_model_cfg(cfg: dict) -> dict:
    """qwen21 config lives in both image.t2i and image.i2i; take t2i first."""
    image_cfg = cfg.get("image", {})
    return image_cfg.get("t2i", {}).get("qwen21") or image_cfg.get("i2i", {}).get("qwen21")

# WAN2.2 I2V resolution reference (fast_ok, user_fav, native)
WAN2_2_RES = {
    "3:4": [(560, 720), (720, 912), (848, 1088)],
    "2:3": [(528, 768), (656, 960), (784, 1136)],
    "9:16": [(480, 848), (608, 1072), (720, 1264)],
    "16:9": [(896, 512), (1264, 720), (1072, 608)],
    "1:1": [(560, 560), (704, 704), (832, 832)],
    "4:3": [(720, 560), (864, 672), (1024, 768)],
    "3:2": [(768, 528), (960, 656), (1136, 784)],
}

WAN2_2_ADDITIONAL = {
    "3:4": [(416, 544), (672, 864), (784, 1008)],
    "2:3": [(384, 576), (624, 912), (736, 1072)],
    "9:16": [(368, 624), (576, 1008), (672, 1184)],
    "16:9": [(416, 240), (640, 368), (1008, 576)],
    "1:1": [(480, 480), (624, 624), (736, 736)],
    "4:3": [(576, 416), (848, 608), (1008, 736)],
    "3:2": [(512, 352), (768, 512), (1184, 768)],
}

def find_closest_wan2_2_resolution(iw: int, ih: int) -> tuple[int, int]:
    """Given input image dimensions, find the closest matching Wan2.2 resolution.
    
    Collects all resolutions from WAN2_2_RES and WAN2_2_ADDITIONAL,
    computes aspect ratio, and picks the one with smallest difference.
    """
    target_ar = iw / ih
    best_diff = float("inf")
    best_resolution = None
    
    all_resolutions = []
    for category, res_list in WAN2_2_RES.items():
        for w, h in res_list:
            all_resolutions.append((w, h))
    for category, res_list in WAN2_2_ADDITIONAL.items():
        for w, h in res_list:
            all_resolutions.append((w, h))
    
    for w, h in all_resolutions:
        ar = w / h
        diff = abs(ar - target_ar)
        if diff < best_diff:
            best_diff = diff
            best_resolution = (w, h)
    
    return best_resolution

def find_nodes_by_class(workflow: dict, class_type: str) -> list[dict]:
    results = []
    for node_id, node_data in workflow.items():
        if not isinstance(node_data, dict):
            continue  # tolerate non-node top-level keys (e.g. metadata)
        if node_data.get("class_type") == class_type:
            results.append((node_id, node_data))
    return results

def resolve_skill_path(p: str) -> str:
    p = str(Path(p).expanduser())
    if not Path(p).is_absolute():
        p = str(SCRIPT_DIR / p)
    return p

def resolve_workspace_path(p: str) -> str:
    p = str(Path(p).expanduser())
    if not Path(p).is_absolute():
        p = str(WORKSPACE_DIR / p)
    return p

def strip_unload_nodes(workflow: dict) -> dict:
    """When keep_models_resident is enabled, remove the workflow's VRAM-cleanup
    nodes (UnloadModel / UnloadAllModels) so the model stays resident between
    runs and successive images skip the cold-reload tax.

    UnloadModel and UnloadAllModels are terminal 'sink' nodes: nothing depends on
    their outputs, so simply dropping them is safe (unlike the producer-style
    nodes that need rerouting via bypass_node).
    """
    import copy
    modified = copy.deepcopy(workflow)
    for nid, nd in list(modified.items()):
        if nd.get("class_type") in ("UnloadAllModels", "UnloadModel"):
            modified.pop(nid, None)
    return modified


def apply_keep_resident(cfg: dict, workflow: dict) -> dict:
    """Return the workflow unchanged unless keep_models_resident is explicitly on."""
    if cfg.get("keep_models_resident", False):
        return strip_unload_nodes(workflow)
    return workflow


def prepare_t2i_workflow(cfg: dict, prompt: str, aspect: str = "1:1",
                         seed: int = None, steps: int = None,
                         model_type: str = "z-image") -> tuple[dict, str, int]:
    """Prepare T2I workflow from config, return (workflow, prompt_type, seed)."""
    if model_type == "sd35":
        return prepare_sd35_workflow(cfg, prompt, aspect, seed, steps)
    
    model_cfg = get_model_cfg(cfg, "z-image")
    workflow_path = resolve_skill_path(model_cfg["workflow_path"])
    with open(workflow_path, "r", encoding="utf-8") as f:
        workflow = json.load(f)
    
    # Fill prompt node
    found = False
    for node_id, node_data in workflow.items():
        ct = node_data.get("class_type", "")
        if ct in ("CLIPTextEncode", "TextMultiline") and "text" in node_data.get("inputs", {}):
            workflow[node_id]["inputs"]["text"] = prompt
            found = True
            break
    if not found:
        raise ValueError("T2I: Could not find a prompt node with 'text' input")
    
    # Set dimensions
    if aspect in ASPECT_RATIOS:
        w, h = ASPECT_RATIOS[aspect]
        for node_id, node_data in find_nodes_by_class(workflow, "EmptySD3LatentImage"):
            workflow[node_id]["inputs"]["width"] = w
            workflow[node_id]["inputs"]["height"] = h

    # Timestamped output prefix (filename scheme: zt2i)
    for node_id, node_data in find_nodes_by_class(workflow, "SaveImage"):
        node_data["inputs"]["filename_prefix"] = _save_prefix("zt2i")
    
    if seed is None:
        import random
        seed = random.randint(0, 2**63 - 1)
    
    # Override KSampler
    ks_nodes = find_nodes_by_class(workflow, "KSampler")
    if ks_nodes:
        node_id, _ = ks_nodes[0]
        workflow[node_id]["inputs"]["seed"] = seed
        if steps is not None:
            workflow[node_id]["inputs"]["steps"] = steps
    
    workflow = apply_keep_resident(cfg, workflow)
    return workflow, "Z-Image T2I", seed

def prepare_sd35_workflow(cfg: dict, prompt: str, aspect: str = "1:1",
                          seed: int = None, steps: int = None,
                          cfg_cfg: float = None, negative: str = "") -> tuple[dict, str, int]:
    model_cfg = get_model_cfg(cfg, "sd35")
    workflow_path = resolve_skill_path(model_cfg["workflow_path"])
    with open(workflow_path, "r", encoding="utf-8") as f:
        workflow = json.load(f)
    
    default_w = model_cfg.get("default_width", 1024)
    default_h = model_cfg.get("default_height", 1024)
    default_steps = model_cfg.get("default_steps", 20)
    default_cfg = model_cfg.get("default_cfg", 4.01)
    
    if seed is None:
        import random
        seed = random.randint(0, 2**63 - 1)
    
    if aspect in ASPECT_RATIOS:
        w, h = ASPECT_RATIOS[aspect]
    else:
        w, h = default_w, default_h
    
    for node_id, _ in find_nodes_by_class(workflow, "EmptySD3LatentImage"):
        workflow[node_id]["inputs"]["width"] = w
        workflow[node_id]["inputs"]["height"] = h

    # Timestamped output prefix (filename scheme: st2i)
    for node_id, node_data in find_nodes_by_class(workflow, "SaveImage"):
        node_data["inputs"]["filename_prefix"] = _save_prefix("st2i")
    
    # Fill prompts
    pos_found = False
    for node_id, node_data in workflow.items():
        ct = node_data.get("class_type", "")
        if ct == "CLIPTextEncode" and "text" in node_data.get("inputs", {}):
            if not pos_found:
                workflow[node_id]["inputs"]["text"] = prompt
                pos_found = True
            else:
                workflow[node_id]["inputs"]["text"] = negative if negative else ""
    
    ks_nodes = find_nodes_by_class(workflow, "KSampler")
    if ks_nodes:
        node_id, _ = ks_nodes[0]
        workflow[node_id]["inputs"]["seed"] = seed
        if steps is not None:
            workflow[node_id]["inputs"]["steps"] = steps
        if cfg_cfg is not None:
            workflow[node_id]["inputs"]["cfg"] = cfg_cfg
    
    workflow = apply_keep_resident(cfg, workflow)
    return workflow, "SD3.5 Medium T2I", seed

def _build_multipart_body(parts: list[tuple[str, str]], files: list[tuple[str, str, str]]) -> tuple[bytes, str]:
    import uuid
    boundary = str(uuid.uuid4())
    body = BytesIO()
    for name, value in parts:
        body.write(f"--{boundary}\r\n".encode())
        body.write(f"Content-Disposition: form-data; name=\"{name}\"\r\n\r\n".encode())
        body.write(f"{value}\r\n".encode())
    for file_name, filepath, content_type in files:
        body.write(f"--{boundary}\r\n".encode())
        body.write(f"Content-Disposition: form-data; name=\"image\"; filename=\"{file_name}\"\r\n".encode())
        body.write(f"Content-Type: {content_type}\r\n\r\n".encode())
        with open(filepath, "rb") as f:
            body.write(f.read())
        body.write(b"\r\n")
    body.write(f"--{boundary}--\r\n".encode())
    return body.getvalue(), boundary

def upload_image_to_comfyui(cfg: dict, local_path: str, filename: str = None) -> str:
    if filename is None:
        filename = Path(local_path).name
    body, boundary = _build_multipart_body(
        [("subfolder", ""), ("type", "input")],
        [(filename, local_path, "image/jpeg")]
    )
    req = urllib.request.Request(
        api_url(cfg, "/upload/image"),
        data=body,
        headers=_merge_headers(
            auth_headers(cfg),
            {"Content-Type": f"multipart/form-data; boundary={boundary}"},
        ),
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=cfg.get("timeout_seconds", 30)) as resp:
        result = json.loads(resp.read().decode())
    return result.get("name", filename)

def _set_qwen21_latent_switch(workflow: dict, use_aspect: bool) -> bool:
    """Route the I2I latent canvas via the workflow's latent switch node.

    The switch feeds KSampler's latent_image: ON = match the first reference
    image's size (encoder output), OFF = use the ResolutionSelector's aspect
    ratio (EmptyLatentImage). Returns True when a switch node was found.
    """
    sampler_latent_src = None
    for node_id, node_data in find_nodes_by_class(workflow, "KSampler"):
        link = node_data.get("inputs", {}).get("latent_image")
        if isinstance(link, list) and len(link) == 2:
            sampler_latent_src = link[0]
    for node_id, node_data in find_nodes_by_class(workflow, "ComfySwitchNode"):
        if node_id == sampler_latent_src:
            node_data["inputs"]["switch"] = not use_aspect
            return True
    return False

def prepare_qwen21_workflow(cfg: dict, prompt: str, aspect: str = "1:1",
                            seed: int = None, steps: int = None,
                            negative: str = "", images: list = None,
                            variant: str = "qwen21") -> tuple[dict, str, int]:
    """Prepare the Qwen-Image 2.x dual-mode workflow (T2I / I2I / multi-image).

    variant: which model entry to load from config — "qwen21" (Qwen-Image 2.1)
             or "qwen21t" (Qwen-Image 2.1 Turbo). Both use the same node
             topology, so the only differences are the workflow file, default
             steps, and the output filename prefix.

    images: list of local image paths. Empty = pure T2I (reference switch OFF).
            1..16 = edit/multi-image (switch ON; image N -> <imageN> in prompt).
    aspect: output canvas shape. In I2I, None means the latent switch matches
            the first reference image's size; any explicit value routes the
            canvas through the ResolutionSelector at that ratio instead.
    """
    import random
    model_cfg = get_model_cfg(cfg, variant)
    workflow_path = resolve_skill_path(model_cfg["workflow_path"])
    with open(workflow_path, "r", encoding="utf-8") as f:
        workflow = json.load(f)

    images = list(images or [])
    if len(images) > QWEN21_MAX_IMAGES:
        raise ValueError(f"qwen21 supports at most {QWEN21_MAX_IMAGES} reference images, got {len(images)}")
    explicit_aspect = aspect is not None
    if aspect is None:
        aspect = "1:1"
    if seed is None:
        seed = random.randint(0, 2**63 - 1)

    # Master switch: OFF = pure T2I, ON = reference image(s)
    for node_id, node_data in find_nodes_by_class(workflow, "PrimitiveBoolean"):
        node_data["inputs"]["value"] = len(images) > 0

    # Latent canvas routing: explicit --aspect (or pure T2I) -> ResolutionSelector
    # preset; I2I without --aspect -> match the first reference image's size.
    if not _set_qwen21_latent_switch(workflow, use_aspect=(not images) or explicit_aspect):
        print("   ⚠️ qwen21 latent switch node not found — I2I canvas will follow reference size", file=sys.stderr)

    # Aspect ratio -> ResolutionSelector preset
    preset = QWEN21_ASPECT_PRESETS.get(aspect)
    for node_id, node_data in find_nodes_by_class(workflow, "ResolutionSelector"):
        if preset:
            node_data["inputs"]["aspect_ratio"] = preset
        node_data["inputs"]["megapixels"] = model_cfg.get("default_megapixels", 1.0)

    # Text encoder: prompt, negative, reference resize target, extra image slots
    for node_id, node_data in find_nodes_by_class(workflow, "TextEncodeQwenImage21"):
        node_data["inputs"]["prompt"] = prompt
        node_data["inputs"]["negative_prompt"] = negative or ""
        node_data["inputs"]["resolution"] = model_cfg.get("default_ref_resolution", 1024)
        if not images:
            # T2I: drop the slot-1 link entirely (placeholder file won't exist server-side)
            node_data["inputs"].pop("images.image_1", None)
        else:
            for i in range(2, len(images) + 1):
                node_data["inputs"][f"images.image_{i}"] = [str(90 + i), 0]

    if not images:
        # T2I: drop the slot-1 link + reference branch nodes (LoadImage 11 +
        # switch 13; the placeholder file won't exist server-side). The latent
        # switch routes the canvas to the ResolutionSelector.
        for node_id, node_data in find_nodes_by_class(workflow, "TextEncodeQwenImage21"):
            node_data["inputs"].pop("images.image_1", None)
        for nid in ("11", "13"):
            if workflow.get(nid, {}).get("class_type") in ("LoadImage", "ComfySwitchNode"):
                workflow.pop(nid)
    else:
        # I2I: reference image(s) uploaded at their native size (never
        # pre-resized); canvas shape is chosen by the latent switch above.
        uploaded = upload_image_to_comfyui(cfg, images[0])
        for node_id, node_data in find_nodes_by_class(workflow, "LoadImage"):
            node_data["inputs"]["image"] = uploaded
        for i in range(2, len(images) + 1):
            fn = upload_image_to_comfyui(cfg, images[i - 1])
            nid = str(90 + i)
            workflow[nid] = {
                "class_type": "LoadImage",
                "inputs": {"image": fn},
                "_meta": {"title": f"Reference image (slot {i})"},
            }

    # KSampler: cfg locked to model default (1.0 — distilled model)
    for node_id, node_data in find_nodes_by_class(workflow, "KSampler"):
        node_data["inputs"]["seed"] = seed
        node_data["inputs"]["steps"] = steps if steps is not None else model_cfg.get("default_steps", 25)
        node_data["inputs"]["cfg"] = model_cfg.get("default_cfg", 1.0)

    # Timestamped output prefix (filename scheme: qt2i/qi2i / qtt2i/qti2i /
    # qei2i / zt2i / st2i). Turbo uses the t-prefixed scheme so its outputs
    # sort separately from the Qwen-Image 2.1 run.
    mode = ("qti2i" if images else "qtt2i") if variant == "qwen21t" else ("qi2i" if images else "qt2i")
    for node_id, node_data in find_nodes_by_class(workflow, "SaveImage"):
        node_data["inputs"]["filename_prefix"] = _save_prefix(mode)

    if variant == "qwen21t":
        base = "Qwen-Image 2.1 Turbo"
    else:
        base = "Qwen-Image 2.1"
    label = f"{base} Edit ({len(images)} ref image)" if images else f"{base} T2I"
    workflow = apply_keep_resident(cfg, workflow)
    return workflow, label, seed


def prepare_i2i_workflow(cfg: dict, prompt: str, image_path: str,
                         seed: int = None, steps: int = None) -> tuple[dict, str, str, int]:
    model_cfg = get_model_cfg(cfg, "qwen_imageedit")
    workflow_path = resolve_skill_path(model_cfg["workflow_path"])
    with open(workflow_path, "r", encoding="utf-8") as f:
        workflow = json.load(f)
    
    uploaded_filename = upload_image_to_comfyui(cfg, image_path)
    
    for node_id, node_data in find_nodes_by_class(workflow, "LoadImage"):
        workflow[node_id]["inputs"]["image"] = uploaded_filename
    
    prompt_nodes = find_nodes_by_class(workflow, "TextEncodeQwenImageEditPlus")
    if prompt_nodes:
        # Find positive prompt node (has a non-empty default prompt)
        positive_node = None
        for node_id, node_data in prompt_nodes:
            default_prompt = node_data.get("inputs", {}).get("prompt", "")
            if default_prompt and default_prompt != "":
                positive_node = (node_id, node_data)
                break
        # Fallback to first node if no positive node found
        if positive_node is None:
            positive_node = prompt_nodes[0]
        node_id, _ = positive_node
        workflow[node_id]["inputs"]["prompt"] = prompt
    
    ks_nodes = find_nodes_by_class(workflow, "KSampler")
    if ks_nodes:
        node_id, _ = ks_nodes[0]
        if seed is None:
            import random
            seed = random.randint(0, 2**63 - 1)
        workflow[node_id]["inputs"]["seed"] = seed
        if steps is not None:
            workflow[node_id]["inputs"]["steps"] = steps

    # Timestamped output prefix (filename scheme: qei2i)
    for node_id, node_data in find_nodes_by_class(workflow, "SaveImage"):
        node_data["inputs"]["filename_prefix"] = _save_prefix("qei2i")

    return workflow, "Qwen Image Edit", uploaded_filename, seed

# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def _save_prefix(base: str) -> str:
    """Server-side SaveImage filename prefix: base + '_' + timestamp (no trailing '_').

    ComfyUI appends '_NNNNN_' after the prefix, so the final filename ends with
    an underscore; save_b64_image() strips that trailing '_' client-side.
    """
    ts = time.strftime("%Y%m%d_%H%M%S")
    return f"{base}_{ts}"


def _strip_trailing_underscore(name: str) -> str:
    """Remove a trailing '_' from a filename, handling both `name_` and `name_.ext`."""
    stem, _, ext = name.rpartition(".")
    if ext and stem.endswith("_"):
        return stem.rstrip("_") + "." + ext
    return name.rstrip("_")


def ensure_output_dir(cfg: dict, model_id: str = None, cmd_output_dir: str = None) -> Path:
    """Get output directory: output_dir + output_subdir.
    
    Output path = resolve_workspace(output_dir) / output_subdir
    
    Args:
        cfg: config dict
        model_id: model identifier (e.g. 'z-image', 'sd35', 'qwen_imageedit', 'wan2.2_i2v')
        cmd_output_dir: override from --output-dir CLI arg (absolute path)
    """
    # CLI override takes highest priority
    if cmd_output_dir:
        return Path(resolve_workspace_path(cmd_output_dir))
    
    # Base output_dir from config
    base = Path(resolve_workspace_path(cfg.get("output_dir", "media/comfyui")))
    
    # Append model-specific output_subdir
    if model_id:
        output_subdir = get_output_subdir(cfg, model_id)
        return base / output_subdir
    
    return base

def save_b64_image(b64_data: str, filename: str, output_dir: Path,
                   fmt: str = "png", jpg_quality: int = 95) -> Path:
    """Save a base64 image, converting to JPG on the client side when fmt='jpg'.

    ComfyUI's SaveImage node always writes PNG server-side; the JPG conversion
    happens here after download (Pillow), so it works with any server setup.
    Falls back to PNG if conversion fails.
    """
    safe_name = sanitize_filename(filename, output_dir)
    if safe_name is None:
        safe_name = f"image_{int(time.time())}.png"  # fallback name
    safe_name = _strip_trailing_underscore(safe_name)  # ComfyUI saves as prefix_NNNNN_.ext — drop the '_'
    raw = base64.b64decode(b64_data)
    if fmt == "jpg":
        if Path(safe_name).suffix.lower() != ".jpg":
            safe_name = Path(safe_name).stem + ".jpg"
        output_path = output_dir / safe_name
        try:
            from PIL import Image
            img = Image.open(io.BytesIO(raw))
            img.load()
            if img.mode not in ("RGB", "L"):
                # JPEG has no alpha channel — composite onto white
                rgba = img.convert("RGBA")
                bg = Image.new("RGB", rgba.size, (255, 255, 255))
                bg.paste(rgba, mask=rgba.split()[-1])
                img = bg
            else:
                img = img.convert("RGB")
            img.save(output_path, "JPEG", quality=jpg_quality, optimize=True)
            return output_path
        except Exception as e:
            print(f"⚠️ JPG conversion failed ({e}) — falling back to PNG", file=sys.stderr)
            output_path = output_dir / Path(safe_name).stem + ".png"
    else:
        output_path = output_dir / safe_name
    with open(output_path, "wb") as f:
        f.write(raw)
    return output_path


def get_output_fmt_args(cfg: dict, args) -> tuple:
    """Resolve (fmt, jpg_quality) from CLI flags, then config.json, then defaults."""
    image_cfg = cfg.get("image", {})
    fmt = getattr(args, "format", None) or image_cfg.get("output_format", "png")
    if fmt not in ("png", "jpg"):
        fmt = "png"
    quality = getattr(args, "jpg_quality", None) or image_cfg.get("jpg_quality", 89)
    return fmt, int(quality)

def print_result(prompt_type: str, prompt: str, images: list[dict],
                 local_paths: list[Path], output_dir: Path, cfg: dict = None,
                 seed: int = None):
    for i, img, path in zip(range(1, len(local_paths)+1), images, local_paths):
        sz = path.stat().st_size / 1024
        print(f"✅ Image {i}: {path.name} ({sz:.0f} KB)")
        print(f"   Prompt: {prompt[:80]}")
        print(f"   File: {path}")
        if seed is not None:
            print(f"   Seed: {seed}")

# ---------------------------------------------------------------------------
# Runtime fallback chain (see references/error-handling.md §4)
#
# Tiers fail on RUNTIME signals only: server timeout / status=error /
# no output images. Config problems (prompt_id is None: missing model file
# or missing node) are NOT retried at another tier — the existing
# missing-model / missing-node paths stay authoritative.
# ---------------------------------------------------------------------------

FAIL_CONFIG = "config problem (missing model file / node) — no fallback"


def _execute_tier(cfg: dict, workflow: dict, timeout: int, output_dir: Path):
    """Send one prepared workflow and collect the result.

    Returns (prompt_id_or_None, failure_reason_or_None, images_or_None).
    failure_reason is None on success.
    """
    prompt_id, err_msg, warns = send_prompt_with_errors(cfg, workflow, timeout, skip_autosubstitute=True)
    for w in warns:
        print(w)
    if prompt_id is None:
        return None, FAIL_CONFIG, None
    try:
        history = wait_for_completion(cfg, prompt_id, timeout)
    except TimeoutError:
        return prompt_id, f"server timeout (>{timeout}s)", None
    except urllib.error.URLError as e:
        # Server unreachable mid-run — every tier on the same server would
        # fail identically, so treat as environment problem, not a model failure.
        return prompt_id, f"cannot connect to ComfyUI ({e}) — config/environment problem, no fallback", None
    status_str = history.get(prompt_id, {}).get("status", {}).get("status_str", "")
    if status_str == "error":
        return prompt_id, "server sampling error", None
    images = get_output_images(history, prompt_id, output_dir)
    if not images:
        return prompt_id, "no output images", None
    return prompt_id, None, images


def _prepare_tier(cfg: dict, args, tier: str, kind: str, seed: int, steps: int):
    """Build one fallback tier with the existing prepare_* functions.

    Returns (workflow, timeout, output_dir, label), or None when the tier is
    not applicable (e.g. qwen_imageedit with multi-image input).
    """
    if kind == "t2i":
        aspect = args.aspect
        if tier == "qwen21t":
            model_cfg = get_model_cfg(cfg, "qwen21t")
            aspect = aspect or model_cfg.get("default_aspect", "1:1")
            if steps is None:
                steps = model_cfg.get("default_steps", 8)
            output_dir = ensure_output_dir(cfg, "qwen21t", args.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            timeout = model_cfg.get("timeout_seconds", 300)
            workflow, label, _ = prepare_qwen21_workflow(
                cfg, args.prompt, aspect=aspect, seed=seed, steps=steps,
                negative=getattr(args, 'negative', '') or "",
                variant="qwen21t")
        elif tier == "qwen21":
            model_cfg = get_qwen21_model_cfg(cfg)
            aspect = aspect or model_cfg.get("default_aspect", "1:1")
            if steps is None:
                steps = model_cfg.get("default_steps", 25)
            output_dir = ensure_output_dir(cfg, "qwen21", args.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            timeout = model_cfg.get("timeout_seconds", 600)
            workflow, label, _ = prepare_qwen21_workflow(
                cfg, args.prompt, aspect=aspect, seed=seed, steps=steps,
                negative=getattr(args, 'negative', '') or "")
        elif tier == "sd35":
            model_cfg = get_model_cfg(cfg, "sd35")
            aspect = aspect or "1:1"
            if steps is None:
                steps = model_cfg.get("default_steps", 20)
            cfg_val = args.cfg if args.cfg is not None else model_cfg.get("default_cfg", 4.01)
            negative = getattr(args, "negative", "") or ""
            output_dir = ensure_output_dir(cfg, "sd35", args.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            timeout = model_cfg.get("timeout_seconds", 100)
            workflow, label, _ = prepare_sd35_workflow(cfg, args.prompt, aspect, seed, steps, cfg_val, negative)
        else:  # z-image
            model_cfg = get_model_cfg(cfg, "z-image")
            aspect = aspect or "1:1"
            if steps is None:
                steps = model_cfg.get("default_steps", 9)
            output_dir = ensure_output_dir(cfg, "z-image", args.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            timeout = model_cfg.get("timeout_seconds", 100)
            workflow, label, _ = prepare_t2i_workflow(cfg, args.prompt, aspect, seed, steps, "z-image")
        return workflow, timeout, output_dir, label

    # i2i
    raw_images = args.image if isinstance(args.image, list) else [args.image]
    image_paths = [str(Path(p).expanduser()) for p in raw_images]
    if tier == "qwen21t":
        model_cfg = get_model_cfg(cfg, "qwen21t")
        if steps is None:
            steps = model_cfg.get("default_steps", 8)
        output_dir = ensure_output_dir(cfg, "qwen21t", args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timeout = model_cfg.get("timeout_seconds", 600)
        workflow, label, _ = prepare_qwen21_workflow(
            cfg, args.prompt,
            aspect=args.aspect,  # None = follow first reference image's ratio
            seed=seed, steps=steps, images=image_paths,
            negative=getattr(args, 'negative', '') or "",
            variant="qwen21t")
        return workflow, timeout, output_dir, label

    if tier == "qwen21":
        model_cfg = get_qwen21_model_cfg(cfg)
        if steps is None:
            steps = model_cfg.get("default_steps", 25)
        output_dir = ensure_output_dir(cfg, "qwen21", args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timeout = model_cfg.get("timeout_seconds", 600)
        workflow, label, _ = prepare_qwen21_workflow(
            cfg, args.prompt,
            aspect=args.aspect,  # None = follow first reference image's ratio
            seed=seed, steps=steps, images=image_paths,
            negative=getattr(args, 'negative', '') or "")
        return workflow, timeout, output_dir, label

    # qwen_imageedit — single input image only
    if len(image_paths) != 1:
        print(f"⚠️ tier {tier} — skipped: this model supports a single input image only")
        return None
    model_cfg = get_model_cfg(cfg, "qwen_imageedit")
    if steps is None:
        steps = model_cfg.get("default_steps", 4)
    output_dir = ensure_output_dir(cfg, "qwen_imageedit", args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    timeout = model_cfg.get("timeout_seconds", 600)
    workflow, label, _fn, _ = prepare_i2i_workflow(cfg, args.prompt, image_paths[0], seed, steps)
    return workflow, timeout, output_dir, label


def _deliver_fallback(cfg: dict, args, images: list[dict], output_dir: Path,
                      label: str, seed: int, used_tier: str, failed: list[str]) -> None:
    """Download + save + print the result of a successful tier, reporting any descent."""
    b64_images = [image_b64_from_comfyui(cfg, img) for img in images]
    fmt, jpg_quality = get_output_fmt_args(cfg, args)
    local_paths = [save_b64_image(b64, img["filename"], output_dir, fmt, jpg_quality)
                   for b64, img in zip(b64_images, images)]
    print_result(label, args.prompt, images, local_paths, output_dir, cfg, seed)
    if failed:
        print(f"🔄 used {used_tier} — fell back because {' / '.join(failed)} failed this run.")
        print("   👉 Want a different model / prompt / seed, or a retry? Just say so.")


def _known_tier_model_files() -> set[str]:
    """Model filenames referenced by the built-in tier workflows (excluded from tier 4)."""
    used: set[str] = set()
    for wf_rel in ("workflows/qwen_image_2.1_api.json", "workflows/z-image_t2i_api.json",
                   "workflows/sd3.5-med_t2i_api.json", "workflows/qwen_image-edit_api.json"):
        try:
            with open(resolve_skill_path(wf_rel), "r", encoding="utf-8") as f:
                wf = json.load(f)
        except Exception:
            continue
        for nd in wf.values():
            if not isinstance(nd, dict):
                continue
            for p in ("unet_name", "ckpt_name"):
                v = nd.get("inputs", {}).get(p)
                if isinstance(v, str) and v:
                    used.add(v)
    return used


def _build_minimal_ckpt_workflow(ckpt_name: str, prompt: str, aspect: str, seed: int, steps: int) -> dict:
    """Minimal standard topology: checkpoint + CLIP x2 + latent + KSampler + VAE + save."""
    w, h = ASPECT_RATIOS.get(aspect, (1024, 1024))
    ts = time.strftime("%Y%m%d_%H%M%S")
    return {
        "1": {"class_type": "CheckpointLoaderSimple",
             "inputs": {"ckpt_name": ckpt_name},
             "_meta": {"title": "Checkpoint (fallback)"}},
        "2": {"class_type": "CLIPTextEncode",
             "inputs": {"text": prompt, "clip": ["1", 1]},
             "_meta": {"title": "Positive (fallback)"}},
        "3": {"class_type": "CLIPTextEncode",
             "inputs": {"text": "", "clip": ["1", 1]},
             "_meta": {"title": "Negative (fallback)"}},
        "4": {"class_type": "EmptySD3LatentImage",
             "inputs": {"width": w, "height": h, "batch_size": 1},
             "_meta": {"title": "Latent (fallback)"}},
        "5": {"class_type": "KSampler",
             "inputs": {"seed": seed, "steps": steps, "cfg": 7.0,
                        "sampler_name": "euler", "scheduler": "normal", "denoise": 1.0,
                        "model": ["1", 0], "positive": ["2", 0],
                        "negative": ["3", 0], "latent_image": ["4", 0]},
             "_meta": {"title": "Sampler (fallback)"}},
        "6": {"class_type": "VAEDecode",
             "inputs": {"samples": ["5", 0], "vae": ["1", 2]},
             "_meta": {"title": "VAEDecode (fallback)"}},
        "7": {"class_type": "SaveImage",
             "inputs": {"filename_prefix": f"fallback/{ts}", "images": ["6", 0]},
             "_meta": {"title": "Save (fallback)"}},
    }


def _print_available_models(cfg: dict) -> None:
    try:
        avail = get_available_models(fetch_object_info(cfg))
        ckpt = [m for m in avail.get("CheckpointLoaderSimple", {}).get("ckpt_name", []) if isinstance(m, str)]
        unet = [m for m in avail.get("UNETLoader", {}).get("unet_name", []) if isinstance(m, str)]
        print(f"   Available checkpoints: {', '.join(ckpt) or '(none)'}")
        print(f"   Available UNet models: {', '.join(unet) or '(none)'}")
    except Exception as e:
        print(f"   (could not fetch the available model list: {e})")


def _attempt_any_available(cfg: dict, args, seed: int, steps: int, failed: list[str]) -> None:
    """Tier 4 (t2i only): try any remaining checkpoint model with the standard topology.

    If none work (or none exist), print the full candidate list for manual choice.
    """
    print("🔎 All configured models failed — probing the server for any available checkpoint model ...")
    try:
        obj_info = fetch_object_info(cfg)
    except Exception as e:
        print(f"❌ Could not fetch the available model list: {e}", file=sys.stderr)
        sys.exit(1)
    avail = get_available_models(obj_info)
    ckpt_names = [m for m in avail.get("CheckpointLoaderSimple", {}).get("ckpt_name", []) if isinstance(m, str)]
    unet_names = [m for m in avail.get("UNETLoader", {}).get("unet_name", []) if isinstance(m, str)]
    used = _known_tier_model_files()
    candidates = [m for m in ckpt_names if m not in used]
    if not candidates:
        print(f"❌ No remaining checkpoint models. Available (for manual choice): {', '.join(ckpt_names) or '(none)'}")
        print(f"   Available UNet models: {', '.join(unet_names) or '(none)'}")
        print("   👉 Tell me a model name and I can retry with --model or a custom workflow.")
        sys.exit(1)

    aspect = args.aspect or "1:1"
    if steps is None:
        steps = 20
    output_dir = ensure_output_dir(cfg, None, args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    timeout = 300

    for m in candidates:
        print(f"⚠️ trying {m} (any available) ...")
        wf = _build_minimal_ckpt_workflow(m, args.prompt, aspect, seed, steps)
        pid, reason, images = _execute_tier(cfg, wf, timeout, output_dir)
        if reason is None:
            _deliver_fallback(cfg, args, images, output_dir, f"any available: {m}", seed, m, failed)
            return
        if reason.startswith("config problem"):
            print(f"   skipped {m}: {reason} (topology/file mismatch for this model)")
            continue
        print(f"   failed: {reason}")

    print("❌ All candidate models failed. Available models (for manual choice):")
    _print_available_models(cfg)
    print("   👉 Tell me a model name or prompt adjustment and I can continue.")
    sys.exit(1)


def _run_with_fallback(cfg: dict, args, kind: str) -> None:
    """Dispatch a t2i/i2i request through the runtime fallback chain."""
    import random
    base_tier = args.model or cfg.get("default_model", {}).get(kind)
    if not base_tier:
        base_tier = "qwen21" if kind == "t2i" else "qwen_imageedit"
    tiers = [base_tier] + [t for t in FALLBACK_TIERS[kind] if t != base_tier]

    seed = args.seed
    if seed is None:
        seed = random.randint(0, 2**63 - 1)
    steps = args.steps

    failed: list[str] = []
    for tier in tiers:
        print(f"🎨 trying {tier} ...")
        try:
            prepared = _prepare_tier(cfg, args, tier, kind, seed, steps)
        except Exception as e:
            print(f"⚠️ tier {tier} — failed during preparation: {e}")
            failed.append(tier)
            continue
        if prepared is None:
            failed.append(tier)  # inapplicable tier (e.g. multi-image on qwen_imageedit)
            continue
        workflow, timeout, output_dir, label = prepared
        pid, reason, images = _execute_tier(cfg, workflow, timeout, output_dir)
        if reason is None:
            _deliver_fallback(cfg, args, images, output_dir, label, seed, tier, failed)
            return
        print(f"⚠️ tier {tier} — failed: {reason}")
        failed.append(tier)
        if reason.startswith("config problem") or "no fallback" in reason:
            print(f"❌ {reason} — not degrading to another model (see references/error-handling.md).")
            sys.exit(1)

    if kind == "t2i":
        _attempt_any_available(cfg, args, seed, steps, failed)
    # i2i: no blind generic topology — a plain T2I model cannot honor the source image.
    print("❌ All edit models failed this run — i2i never degrades blindly without the reference image.")
    print("   Available models (for reference):")
    _print_available_models(cfg)
    print("   👉 Want to retry / switch model / adjust the prompt? Just say so.")
    sys.exit(1)


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------

def get_output_videos(history: dict, prompt_id: str, wan_cfg: dict = None, output_dir: Path = None) -> list:
    result = history.get(prompt_id, {}).get("outputs", {})
    videos = []
    for node_id, node_output in result.items():
        for key, value in node_output.items():
            if isinstance(value, list):
                for item in value:
                    if key in ("gifs", "video") or (isinstance(item, dict) and item.get("type") == "video"):
                        if wan_cfg and wan_cfg.get("keep_interpolated_only"):
                            frame_rate = item.get("frame_rate", 0)
                            filename = item.get("filename", "")
                            safe_name = sanitize_filename(filename, output_dir)
                            if frame_rate == 32 or (safe_name and "_00002_" in safe_name):
                                videos.append(item)
                        else:
                            safe_name = sanitize_filename(item.get("filename", ""), output_dir)
                            if safe_name is None:
                                print(f"⚠️ Skipping unsafe video filename from ComfyUI", file=sys.stderr)
                                continue
                            videos.append(item)
    return videos

def video_b64_from_comfyui(cfg: dict, video_item: dict) -> str:
    filename = video_item.get("filename", "")
    subfolder = video_item.get("subfolder", "")
    v_type = video_item.get("type", "output")
    url = f'{cfg["comfyui_url"].rstrip("/")}/view?filename={urllib.parse.quote(filename)}&subfolder={urllib.parse.quote(subfolder)}&type={urllib.parse.quote(v_type)}'
    try:
        req = urllib.request.Request(url, method="GET", headers=auth_headers(cfg))
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
        return base64.b64encode(data).decode("utf-8")
    except urllib.error.URLError as e:
        print(f"   ❌ Failed to download video: {e}", file=sys.stderr)
        return ""

def save_b64_video(b64_data: str, filename: str, output_dir: Path) -> str:
    output_dir.mkdir(parents=True, exist_ok=True)
    safe_name = sanitize_filename(filename, output_dir)
    if safe_name is None:
        safe_name = f"video_{int(time.time())}.mp4"  # fallback name
    else:
        safe_name = _strip_trailing_underscore(safe_name)  # drop ComfyUI's trailing '_'
    output_path = output_dir / safe_name
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(b64_data))
    return str(output_path)

def print_result_video(prompt_type: str, prompt: str, video_items: list,
                       local_paths: list, output_dir: Path, cfg: dict,
                       seed: int = None) -> None:
    for i, v, p in zip(range(1, len(local_paths)+1), video_items, local_paths):
        p = Path(p) if isinstance(p, str) else p
        sz = p.stat().st_size / 1024
        print(f"✅ Video {i}: {p.name} ({sz:.0f} KB)")
        print(f"   Prompt: {prompt[:80]}")
        print(f"   File: {p}")
        if seed is not None:
            print(f"   Seed: {seed}")

def cmd_t2i(cfg: dict, args: argparse.Namespace) -> None:
    default_model = cfg.get("default_model", {}).get("t2i", "z-image")
    model_type = args.model or default_model
    if model_type not in ("qwen21t", "qwen21", "z-image", "sd35"):
        print(f"❌ Unknown t2i model: {model_type} (expected qwen21t / qwen21 / z-image / sd35)", file=sys.stderr)
        sys.exit(1)

    if getattr(args, "no_fallback", False):
        # Single-model mode: existing behavior, no runtime fallback.
        _run_t2i_single(cfg, args, model_type)
        return
    _run_with_fallback(cfg, args, "t2i")

def _run_t2i_single(cfg: dict, args, model_type: str) -> None:
    """Single-model t2i run (used with --no-fallback)."""
    prompt = args.prompt
    seed = args.seed
    steps = args.steps


    if seed is None:
        import random
        seed = random.randint(0, 2**63 - 1)

    if model_type == "qwen21t":
        model_cfg = get_model_cfg(cfg, "qwen21t")
        aspect = args.aspect or model_cfg.get("default_aspect", "1:1")
        if steps is None:
            steps = model_cfg.get("default_steps", 8)
        if args.cfg is not None:
            print("⚠️ qwen21t (Turbo) — ignoring --cfg, keeping CFG 1.0", file=sys.stderr)
        output_dir = ensure_output_dir(cfg, "qwen21t", args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timeout = model_cfg.get("timeout_seconds", 300)
        workflow, prompt_type_str, seed_used = prepare_qwen21_workflow(
            cfg, prompt, aspect=aspect, seed=seed, steps=steps,
            negative=getattr(args, 'negative', '') or "", variant="qwen21t")
    elif model_type == "qwen21":
        model_cfg = get_qwen21_model_cfg(cfg)
        aspect = args.aspect or model_cfg.get("default_aspect", "1:1")
        if steps is None:
            steps = model_cfg.get("default_steps", 25)
        if args.cfg is not None:
            print("⚠️ qwen21 is a distilled model — ignoring --cfg, keeping CFG 1.0", file=sys.stderr)
        output_dir = ensure_output_dir(cfg, "qwen21", args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timeout = model_cfg.get("timeout_seconds", 600)
        workflow, prompt_type_str, seed_used = prepare_qwen21_workflow(
            cfg, prompt, aspect=aspect, seed=seed, steps=steps,
            negative=getattr(args, 'negative', '') or "")
    elif model_type == "sd35":
        model_cfg = get_model_cfg(cfg, "sd35")
        aspect = args.aspect or "1:1"
        if steps is None:
            steps = model_cfg.get("default_steps", 20)
        cfg_val = args.cfg if args.cfg is not None else model_cfg.get("default_cfg", 4.01)
        negative = getattr(args, 'negative', '') or ''
        output_dir = ensure_output_dir(cfg, "sd35", args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timeout = model_cfg.get("timeout_seconds", 100)
        workflow, prompt_type_str, seed_used = prepare_sd35_workflow(cfg, prompt, aspect, seed, steps, cfg_val, negative)
    else:
        model_cfg = get_model_cfg(cfg, "z-image")
        aspect = args.aspect or "1:1"
        if steps is None:
            steps = model_cfg.get("default_steps", 9)
        output_dir = ensure_output_dir(cfg, "z-image", args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timeout = model_cfg.get("timeout_seconds", 100)
        workflow, prompt_type_str, seed_used = prepare_t2i_workflow(cfg, prompt, aspect, seed, steps, "z-image")
    
    prompt_id, err_msg, errs = send_prompt_with_errors(cfg, workflow, timeout)
    if prompt_id is None:
        for w in errs:
            print(w)
        sys.exit(1)
    
    history = wait_for_completion(cfg, prompt_id, timeout)
    images = get_output_images(history, prompt_id, output_dir)
    if not images:
        print("❌ No images found in output!")
        sys.exit(1)
    
    b64_images = [image_b64_from_comfyui(cfg, img) for img in images]
    fmt, jpg_quality = get_output_fmt_args(cfg, args)
    local_paths = [save_b64_image(b64, img["filename"], output_dir, fmt, jpg_quality)
                   for b64, img in zip(b64_images, images)]
    print_result(prompt_type_str, prompt, images, local_paths, output_dir, cfg, seed_used)

def cmd_i2i(cfg: dict, args: argparse.Namespace) -> None:
    import random
    raw_images = args.image if isinstance(args.image, list) else [args.image]
    image_paths = [Path(p).expanduser() for p in raw_images]
    for p in image_paths:
        if not p.exists():
            print(f"❌ Image not found: {p}", file=sys.stderr)
            sys.exit(1)

    default_model = cfg.get("default_model", {}).get("i2i", "qwen_imageedit")
    model_id = args.model or default_model

    if getattr(args, "no_fallback", False):
        _run_i2i_single(cfg, args, model_id)
        return
    _run_with_fallback(cfg, args, "i2i")

def _run_i2i_single(cfg: dict, args, model_id: str) -> None:
    """Single-model i2i run (used with --no-fallback)."""
    import random
    prompt = args.prompt
    raw_images = args.image if isinstance(args.image, list) else [args.image]
    image_paths = [Path(p).expanduser() for p in raw_images]
    seed = args.seed
    steps = args.steps
    if seed is None:
        seed = random.randint(0, 2**63 - 1)

    if model_id == "qwen21t":
        model_cfg = get_model_cfg(cfg, "qwen21t")
        if steps is None:
            steps = model_cfg.get("default_steps", 8)
        output_dir = ensure_output_dir(cfg, "qwen21t", args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timeout = model_cfg.get("timeout_seconds", 600)
        if len(image_paths) > 1:
            print(f"   Multi-image mode: {len(image_paths)} reference images")
        workflow, prompt_type_str, seed_used = prepare_qwen21_workflow(
            cfg, prompt, aspect=args.aspect,  # None = follow first reference image's ratio
            seed=seed, steps=steps, images=[str(p) for p in image_paths],
            negative=getattr(args, 'negative', '') or "", variant="qwen21t")
    elif model_id == "qwen21":
        model_cfg = get_qwen21_model_cfg(cfg)
        if steps is None:
            steps = model_cfg.get("default_steps", 25)
        output_dir = ensure_output_dir(cfg, "qwen21", args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timeout = model_cfg.get("timeout_seconds", 600)
        if len(image_paths) > 1:
            print(f"   Multi-image mode: {len(image_paths)} reference images")
        workflow, prompt_type_str, seed_used = prepare_qwen21_workflow(
            cfg, prompt, aspect=args.aspect,  # None = follow first reference image's ratio
            seed=seed, steps=steps, images=[str(p) for p in image_paths],
            negative=getattr(args, 'negative', '') or "")
    else:
        if len(image_paths) != 1:
            print(f"❌ Model '{model_id}' supports a single input image only", file=sys.stderr)
            sys.exit(1)
        model_cfg = get_model_cfg(cfg, model_id)
        output_dir = ensure_output_dir(cfg, model_id, args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timeout = model_cfg.get("timeout_seconds", 600)
        if steps is None:
            steps = model_cfg.get("default_steps", 4)
        workflow, prompt_type_str, _uploaded_fn, seed_used = prepare_i2i_workflow(cfg, prompt, str(image_paths[0]), seed, steps)
    prompt_id, err_msg, errs = send_prompt_with_errors(cfg, workflow, timeout)
    if prompt_id is None:
        for w in errs:
            print(w)
        sys.exit(1)
    
    history = wait_for_completion(cfg, prompt_id, timeout)
    images = get_output_images(history, prompt_id, output_dir)
    if not images:
        print("❌ No images found in output!", file=sys.stderr)
        sys.exit(1)
    
    b64_images = [image_b64_from_comfyui(cfg, img) for img in images]
    fmt, jpg_quality = get_output_fmt_args(cfg, args)
    local_paths = [save_b64_image(b64, img["filename"], output_dir, fmt, jpg_quality)
                   for b64, img in zip(b64_images, images)]
    print_result(prompt_type_str, prompt, images, local_paths, output_dir, seed=seed_used)

# ---------------------------------------------------------------------------
# i2m — Image to 3D Mesh (Hunyuan 3D v2.1)
#
# Pipeline: source image -> character extraction (transparent PNG) ->
# Hunyuan 3D v2.1 image-to-mesh -> downloaded GLB file.
#
# SaveGLB (core ComfyUI) emits history outputs as {"3d": [{filename, subfolder,
# type}]} per node — see comfy_extras/nodes_save_3d.py. The GLB bytes come
# through /view like any output file (mimetypes guesses the content type).
# ---------------------------------------------------------------------------

def get_mesh_model_cfg(cfg: dict, model_id: str) -> dict:
    return get_model_cfg(cfg, model_id)


def extract_character_i2i(cfg: dict, image_path: str, model_id: str, prompt_suffix: str,
                           steps: int = None, aspect: str = "1:1") -> Path:
    """Extract the main character from an image into a clean centered cutout
    (transparent background) using the skill's I2I model, saved as PNG.

    The Hunyuan 3D CLIP-vision conditioning wants the subject centered on a
    clean background; a raw photo's scenery becomes mesh junk otherwise.
    """
    model_cfg = get_qwen21_model_cfg(cfg) if model_id == "qwen21" else get_model_cfg(cfg, model_id)
    output_dir = ensure_output_dir(cfg, model_id)
    output_dir.mkdir(parents=True, exist_ok=True)
    timeout = model_cfg.get("timeout_seconds", 600)
    workflow, _label, _seed = prepare_qwen21_workflow(
        cfg, prompt_suffix, aspect=aspect, steps=steps,
        images=[str(image_path)])
    prompt_id, err_msg, warns = send_prompt_with_errors(cfg, workflow, timeout,
                                                        skip_autosubstitute=True)
    for w in warns:
        print(w)
    if prompt_id is None:
        raise RuntimeError(f"character extraction failed: {err_msg}")
    history = wait_for_completion(cfg, prompt_id, timeout)
    status_str = history.get(prompt_id, {}).get("status", {}).get("status_str", "")
    if status_str == "error":
        raise RuntimeError("character extraction: server sampling error")
    images = get_output_images(history, prompt_id, output_dir)
    if not images:
        raise RuntimeError("character extraction: no output images")
    b64 = image_b64_from_comfyui(cfg, images[0])
    out_path = save_b64_image(b64, images[0]["filename"], output_dir, "png", 95)
    return out_path


def extract_character_rembg(cfg: dict, image_path: str) -> Path:
    """Hard character cutout via the Rembg node (u2net human segmentation):
    pixel-precise transparent PNG, no generative re-draw.

    Used with `--extract rembg`. If the Rembg node is missing (older ComfyUI
    / no rembg installed), the error path reports the fix.
    """
    workflow = {
        "1": {"class_type": "LoadImage", "inputs": {"image": "__upload__"}},
        "2": {"class_type": "Image Rembg (Remove Background)",
             "inputs": {"images": ["1", 0], "transparency": True,
                        "model": "u2net_human_seg", "post_processing": True}},
        "3": {"class_type": "SaveImage",
             "inputs": {"filename_prefix": _save_prefix("mcut"), "images": ["2", 0]}},
    }
    uploaded = upload_image_to_comfyui(cfg, image_path)
    workflow["1"]["inputs"]["image"] = uploaded
    output_dir = ensure_output_dir(cfg, None)
    output_dir.mkdir(parents=True, exist_ok=True)
    prompt_id, err_msg, warns = send_prompt_with_errors(cfg, workflow, 300,
                                                        skip_autosubstitute=True)
    for w in warns:
        print(w)
    if prompt_id is None:
        raise RuntimeError(f"rembg extraction failed: {err_msg} "
                           "(rembg not installed on the server?)")
    history = wait_for_completion(cfg, prompt_id, 300)
    status_str = history.get(prompt_id, {}).get("status", {}).get("status_str", "")
    if status_str == "error":
        raise RuntimeError("rembg extraction: server sampling error")
    images = get_output_images(history, prompt_id, output_dir)
    if not images:
        raise RuntimeError("rembg extraction: no output images")
    b64 = image_b64_from_comfyui(cfg, images[0])
    return save_b64_image(b64, images[0]["filename"], output_dir, "png", 95)


def prepare_hunyuan3d_workflow(cfg: dict, image_path: str, seed: int = None,
                                steps: int = None, cfg_scale: float = None,
                                resolution: int = None) -> tuple[dict, str, int]:
    """Prepare the Hunyuan 3D v2.1 image-to-mesh workflow for one source image."""
    import random
    model_cfg = get_mesh_model_cfg(cfg, "hunyuan3d_v2.1")
    workflow_path = resolve_skill_path(model_cfg["workflow_path"])
    with open(workflow_path, "r", encoding="utf-8") as f:
        workflow = json.load(f)

    if seed is None:
        seed = random.randint(0, 2**63 - 1)
    steps = steps if steps is not None else model_cfg.get("default_steps", 30)
    cfg_scale = cfg_scale if cfg_scale is not None else model_cfg.get("default_cfg", 5.0)
    resolution = resolution if resolution is not None else model_cfg.get("default_resolution", 4096)

    uploaded = upload_image_to_comfyui(cfg, image_path)
    for node_id, node_data in find_nodes_by_class(workflow, "LoadImage"):
        node_data["inputs"]["image"] = uploaded
    for node_id, node_data in find_nodes_by_class(workflow, "KSampler"):
        node_data["inputs"]["seed"] = seed
        node_data["inputs"]["steps"] = steps
        node_data["inputs"]["cfg"] = cfg_scale
    for node_id, node_data in find_nodes_by_class(workflow, "EmptyLatentHunyuan3Dv2"):
        node_data["inputs"]["resolution"] = resolution
    # Timestamped GLB output prefix (SaveGLB: no trailing-'_' quirk of SaveImage;
    # keep the scheme consistent with the other modes anyway).
    for node_id, node_data in find_nodes_by_class(workflow, "SaveGLB"):
        node_data["inputs"]["filename_prefix"] = "mesh/" + _save_prefix("i2m")

    workflow = apply_keep_resident(cfg, workflow)
    return workflow, "Hunyuan 3D v2.1 i2m", seed


def get_output_3d_files(history: dict, prompt_id: str, output_dir: Path = None) -> list[dict]:
    """Extract 3D file entries from a prompt result (SaveGLB's `ui.3d` list).

    Mirrors get_output_images: sanitizes filenames against path traversal.
    """
    files = []
    for node_id, node_result in history.get(prompt_id, {}).get("outputs", {}).items():
        for item in node_result.get("3d", []):
            if not isinstance(item, dict) or item.get("type") != "output":
                continue
            safe_name = sanitize_filename(item.get("filename", ""), output_dir)
            if safe_name is None:
                print(f"⚠️ Skipping unsafe 3D filename from ComfyUI", file=sys.stderr)
                continue
            files.append({
                "filename": safe_name,
                "subfolder": item.get("subfolder", ""),
                "type": item.get("type", "output"),
            })
    return files


def file_b64_from_comfyui(cfg: dict, f: dict) -> str:
    """Download any output file (GLB etc.) via /view, base64-encoded."""
    params = urllib.parse.urlencode({
        "filename": f["filename"],
        "subfolder": f.get("subfolder", ""),
        "type": f.get("type", "output"),
    })
    req = urllib.request.Request(
        f"{api_url(cfg, '/view')}?{params}",
        method="GET",
        headers=auth_headers(cfg),
    )
    with urllib.request.urlopen(req, timeout=cfg.get("timeout_seconds", 120)) as resp:
        return base64.b64encode(resp.read()).decode("utf-8")


def save_3d_file(b64_data: str, filename: str, output_dir: Path) -> Path:
    safe_name = sanitize_filename(filename, output_dir)
    if safe_name is None:
        safe_name = f"mesh_{int(time.time())}.glb"
    safe_name = _strip_trailing_underscore(safe_name)
    output_path = output_dir / safe_name
    with open(output_path, "wb") as fp:
        fp.write(base64.b64decode(b64_data))
    return output_path


def scale_glb_inplace(glb_path: Path, factor: float) -> list:
    """Scale a GLB's POSITION data in place by `factor` (around the origin).

    Hunyuan 3D v2.1 emits a normalized, unit-scale mesh (character height
    ≈ 2 units; the GLB declares no units, so by glTF convention it reads as
    a ~2 m figure). The delivery convention is a x3000 scale, so positions
    (and the accessor min/max) are scaled before the GLB gets zipped.
    Returns the new bounding box [min, max] of the first mesh (or []).
    """
    import struct
    raw = open(glb_path, "rb").read()
    magic, ver, _total = struct.unpack_from("<III", raw, 0)
    if magic != 0x46546C67 or ver != 2:
        raise RuntimeError("scale_glb: not a GLB v2 file")
    off, gltf, bin_body = 12, None, None
    while off < len(raw):
        clen, ctype = struct.unpack_from("<II", raw, off)
        body = raw[off + 8: off + 8 + clen]
        if ctype == 0x4E4F534A:
            gltf = json.loads(body.rstrip(b"\x00").decode("utf-8"))
        elif ctype == 0x004E4942:
            bin_body = bytearray(body)
        off += 8 + clen
    if gltf is None or bin_body is None:
        raise RuntimeError("scale_glb: GLB has no JSON/BIN chunk")
    bvs, accs = gltf.get("bufferViews", []), gltf.get("accessors", [])
    comp_sizes = {5126: 4, 5125: 4, 5121: 2, 5123: 2, 5120: 1, 5122: 1}
    first_bbox = None
    for m in gltf.get("meshes", []):
        for prim in m.get("primitives", []):
            pos_idx = prim.get("attributes", {}).get("POSITION")
            if pos_idx is None or not isinstance(pos_idx, int) or pos_idx >= len(accs):
                continue
            acc = accs[pos_idx]
            bv = bvs[acc["bufferView"]]
            comp_size = comp_sizes.get(acc.get("componentType"))
            if comp_size is None:
                continue
            count = acc["count"]
            stride = bv.get("byteStride") or (3 * comp_size)
            base = bv.get("byteOffset", 0)
            for i in range(count):
                o = base + i * stride
                for c in range(3):
                    v = struct.unpack_from("<f", bin_body, o + c * comp_size)[0] * factor
                    struct.pack_into("<f", bin_body, o + c * comp_size, v)
            if "min" in acc and "max" in acc:
                acc["min"] = [v * factor for v in acc["min"]]
                acc["max"] = [v * factor for v in acc["max"]]
                if first_bbox is None:
                    first_bbox = [acc["min"], acc["max"]]
    for n in gltf.get("nodes", []):
        if isinstance(n.get("translation"), list) and len(n["translation"]) == 3:
            n["translation"] = [v * factor for v in n["translation"]]
    # Rebuild: JSON chunk (space-padded) + BIN chunk (zero-padded), 4-byte aligned.
    def pad4(b: bytes, ch: bytes) -> bytes:
        return b + ch * ((-len(b)) % 4)
    json_body = pad4(json.dumps(gltf, separators=(",", ":")).encode("utf-8"), b" ")
    bin_out = pad4(bytes(bin_body), b"\x00")
    header = struct.pack("<III", 0x46546C67, 2,
                         12 + 8 + len(json_body) + 8 + len(bin_out))
    with open(glb_path, "wb") as fp:
        fp.write(header
                 + struct.pack("<II", len(json_body), 0x4E4F534A) + json_body
                 + struct.pack("<II", len(bin_out), 0x004E4942) + bin_out)
    return first_bbox or []


def zip_mesh_files(local_paths: list[Path], output_dir: Path) -> Path:
    """Package the generated GLB file(s) into one zip for delivery.

    The GLB is always delivered as a zip attachment — see the i2m delivery
    rules in SKILL.md (never deliver the raw GLB, never render it).
    """
    import zipfile
    zip_path = output_dir / (local_paths[0].stem + ".zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in local_paths:
            zf.write(p, arcname=p.name)
    return zip_path


def print_result_mesh(mesh_files: list[dict], local_paths: list[Path],
                       output_dir: Path, seed: int = None,
                       extracted_png: Path = None,
                       zip_path: Path = None) -> None:
    for i, (m, p) in enumerate(zip(mesh_files, local_paths), 1):
        sz = p.stat().st_size / 1024
        print(f"✅ Mesh {i}: {p.name} ({sz:.0f} KB)")
        print(f"   File: {p}")
        if seed is not None:
            print(f"   Seed: {seed}")
    if zip_path is not None:
        print(f"   ZIP (send to user as attachment): {zip_path}")
    if extracted_png is not None:
        print(f"   CHARACTER IMAGE (send to user as an image): {extracted_png}")
    if zip_path is not None or extracted_png is not None:
        print("   Delivery: character image as image + ZIP as attachment; "
              "NEVER render the mesh (no GLB → image/video conversion)")


# ---------------------------------------------------------------------------
# pi2m — Image to 3D Mesh (Pixal3D / Trellis2, default I2M)
#
# Pipeline: source image (fed raw, the graph removes its own background via
# birefnet internally) -> Trellis2 latent diffusion -> GLB mesh. The mesh is
# already at a natural delivery scale (no x3000), so delivery scale defaults
# to 1. Save3DAdvanced emits history outputs as {"3d": [{filename,...}]} just
# like SaveGLB — see comfy_extras/nodes_save_3d.py; the GLB bytes come through
# /view like any output file.
# ---------------------------------------------------------------------------

def prepare_trellis2_workflow(cfg: dict, image_path: str, seed: int = None,
                             steps: int = None, cfg_scale: float = None,
                             resolution: int = None) -> tuple[dict, str, int]:
    """Prepare the Pixal3D / Trellis2 image-to-mesh workflow for one source image.

    The user-supplied graph is kept 1:1. Placeholder LoadImage `image` is
    rewritten to the uploaded filename (the script always does this), and the
    trellis2 KSampler seed is stamped per run.
    """
    import random
    model_cfg = get_mesh_model_cfg(cfg, "pi2m")
    workflow_path = resolve_skill_path(model_cfg["workflow_path"])
    with open(workflow_path, "r", encoding="utf-8") as f:
        workflow = json.load(f)

    if seed is None:
        seed = model_cfg.get("default_seed", random.randint(0, 2**63 - 1))
    # steps/cfg/resolution are graph-own defaults here (the trellis2 graph has
    # no single `EmptyLatent` resolution to stamp; keep the CLI passthrough
    # shape consistent but only apply seed + cfg which the graph's KSamplers
    # already carry. resolution is ignored by this graph.
    steps = steps if steps is not None else model_cfg.get("default_steps")
    cfg_scale = cfg_scale if cfg_scale is not None else model_cfg.get("default_cfg")

    uploaded = upload_image_to_comfyui(cfg, image_path)
    for node_id, node_data in find_nodes_by_class(workflow, "LoadImage"):
        node_data["inputs"]["image"] = uploaded
    for node_id, node_data in find_nodes_by_class(workflow, "KSampler"):
        node_data["inputs"]["seed"] = seed
        if steps is not None:
            node_data["inputs"]["steps"] = steps
        if cfg_scale is not None:
            node_data["inputs"]["cfg"] = cfg_scale

    workflow = apply_keep_resident(cfg, workflow)
    return workflow, "Pixal3D / Trellis2 i2m", seed


def cmd_pi2m(cfg: dict, args: argparse.Namespace) -> None:
    """Image -> 3D mesh: Pixal3D / Trellis2 (default I2M).

    The source image feeds straight into the graph — it removes its own
    background internally (birefnet), so no client-side character extraction
    is performed. The mesh is delivered at its natural scale.
    """
    image_path = Path(args.image).expanduser()
    if not image_path.exists():
        print(f"❌ Image not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    model_cfg = get_mesh_model_cfg(cfg, "pi2m")
    timeout = model_cfg.get("timeout_seconds", 1500)
    output_dir = ensure_output_dir(cfg, "pi2m", args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("ℹ️ pi2m feeds the source image directly (the graph removes its own "
          "background internally; no client-side extraction)")

    seed = args.seed if args.seed is not None else model_cfg.get("default_seed")
    print("🧊 Generating 3D mesh (Pixal3D / Trellis2) ...")
    workflow, label, seed_used = prepare_trellis2_workflow(
        cfg, str(image_path), seed=seed,
        steps=args.steps, cfg_scale=args.cfg, resolution=args.resolution)

    prompt_id, err_msg, warns = send_prompt_with_errors(cfg, workflow, timeout,
                                                        skip_autosubstitute=True)
    for w in warns:
        print(w)
    if prompt_id is None:
        print(f"❌ pi2m failed to queue: {err_msg}", file=sys.stderr)
        print("   This graph needs the Pixal3D / Trellis2 custom nodes and their",
              file=sys.stderr)
        print("   checkpoint files (trellis_2_int8_convrot.safetensors, the",
              file=sys.stderr)
        print("   Trellis2 VAEs, moge_2_vitl_normal_fp16.safetensors, and",
              file=sys.stderr)
        print("   birefnet.safetensors) installed on the ComfyUI server.",
              file=sys.stderr)
        sys.exit(1)

    try:
        history = wait_for_completion(cfg, prompt_id, timeout)
    except TimeoutError:
        print(f"❌ Mesh generation timed out after {timeout}s (prompt_id={prompt_id})",
              file=sys.stderr)
        sys.exit(1)
    status_str = history.get(prompt_id, {}).get("status", {}).get("status_str", "")
    if status_str == "error":
        node_msgs = history.get(prompt_id, {}).get("status", {}).get("messages", [])
        print(f"❌ Mesh generation error: {node_msgs}", file=sys.stderr)
        sys.exit(1)

    mesh_files = get_output_3d_files(history, prompt_id, output_dir)
    if not mesh_files:
        print("❌ No GLB file in the output!", file=sys.stderr)
        sys.exit(1)

    local_paths = [save_3d_file(file_b64_from_comfyui(cfg, m), m["filename"], output_dir)
                   for m in mesh_files]
    # Trellis2/Pixal3D already emit at a natural delivery scale — the mesh
    # carries its own units, so we do NOT apply a x3000 upscale. delivery
    # scale therefore defaults to 1.
    scale = args.scale if args.scale is not None else model_cfg.get("default_scale", 1)
    if scale and scale != 1.0:
        for p in local_paths:
            bbox = scale_glb_inplace(p, float(scale))
            if bbox:
                mn, mx = bbox
                print(f"   Scaled ×{scale:g}: {mn[0]:.1f}–{mx[0]:.1f} × "
                      f"{mn[1]:.1f}–{mx[1]:.1f} × {mn[2]:.1f}–{mx[2]:.1f} units "
                      f"({mx[1]-mn[1]:.0f} tall)")
            else:
                print(f"   Scaled ×{scale:g} (no min/max metadata in the GLB)")
    else:
        print(f"   Delivery scale {scale}: Trellis2/Pixal3D mesh kept at its "
              f"natural units (no ×3000 upscale)")
    zip_path = zip_mesh_files(local_paths, output_dir)
    print(f"✅ Mesh: {local_paths[0].name} ({len(local_paths)} file(s))")
    print(f"   File: {local_paths[0]}")
    print(f"   ZIP (send to user as attachment): {zip_path}")
    print(f"   Seed: {seed_used}")
    print("   Delivery: ZIP as attachment; NEVER render the mesh (no GLB → "
          "image/video conversion)")


def cmd_hyi2m(cfg: dict, args: argparse.Namespace) -> None:
    """Image -> 3D mesh: Hunyuan 3D v2.1 (kept as hyi2m).

    Identical to the legacy `i2m` command — renamed to avoid the collision when
    the default I2M model became pi2m.
    """
    cmd_i2m(cfg, args)


def cmd_i2m(cfg: dict, args: argparse.Namespace) -> None:
    """Image -> 3D mesh: optional character extraction, then Hunyuan 3D v2.1."""
    import random
    image_path = Path(args.image).expanduser()
    if not image_path.exists():
        print(f"❌ Image not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    model_cfg = get_mesh_model_cfg(cfg, "hunyuan3d_v2.1")
    timeout = model_cfg.get("timeout_seconds", 900)
    output_dir = ensure_output_dir(cfg, "hunyuan3d_v2.1", args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1 — character extraction (transparent PNG)
    extract_mode = args.extract
    if extract_mode == "none":
        extract_png = image_path
        print("ℹ️ --extract none: using the source image directly as the 3D input")
    else:
        extract_cfg = model_cfg.get("extract", {})
        if extract_mode == "auto":
            extract_mode = extract_cfg.get("workflow", "i2i")
        print(f"🔍 Extracting main character ({extract_mode}) ...")
        try:
            if extract_mode == "rembg":
                extract_png = extract_character_rembg(cfg, str(image_path))
            else:
                extract_png = extract_character_i2i(
                    cfg, str(image_path),
                    extract_cfg.get("model", "qwen21"),
                    extract_cfg.get("prompt_suffix", ""),
                    steps=args.steps_extract,
                    aspect=extract_cfg.get("aspect", "1:1"),
                )
        except Exception as e:
            print(f"⚠️ Character extraction failed ({e}) — continuing with the original image",
                  file=sys.stderr)
            extract_png = image_path
        print(f"   → {extract_png}")

    # Step 2 — Hunyuan 3D v2.1 image-to-mesh
    seed = args.seed if args.seed is not None else random.randint(0, 2**63 - 1)
    print("🧊 Generating 3D mesh (Hunyuan 3D v2.1) ...")
    workflow, label, seed_used = prepare_hunyuan3d_workflow(
        cfg, str(extract_png), seed=seed,
        steps=args.steps, cfg_scale=args.cfg, resolution=args.resolution)

    prompt_id, err_msg, warns = send_prompt_with_errors(cfg, workflow, timeout,
                                                        skip_autosubstitute=True)
    for w in warns:
        print(w)
    if prompt_id is None:
        print(f"❌ i2m failed to queue: {err_msg}", file=sys.stderr)
        print("   Hunyuan 3D v2.1 needs the `hunyuan_3d_v2.1.safetensors` checkpoint in",
              file=sys.stderr)
        print("   ComfyUI/models/checkpoints/ and core nodes from ComfyUI >= 0.37.0.",
              file=sys.stderr)
        sys.exit(1)

    try:
        history = wait_for_completion(cfg, prompt_id, timeout)
    except TimeoutError:
        print(f"❌ Mesh generation timed out after {timeout}s (prompt_id={prompt_id})",
              file=sys.stderr)
        sys.exit(1)
    status_str = history.get(prompt_id, {}).get("status", {}).get("status_str", "")
    if status_str == "error":
        node_msgs = history.get(prompt_id, {}).get("status", {}).get("messages", [])
        print(f"❌ Mesh generation error: {node_msgs}", file=sys.stderr)
        sys.exit(1)

    mesh_files = get_output_3d_files(history, prompt_id, output_dir)
    if not mesh_files:
        print("❌ No GLB file in the output!", file=sys.stderr)
        sys.exit(1)

    local_paths = [save_3d_file(file_b64_from_comfyui(cfg, m), m["filename"], output_dir)
                   for m in mesh_files]
    # Step 3 — delivery scaling: the Hunyuan 3D v2.1 mesh comes out at a
    # normalized unit scale (character ≈ 2 units, no declared units); scale
    # it up before zipping (convention: x3000).
    scale = args.scale if args.scale is not None else model_cfg.get("default_scale", 3000)
    if scale and scale != 1.0:
        for p in local_paths:
            bbox = scale_glb_inplace(p, float(scale))
            if bbox:
                mn, mx = bbox
                print(f"   Scaled ×{scale:g}: {mn[0]:.1f}–{mx[0]:.1f} × "
                      f"{mn[1]:.1f}–{mx[1]:.1f} × {mn[2]:.1f}–{mx[2]:.1f} units "
                      f"({mx[1]-mn[1]:.0f} tall)")
            else:
                print(f"   Scaled ×{scale:g} (no min/max metadata in the GLB)")
    zip_path = zip_mesh_files(local_paths, output_dir)
    print_result_mesh(mesh_files, local_paths, output_dir, seed_used,
                      extract_png, zip_path)


def cmd_test(cfg: dict, args: argparse.Namespace) -> None:
    url = cfg["comfyui_url"].rstrip("/") + "/history"
    try:
        req = urllib.request.Request(url, method="GET", headers=auth_headers(cfg))
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode()
        print(f"✅ ComfyUI is reachable at {cfg['comfyui_url']}")
        print(f"   Response: {data[:100]}")
    except Exception as e:
        _endpoint_setup_help(cfg, e)
        sys.exit(1)

def prepare_wan2_2_i2v_workflow(cfg: dict, prompt: str, image_path: str,
                                 width: int = None, height: int = None,
                                 length: int = None, steps: int = None,
                                 seed: int = None, negative: str = "") -> tuple[dict, str, str, int]:
    import random, time
    model_cfg = get_model_cfg(cfg, "wan2.2_i2v")
    default_w = model_cfg.get("default_width", 528)
    default_h = model_cfg.get("default_height", 768)
    default_len = model_cfg.get("default_length", 81)
    default_steps = model_cfg.get("default_steps", 4)
    
    if seed is None:
        seed = random.randint(0, 2**63 - 1)
    w = width if width is not None else default_w
    h = height if height is not None else default_h
    l = length if length is not None else default_len
    s = steps if steps is not None else default_steps
    
    workflow_path = resolve_skill_path(model_cfg["workflow_path"])
    with open(workflow_path, "r", encoding="utf-8") as f:
        workflow = json.load(f)
    
    uploaded_filename = upload_image_to_comfyui(cfg, image_path)
    for node_id, node_data in find_nodes_by_class(workflow, "LoadImage"):
        workflow[node_id]["inputs"]["image"] = uploaded_filename
    
    clip_nodes = find_nodes_by_class(workflow, "CLIPTextEncode")
    for node_id, node_data in clip_nodes:
        if "clip" in node_data.get("inputs", {}):
            if "the girl" in str(node_data.get("inputs", {}).get("text", "")):
                workflow[node_id]["inputs"]["text"] = prompt
            else:
                workflow[node_id]["inputs"]["text"] = negative if negative else ""
    
    for node_id, node_data in find_nodes_by_class(workflow, "WanImageToVideo"):
        workflow[node_id]["inputs"]["width"] = w
        workflow[node_id]["inputs"]["height"] = h
        workflow[node_id]["inputs"]["length"] = l
    
    for node_id, node_data in find_nodes_by_class(workflow, "WanMoeKSamplerAdvanced"):
        workflow[node_id]["inputs"]["steps"] = s
    for node_id, node_data in find_nodes_by_class(workflow, "Seed (rgthree)"):
        safe_seed = abs(seed) % (1125899906842624 + 1)
        workflow[node_id]["inputs"]["seed"] = safe_seed
    
    timestamp = time.strftime("%Y-%m-%d/%H%M%S")
    for node_id, node_data in find_nodes_by_class(workflow, "VHS_VideoCombine"):
        workflow[node_id]["inputs"]["filename_prefix"] = f"ComfyUI_{timestamp}"
    
    workflow = apply_keep_resident(cfg, workflow)
    return workflow, "Wan2.2 I2V", uploaded_filename, seed

def cmd_wan2_2_i2v(cfg: dict, args: argparse.Namespace) -> None:
    prompt = args.prompt
    image_path = Path(args.image).expanduser()
    if not image_path.exists():
        print(f"❌ Image not found: {image_path}", file=sys.stderr)
        sys.exit(1)
    
    model_cfg = get_model_cfg(cfg, "wan2.2_i2v")
    length = args.length if args.length is not None else model_cfg.get("default_length", 81)
    steps = args.steps if args.steps is not None else model_cfg.get("default_steps", 4)
    seed = args.seed
    negative = args.negative or ""
    output_dir = ensure_output_dir(cfg, "wan2.2_i2v", args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Auto-detect resolution from image aspect ratio
    if args.width is not None and args.height is not None:
        width, height = args.width, args.height
    else:
        from PIL import Image
        try:
            with Image.open(str(image_path)) as img:
                iw, ih = img.size
                # Find closest matching Wan2.2 resolution from ALL available options
                width, height = find_closest_wan2_2_resolution(iw, ih)
                print(f"   Detected image size {iw}x{ih}, using {width}x{height}")
        except Exception as e:
            width = model_cfg.get("default_width", 560)
            height = model_cfg.get("default_height", 720)
    
    workflow, prompt_type_str, uploaded_fn, seed_used = prepare_wan2_2_i2v_workflow(
        cfg, prompt, str(image_path), width, height, length, steps, seed, negative
    )
    timeout = model_cfg.get("timeout_seconds", 1000)
    prompt_id, err_msg, errs = send_prompt_with_errors(cfg, workflow, timeout)
    if prompt_id is None:
        for w in errs:
            print(w)
        sys.exit(1)
    
    history = wait_for_completion(cfg, prompt_id, timeout)
    videos = get_output_videos(history, prompt_id, model_cfg, output_dir)
    if not videos:
        print("❌ No videos found in output!", file=sys.stderr)
        sys.exit(1)
    
    b64_videos = [video_b64_from_comfyui(cfg, v) for v in videos]
    local_paths = [save_b64_video(b64, v["filename"], output_dir)
                   for b64, v in zip(b64_videos, videos)]
    print_result_video(prompt_type_str, prompt, videos, local_paths, output_dir, cfg, seed_used)

# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="ComfyUI media generation client (T2I / I2I / I2V / I2M)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # t2i
    p_t2i = subparsers.add_parser("t2i", help="Text-to-Image generation")
    p_t2i.add_argument("--prompt", required=True, help="Text prompt")
    p_t2i.add_argument("--aspect", default="1:1", choices=list(ASPECT_RATIOS.keys()),
                         help="Aspect ratio (optional; default 1:1 = 1024x1024)")
    p_t2i.add_argument("--model", default=None,
                         choices=["qwen21", "z-image", "sd35"],
                         help="Model: qwen21t (Qwen-Image 2.1 Turbo, default) / qwen21 (Qwen-Image 2.1) / z-image / sd35")
    p_t2i.add_argument("--seed", type=int, default=None)
    p_t2i.add_argument("--steps", type=int, default=None)
    p_t2i.add_argument("--cfg", type=float, default=None, help="CFG scale (SD3.5 only)")
    p_t2i.add_argument("--negative", default="",
                        help="Negative prompt (Qwen-Image 2.1 and SD3.5; ignored by z-image)")
    p_t2i.add_argument("--output-dir", default=None)
    p_t2i.add_argument("--format", default=None, choices=["png", "jpg"],
                        help="Output image format (jpg is converted client-side, PNG fallback)")
    p_t2i.add_argument("--jpg-quality", type=int, default=None,
                        help="JPG quality 1-100 (default: config image.jpg_quality or 89)")
    p_t2i.add_argument("--no-fallback", action="store_true",
                        help="Disable the runtime fallback chain (run only the requested model)")

    # i2i
    p_i2i = subparsers.add_parser("i2i", help="Image-to-Image / Edit generation (multi-image capable)")
    p_i2i.add_argument("--prompt", required=True,
                        help="Edit instructions; for multi-image, reference images as <image1>, <image2>, ...")
    p_i2i.add_argument("--image", required=True, nargs="+",
                        help="Source image file path(s). Pass 2..16 paths for multi-image reference mode")
    p_i2i.add_argument("--model", default=None, choices=["qwen21t", "qwen21", "qwen_imageedit"],
                        help="Model: qwen21t (Qwen-Image 2.1 Turbo, default) / qwen21 (Qwen-Image 2.1) / qwen_imageedit (2511 legacy)")
    p_i2i.add_argument("--aspect", default=None, choices=list(QWEN21_ASPECT_PRESETS.keys()),
                        help="Aspect ratio (optional, qwen21t/qwen21 only; unset = output canvas matches the first "
                             "reference image's size via the workflow's latent switch. Setting it routes the "
                             "canvas through the ResolutionSelector at that ratio, e.g. portrait photo -> 16:9)")
    p_i2i.add_argument("--seed", type=int, default=None)
    p_i2i.add_argument("--steps", type=int, default=None)
    p_i2i.add_argument("--negative", default="",
                        help="Negative prompt (qwen21t / qwen21 only; qwen_imageedit is positive-only)")
    p_i2i.add_argument("--output-dir", default=None)
    p_i2i.add_argument("--format", default=None, choices=["png", "jpg"],
                        help="Output image format (jpg is converted client-side, PNG fallback)")
    p_i2i.add_argument("--jpg-quality", type=int, default=None,
                        help="JPG quality 1-100 (default: config image.jpg_quality or 89)")
    p_i2i.add_argument("--no-fallback", action="store_true",
                        help="Disable the runtime fallback chain (run only the requested model)")

    # i2m / hyi2m (image -> 3D mesh, Hunyuan 3D v2.1).
    # `hyi2m` is the canonical entry point; `i2m` is kept for backwards
    # compatibility (both call the same command below).
    p_i2m = subparsers.add_parser("i2m", help="Image to 3D Mesh (Hunyuan 3D v2.1 -> GLB) [legacy; prefer hyi2m]")
    p_hyi2m = subparsers.add_parser("hyi2m", help="Image to 3D Mesh (Hunyuan 3D v2.1 -> GLB)")
    for p in (p_i2m, p_hyi2m):
        p.add_argument("--image", required=True,
                       help="Source image file path (the character to turn into a 3D mesh)")
        p.add_argument("--extract", default="auto",
                       choices=["auto", "i2i", "rembg", "none"],
                       help="Character extraction before 3D generation: auto (config) / "
                            "i2i (Qwen-Image 2.1 redraw on transparent bg, default) / "
                            "rembg (u2net hard cutout) / none (use the image as-is)")
        p.add_argument("--resolution", type=int, default=None,
                       help="3D latent resolution (default: config default_resolution, 4096)")
        p.add_argument("--steps", type=int, default=None,
                       help="Sampler steps (default: config default_steps, 30)")
        p.add_argument("--cfg", type=float, default=None,
                       help="CFG scale (default: config default_cfg, 5.0)")
        p.add_argument("--seed", type=int, default=None)
        p.add_argument("--scale", type=float, default=None,
                       help="Delivery scale factor for the GLB (default: config "
                            "mesh.hunyuan3d_v2.1.default_scale, 3000; 1 = keep the "
                            "normalized mesh unscaled)")
        p.add_argument("--steps-extract", type=int, default=None,
                       help="Steps for the i2i extraction pass (default: model config, 25)")
        p.add_argument("--output-dir", default=None)

    # pi2m (image -> 3D mesh, default: Pixal3D / Trellis2 -> GLB)
    p_pi2m = subparsers.add_parser("pi2m", help="Image to 3D Mesh (Pixal3D / Trellis2, default -> GLB)")
    p_pi2m.add_argument("--image", required=True,
                       help="Source image file path (the subject to turn into a 3D mesh)")
    p_pi2m.add_argument("--steps", type=int, default=None,
                       help="Sampler steps (default: config default_steps)")
    p_pi2m.add_argument("--cfg", type=float, default=None,
                       help="CFG scale (default: config default_cfg)")
    p_pi2m.add_argument("--resolution", type=int, default=None,
                       help="3D latent resolution (graph-own default; not stamped by this graph)")
    p_pi2m.add_argument("--seed", type=int, default=None)
    p_pi2m.add_argument("--scale", type=float, default=None,
                       help="Delivery scale factor for the GLB (default: config "
                            "mesh.pi2m.default_scale, 1; the Trellis2 mesh carries its "
                            "own units, so no x3000 upscale is applied)")
    p_pi2m.add_argument("--output-dir", default=None)

    # wan2.2
    p_wan22 = subparsers.add_parser("wan2.2", help="Wan2.2 Image-to-Video generation")
    p_wan22.add_argument("--prompt", required=True, help="Motion description")
    p_wan22.add_argument("--image", required=True, help="Input image file path")
    p_wan22.add_argument("--width", type=int, default=None)
    p_wan22.add_argument("--height", type=int, default=None)
    p_wan22.add_argument("--length", type=int, default=None)
    p_wan22.add_argument("--steps", type=int, default=None)
    p_wan22.add_argument("--seed", type=int, default=None)
    p_wan22.add_argument("--negative", default="")
    p_wan22.add_argument("--output-dir", default=None)

    # test
    subparsers.add_parser("test", help="Health check")

    args = parser.parse_args()
    cfg = load_config()

    if args.command in ("t2i", "i2i", "wan2.2", "i2m", "hyi2m", "pi2m"):
        ensure_comfyui_reachable(cfg)

    if args.command == "t2i":
        cmd_t2i(cfg, args)
    elif args.command == "i2i":
        cmd_i2i(cfg, args)
    elif args.command == "wan2.2":
        cmd_wan2_2_i2v(cfg, args)
    elif args.command == "i2m":
        cmd_hyi2m(cfg, args)
    elif args.command == "hyi2m":
        cmd_hyi2m(cfg, args)
    elif args.command == "pi2m":
        cmd_pi2m(cfg, args)
    elif args.command == "test":
        cmd_test(cfg, args)

if __name__ == "__main__":
    main()
