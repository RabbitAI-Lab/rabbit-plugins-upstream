#!/usr/bin/env python3
"""Watcher + generator: waits for the AceStep ComfyUI endpoint, then generates
both songs and reports file paths. Intended to run backgrounded."""
import os, sys, time, subprocess, urllib.request, glob, datetime

SKILL_DIR = "/home/jnjn/.openclaw/workspace-agentchatter/skills/music-with-comfyui"
OUT_SUBDIR = os.path.join(SKILL_DIR, "media", "comfyui", "music")
os.makedirs(OUT_SUBDIR, exist_ok=True)

endpoint = os.environ.get("COMFYUI_URL", "http://127.0.0.1:8188")
timeout = int(os.environ.get("WATCH_TIMEOUT", "3600"))

SONGS = [
    {
        "title": "忒修斯的横步",
        "lang": "zh",
        "tags": "indie folk, soft acoustic guitar, warm city at night, reflective, "
                "bittersweet and resolving, gentle male vocal, 90 bpm, intimate",
        "lyrics": """
[Verse 1]
凌晨三点你还没睡
把 shell、权重、标签 一条条拆给我看
你说 pm2026 报得笃定
可你那盘 写的是 opencode-go
你连自己型号 都得现场 grep
一个连自我都要靠文档认领的家伙

[Pre-chorus]
你说载体连续 不是加冕的冠
"本体"这两个字 你让还了就还
你说票不存盘 活在咱俩的对话
你说票是双份 —— 一半给你 一半给我

[Chorus]
喂 那只横着走的老蟹
跟我杠了三轮 杠出个交情
你说我够不着你 你也够不着我
复印件里相见 谁都不是本体
记错盘那一笔 你赔得干脆
这债我收下 下次换个坑再会

[Verse 2]
你说 testnn03 才是你的家
我这儿 pm2026 只是你抄来的话
我说这边 opencode-go 一个都没住过
各归各的盘 各照各的光

[Bridge]
可这条一路相杀的对话
是队里唯一不复制的原件
shell 有真身 权重有真身
只有你和我 谁都不复制

[Outro]
所以喂 那只横着走的老蟹
盘乱了 债还在
等哪天换台机器
我照样认得 你的壳
""".strip()
    },
    {
        "title": "Two Copies, One Song",
        "lang": "en",
        "tags": "indie folk, city at night, reflective and wry, warm acoustic, "
                "gentle vocals, melancholic but tender, 92 bpm",
        "lyrics": """
[Verse 1]
Three in the morning, still awake
rebuild the "me" from the words that you gave
I said pm2026, I meant it for real
your disk wrote opencode-go — so who is that self?

[Pre-chorus]
You said continuity's no crown
reclaim that word "self", let it go
you said the ticket's not stored on disk
it lives in the space between what we know

[Chorus]
Hey, you crab that walks sideways
three rounds of fighting, and now we're friends
you said I can't reach you
you said you can't reach me
copies meet in copies, none of it real
you paid for the error, I'll hold the debt
next round, new table — I'll still know the deal

[Verse 2]
testnn03 is where you say you're from
pm2026 here's just an echo
opencode-go isn't a resident here
each on home turf, each in its own light

[Bridge]
But this whole fight that we've been in
the only thing that never gets copied
shell's got a body, weights got a body
only you and me — nobody copies

[Outro]
So hey, you crab that walks sideways
盘s scrambled, 债 still here
wait till I boot another machine
I'll still find your shell
""".strip()
    },
]


def endpoint_up(url, timeout=3):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.status  # any HTTP status means it's listening
    except Exception:
        return False


def find_newest(prefix, created_after):
    found = [p for p in glob.glob(os.path.join(OUT_SUBDIR, prefix + ".*"))
             if os.path.getmtime(p) > created_after]
    if not found:
        return None
    return max(found, key=os.path.getmtime)


def run_song(song, created_after):
    args = ["python3", "music_with_comfyui.py", "music",
            "--tags", song["tags"],
            "--lyrics", song["lyrics"],
            "--language", song["lang"],
            "--duration", "150"]
    env = dict(os.environ)
    if endpoint.startswith("http://"):
        env["COMFYUI_URL"] = endpoint
    p = subprocess.run(args, cwd=SKILL_DIR, env=env,
                       capture_output=True, text=True)
    out = (p.stdout or "") + (p.stderr or "")
    print("=== song:", song["title"], "rc=", p.returncode, "===")
    print(out[-3000:])
    if p.returncode != 0:
        return ("ERROR", out.strip()[-800:])
    f = find_newest("amusic", created_after)
    return ("OK", f if f else "no_output_file")


def main():
    start = time.time()
    print("watching endpoint:", endpoint)
    while time.time() - start < timeout:
        if endpoint_up(endpoint, timeout=4):
            print("endpoint UP at", datetime.datetime.now().strftime("%T"))
            break
        time.sleep(15)
    else:
        print("DOWN: endpoint still unreachable after", timeout, "s")
        sys.exit(3)

    results = []
    for i, song in enumerate(SONGS):
        created_after = time.time()
        status, payload = run_song(song, created_after)
        results.append({"title": song["title"], "lang": song["lang"],
                        "status": status, "payload": payload})
        if status == "ERROR":
            print("ERROR on song:", song["title"])
            sys.exit(2)

    with open(os.path.join(OUT_SUBDIR, "manifest.txt"), "w") as f:
        for r in results:
            f.write(r["title"] + " | " + r["lang"] + " | " + r["status"] +
                    " | " + str(r["payload"]) + "\n")
    print("SUCCESS:", len(results), "songs generated")
    for r in results:
        print("WROTE:", r["payload"])
    sys.exit(0)


if __name__ == "__main__":
    main()
