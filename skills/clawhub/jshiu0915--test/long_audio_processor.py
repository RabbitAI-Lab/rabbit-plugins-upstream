#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
长音频处理器模块
处理音频格式转换、分割和转录
"""

import os
import sys
import json
import time
import hashlib
import base64
import wave
import math
import array
import tempfile
import subprocess
from pathlib import Path
import requests
import logging

logger = logging.getLogger(__name__)


def get_audio_info(audio_path: str):
    """获取音频文件信息（支持WAV、MP3等格式）"""
    # 首先尝试使用wave模块（仅适用于WAV文件）
    try:
        with wave.open(audio_path, 'rb') as wav_file:
            frames = wav_file.getnframes()
            rate = wav_file.getframerate()
            duration = frames / float(rate)
            channels = wav_file.getnchannels()
            sampwidth = wav_file.getsampwidth()

            return {
                'duration': duration,
                'sample_rate': rate,
                'channels': channels,
                'sample_width': sampwidth,
                'frames': frames
            }
    except Exception as wave_error:
        # 如果wave模块失败，尝试使用ffprobe获取音频信息
        try:
            # 使用ffprobe获取音频信息
            cmd = [
                'ffprobe',
                '-v', 'quiet',
                '-print_format', 'json',
                '-show_format',
                '-show_streams',
                audio_path
            ]

            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False, check=True)
            # 解码输出，忽略编码错误
            stdout_decoded = result.stdout.decode('utf-8', errors='ignore')
            info = json.loads(stdout_decoded)

            # 查找音频流
            audio_stream = None
            for stream in info.get('streams', []):
                if stream.get('codec_type') == 'audio':
                    audio_stream = stream
                    break

            if audio_stream is None:
                raise ValueError("No audio stream found in file")

            # 获取基本信息
            duration = float(info['format'].get('duration', 0))
            sample_rate = int(audio_stream.get('sample_rate', 0))
            channels = int(audio_stream.get('channels', 0))

            # 获取文件大小
            file_size = os.path.getsize(audio_path)

            return {
                'duration': duration,
                'sample_rate': sample_rate,
                'channels': channels,
                'sample_width': 2,  # 默认假设16位（ffprobe不直接提供此信息）
                'frames': int(duration * sample_rate) if duration > 0 and sample_rate > 0 else 0,
                'file_size': file_size
            }

        except Exception as ffprobe_error:
            logger.error(f"Failed to get audio info for {audio_path}: wave error={wave_error}, ffprobe error={ffprobe_error}")
            raise Exception(f"无法获取音频文件信息: {ffprobe_error}")


def convert_wav_format(input_audio: str, output_wav: str, target_sample_rate: int = 16000, target_channels: int = 1):
    """
    转换音频文件格式（采样率、声道数）
    支持WAV、MP3等多种格式

    Args:
        input_audio: 输入音频文件路径
        output_wav: 输出WAV文件路径
        target_sample_rate: 目标采样率（默认16000）
        target_channels: 目标声道数（默认1，单声道）
    """
    try:
        # 首先尝试使用wave模块（仅适用于WAV文件）
        try:
            with wave.open(input_audio, 'rb') as wav_in:
                params = wav_in.getparams()
                original_rate = params.framerate
                original_channels = params.nchannels
                sampwidth = params.sampwidth
                frames = wav_in.readframes(params.nframes)

                # 将字节数据转换为数组
                if sampwidth == 1:
                    dtype = 'b'  # 8位有符号
                    fmt = 'b'
                elif sampwidth == 2:
                    dtype = 'h'  # 16位有符号
                    fmt = 'h'
                elif sampwidth == 3:
                    # 24位需要特殊处理
                    dtype = 'i'  # 32位有符号
                    fmt = 'i'
                    # 简化处理：转换为16位
                    logger.warning("24-bit audio not fully supported, converting to 16-bit")
                    sampwidth = 2
                elif sampwidth == 4:
                    dtype = 'i'  # 32位有符号
                    fmt = 'i'
                else:
                    raise ValueError(f"Unsupported sample width: {sampwidth}")

                # 转换为数组
                if sampwidth == 1:
                    audio_data = array.array('b', frames)
                elif sampwidth == 2:
                    audio_data = array.array('h')
                    audio_data.frombytes(frames)
                elif sampwidth == 4:
                    audio_data = array.array('i')
                    audio_data.frombytes(frames)

                # 如果是立体声，转换为单声道（平均值）
                if original_channels == 2 and target_channels == 1:
                    # 将左右声道平均
                    mono_data = array.array(fmt)
                    for i in range(0, len(audio_data), 2):
                        if i+1 < len(audio_data):
                            left = audio_data[i]
                            right = audio_data[i+1]
                            mono_value = (left + right) // 2
                            mono_data.append(mono_value)
                    audio_data = mono_data
                    original_channels = 1

                # 重采样（简单实现：线性重采样）
                if original_rate != target_sample_rate:
                    ratio = original_rate / target_sample_rate
                    new_length = int(len(audio_data) / ratio)
                    resampled_data = array.array(fmt)

                    # 简单重采样：线性插值
                    for i in range(new_length):
                        pos = i * ratio
                        idx = int(pos)
                        frac = pos - idx

                        if idx + 1 < len(audio_data):
                            # 线性插值
                            val = audio_data[idx] * (1 - frac) + audio_data[idx + 1] * frac
                        else:
                            val = audio_data[min(idx, len(audio_data) - 1)]

                        resampled_data.append(int(val))

                    audio_data = resampled_data
                    original_rate = target_sample_rate

                # 写入输出文件
                with wave.open(output_wav, 'wb') as wav_out:
                    wav_out.setnchannels(target_channels)
                    wav_out.setsampwidth(sampwidth)
                    wav_out.setframerate(target_sample_rate)
                    wav_out.writeframes(audio_data.tobytes())

                logger.info(f"Converted {input_audio}: {original_rate}Hz {original_channels}ch -> {target_sample_rate}Hz {target_channels}ch")
                return

        except Exception as wave_error:
            # 如果wave模块失败，使用ffmpeg进行转换
            logger.info(f"Wave module failed for {input_audio}, using ffmpeg: {wave_error}")

        # 使用ffmpeg进行音频转换
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', input_audio,           # 输入文件
            '-ar', str(target_sample_rate),  # 采样率
            '-ac', str(target_channels),     # 声道数
            '-acodec', 'pcm_s16le',      # 编码格式：16位有符号PCM
            '-y',                        # 覆盖输出文件
            output_wav
        ]

        logger.info(f"Converting audio with ffmpeg: {' '.join(ffmpeg_cmd)}")
        result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, check=True)

        if result.returncode != 0:
            raise Exception(f"ffmpeg conversion failed: {result.stderr}")

        logger.info(f"Converted {input_audio} -> {output_wav} using ffmpeg")

    except Exception as e:
        logger.error(f"Failed to convert audio format: {e}")
        # 如果转换失败，复制原始文件（如果原始文件是WAV格式）
        try:
            import shutil
            if input_audio.lower().endswith('.wav'):
                shutil.copy2(input_audio, output_wav)
                logger.warning(f"Using original WAV file instead: {output_wav}")
            else:
                raise Exception(f"无法转换非WAV文件: {input_audio}")
        except Exception as copy_error:
            logger.error(f"Failed to copy original file: {copy_error}")
            raise Exception(f"音频格式转换失败: {e}")


def split_wav_file(input_wav: str, output_dir: str, segment_duration: float = 60.0):
    """
    分割WAV文件为多个片段

    Args:
        input_wav: 输入WAV文件路径
        output_dir: 输出目录
        segment_duration: 每个片段的时长（秒）

    Returns:
        分割后的文件路径列表
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    audio_info = get_audio_info(input_wav)
    duration = audio_info['duration']
    sample_rate = audio_info['sample_rate']
    channels = audio_info['channels']
    sampwidth = audio_info['sample_width']

    logger.info(f"Audio duration: {duration:.2f} seconds")
    logger.info(f"Sample rate: {sample_rate} Hz, Channels: {channels}")

    # 计算需要分割的段数
    num_segments = math.ceil(duration / segment_duration)
    logger.info(f"Splitting into {num_segments} segments (max {segment_duration}s each)")

    segment_files = []

    with wave.open(input_wav, 'rb') as wav_in:
        # 获取音频参数
        params = wav_in.getparams()

        # 计算每段的帧数
        frames_per_segment = int(sample_rate * segment_duration)

        for i in range(num_segments):
            # 设置输出文件路径
            stem = Path(input_wav).stem
            output_file = output_dir / f"{stem}_part{i+1:03d}.wav"

            # 计算当前段的起始帧和帧数
            start_frame = i * frames_per_segment
            # 最后一段可能不足frames_per_segment
            if i == num_segments - 1:
                frames_to_read = wav_in.getnframes() - start_frame
            else:
                frames_to_read = frames_per_segment

            if frames_to_read <= 0:
                break

            # 设置输入文件读取位置
            wav_in.setpos(start_frame)

            # 读取音频数据
            frames = wav_in.readframes(frames_to_read)

            # 写入输出文件
            with wave.open(str(output_file), 'wb') as wav_out:
                wav_out.setparams(params)
                wav_out.writeframes(frames)

            segment_duration_actual = frames_to_read / sample_rate
            logger.info(f"Created segment {i+1}: {output_file.name} ({segment_duration_actual:.2f}s)")
            segment_files.append(str(output_file))

    return segment_files


def process_long_audio(recognizer, audio_file: Path, text_dir: Path, segment_duration: float = 30.0):
    """
    处理长音频文件（自动转换格式、分割、转录）

    Args:
        recognizer: BaiduSpeechRecognizer实例
        audio_file: 音频文件路径
        text_dir: 文本输出目录
        segment_duration: 分割时长（秒）

    Returns:
        (success, text_or_error)
    """
    import tempfile
    import shutil

    original_audio_file = audio_file
    temp_file_path = None
    segments_dir = None
    segment_text_files = []

    try:
        # 获取音频信息
        audio_info = get_audio_info(str(audio_file))
        duration = audio_info['duration']
        sample_rate = audio_info['sample_rate']
        channels = audio_info['channels']
        file_size_mb = audio_file.stat().st_size / (1024 * 1024)

        logger.info(f"Audio: {duration:.2f}s, {sample_rate}Hz, {channels}ch, {file_size_mb:.2f}MB")

        # 检查是否需要转换音频格式（百度API要求：16000/8000 Hz，单声道）
        need_conversion = False
        if sample_rate not in [16000, 8000] or channels != 1:
            need_conversion = True
            logger.info(f"Audio format needs conversion: {sample_rate}Hz {channels}ch -> 16000Hz 1ch")

        current_audio_file = audio_file
        if need_conversion:
            # 创建临时转换文件
            temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
            temp_file.close()
            temp_file_path = temp_file.name

            logger.info(f"Converting audio format to 16000Hz mono: {temp_file_path}")
            convert_wav_format(str(audio_file), temp_file_path, target_sample_rate=16000, target_channels=1)

            # 更新当前音频文件为转换后的文件
            current_audio_file = Path(temp_file_path)
            # 重新获取转换后的音频信息
            audio_info = get_audio_info(str(current_audio_file))
            duration = audio_info['duration']
            sample_rate = audio_info['sample_rate']
            channels = audio_info['channels']
            file_size_mb = current_audio_file.stat().st_size / (1024 * 1024)
            logger.info(f"Converted audio: {duration:.2f}s, {sample_rate}Hz, {channels}ch, {file_size_mb:.2f}MB")

        # 判断是否需要分割（百度API限制：文件大小大于4MB或时长大于30秒）
        need_split = False
        if file_size_mb > 4.0 or duration > segment_duration:
            need_split = True
            logger.info(f"Audio needs splitting: size={file_size_mb:.2f}MB > 4MB or duration={duration:.2f}s > {segment_duration}s")

        if need_split:
            # 创建临时目录存放分割片段
            segments_dir = Path(tempfile.mkdtemp(prefix="audio_segments_"))
            logger.info(f"Creating temporary segments directory: {segments_dir}")

            # 分割音频
            segment_files = split_wav_file(str(current_audio_file), segments_dir, segment_duration)

            # 转录每个片段
            all_texts = []
            for segment_file in segment_files:
                try:
                    # 识别音频
                    result = recognizer.recognize_audio(
                        segment_file,
                        file_format="wav",
                        rate=16000,
                        dev_pid=1537
                    )

                    # 提取文本
                    text = recognizer.extract_text_from_result(result)
                    all_texts.append(text)

                    # 保存片段的文本（可选）
                    stem = Path(segment_file).stem
                    output_file = text_dir / f"{stem}.txt"
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(text)
                    segment_text_files.append(output_file)

                    logger.info(f"Transcribed segment: {Path(segment_file).name} -> {text[:50]}...")

                except Exception as e:
                    logger.error(f"Failed to transcribe segment {segment_file}: {e}")
                    all_texts.append(f"[ERROR in segment {Path(segment_file).name}: {str(e)}]")

            # 合并所有文本
            combined_text = "\n".join(all_texts)

            # 保存合并的文本
            combined_file = text_dir / f"{original_audio_file.stem}_combined.txt"
            with open(combined_file, 'w', encoding='utf-8') as f:
                f.write(combined_text)

            logger.info(f"Combined transcription saved to: {combined_file.name}")
            return True, combined_text

        else:
            # 直接转录短音频
            try:
                result = recognizer.recognize_audio(
                    str(current_audio_file),
                    file_format="wav",
                    rate=16000,
                    dev_pid=1537
                )

                text = recognizer.extract_text_from_result(result)

                # 保存文本
                output_file = text_dir / f"{original_audio_file.stem}.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)

                logger.info(f"Transcription completed: {original_audio_file.name} -> {output_file.name}")
                logger.info(f"Text preview: {text[:100]}..." if len(text) > 100 else f"Text: {text}")

                return True, text

            except Exception as e:
                logger.error(f"Failed to transcribe {original_audio_file.name}: {e}")
                return False, str(e)

    except Exception as e:
        logger.error(f"Error processing long audio {audio_file.name}: {e}")
        return False, str(e)

    finally:
        # 清理临时文件
        if temp_file_path and os.path.exists(temp_file_path):
            try:
                os.unlink(temp_file_path)
                logger.info(f"Cleaned up temporary file: {temp_file_path}")
            except Exception as cleanup_error:
                logger.warning(f"Failed to cleanup temporary file {temp_file_path}: {cleanup_error}")

        if segments_dir and segments_dir.exists():
            try:
                # 删除目录及其内容
                for file_path in segments_dir.glob("*"):
                    file_path.unlink()
                segments_dir.rmdir()
                logger.info(f"Cleaned up segments directory: {segments_dir}")
            except Exception as cleanup_error:
                logger.warning(f"Failed to cleanup segments directory {segments_dir}: {cleanup_error}")

        # 清理临时片段文本文件
        for text_file in segment_text_files:
            try:
                if text_file.exists():
                    text_file.unlink()
                    logger.info(f"Cleaned up temporary segment text file: {text_file}")
            except Exception as cleanup_error:
                logger.warning(f"Failed to cleanup temporary text file {text_file}: {cleanup_error}")