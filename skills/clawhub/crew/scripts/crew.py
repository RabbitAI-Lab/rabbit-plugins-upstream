#!/usr/bin/env python3
"""crew: spawn agent CLIs in iTerm2 split panes (one tmux session each),
let them message each other, and save / restore the whole group.

State lives in <project>/.crew.json. Standard library only.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
import time
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
PANE = os.path.join(HERE, "pane.zsh")
STATE = ".crew.json"
ITERM = "/Applications/iTerm.app"
EFFORT_SUFFIX = re.compile(r"-(low|medium|high|xhigh|max)$")
UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
# agy families hidden from the `models` menu (still spawnable by explicit --model).
AGY_MENU_SKIP = {"gemini-4-argon"}
CLAUDE_MODELS = [("fable", "Claude Fable（最新）"), ("opus", "Claude Opus（最新）")]
CLAUDE_EFFORTS = ["low", "medium", "high", "xhigh", "max"]


def die(msg):
    print(json.dumps({"ok": False, "error": msg}, ensure_ascii=False, indent=2))
    sys.exit(1)


def done(**kw):
    print(json.dumps({"ok": True, **kw}, ensure_ascii=False, indent=2))


def run(*argv, stdin=None):
    r = subprocess.run(argv, capture_output=True, text=True, input=stdin)
    return r.returncode, r.stdout.strip()


def tmux(*argv, stdin=None):
    return run("tmux", *argv, stdin=stdin)


# ---------- state ----------

def find_dir(start):
    """Nearest ancestor holding .crew.json, else `start` itself."""
    d = os.path.abspath(start)
    while True:
        if os.path.exists(os.path.join(d, STATE)):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return os.path.abspath(start)
        d = parent


def load(d):
    p = os.path.join(d, STATE)
    if not os.path.exists(p):
        return None
    with open(p) as f:
        return json.load(f)


def store(d, state):
    p = os.path.join(d, STATE)
    with open(p + ".tmp", "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(p + ".tmp", p)


def group_name(d):
    g = re.sub(r"[^a-z0-9]+", "-", os.path.basename(d).lower()).strip("-")
    return g or "crew"


def member(state, name):
    for m in state["members"]:
        if m["name"] == name:
            return m
    return None


# ---------- tmux ----------

def alive(session):
    return tmux("has-session", "-t", "=" + session)[0] == 0


def client_tty(session):
    rc, out = tmux("list-clients", "-t", "=" + session, "-F", "#{client_tty}")
    return out.splitlines()[0] if rc == 0 and out else None


def capture(session, lines=0):
    argv = ["capture-pane", "-p", "-t", "=" + session + ":"]
    if lines:
        argv += ["-S", str(-lines)]
    return tmux(*argv)


def keys(session, *k):
    tmux("send-keys", "-t", "=" + session + ":", *k)


def send_text(session, text):
    """Type text into the agent's prompt, then submit. The pause lets the TUI
    finish taking the text in before Enter arrives."""
    target = "=" + session + ":"
    if "\n" in text:
        tmux("load-buffer", "-b", "crew-msg", "-", stdin=text)
        tmux("paste-buffer", "-p", "-d", "-b", "crew-msg", "-t", target)
    else:
        tmux("send-keys", "-t", target, "-l", text)
    time.sleep(0.6)
    tmux("send-keys", "-t", target, "Enter")


def wait_ready(session, timeout=60):
    """Wait until the agent's screen settles; accept a trust-folder dialog."""
    t0, prev, stable, presses = time.time(), None, 0, 0
    while time.time() - t0 < timeout:
        time.sleep(1)
        rc, cur = capture(session)
        if rc != 0:
            return "exited"
        if re.search(r"trust (this folder|the contents|this directory|the files)", cur, re.I):
            chosen = [l for l in cur.splitlines()
                      if re.match(r"\s*[❯>›]\s*\S", l) and re.search(r"\b(Yes|No)\b", l)]
            if presses >= 4:
                return "trust_prompt"
            keys(session, "Enter" if chosen and "Yes" in chosen[-1] else "Down")
            presses += 1
            prev, stable = None, 0
            continue
        if cur.strip() and cur == prev:
            stable += 1
            if stable >= 2:
                return "ready"
        else:
            stable = 0
        prev = cur
    return "timeout"


# ---------- who is calling ----------

def caller(state, group):
    """(member name, tmux session or None, tty or None) of the calling agent."""
    pane = os.environ.get("TMUX_PANE")
    if os.environ.get("TMUX") and pane:
        rc, sess = tmux("display-message", "-p", "-t", pane, "#{session_name}")
        if rc == 0 and sess:
            for m in (state or {}).get("members", []):
                if m["session"] == sess:
                    return m["name"], sess, client_tty(sess)
            return "main", sess, client_tty(sess)
    pid = os.getpid()
    while pid > 1:
        rc, out = run("ps", "-o", "ppid=,tty=", "-p", str(pid))
        if rc != 0 or not out:
            break
        ppid, tty = out.split()[:2]
        if tty not in ("??", "-"):
            return "main", None, "/dev/" + tty
        pid = int(ppid)
    return "main", None, None


# ---------- iTerm2 ----------

SPLIT = '''
on run argv
  set {fromTTY, dirn, cmd} to argv
  tell application "%s"
    repeat with w in windows
      repeat with t in tabs of w
        repeat with s in sessions of t
          if (tty of s) is fromTTY then
            if dirn is "v" then
              tell s to set n to (split vertically with default profile command cmd)
            else
              tell s to set n to (split horizontally with default profile command cmd)
            end if
            set newTTY to tty of n
            tell s to select
            return newTTY
          end if
        end repeat
      end repeat
    end repeat
  end tell
  return "NOTFOUND"
end run
''' % ITERM

WINDOW = '''
on run argv
  tell application "%s"
    activate
    set w to (create window with default profile command (item 1 of argv))
    set zoomed of w to true
    return tty of current session of w
  end tell
end run
''' % ITERM

FOCUS = '''
on run argv
  tell application "%s"
    repeat with w in windows
      repeat with t in tabs of w
        repeat with s in sessions of t
          if (tty of s) is (item 1 of argv) then
            activate
            select w
            select t
            tell s to select
            return "OK"
          end if
        end repeat
      end repeat
    end repeat
  end tell
  return "NOTFOUND"
end run
''' % ITERM


def osa(script, *argv):
    r = subprocess.run(["/usr/bin/osascript", "-", *argv], input=script,
                       capture_output=True, text=True)
    if r.returncode != 0:
        die("iTerm2 AppleScript 失败：" + r.stderr.strip())
    return r.stdout.strip()


def dq(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def pane_command(session, d, argv):
    return " ".join(["/bin/zsh", dq(PANE), dq(session), dq(d)] + [dq(a) for a in argv])


# ---------- agents ----------

def agent_argv(m, resume):
    sid, model, effort = m.get("session_id"), m.get("model"), m.get("effort")
    a = m["agent"]
    if a == "claude":
        argv = ["claude"]
        if resume and sid:
            argv += ["--resume", sid]
        elif sid:
            argv += ["--session-id", sid]
        if model:
            argv += ["--model", model]
        if effort:
            argv += ["--effort", effort]
        return argv
    if a == "codex":
        argv = ["codex"] + (["resume", sid] if resume and sid else [])
        if model:
            argv += ["-m", model]
        if effort:
            argv += ["-c", "model_reasoning_effort=" + effort]
        if not m.get("sandbox"):
            argv += ["-s", "danger-full-access", "-a", "never"]
        return argv
    if a == "agy":
        argv = ["agy"] + (["--conversation", sid] if resume and sid else [])
        if model:
            # agy model ids carry the effort as a suffix: gemini-4-neon-high
            argv += ["--model", model + "-" + effort if effort else model]
        if effort:
            argv += ["--effort", effort]
        return argv
    die("未知 agent：" + a)


def agy_catalog():
    """{family: {"label":..., "efforts":[...]}} in the CLI's own order."""
    rc, out = run("agy", "models")
    fams = {}
    for line in out.splitlines():
        if "\t" not in line:
            continue
        mid, label = line.split("\t", 1)
        hit = EFFORT_SUFFIX.search(mid)
        if not hit:
            continue
        fam = fams.setdefault(mid[:hit.start()],
                              {"label": re.sub(r"\s*\(.*\)$", "", label), "efforts": []})
        fam["efforts"].append(hit.group(1))
    return fams


def codex_catalog():
    rc, out = run("codex", "debug", "models")
    try:
        models = json.loads(out)["models"]
    except Exception:
        try:
            with open(os.path.expanduser("~/.codex/models_cache.json")) as f:
                models = json.load(f)["models"]
        except Exception:
            return []
    models = [x for x in models if x.get("visibility") == "list"]
    return sorted(models, key=lambda x: x.get("priority", 999))


def live_session_id(m):
    """Session id the agent in this pane is using right now (None if unknown)."""
    rc, out = tmux("list-panes", "-t", "=" + m["session"], "-F", "#{pane_pid}")
    if rc != 0 or not out:
        return None
    pid = out.splitlines()[0]
    pids = [pid] + run("pgrep", "-P", pid)[1].split()
    if m["agent"] == "claude":
        for p in pids:
            try:
                with open(os.path.expanduser("~/.claude/sessions/%s.json" % p)) as f:
                    return json.load(f)["sessionId"]
            except Exception:
                continue
        return None
    pat = {"codex": r"/rollout-[^/]*-(%s)\.jsonl$" % UUID,
           "agy": r"/conversations/(%s)\.db$" % UUID}[m["agent"]]
    for p in pids:
        rc, out = run("lsof", "-p", p, "-Fn")
        for line in out.splitlines():
            hit = re.search(pat, line)
            if hit:
                return hit.group(1)
    return None


def claude_session_running(sid):
    """pid of a live claude process on this session id, else None."""
    for p in glob.glob(os.path.expanduser("~/.claude/sessions/*.json")):
        try:
            with open(p) as f:
                d = json.load(f)
            if d.get("sessionId") == sid:
                os.kill(int(d["pid"]), 0)
                return int(d["pid"])
        except Exception:
            continue
    return None


# ---------- commands ----------

def cmd_models(args):
    rows = []
    for x in codex_catalog()[:2]:
        rows.append({"agent": "codex", "model": x["slug"], "label": x["display_name"],
                     "efforts": [e["effort"] for e in x.get("supported_reasoning_levels", [])]})
    agy = [(f, i) for f, i in agy_catalog().items() if f not in AGY_MENU_SKIP]
    for fam, info in agy[:2]:
        rows.append({"agent": "agy", "model": fam, "label": info["label"],
                     "efforts": info["efforts"]})
    for mid, label in CLAUDE_MODELS:
        rows.append({"agent": "claude", "model": mid, "label": label,
                     "efforts": CLAUDE_EFFORTS})
    for i, r in enumerate(rows, 1):
        r["n"] = i
    done(options=rows)


def intro_text(state, m, main_reachable):
    others = "、".join("%s(%s)" % (x["name"], x["agent"])
                       for x in state["members"] if x["name"] != m["name"])
    t = ("[crew] 你是协作组「%s」的 agent，名称 %s。组员：%s。"
         % (state["group"], m["name"], others))
    if m["agent"] == "codex" and m.get("sandbox"):
        t += "你运行在沙箱内，无法主动给组员发消息；直接在本窗格回答，组员会来读取。"
    else:
        t += ("给组员发消息请运行：python3 %s send --to <名称> \"内容\"（自动署名）。"
              % dq(os.path.abspath(__file__)))
        if not main_reachable:
            t += "main 目前不在 tmux 中，收不到消息，它会主动读取你的窗格。"
    t += "以 [from 名称] 开头的输入来自组员。现在只需回复：%s 就绪。" % m["name"]
    return t


def cmd_spawn(args):
    d = find_dir(args.dir)
    state = load(d)
    group = state["group"] if state else group_name(d)
    who, who_sess, who_tty = caller(state, group)

    if not state:
        if not os.environ.get("CLAUDE_CODE_SESSION_ID"):
            die("目前只支持由 Claude Code 主会话建组（未找到 CLAUDE_CODE_SESSION_ID）。")
        state = {"group": group, "members": [{
            "name": "main", "agent": "claude",
            "model": args.main_model, "effort": os.environ.get("CLAUDE_EFFORT"),
            "session_id": os.environ["CLAUDE_CODE_SESSION_ID"],
            "session": who_sess or group + "-main", "split": None}]}
    elif who == "main" and os.environ.get("CLAUDE_CODE_SESSION_ID"):
        main = member(state, "main")
        main["session_id"] = os.environ["CLAUDE_CODE_SESSION_ID"]
        if args.main_model:
            main["model"] = args.main_model

    name = args.name
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
        die("名称只能用小写字母、数字和连字符：" + name)
    if member(state, name):
        die("组里已有名为 %s 的 agent。" % name)
    session = group + "-" + name
    if alive(session):
        die("tmux 会话 %s 已存在（不在本组记录里）。先确认它是什么，再 tmux kill-session -t %s。"
            % (session, session))

    model, effort = args.model, args.effort
    if args.agent == "agy":
        hit = EFFORT_SUFFIX.search(model)
        if hit:
            model = model[:hit.start()]
        fams = agy_catalog()
        if model not in fams:
            die("agy 没有模型 %s。可选：%s" % (model, "、".join(fams)))
        if effort not in fams[model]["efforts"]:
            die("%s 不支持 effort %s。可选：%s" % (model, effort, "、".join(fams[model]["efforts"])))

    # default layout: 1st agent right of main, 2nd under the 1st, 3rd under main,
    # later ones to the right of earlier agents
    agents = [x for x in state["members"] if x["name"] != "main"]
    k = len(agents) + 1
    if args.split_from:
        src, direction = args.split_from, args.split or "v"
    elif k == 1:
        src, direction = "main", "v"
    elif k == 2:
        src, direction = agents[0]["name"], "h"
    elif k == 3:
        src, direction = "main", "h"
    else:
        src, direction = agents[k - 4]["name"], "v"
    src_m = member(state, src)
    if not src_m:
        die("找不到用来分屏的成员：" + src)
    src_tty = client_tty(src_m["session"]) or (who_tty if src == who else None)
    if not src_tty:
        die("成员 %s 的窗格当前不可见，无法从它分屏。可用 --from 指定其他成员。" % src)

    m = {"name": name, "agent": args.agent, "model": model, "effort": effort,
         "session_id": str(uuid.uuid4()) if args.agent == "claude" else None,
         "session": session, "split": {"from": src, "dir": direction}}
    if args.agent == "codex":
        m["sandbox"] = args.sandbox
    argv = agent_argv(m, resume=False)
    tty = osa(SPLIT, src_tty, direction, pane_command(session, d, argv))
    if tty == "NOTFOUND":
        die("在 iTerm2 里找不到 tty 为 %s 的窗格。" % src_tty)

    for _ in range(20):
        if alive(session):
            break
        time.sleep(0.5)
    else:
        die("窗格已打开但 tmux 会话没有起来（命令可能立即退出）。手动运行查看报错：%s"
            % " ".join(argv))

    state["members"].append(m)
    store(d, state)
    status = wait_ready(session)
    if status == "ready":
        main_sess = member(state, "main")["session"]
        send_text(session, intro_text(state, m, alive(main_sess)))
        for _ in range(30):
            time.sleep(1)
            sid = live_session_id(m)
            if sid:
                m["session_id"] = sid
                break
        store(d, state)
    done(name=name, session=session, tty=tty, status=status, command=" ".join(argv),
         session_id=m["session_id"], state_file=os.path.join(d, STATE),
         note=None if status == "ready" else "agent 未就绪：用 read 查看窗格内容并处理。")


def need_state(args):
    d = find_dir(args.dir)
    state = load(d)
    if not state:
        die("%s 及其上级目录里没有 %s。先 spawn 一个 agent。" % (os.path.abspath(args.dir), STATE))
    return d, state


def cmd_send(args):
    d, state = need_state(args)
    who = caller(state, state["group"])[0]
    m = member(state, args.to)
    if not m:
        die("没有成员 %s。现有：%s" % (args.to, "、".join(x["name"] for x in state["members"])))
    if m["name"] == who:
        die("不能给自己发消息。")
    if not alive(m["session"]):
        die("%s 不在 tmux 中（会话 %s 不存在），收不到消息。" % (m["name"], m["session"])
            + ("main 要在恢复（restore）之后才进 tmux。" if m["name"] == "main" else ""))
    send_text(m["session"], "[from %s] %s" % (who, args.message))
    done(sent_to=m["name"], sender=who)


def cmd_read(args):
    d, state = need_state(args)
    m = member(state, args.name)
    if not m:
        die("没有成员 " + args.name)
    rc, out = capture(m["session"], args.lines)
    if rc != 0:
        die("%s 不在 tmux 中，无法读取。" % m["name"])
    print("\n".join(l for l in out.splitlines() if l.strip()))


def refresh_ids(state, who):
    changes = []
    for m in state["members"]:
        new = None
        if alive(m["session"]):
            new = live_session_id(m)
        elif m["name"] == "main" and who == "main":
            new = os.environ.get("CLAUDE_CODE_SESSION_ID")
        if new and new != m.get("session_id"):
            changes.append({"name": m["name"], "old": m.get("session_id"), "new": new})
            m["session_id"] = new
    return changes


def cmd_status(args):
    d, state = need_state(args)
    rows = []
    for m in state["members"]:
        up = alive(m["session"])
        rows.append({"name": m["name"], "agent": m["agent"], "model": m.get("model"),
                     "effort": m.get("effort"), "session": m["session"], "in_tmux": up,
                     "tty": client_tty(m["session"]) if up else None,
                     "saved_session_id": m.get("session_id"),
                     "live_session_id": live_session_id(m) if up else None})
    done(group=state["group"], dir=d, members=rows)


def cmd_save(args):
    d, state = need_state(args)
    who = caller(state, state["group"])[0]
    if who == "main" and args.main_model:
        member(state, "main")["model"] = args.main_model
    changes = refresh_ids(state, who)
    store(d, state)
    launcher = os.path.join(d, state["group"] + "-crew.command")
    with open(launcher, "w") as f:
        f.write('''#!/bin/zsh
# 双击恢复「%s」agent 组的 iTerm2 窗口。成员、模型、effort、会话 ID 记在同目录的 %s。
emulate -LR zsh
path+=("$HOME/.local/bin" /opt/homebrew/bin /usr/local/bin /Library/Frameworks/Python.framework/Versions/Current/bin)
exec python3 %s restore --dir "${0:A:h}"
''' % (state["group"], STATE, dq(os.path.abspath(__file__))))
    os.chmod(launcher, 0o755)
    missing = [m["name"] for m in state["members"] if not m.get("session_id")]
    done(state_file=os.path.join(d, STATE), launcher=launcher, updated=changes,
         members=[{k: m.get(k) for k in ("name", "agent", "model", "effort", "session_id")}
                  for m in state["members"]],
         missing_session_id=missing,
         note="没有会话 ID 的成员恢复时会开新对话。" if missing else None)


def cmd_restore(args):
    d = os.path.abspath(args.dir)
    state = load(d)
    if not state:
        die("%s 里没有 %s。" % (d, STATE))
    main = member(state, "main")

    tty = client_tty(main["session"])
    if tty and osa(FOCUS, tty) == "OK":
        done(action="focused", note="该组的窗口已打开，已切换过去。")
        return
    if main["agent"] == "claude" and main.get("session_id") and not alive(main["session"]):
        pid = claude_session_running(main["session_id"])
        if pid and not args.force:
            die("main 的对话仍在另一个不在 tmux 里的 claude 进程中运行（pid %d）。"
                "先退出那个窗口，再恢复；否则同一对话会被两个进程同时写入。" % pid)

    opened = []
    for m in state["members"]:
        cmd = pane_command(m["session"], d, agent_argv(m, resume=True))
        if m["name"] == "main":
            osa(WINDOW, cmd)
        else:
            src = member(state, (m.get("split") or {}).get("from", "main")) or main
            src_tty = client_tty(src["session"]) or client_tty(main["session"])
            if not src_tty or osa(SPLIT, src_tty, (m.get("split") or {}).get("dir", "v"), cmd) == "NOTFOUND":
                opened.append({"name": m["name"], "ok": False})
                continue
        for _ in range(30):
            if client_tty(m["session"]):
                break
            time.sleep(0.5)
        opened.append({"name": m["name"], "ok": bool(client_tty(m["session"])),
                       "resumed": bool(m.get("session_id"))})
    tty = client_tty(main["session"])
    if tty:
        osa(FOCUS, tty)
    done(action="restored", members=opened)


def main():
    p = argparse.ArgumentParser(prog="crew")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("models", help="top 2 models of codex / agy / claude (agy skips AGY_MENU_SKIP)")
    s.set_defaults(fn=cmd_models)

    s = sub.add_parser("spawn", help="open a new agent in a split pane")
    s.add_argument("--name", required=True)
    s.add_argument("--agent", required=True, choices=["claude", "codex", "agy"])
    s.add_argument("--model", required=True)
    s.add_argument("--effort", default="high")
    s.add_argument("--sandbox", action="store_true",
                   help="codex only: keep the default sandbox (then it cannot reach tmux)")
    s.add_argument("--from", dest="split_from", help="member whose pane to split")
    s.add_argument("--split", choices=["v", "h"])
    s.add_argument("--main-model", help="model id of the calling main agent")
    s.add_argument("--dir", default=os.getcwd())
    s.set_defaults(fn=cmd_spawn)

    s = sub.add_parser("send", help="message another member")
    s.add_argument("--to", required=True)
    s.add_argument("message")
    s.add_argument("--dir", default=os.getcwd())
    s.set_defaults(fn=cmd_send)

    s = sub.add_parser("read", help="print a member's pane")
    s.add_argument("--name", required=True)
    s.add_argument("--lines", type=int, default=80)
    s.add_argument("--dir", default=os.getcwd())
    s.set_defaults(fn=cmd_read)

    s = sub.add_parser("status")
    s.add_argument("--dir", default=os.getcwd())
    s.set_defaults(fn=cmd_status)

    s = sub.add_parser("save", help="refresh session ids, write the .command launcher")
    s.add_argument("--main-model")
    s.add_argument("--dir", default=os.getcwd())
    s.set_defaults(fn=cmd_save)

    s = sub.add_parser("restore", help="reopen the group's iTerm2 window")
    s.add_argument("--dir", default=os.getcwd())
    s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_restore)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
