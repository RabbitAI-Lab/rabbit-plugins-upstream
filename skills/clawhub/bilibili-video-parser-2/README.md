# B站视频解析

> 丢一个 B 站视频链接，还你一篇深度拆解报告

自动解析 B 站视频内容：提取元数据（标题/UP主/播放量）、下载并合并音视频流、关键帧视觉分析、语音转文字，最终输出结构化报告。

---

## 依赖

- **ffmpeg** — 视频/音频处理
- **curl** — 下载流媒体和调用 API
- **z-ai CLI** — VLM 视觉分析和 ASR 语音转文字
- **Python 3** — JSON 解析与流程编排

---

## 快速开始

```bash
python3 scripts/bilibili_parser.py "https://www.bilibili.com/video/BV1q2RhB9EQC"
```

---

## 解析流程

```
B站视频链接
    │
    ├─ 阶段 1：元数据提取 → 标题、UP主、时长、播放量等
    ├─ 阶段 2：字幕提取 → 检查是否有 CC 字幕（有则跳过 ASR）
    ├─ 阶段 3：流媒体下载 → video.m4s + audio.m4s → merged.mp4
    ├─ 阶段 4a：关键帧提取 → VLM 视觉分析
    ├─ 阶段 4b：音频提取 → ASR 语音转文字
    └─ 阶段 5：综合输出 → 元数据 + 画面描述 + 语音全文 + 摘要
```

---

## 输出结构

```json
{
  "metadata": {
    "title": "视频标题",
    "author": "UP主名称",
    "duration_seconds": 101,
    "views": 19441,
    "likes": 409,
    "published_at": "2026-05-07 09:39:28"
  },
  "visual_analysis": {
    "scenes": ["画面场景描述"],
    "people": ["人物信息"],
    "on_screen_text": ["屏幕文字"],
    "key_frames_analyzed": 5
  },
  "speech_transcript": "完整语音转文字文本...",
  "summary": "综合画面与语音内容的摘要..."
}
```

---

## 文件清单

| 文件 | 用途 |
|------|------|
| `scripts/bilibili_parser.py` | 核心解析脚本，编排全流程 |
| `skill.md` | Skill 工作流文档 |
| `skill.yaml` | Skill 元信息与注册配置 |
| `README.md` | 项目说明 |
| `LICENSE` | MIT 许可证 |

---

## 注意事项

- B 站 API 为非官方公开接口，可能随时变更
- CDN 流媒体链接有时效性，获取后需立即使用
- 下载视频流时必须携带 `Referer: https://www.bilibili.com` 请求头
- 音视频流始终分离（m4s 格式），需合并后使用
- 长视频（>10 分钟）建议只分析特定时间段
