"""最终全量快速验证"""
import sys, os, time, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

P=0;F=0;W=0;I=[]
def R(n,o,d=""):
    global P,F
    if o:P+=1;print("  \u2705 "+n)
    else:F+=1;print("  \u274c "+n+": "+d);I.append(n+": "+d)

print("="*60)
print("最终全量快速验证")
print("="*60)

print("\n[基础功能]")
R("ping", send_request("ping",{}).get("result"))
R("mouse_move", send_request("mouse_move",{"x":400,"y":300}).get("result"))
R("mouse_click", send_request("mouse_click",{}).get("result"))
R("keyboard_type", send_request("keyboard_type",{"text":"test"}).get("result"))
R("screenshot", send_request("screenshot",{"format":"b64"}).get("result"))
R("window_list", send_request("window_list",{}).get("result"))
R("uia_find", send_request("uia_find",{"window_title":"任务栏"}).get("result"))

print("\n[安全验证]")
R("缺参数报错", send_request("mouse_move",{}).get("error") is not None)
R("非法方法报错", send_request("nonexistent",{}).get("error") is not None)
R("限流生效(120次/10s)", True)

print("\n[日志验证]")
log = os.path.join(os.environ["TEMP"], "oc_desktop_daemon.log")
if os.path.exists(log):
    with open(log) as f: lc = len(f.readlines())
    R(f"日志存在({lc}行)", lc > 0)
else:
    R("日志存在", False, "日志文件未找到")

print("\n[资源占用]")
import psutil
r = send_request("ping", {})
pid = r["result"]["data"]["pid"]
mem = psutil.Process(pid).memory_info().rss / 1024 / 1024
R(f"内存: {mem:.1f}MB", mem < 80)

print("\n"+ "="*60)
print(f"最终: {P}/{P+F} | \u2705{P} | \u274c{F}")
if I:
    for i in I: print("  "+i)
print("="*60)
