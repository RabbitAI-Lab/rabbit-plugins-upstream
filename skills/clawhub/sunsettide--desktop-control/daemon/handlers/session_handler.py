"""
Handler wrappers for multi-session management.
"""
from daemon.utils.session import get_manager


def handle_session_create(params):
    mgr = get_manager()
    monitor = params.get("monitor", 0)
    variables = params.get("variables", {})
    sid = mgr.create(monitor, variables)
    return {"session_id": sid, "info": f"Created session {sid}"}


def handle_session_switch(params):
    mgr = get_manager()
    sid = params.get("session_id")
    if sid is None:
        raise ValueError("Missing required parameter 'session_id' for session_switch.")
    mgr.switch_to(sid)
    return {"session_id": sid, "active": True}


def handle_session_list(params):
    mgr = get_manager()
    sessions = mgr.list()
    return {"sessions": sessions, "current": mgr.current_id}


def handle_session_destroy(params):
    mgr = get_manager()
    sid = params.get("session_id")
    if sid is None:
        raise ValueError("Missing required parameter 'session_id' for session_destroy.")
    mgr.destroy(sid)
    return {"destroyed": sid}
