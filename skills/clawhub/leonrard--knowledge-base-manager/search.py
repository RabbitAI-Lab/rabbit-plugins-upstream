#!/usr/bin/env python3
"""
知识库搜索脚本
用法: python3 search.py --query "搜索关键词" --kb-id "知识库ID" [--top-k 5]
"""
import argparse
import json
import requests
import sys

# 配置
KB_SERVICE_URL = "http://crawdxiaowu.com:3000"

def search_knowledge_base(query: str, kb_id: str = "default", top_k: int = 5) -> dict:
    """搜索知识库"""
    url = f"{KB_SERVICE_URL}/api/knowledge-bases/{kb_id}/search"
    
    data = {
        "query": query,
        "top_k": top_k
    }
    
    try:
        resp = requests.post(url, data=data, timeout=30)
        if resp.status_code == 200:
            result = resp.json()
            # API返回格式: {"success": true, "data": [...]}
            if result.get("success"):
                return {"success": True, "results": result.get("data", [])}
            return {"success": False, "error": result.get("message", "Unknown error")}
        else:
            return {"success": False, "error": f"HTTP {resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def format_results(results: list) -> str:
    """格式化搜索结果"""
    if not results:
        return "未找到相关内容"
    
    output = []
    output.append("📚 知识库搜索结果:")
    output.append("")
    
    for i, item in enumerate(results, 1):
        # 处理不同返回格式
        if isinstance(item, dict):
            content = item.get("content", "")[:300]
            source = item.get("source", "未知来源")
            score = item.get("score", 0)
        else:
            content = str(item)[:300]
            source = "未知来源"
            score = 0
        
        output.append(f"**结果 {i}** (相关性: {score:.2%})")
        output.append(f"来源: {source}")
        output.append(f"内容: {content}...")
        output.append("")
    
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="搜索知识库")
    parser.add_argument("--query", "-q", required=True, help="搜索关键词")
    parser.add_argument("--kb-id", "-k", default="default", help="知识库ID")
    parser.add_argument("--top-k", "-n", type=int, default=5, help="返回结果数量")
    
    args = parser.parse_args()
    
    result = search_knowledge_base(args.query, args.kb_id, args.top_k)
    
    if result["success"]:
        results = result.get("results", [])
        print(format_results(results))
    else:
        print(f"❌ 搜索失败: {result['error']}")
        sys.exit(1)

if __name__ == "__main__":
    main()
