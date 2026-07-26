#!/usr/bin/env python3
"""
Jimeng AI Skill 核心脚本
集成工作流：生成图片、管理服务、更新配置
"""

import json
import os
import sys
import subprocess
import time
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent.resolve()
CONFIG_FILE = SKILL_DIR / "config.json"
PID_FILE = SKILL_DIR / ".service.pid"

def load_config():
    """加载配置文件"""
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_config(config):
    """保存配置文件"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

def get_output_dir(config):
    """获取输出目录"""
    output_dir = config.get('output_dir', '~/.openclaw/workspace/output/jimeng/')
    output_path = Path(output_dir).expanduser()
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path

def check_service(port=8000):
    """检查服务是否运行"""
    try:
        req = urllib.request.Request(f"http://127.0.0.1:{port}/ping", method='GET')
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.read().decode() == 'pong'
    except:
        return False

def start_service():
    """启动服务"""
    config = load_config()
    
    if check_service(config['port']):
        print("✅ 服务已在运行")
        return True
    
    env = os.environ.copy()
    env['AUTHORIZATION'] = config['sessionid']
    
    log_file = open(SKILL_DIR / "server.log", 'a')
    
    process = subprocess.Popen(
        ['node', 'dist/index.cjs'],
        cwd=SKILL_DIR,
        env=env,
        stdout=log_file,
        stderr=subprocess.STDOUT,
        start_new_session=True
    )
    
    # 等待服务启动
    for i in range(10):
        time.sleep(1)
        if check_service(config['port']):
            config['service_pid'] = process.pid
            save_config(config)
            with open(PID_FILE, 'w') as f:
                f.write(str(process.pid))
            print(f"✅ 服务启动成功 (PID: {process.pid})")
            return True
    
    print("❌ 服务启动超时")
    return False

def stop_service():
    """停止服务"""
    if PID_FILE.exists():
        with open(PID_FILE, 'r') as f:
            pid = f.read().strip()
        try:
            subprocess.run(['kill', pid], check=False)
            PID_FILE.unlink()
            print(f"✅ 服务已停止 (PID: {pid})")
        except Exception as e:
            print(f"⚠️ 停止服务时出错: {e}")
    else:
        print("ℹ️ 服务未运行")

def generate_image(prompt, n=1, model=None, width=1024, height=1024, output_dir=None):
    """生成图片"""
    config = load_config()
    
    # 确保服务运行
    if not check_service(config['port']):
        print("🚀 服务未运行，正在启动...")
        if not start_service():
            return None
    
    # 使用默认模型
    if model is None:
        model = config.get('default_model', 'jimeng-3.0')
    
    # 获取输出目录
    if output_dir is None:
        output_dir = get_output_dir(config)
    else:
        output_dir = Path(output_dir).expanduser()
        output_dir.mkdir(parents=True, exist_ok=True)
    
    # 调用API
    api_url = f"http://127.0.0.1:{config['port']}/v1/images/generations"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {config['sessionid']}"
    }
    data = {
        'model': model,
        'prompt': prompt,
        'n': min(max(n, 1), 4),
        'width': width,
        'height': height
    }
    
    req = urllib.request.Request(
        api_url,
        data=json.dumps(data).encode(),
        headers=headers,
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        if 'Unauthorized' in error_body or e.code == 401:
            print("❌ sessionid 已过期，请使用 jimeng_update_session 更新")
        else:
            print(f"❌ API 调用失败: {error_body}")
        return None
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        return None
    
    # 下载图片
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    saved_files = []
    
    for i, img_data in enumerate(result.get('data', [])):
        img_url = img_data.get('url')
        if img_url:
            filename = f"jimeng_{timestamp}_{i+1}.png"
            filepath = output_dir / filename
            try:
                urllib.request.urlretrieve(img_url, filepath)
                saved_files.append(str(filepath))
                print(f"✅ 已保存: {filepath}")
            except Exception as e:
                print(f"⚠️ 下载失败: {e}")
    
    return {
        'files': saved_files,
        'count': len(saved_files),
        'model': model,
        'prompt': prompt
    }

def update_session(new_sessionid):
    """更新 sessionid"""
    config = load_config()
    old_sessionid = config.get('sessionid', '')[:10] + '...'
    config['sessionid'] = new_sessionid
    save_config(config)
    print(f"✅ sessionid 已更新")
    print(f"   旧: {old_sessionid}")
    print(f"   新: {new_sessionid[:10]}...")
    
    # 如果服务在运行，需要重启
    if check_service(config['port']):
        print("🔄 检测到服务运行中，正在重启以应用新配置...")
        stop_service()
        time.sleep(2)
        start_service()

def status():
    """检查状态"""
    config = load_config()
    
    print("📊 Jimeng AI 状态检查")
    print("-" * 40)
    
    # 服务状态
    if check_service(config['port']):
        print("✅ 本地服务: 运行中")
    else:
        print("❌ 本地服务: 未运行")
    
    # 配置信息
    sessionid = config.get('sessionid', '')
    print(f"🔑 sessionid: {sessionid[:15]}..." if sessionid else "❌ sessionid: 未配置")
    print(f"🎨 默认模型: {config.get('default_model', 'jimeng-3.0')}")
    print(f"📁 输出目录: {config.get('output_dir', '~/.openclaw/workspace/output/jimeng/')}")
    print(f"🔌 服务端口: {config.get('port', 8000)}")
    
    # 测试API连通性
    if check_service(config['port']):
        try:
            req = urllib.request.Request(
                f"http://127.0.0.1:{config['port']}/token",
                headers={'Authorization': f"Bearer {config['sessionid']}"},
                method='GET'
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                token_info = json.loads(resp.read().decode())
                if token_info.get('success'):
                    print("✅ API 认证: 有效")
                else:
                    print("⚠️ API 认证: 可能已过期")
        except Exception as e:
            print(f"⚠️ API 测试: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: jimeng.py <command> [args...]")
        print("")
        print("Commands:")
        print("  generate <prompt> [n] [model]    生成图片")
        print("  status                           检查状态")
        print("  start                            启动服务")
        print("  stop                             停止服务")
        print("  update-session <sessionid>       更新sessionid")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'generate':
        if len(sys.argv) < 3:
            print("Usage: jimeng.py generate <prompt> [n] [model]")
            sys.exit(1)
        prompt = sys.argv[2]
        n = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        model = sys.argv[4] if len(sys.argv) > 4 else None
        result = generate_image(prompt, n, model)
        if result:
            print(f"\n🎉 成功生成 {result['count']} 张图片")
            for f in result['files']:
                print(f"   {f}")
    
    elif command == 'status':
        status()
    
    elif command == 'start':
        start_service()
    
    elif command == 'stop':
        stop_service()
    
    elif command == 'update-session':
        if len(sys.argv) < 3:
            print("Usage: jimeng.py update-session <sessionid>")
            sys.exit(1)
        update_session(sys.argv[2])
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
