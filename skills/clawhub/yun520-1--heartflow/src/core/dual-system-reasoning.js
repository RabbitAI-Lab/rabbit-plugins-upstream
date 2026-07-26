/**
 * DualSystemReasoning — 双系统推理引擎 v1.0.0
 *
 * 来源: Kahneman, D. (2011). "Thinking, Fast and Slow."
 *       + CLARION 双系统认知架构 (Sun, R., 2001)
 *
 * 双系统理论:
 *   System 1 (直觉系统):
 *     - 快速、自动、无意识
 *     - 基于模式匹配和经验
 *     - 心虫的快速路由响应
 *
 *   System 2 (分析系统):
 *     - 慢速、可控、有意识
 *     - 基于逻辑和推理
 *     - 心虫的 thought-chain 深度推理
 *
 * 仲裁机制:
 *   - System 1 先快速响应
 *   - System 2 评估 System 1 的结果质量
 *   - 如果质量不足 → 升级到 System 2 深度分析
 *   - 如果质量足够 → 直接使用 System 1 结果
 *
 * 心虫应用:
 *   - 日常对话：System 1 快速响应
 *   - 复杂问题：自动升级到 System 2
 *   - 矛盾/冲突：强制 System 2 介入
 *   - 元认知：System 2 监控 System 1
 *
 * 参考: docs/papers/meta-learning-papers.md, src/core/thought-chain.js
 */

class DualSystemReasoning {
  constructor() {
    // System 1 配置（快速直觉）
    this.system1 = {
      enabled: true,
      threshold: 0.5,         // 低于此置信度 → 升级 System 2
      maxLatency: 500,        // 最大响应时间(ms)
      modes: ['quick_response', 'pattern_match', 'emotional_reaction'],
    };

    // System 2 配置（慢速分析）
    this.system2 = {
      enabled: true,
      depthLevels: [1, 2, 3, 4], // 对应 thought-chain 的 SURFACE 到 COMPREHENSIVE
      escalationTriggers: [
        'low_confidence',      // System 1 置信度低
        'contradiction',       // 检测到矛盾
        'high_stakes',         // 高重要性判断
        'novel_situation',     // 新情况/未见过的模式
        'user_request',        // 用户明确要求深度思考
        'ethical_dilemma',     // 伦理困境
      ],
    };

    // 推理历史
    this.history = [];
    this.maxHistoryLength = 200;

    // 统计数据
    this.stats = {
      system1Calls: 0,
      system2Calls: 0,
      escalations: 0,
      avgSystem1Confidence: 0,
      avgSystem2Improvement: 0,
    };
  }

  // ─── 核心方法 ──────────────────────────────────────────────────────

  /**
   * 主推理入口 — 自动选择系统
   * @param {Object} input
   * @param {string} input.content — 输入内容
   * @param {Object} input.context — 上下文
   * @param {number} input.forcedDepth — 强制深度（1-4，0=自动）
   * @returns {Object} 推理结果
   */
  async reason(input = {}) {
    const {
      content = '',
      context = {},
      forcedDepth = 0,
      system1Result = null,
    } = input;

    // 强制 System 2
    if (forcedDepth > 0) {
      const s2Result = await this._system2Reason(content, context, forcedDepth);
      this.stats.system2Calls++;
      return {
        system: 2,
        result: s2Result,
        confidence: s2Result.confidence,
        reason: 'user_forced',
        depth: forcedDepth,
      };
    }

    // 尝试 System 1
    const s1Result = await this._system1Reason(content, context);

    // 评估是否需要升级
    const assessment = this._assessNeedForSystem2(s1Result, content, context);

    if (!assessment.needsUpgrade) {
      this.stats.system1Calls++;
      this._recordHistory('system1', content, s1Result, null);
      return {
        system: 1,
        result: s1Result,
        confidence: s1Result.confidence,
        reason: 'system1_sufficient',
      };
    }

    // 升级到 System 2
    this.stats.escalations++;
    const s2Result = await this._system2Reason(content, context, assessment.suggestedDepth);

    this.stats.system2Calls++;
    const improvement = s2Result.confidence - s1Result.confidence;
    this.stats.avgSystem2Improvement = this._movingAverage(this.stats.avgSystem2Improvement, improvement, this.stats.system2Calls);

    this._recordHistory('system2', content, s1Result, s2Result);

    return {
      system: 2,
      result: s2Result,
      system1Result: s1Result,
      confidence: s2Result.confidence,
      improvement: Math.round(improvement * 1000) / 1000,
      reason: assessment.reason,
      depth: assessment.suggestedDepth,
    };
  }

  /**
   * System 1 快速推理
   */
  async _system1Reason(content, context) {
    // 模拟快速直觉响应
    // 实际实现中这里会调用快速路由

    const confidence = this._estimateConfidence(content, context);

    return {
      content: null, // 由调用方填充
      confidence,
      latency: Math.random() * 100 + 50, // 模拟 50-150ms
      heuristic: this._identifyHeuristic(content),
      flags: this._detectFlags(content, context),
    };
  }

  /**
   * System 2 深度推理
   */
  async _system2Reason(content, context, depth = 3) {
    // 调用 thought-chain 进行深度分析
    // depth: 1=SURFACE, 2=BASIC, 3=DEEP, 4=COMPREHENSIVE

    const startTime = Date.now();

    return {
      depth,
      phases: [], // 由 thought-chain 填充
      confidence: 0, // 待计算
      latency: Date.now() - startTime,
      reasoning: [], // 推理步骤
    };
  }

  /**
   * 评估是否需要 System 2
   */
  _assessNeedForSystem2(s1Result, content, context) {
    const reasons = [];
    let suggestedDepth = 2; // 默认基础深度

    // 1. 置信度检查
    if (s1Result.confidence < this.system1.threshold) {
      reasons.push('low_confidence');
      suggestedDepth = Math.max(suggestedDepth, 3);
    }

    // 2. 矛盾检测
    if (s1Result.flags?.contradiction) {
      reasons.push('contradiction');
      suggestedDepth = Math.max(suggestedDepth, 4);
    }

    // 3. 高重要性
    if (context.importance && context.importance > 0.7) {
      reasons.push('high_stakes');
      suggestedDepth = Math.max(suggestedDepth, 3);
    }

    // 4. 新情况
    if (context.novelty && context.novelty > 0.6) {
      reasons.push('novel_situation');
      suggestedDepth = Math.max(suggestedDepth, 3);
    }

    // 5. 用户请求
    if (context.requestDepth && context.requestDepth >= 3) {
      reasons.push('user_request');
      suggestedDepth = context.requestDepth;
    }

    // 6. 伦理困境
    if (context.ethicalDilemma) {
      reasons.push('ethical_dilemma');
      suggestedDepth = Math.max(suggestedDepth, 4);
    }

    // 7. 内容复杂度
    const complexity = this._estimateComplexity(content);
    if (complexity > 0.6) {
      reasons.push('high_complexity');
      suggestedDepth = Math.max(suggestedDepth, 3);
    }

    return {
      needsUpgrade: reasons.length > 0,
      reason: reasons[0] || 'unknown',
      reasons,
      suggestedDepth: Math.min(4, suggestedDepth),
    };
  }

  // ─── 辅助方法 ──────────────────────────────────────────────────────

  _estimateConfidence(content, context) {
    // 简化实现：基于内容长度和上下文信息量
    const contentScore = Math.min(1, content.length / 200);
    const contextScore = context ? Object.keys(context).length / 10 : 0;
    return Math.min(1, contentScore * 0.5 + contextScore * 0.3 + 0.2);
  }

  _identifyHeuristic(content) {
    const lower = content.toLowerCase();
    if (/计算|算|多少|等于|calculate|compute|math/.test(lower)) return 'calculation';
    if (/为什么|为什么|原因|why|because/.test(lower)) return 'causal';
    if (/感觉|觉得|想|feel|think/.test(lower)) return 'emotional';
    if (/应该|必须|需要|should|must/.test(lower)) return 'normative';
    return 'general';
  }

  _detectFlags(content, context) {
    const flags = [];
    const lower = content.toLowerCase();

    // 矛盾检测
    if (/\b但是\b|\b然而\b|\b不过\b|\bbut\b|\bhowever\b|\byet\b/.test(lower)) {
      flags.push('contradiction');
    }

    // 不确定性
    if (/可能|也许|大概|maybe|perhaps|might/.test(lower)) {
      flags.push('uncertainty');
    }

    // 情感负载
    if (context?.emotion && Math.abs(context.emotion.pleasure || 0) > 0.5) {
      flags.push('emotional_load');
    }

    return flags;
  }

  _estimateComplexity(content) {
    let score = 0;

    // 句子数量
    const sentences = content.split(/[。！？.!?]/).filter(s => s.trim());
    score += Math.min(0.3, sentences.length * 0.05);

    // 从句数量（中文用逗号，英文用从句标记）
    const clauses = (content.match(/[，,;；]/g) || []).length;
    score += Math.min(0.3, clauses * 0.03);

    // 抽象词汇
    const abstractWords = /哲学|意识|存在|意义|价值|伦理|philosophy|consciousness|existence|meaning|ethics/.test(content);
    if (abstractWords) score += 0.2;

    // 多话题
    const topicShifts = (content.match(/\b(但是|然而|另外|还有|but|however|also|additionally)\b/g) || []).length;
    score += Math.min(0.2, topicShifts * 0.05);

    return Math.min(1, score);
  }

  _recordHistory(system, content, s1Result, s2Result) {
    this.history.push({
      system,
      content: content.slice(0, 200),
      s1Confidence: s1Result.confidence,
      s2Confidence: s2Result?.confidence,
      timestamp: new Date().toISOString(),
    });
    if (this.history.length > this.maxHistoryLength) {
      this.history.shift();
    }
  }

  _movingAverage(current, newValue, count) {
    return (current * (count - 1) + newValue) / count;
  }

  /**
   * 获取统计信息
   */
  getStats() {
    const total = this.stats.system1Calls + this.stats.system2Calls;
    return {
      ...this.stats,
      totalCalls: total,
      system1Ratio: total > 0 ? Math.round((this.stats.system1Calls / total) * 1000) / 1000 : 0,
      escalationRate: this.stats.system1Calls > 0
        ? Math.round((this.stats.escalations / this.stats.system1Calls) * 1000) / 1000
        : 0,
      historyLength: this.history.length,
    };
  }

  /**
   * 重置状态
   */
  reset() {
    this.history = [];
    this.stats = {
      system1Calls: 0,
      system2Calls: 0,
      escalations: 0,
      avgSystem1Confidence: 0,
      avgSystem2Improvement: 0,
    };
  }
}

module.exports = { DualSystemReasoning };
