"""
视频文案提取工具
用法: python transcribe.py "视频链接" [模型: turbo/large-v2] [可选提示词]

环境变量:
  WHISPER_DOWNLOAD_ROOT  - Whisper 模型缓存目录（默认: 当前目录下 whisper_cache）
  VIDEO_DOWNLOAD_DIR     - 视频下载目录（默认: 当前目录）
"""
import sys
import os
import subprocess
import io

# 修复 Windows 控制台编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# 配置：优先使用环境变量，否则使用脚本所在目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WHISPER_MODEL = "large-v3"
WHISPER_CACHE = os.environ.get("WHISPER_DOWNLOAD_ROOT", os.path.join(SCRIPT_DIR, "whisper_cache"))
DOWNLOAD_DIR = os.environ.get("VIDEO_DOWNLOAD_DIR", SCRIPT_DIR)

def download_video(url):
    """用 yt-dlp 下载视频"""
    output_path = os.path.join(DOWNLOAD_DIR, "temp_video.%(ext)s")
    cmd = [
        "yt-dlp", url,
        "-o", output_path,
        "--no-check-certificates",
        "--no-update"
    ]
    print("[1/2] 正在下载视频...")
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if result.returncode != 0 and "already downloaded" not in result.stderr:
        print(f"下载失败: {result.stderr}")
        sys.exit(1)
    
    for f in os.listdir(DOWNLOAD_DIR):
        if f.startswith("temp_video."):
            filepath = os.path.join(DOWNLOAD_DIR, f)
            size_mb = os.path.getsize(filepath) / 1024 / 1024
            print(f"  下载完成: {f} ({size_mb:.1f}MB)")
            return filepath
    print("找不到下载文件")
    sys.exit(1)

def transcribe_video(video_path, prompt=None, model_name="large-v3"):
    """用 whisper 转录视频"""
    print(f"[2/2] 正在转录 (模型: {model_name})...")
    
    # 标点符号提示
    if prompt:
        init_prompt = prompt
    else:
        init_prompt = "，。！？、；：\u201c\u201d\u2018\u2019（）"
    
    cache_dir = WHISPER_CACHE.replace("\\", "/")
    video_path_escaped = video_path.replace("\\", "/")
    
    python_code = f"""
import whisper, os, sys, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
cache_dir = r'{cache_dir}'
os.environ['WHISPER_DOWNLOAD_ROOT'] = cache_dir
print('  加载模型...')
start_load = time.time()
model = whisper.load_model('{model_name}', download_root=cache_dir)
print(f'  模型加载耗时: {{time.time()-start_load:.1f}}秒')
print('  转录中...')
start_trans = time.time()
result = model.transcribe(
    r'{video_path_escaped}',
    language='zh',
    initial_prompt='''{init_prompt}''',
    temperature=0.0,
    condition_on_previous_text=False,
    word_timestamps=False
)
elapsed = time.time() - start_trans
print(f'  转录耗时: {{elapsed:.1f}}秒')
for seg in result['segments']:
    start = seg['start']
    end = seg['end']
    text = seg['text'].strip()
    if text:
        print(f'[{{start:.1f}}s-{{end:.1f}}s] {{text}}')
print('---FULLTEXT---')
print(result['text'])
"""
    result = subprocess.run(
        ["python", "-c", python_code],
        capture_output=True, text=True, encoding='utf-8', errors='replace'
    )
    
    if result.returncode != 0 and not result.stdout:
        print(f"转录失败: {result.stderr}")
        sys.exit(1)
    
    # 提取转录结果
    lines = result.stdout.strip().split('\n')
    segments = []
    full_text = ""
    in_segments = False
    in_full = False
    for line in lines:
        if '转录耗时' in line:
            in_segments = True
            continue
        if '---FULLTEXT---' in line:
            in_segments = False
            in_full = True
            continue
        if in_segments and line.startswith('['):
            segments.append(line)
        elif in_full:
            full_text += line
    
    return segments, full_text.strip()

def main():
    if len(sys.argv) < 2:
        print("用法: python transcribe.py \"视频链接\" [模型: turbo/large-v3] [可选提示词]")
        print("示例: python transcribe.py \"https://v.douyin.com/xxx/\" large-v3 \"搞笑视频\"")
        print()
        print("环境变量:")
        print(f"  WHISPER_DOWNLOAD_ROOT = {WHISPER_CACHE} (模型缓存)")
        print(f"  VIDEO_DOWNLOAD_DIR    = {DOWNLOAD_DIR} (视频下载)")
        sys.exit(1)
    
    url = sys.argv[1]
    model_name = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] in ('turbo', 'large-v3') else WHISPER_MODEL
    prompt = sys.argv[3] if len(sys.argv) > 3 else None
    
    video_path = download_video(url)
    segments, full_text = transcribe_video(video_path, prompt, model_name)
    
    print()
    print("=" * 50)
    print("分段文案（带时间戳）：")
    print("=" * 50)
    for seg in segments:
        print(seg)
    print()
    print("=" * 50)
    print("完整文案：")
    print("=" * 50)
    print(full_text)
    print("=" * 50)
    print(f"\n视频已保存: {video_path}")

if __name__ == "__main__":
    main()
