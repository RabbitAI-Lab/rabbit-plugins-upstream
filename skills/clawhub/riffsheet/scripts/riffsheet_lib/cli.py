"""riffsheet: measure a short video and lay out the pictures a reading agent needs.

Needs ffmpeg + ffprobe on PATH and the Python standard library. No network. Only the optional
`transcribe` command needs a package (faster-whisper) and a speech model on this machine; `check`
says whether they are here and what getting them costs.

  check  [VIDEO] [--json]                        facts: what this machine has for an analysis (no network)
  transcribe VIDEO --out T.json [--hint TEXT]    word-timed transcript (optional; needs faster-whisper)
  scan   VIDEO --out DIR [--transcript T.json]   everything up front (run first)
  text   DIR --box x0,y0,x1,y1 [--from S --to E] each distinct state of a region, once, with on/off times
  element DIR --box ROUGH --at T                 measured box and on/off times of a drawn element or pane
  zoom   DIR --at T [--at T ...] [--box ...]     sharp, large view of moments / a region
  frames DIR --from S --to E [--box ...] [--every K]   every real frame of a window, tiled
  mouth  DIR --box ... (--words A-B | --line N | --from S --to E)
                                                 the mouth at each word and pause (--every-frame: all)
  color  DIR --at T --box ...                    measured main colors of a box, with plain names
  hear-check DIR [--answer DIGITS | --cannot-hear]  whether this agent can hear: a test the tool sets and marks
  listen DIR [--from S --to E]                   after a passed hearing check: the sound, cut for listening
  build  DIR [--judgment J.json] [--out O]       no J: the measured sheet to judge against;
                                                 with J: riffsheet.json + riffsheet.md, plus checks

Boxes are fractions of the frame: x0,y0,x1,y1 with 0,0 = top-left. Overview cells carry a 10% grid.
Every label shows the true timestamp of the frame it sits under (from the decoder, not a resampler).
Runs on Python 3.9 or newer; needs ffmpeg 7.0 or newer (filter scripts are passed as -/filter_complex).

Exit status: 0 done; 1 an error (one line on stderr); 2 a usage error; 3 `build` refused (statements
without a confirming view, or of what the sound is without a passed hearing check: nothing written, the
list printed under UNCONFIRMED or NOT HEARD).
"""

import argparse
import sys

from . import FORMAT_VERSION, VERSION
from .build import cmd_build
from .capabilities import cmd_check
from .elements import cmd_element
from .hearing import cmd_hear_check, cmd_listen
from .scan import cmd_scan
from .scandir import remove_scratch
from .text import cmd_text
from .transcript import TRANSCRIBE_MODEL, cmd_transcribe
from .util import die, set_entry
from .views import cmd_color, cmd_zoom, dense


# ----------------------------------------------------------------------------- main
def main(argv=None, entry=None):
    if entry:
        set_entry(entry)
    ap = argparse.ArgumentParser(
        prog="riffsheet", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--version", action="version", version=f"riffsheet {VERSION} (analysis format_version {FORMAT_VERSION})"
    )
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check", help="what this machine can do for an analysis (no network)")
    p.add_argument("video", nargs="?", help="a video: also report its length and whether it has an audio track")
    p.add_argument("--json", action="store_true", help="the report as JSON")
    p.set_defaults(fn=cmd_check)
    p = sub.add_parser("transcribe", help="word-timed transcript (needs faster-whisper; optional)")
    p.add_argument("video")
    p.add_argument("--out", required=True, help="transcript JSON to write")
    p.add_argument("--model", default=TRANSCRIBE_MODEL, help=f"model size or folder (default {TRANSCRIBE_MODEL})")
    p.add_argument("--model-dir", help="model cache folder (default: the Hugging Face cache)")
    p.add_argument("--download", action="store_true", help="allow fetching the model over the network")
    p.add_argument("--language", help="language code; default: detected")
    p.add_argument("--hint", help="names and terms read on screen (brand, product, key terms), to bias spelling")
    p.add_argument("--compare", help="an earlier transcript JSON: print the words that differ")
    p.set_defaults(fn=cmd_transcribe)
    p = sub.add_parser("scan", help="measure + default pictures")
    p.add_argument("video")
    p.add_argument("--out", required=True)
    p.add_argument("--transcript", help="faster-whisper style JSON (segments[].words[] start/end/word)")
    p.add_argument(
        "--transcript-by",
        help="what made the transcript, when it was not `transcribe` (a recognizer and model, or the person)",
    )
    p.set_defaults(fn=cmd_scan)
    p = sub.add_parser("text", help="distinct states of a region with on/off times")
    p.add_argument("dir")
    p.add_argument("--box", required=True)
    p.add_argument("--from", dest="start", type=float)
    p.add_argument("--to", dest="end", type=float)
    p.add_argument("--name")
    p.set_defaults(fn=cmd_text)
    p = sub.add_parser("element", help="measured box and on/off times of a drawn element you point at")
    p.add_argument("dir")
    p.add_argument("--box", required=True, help="rough box around the element")
    p.add_argument("--at", type=float, required=True, help="a moment when it is on screen")
    p.add_argument("--name")
    p.set_defaults(fn=cmd_element)
    p = sub.add_parser("zoom", help="large sharp view of moments (optionally a region)")
    p.add_argument("dir")
    p.add_argument("--at", type=float, action="append")
    p.add_argument("--frame", type=int, action="append")
    p.add_argument("--box")
    p.add_argument("--max-upscale", type=float, default=2.0)
    p.add_argument("--name")
    p.set_defaults(fn=cmd_zoom)
    p = sub.add_parser("color", help="measured main colors of a small box at one moment, with plain names")
    p.add_argument("dir")
    p.add_argument("--at", type=float, required=True)
    p.add_argument("--box", required=True)
    p.add_argument(
        "--ref",
        help="box on something known to be white or neutral gray in the same frame: "
        "colors are also given as if that thing were neutral (corrects the light)",
    )
    p.set_defaults(fn=cmd_color)
    for nm, mouth in (("frames", False), ("mouth", True)):
        p = sub.add_parser(nm, help=("mouth crops aligned with words" if mouth else "every real frame of a window"))
        p.add_argument("dir")
        p.add_argument("--box", required=mouth)
        p.add_argument("--from", dest="start", type=float)
        p.add_argument("--to", dest="end", type=float)
        if mouth:
            p.add_argument("--line", type=int, help="the transcriber's line N (L N on the build sheet)")
            p.add_argument("--words", help="word index range A-B: one of your own lines, as in the judgment file")
        p.add_argument("--every", type=int, default=1, help="keep every Kth real frame")
        if mouth:
            p.add_argument(
                "--every-frame",
                action="store_true",
                help="every real frame of the line (default: one frame per word and per pause)",
            )
        p.add_argument("--size", type=int, help="cell long side in px")
        p.add_argument("--name")
        p.set_defaults(fn=(lambda a, m=mouth: dense(a, m)))
    p = sub.add_parser("hear-check", help="whether this agent can hear: a sound test the tool sets and marks")
    p.add_argument("dir")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--answer", help="the digits you heard in the newest check file, in order")
    g.add_argument("--cannot-hear", action="store_true", help="record that you cannot open a sound file as sound")
    p.set_defaults(fn=cmd_hear_check)
    p = sub.add_parser("listen", help="after a passed hearing check: the video's sound cut into files to open")
    p.add_argument("dir")
    p.add_argument("--from", dest="start", type=float)
    p.add_argument("--to", dest="end", type=float)
    p.set_defaults(fn=cmd_listen)
    p = sub.add_parser("build", help="write riffsheet.json + riffsheet.md from the scan and a judgment file")
    p.add_argument("dir")
    p.add_argument("--judgment", help="the agent's judgment JSON (omit to print the measured sheet)")
    p.add_argument("--out", help="output folder (default DIR/out)")
    p.set_defaults(fn=cmd_build)
    a = ap.parse_args(argv)
    try:
        a.fn(a)
    except KeyboardInterrupt:
        sys.stderr.write("riffsheet: interrupted\n")
        raise SystemExit(130) from None
    except OSError as e:  # a folder that cannot be made or written, a disk that is full
        die(f"{e.strerror or e}: {e.filename}" if getattr(e, "filename", None) else str(e))
    finally:
        remove_scratch()
