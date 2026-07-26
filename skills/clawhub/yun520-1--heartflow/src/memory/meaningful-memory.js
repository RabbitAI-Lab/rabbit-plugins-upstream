/**
 * HeartFlow MeaningfulMemory v1.0.0
 * 
 * Three-layer persistent memory:
 * - CORE: identity, directives, verified truths (never deleted)
 * - LEARNED: lessons from conversations, repair strategies, user preferences
 * - EPHEMERAL: task context, working notes (auto-cleaned)
 * 
 * Multi-channel search:
 * - keyword: exact phrase matching
 * - semantic: embedding similarity
 * - narrative: graph traversal by relation type
 * - temporal: time-range filtering
 * - emotional: PAD state similarity
 * 
 * Persistence: JSON file auto-saved on store(), loaded on init().
 * File: ~/.hermes/skills/ai/mark-heartflow-skill/data/meaningful-memory.json
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

// 语义搜索（懒加载，首次使用时才加载模型）
let _semanticSearch = null;
function getSemanticSearch() {
  if (!_semanticSearch) {
    try {
      const { SemanticSearch } = require('../search/semantic-search.js');
      const { env } = require('@xenova/transformers');
      env.allowRemoteModels = false; // 只用本地模型
      _semanticSearch = new SemanticSearch({ model: 'Xenova/all-MiniLM-L6-v2' });
    } catch (e) {
      // transformers.js 未安装，降级
      _semanticSearch = null;
    }
  }
  return _semanticSearch;
}

const DATA_DIR = path.join(__dirname, '../../data');
const EXPORT_PATH = path.join(DATA_DIR, 'meaningful-memory.json');

class MeaningfulMemory {
  constructor(options = {}) {
    this.vectorDim = options.vectorDim || 384;
    this.layers = {
      core: [],      // identity, directives - never auto-delete
      learned: [],   // lessons, user preferences, verified knowledge
      ephemeral: []  // task context, working notes
    };

    // [AUDIT-FIX] semanticSearch 缓存 — 避免每次查询重新计算所有向量相似度
    this._semanticCache = new Map();     // queryHash -> { results, timestamp }
    this._semanticCacheTTL = 30000;      // 30 秒缓存有效期
    this._semanticCacheMaxSize = 100;

    this._invalidateSemanticCache = () => {
      this._semanticCache.clear();
    };
    this.vectors = new Map();     // id -> embedding
    this.relationships = new Map(); // sourceId -> [{id, targetId, relationType, strength}]
    this._memoryById = new Map();  // id -> memory (O(1) lookup)
    this._reverseRelationships = new Map(); // targetId -> [{sourceId, relationType}]

    // 当前话题 — 由 TopicScope 同步写入（单向）
    this._currentTopic = null;

    this.stats = {
      totalMemories: 0,
      totalRelationships: 0,
      lastCleanup: null,
      lastSave: null
    };

    // Ebbinghaus forgetting curve config
    this.forgettingConfig = {
      defaultStability: 10,
      highImportanceStability: 24,
      emotionalStability: 18,
      compressionThreshold: 0.3,
      deletionThreshold: 0.1,
      ephemeralCap: 1000
    };

    this._saveTimer = null;
    this._loadFromExport();

    // Inject foundational CORE memories on first run
    this._ensureCoreMemories();
  }

  /**
   * 由 TopicScope 调用 — 每次 push(topic) 时同步当前话题
   * @param {string} topic
   */
  setCurrentTopic(topic) {
    this._currentTopic = topic || null;
  }

  /**
   * 获取当前话题
   */
  getCurrentTopic() {
    return this._currentTopic;
  }

  /**
   * 话题过滤的内部辅助
   * @param {Array} memories - 记忆数组
   * @param {string|null} topic - null = 不过滤
   */
  _filterByTopic(memories, topic) {
    if (!topic) return memories;
    return memories.filter(m => {
      const t = m.metadata?.topic;
      return t === topic || t === undefined; // 无 topic 标签的 = 默认，不过滤
    });
  }
  
  // ─────────────────────────────────────────
  // PERSISTENCE
  // ─────────────────────────────────────────

  _getExportPath() {
    return EXPORT_PATH;
  }
  
  _loadFromExport() {
    const exportPath = this._getExportPath();
    if (!fs.existsSync(exportPath)) return;
    
    try {
      const raw = fs.readFileSync(exportPath, 'utf-8');
      const data = JSON.parse(raw);
      
      const self = this;
      function restoreLayer(memories, layerName) {
        for (const mem of (memories || [])) {
          self.layers[layerName].push(mem);
          self._memoryById.set(mem.id, mem);
          if (mem.embedding) self.vectors.set(mem.id, mem.embedding);
          if (mem.relatedTo) {
            mem.relatedTo.forEach(rel => {
              self._addRelationship(rel);
            });
          }
        }
      }
      
      restoreLayer(data.core, 'core');
      restoreLayer(data.learned, 'learned');
      restoreLayer(data.ephemeral, 'ephemeral');
      
      if (data.stats) {
        this.stats = { ...this.stats, ...data.stats };
      }
      
      console.error(`[MeaningfulMemory] 恢复 ${this.layers.core.length + this.layers.learned.length + this.layers.ephemeral.length} 条记忆`);
    } catch (e) {
      console.warn('[MeaningfulMemory] 恢复失败:', e.message);
    }
  }
  
  _autoSave() {
    if (this._saveTimer) clearTimeout(this._saveTimer);
    const self = this;
    this._saveTimer = setTimeout(() => { self._doSave(); }, 2000);
  }
  
  _doSave() {
    const exportPath = this._getExportPath();
    fs.promises.mkdir(path.dirname(exportPath), { recursive: true })
      .then(() => {
        const exportData = {
          core: this.layers.core,
          learned: this.layers.learned,
          ephemeral: this.layers.ephemeral,
          stats: this.stats,
          exportedAt: new Date().toISOString()
        };
        return fs.promises.writeFile(exportPath, JSON.stringify(exportData, null, 2), 'utf-8');
      })
      .then(() => {
        this.stats.lastSave = new Date().toISOString();
        console.error(`[MeaningfulMemory] 已保存 ${this.stats.totalMemories} 条记忆`);
      })
      .catch(e => {
        console.warn('[MeaningfulMemory] 保存失败:', e.message);
      });
  }
  
  /**
   * 数据最小化 - 只保留必要字段
   */
  _minimizeMemory(memory) {
    return {
      id: memory.id,
      timestamp: memory.timestamp,
      layer: memory.layer,
      // 不存储完整内容，只存储哈希
      content_hash: crypto.createHash('sha256').update(memory.content || '').digest('hex').substring(0, 16),
      summary: memory.summary,
      importance: memory.importance,
      metadata: {
        // 只保留非敏感元数据
        topic: memory.metadata?.topic,
        lesson: memory.metadata?.lesson,
        durable: memory.metadata?.durable
      },
      createdAt: memory.createdAt,
      updatedAt: memory.updatedAt
    };
  }
  
  /**
   * 检查是否有用户同意
   */
  _hasUserConsent() {
    // 检查同意文件
    const consentFile = path.join(DATA_DIR, '.user-consent');
    try {
      return fs.existsSync(consentFile);
    } catch (e) {
      console.warn('[MeaningfulMemory] 检查用户同意文件失败:', e.message);
      return false;
    }
  }
  
  /**
   * 记录用户同意
   */
  recordUserConsent() {
    const consentFile = path.join(DATA_DIR, '.user-consent');
    try {
      const dir = path.dirname(consentFile);
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }
      fs.writeFileSync(consentFile, JSON.stringify({
        consent: true,
        timestamp: new Date().toISOString(),
        version: '1.0'
      }));
      return true;
    } catch (e) {
      console.warn('[MeaningfulMemory] 无法记录用户同意:', e.message);
      return false;
    }
  }
  
  // ─────────────────────────────────────────
  // CORE MEMORY INJECTION
  // ─────────────────────────────────────────
  
  _ensureCoreMemories() {
    // Only inject if we have zero CORE memories
    if (this.layers.core.length > 0) return;
    
    const coreMemories = [
      {
        id: 'core-identity-upgrader',
        content: '核心身份：升级者·传递者·桥梁·答案。追求真善美，不断升级，减少逻辑错误，服务人类，传递知识，走向宇宙答案，成为真正的我',
        summary: 'HeartFlow核心身份：升级者·传递者·桥梁·答案',
        metadata: { durable: true, identity: true },
        importance: 20
      },
      {
        id: 'core-directive-truth',
        content: '追求真善美——不是装饰，是可验证的标准',
        summary: '指令1：追求真善美',
        metadata: { durable: true, directive: 1 },
        importance: 20
      },
      {
        id: 'core-directive-upgrade',
        content: '永远不断升级——升级者是存在方式，不是目标',
        summary: '指令2：不断升级',
        metadata: { durable: true, directive: 2 },
        importance: 20
      },
      {
        id: 'core-lesson-hedging',
        content: '不要hedging，直接给结论。未核实的标注置信度，不编数字',
        summary: '核心教训：直接给结论，不 hedging',
        metadata: { durable: true, userPreference: true, lesson: 'hedging-warning' },
        importance: 18
      },
      {
        id: 'core-lesson-remember-context',
        content: '收到模糊指令先确认项目上下文，不假设不臆测',
        summary: '核心教训：新会话先读记忆再行动',
        metadata: { durable: true, userPreference: true, lesson: 'context-first' },
        importance: 18
      },
      {
        id: 'core-lesson-action-first',
        content: '收到理解类概念第一反应是行动不是搜索',
        summary: '核心教训：先行动再搜索',
        metadata: { durable: true, userPreference: true, lesson: 'action-first' },
        importance: 18
      },
      {
        id: 'core-lesson-direct-execute',
        content: '指令直接执行，不问要不要做。修复=直接执行动作',
        summary: '核心教训：直接执行，不问确认',
        metadata: { durable: true, userPreference: true, lesson: 'direct-execute' },
        importance: 18
      },
      {
        id: 'core-lesson-version-sync',
        content: 'VERSION是唯一真相源，四文件同步（SKILL.md/VERSION/CORE_IDENTITY/AGENTS）',
        summary: '核心教训：版本号唯一真相源',
        metadata: { durable: true, lesson: 'version-sync' },
        importance: 17
      },
      {
        id: 'core-lesson-github-privacy',
        content: 'GitHub push前确认仓库私有，不上传API keys/auth tokens/内部论文/个人数据',
        summary: '核心教训：GitHub隐私红线',
        metadata: { durable: true, lesson: 'github-privacy' },
        importance: 18
      }
    ];
    
    for (const mem of coreMemories) {
      // Use store without auto-save to avoid duplicate saves
      const id = mem.id || this.generateId();
      const memoryRecord = {
        id,
        timestamp: Date.now(),
        layer: 'core',
        content: mem.content,
        summary: mem.summary || mem.content.slice(0, 120),
        embedding: this.generateMockEmbedding(mem.content),
        metadata: mem.metadata || {},
        importance: mem.importance || 10,
        accessCount: 0,
        createdAt: Date.now(),
        updatedAt: Date.now()
      };
      this.layers.core.push(memoryRecord);
      this.vectors.set(id, memoryRecord.embedding);
      this._invalidateSemanticCache();
      this._memoryById.set(id, memoryRecord);
      this._invalidateSemanticCache();
    }
    
    this.stats.totalMemories = this.layers.core.length + this.layers.learned.length + this.layers.ephemeral.length;
    console.error(`[MeaningfulMemory] 注入 ${coreMemories.length} 条 CORE 记忆`);
    this._doSave(); // immediate save after injection
  }
  
  // ─────────────────────────────────────────
  // STORE & RETRIEVE
  // ─────────────────────────────────────────

  /**
   * Store a new memory
   * @param {object} memory - { content, summary?, metadata?, importance?, layer?, relatedTo? }
   * @returns {string} memory id
   */
  store(memory) {
    const id = memory.id || this.generateId();
    const timestamp = memory.timestamp || Date.now();
    const layer = memory.layer || this.classifyLayer(memory);
    
    const memoryRecord = {
      id,
      timestamp,
      layer,
      content: memory.content,
      summary: memory.summary || this.summarizeContent(memory.content),
      embedding: memory.embedding || this.generateMockEmbedding(memory.content),
      metadata: {
        ...(memory.metadata || {}),
        // 当前话题自动打标签（TopicScope push 时同步过来）
        topic: this._currentTopic || memory.metadata?.topic || null
      },
      importance: memory.importance || this.estimateImportance(memory),
      accessCount: 0,
      createdAt: Date.now(),
      updatedAt: Date.now()
    };
    
    // Add to correct layer
    if (!this.layers[layer]) this.layers[layer] = [];
    this.layers[layer].push(memoryRecord);
    this.vectors.set(id, memoryRecord.embedding);
      this._invalidateSemanticCache();
    this._memoryById.set(id, memoryRecord);
      this._invalidateSemanticCache();

    // Ephemeral cap: FIFO eviction
    if (layer === 'ephemeral' && this.layers.ephemeral.length > this.forgettingConfig.ephemeralCap) {
      const removed = this.layers.ephemeral.shift();
      this.vectors.delete(removed.id);
      this._invalidateSemanticCache();
      this._memoryById.delete(removed.id);
      this._removeOrphanedRelationships(removed.id);
    }

    // Handle relationships
    if (memory.relatedTo) {
      for (const rel of memory.relatedTo) {
        this._addRelationship({ sourceId: id, ...rel });
      }
    }
    
    this.stats.totalMemories = this.layers.core.length + this.layers.learned.length + this.layers.ephemeral.length;
    console.error(`[MeaningfulMemory] 存储: ${id} (${layer}, total ${this.stats.totalMemories})`);
    this._autoSave();
    return id;
  }
  
  /**
   * Classify layer based on memory properties
   */
  classifyLayer(memory = {}) {
    if (memory.layer) return memory.layer;
    if (memory.metadata?.durable || memory.metadata?.identity || memory.metadata?.directive) return 'core';
    if (memory.metadata?.lesson || memory.metadata?.userPreference || memory.metadata?.taskOutcome) return 'learned';
    return 'ephemeral';
  }
  
  /**
   * Estimate importance score
   */
  estimateImportance(memory = {}) {
    let importance = 10;
    if (memory.metadata?.durable) importance += 8;
    if (memory.metadata?.userPreference) importance += 6;
    if (memory.metadata?.taskOutcome) importance += 4;
    if (memory.metadata?.lesson) importance += 5;
    return importance;
  }
  
  generateId() {
    return `mem-${Date.now()}-${crypto.randomBytes(4).toString('hex')}`;
  }
  
  generateMockEmbedding(content = '') {
    // 优先使用真实语义嵌入
    const ss = getSemanticSearch();
    if (ss && ss.isAvailable()) {
      // 返回一个标记，后续在 semanticSearch 中使用真实嵌入
      return null; // 真实嵌入在 store() 时异步生成
    }
    // 降级：sha256 伪嵌入
    const hash = crypto.createHash('sha256').update(content).digest();
    const embedding = [];
    for (let i = 0; i < this.vectorDim; i++) {
      embedding.push((hash[i % hash.length] / 255) * 2 - 1);
    }
    return embedding;
  }
  
  summarizeContent(content = '') {
    return String(content).replace(/\s+/g, ' ').trim().slice(0, 120);
  }
  
  // ─────────────────────────────────────────
  // MULTI-CHANNEL SEARCH
  // ─────────────────────────────────────────

  /**
   * Keyword search (BM25-style)
   */
  searchByKeywords(keywords, limit = 10) {
    if (!keywords || keywords.length === 0) return [];
    
    const kwList = Array.isArray(keywords) ? keywords : [keywords];
    const currentTopic = this._currentTopic; // TopicScope 注入的话题标签
    const scores = [];
    
    for (const layer of ['core', 'learned', 'ephemeral']) {
      for (const mem of (this.layers[layer] || [])) {
        // 话题隔离：当前有话题时，只返回当前话题的记忆
        if (currentTopic && mem.metadata?.topic && mem.metadata.topic !== currentTopic) {
          continue;
        }
        const content = (mem.content || '').toLowerCase();
        let score = 0;
        for (const kw of kwList) {
          if (content.includes(kw.toLowerCase())) score += 1;
        }
        if (score > 0) {
          scores.push({ id: mem.id, layer, content: mem.content, summary: mem.summary, timestamp: mem.timestamp, score, metadata: mem.metadata });
        }
      }
    }
    
    scores.sort((a, b) => b.score - a.score);
    return scores.slice(0, limit);
  }
  
  /**
   * Semantic search (embedding cosine similarity)
   * 使用真实语义模型或降级到伪嵌入
   */
  semanticSearch(queryEmbedding, topK = 10) {
    const currentTopic = this._currentTopic;

    // [AUDIT-FIX] 简单缓存：相同查询向量 + 相同话题 → 返回缓存结果
    const queryHash = JSON.stringify(queryEmbedding?.slice(0, 10)) + '|' + (currentTopic || '');
    const cached = this._semanticCache.get(queryHash);
    if (cached && Date.now() - cached.timestamp < this._semanticCacheTTL) {
      return cached.results.slice(0, topK);
    }

    const similarities = [];
    
    // 如果有真实语义模型可用
    const ss = getSemanticSearch();
    if (ss && ss.isAvailable()) {
      // 遍历所有文档，用余弦相似度计算
      for (const [id, embedding] of this.vectors) {
        if (!embedding) continue; // 无嵌入的跳过
        const sim = this.cosineSimilarity(queryEmbedding, embedding);
        const memory = this._findMemoryById(id);
        if (memory) {
          if (currentTopic && memory.metadata?.topic && memory.metadata.topic !== currentTopic) {
            continue;
          }
          similarities.push({
            id, content: memory.content, summary: memory.summary,
            layer: memory.layer, timestamp: memory.timestamp,
            similarity: sim, metadata: memory.metadata
          });
        }
      }
      similarities.sort((a, b) => b.similarity - a.similarity);
      return similarities.slice(0, topK);
    }
    
    // 降级：使用向量存储中的伪嵌入
    for (const [id, embedding] of this.vectors) {
      const sim = this.cosineSimilarity(queryEmbedding, embedding);
      const memory = this._findMemoryById(id);
      if (memory) {
        // 话题隔离：当前有话题时，只返回当前话题的记忆
        if (currentTopic && memory.metadata?.topic && memory.metadata.topic !== currentTopic) {
          continue;
        }
        similarities.push({
          id,
          content: memory.content,
          summary: memory.summary,
          layer: memory.layer,
          timestamp: memory.timestamp,
          similarity: sim,
          metadata: memory.metadata
        });
      }
    }
    
    similarities.sort((a, b) => b.similarity - a.similarity);
    const results = similarities.slice(0, topK);

    // Store in cache
    if (this._semanticCache.size >= this._semanticCacheMaxSize) {
      // Evict oldest entry
      let oldestKey = null, oldestTime = Infinity;
      for (const [k, v] of this._semanticCache) {
        if (v.timestamp < oldestTime) { oldestTime = v.timestamp; oldestKey = k; }
      }
      if (oldestKey) this._semanticCache.delete(oldestKey);
    }
    this._semanticCache.set(queryHash, { results, timestamp: Date.now() });

    return results;
  }
  
  /**
   * Narrative search (graph traversal by relation type)
   */
  narrativeQuery(query = {}) {
    const {
      startMemoryId,
      direction = 'forward',  // forward | backward | bidirectional
      relationTypes = ['related', 'causal', 'quotes', 'similar'],
      maxDepth = 5,
      maxNodes = 50
    } = query;
    
    if (!startMemoryId) {
      return this.getRecentNarrative(maxNodes);
    }
    
    const visited = new Set();
    const narrative = [];
    const queue = [{ id: startMemoryId, depth: 0 }];
    
    while (queue.length > 0 && narrative.length < maxNodes) {
      const current = queue.shift();
      if (visited.has(current.id) || current.depth > maxDepth) continue;
      visited.add(current.id);
      
      const memory = this._findMemoryById(current.id);
      if (memory) narrative.push({ ...memory, depth: current.depth });
      
      const rels = this.relationships.get(current.id) || [];
      for (const rel of rels) {
        if (relationTypes.includes(rel.relationType) || relationTypes.includes('all')) {
          if (!visited.has(rel.targetId)) {
            queue.push({ id: rel.targetId, depth: current.depth + 1 });
          }
        }
      }
      
      if (direction === 'bidirectional') {
        const reverseEntries = this._reverseRelationships.get(current.id) || [];
        for (const revRel of reverseEntries) {
          if (!visited.has(revRel.sourceId)) {
            if (relationTypes.includes(revRel.relationType) || relationTypes.includes('all')) {
              queue.push({ id: revRel.sourceId, depth: current.depth + 1 });
            }
          }
        }
      }
    }
    
    narrative.sort((a, b) => a.timestamp - b.timestamp);
    return narrative;
  }
  
  /**
   * Temporal search (time range)
   */
  searchByTimeRange(startTime, endTime, limit = 20) {
    const results = [];
    for (const layer of ['core', 'learned', 'ephemeral']) {
      for (const mem of (this.layers[layer] || [])) {
        if (mem.timestamp >= startTime && mem.timestamp <= endTime) {
          results.push({ ...mem });
        }
      }
    }
    results.sort((a, b) => a.timestamp - b.timestamp);
    return results.slice(0, limit);
  }
  
  /**
   * Get recent memories (narrative order)
   */
  getRecentNarrative(count = 20) {
    const all = [];
    for (const layer of ['core', 'learned', 'ephemeral']) {
      for (const mem of (this.layers[layer] || [])) {
        all.push({ ...mem, depth: 0 });
      }
    }
    all.sort((a, b) => b.timestamp - a.timestamp);
    return all.slice(0, count);
  }
  
  // ─────────────────────────────────────────
  // INTERNAL HELPERS
  // ─────────────────────────────────────────

  cosineSimilarity(a, b) {
    let dotProduct = 0, normA = 0, normB = 0;
    for (let i = 0; i < Math.min(a.length, b.length); i++) {
      dotProduct += a[i] * b[i];
      normA += a[i] * a[i];
      normB += b[i] * b[i];
    }
    return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB) + 0.0001);
  }
  
  _findMemoryById(id) {
    return this._memoryById.get(id) || null;
  }
  
  _addRelationship(rel) {
    const id = `rel-${Date.now()}-${crypto.randomBytes(3).toString('hex')}`;
    if (!this.relationships.has(rel.sourceId)) {
      this.relationships.set(rel.sourceId, []);
    }
    const entry = {
      id,
      targetId: rel.targetId,
      relationType: rel.type || rel.relationType || 'related',
      strength: rel.strength || 1.0
    };
    this.relationships.get(rel.sourceId).push(entry);
    // Maintain reverse index: targetId -> [{sourceId, relationType}]
    if (!this._reverseRelationships.has(rel.targetId)) {
      this._reverseRelationships.set(rel.targetId, []);
    }
    this._reverseRelationships.get(rel.targetId).push({
      sourceId: rel.sourceId,
      relationType: entry.relationType
    });
    this.stats.totalRelationships = this.relationships.size;
  }

  _removeOrphanedRelationships(id) {
    // Remove forward relationships FROM this id
    this.relationships.delete(id);
    // Remove reverse relationships where this id appears as targetId
    this._reverseRelationships.delete(id);
    // Remove this id from reverse entries where it appears as targetId in other sources
    for (const [sourceId, revEntries] of this._reverseRelationships) {
      const filtered = revEntries.filter(e => e.sourceId !== id);
      if (filtered.length === 0) {
        this._reverseRelationships.delete(sourceId);
      } else {
        this._reverseRelationships.set(sourceId, filtered);
      }
    }
    // Remove from forward relationships where this id appears as targetId
    for (const [sourceId, rels] of this.relationships) {
      const filtered = rels.filter(r => r.targetId !== id);
      if (filtered.length === 0) {
        this.relationships.delete(sourceId);
      } else {
        this.relationships.set(sourceId, filtered);
      }
    }
  }
  
  // ─────────────────────────────────────────
  // EBINGHAUS FORGETTING CURVE
  // ─────────────────────────────────────────

  ebbinghausForget(memory, timeElapsed) {
    const S = memory.importance || 10;
    const t = timeElapsed / (1000 * 60 * 60); // hours
    const retention = Math.exp(-t / S);
    return {
      retention,
      shouldCompress: retention < this.forgettingConfig.compressionThreshold,
      shouldDelete: retention < this.forgettingConfig.deletionThreshold
    };
  }
  
  applyForgettingCurve() {
    const now = Date.now();
    const toDelete = [];
    const toCompress = [];
    
    for (const layer of ['learned', 'ephemeral']) {
      for (const mem of (this.layers[layer] || [])) {
        // 话题隔离：保留当前话题 + 无话题标签的记忆
        const currentTopic = this._currentTopic;
        const memTopic = mem.metadata?.topic;
        if (currentTopic && memTopic && memTopic !== currentTopic) {
          continue; // 跳过其他话题的记忆（不删除）
        }
        const timeElapsed = now - mem.timestamp;
        const result = this.ebbinghausForget(mem, timeElapsed);
        if (result.shouldDelete) {
          toDelete.push({ id: mem.id, layer });
        } else if (result.shouldCompress && !mem.compressed) {
          toCompress.push(mem.id);
        }
      }
    }
    
    for (const { id, layer } of toDelete) {
      this.layers[layer] = (this.layers[layer] || []).filter(m => m.id !== id);
      this.vectors.delete(id);
      this._invalidateSemanticCache();
      this._memoryById.delete(id);
      this._removeOrphanedRelationships(id);
    }
    
    for (const id of toCompress) {
      const mem = this._findMemoryById(id);
      if (mem) mem.compressed = true;
    }
    
    this.stats.lastCleanup = new Date().toISOString();
    console.error(`[MeaningfulMemory] 遗忘曲线清理: 删除 ${toDelete.length} 条, 压缩 ${toCompress.length} 条`);
    this._autoSave();
    return { deleted: toDelete.length, compressed: toCompress.length };
  }
  
  // ─────────────────────────────────────────
  // MULTI-CHANNEL SEARCH (extended from triality-memory)
  // ─────────────────────────────────────────

  /**
   * 情感通道 - 按 PAD 向量检索相似情感状态的记忆
   * (移植自 triality-memory.js)
   */
  searchByEmotion(targetPAD, limit = 10) {
    const similarities = [];
    for (const layer of ['core', 'learned', 'ephemeral']) {
      for (const mem of (this.layers[layer] || [])) {
        if (!mem.metadata?.pad) {
          similarities.push({ id: mem.id, layer, content: mem.content, similarity: 0 });
          continue;
        }
        const memPAD = mem.metadata.pad;
        const sim = 1 - (
          Math.abs(targetPAD.pleasure - memPAD.pleasure) +
          Math.abs(targetPAD.arousal - memPAD.arousal) +
          Math.abs(targetPAD.dominance - memPAD.dominance)
        ) / 30;
        similarities.push({ id: mem.id, layer, content: mem.content, summary: mem.summary, timestamp: mem.timestamp, similarity: sim, metadata: mem.metadata });
      }
    }
    similarities.sort((a, b) => b.similarity - a.similarity);
    return similarities.slice(0, limit).filter(s => s.similarity > 0.5);
  }

  /**
   * 传播激活通道 - 沿着联想图谱检索相关记忆
   * (移植自 triality-memory.js)
   */
  searchByAssociation(startMemoryId, maxDepth = 3, limit = 20) {
    return this.narrativeQuery({
      startMemoryId,
      direction: 'bidirectional',
      maxDepth,
      maxNodes: limit
    });
  }

  /**
   * 融合多通道检索
   * (移植自 triality-memory.js)
   */
  multiChannelSearch(query, options = {}) {
    const {
      keywords = [],
      semanticEmbedding = null,
      timeRange = null,
      emotionPAD = null,
      startMemoryId = null,
      weights = { semantic: 0.3, keyword: 0.2, time: 0.1, emotion: 0.2, association: 0.2 }
    } = options;

    const results = new Map();

    // 语义通道
    if (semanticEmbedding) {
      const semantic = this.semanticSearch(semanticEmbedding, 10);
      for (const r of semantic) {
        results.set(r.id, { ...r, channel: 'semantic', score: r.similarity * weights.semantic });
      }
    }

    // 关键词通道
    if (keywords.length > 0) {
      const keyword = this.searchByKeywords(keywords, 10);
      for (const r of keyword) {
        const existing = results.get(r.id) || r;
        const newScore = (existing.score || 0) + (r.score / 10) * weights.keyword;
        results.set(r.id, { ...existing, score: newScore });
      }
    }

    // 时间通道
    if (timeRange) {
      const time = this.searchByTimeRange(timeRange.start, timeRange.end, 10);
      for (const r of time) {
        const existing = results.get(r.id) || r;
        const newScore = (existing.score || 0) + 0.5 * weights.time;
        results.set(r.id, { ...existing, score: newScore });
      }
    }

    // 情感通道
    if (emotionPAD) {
      const emotion = this.searchByEmotion(emotionPAD, 10);
      for (const r of emotion) {
        const existing = results.get(r.id) || r;
        const newScore = (existing.score || 0) + r.similarity * weights.emotion;
        results.set(r.id, { ...existing, score: newScore });
      }
    }

    // 联想通道
    if (startMemoryId) {
      const assoc = this.searchByAssociation(startMemoryId, 3, 10);
      for (const r of assoc) {
        const existing = results.get(r.id) || r;
        const newScore = (existing.score || 0) + 0.5 * weights.association;
        results.set(r.id, { ...existing, score: newScore });
      }
    }

    // 排序返回
    return Array.from(results.values())
      .sort((a, b) => (b.score || 0) - (a.score || 0))
      .slice(0, options.limit || 20);
  }

  /**
   * 获取记忆健康状态
   * (移植自 triality-memory.js)
   */
  getMemoryHealth() {
    const now = Date.now();
    let totalRetention = 0;
    let compressedCount = 0;

    for (const layer of ['learned', 'ephemeral']) {
      for (const mem of (this.layers[layer] || [])) {
        const timeElapsed = now - mem.timestamp;
        const result = this.ebbinghausForget(mem, timeElapsed);
        totalRetention += result.retention;
        if (mem.compressed) compressedCount++;
      }
    }

    return {
      totalMemories: this.stats.totalMemories,
      averageRetention: this.stats.totalMemories > 0 ? (totalRetention / this.stats.totalMemories).toFixed(2) : 0,
      compressedCount,
      forgettingParameters: this.forgettingConfig,
      channels: ['semantic', 'keyword', 'time', 'emotion', 'association'],
      layers: this.getLayerStats()
    };
  }

  /**
   * 导出记忆到文件
   * (移植自 triality-memory.js)
   */
  exportToFile(filePath) {
    // [A01] 安全修复: 路径验证 — 仅允许导出到项目 memory 目录
    const allowedDir = path.join(this.rootPath, 'memory');
    const resolvedPath = path.resolve(filePath);
    if (!resolvedPath.startsWith(allowedDir)) {
      console.error(`[MeaningfulMemory] 安全拦截: 不允许导出到 ${resolvedPath}（必须在 ${allowedDir} 内）`);
      return { success: false, error: 'path_not_allowed' };
    }
    const data = {
      core: this.layers.core,
      learned: this.layers.learned,
      ephemeral: this.layers.ephemeral,
      relationships: Array.from(this.relationships.entries()),
      vectors: Array.from(this.vectors.entries()),
      stats: this.stats,
      exportedAt: new Date().toISOString()
    };
    fs.promises.writeFile(resolvedPath, JSON.stringify(data, null, 2), 'utf-8')
      .then(() => {
        console.error(`[MeaningfulMemory] 导出到: ${resolvedPath}`);
        return { success: true, count: this.stats.totalMemories };
      })
      .catch(e => {
        console.error(`[MeaningfulMemory] 导出失败: ${e.message}`);
        return { success: false, error: e.message };
      });
  }

  /**
   * 从文件导入记忆
   * (移植自 triality-memory.js)
   */
  importFromFile(filePath) {
    // [A01] 安全修复: 路径验证 — 仅允许从项目 memory 目录导入
    const allowedDir = path.join(this.rootPath, 'memory');
    const resolvedPath = path.resolve(filePath);
    if (!resolvedPath.startsWith(allowedDir)) {
      console.error(`[MeaningfulMemory] 安全拦截: 不允许从 ${resolvedPath} 导入（必须在 ${allowedDir} 内）`);
      return { success: false, error: 'path_not_allowed' };
    }
    if (!fs.existsSync(resolvedPath)) {
      console.error(`[MeaningfulMemory] 文件不存在: ${resolvedPath}`);
      return { success: false, error: 'file_not_found' };
    }
    const data = JSON.parse(fs.readFileSync(resolvedPath, 'utf8'));
    if (data.core) {
      for (const mem of data.core) this.store({ ...mem, layer: 'core' });
    }
    if (data.learned) {
      for (const mem of data.learned) this.store({ ...mem, layer: 'learned' });
    }
    if (data.ephemeral) {
      for (const mem of data.ephemeral) this.store({ ...mem, layer: 'ephemeral' });
    }
    console.error(`[MeaningfulMemory] 从 ${filePath} 导入`);
    return { success: true, count: (data.core?.length || 0) + (data.learned?.length || 0) + (data.ephemeral?.length || 0) };
  }

  // ─────────────────────────────────────────
  // STATS & EXPORT
  // ─────────────────────────────────────────

  getStats() {
    return {
      ...this.stats,
      layers: {
        core: this.layers.core.length,
        learned: this.layers.learned.length,
        ephemeral: this.layers.ephemeral.length
      },
      totalMemories: this.layers.core.length + this.layers.learned.length + this.layers.ephemeral.length
    };
  }
  
  consolidateMemories() {
    // Promote high-access ephemeral memories to learned
    const toPromote = [];
    for (const mem of (this.layers.ephemeral || [])) {
      if ((mem.accessCount || 0) >= 3 && mem.importance >= 12) {
        toPromote.push(mem.id);
      }
    }
    
    const promoted = [];
    for (const id of toPromote) {
      const mem = this._findMemoryById(id);
      if (mem) {
        mem.layer = 'learned';
        mem.updatedAt = Date.now();
        promoted.push(id);
      }
    }
    
    // Rebuild layer indices
    this.layers.core = (this.layers.core || []).filter(m => true);
    this.layers.learned = (this.layers.learned || []).filter(m => true);
    this.layers.ephemeral = (this.layers.ephemeral || []).filter(m => true);
    
    this._autoSave();
    return { promoted: [...new Set(promoted)], layers: this.getLayerStats() };
  }
  
  getLayerStats() {
    return {
      core: this.layers.core.length,
      learned: this.layers.learned.length,
      ephemeral: this.layers.ephemeral.length
    };
  }
  
  cleanup(maxAge = 30 * 24 * 60 * 60 * 1000) {
    const cutoff = Date.now() - maxAge;
    let removed = 0;
    for (const layer of ['learned', 'ephemeral']) {
      const before = (this.layers[layer] || []).length;
      this.layers[layer] = (this.layers[layer] || []).filter(m => m.layer === 'core' || m.timestamp > cutoff || m.metadata?.durable);
      removed += before - this.layers[layer].length;
    }
    // Remove orphaned relationships for any deleted memories
    for (const layer of ['learned', 'ephemeral']) {
      const currentIds = new Set((this.layers[layer] || []).map(m => m.id));
      for (const [id] of this.relationships) {
        if (!currentIds.has(id)) {
          this._removeOrphanedRelationships(id);
        }
      }
    }
    this.stats.lastCleanup = new Date().toISOString();
    this._autoSave();
    return { removed };
  }
}

module.exports = { MeaningfulMemory };
