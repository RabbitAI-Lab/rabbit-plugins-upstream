#!/usr/bin/env python3
"""命令行入口：分析图片内容"""

import argparse
import json
import sys
from pathlib import Path

# For local import
sys.path.insert(0, str(Path(__file__).parent))

from __init__ import analyze_image, load_config, save_config, Config


def main():
    parser = argparse.ArgumentParser(
        description="Z.ai 图片理解技能：使用 Z.ai GLM-4V Vision API 分析图片",
        add_help=False  # We'll add help manually
    )
    
    # Special commands first
    parser.add_argument(
        "--init-config", action="store_true", help="创建默认配置文件并退出"
    )
    parser.add_argument(
        "--show-config", action="store_true", help="显示当前配置并退出"
    )
    parser.add_argument(
        "-h", "--help", action="store_true", help="显示帮助信息并退出"
    )
    
    # Main arguments (only required when not using special commands)
    parser.add_argument(
        "-i", "--image", help="图片路径、URL 或 Base64 Data URI"
    )
    parser.add_argument(
        "-p", "--prompt", help="自定义提示词（覆盖配置文件中的默认值）"
    )
    parser.add_argument(
        "-c", "--config", help="配置文件路径（默认: ~/.config/zai-image-understanding/config.json）"
    )
    parser.add_argument(
        "-o", "--output", help="输出文件路径（默认打印到 stdout）"
    )
    parser.add_argument(
        "--save-markdown", action="store_true", help="同时保存为 Markdown 文件到 outputs 目录"
    )

    args = parser.parse_args()

    # Handle help
    if args.help:
        parser.print_help()
        return 0

    # 特殊命令处理
    if args.init_config:
        path = Path(args.config) if args.config else Path.home() / ".config" / "zai-image-understanding" / "config.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        save_config(Config(), str(path))
        print(f"默认配置已创建: {path}")
        return 0

    if args.show_config:
        config = load_config(args.config)
        print(json.dumps(config.to_dict(), indent=2, ensure_ascii=False))
        return 0

    # Validate required arguments for main functionality
    if not args.image:
        parser.error("需要提供 -i/--image 参数，或使用 --init-config / --show-config")

    # 主功能：分析图片
    result = analyze_image(
        image_path=args.image,
        prompt=args.prompt,
        config_path=args.config,
    )

    # 输出结果
    output_json = json.dumps(result, ensure_ascii=False, indent=2)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output_json, encoding="utf-8")
        print(f"结果已保存到: {output_path}")
    else:
        print(output_json)

    # 如果请求保存 markdown
    if args.save_markdown and result.get("status") == "success":
        outputs_dir = Path.home() / ".local" / "share" / "zai-image-understanding" / "outputs"
        outputs_dir.mkdir(parents=True, exist_ok=True)
        
        # 生成文件名：基于输入图片名或哈希
        from hashlib import sha256
        import time
        if args.image.startswith(("http://", "https://")):
            img_hash = sha256(args.image.encode()).hexdigest()[:8]
        elif args.image.startswith("data:image"):
            img_hash = sha256(args.image.encode()).hexdigest()[:8]
        else:
            img_name = Path(args.image).stem
            img_hash = sha256(img_name.encode()).hexdigest()[:8]
        
        timestamp = int(time.time())
        md_file = outputs_dir / f"zai_{img_hash}_{timestamp}.md"
        
        md_content = f"""# 图片理解结果

**输入图片**: {args.image}
**运行模式**: cloud (Z.ai GLM-4V)
**使用模型**: {result.get('model', 'unknown')}
**时间**: {time.ctime(timestamp)}

## 分析内容

{result.get('result', '')}

## Token 使用情况
```json
{json.dumps(result.get('tokens', {}), indent=2)}
```
"""
        md_file.write_text(md_content, encoding="utf-8")
        print(f"Markdown 已保存到: {md_file}")

    # 返回适当的退出码
    return 0 if result.get("status") == "success" else 1


if __name__ == "__main__":
    sys.exit(main())