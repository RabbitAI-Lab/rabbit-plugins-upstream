# 虚拟人口播 / Digital Human

脚本：`scripts/digital_human.py`

## 三条路线怎么选

| 用户手上有什么 | 走哪条 | 命令 |
|---|---|---|
| 只有文案，形象随便挑 | 平台数字人 | `actors` → `perform` |
| 有本人照片，想长期复用这个形象 | 专属数字人 | `persona-create` → `perform` |
| 有一张人像 + 一段现成音频 | 直接对口型 | `lipsync` |

`perform` 的 `--actor-id` 对平台数字人和专属数字人通用，创建完 persona 直接拿返回的 id 传进去即可。

## actors — 平台形象列表

```bash
python3 scripts/digital_human.py actors --gender female --industry beauty --limit 20
```

七个筛选维度都接受多值：`--gender` `--age` `--situation` `--pose` `--shot-type` `--ethnicity` `--industry`。分页用 `--offset` / `--limit`。

## say — 文字转语音（同步）

```bash
python3 scripts/digital_human.py say --actor-id act_123 --script "今天给大家推荐一款好物"
```

返回 `audio_url` 和时长。调音色：`--speed`（语速）、`--stability`（稳定度，低=情绪起伏大）、`--similarity`（贴合原声程度）、`--auto-emotion`（自动情绪）。

产出的 `audio_url` 可以直接喂给 `perform --said-url` 或 `lipsync --audio-url`。

## perform — 数字人口播视频（异步）

```bash
python3 scripts/digital_human.py perform --actor-id act_123 --script "文案内容"
```

- `--script` 与 `--said-url` 二选一：给文案则内部先 TTS 再出画；给音频则跳过 TTS，按这段音频出画
- `--look-id` 指定同一形象下的不同造型
- 音色参数与 `say` 一致，另有 `--style`、`--speaker-boost`

长文案服务端会自动切段生成再拼接，不需要调用方手动分段。

## persona-create — 建专属形象（异步）

```bash
python3 scripts/digital_human.py persona-create \
  --photo-url https://.../portrait.jpg \
  --voice-audio-url https://.../sample.mp3 \
  --name "品牌代言人"
```

`--voice-audio-url` 可选：给了就顺带克隆声音，不给就只有形象、配音时用平台音色。建号是异步的，完成前 `perform` 会失败——用 `persona-status --actor-id` 查进度。

配套命令：`persona-list`（分页）、`persona-status`、`persona-delete`。

## lipsync — 任意人像配任意音频（异步）

```bash
python3 scripts/digital_human.py lipsync \
  --avatar-url https://.../face.jpg \
  --audio-url https://.../voice.mp3
```

不需要提前建形象，一次性使用。`--prompt` 可补充画面描述。

## 素材必须是公网 URL

`--photo-url` `--avatar-url` `--audio-url` 这些都只收 URL，不收本地文件。本地文件先转成 URL：

```bash
python3 scripts/upload.py image ./portrait.jpg
python3 scripts/upload.py audio ./voice.mp3
```

## 耗时参考

| 操作 | 预计 |
|---|---|
| `say` | 数秒（同步返回） |
| `perform` | 2–5 分钟，长文案更久 |
| `persona-create` | 1–3 分钟 |
| `lipsync` | 2–5 分钟 |

异步命令默认提交后自动轮询到出结果。`--no-wait` 只提交拿 `workspace_id`；超时后用 `query --workspace-id <id>` 接着等，任务不会因为轮询中断而丢失。
