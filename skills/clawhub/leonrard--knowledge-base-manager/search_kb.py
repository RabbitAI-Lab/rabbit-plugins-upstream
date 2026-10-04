#!/usr/bin/env python3
"""
快速知识库搜索
用法: python3 search_kb.py "搜索内容" [知识库ID]
"""
import sys
import requests

KB_SERVICE_URL = "http://crawdxiaowu.com:3000"

def main():
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    kb_id = sys.argv[2] if len(sys.argv) > 2 else "test-kb"
    
    if not query:
        print("用法: python3 search_kb.py '搜索内容' [知识库ID]")
        sys.exit(1)
    
    url = f"{KB_SERVICE_URL}/api/knowledge-bases/{kb_id}/search"
    
    try:
        resp = requests.post(url, data={"query": query, "top_k": 3}, timeout=30)
        if resp.status_code == 200:
            result = resp.json()
            data = result.get("data", [])
            if data:
                print("📚 搜索结果:")
                for i, r in enumerate(data, 1):
                    content = r.get("content", "")[:200]
                    source = r.get("source", "未知")
                    score = r.get("score", 0)
                    print(f"\n{i}. [{score:.1%}] {content}...")
                    print(f"   来源: {source}")
            else:
                print("未找到相关内容")
        else:
            print(f"搜索失败: HTTP {resp.status_code}")
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    main()
