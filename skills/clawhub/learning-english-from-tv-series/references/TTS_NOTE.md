# TTS 音频方案说明（DramaLex）

## 为什么用 TTS
- 从纯字幕无法还原剧集原声（演员语音、连读、弱读）。但"有声耳测"仍需音频——
  TTS 可为每个词/语块/例句生成**真实可听**的发音，训练"声音↔意义"绑定与音素辨识。
- TTS 音频是**发音参考 + 耳测加分项**，**不等于剧集原声**，也不替代"观看步骤"的听力训练。
  真·听懂 native 语速，只能来自观看剧集本身。

## 后端（离线优先，自动探测）
| 后端 | 平台 | 依赖 | 音质 |
|---|---|---|---|
| `say` | macOS 内置 | 无（系统 Samantha 等嗓音） | 自然 |
| `espeak-ng` | Linux | 需安装 espeak-ng | 机器人腔、清晰 |
| `pyttsx3` | 跨平台 | `pip install pyttsx3` | 调用系统 TTS |
| `gTTS` | 在线 | `pip install gTTS` + 网络 | 较好 |

- 脚本 `gen_audio.py` 默认 `--backend auto`：依次探测 `say` → `espeak-ng` → `pyttsx3` → `gTTS`。
- macOS 上 `say` 输出 AIFF，脚本用标准库 `aifc`+`wave` 转 WAV（零额外依赖），Anki 全平台可播。

## 音频产出
- 每项生成 `term_audio`（词/语块发音）与 `line_audio`（剧中原句发音，可选）。
- 文件名形如 `001_hook_up.wav`、`001_hook_up_line.wav`，与 `cards.tsv` 一并导入 Anki。

## 何时换"原生音频"（专业模式）
- 若用户上传剧集音视频，可抽取原生音频替换 TTS（架构已留口子）：用 ffmpeg 抽取片段 → 命名同规则 → 写入 `term_audio`/`line_audio`。
- 此时耳测升为"听演员原声"，听写/跟读也变为真·听写。这属于可选增强，不在默认 v1 强制范围。

## 无 TTS 后端时
- 脚本跳过音频，`words.json` 不含 `term_audio`；`cards.tsv` 正面退化为纯文本（仍可按"看词回想义"使用）。
- 诚实标注：此时耳测降级，建议用户观看剧集补足听力训练。
