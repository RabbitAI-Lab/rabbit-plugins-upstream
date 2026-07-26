"""
Dedicated STA thread pool for UIA (pywinauto) operations.
Each thread initializes COM in STA mode and only returns serializable data.
No COM objects cross thread boundaries.
"""
import pythoncom
from concurrent.futures import ThreadPoolExecutor, Future


def _sta_init():
    """Initialize COM as STA for this thread. Called once per worker."""
    pythoncom.CoInitialize()


class UIAThreadPool:
    """
    A thread pool where every worker runs in an STA COM apartment.
    Submit UIA tasks here; they return plain Python data (dicts, strs, ints).
    Never return COM interface pointers or pywinauto wrapper objects across threads.
    """

    def __init__(self, max_workers: int = 2):
        self._executor = ThreadPoolExecutor(
            max_workers=max_workers,
            initializer=_sta_init,
        )

    def submit(self, fn, *args, **kwargs) -> Future:
        """Submit a UIA operation to the STA pool. Returns a Future."""
        return self._executor.submit(fn, *args, **kwargs)

    def shutdown(self, wait: bool = True):
        """Shut down the thread pool. Do NOT call CoUninitialize — threads clean up on exit."""
        self._executor.shutdown(wait=wait)
