#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
百度智能云语音识别API音频转文字工具
"""

import os
import sys
import json
import time
import hashlib
import base64
import requests
import wave
import math
from pathlib import Path
from typing import List, Dict, Optional, Tuple
import logging

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def _strip_nonempty(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text if text else None


def find_claude_workspace_root(*search_starts: Path) -> Optional[Path]:
    """
    从各起点向上查找，返回第一个「含有子目录 .claude」的目录，
    即与 .claude 文件夹同级的项目根（audio_files / text_files 应建在此目录下）。
    """
    for start in search_starts:
        try:
            current = start.resolve()
        except OSError:
            continue
        for directory in [current, *current.parents]:
            try:
                if (directory / ".claude").is_dir():
                    return directory
            except OSError:
                continue
    return None


def resolve_default_audio_text_dirs() -> Tuple[Path, Path]:
    """未显式配置时，在 .claude 同级目录下使用 audio_files 与 text_files。"""
    script_dir = Path(__file__).resolve().parent
    root = find_claude_workspace_root(Path.cwd(), script_dir)
    if root is None:
        root = Path.cwd().resolve()
        logger.warning(
            "未在路径中找到 .claude 目录，已使用当前工作目录作为项目根: %s",
            root,
        )
    return root / "audio_files", root / "text_files"


# 导入长音频处理器
try:
    from long_audio_processor import process_long_audio, get_audio_info
    LONG_AUDIO_SUPPORT = True
except ImportError as e:
    logger.warning(f"长音频处理器导入失败: {e}，长音频处理功能不可用")
    LONG_AUDIO_SUPPORT = False


class BaiduSpeechRecognizer:
    """百度语音识别客户端"""

    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key
        self.token = None
        self.token_expire_time = 0

    def get_access_token(self) -> str:
        """获取访问令牌"""
        # 如果令牌未过期，直接返回
        if self.token and time.time() < self.token_expire_time:
            return self.token

        # 获取新令牌
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.secret_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            result = response.json()

            if "access_token" not in result:
                logger.error(f"获取token失败: {result}")
                raise Exception(f"获取token失败: {result}")

            self.token = result["access_token"]
            # 令牌有效期通常是30天，这里设置为29天以确保安全
            self.token_expire_time = time.time() + result.get("expires_in", 2592000) - 86400

            logger.info("成功获取百度语音识别访问令牌")
            return self.token

        except Exception as e:
            logger.error(f"获取访问令牌失败: {e}")
            raise

    def recognize_audio(
        self,
        audio_file_path: str,
        file_format: str = "wav",
        rate: int = 16000,
        dev_pid: int = 1537
    ) -> Dict:
        """
        识别音频文件

        Args:
            audio_file_path: 音频文件路径
            file_format: 音频格式（pcm, wav, amr, m4a）
            rate: 采样率（16000, 8000）
            dev_pid: 语言模型ID

        Returns:
            识别结果字典
        """
        # 读取音频文件
        try:
            with open(audio_file_path, 'rb') as f:
                audio_data = f.read()
        except Exception as e:
            logger.error(f"读取音频文件失败 {audio_file_path}: {e}")
            raise

        # Base64编码
        audio_base64 = base64.b64encode(audio_data).decode('utf-8')

        # 获取访问令牌
        access_token = self.get_access_token()

        # 调用语音识别API
        url = "https://vop.baidubce.com/server_api"

        # 准备请求头
        headers = {
            'Content-Type': 'application/json'
        }

        # 准备请求体
        payload = {
            "format": file_format,
            "rate": rate,
            "channel": 1,  # 单声道
            "cuid": hashlib.md5(self.api_key.encode()).hexdigest()[:16],
            "token": access_token,
            "dev_pid": dev_pid,
            "speech": audio_base64,
            "len": len(audio_data)
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            result = response.json()

            logger.info(f"音频识别完成: {audio_file_path}")
            return result

        except Exception as e:
            logger.error(f"语音识别API调用失败: {e}")
            if hasattr(e, 'response') and e.response:
                logger.error(f"响应内容: {e.response.text}")
            raise

    def extract_text_from_result(self, result: Dict) -> str:
        """从识别结果中提取文本"""
        if result.get("err_no") != 0:
            error_msg = result.get("err_msg", "未知错误")
            raise Exception(f"语音识别失败: {error_msg}")

        # 提取所有识别结果
        if "result" in result and result["result"]:
            return "".join(result["result"])
        else:
            return ""


class AudioToTextSkill:
    """音频转文字Skill主类"""

    def __init__(
        self,
        api_key: str,
        secret_key: str,
        audio_dir: str = "./音频",
        text_dir: str = "./文字",
        file_format: str = "wav",
        rate: int = 16000,
        dev_pid: int = 1537
    ):
        self.api_key = api_key
        self.secret_key = secret_key
        self.audio_dir = Path(audio_dir).resolve()
        self.text_dir = Path(text_dir).resolve()
        self.file_format = file_format
        self.rate = rate
        self.dev_pid = dev_pid

        # 创建输入/输出目录（与 .claude 同级的 audio_files / text_files 等）
        self.audio_dir.mkdir(parents=True, exist_ok=True)
        self.text_dir.mkdir(parents=True, exist_ok=True)

        # 初始化识别器
        self.recognizer = BaiduSpeechRecognizer(api_key, secret_key)

        logger.info(f"音频目录: {self.audio_dir}")
        logger.info(f"文字目录: {self.text_dir}")
        logger.info(f"长音频处理支持: {'可用' if LONG_AUDIO_SUPPORT else '不可用'}")

    def get_audio_files(self) -> List[Path]:
        """获取音频目录中的所有音频文件"""
        if not self.audio_dir.exists():
            logger.error(f"音频目录不存在: {self.audio_dir}")
            return []

        # 支持的音频文件扩展名（不区分大小写）
        extensions = ['.wav', '.pcm', '.amr', '.m4a', '.mp3', '.aac']

        # 使用集合避免重复
        audio_files_set = set()
        for ext in extensions:
            # 使用glob模式匹配不区分大小写的扩展名
            for pattern in [f"*{ext}", f"*{ext.upper()}"]:
                for file in self.audio_dir.glob(pattern):
                    audio_files_set.add(file)

        # 转换为列表并按修改时间排序
        audio_files = sorted(audio_files_set, key=lambda x: x.stat().st_mtime)

        logger.info(f"找到 {len(audio_files)} 个音频文件")
        return audio_files

    def _needs_long_audio_processing(self, audio_file: Path) -> bool:
        """检查是否需要长音频处理"""
        if not LONG_AUDIO_SUPPORT:
            return False

        try:
            # 检查文件大小（大于4MB需要长音频处理）
            file_size_mb = audio_file.stat().st_size / (1024 * 1024)
            if file_size_mb > 4.0:
                logger.info(f"文件大小 {file_size_mb:.2f}MB > 4MB，需要长音频处理")
                return True

            # 检查音频格式（如果不是16000/8000Hz单声道，可能需要转换）
            try:
                audio_info = get_audio_info(str(audio_file))
                sample_rate = audio_info['sample_rate']
                channels = audio_info['channels']

                if sample_rate not in [16000, 8000] or channels != 1:
                    logger.info(f"音频格式 {sample_rate}Hz {channels}ch 不符合API要求，需要转换")
                    return True

                # 检查时长（大于30秒需要分割）
                duration = audio_info['duration']
                if duration > 30:
                    logger.info(f"音频时长 {duration:.2f}s > 30s，需要分割")
                    return True

            except Exception as e:
                logger.warning(f"获取音频信息失败 {audio_file.name}: {e}，尝试直接处理")
                # 如果无法获取音频信息，尝试直接处理
                return False

        except Exception as e:
            logger.warning(f"检查长音频处理需求失败 {audio_file.name}: {e}")

        return False

    def process_audio_file(self, audio_file: Path) -> Tuple[bool, str]:
        """处理单个音频文件"""
        logger.info(f"处理音频文件: {audio_file.name}")

        # 检查是否需要长音频处理
        if self._needs_long_audio_processing(audio_file) and LONG_AUDIO_SUPPORT:
            logger.info(f"使用长音频处理流程: {audio_file.name}")
            try:
                success, result = process_long_audio(
                    self.recognizer,
                    audio_file,
                    self.text_dir,
                    segment_duration=30.0
                )

                if success:
                    # 长音频处理成功，result是文本
                    # 注意：process_long_audio已经保存了文件，我们只需要返回结果
                    return True, result
                else:
                    # 长音频处理失败，result是错误信息
                    # 尝试使用标准方法作为后备
                    logger.warning(f"长音频处理失败，尝试标准方法: {result}")
            except Exception as e:
                logger.error(f"长音频处理异常: {e}")
                # 继续尝试标准方法

        # 标准处理流程
        try:
            # 识别音频
            result = self.recognizer.recognize_audio(
                str(audio_file),
                file_format=self.file_format,
                rate=self.rate,
                dev_pid=self.dev_pid
            )

            # 提取文本
            text = self.recognizer.extract_text_from_result(result)

            # 保存文本
            output_file = self.text_dir / f"{audio_file.stem}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text)

            # 同时保存原始JSON结果（可选）
            json_file = self.text_dir / f"{audio_file.stem}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            logger.info(f"识别完成: {audio_file.name} -> {output_file.name}")
            logger.info(f"识别文本: {text[:100]}..." if len(text) > 100 else f"识别文本: {text}")

            return True, text

        except Exception as e:
            logger.error(f"处理文件失败 {audio_file.name}: {e}")

            # 如果标准方法失败，且错误是"content len too long"，尝试长音频处理作为后备
            if LONG_AUDIO_SUPPORT and "content len too long" in str(e):
                logger.info(f"检测到'content len too long'错误，尝试长音频处理")
                try:
                    success, result = process_long_audio(
                        self.recognizer,
                        audio_file,
                        self.text_dir,
                        segment_duration=30.0
                    )
                    return success, result
                except Exception as long_audio_error:
                    logger.error(f"长音频处理后备也失败: {long_audio_error}")
                    return False, f"{e} (长音频处理后备也失败: {long_audio_error})"

            return False, str(e)

    def run(self) -> Dict[str, any]:
        """运行音频转文字任务"""
        logger.info("开始音频转文字任务")

        # 获取音频文件
        audio_files = self.get_audio_files()
        if not audio_files:
            return {
                "success": False,
                "message": "未找到音频文件",
                "processed": 0,
                "failed": 0
            }

        # 处理每个文件
        results = []
        processed_count = 0
        failed_count = 0

        for audio_file in audio_files:
            success, result = self.process_audio_file(audio_file)

            if success:
                processed_count += 1
                results.append({
                    "file": audio_file.name,
                    "status": "success",
                    "text": result
                })
            else:
                failed_count += 1
                results.append({
                    "file": audio_file.name,
                    "status": "failed",
                    "error": result
                })

        # 生成报告
        report = {
            "success": True,
            "message": f"处理完成，成功: {processed_count}, 失败: {failed_count}",
            "processed": processed_count,
            "failed": failed_count,
            "total": len(audio_files),
            "results": results
        }

        logger.info(f"任务完成: {report['message']}")

        return report


def main():
    """主函数 - 从命令行参数或环境变量获取配置"""
    import argparse

    parser = argparse.ArgumentParser(description='百度智能云语音识别音频转文字')

    # 添加参数
    parser.add_argument('--api-key', help='百度API Key', default=os.getenv('BAIDU_API_KEY'))
    parser.add_argument('--secret-key', help='百度Secret Key', default=os.getenv('BAIDU_SECRET_KEY'))
    parser.add_argument(
        '--audio-dir',
        help='音频目录（未指定时自动定位到与 .claude 同级的 audio_files）',
        default=None,
    )
    parser.add_argument(
        '--text-dir',
        help='文字输出目录（未指定时自动定位到与 .claude 同级的 text_files）',
        default=None,
    )
    parser.add_argument('--file-format', help='音频文件格式', default='wav')
    parser.add_argument('--rate', type=int, help='采样率', default=16000)
    parser.add_argument('--dev-pid', type=int, help='语言模型ID', default=1537)
    parser.add_argument('--config', help='配置文件路径')

    args = parser.parse_args()

    audio_dir: Optional[str] = None
    text_dir: Optional[str] = None

    # 如果提供了配置文件，从配置文件读取
    if args.config and os.path.exists(args.config):
        with open(args.config, 'r', encoding='utf-8') as f:
            config = json.load(f)

        api_key = config.get('api_key') or args.api_key
        secret_key = config.get('secret_key') or args.secret_key
        audio_dir = _strip_nonempty(config.get('audio_dir'))
        text_dir = _strip_nonempty(config.get('text_dir'))
        file_format = config.get('file_format', args.file_format)
        rate = config.get('rate', args.rate)
        dev_pid = config.get('dev_pid', args.dev_pid)
    else:
        api_key = args.api_key
        secret_key = args.secret_key
        file_format = args.file_format
        rate = args.rate
        dev_pid = args.dev_pid

    # 命令行覆盖配置文件中的目录
    if args.audio_dir is not None:
        audio_dir = args.audio_dir
    if args.text_dir is not None:
        text_dir = args.text_dir

    # 未配置或为空时：自动解析为「含 .claude 的目录」下的 audio_files / text_files
    default_audio, default_text = resolve_default_audio_text_dirs()
    if audio_dir is None:
        audio_dir = str(default_audio)
    if text_dir is None:
        text_dir = str(default_text)

    # 检查必要参数
    if not api_key or not secret_key:
        logger.error("缺少API Key或Secret Key，请通过参数或环境变量提供")
        parser.print_help()
        sys.exit(1)

    # 运行技能
    skill = AudioToTextSkill(
        api_key=api_key,
        secret_key=secret_key,
        audio_dir=audio_dir,
        text_dir=text_dir,
        file_format=file_format,
        rate=rate,
        dev_pid=dev_pid
    )

    result = skill.run()

    # 输出结果
    try:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except UnicodeEncodeError:
        # Windows控制台编码问题，使用ASCII安全输出
        print(json.dumps(result, ensure_ascii=True, indent=2))

    # 根据结果返回适当的退出码
    if result.get("success") and result.get("failed", 0) == 0:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()