# Godot 4.7.2 API forms that work (verified at runtime)

Exact names/shapes confirmed against a running 4.7.2 build. The "obvious" 3.x-era
form appears only as the thing that FAILS — use the stated form.

## Environment (glow = bloom) + fog
- `glow_enabled`, `glow_intensity`, `glow_bloom`, `glow_hdr_threshold` (~0.9); blend `Environment.GLOW_BLEND_MODE_ADDITIVE`; tonemap `Environment.TONE_MAPPER_ACES`; overall brightness via `tonemap_exposure`.
- Fog: `fog_enabled`, `fog_density`, `fog_light_color`.
- HDR emission on a `StandardMaterial3D`: `emission_enabled=true`, `emission` (Color), `emission_energy_multiplier > 1.0` (2.5–4.0 for strong bloom). There is **no** `SHADING_MODE_GLOW` / `TRANSPARENCY_ADD` in 4.7 — do not reach for them.

## GPUParticles3D
- `draw_pass_1` / `draw_pass_2` take a **Mesh**, not a Material: build a `SphereMesh`, set its `.material`, then assign the mesh to `draw_pass_1`. (Assigning a bare `Material` is a type error.)
- `emission_shape` + `emission_shape_scale`; `process_material` is a `ParticleProcessMaterial`.

## Physics / RigidBody3D
- Damping is `linear_damp` and `angular_damp` (NOT `_damping`); `gravity_scale`; velocity is `linear_velocity` (NOT `velocity`).
- World raycast: `direct_space_state` is a **property** on `World3D` (not a method) → `get_world_3d().direct_space_state.intersect_ray(PhysicsRayQueryParameters3D.create(from, to))`. `intersect_ray` takes the single `PhysicsRayQueryParameters3D`, not two `Vector3`s.
- `RayCast3D` node: `target_position`, `enabled`, `collision_mask`; `is_colliding()`, `get_collider()`, `force_raycast_update()`.

## RandomNumberGenerator
- Has `randf()`, `randf_range()`, `randi_range()`, `seed`. **No `.pick()`** — pick manually: `arr[rng.randi_range(0, arr.size()-1)]`.

## Audio
- Use `AudioStreamPlayer3D` (NOT `SoundPlayer3D`). Build `AudioStreamWAV` in code for procedural chimes.

## XR
### Session state (OpenXR interface from `XRServer.find_interface("OpenXR")`)
- `get_session_state()` (enum), `is_initialized()`, signals `session_begun` / `session_stopping`. **No `is_session_started()`.** Drive a `_xr_active` bool from the two signals.

### OpenXRInterface diagnostic surface (4.7.2 — dump before coding)
- **No** `controller_connected` / `controller_disconnected` signals, and **no**
  `get_active_interaction_profile()` method — do not connect the former or call the
  latter (both runtime-error in 4.7.2). Real signals include `session_begun`,
  `session_stopping`, `session_focussed`, `session_visible`, `play_area_changed`,
  `pose_recentered`, `user_presence_changed`.
- Hand-tracking queries (no-arg): `is_hand_tracking_supported()`,
  `is_hand_interaction_supported()`, `get_view_count()`; plus `get_hand_joint_*()`
  (position/rotation/radius/flags/linear+angular velocity). `get_hand_tracking_source()`
  takes **1 argument** (hand side) — calling it with no args errors.
- **Dumping the interface:** iterate `get_signal_list()` / `get_method_list()` and read
  each entry's `"name"` — in 4.7.2 that value is a **`String`**, so convert with
  `str(x)`, NOT `x.string()` (`.string()` on a String errors: "Nonexistent function
  'string' in base 'String'").

### XRController3D
- Props: `tracker` (String — leave `""`/empty to auto-track a standard controller), `pose` (String: use `"grip"` or `"aim"`), `show_when_tracked` (bool).
- ⚠️ `tracker="left_hand"`/`"right_hand"` = **hand-tracking mode** → no pose/input for controllers (invisible hands). `pose="default"` is **unreliably bound** → controllers silently stop tracking. Use `tracker=""` + `pose="grip"`.
- Methods: `is_button_pressed()`, `get_input()`, `get_float()`, `get_vector2()`, `get_tracker_hand()` (returns unknown/0 when the node isn't linked to a tracked controller).
- **No** `tracking` prop, **no** `TrackingType` enum, **no** `get_supported_controls()`.

### Scene structure
```
Main (root, main.gd)
└─ XROrigin3D            # XR root
   ├─ XRCamera3D         # extends Camera3D
   ├─ XRController3D "LeftHand"   (tracker="", pose="grip", show_when_tracked=true)
   └─ XRController3D "RightHand"  (tracker="", pose="grip", show_when_tracked=true)
```

## Error → fix table (fired during the real build)
| Symptom | Cause | Fix |
|---|---|---|
| parse error assigning to `draw_pass_1` | assigned a `Material` | assign a `Mesh` with `.material` set |
| `is_session_started()` not found | wrong method | `get_session_state()` enum + `session_begun`/`session_stopping` signals |
| `.pick()` not found | no such method | `arr[rng.randi_range(0, arr.size()-1)]` |
| `direct_space_state()` / 2-Vector3 `intersect_ray` | wrong shape | property + `PhysicsRayQueryParameters3D.create(a,b)` |
| `get_supported_controls()` not found | no such method | drop it; log `tracker` instead |
| connecting `controller_connected` / calling `get_active_interaction_profile()` | don't exist in 4.7.2 `OpenXRInterface` | use `is_hand_tracking_supported()` / `get_view_count()` / `XRServer.get_tracker()` instead |
| `.string()` on a `String` ("Nonexistent function 'string'") | list entries' `name` is a String in 4.7.2 | `str(x)` |
| `EMISSION_SHAPE_*` / `_damping` / `velocity` names | 3.x-era names | 4.7 names above |

## Verification commands (adjust the project path)
```bash
cd <dir-containing-godot-binary>
GODOT=./Godot_v4.7.2-stable_win64_console.exe   # use your platform's binary
# import
$GODOT --headless --import --path "<project>" > imp.log 2>&1
# run (OpenXR OFF for verification) — expect a startup self-test print
$GODOT --headless --path "<project>" > run.log 2>&1
# screenshot (NON-headless, marker arg the scene looks for) → saves PNG, quits
$GODOT --path "<project>" --preview > prev.log 2>&1
# check (timeout force-kill on Windows emits exit-time RID noise — filter for real errors)
grep -c "SCRIPT ERROR" run.log
grep -iE "SCRIPT ERROR|Parse Error|Failed to load" run.log | sort | uniq -c
```
