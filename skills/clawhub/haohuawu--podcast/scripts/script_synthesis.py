#!/usr/bin/env python3
"""豆包 TTS 2.0 语音合成客户端。

管线设计（一次有损编码）：
  TTS 返回 WAV → 直接拼接 WAV（-c copy）→ 最后一步后处理时编一次 libmp3lame。
  豆包 TTS 2.0 支持直接返回 WAV 格式，省去了 mp3→wav 解码步骤。

失败语义：任何一段重试后仍合成失败 → 整个任务失败（返回 None / False），
绝不插静音占位——内容缺失比中断更糟，缺内容的节目一旦发布无法撤回听众记忆。

文本预处理保留中文全角标点：豆包 seed-tts 原生按中文标点建模韵律，
转半角属负优化（句尾语调退化、顿号停顿被拉长）。
"""

import requests
import base64
import hashlib
import json
import time
import uuid
import re
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional, List, Tuple

sys.path.insert(0, str(Path(__file__).parent))
# 解析器/角色判定/旁白节奏常量的唯一事实源在 script_md（validate/timeline 共用）
from script_md import (NARRATION_CONTEXT_TEXTS, NARRATION_GAIN_DB,      # noqa: F401
                       NARRATION_LEAD_SILENCE_MS, NARRATION_SPEECH_RATE,
                       NARRATION_TAIL_SILENCE_MS, NORMAL_SILENCE_MS,
                       is_host, is_narration, parse_podcast_script)

# 音频后处理链（播客标准）。loudnorm 放链尾，避免 EQ/压缩的增益叠加把
# true peak 推回 0dBFS 之上造成解码端削波。
# highpass: 80Hz 去低频隆隆声
# equalizer: 3kHz +2dB (人声 presence), 12kHz +1dB (空气感)
# acompressor: 3:1 轻柔压缩
# loudnorm: I=-16 LUFS (播客标准响度), TP=-1.5 dBTP, LRA=11
POSTPROCESS_FILTER = (
    "highpass=f=80,"
    "equalizer=f=3000:t=q:w=1:g=2,"
    "equalizer=f=12000:t=q:w=1:g=1,"
    "acompressor=threshold=-20dB:ratio=3:attack=10:release=100:makeup=2,"
    "loudnorm=I=-16:TP=-1.5:LRA=11"
)

SAMPLE_RATE = 24000

# 旁白"广播话筒"音色链：频带收窄（模拟广播链路）+ 200Hz 邻近温暖感 +
# 3kHz presence + 密实电台压缩，最后落到旁白轨音量。用音色本身与对话区分，
# 不依赖垫乐（长时间垫乐干扰人声、易疲劳——真实反馈）。
NARRATION_RADIO_FILTER = (
    "highpass=f=120,lowpass=f=7500,"
    "equalizer=f=200:t=q:w=1:g=3,"
    "equalizer=f=3000:t=q:w=1.5:g=2,"
    "acompressor=threshold=-18dB:ratio=4:attack=5:release=120:makeup=2,"
    f"volume={{gain}}dB"
)

# 拍话筒提示音（"咚、咚"）：垫在每段旁白开头——"领导讲话前拍话筒"的社交信号，
# 瞬时、无持续干扰地告诉听众"插播开始，注意听"。资产以 base64 文本随 skill 分发
#（ClawHub 发布只收纯文本文件，采样本身 CC0），首次用到时无损解码到临时目录；
# 缺失/解码失败静默跳过（不影响合成）。PODCAST_NARRATION_TAP=off 可禁用。
NARRATION_TAP_FILE = str(Path(__file__).parent.parent / "assets" / "mic_tap.wav")
NARRATION_TAP_B64 = str(Path(__file__).parent.parent / "assets" / "mic_tap.b64.txt")
_narration_tap_resolved: Optional[str] = None


def narration_tap_file() -> Optional[str]:
    """返回可用的拍话筒 WAV 路径；无资产时返回 None（调用方静默跳过）。
    优先 assets/mic_tap.wav（本地开发直放）；否则把 assets/mic_tap.b64.txt
    惰性解码到临时目录（字节与原采样一致，合成指纹/缓存语义不变）。"""
    global _narration_tap_resolved
    if os.path.exists(NARRATION_TAP_FILE):
        return NARRATION_TAP_FILE
    if _narration_tap_resolved and os.path.exists(_narration_tap_resolved):
        return _narration_tap_resolved
    if not os.path.exists(NARRATION_TAP_B64):
        return None
    try:
        cache_dir = Path(tempfile.gettempdir()) / "podcast-assets"
        cache_dir.mkdir(parents=True, exist_ok=True)
        out = cache_dir / "mic_tap.wav"
        data = base64.b64decode(Path(NARRATION_TAP_B64).read_text(encoding="ascii"))
        if not out.exists() or out.stat().st_size != len(data):
            out.write_bytes(data)
        _narration_tap_resolved = str(out)
        return _narration_tap_resolved
    except Exception:
        return None

# 分片音频缓存版本号：preprocess 规则 / RESOURCE_ID / 合成参数语义变更时 +1，整池自然失效
CACHE_VER = "v1"

# 确定性失败（凭证/参数/内容审核类 HTTP 状态码）：重试纯浪费且可能重复计费
NON_RETRYABLE_HTTP = {400, 401, 403, 404, 413}


class NonRetryableTTSError(Exception):
    """确定性 TTS 失败（如 401 凭证错误），不应重试。"""


def resolve_voices(host: Optional[str] = None, guest: Optional[str] = None) -> Tuple[str, str]:
    """参数 > 环境变量 > 默认值。dry-run（无 API key）与 DoubaoTTS 构造共用同一逻辑。"""
    return (
        host or os.environ.get("DOUBAO_TTS_HOST_VOICE", DoubaoTTS.DEFAULT_HOST_VOICE),
        guest or os.environ.get("DOUBAO_TTS_GUEST_VOICE", DoubaoTTS.DEFAULT_GUEST_VOICE),
    )


def chunk_cache_key(chunk: str, voice: str, is_narration: bool) -> str:
    """分片缓存 key：合成结果的全部决定因素入哈希——任一变化即新 key，天然自失效。"""
    rate = NARRATION_SPEECH_RATE if is_narration else 0
    ctx = "|".join(NARRATION_CONTEXT_TEXTS) if is_narration else ""
    raw = f"{CACHE_VER}|{DoubaoTTS.RESOURCE_ID}|{voice}|{rate}|{ctx}|{chunk}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def _run_ffmpeg(args: List[str]) -> Tuple[bool, str]:
    """跑 ffmpeg/ffprobe，返回 (成功, stderr 摘要)。统一错误处理，不抛异常。"""
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return False, (result.stderr or "")[-300:]
    return True, ""


def _concat_escape(path: str) -> str:
    """ffmpeg concat 协议中单引号的转义"""
    return path.replace("'", "'\\''")


def _concat_wavs(wav_files: List[str], list_path: str, output_path: str) -> bool:
    """concat demuxer 拼接同参数 WAV（-c copy，无转码）"""
    with open(list_path, "w", encoding="utf-8") as f:
        for wf in wav_files:
            f.write(f"file '{_concat_escape(wf)}'\n")
    ok, err = _run_ffmpeg([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", list_path, "-c", "copy", output_path,
    ])
    if not ok:
        print(f"  ❌ 拼接失败: {err}", flush=True)
    return ok


class DoubaoTTS:
    """豆包 TTS 2.0 客户端"""

    API_URL = "https://openspeech.bytedance.com/api/v3/tts/unidirectional"
    RESOURCE_ID = "seed-tts-2.0"

    DEFAULT_HOST_VOICE = "zh_male_liufei_uranus_bigtts"
    DEFAULT_GUEST_VOICE = "zh_female_tianmeiyueyue_uranus_bigtts"

    MAX_ATTEMPTS = 3  # 每个分片：1 次 + 2 次指数退避重试

    def __init__(
        self,
        api_key: Optional[str] = None,
        host_voice: Optional[str] = None,
        guest_voice: Optional[str] = None,
    ):
        self.api_key = api_key or os.environ.get("DOUBAO_TTS_API_KEY")
        if not self.api_key:
            raise ValueError("缺少 DOUBAO_TTS_API_KEY，请设置环境变量或传入 api_key")

        self.host_voice, self.guest_voice = resolve_voices(host_voice, guest_voice)

        self._session = requests.Session()

    # ===== 文本预处理 =====

    @staticmethod
    def preprocess_text(text: str) -> str:
        """预处理：去 Markdown/emoji、中英文间加空格。保留中文全角标点（韵律依赖）。"""
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)  # bold
        text = re.sub(r'\*([^*]+?)\*', r'\1', text)     # italic
        text = re.sub(r'`([^`]+)`', r'\1', text)        # code
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # links
        text = re.sub(r'(?m)^#{1,6}\s+', '', text)      # headers（仅行首，勿伤正文里的 #）
        # emoji 与变体选择符（含 U+1FA00 段新 emoji）
        text = re.sub(r'[\U0001f300-\U0001faff\U00002600-\U000027bf️]', '', text)

        # 中英文间加空格（帮助分词）
        text = re.sub(r'([一-鿿])([a-zA-Z0-9])', r'\1 \2', text)
        text = re.sub(r'([a-zA-Z0-9])([一-鿿])', r'\1 \2', text)

        text = re.sub(r'\s+', ' ', text).strip()
        return text

    @staticmethod
    def split_long_text(text: str, max_len: int = 200) -> List[str]:
        """长文本拆分为 ≤ max_len 的片段：先按句末标点，再按逗号/顿号，最后硬切兜底。"""
        if len(text) <= max_len:
            return [text]

        # 中文句号后无空格，用零宽断言切分
        sentences = [s for s in re.split(r'(?<=[。！？.!?])\s*', text) if s]
        chunks: List[str] = []
        current = ""

        def flush():
            nonlocal current
            if current:
                chunks.append(current)
                current = ""

        for sent in sentences:
            if len(current) + len(sent) <= max_len:
                current += sent
                continue
            flush()
            if len(sent) <= max_len:
                current = sent
                continue
            # 单句超长：按逗号/顿号切
            parts = [p for p in re.split(r'(?<=[，、,])\s*', sent) if p]
            for p in parts:
                if len(current) + len(p) <= max_len:
                    current += p
                else:
                    flush()
                    # 仍超长（无标点长串）：硬切兜底
                    while len(p) > max_len:
                        chunks.append(p[:max_len])
                        p = p[max_len:]
                    current = p
        flush()
        return chunks

    # ===== TTS 合成 =====

    def _synthesize_chunk(self, text: str, speaker: str, is_narration: bool = False) -> Optional[bytes]:
        """调用 TTS API 合成单个文本片段，返回 WAV bytes。旁白使用慢语速+语气指令。"""
        headers = {
            "X-Api-Key": self.api_key,
            "X-Api-Resource-Id": self.RESOURCE_ID,
            "X-Api-Request-Id": str(uuid.uuid4()),
        }
        audio_params = {"format": "wav", "sample_rate": SAMPLE_RATE}
        additions = None
        if is_narration:
            audio_params["speech_rate"] = NARRATION_SPEECH_RATE
            additions = json.dumps({"context_texts": NARRATION_CONTEXT_TEXTS})

        payload = {
            "user": {"uid": "podcast-gen"},
            "req_params": {
                "text": text,
                "speaker": speaker,
                "audio_params": audio_params,
                **({"additions": additions} if additions else {}),
            },
        }

        try:
            resp = self._session.post(
                self.API_URL, headers=headers, json=payload, stream=True, timeout=60
            )
            if resp.status_code != 200:
                print(f"  ❌ HTTP {resp.status_code}: {resp.text[:200]}", flush=True)
                if resp.status_code in NON_RETRYABLE_HTTP:
                    raise NonRetryableTTSError(f"HTTP {resp.status_code}")
                return None

            audio_chunks = []
            saw_terminal = False
            for line in resp.iter_lines():
                if not line:
                    continue
                try:
                    data = json.loads(line.decode("utf-8"))
                except json.JSONDecodeError:
                    continue
                code = data.get("code")
                if code is not None and code != 0:
                    # 流中途返错（配额/敏感词/限流）：宁可失败也不能拿截断音频当成功
                    print(f"  ❌ TTS 错误 code={code}: {data.get('message', '')[:200]}", flush=True)
                    return None
                if data.get("data"):
                    audio_chunks.append(base64.b64decode(data["data"]))
                elif code == 0:
                    saw_terminal = True
                    break

            # 流被中途掐断（代理/LB 干净关闭、无终止 code=0 事件）同样是失败：
            # 截断音频一旦发布无法撤回，宁可重试
            if not saw_terminal:
                print("  ❌ TTS 流缺少终止事件（连接被中断？），按失败处理", flush=True)
                return None
            return b"".join(audio_chunks) if audio_chunks else None

        except NonRetryableTTSError:
            raise
        except Exception as e:
            print(f"  ❌ 异常: {e}", flush=True)
            return None

    def _chunk_with_retry(self, text: str, speaker: str, is_narration: bool = False) -> Optional[bytes]:
        for attempt in range(self.MAX_ATTEMPTS):
            try:
                audio = self._synthesize_chunk(text, speaker, is_narration=is_narration)
            except NonRetryableTTSError as e:
                print(f"  ❌ 确定性失败（{e}），不重试", flush=True)
                return None
            if audio is not None:
                return audio
            if attempt < self.MAX_ATTEMPTS - 1:
                delay = 2 ** attempt
                print(f"  ↻ 重试 {attempt + 1}/{self.MAX_ATTEMPTS - 1}（{delay}s 后）", flush=True)
                time.sleep(delay)
        return None

    def synthesize(self, text: str, speaker: str, output_wav: str, is_narration: bool = False,
                   cache_dir: Optional[str] = None, force: bool = False) -> bool:
        """合成一段文本到 WAV 文件（预处理->拆分->逐片合成+重试->拼接）。

        旁白使用慢语速 + 语气指令。任一分片重试后仍失败即返回 False--不插静音占位。

        cache_dir: 分片音频缓存目录（key = 内容+参数哈希）。命中即复用不计费；
        合成成功的分片立即写入缓存——中途失败重跑时只重新计费失败的分片。
        force: 跳过缓存读取强制重新合成（新结果仍写入缓存）。
        """
        processed = self.preprocess_text(text)
        if not processed:
            # 纯 emoji/标记的段落预处理后为空：直接失败并说明，不触网重试
            print("  ❌ 文本预处理后为空（纯 emoji/Markdown 标记？），不发起 TTS 调用", flush=True)
            return False
        chunks = self.split_long_text(processed)

        if cache_dir:
            os.makedirs(cache_dir, exist_ok=True)

        wav_files = []
        try:
            for j, chunk in enumerate(chunks):
                cache_path = None
                if cache_dir:
                    cache_path = os.path.join(
                        cache_dir, chunk_cache_key(chunk, speaker, is_narration) + ".wav")

                if cache_path and not force and os.path.exists(cache_path):
                    with open(cache_path, "rb") as f:
                        audio = f.read()
                    print("  ↺ 缓存命中，跳过合成", flush=True)
                else:
                    audio = self._chunk_with_retry(chunk, speaker, is_narration=is_narration)
                    if audio is None:
                        return False
                    if cache_path:
                        # 先写临时文件再原子替换，避免中断留下半截缓存
                        tmp_path = cache_path + ".tmp"
                        with open(tmp_path, "wb") as f:
                            f.write(audio)
                        os.replace(tmp_path, cache_path)

                wav_path = output_wav.replace(".wav", f"_part{j}.wav")
                with open(wav_path, "wb") as f:
                    f.write(audio)
                wav_files.append(wav_path)

            if len(wav_files) == 1:
                shutil.move(wav_files[0], output_wav)
                wav_files = []
                return True

            list_path = output_wav.replace(".wav", "_list.txt")
            try:
                return _concat_wavs(wav_files, list_path, output_wav)
            finally:
                if os.path.exists(list_path):
                    os.remove(list_path)
        finally:
            for wf in wav_files:
                if os.path.exists(wf):
                    os.remove(wf)


def get_duration_seconds(path: str) -> int:
    result = subprocess.run([
        "ffprobe", "-v", "quiet", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", path
    ], capture_output=True, text=True)
    if result.returncode != 0 or not result.stdout.strip():
        print(f"  ⚠️ ffprobe 读取时长失败: {(result.stderr or '')[-200:]}", flush=True)
        return 0
    return int(float(result.stdout.strip()))


def generate_podcast_audio(
    script_path: str,
    output_path: str,
    tts: Optional[DoubaoTTS] = None,
    pause_seconds: float = 0.25,
    postprocess: bool = True,
    cache_dir: Optional[str] = None,
    force: bool = False,
) -> Optional[str]:
    """从播客脚本生成完整 MP3。任一段合成失败返回 None。

    旁白处理：主持人音色 + 语气指令 + 广播话筒音色链（NARRATION_RADIO_FILTER）+
    进场"拍话筒"提示音 + 进场 800ms/退场 1200ms 静音。普通轮间静音 250ms。
    cache_dir/force: 分片缓存目录与强制重合成开关（见 DoubaoTTS.synthesize）。
    失败重跑时已成功分片从缓存复用，只重新计费失败分片。
    """
    if tts is None:
        tts = DoubaoTTS()

    segments = parse_podcast_script(script_path)
    if not segments:
        print("❌ 未解析到任何对话段。检查说话人行格式：**主持人**：/**嘉宾**：/**旁白**：", flush=True)
        return None
    print(f"解析到 {len(segments)} 段对话", flush=True)

    clips_dir = Path(output_path).parent / "clips"
    clips_dir.mkdir(exist_ok=True)

    # 生成两种静音片段：旁白用 800ms，普通轮间用 250ms
    silence_files = {}
    for label, ms in [("normal", NORMAL_SILENCE_MS), ("lead", NARRATION_LEAD_SILENCE_MS),
                      ("tail", NARRATION_TAIL_SILENCE_MS)]:
        path = str(clips_dir / f"silence_{label}.wav")
        ok, err = _run_ffmpeg([
            "ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r={SAMPLE_RATE}:cl=mono",
            "-t", str(ms / 1000), "-c:a", "pcm_s16le", path,
        ])
        if not ok:
            print(f"❌ 生成静音片段失败（ffmpeg 可用吗？）: {err}", flush=True)
            return None
        silence_files[label] = path

    wav_list = []
    prev_was_narration = False
    for i, (speaker, text) in enumerate(segments):
        narration = is_narration(speaker)
        if narration:
            voice = tts.host_voice
        elif is_host(speaker):
            voice = tts.host_voice
        else:
            voice = tts.guest_voice

        clip_path = str(clips_dir / f"clip_{i:04d}.wav")
        role_label = "旁白" if narration else speaker
        print(f"[{i+1}/{len(segments)}] {role_label}: {text[:50]}...", flush=True)

        if not tts.synthesize(text, voice, clip_path, is_narration=narration,
                              cache_dir=cache_dir, force=force):
            print(f"\n❌ 第 {i+1} 段（{role_label}）重试后仍合成失败，任务中止。", flush=True)
            print(f"   失败文本：{text[:120]}", flush=True)
            if cache_dir:
                print(f"   已成功分片已写入缓存 {cache_dir}/；修正脚本后重跑同一命令，"
                      f"只会重新计费失败的分片。", flush=True)
            return None

        # 旁白片段过广播话筒音色链（含降音量）——用音色本身与对话区分
        if narration:
            gain_path = clip_path.replace(".wav", "_gain.wav")
            ok, err = _run_ffmpeg([
                "ffmpeg", "-y", "-i", clip_path,
                "-af", NARRATION_RADIO_FILTER.format(gain=NARRATION_GAIN_DB),
                "-c:a", "pcm_s16le", gain_path,
            ])
            if ok:
                os.remove(clip_path)
                clip_path = gain_path
            else:
                print(f"  ⚠️ 旁白处理失败，使用原始片段: {err}", flush=True)

        # 边界静音：进旁白 800ms，出旁白 1200ms（收束句后多给一拍），普通轮间 250ms
        if len(wav_list) > 0:
            if narration and not prev_was_narration:
                wav_list.append(silence_files["lead"])
            elif prev_was_narration and not narration:
                wav_list.append(silence_files["tail"])
            else:
                wav_list.append(silence_files["normal"])

        # 旁白进场提示音：拍话筒"咚、咚"（含尾部间隔），开场旁白同样适用
        if (narration and not prev_was_narration
                and os.environ.get("PODCAST_NARRATION_TAP") != "off"):
            tap = narration_tap_file()
            if tap:
                wav_list.append(tap)

        wav_list.append(clip_path)
        prev_was_narration = narration

    # 尾部静音不需要
    if wav_list and wav_list[-1].startswith(str(clips_dir / "silence_")):
        wav_list.pop()

    print(f"\n拼接 {len(wav_list)} 个片段...", flush=True)
    raw_path = str(clips_dir / "raw_merged.wav")
    if not _concat_wavs(wav_list, str(clips_dir / "concat_list.txt"), raw_path):
        return None

    # 唯一一次有损编码
    encode_args = ["ffmpeg", "-y", "-i", raw_path]
    if postprocess:
        print("后处理: highpass → EQ → compressor → loudnorm(-16 LUFS)，编码 128k MP3", flush=True)
        encode_args += ["-af", POSTPROCESS_FILTER]
    encode_args += ["-c:a", "libmp3lame", "-b:a", "128k", "-ar", str(SAMPLE_RATE), output_path]
    ok, err = _run_ffmpeg(encode_args)
    if not ok and postprocess:
        print(f"  ⚠️ 后处理失败，回退为无滤镜编码: {err}", flush=True)
        ok, err = _run_ffmpeg([
            "ffmpeg", "-y", "-i", raw_path,
            "-c:a", "libmp3lame", "-b:a", "128k", "-ar", str(SAMPLE_RATE), output_path,
        ])
    if not ok:
        print(f"❌ 编码失败: {err}", flush=True)
        return None

    shutil.rmtree(clips_dir, ignore_errors=True)

    duration = get_duration_seconds(output_path)
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\n✅ 播客音频生成完成", flush=True)
    print(f"   文件: {output_path}", flush=True)
    print(f"   时长: {duration}s ({duration/60:.1f} min)", flush=True)
    print(f"   大小: {size_mb:.1f} MB", flush=True)
    return output_path
