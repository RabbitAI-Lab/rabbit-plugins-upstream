#!/usr/bin/env python3
"""
RAG 知识库自动查询脚本
用于 Hermes Skill 集成，自动调用本地 RAG API 服务
"""

import sys
import json
import subprocess
from pathlib import Path

# API 服务地址
RAG_API_URL = "http://localhost:8000/query"

def query_rag_api(query_text: str, top_k: int = 5, search_mode: str = "hybrid") -> dict:
    """
    调用本地 RAG API 进行查询
    
    Args:
        query_text: 查询文本
        top_k: 返回结果数量
        search_mode: 检索模式 (hybrid/bm25/vector)
    
    Returns:
        API 响应字典
    """
    import urllib.request
    import urllib.error
    
    # 构建请求
    data = json.dumps({
        "query": query_text,
        "top_k": top_k,
        "search_mode": search_mode
    }).encode('utf-8')
    
    req = urllib.request.Request(
        RAG_API_URL,
        data=data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        return {
            "error": f"无法连接到 RAG API 服务: {e}",
            "hint": "请确保服务已启动: uvicorn rag_api:app --host 0.0.0.0 --port 8000"
        }
    except Exception as e:
        return {
            "error": f"查询失败: {e}"
        }

def format_results(response: dict) -> str:
    """
    格式化 RAG API 响应为易读的文本
    
    Args:
        response: API 响应字典
    
    Returns:
        格式化后的文本
    """
    if "error" in response:
        return f"❌ {response['error']}\n\n💡 {response.get('hint', '')}"
    
    query = response.get('query', '')
    results = response.get('results', [])
    query_time = response.get('query_time_ms', 0)
    
    if not results:
        return f"📭 知识库中未找到与「{query}」相关的信息。"
    
    # 构建输出
    lines = []
    lines.append(f"🔍 查询: {query}")
    lines.append(f"⏱️ 耗时: {query_time:.0f}ms")
    lines.append(f"📄 找到 {len(results)} 个相关片段")
    lines.append("")
    
    for i, result in enumerate(results, 1):
        content = result.get('content', '').strip()
        source = result.get('source', 'unknown')
        hybrid_score = result.get('hybrid_score', 0)
        
        # 提取问题和答案
        lines.append(f"{'='*60}")
        lines.append(f"📄 结果 #{i}")
        lines.append(f"{'='*60}")
        
        # 只显示内容的前 300 字符，避免过长
        if len(content) > 300:
            content = content[:300] + "..."
        lines.append(content)
        lines.append("")
    
    return "\n".join(lines)

def is_rag_query(query: str) -> bool:
    """
    判断用户查询是否适合用 RAG 知识库回答
    
    Args:
        query: 用户查询文本
    
    Returns:
        是否适合用 RAG 回答
    """
    # 香港身份/签证相关关键词
    hk_keywords = [
        '香港', '身份', '签证', '优才', '专才', '高才', '高才通',
        '续签', '永居', '永久居民', '受养人', '入境', '逗留',
        'iang', 'qmas', 'asmpt', 'ttps'
    ]
    
    # 公司制度相关关键词
    company_keywords = [
        '公司制度', '考勤', '请假', '报销', '福利', '加班',
        '年假', '病假', '事假', '调休', '迟到', '早退'
    ]
    
    # 技术相关关键词
    tech_keywords = [
        'python', '机器学习', '算法', '编程', '人工智能',
        '深度学习', '神经网络', '数据科学'
    ]
    
    query_lower = query.lower()
    
    # 检查是否包含任何关键词
    all_keywords = hk_keywords + company_keywords + tech_keywords
    return any(kw in query_lower for kw in all_keywords)

def main():
    """主函数：命令行调用"""
    if len(sys.argv) < 2:
        print("用法: python rag_query_auto.py \"查询文本\"")
        print("示例: python rag_query_auto.py \"香港专才计划申请条件\"")
        sys.exit(1)
    
    query_text = sys.argv[1]
    
    # 检查是否适合 RAG 查询
    if not is_rag_query(query_text):
        print(f"💡 该查询似乎不适合用知识库回答，直接回答即可。")
        sys.exit(0)
    
    # 调用 RAG API
    print(f"🔍 正在查询知识库: {query_text}")
    response = query_rag_api(query_text)
    
    # 格式化输出
    print(format_results(response))

if __name__ == "__main__":
    main()
