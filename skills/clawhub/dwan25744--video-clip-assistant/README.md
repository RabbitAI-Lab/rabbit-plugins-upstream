# Video Clip Assistant v2

AI 智能视频剪辑助手。基于 [video-use](https://github.com/browser-use/video-use) 架构改进。

## 核心理念

> 用户只需描述剪辑意图，AI Agent 自动完成转录 → 分析 → 编辑决策 → 渲染 → 自检全流程。无需手动操作时间轴。

## 架构

```
素材文件夹 → 转录层 → AI决策层 → 渲染层 → 自检层 → 成品
```

## 脚本清单

| 脚本 | 类型 | 说明 |
|------|------|------|
| `scripts/transcribe.py` | 新增 | ASR 转录，输出 packed transcript JSON |
| `scripts/generate_edl.py` | 新增 | LLM 读取 transcript → 生成 Edit Decision List |
| `scripts/render_edl.py` | 新增 | 按 EDL 调用 FFmpeg 渲染视频 |
| `scripts/self_eval.py` | 新增 | 渲染后质量自检 |
| `scripts/generate_subtitles.py` | 新增 | 词级时间戳 → SRT 字幕 |
| `scripts/cut_video.py` | 增强 | 支持 EDL JSON 输入 |
| `scripts/extract_highlights.py` | 增强 | 场景+音频+语义三维度 |
| `scripts/burn_subtitles.py` | 增强 | 支持 6 种字幕风格预设 |
| `scripts/export_social.py` | 保留 | 多平台格式导出 |

## 模板

| 文件 | 说明 |
|------|------|
| `templates/edl_schema.json` | Edit Decision List JSON Schema |
| `templates/clip_strategies.yaml` | 6 种预置剪辑策略 |
| `templates/subtitle_styles.json` | 6 种字幕风格预设 |

## 安装

```bash
# 最小安装
pip install openai-whisper pyyaml

# 全功能
pip install openai-whisper faster-whisper pyyaml funasr funclip
```

依赖: FFmpeg, Python 3.9+

## 对比 video-use

| 维度 | video-use | 本 Skill |
|------|-----------|---------|
| ASR | ElevenLabs 付费 | 本地 Whisper 免费 |
| 平台 | Claude Code 专属 | WorkBuddy 通用 |
| 中文 | 基础 | 深度优化 |
| 策略 | 无模板 | 6 种预置+自定义 |
| 导出 | 无 | 多平台适配 |
| 字幕 | 基础 | 6 种风格预设 |

## License

MIT
