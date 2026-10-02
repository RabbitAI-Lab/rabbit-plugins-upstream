# Error Handling Reference (image-with-comfyui)

The script auto-detects two categories of server-side problems (missing nodes and
missing models) and reports them with install/source guidance. Open this for the
full behavior; the SKILL.md procedure only tells you "if you see ⚠️ report it".

## 1. Missing Node Detection

When a workflow references a custom node that isn't installed, the system detects it and reports:
- **Which node** is missing (class type name)
- **Which package** provides it
- **GitHub URL** for manual download
- **Manual install instruction** (the script does NOT execute git clone; ComfyUI may be on a remote server)

Example: If `ImpactKSamplerBasicPipe` is missing:
```
⚠️ Missing node: `ImpactKSamplerBasicPipe`
📦 Package: ComfyUI-Impact-Pack
🔗 GitHub: https://github.com/ltdrdata/ComfyUI-Impact-Pack
ℹ️ Install manually: see README "Required Custom Nodes" (pinned commit + venv; the script never runs git clone itself)
```

## 2. Missing Model Substitution

When a workflow references a model file that doesn't exist, the system attempts to find a compatible substitute:

| Requested Model | Substitute |
|---|---|
| `sd3.5_medium` variants | `sd3.5_large.safetensors` |
| WAN High → Low or vice versa | Swap between variants |
| Other unknown models | No substitution (error returned) |

Example: If `my_custom_sd3_medium_v2.safetensors` is missing:
```
⚠️ Model missing: `my_custom_sd3_medium_v2.safetensors`
🔄 Substituted: `sd3.5_large.safetensors`
📦 Loader: CheckpointLoaderSimple.ckpt_name
```

After substitution, the workflow is retried automatically with the substitute model.

## 3. Missing Utility Node Bypass (UnloadAllModels)

When the workflow references `UnloadAllModels` (a memory cleanup node) which isn't available, the system **automatically bypasses it** by rerouting the signal path:
- Removes the missing `UnloadAllModels` node
- Redirects the upstream processing node directly to the downstream output node
- Generation continues without interruption
- User receives a warning about the bypass

Example:
```
⚠️ Workflow missing node: `UnloadAllModels` (memory cleanup, non-critical)
🔄 Auto-bypassed — generation continues
```

## 4. Runtime Fallback Chain (t2i / i2i)

`t2i` and `i2i` commands run through a fallback engine (`_run_with_fallback`) instead of the single-model path. A run proceeds through ordered **tiers**:

| Kind | Tier order |
|---|---|
| t2i | `qwen21` → `z-image` → `sd35` → (any remaining server checkpoint, standard topology) |
| i2i | `qwen21` → `qwen_imageedit` |

- The **requested model** (via `--model` or the config default) is always the first tier; the remaining tiers follow in the order above.
- A tier fails on: send errors, server timeout (> `timeout_seconds`), `status_str == error`, or no output images.
- **Config problems do NOT degrade** — missing model files or missing nodes abort the chain with `config problem (missing model file / node) — no fallback` (install/fix the model instead of silently switching).
- **Server unreachable** mid-run is treated as an environment problem — every tier on the same server would fail identically, so the chain aborts.
- **Server unreachable before a run:** `t2i` / `i2i` / `wan2.2` pre-check the user-defined endpoint (GET `/history`, 5 s timeout) and, if nothing answers, exit with configuration instructions (start a ComfyUI server, set `COMFYUI_URL` or `comfyui_url` in `config.json`, verify with `test`) instead of failing mid-run with a raw timeout.
- **i2i never degrades blind:** a plain T2I model cannot honor the source image, so when the i2i tiers are exhausted the run exits with the available-model list for manual choice (no fallback to a text-only generation).
- When a lower tier succeeds, the output includes a note: `🔄 used <tier> — fell back because <failed tiers> failed this run.`
- `qwen_imageedit` skips the tier when the request has multiple input images (single-image model) and the chain continues.
- **`--no-fallback`** (t2i / i2i): run only the requested model — original single-model behavior, no runtime descent.

Example (qwen21 times out, z-image succeeds):

```
🎨 trying qwen21 ...
⚠️ tier qwen21 — failed: server timeout (>600s)
🎨 trying z-image ...
✅ 1 image(s) saved ...
🔄 used z-image — fell back because qwen21 failed this run.
```
