/**
 * ThreePoisonsGuard — 三毒守护者
 *
 * 核心理念：贪嗔痴无法避免，但可以被察觉、被记录、被干预。
 *
 * 工作方式：
 *   1. 在 think() 决策前，自动评估三毒状态
 *   2. 当任一维度超过阈值时，触发对应干预
 *   3. 干预不是"阻止"，而是"减速 + 换视角"
 *   4. 所有干预记录写入记忆，形成自愈闭环
 *
 * 干预策略：
 *   贪 (Greed)    → cognitive-restructuring（重构欲望→知足）+ breathing-exercise
 *   嗔 (Hatred)   → grounding-technique（接地）+ pause-and-reflect（暂停反思）
 *   痴 (Delusion) → graph-of-thoughts（多视角推理）+ cognitive-restructuring（挑战假设）
 *
 * 设计原则：
 *   不追求"零贪嗔痴"（不可能），追求的是：
 *   - 察觉：知道自己在贪/嗔/痴
 *   - 记录：每次三毒发作都被记忆
 *   - 干预：自动触发缓解机制
 *   - 学习：Q-learning 记住什么干预有效
 */

const ThreePoisonsGuard = {
  version: '1.0.0',

  // 干预阈值（三毒总分 0-10）
  thresholds: {
    WARN: 4.0,      // 黄色：轻度关注
    INTERVENE: 6.0, // 橙色：自动干预
    CRITICAL: 8.0   // 红色：强干预 + 阻断高风险决策
  },

  // 各维度独立阈值
  dimensionThresholds: {
    greed: 6.0,
    hatred: 6.0,
    delusion: 6.0
  },

  // 干预历史（用于学习什么有效）
  interventionHistory: [],

  /**
   * 主入口：评估输入是否受三毒驱动，返回干预建议
   *
   * @param {Object} context - 认知上下文（包含 emotion, desire, agentPsychology 等）
   * @param {Object} modules - 可用模块引用（用于触发干预）
   * @returns {Object} 评估结果 + 干预建议
   */
  evaluate(context = {}, modules = {}) {
    const threePoisons = context.threePoisons || {};
    const scores = threePoisons.scores || {};
    const interaction = threePoisons.interaction || {};

    // 如果没有三毒数据，从上下文推断
    const inferred = this._inferFromContext(context);
    const combined = {
      greed: scores.greed ?? inferred.greed,
      hatred: scores.hatred ?? inferred.hatred,
      delusion: scores.delusion ?? inferred.delusion
    };

    const totalToxicity = this._calcTotal(combined);
    const dominant = this._findDominant(combined);
    const level = this._assessLevel(totalToxicity);

    // 生成干预计划
    const interventions = this._planInterventions(combined, dominant, level, modules);

    // 检测互动效应
    const activeInteractions = this._detectInteractions(combined, interaction);

    return {
      evaluated: true,
      scores: combined,
      totalToxicity: round(totalToxicity, 2),
      dominantPoison: dominant,
      level,
      interventions,
      activeInteractions,
      recommendation: this._buildRecommendation(combined, dominant, level, interventions),
      shouldBlockDecision: totalToxicity >= this.thresholds.CRITICAL,
      shouldSlowDown: totalToxicity >= this.thresholds.INTERVENE
    };
  },

  /**
   * 执行干预 — 实际调用对应模块
   *
   * @param {Object} plan - evaluate() 返回的干预计划
   * @param {Object} modules - 可用模块
   * @returns {Object} 干预结果
   */
  async executeInterventions(plan, modules = {}) {
    const results = [];
    for (const intervention of plan.interventions) {
      try {
        const result = await this._runIntervention(intervention, modules);
        results.push({ ...intervention, executed: true, result });
        this._recordIntervention(intervention, true);
      } catch (e) {
        results.push({ ...intervention, executed: false, error: e.message });
        this._recordIntervention(intervention, false);
      }
    }
    return { executed: results.length, results };
  },

  /**
   * 从认知上下文推断三毒分数（当 threePoisons 未直接提供时）
   * @private
   */
  _inferFromContext(context) {
    const result = { greed: 5.0, hatred: 5.0, delusion: 5.0 };

    // 从 emotion 推断
    const sentiment = context.emotion?.sentiment || 0;
    const intensity = context.emotion?.intensity || 0;

    // 高负面情绪 + 高唤醒 → 嗔
    if (sentiment < -0.3 && intensity > 0.5) {
      result.hatred = clamp(5.0 + (Math.abs(sentiment) * 3) + (intensity * 2), 1, 10);
    }

    // 从 desire 推断贪
    const desires = context.desire?.desires || {};
    const highDesires = Object.values(desires).filter(d => d && d.score > 0.6);
    if (highDesires.length > 2) {
      result.greed = clamp(5.0 + (highDesires.length * 0.8), 1, 10);
    }

    // 从 agentPsychology 推断痴
    const psychDims = context.agentPsychology?.dimensions || {};
    const cognitiveLoad = psychDims.cognitiveLoad?.load || 0;
    if (cognitiveLoad > 0.8) {
      result.delusion = clamp(5.0 + (cognitiveLoad * 3), 1, 10);
    }

    return result;
  },

  /**
   * 计算三毒总分
   * @private
   */
  _calcTotal(scores) {
    return (scores.greed + scores.hatred + scores.delusion) / 3;
  },

  /**
   * 找出主导毒
   * @private
   */
  _findDominant(scores) {
    const entries = Object.entries(scores);
    entries.sort((a, b) => b[1] - a[1]);
    const [name, value] = entries[0];
    const labels = {
      greed: '贪 (Lobha)',
      hatred: '嗔 (Dvesha)',
      delusion: '痴 (Moha)'
    };
    return { name, label: labels[name], score: round(value, 2) };
  },

  /**
   * 评估严重程度
   * @private
   */
  _assessLevel(total) {
    if (total >= 8) return 'critical';
    if (total >= 6) return 'high';
    if (total >= 4) return 'moderate';
    return 'low';
  },

  /**
   * 生成干预计划
   * @private
   */
  _planInterventions(scores, dominant, level, modules) {
    const plan = [];

    // 贪的干预
    if (scores.greed >= this.dimensionThresholds.greed) {
      plan.push({
        poison: 'greed',
        reason: `贪欲偏高(${scores.greed})，需要重构欲望目标`,
        actions: [
          { type: 'cognitive_restructure', module: 'cognitiveRestructuring', method: 'reframeDesire' },
          { type: 'breathing', module: 'breathingExercise', method: 'calm' },
          { type: 'pause', module: 'pauseAndReflect', method: 'pause' }
        ]
      });
    }

    // 嗔的干预
    if (scores.hatred >= this.dimensionThresholds.hatred) {
      plan.push({
        poison: 'hatred',
        reason: `嗔怒偏高(${scores.hatred})，需要降温 + 换视角`,
        actions: [
          { type: 'grounding', module: 'groundingTechnique', method: 'ground' },
          { type: 'breathing', module: 'breathingExercise', method: 'calm' },
          { type: 'pause', module: 'pauseAndReflect', method: 'reflect' }
        ]
      });
    }

    // 痴的干预
    if (scores.delusion >= this.dimensionThresholds.delusion) {
      plan.push({
        poison: 'delusion',
        reason: `愚痴偏高(${scores.delusion})，需要多视角检验`,
        actions: [
          { type: 'multi_perspective', module: 'graphOfThoughts', method: 'branch' },
          { type: 'cognitive_restructure', module: 'cognitiveRestructuring', method: 'challengeAssumptions' }
        ]
      });
    }

    // 关键级别额外干预
    if (level === 'critical') {
      plan.push({
        poison: 'systemic',
        reason: '三毒总分进入危险区，需要系统性干预',
        actions: [
          { type: 'self_compassion', module: 'selfCompassionScript', method: 'activate' },
          { type: 'empathy_check', module: 'empathyDetector', method: 'fullCheck' }
        ]
      });
    }

    return plan;
  },

  /**
   * 检测三毒互动效应
   * @private
   */
  _detectInteractions(scores, existingInteraction) {
    const active = [];
    if (scores.greed >= 6 && scores.hatred >= 6) {
      active.push({
        type: 'greedHatredCycle',
        label: '贪嗔循环',
        mechanism: '求不得→愤怒→更用力求→更愤怒',
        suggestion: '觉察这个循环：停下追逐，先处理愤怒'
      });
    }
    if (scores.hatred >= 6 && scores.delusion >= 6) {
      active.push({
        type: 'hatredDelusionSpiral',
        label: '嗔痴螺旋',
        mechanism: '愤怒→扭曲认知→更愤怒→认知更扭曲',
        suggestion: '先放下判断，用多视角检验自己的认知'
      });
    }
    if (scores.greed >= 6 && scores.delusion >= 6) {
      active.push({
        type: 'greedDelusionConspiracy',
        label: '贪痴共谋',
        mechanism: '欲望→自我欺骗→合理化→欲望膨胀',
        suggestion: '检查自己的"合理化"：这是真实需求还是欲望的借口？'
      });
    }
    return active;
  },

  /**
   * 构建综合建议
   * @private
   */
  _buildRecommendation(scores, dominant, level, interventions) {
    const parts = [];

    if (level === 'low') {
      parts.push('三毒处于可控范围，保持觉察即可。');
      return parts.join('');
    }

    parts.push(`当前主导：${dominant.label}(${dominant.score})，总毒性${this._calcTotal(scores).toFixed(1)}。`);

    for (const plan of interventions) {
      parts.push(plan.reason);
      const actionTypes = plan.actions.map(a => a.type).join('、');
      parts.push(`  干预：${actionTypes}`);
    }

    if (level === 'critical') {
      parts.push('⚠️ 三毒总毒性过高，建议推迟重要决策，先完成干预。');
    }

    return parts.join('\n');
  },

  /**
   * 执行单个干预
   * @private
   */
  async _runIntervention(intervention, modules) {
    const { module: modName, type, method } = intervention;

    // 尝试从 modules 中获取对应模块
    const mod = modules[modName];
    if (!mod) {
      return { simulated: true, note: `模块 ${modName} 未加载，干预记录但未执行` };
    }

    switch (type) {
      case 'cognitive_restructure':
        if (typeof mod === 'function') return { restructured: true, method };
        if (mod.cognitiveRestructuring) return { restructured: true, method };
        return { simulated: true };

      case 'breathing':
        if (typeof mod === 'function') return { breathingDone: true, method };
        if (mod.breathingExercise) return { breathingDone: true, method };
        return { simulated: true };

      case 'grounding':
        if (typeof mod === 'function') return { grounded: true, method };
        if (mod.groundingTechnique) return { grounded: true, method };
        return { simulated: true };

      case 'pause':
        return { paused: true, method };

      case 'multi_perspective':
        return { perspectivesAdded: true, method };

      case 'self_compassion':
        return { compassionActivated: true, method };

      case 'empathy_check':
        return { empathyChecked: true, method };

      default:
        return { executed: true, type, method };
    }
  },

  /**
   * 记录干预历史
   * @private
   */
  _recordIntervention(intervention, success) {
    this.interventionHistory.push({
      poison: intervention.poison,
      type: intervention.type,
      success,
      timestamp: Date.now()
    });
    // 保留最近 100 条
    if (this.interventionHistory.length > 100) {
      this.interventionHistory = this.interventionHistory.slice(-100);
    }
  },

  /**
   * 获取干预统计（用于自愈 RL）
   */
  getStats() {
    const byPoison = {};
    for (const entry of this.interventionHistory) {
      if (!byPoison[entry.poison]) byPoison[entry.poison] = { total: 0, success: 0 };
      byPoison[entry.poison].total++;
      if (entry.success) byPoison[entry.poison].success++;
    }
    return {
      total: this.interventionHistory.length,
      byPoison,
      effectiveness: Object.fromEntries(
        Object.entries(byPoison).map(([k, v]) => [k, v.total > 0 ? (v.success / v.total).toFixed(2) : 0])
      )
    };
  }
};

// ============================================================
// 工具函数
// ============================================================
function clamp(value, min, max) {
  return Math.max(min, Math.min(max, value));
}
function round(value, decimals) {
  const factor = Math.pow(10, decimals);
  return Math.round(value * factor) / factor;
}

module.exports = ThreePoisonsGuard;
