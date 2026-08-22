#!/usr/bin/env python3
"""Manage kuaidi-query privacy policy without touching API credentials."""
from __future__ import annotations
import argparse, json, os, tempfile
from pathlib import Path
from typing import Any
CONFIG_PATH=Path(os.path.expanduser(os.environ.get("KUAIDI_PRIVACY_FILE","~/.openclaw/config/kuaidi-query-privacy.json")))
VALID_MODES=("redact","allowlist","full")
def load_config()->dict[str,Any]:
 if not CONFIG_PATH.exists(): return {"group_mode":"allowlist","trusted_groups":{}}
 try: data=json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError) as e: raise SystemExit(f"隐私配置无法读取或 JSON 已损坏：{CONFIG_PATH}: {e}")
 if not isinstance(data,dict): raise SystemExit(f"隐私配置格式错误：{CONFIG_PATH}")
 mode=data.get("group_mode","allowlist"); groups=data.get("trusted_groups",{})
 if mode not in VALID_MODES or not isinstance(groups,dict): raise SystemExit(f"隐私配置字段无效：{CONFIG_PATH}")
 return {"group_mode":mode,"trusted_groups":groups}
def save_config(data):
 CONFIG_PATH.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix=f".{CONFIG_PATH.name}.",dir=CONFIG_PATH.parent)
 try:
  with os.fdopen(fd,"w",encoding="utf-8") as f: json.dump(data,f,ensure_ascii=False,indent=2); f.write("\n"); f.flush(); os.fsync(f.fileno())
  os.chmod(tmp,0o600); os.replace(tmp,CONFIG_PATH); os.chmod(CONFIG_PATH,0o600)
 finally:
  if os.path.exists(tmp): os.unlink(tmp)
def resolved_policy(data,chat_type,chat_id):
 if chat_type in {"direct","private","c2c"}: return "full"
 mode=data["group_mode"]
 if mode=="full": return "full"
 if mode=="redact": return "redact"
 return "full" if chat_id and chat_id in data["trusted_groups"] else "redact"
def emit(v,j): print(json.dumps(v,ensure_ascii=False,indent=2) if j else v.get("message",json.dumps(v,ensure_ascii=False)))
def parser():
 p=argparse.ArgumentParser(description="管理快递查询的群聊隐私策略"); sub=p.add_subparsers(dest="command",required=True)
 s=sub.add_parser("show"); s.add_argument("--json",action="store_true")
 s=sub.add_parser("set-mode"); s.add_argument("mode",choices=VALID_MODES); s.add_argument("--json",action="store_true")
 s=sub.add_parser("trust"); s.add_argument("group_id"); s.add_argument("--name",default=""); s.add_argument("--json",action="store_true")
 s=sub.add_parser("untrust"); s.add_argument("group_id"); s.add_argument("--json",action="store_true")
 s=sub.add_parser("resolve"); s.add_argument("--chat-type",required=True); s.add_argument("--chat-id"); s.add_argument("--json",action="store_true"); return p
def main():
 args=parser().parse_args(); data=load_config()
 if args.command=="set-mode": data["group_mode"]=args.mode; save_config(data)
 elif args.command=="trust": data["trusted_groups"][args.group_id]={"name":args.name} if args.name else {}; save_config(data)
 elif args.command=="untrust": data["trusted_groups"].pop(args.group_id,None); save_config(data)
 elif args.command=="resolve": emit({"success":True,"policy":resolved_policy(data,args.chat_type,args.chat_id)},args.json); return 0
 emit({"success":True,"group_mode":data["group_mode"],"trusted_groups":data["trusted_groups"],"message":f"群聊隐私模式：{data['group_mode']}；白名单群：{len(data['trusted_groups'])} 个"},args.json); return 0
if __name__=="__main__": raise SystemExit(main())
