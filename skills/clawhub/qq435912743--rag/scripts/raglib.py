#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""raglib —— RAG 共享检索原语（纯 Python，无第三方依赖）。

提供：分词、TF-IDF 向量化、余弦相似度。作为 rag_index / rag_query /
rag_synthesize 的公共底座，保证可离线运行（不依赖 sentence-transformers /
faiss 等重依赖），同时保留接入稠密向量的接口位。
"""
import re, math, json

_TOKEN_RE = re.compile(r"[a-zA-Z0-9]+|[\u4e00-\u9fff]")

def tokenize(text):
    """英文/数字按词，中文按字。返回小写的 token 列表。"""
    if not text:
        return []
    toks = []
    for m in _TOKEN_RE.finditer(text.lower()):
        t = m.group(0)
        if len(t) == 1 and t.isascii():
            # 单字母英文无意义，丢弃
            continue
        toks.append(t)
    return toks


def build_idf(docs_tokens):
    """docs_tokens: list[list[token]]。返回 idf dict（平滑）。"""
    df = {}
    n = len(docs_tokens) or 1
    for toks in docs_tokens:
        seen = set(toks)
        for t in seen:
            df[t] = df.get(t, 0) + 1
    idf = {t: math.log((n + 1) / (c + 1)) + 1.0 for t, c in df.items()}
    return idf


def tfidf_vector(tokens, idf):
    """把 token 列表转成 tf-idf 稀疏向量（dict）。"""
    tf = {}
    total = len(tokens) or 1
    for t in tokens:
        tf[t] = tf.get(t, 0) + 1
    vec = {}
    for t, c in tf.items():
        idf_t = idf.get(t, math.log(2) + 1.0)
        vec[t] = (c / total) * idf_t
    return vec


def cosine(a, b):
    """两个稀疏向量的余弦相似度。"""
    if not a or not b:
        return 0.0
    # 用较短的做迭代
    if len(a) > len(b):
        a, b = b, a
    dot = sum(v * b.get(k, 0.0) for k, v in a.items())
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot / (na * nb)


def chunk_text(text, size=400, overlap=80):
    """滑动窗口分块（按 token 数）。返回 [(start, end, text)]。"""
    toks = tokenize(text)
    if not toks:
        return []
    chunks = []
    step = max(1, size - overlap)
    i = 0
    while i < len(toks):
        piece = toks[i:i + size]
        if not piece:
            break
        chunks.append(("".join(piece)))
        if i + size >= len(toks):
            break
        i += step
    return chunks
