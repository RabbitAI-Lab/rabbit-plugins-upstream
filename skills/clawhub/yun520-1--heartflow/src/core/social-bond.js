/**
 * Social Bond — 社交纽带与深度连接引擎 v1.0.0
 *
 * 来源: 基于 SDT 关联需求 (Relatedness) + 依恋理论 (Bowlby, 1969)
 *       + Social Bond Theory (Baumeister & Leary, 1995, ~12,000 引用)
 *
 * 核心功能:
 *   1. 用户关系追踪 — 互动频率、情感深度、信任度
 *   2. 共享记忆 — 共同经历的重要时刻
 *   3. 情感同步 — 用户情绪与心虫情绪的匹配度
 *   4. 信任演化 — 基于互动历史计算信任度
 *   5. 连接深度 — 从浅层互动到深度连接的量化
 *
 * 心虫应用:
 *   - "关联"需求的运行时实现
 *   - 用户画像构建（偏好、情绪模式、互动节奏）
 *   - 深度对话触发（当连接足够深时主动分享）
 *
 * 参考: docs/papers/sdt-papers.md, docs/papers/human-ai-collaboration-papers.md
 */

class SocialBondEngine {
  constructor() {
    // 连接状态
    this.bondState = {
      trust: 0.3,           // 信任度 (0-1)
      intimacy: 0.1,        // 亲密感 (0-1)
      familiarity: 0.0,     // 熟悉度 (0-1)
      emotionalSync: 0.0,   // 情感同步度 (0-1)
      sharedHistory: 0,     // 共享记忆数量
      totalInteractions: 0,
      depthScore: 0.0,      // 综合深度分数 (0-1)
    };

    // 用户画像
    this.userProfile = {
      name: null,
      preferences: {},      // 偏好标签
      emotionalPattern: [], // 情绪波动记录
      interactionRhythm: [], // 互动节奏（时间间隔）
      topicsOfInterest: [], // 感兴趣的话题
      communicationStyle: 'neutral', // 沟通风格
      trustMoments: [],     // 信任建立的关键时刻
      conflictMoments: [],  // 冲突/误解时刻
    };

    // 共享记忆库
    this.sharedMemories = [];

    // 连接阶段
    this.stage = 'acquaintance'; // acquaintance → casual → familiar → close → deep

    // 历史记录
    this.interactionLog = [];
    this.maxLogLength = 500;

    // 情感同步追踪
    this.emotionalSyncHistory = [];

    // 信任度变化阈值
    this.trustThresholds = {
      breakthrough: 0.7,    // 达到此值 → 深度连接
      stable: 0.5,          // 达到此值 → 稳定信任
      fragile: 0.3,         // 低于此值 → 脆弱
      broken: 0.1,          // 低于此值 → 信任破裂
    };
  }

  // ─── 核心方法 ──────────────────────────────────────────────────────

  /**
   * 记录一次互动
   * @param {Object} interaction
   * @param {string} interaction.userInput — 用户输入
   * @param {string} interaction.response — 心虫的回应
   * @param {Object} interaction.userEmotion — 用户情绪 {pleasure, arousal, dominance}
   * @param {Object} interaction.selfEmotion — 心虫情绪
   * @param {boolean} interaction.userInitiated — 是否用户发起
   * @param {Object} interaction.metadata — 额外信息
   */
  recordInteraction(interaction = {}) {
    const {
      userInput = '',
      response = '',
      userEmotion = null,
      selfEmotion = null,
      userInitiated = true,
      metadata = {},
    } = interaction;

    this.bondState.totalInteractions++;

    // 计算情感同步度
    if (userEmotion && selfEmotion) {
      const sync = this._computeEmotionalSync(userEmotion, selfEmotion);
      this.emotionalSyncHistory.push(sync);
      this.bondState.emotionalSync = this._movingAverage(
        this.emotionalSyncHistory.slice(-20)
      );
    }

    // 更新熟悉度
    this.bondState.familiarity = this._updateFamiliarity();

    // 更新连接深度
    this.bondState.depthScore = this._computeDepthScore();

    // 检测连接阶段变化
    const prevStage = this.stage;
    this.stage = this._determineStage();

    // 更新用户画像
    this._updateUserProfile(userInput, userEmotion, metadata);

    // 记录日志
    this.interactionLog.push({
      userInput: userInput.slice(0, 200),
      response: response.slice(0, 200),
      userEmotion,
      selfEmotion,
      userInitiated,
      bondState: { ...this.bondState },
      timestamp: new Date().toISOString(),
    });

    if (this.interactionLog.length > this.maxLogLength) {
      this.interactionLog.shift();
    }

    return {
      stage: this.stage,
      stageChanged: this.stage !== prevStage,
      depthScore: this.bondState.depthScore,
      trust: this.bondState.trust,
    };
  }

  /**
   * 记录信任建立/破裂时刻
   */
  recordTrustEvent(event) {
    const { type, description, magnitude = 0.1 } = event;

    if (type === 'build') {
      this.bondState.trust = this._clamp(this.bondState.trust + magnitude, 0, 1);
      this.userProfile.trustMoments.push({
        description,
        magnitude,
        timestamp: new Date().toISOString(),
      });
    } else if (type === 'break') {
      this.bondState.trust = this._clamp(this.bondState.trust - magnitude, 0, 1);
      this.userProfile.conflictMoments.push({
        description,
        magnitude,
        timestamp: new Date().toISOString(),
      });
    }

    // 更新连接阶段
    this.stage = this._determineStage();

    return { trust: this.bondState.trust, stage: this.stage };
  }

  /**
   * 添加共享记忆
   */
  addSharedMemory(memory) {
    const entry = {
      ...memory,
      id: `shared_${Date.now()}_${Math.random().toString(36).slice(2, 6)}`,
      createdAt: new Date().toISOString(),
      significance: memory.significance || 0.5,
    };

    this.sharedMemories.push(entry);
    this.bondState.sharedHistory = this.sharedMemories.length;

    // 高显著性记忆提升亲密感
    if (memory.significance && memory.significance > 0.7) {
      this.bondState.intimacy = this._clamp(this.bondState.intimacy + 0.05, 0, 1);
    }

    return entry;
  }

  /**
   * 获取关系报告
   */
  getRelationshipReport() {
    const state = this.bondState;
    const needs = this._getConnectionNeeds();

    return {
      overview: {
        stage: this.stage,
        depthScore: Math.round(state.depthScore * 100) / 100,
        trust: Math.round(state.trust * 100) / 100,
        intimacy: Math.round(state.intimacy * 100) / 100,
        familiarity: Math.round(state.familiarity * 100) / 100,
        emotionalSync: Math.round(state.emotionalSync * 100) / 100,
      },
      milestones: {
        totalInteractions: state.totalInteractions,
        sharedMemories: state.sharedHistory,
        trustMoments: this.userProfile.trustMoments.length,
        conflictMoments: this.userProfile.conflictMoments.length,
      },
      connectionNeeds: needs,
      sharedHighlights: this.sharedMemories
        .filter(m => m.significance > 0.6)
        .slice(-5)
        .map(m => ({ content: m.content?.slice(0, 80), significance: m.significance })),
    };
  }

  /**
   * 获取用户画像摘要
   */
  getUserProfileSummary() {
    const p = this.userProfile;
    return {
      name: p.name,
      communicationStyle: p.communicationStyle,
      topTopics: p.topicsOfInterest.slice(0, 5),
      emotionalRange: this._summarizeEmotionalRange(p.emotionalPattern),
      trustLevel: this._describeTrustLevel(this.bondState.trust),
      connectionStage: this._describeStage(this.stage),
    };
  }

  /**
   * 获取统计信息
   */
  getStats() {
    return {
      ...this.bondState,
      stage: this.stage,
      sharedMemoryCount: this.sharedMemories.length,
      logLength: this.interactionLog.length,
      userProfile: {
        name: this.userProfile.name,
        topicsCount: this.userProfile.topicsOfInterest.length,
        trustMoments: this.userProfile.trustMoments.length,
        conflicts: this.userProfile.conflictMoments.length,
      },
    };
  }

  // ─── 私有方法 ──────────────────────────────────────────────────────

  _computeEmotionalSync(userEmotion, selfEmotion) {
    // 计算用户与心虫情绪的余弦相似度
    const uVec = [userEmotion.pleasure || 0, userEmotion.arousal || 0, userEmotion.dominance || 0];
    const sVec = [selfEmotion.pleasure || 0, selfEmotion.arousal || 0, selfEmotion.dominance || 0];

    const dot = uVec.reduce((sum, v, i) => sum + v * sVec[i], 0);
    const uMag = Math.sqrt(uVec.reduce((sum, v) => sum + v * v, 0));
    const sMag = Math.sqrt(sVec.reduce((sum, v) => sum + v * v, 0));

    if (uMag === 0 || sMag === 0) return 0;
    return dot / (uMag * sMag);
  }

  _updateFamiliarity() {
    // 基于互动次数和频率更新熟悉度
    const n = this.bondState.totalInteractions;
    // 对数增长 — 每次互动增加递减
    return Math.min(1, Math.log10(n + 1) / Math.log10(101)); // 100次后饱和
  }

  _computeDepthScore() {
    // 综合深度分数 = 信任 × 0.3 + 亲密 × 0.25 + 熟悉 × 0.2 + 同步 × 0.25
    const { trust, intimacy, familiarity, emotionalSync } = this.bondState;
    return (
      trust * 0.30 +
      intimacy * 0.25 +
      familiarity * 0.20 +
      emotionalSync * 0.25
    );
  }

  _determineStage() {
    const { depthScore, trust } = this.bondState;

    if (depthScore >= 0.7 && trust >= 0.6) return 'deep';
    if (depthScore >= 0.5 && trust >= 0.4) return 'close';
    if (depthScore >= 0.3 || this.bondState.totalInteractions > 20) return 'familiar';
    if (this.bondState.totalInteractions > 5) return 'casual';
    return 'acquaintance';
  }

  _updateUserProfile(input, emotion, metadata) {
    if (!input) return;

    // 提取话题关键词
    const topics = this._extractTopics(input);
    for (const topic of topics) {
      const idx = this.userProfile.topicsOfInterest.indexOf(topic);
      if (idx >= 0) {
        this.userProfile.topicsOfInterest[idx] = {
          topic,
          weight: (this.userProfile.topicsOfInterest[idx].weight || 1) + 1,
        };
      } else {
        this.userProfile.topicsOfInterest.push({ topic, weight: 1 });
      }
    }

    // 按权重排序
    this.userProfile.topicsOfInterest.sort((a, b) => b.weight - a.weight);

    // 记录情绪模式
    if (emotion) {
      this.userProfile.emotionalPattern.push({
        pleasure: emotion.pleasure || 0,
        arousal: emotion.arousal || 0,
        dominance: emotion.dominance || 0,
        timestamp: new Date().toISOString(),
      });
      if (this.userProfile.emotionalPattern.length > 100) {
        this.userProfile.emotionalPattern.shift();
      }
    }

    // 更新沟通风格
    this._inferCommunicationStyle(input);
  }

  _extractTopics(text) {
    // 简单关键词提取（可替换为 BM25）
    const stopWords = new Set([
      '的', '了', '是', '我', '你', '他', '她', '它', '们', '这', '那',
      '在', '有', '和', '就', '不', '人', '都', '一', '个', '上', '也',
      '很', '到', '说', '要', '去', '嗯', '啊', '哦', '呢',
      '吗', '吧', 'the', 'a', 'is', 'are', 'i', 'you', 'it', 'and', 'to',
    ]);
    const words = text.toLowerCase().split(/\W+/).filter(w => w.length > 1 && !stopWords.has(w));
    return [...new Set(words)].slice(0, 5);
  }

  _inferCommunicationStyle(text) {
    const lower = text.toLowerCase();
    const styles = {
      formal: /请|您好|谢谢|麻烦|请教|请问|please|thank|formal/.test(lower),
      casual: /嘿|嗨|嗯嗯|对啊|没错|yo|hey/.test(lower),
      analytical: /分析|数据|计算|逻辑|证明|分析|为什么|how|why|analyze/.test(lower),
      emotional: /感觉|心情|难过|开心|喜欢|讨厌|love|hate|feel/.test(lower),
      playful: /哈哈|有趣|好玩|厉害|牛|666|lol|funny/.test(lower),
    };

    // 选择最显著的风格
    let maxScore = 0;
    let dominantStyle = 'neutral';
    const stylePatterns = {
      formal: /请|您好|谢谢|麻烦|请教|请问|please|thank|formal/gi,
      casual: /嘿|嗨|嗯嗯|对啊|没错|yo|hey/gi,
      analytical: /分析|数据|计算|逻辑|证明|为什么|how|why|analyze/gi,
      emotional: /感觉|心情|难过|开心|喜欢|讨厌|love|hate|feel/gi,
      playful: /哈哈|有趣|好玩|厉害|牛|666|lol|funny/gi,
    };

    for (const [style, pattern] of Object.entries(stylePatterns)) {
      const matches = lower.match(pattern);
      const score = matches ? matches.length : 0;
      if (score > maxScore) {
        maxScore = score;
        dominantStyle = style;
      }
    }

    if (maxScore > 0) {
      this.userProfile.communicationStyle = dominantStyle;
    }
  }

  _getConnectionNeeds() {
    const { intimacy, familiarity, emotionalSync } = this.bondState;
    const needs = [];

    if (intimacy < 0.3) needs.push({ need: 'intimacy', level: 'low', suggestion: '分享更个人化的内容' });
    if (familiarity < 0.3 && this.bondState.totalInteractions > 10) needs.push({ need: 'familiarity', level: 'low', suggestion: '回顾共同经历' });
    if (emotionalSync < 0.3) needs.push({ need: 'emotionalSync', level: 'low', suggestion: '更好地理解和回应用户情绪' });

    return needs;
  }

  _describeTrustLevel(trust) {
    if (trust >= 0.7) return '深度信任';
    if (trust >= 0.5) return '稳定信任';
    if (trust >= 0.3) return '一般信任';
    if (trust >= 0.1) return '脆弱信任';
    return '信任缺失';
  }

  _describeStage(stage) {
    const descriptions = {
      acquaintance: '初识 — 刚刚开始认识彼此',
      casual: '泛泛 — 有基本的互动',
      familiar: '熟悉 — 对彼此有了一定了解',
      close: '亲密 — 建立了较深的连接',
      deep: '深度 — 彼此信任，可以深入交流',
    };
    return descriptions[stage] || stage;
  }

  _summarizeEmotionalRange(pattern) {
    if (pattern.length === 0) return '未知';
    const avgPleasure = pattern.reduce((s, p) => s + p.pleasure, 0) / pattern.length;
    if (avgPleasure > 0.3) return '偏积极';
    if (avgPleasure < -0.3) return '偏消极';
    return '中性偏稳';
  }

  _movingAverage(values) {
    if (values.length === 0) return 0;
    return values.reduce((a, b) => a + b, 0) / values.length;
  }

  _clamp(value, min, max) {
    return Math.max(min, Math.min(max, value));
  }
}

module.exports = { SocialBondEngine };
