"""
File drag-and-drop handler.

Architecture decision: we use **clipboard-based paste + Enter** as the pragmatic
middle ground for common file-upload / import dialogs.

Why not SHDoDragDrop?
  - SHDoDragDrop is *modal* — it blocks until the drag operation completes,
    which means it needs to run in a STA thread.  It also requires correctly
    implementing IDataObject (GetData, EnumFormatEtc, etc.) which is ~200 lines
    of fragile COM boilerplate.
  - WM_DROPFILES is simpler: we post a registered message to the target window
    and pass a FILEGROUPDESCRIPTOR / CF_HDROP via global memory.
    This works for Windows Explorer, FileOpen/Save dialogs, and many apps.

Why not pure mouse-simulation drag?
  - Mouse-sim drag (press -> move -> release) has very poor success rate with
    actual shell drop targets.  Many applications check for OLE drag-drop
    context (DoDragDrop) and ignore plain mouse events.

Current implementation (pragmatic middle ground):
  1. Copy file path to clipboard as CF_HDROP.
  2. Bring the target window to foreground, click the target position.
  3. Ctrl+V to paste the path into the dialog's file-name field.
  4. **Press Enter** to confirm / open the file.   ← critical step
  5. Clear the clipboard (but keep a save/restore for future iterations).

A full SHDoDragDrop implementation is deferred to a future iteration
when the COM IDataObject boilerplate can be tested properly.
"""
import os
import struct
import time

import win32gui
import win32clipboard

from daemon.utils import sendinput as si


def _is_valid_path(path):
    """Check that the given path exists (file or directory)."""
    return os.path.exists(path)


def _get_window_client_rect(hwnd):
    """Return (left, top, right, bottom) of the client area in screen coords."""
    rect = win32gui.GetClientRect(hwnd)
    left, top = win32gui.ClientToScreen(hwnd, (rect[0], rect[1]))
    right, bottom = win32gui.ClientToScreen(hwnd, (rect[2], rect[3]))
    return left, top, right, bottom


def _copy_files_to_clipboard(file_paths):
    """Place one or more file paths on the clipboard as CF_HDROP.

    This is how Explorer's copy-paste of files works internally.
    """
    file_list = "\0".join(file_paths) + "\0\0"
    DROPFILES_STRUCT = struct.Struct("=Iiiii?")
    pfiles = DROPFILES_STRUCT.size
    drop_data = DROPFILES_STRUCT.pack(pfiles, 0, 0, False, True) + file_list.encode("utf-16-le")

    win32clipboard.OpenClipboard()
    try:
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_HDROP, drop_data)
    finally:
        win32clipboard.CloseClipboard()


def _clear_clipboard():
    """Empty the clipboard to prevent accidental paste leakage."""
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
    except Exception:
        pass
    finally:
        try:
            win32clipboard.CloseClipboard()
        except Exception:
            pass


def handle_file_drag_drop(params):
    """Drag-and-drop a file onto a target window.

    Workflow:
      1. Copy file path to clipboard (CF_HDROP)
      2. Focus target window & click target position
      3. Ctrl+V to paste path
      4. Press Enter to confirm open/upload

    Params:
        hwnd:       target window handle (required)
        file_path:  absolute path to the file/folder to drop (required)
        x, y:       target coordinates within the window client area (optional;
                    defaults to centre of the window)

    Returns:
        {"action": "file_drag_drop", "hwnd": hwnd, "file": file_path}
    """
    hwnd = params.get("hwnd")
    if not hwnd:
        raise ValueError(
            "Missing required parameter 'hwnd' for file_drag_drop. "
            "Example: {\"hwnd\": 123456, \"file_path\": \"C:\\\\test.png\", \"x\": 100, \"y\": 200}"
        )
    file_path = params.get("file_path", "")
    if not file_path:
        raise ValueError("Missing required parameter 'file_path' for file_drag_drop.")

    if not _is_valid_path(file_path):
        raise ValueError(f"File not found: {file_path}")

    if not win32gui.IsWindow(hwnd):
        raise ValueError(f"Invalid or destroyed hwnd: {hwnd}")

    x = params.get("x")
    y = params.get("y")

    if x is None or y is None:
        left, top, right, bottom = _get_window_client_rect(hwnd)
        x = (left + right) // 2
        y = (top + bottom) // 2

    # Step 1: Copy file path to clipboard
    _copy_files_to_clipboard([file_path])

    try:
        # Step 2: Bring target window to foreground
        try:
            from .window import _force_foreground
            _force_foreground(hwnd)
        except Exception:
            win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.3)

        # Step 3: Click target position to focus the file-name input
        si.mouse_move(x, y)
        time.sleep(0.1)
        si.mouse_click(x, y, "left", 1)
        time.sleep(0.2)

        # Step 4: Ctrl+V to paste the file path
        si.keyboard_hotkey(si.VK["ctrl"], ord("V"))
        time.sleep(0.2)

        # Step 5: Press Enter to submit the dialog
        si.keyboard_press(si.VK["enter"])
        time.sleep(0.3)
    finally:
        # Always clear the clipboard — never leave user data exposed
        _clear_clipboard()

    return {
        "action": "file_drag_drop",
        "hwnd": hwnd,
        "file": file_path,
        "x": x,
        "y": y,
        "method": "clipboard_paste_enter",
        "note": "Clipboard paste + Enter. Full SHDoDragDrop deferred.",
    }
