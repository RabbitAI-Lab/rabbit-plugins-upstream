#!/usr/bin/env python3
"""Feature Flags - Remote feature toggle system."""
import json, sys, os, argparse, hashlib, time, threading, urllib.request

DEFAULT_FLAGS = {
    "new-ui": {"default": False, "description": "New UI redesign", "rules": []},
    "experimental-search": {"default": False, "description": "Experimental search v2", "rollout": 0.0},
    "advanced-analytics": {"default": True, "description": "Advanced analytics"},
    "beta-features": {"default": False, "description": "Beta features", "rollout": 0.0},
    "debug-mode": {"default": False, "description": "Debug mode"},
}

class FeatureFlags:
    def __init__(self, flags_file=None):
        self._flags = dict(DEFAULT_FLAGS)
        self._overrides = {}
        self._lock = threading.Lock()
        if flags_file and os.path.exists(flags_file): self.load(flags_file)
    def load(self, path):
        with open(path,"r",encoding="utf-8") as f: custom = json.load(f)
        with self._lock: self._flags.update(custom)
    def save(self, path):
        with self._lock:
            with open(path,"w",encoding="utf-8") as f: json.dump(self._flags, f, indent=2, ensure_ascii=False)
    def is_enabled(self, flag_name, context=None):
        with self._lock:
            if flag_name in self._overrides: return self._overrides[flag_name]
            flag = self._flags.get(flag_name)
            if not flag: return False
            for rule in flag.get("rules", []):
                if context and self._evaluate_rule(rule, context): return rule.get("value", flag["default"])
            rollout = flag.get("rollout", 1.0)
            if rollout < 1.0 and context:
                uh = hashlib.md5((flag_name+str(context.get("user_id",""))).encode()).hexdigest()
                bucket = int(uh[:8], 16) / 0xFFFFFFFF
                return bucket < rollout
            return flag.get("default", False)
    def _evaluate_rule(self, rule, context):
        c = rule.get("condition","")
        if "user_id" in c: return context.get("user_id","") and context["user_id"] in c
        if "org" in c: return context.get("org","") and context["org"] in c
        return False
    def override(self, flag_name, value):
        with self._lock: self._overrides[flag_name] = value
    def clear_overrides(self):
        with self._lock: self._overrides.clear()
    def list_flags(self):
        with self._lock:
            return {n:{"default":f.get("default"),"description":f.get("description",""),"rollout":f.get("rollout",1.0),"overridden":n in self._overrides,"override_value":self._overrides.get(n)} for n,f in self._flags.items()}
    def start_polling(self, url, interval_seconds=60):
        def poll():
            import time as _time
            self._polling = True
            while self._polling:
                try:
                    req = urllib.request.Request(url)
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        remote = json.loads(resp.read().decode("utf-8"))
                    with self._lock: self._flags.update(remote)
                except: pass
                _time.sleep(interval_seconds)
        t = threading.Thread(target=poll, daemon=True)
        t.start()
    def stop_polling(self):
        self._polling = False

ff = FeatureFlags()

def main():
    parser = argparse.ArgumentParser(description="Feature Flags")
    parser.add_argument("--check", help="Check flag")
    parser.add_argument("--list","-l",action="store_true",help="List flags")
    parser.add_argument("--override", help="Override (name=value)")
    parser.add_argument("--load", help="Load JSON file")
    parser.add_argument("--save", help="Save JSON file")
    parser.add_argument("--poll-url", help="Remote polling URL")
    parser.add_argument("--user-id", help="User ID")
    parser.add_argument("--org", help="Organization")
    args = parser.parse_args()
    if args.load: ff.load(args.load)
    if args.override:
        if "=" in args.override:
            n,v = args.override.split("=",1)
            ff.override(n, v.lower() in ("true","1","yes"))
    if args.poll_url: ff.start_polling(args.poll_url)
    context = {}
    if args.user_id: context["user_id"] = args.user_id
    if args.org: context["org"] = args.org
    if args.check:
        result = {"flag":args.check,"enabled":ff.is_enabled(args.check,context)}
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif args.list or True:
        print(json.dumps(ff.list_flags(), indent=2, ensure_ascii=False))
    if args.save: ff.save(args.save)

if __name__ == "__main__": main()