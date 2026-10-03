# video-en2zh-dub

把英文视频变成中文配音视频。三大件：**Whisper**（语音识别）→ **大模型**（字幕翻译）→ **edge-tts**（语音合成）→ **ffmpeg**（音画封装）。

全部离线/免费组件，不需要任何 API key。

## 快速开始

```bash
# 1. 安装 Python 依赖
pip install -r requirements.txt

# 2. 确认环境（依赖 + ffmpeg）
python scripts/check_env.py

# 3. 把英文视频放到工作目录，命名 input.mp4，然后：
python scripts/transcribe.py    # input.mp4 -> input.srt（英文字幕）
#    ↓  由你的 AI 助手把 input.srt 翻译成 output.srt
python scripts/synthesize.py    # output.srt -> output.mp3（中文配音）
ffmpeg -y -i input.mp4 -i output.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4
```

作为 Agent skill 使用时，由 Agent 自动编排上述流程，**你只需要提供视频**。

## 实测数据

一条 9 分 29 秒 / 1280x720 的英文访谈：

| 环节 | 耗时 | 产物 |
| --- | --- | --- |
| whisper `base`（CPU）转写 | 57 秒 | 166 条英文字幕 |
| 大模型翻译 | — | 166 条中文字幕，三项自检零偏差 |
| edge-tts 配音 | 约 34 分钟（旧版 sleep 10） | output.mp3，569.7 秒 |
| ffmpeg 合成 | 5.35 秒 | output.mp4，39MB |

改用本版默认的 `--sleep 1.5` 后，配音环节约 6 分钟。

成片音视频时长差 0.21 秒。

## 三种输出模式

| 模式 | 适用场景 | 命令要点 |
| --- | --- | --- |
| 替换原音 | 纯中文配音 | `-map 0:v:0 -map 1:a:0` |
| 双音轨并存 | 中英可切换 | 两条 audio 都 map，并打 `-metadata:s:a:N language=` |
| 混音 | 中文为主 + 英文背景音 | `amix` + `volume=0.25` |

双音轨务必打语言标记，否则播放器里只会显示"音轨 1 / 音轨 2"。

## 目录结构

```
video-en2zh-dub/
├── SKILL.md                      # Agent 读取的指令（含 frontmatter）
├── README.md                     # 本文件
├── LICENSE                       # MIT-0（ClawHub 要求）
├── requirements.txt
├── .clawhubignore
├── scripts/
│   ├── check_env.py              # 环境自检，仅依赖标准库
│   ├── transcribe.py             # 步骤 1：Whisper 转写
│   └── synthesize.py             # 步骤 3：edge-tts 配音
└── references/
    ├── pitfalls.md               # 踩坑笔记
    └── sync-tuning.md            # 音画同步优化
```

## 价值在哪里

两个脚本本身不难写。真正难的是 **`references/pitfalls.md`** 里那些东西——它们只有在完整跑通过几百条字幕后才会暴露：清理临时目录导致的"假失败"、`SSLKEYLOGFILE` 把"已安装"伪装成"未安装"、后台任务 stdout 缓冲让进度看起来像卡死、Whisper 把 Susie Wiles 听成 "Suzy Walsh"、配音时长溢出字幕时槽。

每个人自己踩一遍要花掉好几个小时。

## 已知局限

- **音画同步是 TTS 方案的固有短板**。中文朗读时长常超出字幕时槽，实测约三到四成条目会溢出。缓解办法见 `references/sync-tuning.md`，但无法彻底消除
- **edge-tts 依赖微软在线服务**，离线不可用，且可能被限流。脚本内置指数退避重试，可通过 `--sleep` 调节节奏
- **CPU 推理下 Whisper 较慢**。`base` 处理 10 分钟视频约 1 分钟，换 `small`/`medium` 精度更高但耗时成倍增长

## 发布到 ClawHub

```bash
npm i -g clawhub
clawhub login
clawhub skill publish ./video-en2zh-dub \
  --slug video-en2zh-dub \
  --name "Video English to Chinese Dub" \
  --categories creative,automation \
  --topics "whisper,tts,ffmpeg,subtitle,video-dubbing"
```

发布前请确认：

1. `LICENSE` 中的 `YOUR_NAME` 已替换为你的名字
2. 本 skill 会以 **MIT-0** 授权发布，且该许可证不可覆盖——等同于放弃著作权保护
3. 包内不含 `input.mp4` / `ffmpeg.exe` 等大文件（见 `.clawhubignore`）
4. 已在另一台机器上验证过 `check_env.py` 能跑通

> 首次发布的版本在安全扫描完成前，可能暂不出现在公开安装列表。
