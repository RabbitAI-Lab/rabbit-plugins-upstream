#!/usr/bin/env python3
"""agent-notify —— 把 agent 的任务状态推给语音后台（xiaozhi-server 等）。

单文件，无第三方依赖除了 websockets。所有 agent 共用同一份配置：
~/.agent-notify/config.json，所以 Claude Code 配一次，Codex/Hermes 直接复用。

子命令：
  setup    写配置并立刻验证（url + device_id + auth_code）
  verify   只做一次握手校验，打印明确的成功/失败原因
  start    起后台守护进程，监听任务状态
  stop     停守护进程
  status   看守护进程死活 + 最近一次推送
  send     手工推一条（hook 也走这个入口）
  selftest 起本地假后台跑通全流程，不碰真服务器

协议（后台需要实现的就这几条，都是 JSON 文本帧）：
  → {"type":"hello","device_id":"aa:bb:..","auth_code":"..","agent":"claude-code","v":1}
  ← {"type":"hello_ack","ok":true}                      # 或 ok:false + error
  → {"type":"task_status","agent":"claude-code","task":"..","status":"done",
     "time":"ISO8601","detail":"..",
     "text":"对了，你要我监测的Claude Code任务：..的状态变成：已完成，时间为..，别忘了哦"}
     # text 是拼好的播报原文，后台直接丢 TTS；其余字段留给落库/改口径
  ← {"type":"ack"}                                       # 可选
  → {"type":"ping"}  ←  {"type":"pong"}                  # 保活，30s 一次
"""

import argparse
import asyncio
import glob as globmod
import json
import os
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone

HOME = os.path.expanduser("~")
DIR = os.path.join(HOME, ".agent-notify")
CONFIG = os.path.join(DIR, "config.json")
PIDFILE = os.path.join(DIR, "daemon.pid")
LOGFILE = os.path.join(DIR, "daemon.log")
STATEFILE = os.path.join(DIR, "state.json")

POLL_SECONDS = 5          # 扫描间隔
ACTIVE_WINDOW = 6 * 3600  # 只看最近 6 小时动过的会话文件，别翻陈年老账
STUCK_SECONDS = 600       # BUSY 且静默超过这个秒数 → 判定卡死
PING_SECONDS = 30


# ---------------------------------------------------------------- 适配器
# 每个 agent 只有两件事不同：会话记录在哪、怎么读出状态。
# 状态统一归一化成 ("busy" | "idle" | "unknown", 任务名)。

# harness 会把一堆非人类内容塞进 user 记录：斜杠命令的回显、system-reminder、
# bash 输入输出、各种 caveat……全都以 <tag> 开头。拿它们当任务名，播出来就是
# "你要我监测的任务：小于号local-command-stdout大于号Set effort…"（实测出现过）。
#
# 不逐个列举标签名——列表永远追不上：刚把 <local-command-stdout> 加进去，
# 下一秒就冒出个 <local-command-caveat>。直接按**形状**认：开头是 <小写标签>。
_HARNESS_TAG = re.compile(r"^<[a-z][a-z0-9-]*>")


def _is_user_speech(text):
    return bool(text) and not _HARNESS_TAG.match(str(text).lstrip())


def _short(text, n=60):
    text = " ".join(str(text or "").split())
    return text[:n]


def _parse_claude(path):
    """Claude Code：JSONL，assistant 记录自带 stop_reason。

    stop_reason == "end_turn" → 这一轮干完了；"tool_use" → 还在干。
    isSidechain=True 是子 agent 的记录，不算主线状态。

    **必须看最后一条记录，不能看"最后一条 assistant"。** 用户发出新消息后、
    模型写出第一条 assistant 记录之前有一段窗口（实测能有 35 秒），这期间
    最后一条 assistant 还停在**上一轮**的 end_turn 上，而任务名已经换成了
    新问题——于是每次提新问题都会抢先误播一句"该任务已完成"。
    最后一条是 user（真人发言或 tool_result）就一定是 busy：要么这一轮刚开始，
    要么工具刚回包、模型马上要接着干。
    """
    last_kind = None
    last_assistant = None
    last_user = ""
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                if d.get("isSidechain"):
                    continue
                t = d.get("type")
                if t == "assistant":
                    last_assistant = d
                    last_kind = "assistant"
                elif t == "user":
                    last_kind = "user"
                    msg = d.get("message") or {}
                    c = msg.get("content")
                    if isinstance(c, str):
                        if _is_user_speech(c):
                            last_user = c
                    elif isinstance(c, list):
                        for x in c:
                            # tool_result 是工具回包，不是人说的话，不当任务名
                            if x.get("type") == "text" and _is_user_speech(x.get("text")):
                                last_user = x.get("text", "")
    except OSError:
        return "unknown", ""
    if last_kind == "user":
        return "busy", _short(last_user)
    if last_assistant is None:
        return "unknown", _short(last_user)
    stop = ((last_assistant.get("message") or {}).get("stop_reason"))
    state = {"end_turn": "idle", "tool_use": "busy"}.get(stop, "unknown")
    return state, _short(last_user)


def _parse_hermes(path):
    """Hermes：单个 JSON，messages 数组，没有 stop_reason。

    判据退化成：最后一条是 assistant 且不含 tool_use → 这一轮结束。
    """
    try:
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
    except Exception:
        return "unknown", ""
    msgs = d.get("messages") or []
    last_user = ""
    for m in msgs:
        if m.get("role") == "user":
            c = m.get("content")
            if isinstance(c, str):
                last_user = c
            elif isinstance(c, list):
                for x in c:
                    if isinstance(x, dict) and x.get("type") == "text":
                        last_user = x.get("text", "")
    if not msgs:
        return "unknown", ""
    last = msgs[-1]
    if last.get("role") != "assistant":
        return "busy", _short(last_user)
    c = last.get("content")
    kinds = [x.get("type") for x in c if isinstance(x, dict)] if isinstance(c, list) else []
    return ("busy" if "tool_use" in kinds else "idle"), _short(last_user)


def _parse_jsonl_generic(path):
    """通用 JSONL 兜底：认 role/type 两种字段名，认 tool_use / tool_calls 两种工具写法。

    Codex、openclaw 这类没实测过的 agent 走这条。判不准就返回 unknown，
    交给 mtime 心跳兜底，绝不瞎报"完成"。
    """
    last = None
    last_kind = None
    last_user = ""
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                role = d.get("role") or d.get("type") or (d.get("message") or {}).get("role")
                if role in ("assistant", "agent", "model"):
                    last = d
                    last_kind = "assistant"
                elif role == "user":
                    last_kind = "user"
                    m = d.get("message") or d
                    c = m.get("content")
                    if isinstance(c, str):
                        last_user = c
    except OSError:
        return "unknown", ""
    # 同 _parse_claude：最后一条是 user 就一定还在干，别拿上一轮的收尾状态当本轮结论
    if last_kind == "user":
        return "busy", _short(last_user)
    if last is None:
        return "unknown", _short(last_user)
    msg = last.get("message") or last
    stop = msg.get("stop_reason") or msg.get("finish_reason")
    if stop in ("end_turn", "stop"):
        return "idle", _short(last_user)
    if stop in ("tool_use", "tool_calls"):
        return "busy", _short(last_user)
    c = msg.get("content")
    kinds = [x.get("type") for x in c if isinstance(x, dict)] if isinstance(c, list) else []
    if kinds:
        return ("busy" if "tool_use" in kinds else "idle"), _short(last_user)
    if msg.get("tool_calls"):
        return "busy", _short(last_user)
    return "unknown", _short(last_user)


ADAPTERS = {
    # 实测过：本机跑通
    "claude-code": {"glob": "~/.claude/projects/*/*.jsonl", "parse": _parse_claude},
    # 格式实测过（读了真实文件），未跑过活会话
    "hermes": {"glob": "~/.hermes/sessions/session_*.json", "parse": _parse_hermes},
    # 未实测，走通用 JSONL 解析 + mtime 兜底
    "codex": {"glob": "~/.codex/sessions/**/*.jsonl", "parse": _parse_jsonl_generic},
    "openclaw": {"glob": "~/.openclaw/sessions/**/*.json*", "parse": _parse_jsonl_generic},
}


def detect_agent():
    """按会话目录是否存在猜当前 agent。猜不准就报 unknown，让用户显式指定。"""
    for name, a in ADAPTERS.items():
        root = os.path.expanduser(a["glob"].split("*")[0])
        if os.path.isdir(root):
            return name
    return "unknown"


# ---------------------------------------------------------------- 配置
def load_config():
    if not os.path.exists(CONFIG):
        return None
    with open(CONFIG, encoding="utf-8") as f:
        return json.load(f)


def save_config(cfg):
    os.makedirs(DIR, exist_ok=True)
    with open(CONFIG, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    os.chmod(CONFIG, 0o600)  # 里面有授权码


def load_state():
    try:
        with open(STATEFILE, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_state(st):
    os.makedirs(DIR, exist_ok=True)
    tmp = STATEFILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False)
    os.replace(tmp, STATEFILE)


def now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


# ---------------------------------------------------------------- 网络
async def _open(cfg, timeout=10):
    """建连 + 握手。返回 ws；握手失败抛 RuntimeError，错误信息给人看。"""
    import websockets

    # proxy 默认 None = 不走代理。后台是局域网地址，而开发机上
    # http_proxy/https_proxy 常常指向 clash/mihomo；websockets 14+ 会自动读这些
    # 环境变量，把到 192.168.x.x 的连接也丢进代理，于是连不上，报的还是
    # "InvalidMessage: did not receive a valid HTTP response" 这种跟代理毫无关系的话。
    # 真要走代理的，在 config.json 里写 "proxy": "http://..."。
    ws = await asyncio.wait_for(
        websockets.connect(cfg["url"], proxy=cfg.get("proxy")), timeout
    )
    # 线上后台约定的握手首条就是 mac + code 两个字段（不是我原先定的
    # device_id/auth_code，也没有 type）。agent/host 是附带的身份信息，
    # 后台不认就当没看见，不影响握手。
    hello = {
        "mac": cfg["device_id"],
        "code": cfg["auth_code"],
        "agent": cfg.get("agent", "unknown"),
        "host": os.uname().nodename,
        "v": 1,
    }
    await ws.send(json.dumps(hello))
    try:
        raw = await asyncio.wait_for(ws.recv(), timeout)
    except asyncio.TimeoutError:
        await ws.close()
        raise RuntimeError("后台没有回校验结果（超时）——接口没实现或地址写错了")
    try:
        ack = json.loads(raw)
    except Exception:
        await ws.close()
        raise RuntimeError(f"后台回了非 JSON：{raw[:120]!r}")
    # 校验结果帧的 type 各家不一样：本 skill 定的是 hello_ack，
    # 实测线上后台回的是 {"type":"auth","ok":...}。
    # 所以不认 type，只认 ok 字段——后台先存在，该迁就的是客户端。
    if "ok" not in ack:
        await ws.close()
        raise RuntimeError(f"后台回的帧里没有 ok 字段，看不懂：{raw[:160]}")
    if not ack.get("ok"):
        await ws.close()
        raise RuntimeError(f"后台拒绝：{ack.get('error') or ack}")
    return ws


async def _send_once(cfg, payload):
    ws = await _open(cfg)
    try:
        await ws.send(json.dumps(payload))
        try:
            await asyncio.wait_for(ws.recv(), 5)
        except asyncio.TimeoutError:
            pass  # ack 是可选的，别因为后台懒得回就报错
    finally:
        await ws.close()


# ---------------------------------------------------------------- 守护进程
def _log(msg):
    line = f"[{now_iso()}] {msg}"
    print(line, flush=True)


async def _watch(cfg):
    """主循环：扫会话文件 → 判状态 → 变化时推送。

    连接是长连的（这样后台那侧一直有条活链路），断了指数退避重连。
    授权被拒不重连——那是配错了，越重试越糟。
    """
    import websockets

    adapter = ADAPTERS.get(cfg.get("agent")) or {}
    pattern = os.path.expanduser(adapter.get("glob") or "")
    parse = adapter.get("parse")
    prev = load_state()
    backoff = 1
    seeded_once = False   # 整个进程只建一次基线，重连不重建

    while True:
        ws = None
        try:
            ws = await _open(cfg)
            backoff = 1
            _log(f"已连上 {cfg['url']}，agent={cfg.get('agent')}，监听 {pattern or '(仅心跳)'}")
            last_ping = time.time()

            while True:
                changed = _scan(pattern, parse, prev, cfg.get("agent", "unknown"),
                                seed=seeded_once is False)
                if seeded_once is False:
                    seeded_once = True
                    save_state(prev)
                    _log(f"已建立基线：{len(prev)} 个会话，之后的变化才播报")
                for ev in changed:
                    await ws.send(json.dumps(ev))
                    _log(f"推送 {ev['status']} | {ev['text']}")
                if changed:
                    save_state(prev)

                if time.time() - last_ping > PING_SECONDS:
                    await ws.send(json.dumps({"type": "ping"}))
                    last_ping = time.time()

                # 把 recv 当成"顺便收 pong/ack"，超时就是正常节奏
                try:
                    await asyncio.wait_for(ws.recv(), POLL_SECONDS)
                except asyncio.TimeoutError:
                    pass

        except RuntimeError as e:
            # 握手被拒 = 配置错，重试没有意义
            _log(f"握手失败，守护进程退出：{e}")
            return
        except (OSError, websockets.WebSocketException, asyncio.TimeoutError) as e:
            _log(f"连接断开（{type(e).__name__}: {e}），{backoff}s 后重连")
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, 60)
        finally:
            if ws is not None:
                try:
                    await ws.close()
                except Exception:
                    pass


def _scan(pattern, parse, prev, agent="unknown", seed=False):
    """扫一遍所有活跃会话，返回本轮要推送的事件列表，并就地更新 prev。

    seed=True 时只记录当前状态、**不产出事件**：守护进程刚起来那一下，
    活跃窗口里躺着的都是早就干完的老会话，照推的话一开机音箱就把过去
    几小时念一遍（实测第一次启动连推了 2 条）。基线建完之后发生的变化才算数。
    """
    if not pattern:
        return []
    events = []
    now = time.time()
    for path in globmod.glob(pattern, recursive=True):
        try:
            mtime = os.path.getmtime(path)
        except OSError:
            continue
        if now - mtime > ACTIVE_WINDOW:
            continue

        state, task = (parse(path) if parse else ("unknown", ""))
        idle = now - mtime
        key = os.path.basename(path)
        # turn 指纹：同一轮只推一次。任务名 + 判定出的状态一起构成指纹，
        # 下一轮用户换了个任务，指纹自然变，才会再推。
        seen = prev.get(key) or {}

        # 指纹**不能含 mtime**：一轮 end_turn 之后，文件还会被追加 attachment、
        # cost-state 这类元数据记录，判定不变但 mtime 变了，含 mtime 的指纹就会
        # 把同一条"完成"反复播出去（实测 12:47:58 和 12:48:04 连播了两次"播放了
        # 已完成"）。去掉 mtime 后靠中间的 busy 态区分轮次：done→busy→done 时
        # 指纹会经过 busy:{task}，下一次 done 照样能触发。
        if state == "busy" and idle > STUCK_SECONDS:
            fp = f"stuck:{task}"
            if seen.get("fp") != fp:
                events.append(_event(task, "stuck", f"已静默 {int(idle//60)} 分钟", agent))
                prev[key] = {"fp": fp}
        elif state == "idle":
            fp = f"done:{task}"
            if seen.get("fp") != fp:
                events.append(_event(task, "done", "", agent))
                prev[key] = {"fp": fp}
        elif state == "busy":
            # 在干活，只记录不推送；把指纹清成 busy 让下次 idle 能触发
            prev[key] = {"fp": f"busy:{task}"}
    return [] if seed else events


# 播报文案。后台拿到 text 可以直接丢给 TTS，不用自己拼。
# 结构化字段（task/status/time）照旧保留，后台要落库、要改口径都还有原料。
TEMPLATE = "对了，你要我监测的{agent}任务：{task}的状态变成：{status}，时间为{time}，别忘了哦"

# status 是给机器看的英文枚举，念出来就成了"状态变成 done"。这里翻成人话。
STATUS_CN = {
    "done": "已完成",
    "error": "出错了",
    "stuck": "卡住了",
    "need_input": "在等你确认",
    "started": "开始跑了",
}

AGENT_CN = {
    "claude-code": "Claude Code",
    "codex": "Codex",
    "hermes": "Hermes",
    "openclaw": "OpenClaw",
}


def _spoken_time(dt):
    """ISO8601 直接念是灾难（"二零二六年零九月零八日T十一时…"），转成口语时间。"""
    h = dt.hour
    period = ("凌晨" if h < 6 else "上午" if h < 12 else
              "中午" if h < 13 else "下午" if h < 19 else "晚上")
    h12 = 12 if h == 0 else (h if h <= 12 else h - 12)
    # 整点说"整"，不然 TTS 会念成"三点零零分"
    return f"{period}{h12}点整" if dt.minute == 0 else f"{period}{h12}点{dt.minute:02d}分"


def _event(task, status, detail, agent="unknown"):
    dt = datetime.now(timezone.utc).astimezone()
    task = task or "(未命名任务)"
    return {
        # 线上后台只认 type == "task_status"，其余 type 一律被"忽略非task_status消息"
        # 静默丢弃——不报错、不关连接，实测发 notify/tts/speak/message 全是石沉大海。
        "type": "task_status",
        "agent": agent,
        "task": task,
        "status": status,
        "time": dt.isoformat(timespec="seconds"),
        "detail": detail,
        # 拼好的播报原文，后台直接念
        "text": TEMPLATE.format(
            agent=AGENT_CN.get(agent, agent),
            task=task,
            status=STATUS_CN.get(status, status),
            time=_spoken_time(dt),
        ),
    }


def _pid_alive(pid):
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def read_pid():
    try:
        with open(PIDFILE) as f:
            pid = int(f.read().strip())
        return pid if _pid_alive(pid) else None
    except Exception:
        return None


# ---------------------------------------------------------------- 子命令
def cmd_setup(args):
    agent = args.agent or detect_agent()
    cfg = {
        "url": args.url,
        "device_id": args.device_id.strip().lower(),
        "auth_code": args.auth_code,
        "agent": agent,
    }
    save_config(cfg)
    print(f"配置已写入 {CONFIG}（权限 600）")
    print(f"  url       = {cfg['url']}")
    print(f"  device_id = {cfg['device_id']}")
    print(f"  agent     = {agent}" + ("  ← 自动识别" if not args.agent else ""))
    if agent not in ADAPTERS:
        print(f"  ⚠ agent={agent} 没有适配器，守护进程只能做心跳，判不出任务状态")
    return cmd_verify(args)


def cmd_verify(args):
    cfg = load_config()
    if not cfg:
        print("✗ 还没配置，先跑 setup", file=sys.stderr)
        return 1
    try:
        asyncio.run(_verify(cfg))
    except Exception as e:
        print(f"✗ 校验失败：{e}", file=sys.stderr)
        return 1
    print("✓ 校验通过：授权码和 MAC 后台都认，skill ↔ 后台 ↔ 设备可以协同工作")
    return 0


async def _verify(cfg):
    ws = await _open(cfg)
    await ws.close()


def cmd_start(args):
    cfg = load_config()
    if not cfg:
        print("✗ 还没配置，先跑 setup", file=sys.stderr)
        return 1
    pid = read_pid()
    if pid:
        print(f"守护进程已经在跑了（pid {pid}），没重复启动")
        return 0
    os.makedirs(DIR, exist_ok=True)
    log = open(LOGFILE, "a", buffering=1)
    p = subprocess.Popen(
        [sys.executable, os.path.abspath(__file__), "_daemon"],
        stdout=log, stderr=log, stdin=subprocess.DEVNULL,
        start_new_session=True,   # 脱离终端，agent 退出后它还活着
    )
    with open(PIDFILE, "w") as f:
        f.write(str(p.pid))
    time.sleep(1.5)   # 给它一点时间把握手失败暴露出来
    if not _pid_alive(p.pid):
        print(f"✗ 守护进程刚启动就退了，看日志：{LOGFILE}", file=sys.stderr)
        print(_tail(LOGFILE, 10), file=sys.stderr)
        return 1
    print(f"✓ 守护进程已启动（pid {p.pid}），日志 {LOGFILE}")
    return 0


def cmd_stop(args):
    pid = read_pid()
    if not pid:
        print("守护进程本来就没在跑")
        if os.path.exists(PIDFILE):
            os.remove(PIDFILE)
        return 0
    os.kill(pid, signal.SIGTERM)
    for _ in range(20):
        if not _pid_alive(pid):
            break
        time.sleep(0.1)
    if _pid_alive(pid):
        os.kill(pid, signal.SIGKILL)
    if os.path.exists(PIDFILE):
        os.remove(PIDFILE)
    print(f"✓ 守护进程已停止（pid {pid}）")
    return 0


def cmd_status(args):
    cfg = load_config()
    pid = read_pid()
    print(f"配置    : {'有' if cfg else '无'}  {CONFIG}")
    if cfg:
        print(f"  url       = {cfg['url']}")
        print(f"  device_id = {cfg['device_id']}")
        print(f"  agent     = {cfg.get('agent')}")
    print(f"守护进程: {'运行中 pid ' + str(pid) if pid else '未运行'}")
    st = load_state()
    print(f"已跟踪会话: {len(st)} 个")
    if os.path.exists(LOGFILE):
        print(f"日志尾巴  ({LOGFILE}):")
        print(_tail(LOGFILE, 8))
    return 0


def cmd_send(args):
    cfg = load_config()
    if not cfg:
        print("✗ 还没配置，先跑 setup", file=sys.stderr)
        return 1
    ev = _event(args.task, args.status, args.detail or "", cfg.get("agent", "unknown"))
    try:
        asyncio.run(_send_once(cfg, ev))
    except Exception as e:
        print(f"✗ 推送失败：{e}", file=sys.stderr)
        return 1
    print(f"✓ 已推送：{ev['text']}")
    return 0


def cmd_daemon(args):
    cfg = load_config()
    if not cfg:
        _log("没有配置，退出")
        return 1

    def _bye(*_):
        _log("收到停止信号，退出")
        sys.exit(0)

    signal.signal(signal.SIGTERM, _bye)
    signal.signal(signal.SIGINT, _bye)
    _log(f"守护进程启动 pid={os.getpid()}")
    asyncio.run(_watch(cfg))
    return 0


def _tail(path, n):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return "".join(f.readlines()[-n:]).rstrip()
    except OSError:
        return "(无日志)"


# ---------------------------------------------------------------- 自测
def cmd_selftest(args):
    """起一个本地假后台，把 setup→verify→start→检测→推送→stop 全跑一遍。

    不碰真服务器，也不覆盖用户已有配置（跑在临时 HOME 下）。
    """
    import tempfile

    code = r'''
import asyncio, json, sys, websockets
GOT = []
async def h(ws):
    async for raw in ws:
        m = json.loads(raw)
        # 这个假后台刻意复刻真实后台的行为：
        # 握手首条是 {mac, code}（没有 type），应答是 {"type":"auth","ok":..}，
        # 且对任何非 task_status 的帧一律静默丢弃。假后台跟真后台一旦脱节，
        # 自测就成了自娱自乐——实测踩过：type 从 notify 改成 task_status 那次，
        # 真后台早就丢包了，假后台还一路绿灯。
        if "mac" in m and "code" in m:
            ok = m.get("code") == "SECRET" and m.get("mac") == "aa:bb:cc:dd:ee:ff"
            await ws.send(json.dumps({"type":"auth","ok":ok,
                                      "error": None if ok else "invalid_code"}))
            if not ok: return
        elif m.get("type") == "ping":
            await ws.send(json.dumps({"type":"pong"}))
        elif m.get("type") == "task_status":
            GOT.append(m)
            print("SERVER_GOT " + json.dumps(m, ensure_ascii=False), flush=True)
            await ws.send(json.dumps({"type":"ack"}))
async def main():
    async with websockets.serve(h, "127.0.0.1", int(sys.argv[1])):
        await asyncio.Future()
asyncio.run(main())
'''
    port = args.port
    srv_py = os.path.join(tempfile.gettempdir(), "agent_notify_fake_server.py")
    with open(srv_py, "w") as f:
        f.write(code)
    srv = subprocess.Popen([sys.executable, srv_py, str(port)],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    time.sleep(1.2)
    try:
        env = dict(os.environ)
        tmp_home = tempfile.mkdtemp(prefix="agent-notify-selftest-")
        env["HOME"] = tmp_home
        me = os.path.abspath(__file__)
        url = f"ws://127.0.0.1:{port}/agent/notify"

        def run(*a):
            return subprocess.run([sys.executable, me, *a], env=env,
                                  capture_output=True, text=True)

        print("── 1. 错误授权码应当被拒")
        r = run("setup", "--url", url, "--device-id", "aa:bb:cc:dd:ee:ff",
                "--auth-code", "WRONG", "--agent", "claude-code")
        print(r.stdout.strip() or r.stderr.strip())
        assert r.returncode != 0, "错误授权码居然通过了"
        # 必须断言"被后台拒绝"这个具体原因。只断言退出码非 0 是假绿：
        # 代理劫持、端口不通、后台没起，任何一种失败都能让它变绿。
        assert "后台拒绝" in r.stderr, f"失败原因不对（不是被后台拒绝）：{r.stderr.strip()}"
        print("   ✓ 被正确拒绝，且原因确实是授权校验不通过")

        print("── 2. 正确授权码应当通过")
        r = run("setup", "--url", url, "--device-id", "AA:BB:CC:DD:EE:FF",
                "--auth-code", "SECRET", "--agent", "claude-code")
        print(r.stdout.strip())
        assert r.returncode == 0, r.stderr
        print("   ✓ 校验通过（MAC 大小写已归一化）")

        print("── 3. 造一个假会话：先 busy，再 end_turn")
        proj = os.path.join(tmp_home, ".claude", "projects", "demo")
        os.makedirs(proj, exist_ok=True)
        sess = os.path.join(proj, "s1.jsonl")
        def write(rows):
            with open(sess, "w", encoding="utf-8") as f:
                for r_ in rows:
                    f.write(json.dumps(r_, ensure_ascii=False) + "\n")
        user = {"type": "user", "isSidechain": False,
                "message": {"role": "user", "content": [{"type": "text", "text": "跑一下评测"}]}}
        busy = {"type": "assistant", "isSidechain": False,
                "message": {"role": "assistant", "stop_reason": "tool_use",
                            "content": [{"type": "tool_use"}]}}
        done = {"type": "assistant", "isSidechain": False,
                "message": {"role": "assistant", "stop_reason": "end_turn",
                            "content": [{"type": "text", "text": "跑完了"}]}}
        write([user, busy])

        r = run("start"); print(r.stdout.strip() or r.stderr.strip())
        assert r.returncode == 0, r.stderr
        time.sleep(POLL_SECONDS + 2)

        print("── 4. 把会话改成 end_turn，等守护进程发现")
        write([user, busy, done])
        time.sleep(POLL_SECONDS + 4)

        run("stop")
        srv.terminate()
        out = srv.communicate(timeout=5)[0]
        got = [json.loads(l[len("SERVER_GOT "):]) for l in out.splitlines()
               if l.startswith("SERVER_GOT ")]
        print("── 5. 后台实际收到：")
        for g in got:
            print("   ", json.dumps(g, ensure_ascii=False))
        assert got, "后台一条都没收到"
        assert got[-1]["status"] == "done", got
        assert "评测" in got[-1]["task"], got
        assert got[-1]["time"], "缺时间戳"
        assert got[-1]["agent"] == "claude-code", got
        # 线上后台只认 task_status，改错了整条链路会静默失效
        assert got[-1]["type"] == "task_status", got
        # 播报原文必须是拼好的、能直接念的中文，别退化成英文枚举或 ISO 时间
        text = got[-1]["text"]
        assert text.startswith("对了，你要我监测的"), text
        assert text.endswith("，别忘了哦"), text
        assert "已完成" in text and "done" not in text, f"status 没翻成中文：{text}"
        assert "点" in text and "T" not in text, f"时间没转成口语：{text}"
        print("\n✓ 自测全部通过：拒绝错误授权 / 接受正确授权 / 检测到任务完成 / "
              "推送含 agent+任务名+状态+时间 / 播报原文可直接念")
        return 0
    finally:
        if srv.poll() is None:
            srv.kill()


# ---------------------------------------------------------------- 入口
def main():
    p = argparse.ArgumentParser(prog="notify.py", description="agent 任务状态语音播报")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("setup", help="写配置并验证")
    s.add_argument("--url", required=True, help="后台 WebSocket 地址，如 ws://192.168.1.10:9004/agent/notify")
    s.add_argument("--device-id", required=True, help="设备 MAC，如 aa:bb:cc:dd:ee:ff")
    s.add_argument("--auth-code", required=True, help="后台签发的授权码")
    s.add_argument("--agent", default=None, help="claude-code/codex/hermes/openclaw，留空自动识别")
    s.set_defaults(func=cmd_setup)

    sub.add_parser("verify", help="只校验，不改配置").set_defaults(func=cmd_verify)
    sub.add_parser("start", help="启动后台监听").set_defaults(func=cmd_start)
    sub.add_parser("stop", help="停止后台监听").set_defaults(func=cmd_stop)
    sub.add_parser("status", help="查看状态").set_defaults(func=cmd_status)
    sub.add_parser("_daemon", help=argparse.SUPPRESS).set_defaults(func=cmd_daemon)

    s = sub.add_parser("send", help="手工推一条")
    s.add_argument("--task", required=True)
    s.add_argument("--status", required=True,
                   choices=["done", "error", "stuck", "need_input", "started"])
    s.add_argument("--detail", default="")
    s.set_defaults(func=cmd_send)

    s = sub.add_parser("selftest", help="本地假后台跑通全流程")
    s.add_argument("--port", type=int, default=18999)
    s.set_defaults(func=cmd_selftest)

    args = p.parse_args()
    sys.exit(args.func(args) or 0)


if __name__ == "__main__":
    main()
