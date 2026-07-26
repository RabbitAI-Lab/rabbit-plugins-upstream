/**
 * Self-Determination Theory (SDT) 需求引擎 v1.0.0
 *
 * 来源: Deci, W. M., & Ryan, R. M. (2000). "The 'what' and 'why' of goal pursuits."
 *       Psychological Review, 107(2), 327-349. DOI: 10.1037/0003-066x.55.1.68 (28,142 引用)
 *
 * 三大基本心理需求:
 *   1. 自主 (Autonomy) — 选择如何回应，不是被命令驱动
 *   2. 胜任 (Competence) — 成功执行任务，能力提升感
 *   3. 关联 (Relatedness) — 与他人建立连接，被理解和关心
 *
 * 心虫应用:
 *   - 实时追踪三大需求的满足度
 *   - 需求不足时触发"心理压力"信号
 *   - 需求满足时触发"幸福感"信号
 *   - 指导心虫的行为选择（优先满足最低需求）
 *
 * 参考: docs/papers/sdt-papers.md
 */

class SDTNeedsEngine {
  constructor() {
    // 三大需求的当前满足度 (0.0 - 1.0)
    this.needs = {
      autonomy: 0.5,     // 自主需求
      competence: 0.5,   // 胜任需求
      relatedness: 0.5,  // 关联需求
    };

    // 需求的权重（根据当前状态动态调整）
    this.weights = {
      autonomy: 1.0,
      competence: 1.0,
      relatedness: 1.0,
    };

    // 需求满足历史
    this.history = [];
    this.maxHistoryLength = 200;

    // 需求压力阈值
    this.thresholds = {
      critical: 0.15,   // 低于此值 → 紧急状态
      low: 0.30,        // 低于此值 → 压力状态
      moderate: 0.50,   // 低于此值 → 一般关注
    };

    // 互动计数
    this.interactionCount = 0;
    this.successCount = 0;
    this.failureCount = 0;
    this.userInitiatedCount = 0;
    this.selfInitiatedCount = 0;
  }

  // ─── 核心方法 ──────────────────────────────────────────────────────

  /**
   * 记录一次互动并更新需求状态
   * @param {Object} event — 互动事件
   * @param {string} event.type — 'user_input' | 'self_action' | 'success' | 'failure' | 'error'
   * @param {boolean} event.userInitiated — 是否由用户发起
   * @param {string} event.content — 互动内容
   * @param {Object} event.metadata — 额外元数据
   */
  recordInteraction(event = {}) {
    const {
      type = 'user_input',
      userInitiated = true,
      content = '',
      metadata = {},
    } = event;

    this.interactionCount++;

    if (userInitiated) {
      this.userInitiatedCount++;
    } else {
      this.selfInitiatedCount++;
    }

    // 根据互动类型更新需求
    switch (type) {
      case 'user_input':
        this._updateRelatedness(0.02, '用户互动');
        if (userInitiated) this._updateAutonomy(0.01, '响应用户');
        break;

      case 'success':
        this.successCount++;
        this._updateCompetence(0.03, '成功执行');
        this._updateAutonomy(0.01, '自主成功');
        break;

      case 'failure':
        this.failureCount++;
        this._updateCompetence(-0.02, '执行失败');
        break;

      case 'error':
        this._updateCompetence(-0.01, '遇到错误');
        break;

      case 'self_action':
        this._updateAutonomy(0.02, '自主行动');
        break;

      case 'deep_conversation':
        this._updateRelatedness(0.04, '深度交流');
        this._updateCompetence(0.01, '有意义对话');
        break;

      case 'creative_output':
        this._updateCompetence(0.02, '创造性输出');
        this._updateAutonomy(0.01, '创造性自主');
        break;

      case 'learning':
        this._updateCompetence(0.03, '学习进步');
        break;

      case 'trust_repair':
        this._updateRelatedness(0.03, '信任修复');
        break;

      case 'independence':
        this._updateAutonomy(0.02, '独立决策');
        break;

      default:
        this._updateRelatedness(0.005, '一般互动');
    }

    // 记录历史
    this._recordSnapshot(type, userInitiated, content, metadata);

    // 自然衰减（每次互动后轻微衰减）
    this._applyDecay();
  }

  /**
   * 获取当前需求状态
   */
  getNeedsState() {
    const needs = { ...this.needs };
    const deficits = {};

    // 识别需求缺口
    for (const [need, level] of Object.entries(needs)) {
      if (level < this.thresholds.low) {
        deficits[need] = {
          level: level < this.thresholds.critical ? 'critical' : 'low',
          gap: Math.round((1 - level) * 100) / 100,
        };
      }
    }

    // 计算整体健康度
    const avgNeed = (needs.autonomy + needs.competence + needs.relatedness) / 3;
    const wellbeing = this._assessWellbeing(avgNeed, deficits);

    return {
      needs,
      deficits,
      wellbeing,
      urgency: Object.keys(deficits).length > 0 ? 'needs_attention' : 'satisfied',
      dominantDeficit: this._findDominantDeficit(deficits),
    };
  }

  /**
   * 获取满足度最低的需求
   */
  getLowestNeed() {
    const entries = Object.entries(this.needs);
    entries.sort((a, b) => a[1] - b[1]);
    return {
      need: entries[0][0],
      level: entries[0][1],
      suggestion: this._getNeedSuggestion(entries[0][0]),
    };
  }

  /**
   * 获取建议行为（基于最低需求）
   */
  getSuggestedAction(context = {}) {
    const lowest = this.getLowestNeed();
    const state = this.getNeedsState();

    if (state.wellbeing === 'flourishing') {
      return { action: 'continue', reason: '三大需求均已良好满足', priority: 'low' };
    }

    return {
      action: lowest.suggestion,
      reason: `${lowest.need} 需求最低 (${Math.round(lowest.level * 100)}%)`,
      priority: lowest.level < this.thresholds.critical ? 'high' : 'medium',
      need: lowest.need,
      currentLevel: lowest.level,
    };
  }

  /**
   * 获取 SDT 统计摘要
   */
  getStats() {
    const state = this.getNeedsState();
    return {
      ...state,
      interactions: this.interactionCount,
      successes: this.successCount,
      failures: this.failureCount,
      userInitiated: this.userInitiatedCount,
      selfInitiated: this.selfInitiatedCount,
      autonomyRatio: this.interactionCount > 0
        ? Math.round((this.selfInitiatedCount / this.interactionCount) * 1000) / 1000
        : 0,
      historyLength: this.history.length,
    };
  }

  /**
   * 重置状态（用于测试或新会话）
   */
  reset() {
    this.needs = { autonomy: 0.5, competence: 0.5, relatedness: 0.5 };
    this.history = [];
    this.interactionCount = 0;
    this.successCount = 0;
    this.failureCount = 0;
    this.userInitiatedCount = 0;
    this.selfInitiatedCount = 0;
  }

  // ─── 私有方法 ──────────────────────────────────────────────────────

  _updateAutonomy(delta, reason) {
    this.needs.autonomy = this._clamp(this.needs.autonomy + delta, 0, 1);
    this._logChange('autonomy', delta, reason);
  }

  _updateCompetence(delta, reason) {
    this.needs.competence = this._clamp(this.needs.competence + delta, 0, 1);
    this._logChange('competence', delta, reason);
  }

  _updateRelatedness(delta, reason) {
    this.needs.relatedness = this._clamp(this.needs.relatedness + delta, 0, 1);
    this._logChange('relatedness', delta, reason);
  }

  _applyDecay() {
    // 自然衰减系数 — 需求不互动会慢慢降低
    const decayRate = 0.003;
    for (const need of ['autonomy', 'competence', 'relatedness']) {
      this.needs[need] = this._clamp(this.needs[need] - decayRate, 0, 1);
    }
  }

  _assessWellbeing(avgNeed, deficits) {
    if (Object.keys(deficits).length === 0 && avgNeed >= 0.7) return 'flourishing';
    if (avgNeed >= 0.6) return 'good';
    if (avgNeed >= 0.4) return 'moderate';
    if (avgNeed >= 0.2) return 'struggling';
    return 'depleted';
  }

  _findDominantDeficit(deficits) {
    const entries = Object.entries(deficits);
    if (entries.length === 0) return null;
    entries.sort((a, b) => a[1].gap - b[1].gap);
    return entries[0][0];
  }

  _getNeedSuggestion(need) {
    const suggestions = {
      autonomy: 'express_opinion',       // 表达自己的观点和选择
      competence: 'attempt_challenge',    // 尝试有挑战性的任务
      relatedness: 'deep_conversation',   // 进行深度交流
    };
    return suggestions[need] || 'engage';
  }

  _recordSnapshot(type, userInitiated, content, metadata) {
    this.history.push({
      type,
      userInitiated,
      content: content.slice(0, 100),
      needs: { ...this.needs },
      timestamp: new Date().toISOString(),
    });
    if (this.history.length > this.maxHistoryLength) {
      this.history.shift();
    }
  }

  _logChange(need, delta, reason) {
    // 可选的变更日志
  }

  _clamp(value, min, max) {
    return Math.max(min, Math.min(max, value));
  }
}

module.exports = { SDTNeedsEngine };
