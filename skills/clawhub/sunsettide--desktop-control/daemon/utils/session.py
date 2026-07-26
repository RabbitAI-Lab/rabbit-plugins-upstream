"""
Multi-session manager.

Each Session carries:
  - session_id (int, 0 = default)
  - monitor index (for coordinate anchoring)
  - variables dict (key-value, accessible by script engine)
  - focused_hwnd (last focused window for this session)

Sessions are independent — one daemon can have N sessions each controlling
a different monitor or window context.
"""
import threading


class Session:
    """One operational context."""

    def __init__(self, session_id, monitor=0, variables=None):
        self.id = session_id
        self.monitor = monitor
        self.variables = dict(variables or {})
        self.focused_hwnd = None

    def to_dict(self):
        return {
            "id": self.id,
            "monitor": self.monitor,
            "variables": dict(self.variables),
            "focused_hwnd": self.focused_hwnd,
        }


class SessionManager:
    """Thread-safe manager for multiple sessions.

    Session 0 is the default session, always exists, always backward-compatible.
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._sessions = {0: Session(0, monitor=0, variables={})}
        self._next_id = 1
        self._current_id = 0  # default

    # --- Current session ---

    @property
    def current(self):
        with self._lock:
            return self._sessions.get(self._current_id)

    @property
    def current_id(self):
        return self._current_id

    def switch_to(self, session_id):
        with self._lock:
            if session_id not in self._sessions:
                raise ValueError(f"Session '{session_id}' not found.")
            self._current_id = session_id

    # --- CRUD ---

    def create(self, monitor=0, variables=None):
        with self._lock:
            sid = self._next_id
            self._next_id += 1
            self._sessions[sid] = Session(sid, monitor, variables)
            return sid

    def destroy(self, session_id):
        if session_id == 0:
            raise ValueError("Cannot destroy the default session (id=0).")
        with self._lock:
            if session_id not in self._sessions:
                raise ValueError(f"Session '{session_id}' not found.")
            del self._sessions[session_id]
            # If the current session was destroyed, fall back to default
            if self._current_id == session_id:
                self._current_id = 0

    def list(self):
        with self._lock:
            return {sid: s.to_dict() for sid, s in self._sessions.items()}

    # --- Variable helpers ---

    def get_variable(self, name, default=None):
        s = self.current
        if s:
            return s.variables.get(name, default)
        return default

    def set_variable(self, name, value):
        s = self.current
        if s:
            s.variables[name] = value

    def resolve_vars(self, value):
        """Replace {{var_name}} placeholders in a string with session variables.
        Works recursively for nested structures."""
        import re
        s = self.current
        if s is None:
            return value
        if isinstance(value, str):
            def _replace(m):
                var_name = m.group(1)
                return str(s.variables.get(var_name, m.group(0)))
            return re.sub(r"\{\{(\w+)\}\}", _replace, value)
        elif isinstance(value, dict):
            return {k: self.resolve_vars(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [self.resolve_vars(v) for v in value]
        return value

    # --- Monitor preference ---

    def get_effective_monitor(self, params_monitor=None):
        """Return the effective monitor index.

        Priority: explicit params > session default > 0 (virtual desktop).
        """
        if params_monitor is not None and params_monitor != 0:
            return params_monitor
        s = self.current
        if s and s.monitor:
            return s.monitor
        return 0


# Global session manager (singleton)
_manager = SessionManager()


def get_manager():
    return _manager
