#!/usr/bin/env python3
"""
知识库向量化索引脚本
将 knowledge 目录下的文档转换为向量并存储到 Chroma 数据库

使用方法:
    python index_knowledge.py [--knowledge-dir ./knowledge] [--output-dir ./vectorstore]
"""

import os
import sys
import argparse
import json
from pathlib import Path

# Windows 控制台 UTF-8 支持
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# 检查依赖
try:
    from langchain_community.document_loaders import (
        DirectoryLoader,
        PyPDFLoader,
        UnstructuredMarkdownLoader,
        UnstructuredWordDocumentLoader,
    )
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores import Chroma
    from langchain_community.embeddings import HuggingFaceEmbeddings
    print("✓ LangChain 依赖已加载")
except ImportError as e:
    print(f"✗ 缺少依赖：{e}")
    print("\n请安装必要的包:")
    print("  pip install langchain langchain-community chromadb pypdf unstructured python-docx")
    sys.exit(1)

# 混合检索模块
try:
    from hybrid_retriever import HybridRetriever
    HYBRID_AVAILABLE = True
except ImportError:
    HYBRID_AVAILABLE = False
    print("⚠️  混合检索模块未加载，将仅使用向量检索")
    print("   如需混合检索，请确保 hybrid_retriever.py 在同目录")


def create_embeddings():
    """创建 Embedding 模型实例 - 使用 BGE-M3"""
    print("正在加载 Embedding 模型 (BAAI/bge-m3)...")
    
    from transformers import AutoTokenizer, AutoModel
    import torch
    
    tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-m3")
    model = AutoModel.from_pretrained("BAAI/bge-m3")
    model.eval()
    
    class BGEM3Embeddings:
        def __init__(self, model, tokenizer):
            self.model = model
            self.tokenizer = tokenizer
        
        def embed_documents(self, texts):
            embeddings = []
            with torch.no_grad():
                for text in texts:
                    inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
                    outputs = self.model(**inputs)
                    attention_mask = inputs['attention_mask']
                    last_hidden = outputs.last_hidden_state
                    mask_expanded = attention_mask.unsqueeze(-1).expand(last_hidden.size()).float()
                    sum_embeddings = torch.sum(last_hidden * mask_expanded, 1)
                    sum_mask = torch.clamp(mask_expanded.sum(1), min=1e-9)
                    embedding = (sum_embeddings / sum_mask).squeeze().numpy()
                    embeddings.append(embedding)
            return embeddings
        
        def embed_query(self, text):
            return self.embed_documents([text])[0]
    
    return BGEM3Embeddings(model, tokenizer)


def load_documents(knowledge_dir: str):
    """加载知识库目录下的所有文档"""
    knowledge_path = Path(knowledge_dir)
    
    if not knowledge_path.exists():
        raise FileNotFoundError(f"知识库目录不存在：{knowledge_dir}")
    
    print(f"正在扫描知识库目录：{knowledge_path.absolute()}")
    
    # 统计文件
    files_found = {
        'pdf': 0, 'md': 0, 'txt': 0, 'docx': 0, 'xlsx': 0
    }
    
    for ext in ['**/*.pdf', '**/*.md', '**/*.txt', '**/*.docx', '**/*.xlsx']:
        count = len(list(knowledge_path.glob(ext)))
        files_found[ext.strip('**/*.')] = count
    
    total = sum(files_found.values())
    print(f"发现文件总数：{total}")
    for ext, count in files_found.items():
        if count > 0:
            print(f"  - .{ext}: {count} 个")
    
    # 加载文档
    documents = []
    
    # 加载 PDF
    pdf_files = list(knowledge_path.glob("**/*.pdf"))
    if pdf_files:
        print(f"\n正在加载 {len(pdf_files)} 个 PDF 文件...")
        for pdf_file in pdf_files:
            try:
                loader = PyPDFLoader(str(pdf_file))
                docs = loader.load()
                for doc in docs:
                    doc.metadata['source'] = str(pdf_file.relative_to(knowledge_path))
                documents.extend(docs)
                print(f"  ✓ {pdf_file.relative_to(knowledge_path)}")
            except Exception as e:
                print(f"  ✗ {pdf_file.name}: {e}")
    
    # 加载 Markdown
    md_files = list(knowledge_path.glob("**/*.md"))
    if md_files:
        print(f"\n正在加载 {len(md_files)} 个 Markdown 文件...")
        for md_file in md_files:
            try:
                loader = UnstructuredMarkdownLoader(str(md_file))
                docs = loader.load()
                for doc in docs:
                    doc.metadata['source'] = str(md_file.relative_to(knowledge_path))
                documents.extend(docs)
                print(f"  ✓ {md_file.relative_to(knowledge_path)}")
            except Exception as e:
                print(f"  ✗ {md_file.name}: {e}")
    
    # 加载 TXT
    txt_files = list(knowledge_path.glob("**/*.txt"))
    if txt_files:
        print(f"\n正在加载 {len(txt_files)} 个 TXT 文件...")
        for txt_file in txt_files:
            try:
                loader = DirectoryLoader(
                    str(txt_file.parent),
                    glob=str(txt_file.name),
                    loader_cls=UnstructuredMarkdownLoader
                )
                docs = loader.load()
                documents.extend(docs)
                print(f"  ✓ {txt_file.relative_to(knowledge_path)}")
            except Exception as e:
                print(f"  ✗ {txt_file.name}: {e}")
    
    # 加载 Word 文档
    docx_files = list(knowledge_path.glob("**/*.docx"))
    if docx_files:
        print(f"\n正在加载 {len(docx_files)} 个 Word 文档...")
        for docx_file in docx_files:
            try:
                loader = UnstructuredWordDocumentLoader(str(docx_file))
                docs = loader.load()
                for doc in docs:
                    doc.metadata['source'] = str(docx_file.relative_to(knowledge_path))
                documents.extend(docs)
                print(f"  ✓ {docx_file.relative_to(knowledge_path)}")
            except Exception as e:
                print(f"  ✗ {docx_file.name}: {e}")
    
    print(f"\n✓ 成功加载 {len(documents)} 个文档片段")
    return documents, knowledge_path


def split_documents(documents, chunk_size=500, chunk_overlap=50):
    """将文档分割为小块"""
    print(f"\n正在进行文本分块 (chunk_size={chunk_size}, overlap={chunk_overlap})...")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", "。", "！", "？", "；", " ", ""]
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f"✓ 分块完成：{len(chunks)} 个片段")
    return chunks


def create_vectorstore(chunks, embeddings, output_dir: str):
    """创建向量数据库"""
    output_path = Path(output_dir)
    
    print(f"\n正在创建向量数据库...")
    print(f"存储路径：{output_path.absolute()}")
    
    # 创建或加载向量库
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(output_path),
        collection_name="knowledge_base"
    )
    
    print(f"\n✓ 向量数据库创建成功!")
    print(f"  - 文档片段：{len(chunks)} 个")
    print(f"  - 向量维度：{len(embeddings.embed_query('test'))}")
    print(f"  - 存储位置：{output_path.absolute()}")
    
    return vectorstore


def build_hybrid_index(chunks, output_dir: str, bm25_weight: float = 0.4, vector_weight: float = 0.6):
    """
    构建混合检索索引（BM25 + 向量）
    
    Args:
        chunks: 文档分块列表
        output_dir: 输出目录
        bm25_weight: BM25 检索权重
        vector_weight: 向量检索权重
    """
    if not HYBRID_AVAILABLE:
        print("\n⚠️  混合检索模块不可用，跳过 BM25 索引构建")
        return None
    
    print(f"\n🔧 构建混合检索索引...")
    print(f"   BM25 权重: {bm25_weight}, 向量权重: {vector_weight}")
    
    # 准备文档数据
    documents = []
    for i, chunk in enumerate(chunks):
        # 使用唯一 doc_id，包含 source 和 chunk_index
        source = chunk.metadata.get("source", f"chunk_{i}")
        doc_id = f"{source}#{i}"
        doc = {
            "id": doc_id,
            "content": chunk.page_content,
            "metadata": {
                **chunk.metadata,
                "chunk_index": i
            }
        }
        documents.append(doc)
    
    # 创建混合检索器并构建 BM25 索引
    retriever = HybridRetriever(
        bm25_weight=bm25_weight,
        vector_weight=vector_weight
    )
    retriever.build_bm25_index(documents)
    
    # 保存索引
    retriever.save_index(output_dir)
    
    print(f"✓ 混合检索索引构建完成")
    return retriever


def main():
    parser = argparse.ArgumentParser(description="知识库向量化索引工具 (支持混合检索)")
    parser.add_argument(
        "--knowledge-dir", "-k",
        default="./knowledge",
        help="知识库目录路径 (默认：./knowledge)"
    )
    parser.add_argument(
        "--output-dir", "-o",
        default="./vectorstore",
        help="向量数据库输出目录 (默认：./vectorstore)"
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=500,
        help="文本分块大小 (默认：500)"
    )
    parser.add_argument(
        "--chunk-overlap",
        type=int,
        default=50,
        help="文本分块重叠 (默认：50)"
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="强制重建向量库 (删除已有数据)"
    )
    # 混合检索参数
    parser.add_argument(
        "--hybrid",
        action="store_true",
        default=True,
        help="启用混合检索 (BM25 + 向量) (默认：True)"
    )
    parser.add_argument(
        "--bm25-weight",
        type=float,
        default=0.4,
        help="BM25 检索权重 (默认：0.4)"
    )
    parser.add_argument(
        "--vector-weight",
        type=float,
        default=0.6,
        help="向量检索权重 (默认：0.6)"
    )
    parser.add_argument(
        "--rrf-k",
        type=int,
        default=60,
        help="RRF 融合参数 k (默认：60)"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("📚 OpenClaw RAG 知识库索引工具 (混合检索版)")
    print("=" * 60)
    
    if args.hybrid and HYBRID_AVAILABLE:
        print("\n🔀 混合检索模式: BM25 + 向量语义检索")
    else:
        print("\n📊 纯向量检索模式")
    
    # 检查是否强制重建
    output_path = Path(args.output_dir)
    if output_path.exists() and args.rebuild:
        print(f"\n⚠️  检测到已有向量库，正在删除...")
        import shutil
        shutil.rmtree(output_path)
        print("✓ 已清理旧数据")
    elif output_path.exists():
        print(f"\n⚠️  检测到已有向量库：{output_path.absolute()}")
        print("   如需重建，请添加 --rebuild 参数")
        print("   本次将在现有基础上追加索引")
    
    try:
        # 1. 加载文档
        documents, knowledge_path = load_documents(args.knowledge_dir)
        
        if not documents:
            print("\n✗ 未找到任何可索引的文档!")
            print("   支持格式：.pdf, .md, .txt, .docx")
            sys.exit(1)
        
        # 2. 创建 Embedding 模型
        embeddings = create_embeddings()
        
        # 3. 分割文档
        chunks = split_documents(
            documents,
            chunk_size=args.chunk_size,
            chunk_overlap=args.chunk_overlap
        )
        
        # 4. 创建向量库
        vectorstore = create_vectorstore(chunks, embeddings, args.output_dir)
        
        # 5. 构建混合检索索引（BM25）
        hybrid_retriever = None
        if args.hybrid and HYBRID_AVAILABLE:
            hybrid_retriever = build_hybrid_index(
                chunks,
                args.output_dir,
                bm25_weight=args.bm25_weight,
                vector_weight=args.vector_weight
            )
        
        # 6. 保存配置信息
        config = {
            "knowledge_dir": str(knowledge_path.absolute()),
            "vectorstore_dir": str(output_path.absolute()),
            "chunk_size": args.chunk_size,
            "chunk_overlap": args.chunk_overlap,
            "embedding_model": "BAAI/bge-m3",
            "document_count": len(documents),
            "chunk_count": len(chunks),
            "hybrid_search": {
                "enabled": args.hybrid and HYBRID_AVAILABLE,
                "bm25_weight": args.bm25_weight,
                "vector_weight": args.vector_weight,
                "rrf_k": args.rrf_k
            }
        }
        
        config_file = output_path / "index_config.json"
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        print(f"\n✓ 配置已保存：{config_file}")
        
        print("\n" + "=" * 60)
        print("✅ 索引完成！现在可以使用 RAG 进行智能检索了")
        if args.hybrid and HYBRID_AVAILABLE:
            print("   支持混合检索: --hybrid (BM25 + 向量)")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ 索引失败：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
