# TTS 供应商对比

`text-to-video` 的 Stage 2 需要选 TTS。中文口播最常见的几个：

## 选型速查

| 供应商 | 音色质量 | 价格 | 中文音色 | 接入难度 | 适用场景 |
|---|---|---|---|---|---|
| **阿里云百炼（CosyVoice）** | ★★★★★ | ~¥0.5/万字 | 多（推荐"龙小燕"女声/"云小希"） | 需 API key | 商业项目首选 |
| **字节豆包 TTS** | ★★★★ | 较便宜 | 多 | 需 API key | 字节系产品/抖音视频 |
| **OpenAI TTS** | ★★★★★ | $15/1M 字符 | 弱（中文是英文模型硬读） | 需 API key | 英文为主 |
| **macOS `say`** | ★★ | 免费 | "Tingting"(女) / "美佳" | 零配置 | 草稿/无 key 备选 |
| **Kokoro-82M** | ★★★★ | 免费本地 | 多 | 需 onnx runtime + Python | 本地化/隐私 |

## 推荐默认

**商业项目**：阿里云百炼 CosyVoice
**草稿阶段**：macOS `say -v Tingting`（先听节奏，再花钱出正式版）
**本地优先**：Kokoro-82M

## macOS `say` 速查（最常用，零成本）

```bash
# 列中文音色
say -v '?' | grep -i "tingting\|meijia\|sin-ji"

# 单句试听
say -v Tingting -o test.aiff "最近在看 AI 硬件"

# 转 mp3
ffmpeg -y -i test.aiff -codec:a libmp3lame -qscale:a 2 test.mp3

# 长脚本（按句切分避免一口气念完）
python3 -c "
import subprocess
sentences = ['最近在看 AI 硬件。', '为什么大厂都在做 AI 眼镜？', ...]
for i, s in enumerate(sentences):
    subprocess.run(['say', '-v', 'Tingting', '-o', f'chunks/{i:02d}.aiff', s])
"
```

## 阿里云百炼（CosyVoice）调用范式

```python
# pip install dashscope
import dashscope
from dashscope.audio.tts import SpeechSynthesizer

dashscope.api_key = os.environ.get("DASHSCOPE_API_KEY")
result = SpeechSynthesizer.call(
    model="cosyvoice-v1",
    voice="longxiaobai",        # 女声示例
    text="最近在看 AI 硬件",
    format="mp3",
    sample_rate=24000,
)
with open("chunks/00.mp3", "wb") as f:
    f.write(result.get_audio_data())
```

## hyperframes 自带 TTS

```bash
# 需要先 npx hyperframes tts --help 看最新选项
npx hyperframes tts --text "最近在看 AI 硬件" --voice af_heart --output chunks/00.mp3
```

> ⚠️ hyperframes 内置 TTS 主要是英文 Kokoro 类的；中文场景建议用上面外部 API。

## TTS 配置写到 `_video_plan.md`

Stage 1 确认门 1 之前，方案包里要写：

```markdown
## 5. TTS 配置
- **供应商**: 阿里云百炼 CosyVoice
- **音色**: longxiaobai (干练女声)
- **语速**: 1.0x
- **音调**: 0
- **采样率**: 24000Hz
- **格式**: mp3
- **API Key 环境变量名**: DASHSCOPE_API_KEY
- **每段切分**: 按场景切（避免跨场景串句）
```

Stage 2 拿这个跑 `scripts/generate_tts.sh` 出全部音轨。
