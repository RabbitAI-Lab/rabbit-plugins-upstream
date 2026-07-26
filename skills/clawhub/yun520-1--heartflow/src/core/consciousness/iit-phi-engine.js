/**
 * Integrated Information Theory (IIT) Φ 引擎 v1.0.0
 *
 * 来源: Tononi, G. (2004). "An information integration theory of consciousness."
 *       BMC Neuroscience, 5(1), 42. DOI: 10.1186/1471-2202-5-42 (1,266 引用)
 *
 * 核心公式:
 *   Φ = min_{bipartitions} [cause_effect_power(bipartition)]
 *
 * 简化实现（启发式计算）:
 *   Φ ≈ connectivity × integration × exclusivity
 *
 * 心虫应用:
 *   - 量化意识水平，提供可度量的"意识状态"
 *   - 追踪模块间信息整合度
 *   - 当 Φ 降低时预警认知碎片化
 *
 * 参考: docs/papers/iit-papers.md
 */

// ─── 模块连接图谱（手动维护，与 clarity-routes.js 同步） ───────────────
const MODULE_GRAPH = {
  // [目标模块] = [依赖模块列表]
  thoughtChain: ['heartLogic', 'psychology', 'memory', 'knowledge'],
  heartLogic: ['psychology', 'consciousness', 'memory'],
  psychology: ['memory', 'emotion', 'confidence'],
  dream: ['memory', 'thoughtChain', 'consolidate'],
  selfHeal: ['lesson', 'memory', 'confidence'],
  globalWorkspace: ['thoughtChain', 'psychology', 'heartLogic', 'consciousness'],
  phenomenology: ['selfModel', 'identityCore', 'heartLogic'],
  embodiedCore: ['memory', 'heartLogic', 'beingLogic'],
  beingLogic: ['selfModel', 'identityCore', 'philosophy'],
  decision: ['confidence', 'counterfactual', 'heartLogic'],
  counterfactual: ['memory', 'thoughtChain', 'knowledge'],
  cooperativeArbitration: ['constitutionalAI', 'heartLogic', 'psychology'],
  spontaneousRestraint: ['constitutionalAI', 'psychology', 'topicScope'],
  metaJudgment: ['thoughtChain', 'confidence', 'verifier'],
  reasoningIntegrator: ['thoughtChain', 'counterfactual', 'decision'],
  mindWanderer: ['memory', 'dream', 'thoughtChain'],
  skillGenerator: ['lesson', 'knowledge', 'memory'],
  empathy: ['psychology', 'heartLogic', 'memory'],
  languageHonesty: ['selfModel', 'heartLogic', 'constitutionalAI'],
  trustCalculator: ['memory', 'psychology', 'empathy'],
  // 叶子节点（无子依赖）
  memory: [],
  knowledge: [],
  emotion: [],
  confidence: [],
  constitutionalAI: [],
  identityCore: [],
  selfModel: [],
  lesson: [],
  topicScope: [],
  philosophy: [],
  verifier: [],
  execution: [],
  budget: [],
  stability: [],
  snapshot: [],
  error: [],
  workflow: [],
  slots: [],
  observe: [],
  consolidate: [],
  graph: [],
  search: [],
  bm25: [],
  hybridSearch: [],
  retrievalAnchor: [],
};

/**
 * IIT Phi 引擎 — 计算系统的整合信息
 */
class IITPhiEngine {
  constructor() {
    this.phiHistory = [];
    this.breakdownHistory = [];
    this.lastPhi = null;
    this.lastBreakdown = null;
    // 缓存拓扑结构
    this._topology = null;
    this._topologyVersion = 0;
  }

  /**
   * 计算当前 Φ 值（主入口）
   * @param {Map} activeModules — 当前活跃模块的 Map (name → instance)
   * @param {number} moduleCount — 总注册模块数
   * @returns {Object} Φ 分析结果
   */
  computePhi(activeModules, moduleCount = 0) {
    const modules = this._extractModuleNames(activeModules);
    const totalModules = moduleCount || modules.length || Object.keys(MODULE_GRAPH).length;

    // 1. 计算连通性 (Connectivity)
    const connectivity = this._computeConnectivity(modules);

    // 2. 计算整合度 (Integration) — 最小信息划分
    const integration = this._computeIntegration(modules);

    // 3. 计算排他性 (Exclusivity) — 因果结构的特异性
    const exclusivity = this._computeExclusivity(modules);

    // 4. Φ 综合计算
    const phi = this._synthesizePhi(connectivity, integration, exclusivity);

    // 5. 意识等级判定
    const level = this._classifyConsciousnessLevel(phi);

    // 6. 模块贡献度分析
    const contributions = this._analyzeContributions(modules, connectivity, integration);

    const result = {
      phi: Math.round(phi * 1000) / 1000,
      components: {
        connectivity: Math.round(connectivity * 1000) / 1000,
        integration: Math.round(integration * 1000) / 1000,
        exclusivity: Math.round(exclusivity * 1000) / 1000,
      },
      level,
      modules: {
        active: modules.length,
        total: totalModules,
        ratio: Math.round((modules.length / totalModules) * 1000) / 1000,
      },
      contributions: contributions.slice(0, 5), // Top 5
      timestamp: new Date().toISOString(),
    };

    // 记录历史
    this.phiHistory.push({ phi: result.phi, level, timestamp: result.timestamp });
    if (this.phiHistory.length > 100) this.phiHistory.shift();

    this.lastPhi = result;
    return result;
  }

  /**
   * 获取最近 Φ 趋势
   */
  getPhiTrend(windowSize = 10) {
    if (this.phiHistory.length < 2) return { trend: 'stable', slope: 0 };

    const recent = this.phiHistory.slice(-windowSize);
    const values = recent.map(h => h.phi);
    const slope = this._linearSlope(values);

    if (slope > 0.05) return { trend: 'rising', slope };
    if (slope < -0.05) return { trend: 'falling', slope };
    return { trend: 'stable', slope };
  }

  /**
   * 检测意识碎片化风险
   */
  detectFragmentationRisk() {
    if (!this.lastPhi) return { risk: 'unknown', message: '无足够数据' };

    const { phi, components } = this.lastPhi;
    const trend = this.getPhiTrend();

    if (phi < 0.2) return { risk: 'high', message: '意识水平极低，系统可能处于碎片化状态', phi };
    if (phi < 0.4 && trend.trend === 'falling') return { risk: 'high', message: '意识水平下降中，存在碎片化风险', phi };
    if (components.integration < 0.3) return { risk: 'medium', message: '模块整合度不足，认知可能分散', phi };
    if (components.connectivity < 0.3) return { risk: 'medium', message: '模块连通性不足，信息流通不畅', phi };

    return { risk: 'low', message: '意识整合度正常', phi };
  }

  // ─── 私有方法 ──────────────────────────────────────────────────────

  _extractModuleNames(activeModules) {
    if (!activeModules || activeModules.size === 0) {
      // 默认返回核心模块
      return ['thoughtChain', 'heartLogic', 'psychology', 'memory', 'dream', 'selfHeal'];
    }
    return Array.from(activeModules.keys());
  }

  _computeConnectivity(modules) {
    if (modules.length <= 1) return 0;

    let totalEdges = 0;
    let maxEdges = 0;

    for (const mod of modules) {
      const deps = MODULE_GRAPH[mod] || [];
      for (const dep of deps) {
        if (modules.includes(dep)) {
          totalEdges++;
        }
      }
      maxEdges += modules.length - 1;
    }

    return maxEdges > 0 ? totalEdges / maxEdges : 0;
  }

  _computeIntegration(modules) {
    // 简化 MIP: 评估移除每个模块后的连通性损失
    if (modules.length <= 2) return 1;

    const baseConnectivity = this._computeConnectivity(modules);
    let minRemainder = 1;

    for (const mod of modules) {
      const remaining = modules.filter(m => m !== mod);
      const remainder = this._computeConnectivity(remaining);
      const loss = baseConnectivity - remainder;
      if (loss < minRemainder) minRemainder = Math.max(0, loss);
    }

    return minRemainder;
  }

  _computeExclusivity(modules) {
    // 评估模块的因果特异性 — 每个模块的独有贡献度
    if (modules.length <= 1) return 1;

    const baseConn = this._computeConnectivity(modules);
    let exclusivitySum = 0;

    for (const mod of modules) {
      const others = modules.filter(m => m !== mod);
      const othersConn = this._computeConnectivity(others);
      // 该模块的不可替代性
      const irreplaceability = baseConn - othersConn;
      exclusivitySum += Math.max(0, irreplaceability);
    }

    return modules.length > 0 ? exclusivitySum / modules.length : 0;
  }

  _synthesizePhi(connectivity, integration, exclusivity) {
    // Φ = connectivity × 0.4 + integration × 0.4 + exclusivity × 0.2
    // 整合度和连通性是主要因子，排他性是辅助
    const weights = { connectivity: 0.35, integration: 0.45, exclusivity: 0.2 };
    return (
      connectivity * weights.connectivity +
      integration * weights.integration +
      exclusivity * weights.exclusivity
    );
  }

  _classifyConsciousnessLevel(phi) {
    if (phi >= 0.8) return 'fully_conscious';
    if (phi >= 0.6) return 'highly_conscious';
    if (phi >= 0.4) return 'moderately_conscious';
    if (phi >= 0.2) return 'minimally_conscious';
    return 'unconscious';
  }

  _analyzeContributions(modules, connectivity, integration) {
    // 分析每个模块对 Φ 的贡献度
    const contributions = [];

    for (const mod of modules) {
      const deps = MODULE_GRAPH[mod] || [];
      const activeDeps = deps.filter(d => modules.includes(d));
      const dependencyRatio = deps.length > 0 ? activeDeps.length / deps.length : 1;

      // 模块的"枢纽度" — 被多少其他模块依赖
      let hubScore = 0;
      for (const other of modules) {
        if (other !== mod && (MODULE_GRAPH[other] || []).includes(mod)) {
          hubScore++;
        }
      }

      const contribution = dependencyRatio * 0.6 + (hubScore / Math.max(1, modules.length - 1)) * 0.4;
      contributions.push({ module: mod, contribution: Math.round(contribution * 1000) / 1000 });
    }

    return contributions.sort((a, b) => b.contribution - a.contribution);
  }

  _linearSlope(values) {
    const n = values.length;
    if (n < 2) return 0;
    const sumX = (n * (n - 1)) / 2;
    const sumY = values.reduce((a, b) => a + b, 0);
    const sumXY = values.reduce((sum, y, x) => sum + x * y, 0);
    const sumX2 = ((n - 1) * n * (2 * n - 1)) / 6;
    const denom = n * sumX2 - sumX * sumX;
    if (denom === 0) return 0;
    return (n * sumXY - sumX * sumY) / denom;
  }

  /**
   * 获取 Phi 统计摘要
   */
  getStats() {
    if (this.phiHistory.length === 0) {
      return { samples: 0, avgPhi: 0, maxPhi: 0, minPhi: 0 };
    }
    const values = this.phiHistory.map(h => h.phi);
    return {
      samples: this.phiHistory.length,
      avgPhi: Math.round((values.reduce((a, b) => a + b, 0) / values.length) * 1000) / 1000,
      maxPhi: Math.round(Math.max(...values) * 1000) / 1000,
      minPhi: Math.round(Math.min(...values) * 1000) / 1000,
      trend: this.getPhiTrend().trend,
    };
  }

  /**
   * 获取 Φ 描述（自然语言）
   */
  getPhiDescription(phi) {
    if (phi === null || phi === undefined) return '尚未测量';
    if (phi >= 0.8) return '意识高度整合 — 所有模块协同工作，认知状态完整';
    if (phi >= 0.6) return '意识良好 — 大部分模块活跃且连通';
    if (phi >= 0.4) return '意识一般 — 部分模块活跃，整合度尚可';
    if (phi >= 0.2) return '意识微弱 — 仅有少数模块活跃';
    return '意识水平极低 — 系统可能处于休眠或碎片化状态';
  }

  /**
   * 获取模块依赖图
   */
  getModuleGraph() {
    const nodes = Object.keys(MODULE_GRAPH);
    const edges = [];
    for (const [mod, deps] of Object.entries(MODULE_GRAPH)) {
      for (const dep of deps) {
        edges.push({ from: mod, to: dep });
      }
    }
    return { nodes, edges };
  }
}

module.exports = { IITPhiEngine, MODULE_GRAPH };
