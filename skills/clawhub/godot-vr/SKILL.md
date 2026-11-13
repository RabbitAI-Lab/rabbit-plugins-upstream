---
name: godot-vr
description: "Build & headless-verify Godot 4.7 OpenXR/VR apps — room-scale workflow, Pimax Crystal tested in-visor, controller-binding pitfalls covered."
version: 1.0.0
author: Maxwell McClure
license: MIT
metadata:
  hermes:
    tags: [godot, godot-4, openxr, vr, pimax, room-scale, headless]
    related_skills: [blender-headless]
---

Build a Godot 4 (OpenXR) VR app and verify it headlessly (no editor/GPU loop, no headset during the build). Deliver a real, running project
verified by execution — not a description. (Sibling of `blender-headless`; different
engine, same headless-verify discipline.)

## When to Use
- The user wants a Godot 4 VR/AR or OpenXR app (headset target like Pimax Crystal — works on **either** Pimax runtime once the action-map/tracker binding is right; see the reference).
- You must headless-verify a Godot 4 scene without the editor: import → headless run → non-headless screenshot.
- You hit Godot 4.7 parse/runtime errors on render / particles / physics / XR APIs — the reference holds the working forms.

## Environment (example — adapt the paths)
- Use the Godot 4.7.2-stable win64 **standard** build (standard, not .NET — it has OpenXR compiled in) from the godotengine releases page. Put the binary wherever you like (example: `M:/Godot/.tools/godot/Godot_v4.7.2-stable_win64_console.exe`); confirm with `--version` before use.
- Headless build/verify needs no headset runtime installed. Targeting a Pimax Crystal? Controllers emulate Oculus Touch and work in Godot on **both** Pimax OpenXR 0.1.0 (Pimax Play built-in) and PimaxXR (Unofficial) 0.4.4 once the action map + tracker binding are correct (see `references/xr-controller-troubleshooting.md`); SteamVR unverified.
- Put the project on a drive with room to spare (example: `M:/Godot/<project>`).
- Windows under a bash with MSYS path conversion disabled: invoke the binary with **drive-letter** paths (`M:/...`), not MSYS `/m/...` (bash builtins like `cd /m/...` are fine).

## Workflow (in order)
1. **Scaffold** `project.godot`: `config/features=PackedStringArray("4.7","Forward Plus")` (do **NOT** include `"OpenXR"` — it triggers a false-positive editor warning; runtime OpenXR is driven by `[xr] openxr/enabled=true`, not the feature tag), `[rendering] renderer/rendering_method="forward_plus"`, an `[xr]` block with `openxr/enabled=true`, `openxr/always_in_xr=true`, `shaders/enabled=true`, and a 1600x900 viewport.
2. **Build the scene procedurally in code** — primitives only, no external assets (that is the default here). One `main.gd` on the root node builds: Environment (glow/bloom + fog), a directional "moon" light, `OmniLight3D` point lights for the glow, and the geometry (trees, props, a focal glowing centerpiece).
3. **XR root**: `XROrigin3D` → children `XRCamera3D` + two `XRController3D`, each `tracker="left_hand"` / `"right_hand"` (the tracker names `OpenXRInterface::find_tracker()` registers with `XRServer`), `pose="grip"` (or `"aim"`), `show_when_tracked=true`. ⚠️ `XRController3D` has **NO auto-detect**: an empty `tracker` → `get_tracker("")` → null → the node never binds (frozen pose, `hand=0`, invisible hands). Set `tracker` explicitly to `"left_hand"`/`"right_hand"`. Never `pose="default"` (unreliably bound → controllers silently stop tracking). See `references/xr-controller-troubleshooting.md`.
4. **Grab without a plugin**: native `XRController3D` + a world-space ray (`get_world_3d().direct_space_state.intersect_ray(PhysicsRayQueryParameters3D.create(from,to))`). The GodotVR XR-Interaction plugin is unavailable (its repos moved) — do not block on it.
5. **Fallback camera + self-screenshot** so the scene is checkable without a headset: in `_ready`, if no XR session, add a `Camera3D` pointed at the scene; if the run was given a marker arg (e.g. `--preview`), wait ~12 frames then `get_viewport().get_texture().get_image().save_png(path)` and `get_tree().quit()`.
6. **Headless-verify (OpenXR OFF — see gate below)** until 0 script errors; confirm the startup self-test print shows the `XROrigin3D` with its `XRCamera3D` + both controllers.
7. **GPU screenshot**: run NON-headless with the marker arg → PNG, then vision-check it (real geometry/lighting, not a blank/black frame).
8. **Re-enable OpenXR** for delivery (`openxr/enabled=true`; leave `"OpenXR"` out of `config/features`). The in-visor feel is the user's final check.

## Pitfalls
- **OpenXR + `--headless` stalls in the main loop, AFTER `_ready`** — scene load and every `_ready` run and print normally, then the engine enters the main loop, detects the HMD, and hangs to timeout (no display/form factor). So a short-timeout headless run IS a valid no-headset check that a code edit landed: `timeout 20 <bin> --headless --path <proj> 2>&1 | grep -iE "Parse Error|SCRIPT ERROR|not found in base|ready"` surfaces scene-load parse errors and your `_ready` prints (e.g. `[LeftHand] ready (tracker=… pose=…)`) before the stall — use it to confirm a change took effect (and it is the only reliable way to catch native-method parse errors, since `--import` does not parse scene scripts against the native API). Use a full run with **OpenXR OFF** for real 0-error / self-test verification, then re-enable OpenXR for delivery. Do not chase a ticking "headless VR" main loop — it won't run past session start without a display.
- **`--headless` never renders.** Any visual check must run NON-headless (marker arg) so a window opens and GPU draws; the scene saves its own PNG.
- **Godot 4.7 renamed/changed several 3.x-era APIs** — the "obvious" form throws parse/runtime errors. Check `references/godot-47-api.md` before writing render/particles/physics/XR code; it lists the working forms and the errors they prevent.
- **`write_file` refuses overwrite even after a full read.** `rm -f` the target first, then write to the fresh path (same workaround works for re-writing scene `.tscn`/`.gd`).
- **Don't trust import alone.** Run the project headless after import — most errors here were *runtime* (wrong API shape), which `--import` does not surface.
- **Headless-verify passing ≠ controllers work.** A clean headless run + screenshot proves the scene runs and renders; it can't see the visor, so it says nothing about whether controllers track in it. When the user reports "no hands / can't interact," go straight to `references/xr-controller-troubleshooting.md` — do not re-tune the scene or chase a headless VR run.
- **"No hands" on Pimax Crystal is the binding layer (case A), NOT the runtime.** Verified in-visor: with the case A fixes in place, the same project works on **both** Pimax OpenXR 0.1.0 (Pimax Play built-in) and PimaxXR (Unofficial) 0.4.4. The case A fixes: (1) `XRController3D.tracker` must be set explicitly to `"left_hand"`/`"right_hand"` (no auto-detect — empty never binds), and (2) the OpenXR action map must be trimmed to only the profiles the runtime recognizes — for Crystal keep **only** `oculus/touch_controller`, drop the other three stock profiles (generic, pico4, hand) and every `grip_surface/pose` (OpenXR 1.1 palm-pose) binding. One unsupported path fails the whole `xrSuggestInteractionProfileBindings` call (`XR_ERROR_PATH_UNSUPPORTED`) → no controller binds, on **any** runtime. No `openxr/default_action_map` pin needed — the engine default is already `res://openxr_action_map.tres` (probe-verified); just keep the edited file at that path. (Early "no hands" on PiOpenXR/SteamVR predated the binding fix; the runtime switch that once seemed to fix it was coincidental. SteamVR was never re-tested after the fix — unverified.)
- **"feature `OpenXR` not supported by this version" is a 4.7.2 editor false-positive** when `"OpenXR"` is in `config/features` (the build has OpenXR; it initializes at runtime). Dismissable ("Open anyway"), but you can avoid it by leaving `"OpenXR"` out of `config/features` — runtime OpenXR is driven by `[xr] openxr/enabled=true`, not the feature tag. Confirm OpenXR actually loaded via the `Running on OpenXR runtime: …` Output line, not the feature list.

## References
- `references/godot-47-api.md` — confirmed 4.7.2 API forms (Environment glow, GPUParticles3D, RigidBody3D, raycast, XR session state, XRController3D) + the `XROrigin3D` scene structure + the error→fix table that actually fired during the build + the exact verification commands.
- `references/xr-controller-troubleshooting.md` — controllers don't show / no interaction in the visor: the decisive diagnostic (which of 3 failure cases), the case A two-sub-fix detail (explicit `tracker` + trimmed action map — the real Pimax Crystal fix, works on both Pimax runtimes), OpenXR runtime selection on Windows (registry / env override / restart / verify line), and the benign warnings to ignore.
