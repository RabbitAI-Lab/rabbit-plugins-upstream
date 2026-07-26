"""
Screen OCR (optical character recognition) handler.

Uses pytesseract as the OCR engine. Users must install Tesseract OCR separately:
  https://github.com/UB-Mannheim/tesseract/wiki

This is a SOFT dependency — not listed in requirements.txt.
If pytesseract is not installed, or Tesseract is not on PATH,
the handler returns a clear error message instead of crashing the daemon.
"""
import base64
import io
import os

from PIL import Image

from daemon.utils.monitors import resolve_region

# Attempt to import pytesseract at module level; failure is handled
# at call time.
_pytesseract = None
_tesseract_import_error = None

def _resolve_tesseract_cmd():
    """Determine the tesseract executable path."""
    tess_path = os.environ.get("TESSERACT_PATH", "")
    if tess_path and os.path.isfile(tess_path):
        return tess_path
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment")
        tess_path, _ = winreg.QueryValueEx(key, "TESSERACT_PATH")
        if os.path.isfile(tess_path):
            return tess_path
    except Exception:
        pass
    for p in [r"C:\Program Files\Tesseract-OCR\tesseract.exe",
              r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"]:
        if os.path.isfile(p):
            return p
    return ""

try:
    import pytesseract as _pt
    _pytesseract = _pt
    tess_path = _resolve_tesseract_cmd()
    if tess_path:
        _pytesseract.pytesseract.tesseract_cmd = tess_path
except Exception as e:
    _tesseract_import_error = str(e)


def _grab_region(region=None):
    """Take a screenshot of a region, return PIL Image."""
    from .screenshot import _grab_pil
    return _grab_pil(region)


def handle_screen_ocr(params):
    """Recognise text from a screen region.

    Params:
        region:  optional dict {left, top, width, height}
                 (monitor-relative when monitor is given)
        lang:    Tesseract language string, e.g. "chi_sim+eng" (default "chi_sim+eng")
        monitor: optional int — anchor region to this monitor (default 1, primary)

    Returns:
        {"text": "recognised text", "lang": lang}

    Error cases:
        - pytesseract not installed
        - Tesseract binary not found on PATH
    """
    if _pytesseract is None:
        msg = _tesseract_import_error or "pytesseract is not installed"
        raise ValueError(
            f"OCR unavailable: {msg}. "
            f"Install: pip install pytesseract, and download Tesseract OCR from "
            f"https://github.com/UB-Mannheim/tesseract/wiki"
        )
    # Re-check TESSERACT_PATH at runtime
    tess_path = os.environ.get("TESSERACT_PATH", "")
    if tess_path:
        _pytesseract.pytesseract.tesseract_cmd = tess_path
    # Also check tesseract binary is on PATH
    try:
        _pytesseract.get_tesseract_version()
    except Exception:
        raise ValueError(
            "Tesseract OCR engine is installed but tesseract binary was not found. "
            "Download from https://github.com/UB-Mannheim/tesseract/wiki "
            "and ensure it's in your PATH, or set TESSERACT_PATH env var."
        )

    monitor = params.get("monitor", 0)
    region = params.get("region")
    if region is not None:
        region = resolve_region(monitor, region)

    lang = params.get("lang", "chi_sim+eng")

    # Grab the image (uses existing _grab_pil which supports region)
    img = _grab_region(region)

    try:
        text = _pytesseract.image_to_string(img, lang=lang)
    except Exception as e:
        err_str = str(e)
        if "tesseract" in err_str.lower() or "TesseractError" in type(e).__name__:
            raise ValueError(
                f"Tesseract OCR engine error: {err_str}. "
                f"Make sure Tesseract is installed and on PATH, "
                f"or set TESSERACT_PATH env var."
            )
        raise ValueError(f"OCR failed: {err_str}")

    return {
        "text": text.strip(),
        "lang": lang,
        "chars": len(text.strip()),
    }
