# 混合检索测试验证指南

## 测试环境准备

```bash
# 1. 创建测试知识库
mkdir -p ~/test-knowledge

# 2. 添加测试文档（建议包含 FAQ 格式文档）
cp /path/to/your/faq_document.md ~/test-knowledge/

# 3. 构建混合检索索引
cd scripts
source venv/bin/activate
python index_knowledge.py --knowledge-dir ~/test-knowledge --output-dir ~/test-vectorstore --rebuild --hybrid
```

## 测试用例

### 测试 1：精确关键词匹配

```bash
python rag_query.py "香港身份续签一定要有工作吗" --vectorstore ~/test-vectorstore --top-k 5
```

**预期结果**：
- 混合检索应返回包含精确问题匹配的片段
- 结果应显示 BM25 和向量两种分数
- 来源应为 faq_immigration_20260618.md

### 测试 2：语义查询（无直接关键词）

```bash
python rag_query.py "没有香港工作还能续签吗" --vectorstore ~/test-vectorstore --top-k 3
```

**预期结果**：
- 混合检索应返回语义相关的内容（如"更换工作影响续签"）
- BM25 可能仍有结果（分词后匹配"续签"等词）
- 向量检索应能理解"没有工作"≈"无雇佣关系"

### 测试 3：三种模式对比

```bash
# 混合检索（默认）
python rag_query.py "优才计划申请条件" --vectorstore ~/test-vectorstore --top-k 3

# 仅 BM25
python rag_query.py "优才计划申请条件" --vectorstore ~/test-vectorstore --top-k 3 --bm25-only

# 仅向量
python rag_query.py "优才计划申请条件" --vectorstore ~/test-vectorstore --top-k 3 --vector-only
```

**预期结果**：
- 混合检索：综合两种模式的优势，排序最准确
- BM25 仅：精确匹配关键词，可能包含重复内容
- 向量仅：语义理解好，但可能缺少精确匹配

### 测试 4：口语化查询

```bash
python rag_query.py "高才通怎么申请" --vectorstore ~/test-vectorstore --top-k 3
```

**预期结果**：
- 应返回 "高端人才通行证计划" 相关内容
- 展示语义检索的同义词理解能力

## 验证指标

### 检索结果检查清单

- [ ] 混合检索返回的结果数量符合 `--top-k` 设置
- [ ] 结果中包含 `分数详情`（BM25 + 向量 + 融合分数）
- [ ] 来源文件正确显示
- [ ] 文档内容完整（无截断或空内容）
- [ ] RRF 融合结果数量合理（BM25 + 向量 - 交集）

### 常见问题排查

**问题 1：混合检索只返回 1 个结果**

**原因**：doc_id 未对齐，BM25 和向量库的 ID 格式不一致

**解决**：
```python
# 确保 index_knowledge.py 和 hybrid_retriever.py 使用相同的 doc_id 格式
# 推荐格式：f"{source}#{chunk_index}"
```

**问题 2：BM25 检索结果很多，但融合后为空**

**原因**：RRF 分数低于阈值，或 doc_id 不匹配导致融合失败

**解决**：
```bash
# 降低阈值测试
python rag_query.py "问题" --score-threshold 0.3

# 检查索引配置
cat ~/test-vectorstore/index_config.json
```

**问题 3：向量检索结果为空**

**原因**：Chroma 向量库未正确加载，或 L2 距离阈值过高

**解决**：
```bash
# 检查向量库文件
ls -la ~/test-vectorstore/chroma.sqlite3

# 重新构建索引
python index_knowledge.py --knowledge-dir ~/test-knowledge --output-dir ~/test-vectorstore --rebuild
```

## 性能基准

基于 63 个文档片段的测试数据：

| 指标 | 数值 |
|------|------|
| 索引构建时间 | ~30 秒 (CPU, BGE-M3) |
| BM25 索引大小 | ~5 KB (pickle) |
| 混合检索延迟 | ~500ms (含模型加载) |
| 纯向量检索延迟 | ~450ms |
| 纯 BM25 检索延迟 | ~50ms |

## 大规模测试建议

对于 1000+ 文档的知识库：

1. **分批索引**：避免内存溢出
2. **调整 RRF 参数**：`--rrf-k 40` 更强调头部结果
3. **增加 BM25 权重**：`--bm25-weight 0.5` 提高精确匹配优先级
4. **监控内存**：BM25 索引内存占用约为原始文本的 2-3 倍
