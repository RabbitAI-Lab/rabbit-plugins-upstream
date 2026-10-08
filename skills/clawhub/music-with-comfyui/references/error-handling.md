# Error Handling Reference (music-with-comfyui)

The script auto-detects the same categories of server-side problems as the
image skill (see references/error-handling.md for the shared contract). This
file notes the audio-specific differences.

## 1. Missing Node Detection

When the workflow references a node that isn't installed, the script reports:

- **Which node** is missing (class type name)
- **Which package** provides it
- **GitHub URL** for manual download
- **Manual install instruction** (the script never runs `git clone`)

For AceStep 1.5 the relevant packages are:

| Node | Package | Source |
|---|---|---|
| `TextEncodeAceStepAudio1.5`, `EmptyAceStep1.5LatentAudio` | AceStep-ComfyUI | https://github.com/AceStep/AceStep-ComfyUI |
| `VAEDecodeAudio` | ComfyUI-Audio | https://github.com/ligersearch/ComfyUI-Audio |
| `SaveAudioAdvanced` | ComfyUI-VideoHelperSuite | https://github.com/Fannovel16/ComfyUI-VideoHelperSuite |
| `ModelSamplingAuraFlow` | ComfyUI core node | update ComfyUI (no custom package) |

## 2. Missing Models — No Blind Substitution

Unlike the image skill, there is **only one** model in this workflow. If the
required files are missing the script aborts with the install hint rather than
substituting a compatible model:

```
❌ Music generation failed to queue: missing file(s)
   AceStep 1.5 needs `acestep_v1.5_xl_turbo_bf16.safetensors`
   plus `qwen_*_ace15.safetensors` (CLIP) and `ace_1.5_vae.safetensors`
   in the server's ComfyUI model folders.
```

There is no fallback tier — the run exits so the user can fix the model setup.

## 3. Non-Critical Utility Nodes

`UnloadAllModels` (and any `UnloadModel`) VRAM-cleanup nodes are bypassed
automatically if a given ComfyUI instance doesn't have them, without
interrupting generation — the same mechanism as the image skill.

## 4. Server Unreachable / Timeout

- **Before a run:** the script pre-checks the user-defined endpoint (GET
  `/history`, 5 s timeout) and, if nothing answers, exits with configuration
  instructions instead of failing mid-run with a raw timeout.
- **During a run:** if the status reports an error, the script prints the
  server's error message and exits. A timeout beyond `timeout_seconds` also
  aborts (see the timeout reference).
- **No output audio:** if the run completes but no audio entry is found, the
  script reports it (the `SaveAudioAdvanced` node may be missing on that server,
  or audio is stored under a different output key).

## 5. Common Server-Side Errors

| Symptom | Likely cause | Fix |
|---|---|---|
| Missing node `TextEncodeAceStepAudio1.5` | AceStep custom node not installed | `git clone` AceStep-ComfyUI |
| Missing `acestep_v1.5…` | Model file not on disk | drop the weight in (see MODEL_URL.txt) |
| `SaveAudioAdvanced` missing | VideoHelperSuite not installed | install the node |
| `ModelSamplingAuraFlow` missing | old ComfyUI | update ComfyUI (core node) |
