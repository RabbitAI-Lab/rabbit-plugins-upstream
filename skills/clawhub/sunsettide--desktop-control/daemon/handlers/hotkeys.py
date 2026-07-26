"""
Hotkey handler wrappers.

Delegates to daemon.utils.hotkeys for the actual logic.
Keeps handler files in daemon/handlers/ for consistency.
"""

from daemon.utils import hotkeys as hk


def handle_register(params):
    hotkey_id = params.get("id")
    if not hotkey_id:
        raise ValueError(
            "Missing required parameter 'id' for register_hotkey. "
            "Example: {\"id\": \"my_hotkey\", \"modifiers\": 2, \"key\": 120, "
            "\"action\": \"screenshot\", \"params\": {}}"
        )
    modifiers = params.get("modifiers", 0)
    key = params.get("key")
    if not key:
        raise ValueError("Missing required parameter 'key' (virtual key code) for register_hotkey.")
    action = params.get("action")
    if not action:
        raise ValueError("Missing required parameter 'action' for register_hotkey.")
    act_params = params.get("params", {})

    return hk.register(hotkey_id, int(modifiers), int(key), action, act_params)


def handle_unregister(params):
    hotkey_id = params.get("id")
    unregister_all = params.get("all", False)
    if not hotkey_id and not unregister_all:
        raise ValueError(
            "Provide 'id' to unregister one hotkey, or 'all': true to clear all."
        )
    return hk.unregister(hotkey_id, unregister_all)


def handle_list(params):
    return hk.list_hotkeys()
