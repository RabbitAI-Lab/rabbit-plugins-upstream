#!/usr/bin/env python3
"""
QQ音乐控制器 - macOS
====================
通过 MediaRemote 私有框架控制 QQ 音乐播放，无需 Accessibility 权限。

用法：
    python3 qq_music.py <command> [options]

命令：
    play        播放 / 暂停（切换）
    start       开始播放（如果是暂停状态）
    pause       暂停
    next        下一首
    prev        上一首
    random      随机播放一首（连续跳转 + 播放）
    volume-up   音量加
    volume-down 音量减
    status      检查 QQ 音乐运行状态
    launch      启动 QQ 音乐（如果未运行）
"""

import ctypes
import ctypes.util
import subprocess
import sys
import time
import random

# ─── MediaRemote 命令常量 ───
MR_PLAY = 0
MR_PAUSE = 1
MR_TOGGLE_PLAY = 2
MR_STOP = 3
MR_NEXT = 4
MR_PREVIOUS = 5
MR_VOLUME_UP = 6
MR_VOLUME_DOWN = 7

COMMAND_MAP = {
    "play": MR_TOGGLE_PLAY,
    "start": MR_PLAY,
    "pause": MR_PAUSE,
    "next": MR_NEXT,
    "prev": MR_PREVIOUS,
    "previous": MR_PREVIOUS,
    "volume-up": MR_VOLUME_UP,
    "volume-down": MR_VOLUME_DOWN,
}

QQMUSIC_BUNDLE = "com.tencent.QQMusicMac"
QQMUSIC_APP_NAME = "QQMusic"


def get_media_remote():
    """加载 MediaRemote 私有框架"""
    try:
        return ctypes.cdll.LoadLibrary(
            "/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote"
        )
    except Exception:
        return None


def send_media_command(mr, command_id):
    """发送媒体控制命令"""
    result = mr.MRMediaRemoteSendCommand(command_id, None)
    return result == 1


def is_qqmusic_running():
    """检查 QQ 音乐是否在运行"""
    result = subprocess.run(
        ["pgrep", "-x", QQMUSIC_APP_NAME],
        capture_output=True,
    )
    return result.returncode == 0


def launch_qqmusic():
    """启动 QQ 音乐"""
    if is_qqmusic_running():
        print("QQ音乐已在运行")
        return True
    print("正在启动 QQ 音乐...")
    subprocess.run(["open", "-a", QQMUSIC_APP_NAME], check=False)
    # 等待启动
    for _ in range(10):
        time.sleep(1)
        if is_qqmusic_running():
            print("QQ音乐已启动")
            time.sleep(2)  # 额外等待 UI 就绪
            return True
    print("警告：QQ 音乐启动超时")
    return False


def activate_qqmusic():
    """将 QQ 音乐置于前台"""
    subprocess.run(
        ["osascript", "-e", f'tell application "{QQMUSIC_APP_NAME}" to activate'],
        capture_output=True,
    )


def random_play(mr):
    """随机播放一首歌"""
    if not is_qqmusic_running():
        launch_qqmusic()

    # 先激活 QQ 音乐
    activate_qqmusic()
    time.sleep(1)

    # 先确保在播放
    send_media_command(mr, MR_PLAY)
    time.sleep(0.5)

    # 随机跳转 1-5 次来随机选择歌曲
    skips = random.randint(1, 5)
    print(f"随机跳转 {skips} 次...")
    for i in range(skips):
        send_media_command(mr, MR_NEXT)
        time.sleep(0.3)

    # 确保播放
    send_media_command(mr, MR_PLAY)
    print(f"已随机切换到一首新歌（跳了 {skips} 首）")
    return True


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1].lower()

    # status 命令不需要 MediaRemote
    if cmd == "status":
        running = is_qqmusic_running()
        print(f"QQ音乐运行状态: {'运行中' if running else '未运行'}")
        if running:
            activate_qqmusic()
        sys.exit(0)

    # launch 命令
    if cmd == "launch":
        launch_qqmusic()
        sys.exit(0)

    # 其他命令需要 MediaRemote
    mr = get_media_remote()
    if mr is None:
        print("错误：无法加载 MediaRemote 框架")
        sys.exit(1)

    # random 命令特殊处理
    if cmd == "random":
        success = random_play(mr)
        sys.exit(0 if success else 1)

    # 标准命令
    if cmd not in COMMAND_MAP:
        print(f"未知命令：{cmd}")
        print(__doc__)
        sys.exit(1)

    # 确保QQ音乐在运行
    if not is_qqmusic_running():
        print("QQ 音乐未运行，正在启动...")
        launch_qqmusic()

    command_id = COMMAND_MAP[cmd]
    success = send_media_command(mr, command_id)

    if success:
        action_desc = {
            "play": "播放/暂停 已切换",
            "start": "开始播放",
            "pause": "已暂停",
            "next": "已切换到下一首",
            "prev": "已切换到上一首",
            "volume-up": "音量已增加",
            "volume-down": "音量已减小",
        }
        print(action_desc.get(cmd, f"命令 {cmd} 已发送"))
    else:
        print(f"命令 {cmd} 发送失败")
        sys.exit(1)


if __name__ == "__main__":
    main()
