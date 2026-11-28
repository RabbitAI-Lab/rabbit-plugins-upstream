---
name: weixin-chat
description: Read and monitor the user's own local weixin (薇芯) chat history on Windows. Use this when the user asks an AI to access their own weixin conversations — e.g. read the FULL chat history of a specified conversation, or WATCH a specified conversation for new incoming messages in real time. All processing is local (no network); it decrypts the user's own local database on their own machine. Commands are a plain Python CLI (`wxskill.py`) that outputs JSON, so any agent can use it.
license: for personal, local, educational use on the user's own account only
---

# weixin-chat — 本机薇芯聊天记录读取 / 监听

把本机**已登录薇芯（个人号）**的聊天记录解密后，以 **JSON** 暴露给任意 AI。两大能力：

1. **读取指定会话的全量聊天记录** → `wxskill.py history "<会话>"`
2. **监听指定会话的实时增量消息** → `wxskill.py poll "<会话>"`（反复调用）或 `wxskill.py watch "<会话>"`（常驻写文件）

> 仅限**本人设备、本人账号**、本地学习研究。解密的是用户本机自己的数据库，全程无网络。导出内容含他人隐私，勿外传。

## 已验证环境 / 操作系统支持

实测通过：Windows 11（10.0.26300, x64）、Python 3.15.1、weixin 4.2.1.11（64 位）、pycryptodome 4.6.0、psutil 7.2.2、frida 17.28.0、zstandard 0.25.0。

**仅 Windows 已验证**：`setup` 抓密钥依赖 Frida hook `Weixin.dll`（x64），是 Windows 专有的；macOS/Linux 未支持。读取/导出为纯 Python，给定 `keys/<wxid>.json` 理论跨平台，但未在非 Windows 验证。

## 前置条件（AI 先自检）

先运行 `python wxskill.py status`，它返回 JSON：`account` / `weixin_running` / `keys_ready{contact,session,message}` / `deps` / `ready`。

- 平台 **Windows**；薇芯正在运行并已登录。
- 依赖：`pip install pycryptodome psutil frida zstandard`（`frida` 仅 `setup` 抓密钥时需要；ffmpeg 可选）。
- **密钥**：首次使用需抓一次密钥（见下）。`ready:false` 或 `keys_ready.message:false` 时，提示用户先做 setup。

### 抓密钥（一次性，需真人配合）

```bash
python wxskill.py setup --seconds 90
```

运行期间**请用户到薇芯里**多点开会话、搜索聊天内容、打开收藏/朋友圈/公众号——每个数据库的连接首次打开时才会暴露它的密钥。AI 无法代替这一步的人工操作。抓到的密钥存 `keys/<wxid>.json`，稳定，长期复用。

## 命令

所有数据命令向 **stdout 输出一行/一段 JSON**；出错输出 `{"error": "..."}` 且退出码非 0。会话可用**显示名或 wxid**（子串或精确）指定。

| 命令 | 作用 |
|---|---|
| `python wxskill.py status` | 自检前置条件 |
| `python wxskill.py list` | 列出可导出会话 `[{display, wxid, kind, count, last_time, last}]` |
| `python wxskill.py history "<会话>" [--limit N] [--media] [--out FILE]` | **能力1**：全量历史 |
| `python wxskill.py poll "<会话>" [--media] [--backlog]` | **能力2**：增量（首次建基线返回空，之后只给新消息） |
| `python wxskill.py watch "<会话>" [--interval 5] [--out FILE]` | **能力2**（流式）：常驻，把新消息逐行 NDJSON 追加到文件并打印 |
| `python wxskill.py setup [--seconds 90]` | 抓密钥（需真人配合） |
| `python wxskill.py reset [--yes]` | 清理所有生成物，还原初始状态 |

多账号时加 `--account <wxid>`（默认取运行中的那个）。

## 消息记录字段（JSON）

```json
{
  "local_id": 128,
  "ts": 1700000000,
  "time": "2026-11-28 01:32:48",
  "sender": "张三",
  "sender_wxid": "wxid_xxxxxxxx",
  "is_me": false,
  "type": "file",
  "content": "[文件:example.pdf 502.0KB]",
  "media": "media/张三/example.pdf"
}
```

- `sender` 显示名（群昵称 > 备注/昵称 > wxid）；`sender_wxid` 是**唯一标识**，昵称撞名也能区分；本人 `is_me:true`、`sender:"我"`。
- `type`：`text/image/voice/video/file/link/quote/transfer/redpacket/sticker/card/location/call/miniapp/channel/merged/system/unknown`。
- `content`：人类可读文本（文本原样；其余带细节占位）。
- `media`：仅当带 `--media` 且是文件/视频时，复制本体后给相对路径；否则 `null`。

## 两条主流程

**读全量：**
```bash
python wxskill.py list                      # 看有哪些会话
python wxskill.py history "张三" --out h.json  # 读某会话全部历史
```

**监听增量（推荐轮询式，最契合工具调用型 AI）：**
```bash
python wxskill.py poll "张三"     # 第一次：建基线，new:0
# …对方来消息后…
python wxskill.py poll "张三"     # 只返回新到的那几条；无新消息 new:0
```
或常驻流式（适合"后台跑 + tail 文件"型 AI）：
```bash
python wxskill.py watch "张三" --out 张三.jsonl   # 新消息逐行追加到 jsonl
```

## 通用性 / 安装

本目录即一个 skill：可复制到任意 agent 的 skills 目录（如 `~/.claude/skills/weixin-chat/`），或直接运行 `wxskill.py`。输出是纯 JSON，与具体模型/平台无关。除 `wxskill.py` 外，仓库还带一个交互式终端程序 `wechat_export.py`（见 `README.md`）。

## 限制

- **准实时**：只解密主库，最新消息可能还在未落盘的 `-wal` 里，有几秒延迟。
- **图片 / 语音**本体暂不导出（图片是 weixin 自有 wxgf/HEVC 格式且密钥取不到；语音在 media 库）；`content` 仍给占位。
- 文件、视频本体可用 `--media` 复制到 `export/<wxid>/media/`。
- 群成员无昵称时 `sender` 回退为其 wxid（唯一标识仍在）。
