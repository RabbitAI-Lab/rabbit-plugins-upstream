#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sugon-Scnet 图片转 Word 服务技能主脚本
接收命令行参数：ocrType filePath
输出：转换后的 Word 文件下载地址
"""

import os
import sys
import json
import time
import requests
import mimetypes
from pathlib import Path

# 获取技能根目录（脚本所在目录的上一级）
SKILL_ROOT = Path(__file__).parent.parent.absolute()
ENV_FILE = SKILL_ROOT / "config" / ".env"

# 重试配置
MAX_RETRIES = 3
RETRY_BACKOFF_FACTOR = 2
INITIAL_RETRY_DELAY = 1

# 默认轮询配置
DEFAULT_POLL_INTERVAL = 5
DEFAULT_MAX_POLL_TIME = 600

SUPPORTED_TYPES = {
    "IMAGE_TO_WORD": {"input": "image", "output": ".docx"},
}


def load_config():
    """从 .env 文件加载配置，若文件不存在则抛出友好错误"""
    config_from_env = {}
    for key in ["SCNET_API_KEY", "SCNET_API_BASE", "SCNET_POLL_INTERVAL", "SCNET_MAX_POLL_TIME"]:
        value = os.environ.get(key)
        if value:
            config_from_env[key] = value

    if not ENV_FILE.exists() and "SCNET_API_KEY" not in config_from_env:
        error_msg = (
            "\n===============================================\n"
            "Scnet 文档转换配置文件不存在\n"
            "===============================================\n"
            "⚠️ 安全警告：切勿在聊天中直接粘贴 API Key！\n\n"
            "请按以下步骤安全配置：\n\n"
            "1. 申请 Scnet API Token：\n"
            "   访问 https://www.scnet.cn 注册并获取密钥\n\n"
            "2. 配置 Token（选择一种方式）：\n"
            "   a) 环境变量（推荐）：\n"
            "      export SCNET_API_KEY='你的密钥'\n"
            "   b) 配置文件：\n"
            f"      mkdir -p {SKILL_ROOT}/config\n"
            f"      echo 'SCNET_API_KEY=你的密钥' > {ENV_FILE}\n"
            f"      chmod 600 {ENV_FILE}\n"
            "\n配置完成后重新运行。"
        )
        sys.exit(error_msg)

    config = dict(config_from_env)
    if ENV_FILE.exists():
        with open(ENV_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    # 环境变量优先级高于配置文件
                    if key not in config:
                        config[key] = value

    # 检查必要配置
    api_key = config.get('SCNET_API_KEY', '')
    if not api_key or api_key == 'your_scnet_api_key_here':
        error_msg = (
            "\n===============================================\n"
            "Scnet API Key 未配置\n"
            "===============================================\n"
            "请按以下步骤配置：\n\n"
            "1. 申请 Scnet API Token：\n"
            "   访问 https://www.scnet.cn 注册并获取密钥\n\n"
            "2. 配置 Token：\n"
            f"   编辑 {ENV_FILE}\n"
            "   设置 SCNET_API_KEY=你的密钥\n"
        )
        sys.exit(error_msg)

    config.setdefault('SCNET_API_BASE', 'https://api.scnet.cn/api/llm/v1')

    try:
        config.setdefault('SCNET_POLL_INTERVAL', str(DEFAULT_POLL_INTERVAL))
        config.setdefault('SCNET_MAX_POLL_TIME', str(DEFAULT_MAX_POLL_TIME))
        config['SCNET_POLL_INTERVAL'] = int(config['SCNET_POLL_INTERVAL'])
        config['SCNET_MAX_POLL_TIME'] = int(config['SCNET_MAX_POLL_TIME'])
    except ValueError:
        sys.exit("错误: SCNET_POLL_INTERVAL 和 SCNET_MAX_POLL_TIME 必须为整数")

    return config


def handle_http_error(response, action="请求"):
    """根据 HTTP 状态码输出友好错误信息"""
    if response.status_code in (401, 403):
        error_msg = (
            "\n===============================================\n"
            "Scnet API Token 无效或已过期\n"
            "===============================================\n"
            f"HTTP 状态码: {response.status_code}\n\n"
            "⚠️ 安全警告：请勿在聊天中直接粘贴 API Key！\n\n"
            "解决方法（二选一）：\n"
            "1. 环境变量方式：\n"
            "   export SCNET_API_KEY='你的新Token'\n"
            "2. 配置文件方式：\n"
            f"   echo 'SCNET_API_KEY=你的新Token' > {ENV_FILE}\n"
            f"   chmod 600 {ENV_FILE}\n"
            "\n更新后重新运行。"
        )
        sys.exit(error_msg)
    sys.exit(f"错误: {action}失败，HTTP {response.status_code}: {response.text}")


def submit_task(ocr_type, file_path, config, retry_count=0):
    """提交文档转换任务，返回 task_id"""
    api_base = config['SCNET_API_BASE']
    api_key = config['SCNET_API_KEY']
    url = f"{api_base}/doc/convert/task"

    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'

    try:
        with open(file_path, 'rb') as f:
            files = {
                'file': (os.path.basename(file_path), f, mime_type)
            }
            data = {
                'ocr_type': ocr_type,
            }
            response = requests.post(url, headers=headers, data=data, files=files, timeout=60)
    except Exception as e:
        sys.exit(f"网络请求失败: {str(e)}")

    if response.status_code == 429:
        if retry_count >= MAX_RETRIES:
            sys.exit(f"错误: 请求被限流 (429)，已达到最大重试次数 {MAX_RETRIES}。请稍后再试。")
        retry_after = INITIAL_RETRY_DELAY * (RETRY_BACKOFF_FACTOR ** retry_count)
        try:
            error_data = response.json()
            if 'retry_after' in error_data:
                retry_after = int(error_data['retry_after'])
        except Exception:
            pass
        sys.stderr.write(
            f"⚠️ 请求过于频繁，等待 {retry_after} 秒后重试... (第 {retry_count + 1}/{MAX_RETRIES} 次重试)\n")
        time.sleep(retry_after)
        return submit_task(ocr_type, file_path, config, retry_count + 1)

    if response.status_code != 200:
        handle_http_error(response, "提交转换任务")

    try:
        result = response.json()
    except Exception:
        sys.exit(f"错误: 响应不是有效的 JSON: {response.text}")

    if result.get('code') != '0':
        sys.exit(f"错误: API 错误 {result.get('code')}: {result.get('msg')}")

    output = result.get('data', {}).get('output', {})
    task_id = output.get('task_id')
    if not task_id:
        sys.exit(f"错误: 未获取到 task_id，响应内容: {json.dumps(result, ensure_ascii=False)}")

    return task_id


def query_results(task_ids, config, retry_count=0):
    """查询任务状态，返回任务结果列表"""
    api_base = config['SCNET_API_BASE']
    api_key = config['SCNET_API_KEY']
    url = f"{api_base}/ocrdoc/result"

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {"task_ids": task_ids}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
    except Exception as e:
        sys.exit(f"网络请求失败: {str(e)}")

    if response.status_code == 429:
        if retry_count >= MAX_RETRIES:
            sys.exit(f"错误: 查询被限流 (429)，已达到最大重试次数 {MAX_RETRIES}。请稍后再试。")
        retry_after = INITIAL_RETRY_DELAY * (RETRY_BACKOFF_FACTOR ** retry_count)
        try:
            error_data = response.json()
            if 'retry_after' in error_data:
                retry_after = int(error_data['retry_after'])
        except Exception:
            pass
        sys.stderr.write(
            f"⚠️ 查询过于频繁，等待 {retry_after} 秒后重试... (第 {retry_count + 1}/{MAX_RETRIES} 次重试)\n")
        time.sleep(retry_after)
        return query_results(task_ids, config, retry_count + 1)

    if response.status_code != 200:
        handle_http_error(response, "查询任务状态")

    try:
        result = response.json()
    except Exception:
        sys.exit(f"错误: 响应不是有效的 JSON: {response.text}")

    if result.get('code') != '0':
        sys.exit(f"错误: API 错误 {result.get('code')}: {result.get('msg')}")

    return result.get('data', [])


def poll_task_until_done(task_id, config):
    """轮询任务直到完成、失败或超时"""
    poll_interval = config['SCNET_POLL_INTERVAL']
    max_poll_time = config['SCNET_MAX_POLL_TIME']
    start_time = time.time()

    while True:
        elapsed = time.time() - start_time
        if elapsed > max_poll_time:
            sys.exit(f"错误: 等待任务 {task_id} 完成超时（{max_poll_time} 秒）")

        results = query_results([task_id], config)
        task_output = None
        for item in results:
            output = item.get('output', {})
            if output.get('task_id') == task_id:
                task_output = output
                break

        if task_output is None:
            sys.exit(f"错误: 未在响应中找到任务 {task_id} 的状态信息")

        status = task_output.get('task_status')
        if status == 'succeeded':
            return task_output
        elif status == 'failed':
            error_code = task_output.get('error_code', 'unknown')
            error_message = task_output.get('error_message', '未知错误')
            sys.exit(f"错误: 任务执行失败 [{error_code}] {error_message}")
        elif status in ('pending', 'running'):
            sys.stderr.write(f"⏳ 任务 {task_id} 状态: {status}，已等待 {int(elapsed)} 秒，继续轮询...\n")
            time.sleep(poll_interval)
        else:
            sys.exit(f"错误: 任务 {task_id} 未知状态: {status}")


def main():
    if len(sys.argv) != 3:
        print("用法: python main.py <ocrType> <filePath>")
        print("ocrType 可选值: IMAGE_TO_WORD")
        sys.exit(1)

    ocr_type = sys.argv[1]
    file_path = sys.argv[2]

    if ocr_type not in SUPPORTED_TYPES:
        sys.exit(f"错误: 不支持的 ocrType '{ocr_type}'，可选值: {', '.join(SUPPORTED_TYPES.keys())}")

    if not os.path.isfile(file_path):
        sys.exit(f"错误: 文件不存在 - {file_path}")

    config = load_config()

    sys.stderr.write(f"🚀 正在提交 {ocr_type} 转换任务: {file_path}\n")
    task_id = submit_task(ocr_type, file_path, config)
    sys.stderr.write(f"✅ 任务已提交，task_id: {task_id}\n")

    task_output = poll_task_until_done(task_id, config)

    # 输出结果
    output_payload = {
        "task_id": task_output.get("task_id"),
        "task_status": task_output.get("task_status"),
        "submit_time": task_output.get("submit_time"),
        "end_time": task_output.get("end_time"),
        "results": task_output.get("results", []),
    }
    print(json.dumps(output_payload, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
