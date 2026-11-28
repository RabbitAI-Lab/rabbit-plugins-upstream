"""Tuned thresholds and limits shared across the measuring modules."""

import os

# exit status: 0 done, 1 an error (one line on stderr), 2 a usage error (argparse), and this when
# `build` refuses: statements without a confirming view, nothing written (a caller can tell it apart)
EXIT_REFUSED = 3
LONG_VIDEO_S = 180  # the tool is made for short clips; past this, scan warns what will be slow or large
FFMPEG_MIN_MAJOR = 7
REGION_SETTLE_MIN = 0.10  # a suggested region whose changes settle less than this is probably motion
# --- image budget (vision model cap: long side 1568 px, about 1.15 megapixels) ---
MAX_SIDE = 1568
MAX_PIXELS = 1_150_000
PAD = 4  # gap between tiles
# --- change measurement ---
GRID_N = 12  # cells across the short side of the frame (cells are square-ish)
CELL_FLOOR = 0.02  # a cell's mean abs luma change below this is compression noise
CELL_JUMP_X = 3.0  # a cell "changed" at a frame when its change is >= 3x its own usual change
BASELINE_S = 0.5  # "usual change" = median over +-0.5 s around the frame
# one-frame-spike rule for hard cuts: whole-frame change measured on 32x32 gray at the source frame rate
SPIKE_FLOOR = 0.004
SPIKE_NEIGHBOR_X = 4.0
SPIKE_LOCAL_X = 6.0
SPIKE_WINDOW_S = 1.0
STEP_X = 2.0  # one-frame step: >= 2x the change into the frames either side
SCDET_THRESHOLD = 8  # ffmpeg scdet threshold: a second, independent cut detector beside the spike rule
STILL_CELL = 0.003  # a cell whose median change over a shot is below this is pixel-still
STILL_LOCKED = 0.30  # >= this share of still cells: camera locked (or picture frozen)
STILL_MOVING = 0.05  # <= this share: the whole picture moves every frame

FONT_CANDIDATES = [
    os.environ.get("RIFFSHEET_FONT", ""),
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]
HOLD_T = 12  # a pixel "holds" from one frame to the next when its gray level moves <= this
EXACT_T = 4  # a drawn layer holds to within compression noise; filmed things rarely do


# ----------------------------------------------------------------------------- build (final outputs)
VIDEO_FORMATS = (
    "single_shot",
    "split_screen_left_right",
    "split_screen_top_bottom",
    "picture_in_picture",
    "multi_grid_2x2",
    "multi_grid_other",
)
# Pace bands: natural speech is about 2.5-3 words/s in English (3.5-4 characters/s in Chinese), and
# 4.0 words/s (5.5 characters/s) over a line's window is where speech is clearly rushed. The rate here
# runs from the first word's start to the last word's end, without a window's slack before and after,
# so it reads about half a unit higher than a window rate: measured = the natural band, rapid-fire =
# past the rushed ceiling.
PACE_BANDS = {"words": (2.5, 3.5, 4.5), "characters": (3.5, 4.5, 6.0)}
PACE_WORDS = ("unhurried", "measured", "brisk", "rapid-fire")
LINE_PAUSE_S = 0.15  # a gap between words this long or longer is a pause (a line may end there)
SENTENCE_ENDS = (".", "?", "!", "…", "。", "？", "！")
FORMULA_KEYS = (
    "funnel_stage",
    "function",
    "mechanism",
    "viewer_state_before",
    "viewer_state_after",
    "meaning_contract",
    "constraint",
    "sensory_channel",
    "retention_anchor",
    "linguistic_craft",
)
DESCENDERS = set("gjpqy,;")
