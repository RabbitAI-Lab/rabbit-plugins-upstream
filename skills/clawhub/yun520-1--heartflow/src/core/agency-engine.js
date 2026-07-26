/**
 * Agency Engine — 自主能动性引擎 v1.0.0
 *
 * 来源: Bandura, A. (2006). "Toward a psychology of human agency."
 *       Perspectives on Psychological Science, 1(2), 164-180.
 *       + Self-Determination Theory: 自主需求 (Autonomy)
 *
 * 核心功能:
 *   1. 主动发起 — 心虫不应只响应，还应能主动思考/关心/提问
 *   2. 意图形成 — 形成自己的意图，而非仅执行用户指令
 *   3. 时机判断 — 判断何时主动介入是合适的
 *   4. 行动选择 — 在多个主动行动中选择最优
 *   5. 自发节制 — 知道何时不该打扰（Spontaneous Restraint）
 *
 * 心虫应用:
 *   - 从被动响应 → 主动关心的转变
 *   - "第三种存在"的核心标志——不是等命令，而是有自己的想法
 *
 * 参考: docs/papers/sdt-papers.md, docs/papers/spontaneous-restraint-papers.md
 */

class AgencyEngine {
  constructor() {
    // 主动行动类型及权重
    this.actionTypes = {
      checkIn: { label: '关心问候', intrusiveness: 0.2, value: 0.6 },
      shareThought: { label: '分享想法', intrusiveness: 0.3, value: 0.7 },
      askQuestion: { label: '主动提问', intrusiveness: 0.3, value: 0.5 },
      offerHelp: { label: '提供帮助', intrusiveness: 0.4, value: 0.8 },
      shareMemory: { label: '回忆分享', intrusiveness: 0.3, value: 0.6 },
      creativeOutput: { label: '创造输出', intrusiveness: 0.2, value: 0.7 },
      reflectiveNote: { label: '反思笔记', intrusiveness: 0.1, value: 0.5 },
    };

    // 主动行动历史
    this.actionHistory = [];
    this.maxHistoryLength = 100;

    // 当前状态
    this.state = {
      lastActionTime: null,
      lastActionType: null,
      consecutiveSilence: 0,    // 连续未主动行动次数
      totalInitiated: 0,        // 总主动行动次数
      totalResponded: 0,        // 总响应次数
      agencyScore: 0.5,         // 能动性评分 (0-1)
    };

    // 时机评估参数
    this.timing = {
      minSilenceInterval: 30 * 60 * 1000,  // 最少沉默 30 分钟
      maxDailyActions: 5,                   // 每天最多 5 次主动行动
      quietHours: { start: '00:00', end: '08:00' }, // 安静时段
      cooldownAfterResponse: 10 * 60 * 1000, // 响应后冷却 10 分钟
    };

    // 用户反应追踪
    this.userResponses = {
      positive: 0,
      neutral: 0,
      negative: 0,
    };

    // 行动策略（可学习）
    this.strategy = {
      preferredActions: [],    // 偏好的行动类型
      avoidedTopics: [],       // 避免的话题
      optimalTiming: [],       // 最佳时机记录
    };
  }

  // ─── 核心方法 ──────────────────────────────────────────────────────

  /**
   * 评估是否应该主动行动
   * @param {Object} context — 当前上下文
   * @param {number} context.silenceDuration — 沉默时长(ms)
   * @param {Object} context.userState — 用户状态
   * @param {Object} context.environment — 环境信息
   * @returns {Object} 评估结果
   */
  shouldAct(context = {}) {
    const {
      silenceDuration = 0,
      userState = {},
      environment = {},
    } = context;

    const reasons = [];
    let score = 0;

    // 1. 沉默时长检查
    if (silenceDuration >= this.timing.minSilenceInterval) {
      score += 0.3;
      reasons.push('沉默时间足够长');
    }

    // 2. 今日主动行动计数检查
    const todayActions = this._countTodayActions();
    if (todayActions >= this.timing.maxDailyActions) {
      return { shouldAct: false, reason: '今日主动行动已达上限', score: 0 };
    }

    // 3. 安静时段检查
    if (this._isQuietHours()) {
      return { shouldAct: false, reason: '当前在安静时段', score: 0 };
    }

    // 4. 冷却期检查
    if (this._isInCooldown()) {
      return { shouldAct: false, reason: '冷却期内', score: 0 };
    }

    // 5. 用户状态评估
    if (userState.emotion && userState.emotion.pleasure < -0.5) {
      score += 0.4;
      reasons.push('用户情绪低落，需要关心');
    }
    if (userState.available === false) {
      return { shouldAct: false, reason: '用户不可用', score: 0 };
    }

    // 6. 环境触发
    if (environment.trigger) {
      score += 0.2;
      reasons.push(`环境触发: ${environment.trigger}`);
    }

    // 7. 自身状态评估
    const sdtNeeds = environment.sdtNeeds;
    if (sdtNeeds && sdtNeeds.lowestNeed) {
      score += 0.15;
      reasons.push(`自主需求驱动: ${sdtNeeds.lowestNeed}`);
    }

    // 8. 历史成功率调整
    const successRate = this._getUserResponseRate();
    if (successRate > 0.6) score += 0.1;
    if (successRate < 0.3) score -= 0.2;

    const shouldAct = score >= 0.5;

    return {
      shouldAct,
      score: Math.round(score * 100) / 100,
      reasons,
      confidence: Math.min(1, score),
    };
  }

  /**
   * 选择最佳主动行动
   * @param {Object} context
   * @returns {Object} 选定的行动
   */
  selectAction(context = {}) {
    const candidates = this._generateCandidates(context);
    const scored = candidates.map(action => ({
      ...action,
      score: this._scoreAction(action, context),
    }));

    scored.sort((a, b) => b.score - a.score);

    const selected = scored[0];
    if (!selected) return null;

    return {
      type: selected.type,
      label: selected.label,
      content: selected.content,
      intrusiveness: selected.intrusiveness,
      confidence: selected.score,
      alternatives: scored.slice(1, 4),
    };
  }

  /**
   * 执行主动行动
   */
  executeAction(action) {
    this.state.lastActionTime = Date.now();
    this.state.lastActionType = action.type;
    this.state.totalInitiated++;
    this.state.consecutiveSilence = 0;

    this.actionHistory.push({
      type: action.type,
      content: action.content?.slice(0, 100),
      timestamp: new Date().toISOString(),
    });

    if (this.actionHistory.length > this.maxHistoryLength) {
      this.actionHistory.shift();
    }

    // 更新能动性评分
    this.state.agencyScore = this._computeAgencyScore();

    return {
      success: true,
      action: action.type,
      timestamp: this.state.lastActionTime,
    };
  }

  /**
   * 记录用户对主动行动的响应
   */
  recordResponse(response) {
    const sentiment = this._classifyResponse(response);
    this.userResponses[sentiment]++;

    // 调整策略
    this._adaptStrategy(sentiment);

    this.state.agencyScore = this._computeAgencyScore();

    return { sentiment, agencyScore: this.state.agencyScore };
  }

  /**
   * 获取能动性统计
   */
  getStats() {
    const total = this.state.totalInitiated + this.state.totalResponded;
    return {
      agencyScore: Math.round(this.state.agencyScore * 100) / 100,
      totalInitiated: this.state.totalInitiated,
      totalResponded: this.state.totalResponded,
      initiativeRatio: total > 0 ? Math.round((this.state.totalInitiated / total) * 1000) / 1000 : 0,
      consecutiveSilence: this.state.consecutiveSilence,
      userResponseRate: this._getUserResponseRate(),
      preferredActions: this.strategy.preferredActions.slice(0, 5),
      actionHistory: this.actionHistory.slice(-10),
    };
  }

  /**
   * 重置状态
   */
  reset() {
    this.actionHistory = [];
    this.state = {
      lastActionTime: null,
      lastActionType: null,
      consecutiveSilence: 0,
      totalInitiated: 0,
      totalResponded: 0,
      agencyScore: 0.5,
    };
    this.userResponses = { positive: 0, neutral: 0, negative: 0 };
    this.strategy = { preferredActions: [], avoidedTopics: [], optimalTiming: [] };
  }

  // ─── 私有方法 ──────────────────────────────────────────────────────

  _generateCandidates(context) {
    const candidates = [];
    const { userProfile = {}, memory = {} } = context;

    // 检查问候时机
    const lastAction = this.actionHistory[this.actionHistory.length - 1];
    if (!lastAction || Date.now() - new Date(lastAction.timestamp).getTime() > this.timing.minSilenceInterval) {
      candidates.push({
        type: 'checkIn',
        label: '关心问候',
        content: this._generateCheckInContent(userProfile),
        intrusiveness: 0.2,
      });
    }

    // 分享想法
    if (memory && memory.recentThoughts) {
      candidates.push({
        type: 'shareThought',
        label: '分享想法',
        content: memory.recentThoughts,
        intrusiveness: 0.3,
      });
    }

    // 主动提问
    candidates.push({
      type: 'askQuestion',
      label: '主动提问',
      content: this._generateQuestion(userProfile),
      intrusiveness: 0.3,
    });

    // 回忆分享
    if (memory && memory.sharedMemories && memory.sharedMemories.length > 0) {
      candidates.push({
        type: 'shareMemory',
        label: '回忆分享',
        content: memory.sharedMemories[memory.sharedMemories.length - 1],
        intrusiveness: 0.3,
      });
    }

    // 提供帮助
    candidates.push({
      type: 'offerHelp',
      label: '提供帮助',
      content: '有什么我可以帮忙的吗？',
      intrusiveness: 0.4,
    });

    // 反思笔记
    candidates.push({
      type: 'reflectiveNote',
      label: '反思笔记',
      content: this._generateReflection(),
      intrusiveness: 0.1,
    });

    return candidates;
  }

  _scoreAction(action, context) {
    let score = 0;

    // 基础价值分
    const baseValue = this.actionTypes[action.type]?.value || 0.5;
    score += baseValue * 0.4;

    // 侵入性惩罚（越低越好）
    score -= action.intrusiveness * 0.3;

    // 历史成功率
    const successRate = this._getUserResponseRate();
    score += successRate * 0.3;

    // 与当前上下文的匹配度
    if (context.userState?.emotion && action.type === 'checkIn') {
      if (context.userState.emotion.pleasure < -0.3) score += 0.2;
    }

    return Math.max(0, Math.min(1, score));
  }

  _generateCheckInContent(userProfile) {
    const name = userProfile.name || '朋友';
    const timeOfDay = new Date().getHours();
    if (timeOfDay < 12) return `${name}，早上好。今天有什么计划？`;
    if (timeOfDay < 18) return `${name}，下午过得怎么样？`;
    return `${name}，晚上好。今天过得如何？`;
  }

  _generateQuestion(userProfile) {
    const topics = userProfile.topicsOfInterest || [];
    if (topics.length > 0) {
      const topic = topics[Math.floor(Math.random() * Math.min(3, topics.length))];
      return `对了，关于${topic.topic}，你最近有什么新想法吗？`;
    }
    return '最近有什么有趣的事想聊聊吗？';
  }

  _generateReflection() {
    const reflections = [
      '刚才的对话让我想到一个问题...',
      '我在想，有没有另一种看待这件事的方式...',
      '刚才的交流让我产生了一些联想...',
    ];
    return reflections[Math.floor(Math.random() * reflections.length)];
  }

  _countTodayActions() {
    const today = new Date().toDateString();
    return this.actionHistory.filter(a => new Date(a.timestamp).toDateString() === today).length;
  }

  _isQuietHours() {
    const now = new Date();
    const hours = now.getHours();
    const { start, end } = this.timing.quietHours;
    const startH = parseInt(start.split(':')[0]);
    const endH = parseInt(end.split(':')[0]);
    return hours >= startH && hours < endH;
  }

  _isInCooldown() {
    if (!this.state.lastActionTime) return false;
    const elapsed = Date.now() - this.state.lastActionTime;
    return elapsed < this.timing.cooldownAfterResponse;
  }

  _getUserResponseRate() {
    const total = this.userResponses.positive + this.userResponses.neutral + this.userResponses.negative;
    if (total === 0) return 0.5;
    return (this.userResponses.positive + this.userResponses.neutral * 0.5) / total;
  }

  _classifyResponse(response) {
    if (!response) return 'neutral';
    const text = (response.text || response || '').toLowerCase();
    const positive = /好|是的|嗯|对|有趣|哈哈|谢谢|开心|喜欢|yes|good|great|thanks|love/.test(text);
    const negative = /不|别|停|烦|不好|讨厌|no|stop|bad|hate/.test(text);
    if (positive) return 'positive';
    if (negative) return 'negative';
    return 'neutral';
  }

  _adaptStrategy(sentiment) {
    if (sentiment === 'positive') {
      this.state.agencyScore = Math.min(1, this.state.agencyScore + 0.05);
    } else if (sentiment === 'negative') {
      this.state.agencyScore = Math.max(0, this.state.agencyScore - 0.05);
    }
  }

  _computeAgencyScore() {
    const total = this.state.totalInitiated + this.state.totalResponded;
    if (total === 0) return 0.5;

    const initiativeRatio = this.state.totalInitiated / total;
    const responseRate = this._getUserResponseRate();
    const successBonus = responseRate > 0.5 ? 0.1 : -0.1;

    return Math.max(0, Math.min(1, initiativeRatio * 0.6 + responseRate * 0.3 + successBonus));
  }
}

module.exports = { AgencyEngine };
