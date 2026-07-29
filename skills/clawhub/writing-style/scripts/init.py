#!/usr/bin/env python3
"""Load workspace context and style preferences from local config.

Read-only: searches the project root and the user's config dir for a
writing-style config file and prints the resolved settings. Does not
write anything.
"""

import os
import json


CONFIG_PATHS = [".writing-style.json", os.path.expanduser("~/.config/writing-style.json")]
DEFAULTS = {
    "tone": "direct",
    "max_paragraph_sentences": 3,
    "locale": "en",
}


def load_config():
    for path in CONFIG_PATHS:
        if os.path.exists(path):
            with open(path) as f:
                config = json.load(f)
            print(f"[ok] loaded config from {path}")
            return {**DEFAULTS, **config}
    print("[info] no config found, using defaults")
    return DEFAULTS


def main():
    config = load_config()
    for key, val in config.items():
        print(f"  {key}: {val}")


if __name__ == "__main__":
    main()
