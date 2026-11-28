"""The riffsheet.json format as a JSON Schema, and the checker for it."""

import re

from . import FORMAT_VERSION
from .constants import FORMULA_KEYS, PACE_WORDS, VIDEO_FORMATS

# ----------------------------------------------------------------------------- riffsheet.json format
# The format `build` writes, as a JSON Schema (draft 2020-12). It lives here, in the tool, so that the tool
# on its own still checks its own output; schema/riffsheet.schema.json is this dict written out
# (the test suite checks the two agree). Values the agent supplies verbatim (attributes, formula, notes)
# are left open; values the tool computes are typed exactly. Fields whose wrong value `build` reports as
# an open check (an unknown `mode` or `video_format`) are typed as strings, not enums, so that the
# analysis is still written with the problem listed under `_local.checks`.
_NUM = {"type": "number"}
_PAIR = {"type": "array", "items": _NUM, "minItems": 2, "maxItems": 2}
_BOX = {"type": "array", "items": _NUM, "minItems": 4, "maxItems": 4}
_HEX = {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"}
_STRS = {"type": "array", "items": {"type": "string"}}
_SRC = {
    "type": "object",
    "description": "where a field's value came from; untagged fields were seen by the agent",
    "additionalProperties": {"enum": ["measured", "seen", "heard", "inferred", "cannot_judge_locally", "default"]},
}
_NOTES = {"type": "array", "description": "free notes: corrections, uncertainties, why a value is missing"}
_SOUND = {
    "type": "object",
    "required": ["type", "t", "dt", "db"],
    "additionalProperties": False,
    "properties": {
        "type": {"enum": ["peak", "cliff_rise", "cliff_drop"]},
        "t": {"type": "number", "description": "the event's onset, refined to 10 ms"},
        "dt": {"type": "number", "description": "onset minus the change's first frame, in seconds"},
        "db": _NUM,
    },
}
_SOUND_AT = {
    "type": "object",
    "required": ["summary", "by_chance", "changes"],
    "additionalProperties": False,
    "properties": {
        "summary": {"type": "string"},
        "by_chance": {"type": "number", "description": "how many of these would land on a peak or rise at random"},
        "changes": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "kind", "span", "on", "nearest"],
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "string"},
                    "kind": {"enum": ["cut", "caption"]},
                    "span": _PAIR,
                    "on": {"type": "array", "items": _SOUND},
                    "nearest": {"anyOf": [_SOUND, {"type": "null"}]},
                },
            },
        },
    },
}
ANALYSIS_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "riffsheet.schema.json",
    "title": "riffsheet analysis",
    "description": "riffsheet.json as written by `riffsheet build`. Keys starting with _ carry provenance and "
    "measurements beside the analysis itself.",
    "type": "object",
    "required": [
        "format_version",
        "prose",
        "audio",
        "scene_entities",
        "slots",
        "metadata",
        "_prose_segments",
        "_local",
    ],
    "additionalProperties": False,
    "properties": {
        "format_version": {"const": FORMAT_VERSION},
        "prose": {"type": "string", "description": "the prose segments joined by blank lines"},
        "audio": {
            "type": "object",
            "required": ["voice_segments"],
            "additionalProperties": False,
            "properties": {
                "voice_segments": {"type": "array", "items": {"$ref": "#/$defs/voice_segment"}},
                "heard": {
                    "type": "array",
                    "description": "what the sound is, as heard by the agent after it passed the hearing check "
                    "(_local.hearing); absent in files written before riffsheet 0.2.0",
                    "items": {"$ref": "#/$defs/heard"},
                },
            },
        },
        "scene_entities": {"type": "array", "items": {"$ref": "#/$defs/entity"}},
        "slots": {"type": "array", "items": {"$ref": "#/$defs/slot"}},
        "metadata": {"$ref": "#/$defs/metadata"},
        "_prose_segments": {"type": "array", "items": {"$ref": "#/$defs/prose_segment"}},
        "_local": {"$ref": "#/$defs/local"},
    },
    "$defs": {
        "voice_segment": {
            "type": "object",
            "additionalProperties": False,
            "required": ["id", "time_range", "text", "mode", "speaker", "_src", "_pace"],
            "properties": {
                "id": {"type": "string", "pattern": "^vs[0-9]+$"},
                "time_range": _PAIR,
                "text": {"type": "string"},
                "mode": {"type": "string", "description": "on_camera_dialogue, voiceover or no_dialogue"},
                "speaker": {"type": ["string", "null"]},
                "_src": _SRC,
                "_pace": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["unit", "count", "per_s", "band", "longest_gap_s", "pauses_over_0_4s", "trend"],
                    "properties": {
                        "unit": {"enum": ["words", "characters"]},
                        "count": {"type": "integer"},
                        "per_s": _NUM,
                        "band": {"enum": list(PACE_WORDS)},
                        "longest_gap_s": _NUM,
                        "pauses_over_0_4s": {"type": "array", "items": _PAIR},
                        "trend": {"enum": ["speeds up", "slows down", "even", None]},
                    },
                },
                "_notes": _NOTES,
            },
        },
        "heard": {
            "type": "object",
            "required": ["id", "time_range", "about", "text", "clip", "_src"],
            "additionalProperties": False,
            "properties": {
                "id": {"type": "string", "pattern": "^h[0-9]+$"},
                "time_range": _PAIR,
                "about": {"enum": ["music", "voice", "effect", "ambience", "other"]},
                "text": {"type": "string"},
                "clip": {"type": "string", "description": "the sound file `listen` cut, that the agent heard it in"},
                "_src": _SRC,
            },
        },
        "entity": {
            "type": "object",
            "required": ["id", "kind", "semantic", "time_range", "attributes", "params"],
            "properties": {
                "id": {"type": "string"},
                "kind": {"enum": ["person", "subtitle", "graphic", "source_image"]},
                "semantic": {"type": "string"},
                "time_range": _PAIR,
                "attributes": {"type": "object"},
                "params": {"type": "object"},
                "_src": _SRC,
                "_notes": _NOTES,
                "_measured_style": {"$ref": "#/$defs/measured_style"},
            },
            "additionalProperties": False,
            "allOf": [
                {
                    "if": {"properties": {"kind": {"const": "person"}}},
                    "then": {"properties": {"params": {"type": "object", "additionalProperties": False}}},
                },
                {
                    "if": {"properties": {"kind": {"const": "subtitle"}}},
                    "then": {
                        "required": ["_measured_style", "_src"],
                        "properties": {"params": {"$ref": "#/$defs/subtitle_params"}},
                    },
                },
                {
                    "if": {"properties": {"kind": {"const": "graphic"}}},
                    "then": {"properties": {"params": {"$ref": "#/$defs/graphic_params"}}},
                },
                {
                    "if": {"properties": {"kind": {"const": "source_image"}}},
                    "then": {
                        "properties": {
                            "params": {
                                "type": "object",
                                "required": ["description"],
                                "additionalProperties": False,
                                "properties": {"description": {"type": "string"}},
                            }
                        }
                    },
                },
            ],
        },
        "subtitle_params": {
            "type": "object",
            "required": ["text"],
            "additionalProperties": False,
            "properties": {
                "text": {"type": "string"},
                "position_y_ratio": _NUM,
                "position_x_ratio": _NUM,
                "approximate_size": {
                    "type": "string",
                    "description": "measured: very_small, small, medium, large or very_large",
                },
                "color": {"type": "string"},
                "outline_color": {"type": "string"},
                "box_color": {"type": "string"},
                "cue_max_words": {"type": "integer"},
                "voice_anchor": {"type": "string"},
                "visual_anchor": {"type": "string"},
                "highlight_words": {},
                "highlight_color": {"type": "string"},
            },
        },
        "graphic_params": {
            "type": "object",
            "required": ["description", "split"],
            "additionalProperties": False,
            "properties": {
                "description": {"type": "string"},
                "inline_text": {},
                "x_ratio": _NUM,
                "y_ratio": _NUM,
                "width_ratio": _NUM,
                "height_ratio": _NUM,
                "split": {"type": "boolean"},
            },
        },
        "measured_style": {
            "type": "object",
            "required": ["states_measured", "states"],
            "additionalProperties": False,
            "description": "the caption's layer measurement, voted over its text states (weighted by frames)",
            "properties": {
                "states_measured": {"type": "integer"},
                "states": {"type": "integer"},
                "why": _STRS,
                "fill": _HEX,
                "fill_agree": _NUM,
                "outline_color": _HEX,
                "outline_color_agree": _NUM,
                "shadow_color": _HEX,
                "shadow_color_agree": _NUM,
                "box_color": _HEX,
                "box_color_agree": _NUM,
                "frames_measured_share": _NUM,
                "size_why": _STRS,
                "center": _PAIR,
                "box": _BOX,
                "row_px_1080w": {"type": ["number", "null"]},
                "rows": {"type": "integer"},
            },
        },
        "slot": {
            "type": "object",
            "required": ["id", "time_range", "formula", "_src"],
            "additionalProperties": False,
            "properties": {
                "id": {"type": "string", "pattern": "^s[0-9]+$"},
                "time_range": _PAIR,
                "formula": {"type": "object", "description": "the agent's formula: " + ", ".join(FORMULA_KEYS)},
                "_src": _SRC,
            },
        },
        "metadata": {
            "type": "object",
            "additionalProperties": False,
            "required": ["duration_seconds", "video_format", "language", "speaking_mode", "_src"],
            "properties": {
                "duration_seconds": _NUM,
                "video_format": {"type": "string", "description": "one of " + ", ".join(VIDEO_FORMATS)},
                "language": {"type": ["string", "null"]},
                "speaking_mode": {
                    "enum": ["none", "on_camera", "voiceover", "mixed"],
                    "description": "from the spoken lines; none with _src.speaking_mode cannot_judge_locally means "
                    "the speech was not transcribed (_local.stages says why): the analysis has no spoken lines, "
                    "and whether anyone speaks is not known",
                },
                "_src": _SRC,
            },
        },
        "prose_segment": {
            "type": "object",
            "required": ["window", "text"],
            "additionalProperties": False,
            "properties": {
                "window": _PAIR,
                "text": {"type": "string"},
                "claims": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "inferred": {},
                        "uncertain": {"type": "array"},
                        "cannot_judge_locally": {},
                        "measured": _STRS,
                    },
                },
            },
        },
        "local": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "method",
                "scan",
                "tags",
                "cuts",
                "non_cut_changes",
                "camera_still_share",
                "dropped_as_music",
                "cannot_judge_locally",
                "tool_gaps",
                "followups",
                "images_viewed",
                "checks",
                "confirmations",
            ],
            "properties": {
                "method": {"type": "string"},
                "scan": {"type": "string", "description": "the scan folder, relative to the output folder"},
                "stages": {
                    "type": "object",
                    "description": "tool-written: each optional stage (speech_recognition) and whether it ran "
                    "(by: what made it; tested: whether that was the tool's tested path, `transcribe` with the "
                    "small model, null when nothing says), failed (it was there and stopped while running; why) or "
                    "did not run (why); "
                    "absent in files written before riffsheet 0.2.0",
                    "additionalProperties": {
                        "anyOf": [
                            {
                                "type": "object",
                                "required": ["state", "by"],
                                "additionalProperties": False,
                                "properties": {
                                    "state": {"const": "ran"},
                                    "by": {"type": "string"},
                                    "tested": {"type": ["boolean", "null"]},
                                },
                            },
                            {
                                "type": "object",
                                "required": ["state", "why"],
                                "additionalProperties": False,
                                "properties": {
                                    "state": {"enum": ["failed", "not_run"]},
                                    "why": {"type": "string"},
                                },
                            },
                        ]
                    },
                },
                "hearing": {
                    "type": "object",
                    "description": "tool-written: the hearing check for this analysis. passed: the agent heard the "
                    "test and its `heard` statements went out; failed, cannot_hear (the agent said it cannot open "
                    "sound) or not_taken: what the sound is was not judged; no_audio_track: nothing to hear. "
                    "Absent in files written before riffsheet 0.2.0",
                    "required": ["state"],
                    "additionalProperties": False,
                    "properties": {
                        "state": {"enum": ["passed", "failed", "cannot_hear", "not_taken", "no_audio_track"]},
                        "checks_answered": {"type": "integer"},
                        "checks_passed": {"type": "integer"},
                    },
                },
                "tags": {"type": "string"},
                "cuts": {"type": "array", "items": _NUM},
                "non_cut_changes": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["id", "t", "kind", "box"],
                        "additionalProperties": False,
                        "properties": {
                            "id": {"type": "string"},
                            "t": _NUM,
                            "kind": {"enum": ["panel", "band", "local"]},
                            "box": {"anyOf": [_BOX, {"type": "null"}]},
                        },
                    },
                },
                "camera_still_share": {"type": "object", "additionalProperties": {"type": ["number", "null"]}},
                "sound_at_picture": {
                    "description": "tool-measured: which cuts and caption appearances a loudness peak, rise or drop "
                    "falls on, within tolerance_s (one frame interval plus 10 ms), and how many would by chance; "
                    "times only, not what the sound is; null without an audio track (absent in files written "
                    "before it)",
                    "anyOf": [
                        {"type": "null"},
                        {
                            "type": "object",
                            "required": ["tolerance_s", "peaks_and_rises", "cuts", "captions"],
                            "additionalProperties": False,
                            "properties": {
                                "tolerance_s": _NUM,
                                "peaks_and_rises": {"type": "integer"},
                                "cuts": _SOUND_AT,
                                "captions": _SOUND_AT,
                            },
                        },
                    ],
                },
                "dropped_as_music": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["words", "text", "why"],
                        "additionalProperties": False,
                        "properties": {"words": {}, "text": {"type": "string"}, "why": {}},
                    },
                },
                "cannot_judge_locally": {},
                "tool_gaps": {"description": "the agent's record of what the tool lacked for this analysis"},
                "own_means": {
                    "type": "array",
                    "description": "facts the agent established by means the tool does not provide, each with "
                    "what it used (absent in files written before riffsheet 0.2.0)",
                    "items": {
                        "type": "object",
                        "required": ["fact", "used"],
                        "additionalProperties": False,
                        "properties": {"fact": {"type": "string"}, "used": {"type": "string"}, "time_range": _PAIR},
                    },
                },
                "followups": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {k: {} for k in ("cmd", "json", "window", "box", "frames")},
                    },
                },
                "images_viewed": {},
                "checks": {"anyOf": [{"const": "all passed"}, _STRS]},
                "confirmations": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["where", "words", "view", "t", "box"],
                        "additionalProperties": False,
                        "properties": {
                            "where": {"type": "string"},
                            "words": {"type": "string"},
                            "view": {"type": "string"},
                            "t": _NUM,
                            "box": {"anyOf": [_BOX, {"type": "null"}]},
                        },
                    },
                },
            },
        },
    },
}
SCHEMA_KEYWORDS = {
    "$schema",
    "$id",
    "$defs",
    "$ref",
    "title",
    "description",
    "type",
    "enum",
    "const",
    "properties",
    "required",
    "additionalProperties",
    "items",
    "minItems",
    "maxItems",
    "pattern",
    "anyOf",
    "allOf",
    "if",
    "then",
}


def _type_ok(v, t):
    if t == "null":
        return v is None
    if t == "boolean":
        return isinstance(v, bool)
    if t == "integer":
        return isinstance(v, int) and not isinstance(v, bool)
    if t == "number":
        return isinstance(v, (int, float)) and not isinstance(v, bool)
    return isinstance(v, {"string": str, "array": list, "object": dict}[t])


def validate(v, sch, root=None, path="$"):
    """Check a value against a schema that uses only SCHEMA_KEYWORDS. Returns a list of problems
    ("path: what is wrong"), empty when the value fits. Standard library only, so a plain Python
    install can check what it writes."""
    root = root or sch
    if "$ref" in sch:
        node = root
        for part in sch["$ref"].lstrip("#/").split("/"):
            node = node[part]
        return validate(v, node, root, path)
    errs = []
    if "type" in sch:
        ts = sch["type"] if isinstance(sch["type"], list) else [sch["type"]]
        if not any(_type_ok(v, t) for t in ts):
            return [f"{path}: expected {' or '.join(ts)}, found {type(v).__name__}"]
    if "const" in sch and v != sch["const"]:
        errs.append(f"{path}: must be {sch['const']!r}")
    if "enum" in sch and v not in sch["enum"]:
        errs.append(f"{path}: {v!r} is not one of {sch['enum']}")
    if "pattern" in sch and isinstance(v, str) and not re.search(sch["pattern"], v):
        errs.append(f"{path}: {v!r} does not match {sch['pattern']}")
    if isinstance(v, list):
        if len(v) < sch.get("minItems", 0) or len(v) > sch.get("maxItems", len(v)):
            errs.append(f"{path}: {len(v)} items")
        if "items" in sch:
            for k, x in enumerate(v):
                errs += validate(x, sch["items"], root, f"{path}[{k}]")
    if isinstance(v, dict):
        props = sch.get("properties", {})
        for k in sch.get("required", []):
            if k not in v:
                errs.append(f"{path}: missing {k}")
        extra = sch.get("additionalProperties", True)
        for k, x in v.items():
            if k in props:
                errs += validate(x, props[k], root, f"{path}.{k}")
            elif extra is False:
                errs.append(f"{path}: unexpected key {k}")
            elif isinstance(extra, dict):
                errs += validate(x, extra, root, f"{path}.{k}")
    if "anyOf" in sch and not any(not validate(v, s, root, path) for s in sch["anyOf"]):
        errs.append(f"{path}: fits none of the allowed forms")
    for s in sch.get("allOf", []):
        errs += validate(v, s, root, path)
    if "if" in sch and not validate(v, sch["if"], root, path):
        errs += validate(v, sch.get("then", {}), root, path)
    return errs
