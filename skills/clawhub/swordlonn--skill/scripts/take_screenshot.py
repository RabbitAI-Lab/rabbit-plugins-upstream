#!/usr/bin/env python3
"""
WatchItAI - Cross-platform screenshot helper (macOS / Linux)

Supports:
  - Full-screen capture (all displays on macOS, virtual desktop on Linux)
  - App-specific window capture (macOS only)
  - Specific window (by id or name)
  - Active/frontmost window
  - Pixel region capture
  - Multiple output modes: default (Pictures folder), temp, or explicit path

Usage:
  python3 take_screenshot.py                          # full screen, default location
  python3 take_screenshot.py --mode temp              # full screen, temp dir
  python3 take_screenshot.py --path /path/to/out.png  # explicit path
  python3 take_screenshot.py --app "AppName"          # capture all windows of an app (macOS)
  python3 take_screenshot.py --active-window          # active window only
  python3 take_screenshot.py --window-id 12345        # specific window id
  python3 take_screenshot.py --region x,y,w,h         # pixel region
  python3 take_screenshot.py --list-windows --app "X" # list matching windows (macOS)
"""

import argparse
import os
import sys
import tempfile
import time
import subprocess
from pathlib import Path


def get_platform():
    return sys.platform


def is_macos():
    return sys.platform == "darwin"


def is_linux():
    return sys.platform.startswith("linux")


def get_default_screenshot_dir():
    """Get OS default screenshot location."""
    if is_macos():
        # macOS default is Desktop
        desktop = Path.home() / "Desktop"
        if desktop.exists():
            return str(desktop)
    elif is_linux():
        # Try XDG_PICTURES_DIR, then ~/Pictures, then ~/Desktop
        pictures = os.environ.get("XDG_PICTURES_DIR", str(Path.home() / "Pictures"))
        p = Path(pictures)
        if p.exists():
            return str(p)
        desktop = Path.home() / "Desktop"
        if desktop.exists():
            return str(desktop)
    return str(Path.home())


def generate_filename(prefix="watchitai", ext="png"):
    timestamp = time.strftime("%Y-%m-%d at %H.%M.%S")
    return f"{prefix} {timestamp}.{ext}"


def run_cmd(cmd, check=True):
    """Run a command and return (returncode, stdout, stderr)."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=check,
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except FileNotFoundError:
        return 127, "", f"Command not found: {cmd[0]}"
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stdout.strip(), e.stderr.strip()


# ============================================================
# macOS capture with Quartz API (no subprocess)
# ============================================================
def macos_capture_quartz(region=None, window_id=None):
    """Capture screen using macOS Quartz API (no subprocess needed)."""
    import Quartz
    import LaunchServices
    import io
    
    if window_id:
        image = Quartz.CGWindowListCreateImage(
            Quartz.CGRectInfinite,
            Quartz.kCGWindowListOptionIncludingWindow,
            window_id,
            Quartz.kCGWindowImageDefault
        )
    elif region:
        x, y, w, h = region
        rect = Quartz.CGRectMake(x, y, w, h)
        image = Quartz.CGWindowListCreateImage(
            rect,
            Quartz.kCGWindowListOptionOnScreenOnly,
            0,
            Quartz.kCGWindowImageDefault
        )
    else:
        image = Quartz.CGWindowListCreateImage(
            Quartz.CGRectInfinite,
            Quartz.kCGWindowListOptionOnScreenOnly,
            0,
            Quartz.kCGWindowImageDefault
        )
    
    if not image:
        raise RuntimeError("Failed to capture screen with Quartz")
    
    data = Quartz.CFDataCreateMutable(None, 0)
    destination = Quartz.CGImageDestinationCreateWithData(data, LaunchServices.kUTTypePNG, 1, None)
    
    properties = {Quartz.kCGImageDestinationLossyCompressionQuality: 0.9}
    Quartz.CGImageDestinationAddImage(destination, image, properties)
    success = Quartz.CGImageDestinationFinalize(destination)
    
    if not success:
        raise RuntimeError("Failed to write image")
    
    return Quartz.CFDataGetBytePtr(data)[:Quartz.CFDataGetLength(data)]


# ============================================================
# macOS capture
# ============================================================
def macos_screencapture(path, region=None, window_id=None, interactive=False):
    """Capture using macOS screencapture command."""
    cmd = ["screencapture", "-x"]  # -x = no sound

    if region:
        x, y, w, h = region
        cmd += ["-R", f"{x},{y},{w},{h}"]
    elif window_id:
        cmd += ["-l", str(window_id)]
    elif interactive:
        cmd += ["-i"]

    cmd.append(path)

    ret, out, err = run_cmd(cmd, check=False)
    if ret != 0:
        raise RuntimeError(f"screencapture failed: {err or out}")
    return path


def macos_list_windows(app_name=None):
    """List windows using Quartz (if available) or AppleScript."""
    try:
        import Quartz
        options = Quartz.kCGWindowListOptionOnScreenOnly
        if app_name:
            # Get all windows, filter by app name
            window_list = Quartz.CGWindowListCopyWindowInfo(options, 0)
            result = []
            for w in window_list or []:
                owner = w.get("kCGWindowOwnerName", "")
                if app_name.lower() in owner.lower():
                    wid = w.get("kCGWindowNumber", 0)
                    name = w.get("kCGWindowName", "")
                    bounds = w.get("kCGWindowBounds", {})
                    result.append({
                        "id": wid,
                        "app": owner,
                        "title": name,
                        "x": bounds.get("X", 0),
                        "y": bounds.get("Y", 0),
                        "width": bounds.get("Width", 0),
                        "height": bounds.get("Height", 0),
                    })
            return result
        else:
            window_list = Quartz.CGWindowListCopyWindowInfo(options, 0)
            return [
                {
                    "id": w.get("kCGWindowNumber", 0),
                    "app": w.get("kCGWindowOwnerName", ""),
                    "title": w.get("kCGWindowName", ""),
                    "x": w.get("kCGWindowBounds", {}).get("X", 0),
                    "y": w.get("kCGWindowBounds", {}).get("Y", 0),
                    "width": w.get("kCGWindowBounds", {}).get("Width", 0),
                    "height": w.get("kCGWindowBounds", {}).get("Height", 0),
                }
                for w in window_list or []
            ]
    except ImportError:
        # Fallback: AppleScript (less detailed)
        script = 'tell application "System Events" to get {name, id} of every window of every process whose visible is true'
        ret, out, err = run_cmd(["osascript", "-e", script], check=False)
        if ret != 0:
            raise RuntimeError(f"Cannot list windows: {err or out}")
        return []


def macos_capture_app(app_name, output_dir):
    """Capture all visible windows of a specific app (macOS only)."""
    windows = macos_list_windows(app_name)
    if not windows:
        raise RuntimeError(f"No windows found for app: {app_name}")

    saved_paths = []
    for w in windows:
        wid = w["id"]
        if not wid:
            continue
        fname = f"watchitai-{w['app'].replace(' ', '_')}-w{wid}.png"
        outpath = str(Path(output_dir) / fname)
        try:
            macos_screencapture(outpath, window_id=wid)
            saved_paths.append(outpath)
        except Exception as e:
            print(f"Warning: failed to capture window {wid}: {e}", file=sys.stderr)

    if not saved_paths:
        raise RuntimeError(f"Failed to capture any windows for {app_name}")
    return saved_paths


# ============================================================
# Linux capture
# ============================================================
def linux_find_tool():
    """Find the first available screenshot tool on Linux."""
    tools = [
        ("scrot", ["scrot"]),
        ("gnome-screenshot", ["gnome-screenshot", "-f"]),
        ("import", ["import", "-window", "root"]),
    ]
    for name, cmd in tools:
        ret, _, _ = run_cmd(["which", name], check=False)
        if ret == 0:
            return name, cmd
    return None, None


def linux_capture(path, region=None, active_window=False):
    """Capture screen on Linux using best available tool."""
    tool_name, tool_cmd = linux_find_tool()
    if not tool_name:
        raise RuntimeError(
            "No screenshot tool found. Install one of: scrot, gnome-screenshot, ImageMagick (import)"
        )

    cmd = list(tool_cmd)

    if tool_name == "scrot":
        if region:
            x, y, w, h = region
            cmd += ["-a", f"{x},{y},{w},{h}"]
        elif active_window:
            cmd += ["-u"]
        cmd.append(path)
    elif tool_name == "gnome-screenshot":
        if region:
            cmd = ["gnome-screenshot", "-a", "-f", path]
        elif active_window:
            cmd = ["gnome-screenshot", "-w", "-f", path]
        else:
            cmd = ["gnome-screenshot", "-f", path]
    elif tool_name == "import":
        if region:
            x, y, w, h = region
            cmd = ["import", "-window", "root", "-crop", f"{w}x{h}+{x}+{y}", path]
        elif active_window:
            cmd = ["import", "-window", "root", path]  # import doesn't have active window easily
        else:
            cmd.append(path)

    ret, out, err = run_cmd(cmd, check=False)
    if ret != 0:
        raise RuntimeError(f"{tool_name} failed: {err or out}")
    return path


# ============================================================
# Main
# ============================================================
def compress_image(data, quality=85, max_width=None):
    """Compress image with optional resizing."""
    try:
        from PIL import Image
        import io
        
        img = Image.open(io.BytesIO(data))
        
        if max_width and img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.LANCZOS)
        
        output = io.BytesIO()
        img.save(output, format="JPEG", quality=quality, optimize=True)
        return output.getvalue()
    except ImportError:
        return data


def capture_to_buffer(region=None, window_id=None, quality=85, max_width=None):
    """Capture screen and return compressed image bytes."""
    import io
    
    if is_macos():
        try:
            data = macos_capture_quartz(region=region, window_id=window_id)
            if data:
                return compress_image(data, quality=quality, max_width=max_width)
        except (ImportError, RuntimeError):
            pass
        
        tmp_path = os.path.join(tempfile.gettempdir(), f"watchitai_capture_{os.getpid()}.png")
        cmd = ["screencapture", "-x", "-t", "png", tmp_path]
        if region:
            x, y, w, h = region
            cmd += ["-R", f"{x},{y},{w},{h}"]
        elif window_id:
            cmd += ["-l", str(window_id)]
        
        result = subprocess.run(cmd, capture_output=True)
        if result.returncode != 0:
            raise RuntimeError(f"screencapture failed: {result.stderr.decode('utf-8', errors='ignore')}")
        
        if os.path.exists(tmp_path):
            with open(tmp_path, "rb") as f:
                data = f.read()
            os.unlink(tmp_path)
            return compress_image(data, quality=quality, max_width=max_width)
        raise RuntimeError("screencapture failed: no file created")
    
    elif is_linux():
        tool_name, tool_cmd = linux_find_tool()
        if not tool_name:
            raise RuntimeError("No screenshot tool found")
        
        cmd = list(tool_cmd)
        if tool_name == "scrot":
            if region:
                x, y, w, h = region
                cmd += ["-a", f"{x},{y},{w},{h}"]
            cmd += ["-e", "cat $f"]
        elif tool_name == "gnome-screenshot":
            if region:
                cmd = ["gnome-screenshot", "-a", "-f", "/dev/stdout"]
            else:
                cmd = ["gnome-screenshot", "-f", "/dev/stdout"]
        elif tool_name == "import":
            if region:
                x, y, w, h = region
                cmd = ["import", "-window", "root", "-crop", f"{w}x{h}+{x}+{y}", "/dev/stdout"]
            else:
                cmd = ["import", "-window", "root", "/dev/stdout"]
        
        result = subprocess.run(cmd, capture_output=True)
        if result.returncode != 0:
            raise RuntimeError(f"{tool_name} failed: {result.stderr.decode('utf-8', errors='ignore')}")
        return result.stdout
    
    else:
        raise RuntimeError(f"Unsupported platform: {get_platform()}")


def run_server_mode():
    """Run in server mode: read commands from stdin, write image bytes to stdout."""
    import sys
    import json
    
    sys.stdout.reconfigure(line_buffering=True)
    
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            
            line = line.strip()
            if not line:
                continue
            
            if line == "QUIT":
                break
            
            try:
                cmd = json.loads(line)
            except json.JSONDecodeError:
                cmd = {"action": "capture"}
            
            action = cmd.get("action", "capture")
            
            if action == "capture":
                region = cmd.get("region")
                window_id = cmd.get("window_id")
                quality = cmd.get("quality", 85)
                max_width = cmd.get("maxWidth")
                
                try:
                    data = capture_to_buffer(
                        region=region, 
                        window_id=window_id,
                        quality=quality,
                        max_width=max_width,
                    )
                    sys.stdout.write(f"OK {len(data)}\n")
                    sys.stdout.flush()
                    sys.stdout.buffer.write(data)
                    sys.stdout.flush()
                except Exception as e:
                    sys.stdout.write(f"ERROR {str(e)}\n")
                    sys.stdout.flush()
            
            elif action == "ping":
                sys.stdout.write("OK 4\n")
                sys.stdout.flush()
                sys.stdout.buffer.write(b"pong")
                sys.stdout.flush()
            
            else:
                sys.stdout.write(f"ERROR Unknown action: {action}\n")
                sys.stdout.flush()
                
        except Exception as e:
            try:
                sys.stdout.write(f"ERROR {str(e)}\n")
                sys.stdout.flush()
            except:
                break


def main():
    parser = argparse.ArgumentParser(description="WatchItAI screenshot helper")
    parser.add_argument("--mode", choices=["default", "temp"], default="default",
                        help="Output mode: default (Pictures/Desktop) or temp directory")
    parser.add_argument("--path", type=str, help="Explicit output file path")
    parser.add_argument("--app", type=str, help="Capture all windows of this app (macOS only)")
    parser.add_argument("--window-name", type=str, help="Window title to match (macOS only)")
    parser.add_argument("--window-id", type=int, help="Capture specific window ID")
    parser.add_argument("--active-window", action="store_true", help="Capture active/frontmost window")
    parser.add_argument("--list-windows", action="store_true", help="List matching windows (macOS only)")
    parser.add_argument("--region", type=str, help="Pixel region: x,y,w,h")
    parser.add_argument("--server", action="store_true", help="Run in server mode (pipe communication)")

    args = parser.parse_args()
    
    if args.server:
        run_server_mode()
        return

    # Determine output path / directory
    if args.path:
        out_path = args.path
        out_dir = str(Path(out_path).parent)
        Path(out_dir).mkdir(parents=True, exist_ok=True)
    elif args.mode == "temp":
        out_dir = tempfile.gettempdir()
        out_path = str(Path(out_dir) / generate_filename())
    else:
        out_dir = get_default_screenshot_dir()
        out_path = str(Path(out_dir) / generate_filename())

    # --list-windows
    if args.list_windows:
        if not is_macos():
            print("Error: --list-windows is only supported on macOS", file=sys.stderr)
            sys.exit(1)
        try:
            windows = macos_list_windows(args.app)
            for w in windows:
                print(f"Window ID: {w['id']:>8} | App: {w['app']:<30} | Title: {w['title']}")
            return
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    region = None
    if args.region:
        try:
            parts = [int(x.strip()) for x in args.region.split(",")]
            if len(parts) != 4:
                raise ValueError
            region = tuple(parts)
        except ValueError:
            print("Error: --region must be x,y,w,h (e.g. 100,200,800,600)", file=sys.stderr)
            sys.exit(1)

    try:
        saved = []

        if is_macos():
            if args.app and not args.window_id and not args.window_name:
                saved = macos_capture_app(args.app, out_dir if not args.path else str(Path(out_path).parent))
            elif args.window_id:
                macos_screencapture(out_path, window_id=args.window_id)
                saved = [out_path]
            elif args.active_window:
                # On macOS, capture active window using screencapture -w (interactive-ish)
                # We'll just do full screen for simplicity, or use Quartz
                macos_screencapture(out_path, region=region)
                saved = [out_path]
            else:
                macos_screencapture(out_path, region=region)
                saved = [out_path]

        elif is_linux():
            linux_capture(out_path, region=region, active_window=args.active_window)
            saved = [out_path]

        else:
            print(f"Error: unsupported platform: {get_platform()}", file=sys.stderr)
            sys.exit(1)

        # Print saved paths (one per line)
        for p in saved:
            print(p)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        # Check for common permission errors and give helpful hints
        err_str = str(e).lower()
        if is_macos() and ("could not create image" in err_str or "screen capture" in err_str):
            print("\nHint: Screen Recording permission may be missing.", file=sys.stderr)
            print("Go to System Settings → Privacy & Security → Screen Recording", file=sys.stderr)
            print("and enable permission for your terminal / Trae.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
