#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rag_synthesize —— 检索增强的"生成"：基于 top-k 上下文产出带引用的回答。

两种模式：
  1) 离线抽取式（默认）：从检索到的分块中抽取与问题最相关的句子，拼接成带 [n] 引用的结构化回答。无需任何外部服务。
  2) LLM 生成式（可选）：若环境变量 OPENAI_API_KEY 与 OPENAI_BASE_URL 同时设置，
     调用兼容 OpenAI 的接口，把检索上下文作为 evidence 注入 prompt，产出生成式回答。
     使用标准库 urllib 实现，无第三方依赖。

用法：
  python rag_synthesize.py --index <index.json> --question "..." [--topk 5] [--out answer.md]
"""
import os, sys, json, argparse, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from raglib import tokenize, tfidf_vector, cosine


def load_index(path):
    d = json.load(open(path, encoding="utf-8"))
    chunks = d["chunks"]
    vecs = d.get("vectors", [])
    for c, v in zip(chunks, vecs):
        c["vec"] = v
    return d, chunks


def retrieve(d, chunks, question, topk):
    qvec = tfidf_vector(tokenize(question), d["idf"])
    scored = [(cosine(qvec, c.get("vec", {})), c) for c in chunks]
    scored = [(s, c) for s, c in scored if s > 0]
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:topk]


def extractive_answer(question, hits):
    """离线抽取式：挑选含有问题关键词的句子，按相关度排序拼接。"""
    qterms = set(tokenize(question))
    sentences = []
    for rank, (score, c) in enumerate(hits, 1):
        for sent in [s.strip() for s in c["text"].replace("\n", "。").split("。") if s.strip()]:
            st = set(tokenize(sent))
            overlap = len(qterms & st)
            if overlap == 0:
                continue
            sentences.append((overlap, rank, score, sent, c["doc"]))
    sentences.sort(key=lambda x: (x[0], x[2]), reverse=True)
    seen = set()
    picked = []
    for overlap, rank, score, sent, doc in sentences:
        key = sent[:30]
        if key in seen:
            continue
        seen.add(key)
        picked.append(f"[{rank}] {sent}（来源：{doc}）")
        if len(picked) >= 5:
            break
    return picked


def llm_generate(question, hits):
    """调用兼容 OpenAI 的接口做生成式回答。失败则回退抽取式。"""
    key = os.environ.get("OPENAI_API_KEY")
    base = os.environ.get("OPENAI_BASE_URL")
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    if not (key and base):
        return None
    evidence = "\n\n".join(f"[{i+1}] ({c['doc']})\n{t['text']}" for i, (s, c) in enumerate(hits))
    prompt = (
        "你是严谨的检索增强问答助手。只依据下面的【证据】回答，"
        "并在句末用 [n] 标注引用编号。若证据不足，明确说不知道。\n\n"
        f"【证据】\n{evidence}\n\n【问题】\n{question}\n\n【回答】"
    )
    payload = {"model": model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}
    req = urllib.request.Request(
        base.rstrip("/") + "/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"⚠️ LLM 调用失败，回退抽取式：{e}")
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True)
    ap.add_argument("--question", required=True)
    ap.add_argument("--topk", type=int, default=5)
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    d, chunks = load_index(args.index)
    hits = retrieve(d, chunks, args.question, args.topk)

    answer = llm_generate(args.question, hits)
    mode = "LLM生成式"
    if not answer:
        mode = "离线抽取式"
        picked = extractive_answer(args.question, hits)
        answer = "\n".join(picked) if picked else "（检索到的证据中未找到与问题直接相关的内容）"

    refs = "\n".join(f"[{i+1}] {c['doc']}" for i, (s, c) in enumerate(hits))
    md = f"# 检索增强回答（{mode}）\n\n**问题：** {args.question}\n\n**回答：**\n{answer}\n\n## 引用来源\n{refs}\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"✅ {mode}回答已写入 {args.out}")
    else:
        print(md)
    print(f"检索命中 {len(hits)} 条，模式={mode}")


if __name__ == "__main__":
    main()
