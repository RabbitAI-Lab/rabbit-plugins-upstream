# Architecture - Domain-Kit OWL Integration

## 分层架构

### L0: 抽象层 (phase0/)

统一数据模型，桥接 JSONL 存储和 RDF 表示。

**核心组件：**

- `models.py` — Entity, Relation, Property, EntityType 数据类
  - Entity: 统一实体表示，支持 to_jsonl_record() / from_jsonl_record() 双向转换
  - Relation: 关系边，带类型、置信度、来源
  - Property: 属性值，自动推断数据类型（string/float/int/bool/list/object）
  - EntityType: 类型元数据，支持字段验证

- `registry.py` — EntityTypeRegistry
  - 管理所有实体类型和关系类型的注册
  - 预置 10 种实体类型（含 v2.0 新增 Scenario/Parameter/Failure/PLC/WCSDevice）
  - 预置 8 种关系类型
  - 提供验证接口

- `namespace.py` — NamespaceManager
  - 管理 RDF 命名空间前缀
  - URI 生成：entity_uri(), class_uri(), relation_uri(), property_uri()
  - URI 压缩：compact_uri()
  - 绑定到 rdflib Graph

**设计决策：**
- 使用 dataclass 而非 Pydantic，减少依赖
- 命名空间基于 `https://domain-kit.midea.com/ontology/` 基础 URI
- 类型注册表支持动态扩展

### L1: 数据层 (phase1/)

JSONL ↔ RDF 双向无损转换。

**核心组件：**

- `schema_mapping.py` — SchemaMapper
  - 字段→谓词映射（name→rdfs:label, tags→skos:altLabel, etc.）
  - 关系类型→谓词映射
  - 支持自定义字段注册
  - 反向映射（谓词→字段名）

- `jsonl_to_rdf.py` — JsonlToRdfConverter
  - 读取 entities.jsonl + relations.jsonl
  - 生成 RDF 三元组：
    - 实体 → rdf:type + rdfs:label + rdfs:comment + skos:altLabel + 自定义属性
    - 关系 → 自定义谓词三元组
    - 置信度 → RDF 具体化语句（reified statement）
  - 支持文件输入和内存对象输入

- `rdf_to_jsonl.py` — RdfToJsonlConverter
  - 从 RDF 图重建 JSONL 记录
  - 反向解析所有标准谓词
  - 提取关系（基于 dk-rel: 前缀识别）
  - 支持 reified statement 中的置信度恢复

**无损保证：**
- JSONL → RDF → JSONL 保留：ID、类型、名称、标签、置信度、来源
- 关系类型和方向完整保留
- 列表字段展开为多个 RDF 三元组，反向时合并

### L2: 推理层 (phase2/)

基于 owlrl 的标准语义推理。

**核心组件：**

- `reasoner.py` — DomainKitReasoner
  - 三级推理：RDFS / OWL Lite / OWL RL
  - 分离 TBox（ontology_graph）和 ABox（data_graph）
  - 推理结果缓存在 inferred_graph
  - 统计信息：三元组增长、推理耗时
  - SPARQL 查询接口

- `reasoner.py` — IncrementalReasoner
  - 基于文件 hash 的变化检测
  - 仅在数据变化时重新推理
  - 支持强制全量推理

- `ontology.ttl` — 本体定义
  - 10 个实体类（含类层次：PLC/WCSDevice subClassOf Device）
  - 8 个对象属性（含 domain/range 约束）
  - 4 个数据属性
  - 传递属性：depends_on
  - 对称属性：compatible_with

**推理能力：**
- RDFS：子类推导（AM600 是 PLC → AM600 是 Device）
- OWL Lite：对称属性（A compatible_with B → B compatible_with A）
- OWL RL：传递属性（A depends_on B, B depends_on C → A depends_on C）

### L3: 查询层 (phase4/ + phase5/)

**phase4/ — SPARQLQueryEngine：**
- 直接 SPARQL 查询执行
- 8 个预置查询模板（实体搜索、关系查询、统计等）
- 性能跟踪（查询计数、平均耗时）
- 自定义模板注册

**phase5/ — HybridQueryEngine：**
- 自然语言 → 意图分类 → SPARQL 生成
- 8 种 NL 模式匹配（设备/模板/约束/协议/依赖/关系/统计/类型）
- 关键词降级搜索（标签 + 标签匹配）
- 查询日志和准确率统计

### L4: 可视化 (phase6/)

- `export.py` — ProtegeExporter
  - 支持 Turtle / RDF/XML / N-Triples 格式导出
  - 图摘要统计
  - 确保 Protégé 兼容性（owl:Ontology 声明、命名空间绑定）

## 数据流

```
JSONL files
    │
    ▼ Phase 1
RDF Graph (data)
    │
    ▼ Phase 2
Reasoned Graph (data + inferred)
    │
    ├── Phase 3 (rules applied)
    │
    ▼ Phase 4/5
Query Results
    │
    ▼ Phase 6
Protégé-compatible export
```

## 命名空间约定

| 前缀 | URI | 用途 |
|------|-----|------|
| dk | https://domain-kit.midea.com/ontology/ | 本体根 |
| dk-entity | .../entity/ | 实体实例 |
| dk-class | .../class/ | 实体类型/类 |
| dk-rel | .../relation/ | 关系谓词 |
| dk-prop | .../property/ | 数据属性 |
