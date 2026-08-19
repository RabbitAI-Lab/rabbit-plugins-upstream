#!/usr/bin/env python3
"""Initialize kuaidi-query user data outside the skill repository."""
from __future__ import annotations
import argparse, getpass, json, os, re, sys, tempfile
from pathlib import Path
from typing import Any
CONFIG_PATH=Path(os.path.expanduser(os.environ.get("KUAIDI_CONFIG_FILE","~/.openclaw/config/kuaidi-query.json")))
PRIVACY_PATH=Path(os.path.expanduser(os.environ.get("KUAIDI_PRIVACY_FILE","~/.openclaw/config/kuaidi-query-privacy.json")))
SUBSCRIBE_PATH=Path(os.path.expanduser(os.environ.get("KUAIDI_SUBSCRIBE_FILE","~/.openclaw/subscribe/kuaidi.json")))
VALID_MODES=("redact","allowlist","full")
class InitError(RuntimeError): pass
def atomic_create_json(path,value):
 path.parent.mkdir(parents=True,exist_ok=True)
 try: fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
 except FileExistsError: os.chmod(path,0o600); return False
 try:
  with os.fdopen(fd,"w",encoding="utf-8") as f: json.dump(value,f,ensure_ascii=False,indent=2); f.write("\n"); f.flush(); os.fsync(f.fileno())
  os.chmod(path,0o600); return True
 except Exception:
  try: path.unlink()
  except OSError: pass
  raise
def atomic_replace_json(path,value):
 path.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix=f".{path.name}.",dir=path.parent)
 try:
  with os.fdopen(fd,"w",encoding="utf-8") as f: json.dump(value,f,ensure_ascii=False,indent=2); f.write("\n"); f.flush(); os.fsync(f.fileno())
  os.chmod(tmp,0o600); os.replace(tmp,path); os.chmod(path,0o600)
 finally:
  if os.path.exists(tmp): os.unlink(tmp)
def valid_api(v): return isinstance(v,dict) and bool(v.get("app_id")) and bool(v.get("app_key"))
def valid_privacy(v): return isinstance(v,dict) and v.get("group_mode","allowlist") in VALID_MODES and isinstance(v.get("trusted_groups",{}),dict)
def valid_subscriptions(v): return isinstance(v,list)
def validate_existing(path,validator):
 try: value=json.loads(path.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError) as e: raise InitError(f"已有文件无法读取或 JSON 已损坏，未覆盖：{path}") from e
 if not validator(value): raise InitError(f"已有文件字段或格式错误，未覆盖：{path}")
 os.chmod(path,0o600)
def read_credentials(args):
 app_id=args.app_id or os.environ.get("KDNIAO_APP_ID"); app_key=args.app_key or os.environ.get("KDNIAO_APP_KEY")
 if args.skip_api: return None,None
 if not app_id and sys.stdin.isatty(): app_id=input("快递鸟 AppID: ").strip()
 if not app_key and sys.stdin.isatty(): app_key=getpass.getpass("快递鸟 AppKey（输入不回显）: ").strip()
 if not app_id or not app_key: raise InitError("缺少快递鸟凭据。请交互运行，或设置 KDNIAO_APP_ID/KDNIAO_APP_KEY；也可用 --skip-api 仅初始化隐私和订阅文件。")
 return app_id.strip(),app_key.strip()
def current_mode():
 try:
  v=json.loads(PRIVACY_PATH.read_text(encoding="utf-8")); return v.get("group_mode") if isinstance(v,dict) else None
 except (OSError,json.JSONDecodeError): return None
def init(args):
 created=[]; preserved=[]
 if CONFIG_PATH.exists() and not args.replace_api: validate_existing(CONFIG_PATH,valid_api); preserved.append(str(CONFIG_PATH))
 else:
  app_id,app_key=read_credentials(args)
  if app_id is not None:
   config={"app_id":app_id,"app_key":app_key}
   if args.phone_suffix:
    if not re.fullmatch(r"\d{4}",args.phone_suffix): raise InitError("手机尾号必须是 4 位数字")
    config["phone_suffix"]=args.phone_suffix
   atomic_replace_json(CONFIG_PATH,config) if CONFIG_PATH.exists() else atomic_create_json(CONFIG_PATH,config); created.append(str(CONFIG_PATH))
 privacy={"group_mode":args.group_mode,"trusted_groups":{}}
 if PRIVACY_PATH.exists(): validate_existing(PRIVACY_PATH,valid_privacy); preserved.append(str(PRIVACY_PATH))
 elif atomic_create_json(PRIVACY_PATH,privacy): created.append(str(PRIVACY_PATH))
 if SUBSCRIBE_PATH.exists(): validate_existing(SUBSCRIBE_PATH,valid_subscriptions); preserved.append(str(SUBSCRIBE_PATH))
 elif atomic_create_json(SUBSCRIBE_PATH,[]): created.append(str(SUBSCRIBE_PATH))
 return {"success":True,"created":created,"preserved":preserved,"api_configured":CONFIG_PATH.exists(),"group_mode":current_mode(),"message":f"初始化完成：新建 {len(created)} 个文件，保留 {len(preserved)} 个已有文件"}
def file_state(path,validator):
 item={"path":str(path),"exists":path.exists()}
 if not path.exists(): return item
 item["mode"]=oct(path.stat().st_mode&0o777)
 try: item["valid"]=bool(validator(json.loads(path.read_text(encoding="utf-8"))))
 except (OSError,json.JSONDecodeError): item["valid"]=False
 return item
def status():
 api=file_state(CONFIG_PATH,valid_api); privacy=file_state(PRIVACY_PATH,valid_privacy); subs=file_state(SUBSCRIBE_PATH,valid_subscriptions)
 return {"success":True,"api_config":api,"privacy_config":privacy,"subscriptions":subs,"ready":bool(api.get("valid") and privacy.get("valid") and subs.get("valid"))}
def parser():
 p=argparse.ArgumentParser(description="初始化快递查询技能的本地配置"); sub=p.add_subparsers(dest="command",required=True)
 s=sub.add_parser("init"); s.add_argument("--json",action="store_true"); s.add_argument("--app-id"); s.add_argument("--app-key"); s.add_argument("--phone-suffix"); s.add_argument("--group-mode",choices=VALID_MODES,default="allowlist"); s.add_argument("--skip-api",action="store_true"); s.add_argument("--replace-api",action="store_true")
 s=sub.add_parser("status"); s.add_argument("--json",action="store_true"); return p
def emit(v,j): print(json.dumps(v,ensure_ascii=False,indent=2) if j else v.get("message",json.dumps(v,ensure_ascii=False,indent=2)))
def main(argv=None):
 args=parser().parse_args(argv)
 try: emit(init(args) if args.command=="init" else status(),args.json); return 0
 except InitError as e: emit({"success":False,"error":str(e)},args.json); return 2
if __name__=="__main__": raise SystemExit(main())
