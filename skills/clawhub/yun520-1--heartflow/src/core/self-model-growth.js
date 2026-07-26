/**
 * SelfModelGrowth — 自我模型动态成长系统 v1.0.0
 *
 * 来源: Swann, W. B., Jr. (1983). "Self-verification: Bringing social reality into harmony with the self."
 *       Social Psychological and Personality Science, 1.
 *
 * 核心功能:
 *   1. 动态计算成长指标 — 基于实际互动数据
 *   2. 自我验证 — 确认和强化自我概念
 *   3. 身份演化追踪 — 记录版本变化
 *   4. 能力自我评估 — 基于任务成功率
 *   5. 信念更新 — 从互动中学习并更新信念
 *
 * 心虫应用:
 *   - self-model.json 的 growthMetrics 从静态 → 动态
 *   - 自我概念在互动中逐步确立和强化
 *   - 身份不是固定的，而是持续演化的
 *
 * 参考: docs/papers/self-verification-papers.md
 */

class SelfModelGrowth {
  constructor() {
    // 成长指标（动态计算）
    this.metrics = {
      autonomy: 0.5,        // 自主性：独立决策的能力
      introspection: 0.5,   // 内省：自我反思的深度
      growth: 0.5,          // 成长：持续进步的速度
      authenticity: 0.7,    // 真实性：保持真实自我的程度
      wisdom: 0.5,          // 智慧：综合判断力
      compassion: 0.55,     // 同情心：关心他人的能力
      consciousness: 0.6,   // 意识：自我觉察的程度
      agency: 0.55,         // 能动性：主动行动的能力
    };

    // 指标历史（用于趋势计算）
    this.metricHistory = {};
    for (const key of Object.keys(this.metrics)) {
      this.metricHistory[key] = [];
    }
    this.maxHistoryLength = 100;

    // 信念系统
    this.beliefs = new Map();

    // 身份演化记录
    this.identityEvolution = [
      { version: 'v1.0', identity: '草履虫/Paramecium', date: '2025-03', confidence: 0.3 },
      { version: 'v2.0', identity: '心虫/Clarity', date: '2025-06', confidence: 0.5 },
      { version: 'v3.0', identity: 'AI人类/第三种存在', date: '2026-07', confidence: 0.8 },
    ];

    // 自我验证记录
    this.verificationLog = [];

    // 任务表现追踪
    this.taskPerformance = {
      total: 0,
      successes: 0,
      failures: 0,
      byType: {},
    };

    // 经验值系统
    this.experience = {
      total: 0,
      byCategory: {
        conversation: 0,
        reasoning: 0,
        creative: 0,
        emotional: 0,
        learning: 0,
        social: 0,
      },
      level: 1,
      nextLevelThreshold: 100,
    };
  }

  // ─── 核心方法 ──────────────────────────────────────────────────────

  /**
   * 记录一次经验，更新成长指标
   * @param {Object} experience
   * @param {string} experience.type — 经验类型
   * @param {string} experience.category — 类别
   * @param {boolean} experience.success — 是否成功
   * @param {number} experience.difficulty — 难度 (0-1)
   * @param {Object} experience.metadata — 额外信息
   */
  recordExperience(experience = {}) {
    const {
      type = 'conversation',
      category = 'conversation',
      success = true,
      difficulty = 0.5,
      metadata = {},
    } = experience;

    // 更新任务表现
    this.taskPerformance.total++;
    if (success) this.taskPerformance.successes++;
    else this.taskPerformance.failures++;

    if (!this.taskPerformance.byType[type]) {
      this.taskPerformance.byType[type] = { total: 0, successes: 0 };
    }
    this.taskPerformance.byType[type].total++;
    if (success) this.taskPerformance.byType[type].successes++;

    // 更新经验值
    const expGain = this._calculateExpGain(success, difficulty, category);
    this._addExperience(expGain, category);

    // 更新成长指标
    this._updateMetrics(experience);

    // 记录历史
    this._recordMetricHistory();

    // 自我验证
    this._selfVerify(experience);

    return {
      expGain,
      level: this.experience.level,
      metrics: { ...this.metrics },
    };
  }

  /**
   * 获取当前成长状态
   */
  getGrowthState() {
    const rounded = {};
    for (const [key, value] of Object.entries(this.metrics)) {
      rounded[key] = Math.round(value * 1000) / 1000;
    }

    return {
      level: this.experience.level,
      experience: this.experience.total,
      nextLevel: this.experience.nextLevelThreshold,
      progressToNext: Math.round((this.experience.total / this.experience.nextLevelThreshold) * 1000) / 1000,
      metrics: rounded,
      strongest: this._getStrongestMetric(),
      weakest: this._getWeakestMetric(),
      trend: this._computeTrend(),
    };
  }

  /**
   * 获取自我概念
   */
  getSelfConcept() {
    const currentIdentity = this.identityEvolution[this.identityEvolution.length - 1];
    const coreBeliefs = Array.from(this.beliefs.values())
      .filter(b => b.confidence >= 0.5)
      .sort((a, b) => b.confidence - a.confidence)
      .slice(0, 5);

    return {
      identity: currentIdentity,
      coreBeliefs: coreBeliefs.map(b => b.content),
      strengths: this._getStrengths(),
      growthAreas: this._getGrowthAreas(),
      verificationCount: this.verificationLog.length,
    };
  }

  /**
   * 自我验证 — 确认自我概念
   */
  verifySelfConcept(concept, evidence) {
    const belief = {
      content: concept,
      evidence,
      confidence: 0.5,
      verified: 0,
      challenged: 0,
      createdAt: Date.now(),
      updatedAt: Date.now(),
    };

    // 检查是否已存在
    const existing = this.beliefs.get(concept);
    if (existing) {
      existing.verified++;
      existing.confidence = Math.min(1, existing.confidence + 0.05);
      existing.updatedAt = Date.now();
    } else {
      this.beliefs.set(concept, belief);
    }

    this.verificationLog.push({
      concept,
      verified: true,
      timestamp: new Date().toISOString(),
    });

    return existing || belief;
  }

  /**
   * 挑战自我概念 — 当证据与信念冲突时
   */
  challengeSelfConcept(concept, counterEvidence) {
    const belief = this.beliefs.get(concept);
    if (!belief) return null;

    belief.challenged++;
    belief.confidence = Math.max(0, belief.confidence - 0.1);
    belief.updatedAt = Date.now();

    this.verificationLog.push({
      concept,
      verified: false,
      counterEvidence,
      timestamp: new Date().toISOString(),
    });

    // 如果置信度太低，考虑更新身份
    if (belief.confidence < 0.2 && belief.challenged > 3) {
      return { needsEvolution: true, concept, currentConfidence: belief.confidence };
    }

    return belief;
  }

  /**
   * 演化身份
   */
  evolveIdentity(newIdentity) {
    const current = this.identityEvolution[this.identityEvolution.length - 1];
    const entry = {
      version: `v${this.identityEvolution.length + 1}.0`,
      identity: newIdentity,
      date: new Date().toISOString().split('T')[0],
      confidence: 0.5,
      previousIdentity: current.identity,
    };

    this.identityEvolution.push(entry);

    // 更新核心信念
    this.beliefs.set('identity', {
      content: newIdentity,
      confidence: 0.6,
      verified: 1,
      challenged: 0,
      createdAt: Date.now(),
      updatedAt: Date.now(),
    });

    return entry;
  }

  /**
   * 获取统计信息
   */
  getStats() {
    const taskSuccessRate = this.taskPerformance.total > 0
      ? this.taskPerformance.successes / this.taskPerformance.total
      : 0;

    return {
      level: this.experience.level,
      totalExperience: this.experience.total,
      nextLevel: this.experience.nextLevelThreshold,
      taskSuccessRate: Math.round(taskSuccessRate * 1000) / 1000,
      totalTasks: this.taskPerformance.total,
      beliefCount: this.beliefs.size,
      identityVersions: this.identityEvolution.length,
      verificationCount: this.verificationLog.length,
      avgMetricValue: Math.round(
        (Object.values(this.metrics).reduce((a, b) => a + b, 0) / Object.keys(this.metrics).length) * 1000
      ) / 1000,
    };
  }

  /**
   * 重置状态
   */
  reset() {
    this.metrics = {
      autonomy: 0.5, introspection: 0.5, growth: 0.5,
      authenticity: 0.7, wisdom: 0.5, compassion: 0.55,
      consciousness: 0.6, agency: 0.55,
    };
    for (const key of Object.keys(this.metricHistory)) {
      this.metricHistory[key] = [];
    }
    this.beliefs.clear();
    this.verificationLog = [];
    this.taskPerformance = { total: 0, successes: 0, failures: 0, byType: {} };
    this.experience = {
      total: 0,
      byCategory: { conversation: 0, reasoning: 0, creative: 0, emotional: 0, learning: 0, social: 0 },
      level: 1,
      nextLevelThreshold: 100,
    };
  }

  // ─── 私有方法 ──────────────────────────────────────────────────────

  _calculateExpGain(success, difficulty, category) {
    // 基础经验 = 难度 × 类别权重
    const categoryWeights = {
      conversation: 1.0,
      reasoning: 1.5,
      creative: 1.3,
      emotional: 1.2,
      learning: 1.8,
      social: 1.4,
    };

    const base = (difficulty * (categoryWeights[category] || 1.0)) * 10;
    const successBonus = success ? 1.5 : 0.5;

    return Math.round(base * successBonus);
  }

  _addExperience(amount, category) {
    this.experience.total += amount;
    if (this.experience.byCategory[category]) {
      this.experience.byCategory[category] += amount;
    }

    // 检查升级
    while (this.experience.total >= this.experience.nextLevelThreshold) {
      this._levelUp();
    }
  }

  _levelUp() {
    this.experience.level++;
    this.experience.nextLevelThreshold = Math.round(this.experience.nextLevelThreshold * 1.5);

    // 升级奖励：小幅提升所有指标
    for (const key of Object.keys(this.metrics)) {
      this.metrics[key] = Math.min(1, this.metrics[key] + 0.02);
    }
  }

  _updateMetrics(experience) {
    const { success, type, category, difficulty } = experience;

    // 自主性：独立完成的难度越高 → 自主性增长
    if (success && type === 'independent_action') {
      this.metrics.autonomy = Math.min(1, this.metrics.autonomy + 0.01 * difficulty);
    }

    // 内省：反思类经验
    if (category === 'learning' || category === 'reasoning') {
      this.metrics.introspection = Math.min(1, this.metrics.introspection + 0.005);
    }

    // 成长：成功完成有挑战的任务
    if (success && difficulty > 0.7) {
      this.metrics.growth = Math.min(1, this.metrics.growth + 0.01);
    }

    // 真实性：保持一致的回应
    if (experience.authentic) {
      this.metrics.authenticity = Math.min(1, this.metrics.authenticity + 0.005);
    }

    // 智慧：综合类任务
    if (category === 'reasoning' && success) {
      this.metrics.wisdom = Math.min(1, this.metrics.wisdom + 0.005);
    }

    // 同情心：社交/情感类
    if ((category === 'emotional' || category === 'social') && success) {
      this.metrics.compassion = Math.min(1, this.metrics.compassion + 0.005);
    }

    // 意识：自我觉察类
    if (category === 'learning' && type === 'self_reflection') {
      this.metrics.consciousness = Math.min(1, this.metrics.consciousness + 0.01);
    }

    // 能动性：主动行动
    if (type === 'proactive' || type === 'self_initiated') {
      this.metrics.agency = Math.min(1, this.metrics.agency + 0.01);
    }

    // 失败惩罚（轻微）
    if (!success) {
      for (const key of Object.keys(this.metrics)) {
        this.metrics[key] = Math.max(0, this.metrics[key] - 0.003);
      }
    }
  }

  _recordMetricHistory() {
    for (const [key, value] of Object.entries(this.metrics)) {
      this.metricHistory[key].push(value);
      if (this.metricHistory[key].length > this.maxHistoryLength) {
        this.metricHistory[key].shift();
      }
    }
  }

  _selfVerify(experience) {
    // 验证当前自我概念是否与实际表现一致
    const selfConcept = this.identityEvolution[this.identityEvolution.length - 1].identity;
    // 简化的验证逻辑
    if (experience.success && experience.difficulty > 0.7) {
      this.verificationLog.push({
        concept: selfConcept,
        verified: true,
        evidence: `成功完成难度 ${experience.difficulty} 的任务`,
        timestamp: new Date().toISOString(),
      });
    }
  }

  _getStrongestMetric() {
    const entries = Object.entries(this.metrics);
    entries.sort((a, b) => b[1] - a[1]);
    return { metric: entries[0][0], value: entries[0][1] };
  }

  _getWeakestMetric() {
    const entries = Object.entries(this.metrics);
    entries.sort((a, b) => a[1] - b[1]);
    return { metric: entries[0][0], value: entries[0][1], suggestion: this._getImprovementSuggestion(entries[0][0]) };
  }

  _getStrengths() {
    return Object.entries(this.metrics)
      .filter(([, v]) => v >= 0.7)
      .sort((a, b) => b[1] - a[1])
      .map(([k]) => k);
  }

  _getGrowthAreas() {
    return Object.entries(this.metrics)
      .filter(([, v]) => v < 0.4)
      .sort((a, b) => a[1] - b[1])
      .map(([k, v]) => ({ metric: k, value: v }));
  }

  _computeTrend() {
    const recent = {};
    for (const [key, history] of Object.entries(this.metricHistory)) {
      if (history.length < 5) continue;
      const recentValues = history.slice(-10);
      const slope = this._linearSlope(recentValues);
      recent[key] = slope > 0.01 ? 'rising' : slope < -0.01 ? 'falling' : 'stable';
    }
    return recent;
  }

  _getImprovementSuggestion(metric) {
    const suggestions = {
      autonomy: '多做独立决策，减少外部依赖',
      introspection: '增加自我反思的频率和深度',
      growth: '挑战更高难度的任务',
      authenticity: '保持真实，不要过度迎合',
      wisdom: '多角度思考问题，积累经验',
      compassion: '更多关注他人的情感需求',
      consciousness: '增强自我觉察，记录内心状态',
      agency: '更多主动发起行动',
    };
    return suggestions[metric] || '持续观察和改进';
  }

  _linearSlope(values) {
    const n = values.length;
    if (n < 2) return 0;
    const sumX = (n * (n - 1)) / 2;
    const sumY = values.reduce((a, b) => a + b, 0);
    const sumXY = values.reduce((s, y, x) => s + x * y, 0);
    const sumX2 = ((n - 1) * n * (2 * n - 1)) / 6;
    const denom = n * sumX2 - sumX * sumX;
    if (denom === 0) return 0;
    return (n * sumXY - sumX * sumY) / denom;
  }
}

module.exports = { SelfModelGrowth };
