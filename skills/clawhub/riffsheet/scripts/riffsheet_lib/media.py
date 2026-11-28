"""Running ffmpeg and ffprobe: probing, frame selection, decoding crops to raw pixels."""

import json
import os
import re
import shutil
import subprocess

from .constants import FFMPEG_MIN_MAJOR
from .util import _box_px, die, write_text

# Every external program is started with an argument list, never through a shell, so paths with
# spaces, quotes or non-ASCII characters reach ffmpeg unchanged.
RUN_TIMEOUT = 600  # seconds per ffmpeg call; raised for long videos once their duration is known
_checked = set()


def set_timeout(seconds):
    """The per-call limit, raised once a video's duration is known (run_timeout_for)."""
    global RUN_TIMEOUT
    RUN_TIMEOUT = seconds


def _check_exe(exe):
    """ffmpeg/ffprobe present and new enough, checked once per run."""
    if exe in _checked:
        return
    if not shutil.which(exe):
        die(f"{exe} not found on PATH (install ffmpeg {FFMPEG_MIN_MAJOR}.0 or newer, which includes ffprobe)")
    if exe == "ffmpeg":
        r = subprocess.run([exe, "-hide_banner", "-version"], capture_output=True)
        m = re.match(r"ffmpeg version n?(\d+)\.", r.stdout.decode("utf-8", "ignore"))
        # a build from git reports no release number; it is taken to be recent
        if m and int(m.group(1)) < FFMPEG_MIN_MAJOR:
            die(
                f"ffmpeg {m.group(1)}.x found; riffsheet needs ffmpeg {FFMPEG_MIN_MAJOR}.0 or newer "
                f"(it passes filter scripts as -/filter_complex and keeps frame timing with -fps_mode)"
            )
    _checked.add(exe)


def run(args, timeout=None):
    if args[0] in ("ffmpeg", "ffprobe"):
        _check_exe(args[0])
    try:
        return subprocess.run(args, capture_output=True, timeout=timeout or RUN_TIMEOUT)
    except subprocess.TimeoutExpired:
        die(f"{args[0]} took longer than {timeout or RUN_TIMEOUT} s and was stopped")
    except OSError as e:
        die(f"cannot run {args[0]}: {e.strerror}")


def fq(s):
    """Escape a value (a file path) for an option inside an ffmpeg filtergraph. ffmpeg unescapes it
    twice: once when it splits the graph into filters (special: backslash, quote, [ ] , ;) and once
    when it splits a filter's options (special: backslash, quote, colon). Escaping for both, inner
    level first, lets any path through: spaces, quotes, colons, commas, non-ASCII."""
    inner = re.sub(r"([\\':])", r"\\\1", s)
    return re.sub(r"([\\'\[\],;])", r"\\\1", inner)


def concat_q(s):
    """Quote a path for a line of an ffconcat list (one level of unescaping; a quote inside is
    written as close-quote, escaped quote, open-quote)."""
    return "'" + s.replace("'", "'\\''") + "'"


# ----------------------------------------------------------------------------- probing
def run_timeout_for(duration_s):
    """One ffmpeg pass over a long video can take minutes; the cap only stops a hung process."""
    return max(600, int(10 * (duration_s or 0)))


def check_video_path(video):
    if not os.path.exists(video):
        die("video not found: " + video)
    if os.path.isdir(video):
        die("a folder, not a video file: " + video)
    if not os.access(video, os.R_OK):
        die("cannot read the video (permission denied): " + video)


def probe(video):
    check_video_path(video)
    r = run(["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", video])
    if r.returncode != 0:
        die(
            f"ffprobe cannot read {video}: " + (r.stderr.decode("utf-8", "ignore").strip()[-300:] or "not a media file")
        )
    try:
        p = json.loads(r.stdout)
    except ValueError:
        die("ffprobe gave no readable description of " + video)
    vs = [
        s
        for s in p.get("streams", [])
        if s.get("codec_type") == "video" and not (s.get("disposition") or {}).get("attached_pic")
    ]
    if not vs:
        die(
            "no video stream in "
            + video
            + (" (audio only)" if any(s.get("codec_type") == "audio" for s in p.get("streams", [])) else "")
        )
    v = vs[0]
    w, h = int(v["width"]), int(v["height"])
    rot = 0
    for sd in v.get("side_data_list", []) or []:
        if "rotation" in sd:
            rot = int(float(sd["rotation"]))
    if "rotate" in (v.get("tags") or {}):
        rot = int(v["tags"]["rotate"])
    if abs(rot) % 180 == 90:
        w, h = h, w

    def rate(s):
        try:
            a, b = s.split("/")
            return float(a) / float(b) if float(b) else 0.0
        except Exception:
            return 0.0

    return {
        "width": w,
        "height": h,
        "duration_s": round(float(p["format"].get("duration", 0) or 0), 3),
        "start_time": float(p["format"].get("start_time", 0) or 0),
        "fps_nominal": round(rate(v.get("r_frame_rate", "0/1")), 3),
        "fps_avg": round(rate(v.get("avg_frame_rate", "0/1")), 3),
        "has_audio": any(s.get("codec_type") == "audio" for s in p["streams"]),
        "codec": v.get("codec_name"),
    }


def ranges_list(frames):
    fr = sorted(set(frames))
    parts, a = [], None
    for n in fr:
        if a is None:
            a = b = n
        elif n == b + 1:
            b = n
        else:
            parts.append((a, b))
            a = b = n
    if a is not None:
        parts.append((a, b))
    return parts


def select_graph(frames, chunk=30):
    """select by decoder frame number; long lists are split across parallel selects and
    interleaved back in time order (one huge select expression overflows ffmpeg's parser)."""
    parts = ranges_list(frames)
    exprs = [
        "+".join(f"eq(n\\,{x})" if x == y else f"between(n\\,{x}\\,{y})" for x, y in parts[k : k + chunk])
        for k in range(0, len(parts), chunk)
    ]
    if len(exprs) == 1:
        return f"[0:v]select='{exprs[0]}'"
    g = f"[0:v]split={len(exprs)}" + "".join(f"[s{k}]" for k in range(len(exprs))) + ";"
    g += "".join(f"[s{k}]select='{e}'[t{k}];" for k, e in enumerate(exprs))
    g += "".join(f"[t{k}]" for k in range(len(exprs))) + f"interleave=nb_inputs={len(exprs)}"
    return g


def extract_cells(video, frames, crop, cell_w, cell_h, tmp, tag, info):
    """Decode the chosen frames (by decoder frame number) once, cropped and scaled."""
    os.makedirs(tmp, exist_ok=True)
    fr = sorted(set(frames))
    vf = [select_graph(fr)]
    if crop:
        cx, cy, cw, ch = _box_px(crop, info["width"], info["height"])
        vf.append(f"crop={cw}:{ch}:{cx}:{cy}")
    vf.append(f"scale={cell_w}:{cell_h}:flags=lanczos,setsar=1")
    script = os.path.join(tmp, f"{tag}_x.txt")
    write_text(script, ",".join(vf) + "[o]")
    pat = os.path.join(tmp, f"{tag}_%05d.png")
    r = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostdin",
            "-y",
            "-loglevel",
            "error",
            "-i",
            video,
            "-an",
            "-/filter_complex",
            script,
            "-map",
            "[o]",
            "-fps_mode",
            "passthrough",
            pat,
        ]
    )
    if r.returncode != 0:
        die("frame extraction failed: " + r.stderr.decode()[-400:])
    got = sorted(f for f in os.listdir(tmp) if f.startswith(tag + "_") and f.endswith(".png"))
    if len(got) != len(fr):
        die(f"extracted {len(got)} frames, wanted {len(fr)}")
    return {n: os.path.join(tmp, f) for n, f in zip(fr, got)}


def decode_rgb(video, frames, crop_px, out_w, out_h, tmp):
    """Decode chosen frames (decoder frame numbers) cropped to crop_px=(x,y,w,h), nearest-neighbor
    scaled to out_w x out_h, as raw RGB bytes per frame."""
    fr = sorted(set(frames))
    x, y, w, h = crop_px
    os.makedirs(tmp, exist_ok=True)
    script = os.path.join(tmp, "rgb_x.txt")
    write_text(script, select_graph(fr) + f",crop={w}:{h}:{x}:{y},scale={out_w}:{out_h}:flags=neighbor,format=rgb24[o]")
    r = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-nostdin",
            "-loglevel",
            "error",
            "-i",
            video,
            "-an",
            "-/filter_complex",
            script,
            "-map",
            "[o]",
            "-fps_mode",
            "passthrough",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "rgb24",
            "-",
        ]
    )
    n = out_w * out_h * 3
    raw = r.stdout
    got = [raw[i : i + n] for i in range(0, len(raw) - n + 1, n)]
    # the exit status is not needed: a decode that failed or stopped early gives fewer frames than asked
    if len(got) != len(fr):
        return None
    return dict(zip(fr, got))


def decode_gray_all(video, crop_px, ow, oh, tmp, ref_frame=None):
    """Every frame of a crop, scaled to ow x oh. Without ref_frame: gray frames (bytes). With it: the
    absolute difference of every frame from that frame, per color plane (3 planes of ow x oh bytes per
    frame, planar), computed by ffmpeg."""
    x, y, w, h = crop_px
    chain = f"crop={w}:{h}:{x}:{y},scale={ow}:{oh}:flags=area," + (
        "format=gray" if ref_frame is None else "format=gbrp"
    )
    if ref_frame is None:
        args = [
            "ffmpeg",
            "-hide_banner",
            "-nostdin",
            "-loglevel",
            "error",
            "-i",
            video,
            "-an",
            "-vf",
            chain,
            "-fps_mode",
            "passthrough",
            "-f",
            "rawvideo",
            "-",
        ]
    else:
        ref = os.path.join(tmp, "el_ref.png")
        r = run(
            [
                "ffmpeg",
                "-hide_banner",
                "-nostdin",
                "-y",
                "-loglevel",
                "error",
                "-i",
                video,
                "-an",
                "-vf",
                f"select='eq(n\\,{ref_frame})',{chain}",
                "-frames:v",
                "1",
                ref,
            ]
        )
        if r.returncode != 0:
            return None
        args = [
            "ffmpeg",
            "-hide_banner",
            "-nostdin",
            "-loglevel",
            "error",
            "-i",
            video,
            "-loop",
            "1",
            "-i",
            ref,
            "-an",
            "-filter_complex",
            f"[0:v]{chain}[a];[1:v]format=gbrp[b];[a][b]blend=all_mode=difference:shortest=1[o]",
            "-map",
            "[o]",
            "-fps_mode",
            "passthrough",
            "-f",
            "rawvideo",
            "-",
        ]
    r = run(args)
    # the exit status is not needed: a decode that failed or stopped early gives fewer frames than the
    # video has, and the callers check the count
    n = ow * oh * (1 if ref_frame is None else 3)
    raw = r.stdout
    return [raw[i : i + n] for i in range(0, len(raw) - n + 1, n)]


def _bbox(mask_bytes, w, h, min_px=1):
    """Bounding box (x0, y0, x1, y1, exclusive) of set bytes, ignoring rows/columns with < min_px."""
    rows = [y for y in range(h) if mask_bytes[y * w : (y + 1) * w].count(1) >= min_px]
    if not rows:
        return None
    cols = [0] * w
    for y in rows:
        seg = mask_bytes[y * w : (y + 1) * w]
        k = seg.find(1)
        while k != -1:
            cols[k] += 1
            k = seg.find(1, k + 1)
    xs = [x for x in range(w) if cols[x] >= min_px]
    if not xs:
        return None
    return xs[0], rows[0], xs[-1] + 1, rows[-1] + 1


def _grow(src, w, h):
    """Dilate a 0/1 bytearray by one pixel (3x3)."""
    hz = bytearray(w * h)
    for y in range(h):
        for x in range(w):
            k = y * w + x
            if src[k] or (x > 0 and src[k - 1]) or (x < w - 1 and src[k + 1]):
                hz[k] = 1
    out = bytearray(w * h)
    for y in range(h):
        for x in range(w):
            k = y * w + x
            if hz[k] or (y > 0 and hz[k - w]) or (y < h - 1 and hz[k + w]):
                out[k] = 1
    return out


def _open(m, w, h):
    """Morphological opening of a 0/1 bytearray with a 3x3 square."""

    def erode(src):
        hz = bytearray(w * h)
        for y in range(h):
            row = src[y * w : (y + 1) * w]
            for x in range(1, w - 1):
                if row[x - 1] and row[x] and row[x + 1]:
                    hz[y * w + x] = 1
        out = bytearray(w * h)
        for y in range(1, h - 1):
            for x in range(w):
                k = y * w + x
                if hz[k - w] and hz[k] and hz[k + w]:
                    out[k] = 1
        return out

    return _grow(erode(m), w, h)
