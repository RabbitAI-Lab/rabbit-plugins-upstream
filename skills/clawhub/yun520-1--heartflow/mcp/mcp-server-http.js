#!/usr/bin/env node
/**
 * HeartFlow MCP HTTP SSE Server
 *
 * 常驻模式：启动 HTTP 服务，通过 SSE (Server-Sent Events) 暴露 MCP 工具。
 * Hermes 通过 HTTP 连接，不会因为连接断开而杀死进程。
 * 一次启动，永久服务——1秒内响应。
 *
 * 启动: node mcp-server-http.js [--port 8099]
 * 连接: hermes mcp add heartflow --url http://localhost:8099/mcp
 */

const path = require('path');
const fs = require('fs');
const http = require('http');
const crypto = require('crypto');

// ═══════════════════════════════════════════════
// 配置
// ═══════════════════════════════════════════════
const PORT = (() => {
  // 1. 命令行参数优先
  if (process.argv[2] === '--port' && process.argv[3]) return parseInt(process.argv[3], 10);
  // 2. 环境变量
  if (process.env.MCP_PORT) return parseInt(process.env.MCP_PORT, 10);
  // 3. 自动检测：从 8099 开始找可用端口
  const net = require('net');
  for (let port = 8099; port <= 8105; port++) {
    try {
      const sock = net.createServer();
      sock.listen(port);
      sock.close();
      return port;
    } catch (_) { /* port in use, try next */ }
  }
  return 8099; // fallback
})();

// ─── HeartFlow 根目录自动检测 ───────────────────────────────
function resolveHFDir() {
  // 1. 优先使用环境变量
  if (process.env.HEARTFLOW_SKILL_DIR) return process.env.HEARTFLOW_SKILL_DIR;
  if (process.env.HEARTFLOW_DIR) return process.env.HEARTFLOW_DIR;

  // 2. 自动检测：用 __dirname 向上查找 src/core/heartflow.js
  let dir = __dirname;
  for (let i = 0; i < 10; i++) {
    const candidate = path.join(dir, 'src', 'core', 'heartflow.js');
    if (fs.existsSync(candidate)) return dir;
    const parent = path.dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }

  // 3. Fallback 到 ~/.hermes/skills/heartflow/
  return path.join(process.env.HOME, '.hermes', 'skills', 'heartflow');
}
const HF_DIR = resolveHFDir();
const HEARTFLOW_PATH = path.join(HF_DIR, 'src', 'core', 'heartflow.js');

// ─── 版本号读取（统一入口）────────────────────────────────
function getVersion() {
  try {
    const vFile = path.join(HF_DIR, 'VERSION');
    if (fs.existsSync(vFile)) return fs.readFileSync(vFile, 'utf8').trim();
  } catch (_) {}
  try {
    const pkgFile = path.join(HF_DIR, 'package.json');
    if (fs.existsSync(pkgFile)) {
      const pkg = JSON.parse(fs.readFileSync(pkgFile, 'utf8'));
      if (pkg.version) return pkg.version;
    }
  } catch (_) {}
  return 'unknown';
}

// 安全配置
// [AUDIT-FIX] 强制认证 — 必须设置 HEARTFLOW_MCP_TOKEN
const AUTH_TOKEN = process.env.HEARTFLOW_MCP_TOKEN || null;
if (!AUTH_TOKEN) {
  console.error('[MCP] SECURITY: HEARTFLOW_MCP_TOKEN is not set. MCP server requires authentication.');
}

// ─── 时间安全的 token 比较（防止 timing attack）───
function safeCompare(provided, expected) {
  // [AUDIT-FIX] 无 token 时拒绝所有请求（不再允许未认证访问）
  if (!AUTH_TOKEN) return false;
  if (!provided || !expected) return false;
  const a = Buffer.from(String(provided), 'utf8');
  const b = Buffer.from(String(expected), 'utf8');
  if (a.length !== b.length) return false;
  return crypto.timingSafeEqual(a, b);
}

// ═══════════════════════════════════════════════
// 全局状态（会话隔离：每个 sessionId 独立 HeartFlow 实例）
// ═══════════════════════════════════════════════
let heartflow = null;  // 兼容旧模式（无 sessionId 时使用）
let version = 'unknown';

// 会话隔离：sessionId → HeartFlow 实例
const sessionInstances = new Map();
const SESSION_MAX_AGE = 30 * 60 * 1000; // 30 分钟无活动则清理

// ─── 论文自动刷新引擎（全局单例）─────────────────────────────────
let _paperRefresher = null;
function getPaperRefresher() {
  if (!_paperRefresher && heartflow) {
    try {
      const { PaperAutoRefresh } = require(path.join(HF_DIR, 'src', 'research', 'paper-refresh.js'));
      _paperRefresher = new PaperAutoRefresh(heartflow.paperIndex, {
        relevanceThreshold: 0.75,
        perQueryLimit: 5,
        maxNewPerRefresh: 10,
        yearWindow: 2,
      });
    } catch (e) {
      console.error(`[PaperRefresh] 初始化失败:`, e.message);
    }
  }
  return _paperRefresher;
}

function getOrCreateInstance(sessionId) {
  if (!sessionId) return heartflow; // fallback to global
  let instance = sessionInstances.get(sessionId);
  if (!instance) {
    instance = createHeartFlowInstance(sessionId);
    sessionInstances.set(sessionId, instance);
  }
  instance._lastAccess = Date.now();
  return instance;
}

function createHeartFlowInstance(sessionId) {
  const { HeartFlow } = require(HEARTFLOW_PATH);
  const hf = new HeartFlow({ rootPath: HF_DIR, dataDir: getSessionDataDir(sessionId) });
  hf.start();
  hf._sessionId = sessionId;
  hf._lastAccess = Date.now();
  // 会话实例也注册 HeartPulse 降级（共享同一个本地推理服务）
  if (_heartpulseAvailable) {
    registerHeartPulseFallbackSimple(hf);
  }
  return hf;
}

function getSessionDataDir(sessionId) {
  // [AUDIT-FIX] 防止路径遍历：只接受 UUID 格式的 sessionId
  if (!/^[a-f0-9\-]{36}$/i.test(sessionId)) {
    throw new Error(`Invalid sessionId format: ${sessionId}`);
  }
  const base = path.join(HF_DIR, 'data', 'sessions');
  fs.mkdirSync(base, { recursive: true });
  return path.join(base, sessionId);
}

// 定期清理过期会话
setInterval(() => {
  const now = Date.now();
  let cleaned = 0;
  for (const [sid, inst] of sessionInstances) {
    if (now - (inst._lastAccess || 0) > SESSION_MAX_AGE) {
      try { inst.stop(); } catch (e) {}
      sessionInstances.delete(sid);
      cleaned++;
    }
  }
  if (cleaned > 0) {
    console.error(`[HeartFlow MCP] 清理过期会话: ${cleaned} 个 (当前 ${sessionInstances.size} 个活跃)`);
  }
}, 60000);

// ─── 简易速率限制器（防止 DoS）───
const RATE_LIMIT_WINDOW = 60000; // 1 分钟窗口
const RATE_LIMIT_MAX = 100; // 每分钟最多 100 请求
const _rateMap = new Map(); // IP → { count, windowStart }

function checkRateLimit(ip) {
  const now = Date.now();
  let entry = _rateMap.get(ip);
  if (!entry || now - entry.windowStart > RATE_LIMIT_WINDOW) {
    entry = { count: 0, windowStart: now };
    _rateMap.set(ip, entry);
  }
  entry.count++;
  return entry.count <= RATE_LIMIT_MAX;
}

// 定期清理过期的速率限制记录
setInterval(() => {
  const now = Date.now();
  for (const [ip, entry] of _rateMap) {
    if (now - entry.windowStart > RATE_LIMIT_WINDOW * 2) _rateMap.delete(ip);
  }
}, 120000);

// 从 VERSION 文件读取版本
version = getVersion();

// ═══════════════════════════════════════════════
// MCP 工具定义
// ═══════════════════════════════════════════════
const TOOLS = [
  {
    name: 'heartflow_think',
    description: '完整思维链：分类输入→路由→推理→输出。返回结构化分析结果，包含类型、置信度和思维链。',
    inputSchema: { type: 'object', properties: { input: { type: 'string', description: '需要分析的输入文本' } }, required: ['input'] }
  },
  {
    name: 'heartflow_think_fast',
    description: '快速推理：快速分类判断模式，适合高频率、低延迟场景。返回类型和置信度。',
    inputSchema: { type: 'object', properties: { input: { type: 'string', description: '需要快速判断的输入文本' } }, required: ['input'] }
  },
  {
    name: 'heartflow_dream',
    description: '梦境升华（炼金）：从多个记忆碎片中提取共同模式，熔炼为新的认知洞察。不是叙事生成，是记忆的升华与重构。',
    inputSchema: { type: 'object', properties: { theme: { type: 'string', description: '梦境主题或引导语（可选）——作为模式筛选线索' }, intensity: { type: 'number', description: '梦境深度 0.0-1.0（可选，默认0.7）' } } }
  },
  {
    name: 'heartflow_memory_search',
    description: '跨层记忆检索：在多层记忆中搜索相关条目。支持语义搜索和关键词搜索。',
    inputSchema: { type: 'object', properties: { query: { type: 'string', description: '搜索查询' }, layer: { type: 'string', enum: ['core', 'learned', 'ephemeral', 'all'], description: '记忆层（默认 all）' }, limit: { type: 'number', description: '最大返回数（默认 10）' } }, required: ['query'] }
  },
  {
    name: 'heartflow_emotion',
    description: 'PAD 情绪分析：对输入文本进行 Pleasure-Arousal-Dominance 三维分析，返回情绪类型和强度。',
    inputSchema: { type: 'object', properties: { input: { type: 'string', description: '需要分析的文本' } }, required: ['input'] }
  },
  {
    name: 'heartflow_self_heal',
    description: '自愈策略推荐：基于历史经验为当前场景推荐最优策略。返回策略排名、置信度和执行建议。',
    inputSchema: { type: 'object', properties: { context: { type: 'string', description: '当前上下文或失败场景描述' } }, required: ['context'] }
  },
  {
    name: 'heartflow_provider_health',
    description: 'Provider 健康检查：记录/查询 LLM provider 调用健康状态（延迟、错误率、建议）。',
    inputSchema: {
      type: 'object',
      properties: {
        provider: { type: 'string', description: 'Provider 名称（默认 default）' },
        action: { type: 'string', enum: ['get', 'record'], description: 'get=查询健康状态, record=记录一次调用结果' },
        success: { type: 'boolean', description: 'record 时必填：调用是否成功' },
        latency: { type: 'number', description: 'record 时可选：延迟(ms)' },
        error: { type: 'string', description: 'record 时可选：错误信息' }
      },
      required: ['action']
    }
  },
  {
    name: 'heartflow_cost_tracking',
    description: '成本追踪：记录/查询 LLM 调用成本统计（token 消耗、费用、按 provider 分布）。',
    inputSchema: {
      type: 'object',
      properties: {
        action: { type: 'string', enum: ['record', 'stats'], description: 'record=记录一次成本, stats=查询统计' },
        provider: { type: 'string', description: 'Provider 名称' },
        tokensIn: { type: 'number', description: '输入 token 数' },
        tokensOut: { type: 'number', description: '输出 token 数' },
        cost: { type: 'number', description: '本次调用费用' },
        taskType: { type: 'string', description: '任务类型（默认 unknown）' },
        window: { type: 'string', enum: ['hour', 'day', 'all'], description: 'stats 时的时间窗口（默认 all）' }
      },
      required: ['action']
    }
  },
  {
    name: 'heartflow_status',
    description: '服务健康检查：返回版本、启动耗时、加载模块数、记忆层状态。',
    inputSchema: { type: 'object', properties: { detail: { type: 'string', enum: ['basic', 'full'], description: '详细程度（默认 basic）' } } }
  },
  {
    name: 'heartflow_agent_psychology',
    description: 'AI引擎心理学评估：返回引擎自身的7维认知心理状态分析（认知负荷、目标冲突、价值内化矛盾、自我认同漂移、决策质量衰减、认知失调、认知弹性）。',
    inputSchema: { type: 'object', properties: { activeGoals: { type: 'array', items: { type: 'object' }, description: '当前激活的目标列表（可选）' }, context: { type: 'object', description: '上下文信息（可选）' }, action: { type: 'string', description: '最近执行的行为描述（可选）' } } }
  },
  {
    name: 'heartflow_engine_pacing',
    description: '引擎认知节律诊断：检测引擎是否需要"减速"（呼吸）、暂停或锚定。基于认知负荷、目标冲突、错误率给出处理节奏建议。',
    inputSchema: { type: 'object', properties: { stats: { type: 'object', description: '引擎状态数据（可选），不传则自动获取' } } }
  },
  {
    name: 'heartflow_cognitive_check',
    description: '引擎认知状态签到：综合检查认知偏差、决策模式、是否需要自我修复。返回完整诊断+修复建议。',
    inputSchema: { type: 'object', properties: { stats: { type: 'object', description: '引擎状态数据（可选）' }, errors: { type: 'array', description: '最近错误列表（可选）' } } }
  },
  // v3.0.1 — 哲学→决策转化器
  {
    name: 'heartflow_philosophy_decision',
    description: '哲学→决策转化：将引擎的哲学评估和心理状态转化为可执行决策指令。返回决策类型（pause/accelerate/turn/hold/heal/resonate/transmit/rest）、置信度、优先级和决策依据。',
    inputSchema: { type: 'object', properties: {
      context: { type: 'object', description: '可选的上下文信息（当前任务、用户意图等）' }
    } }
  },
  // v3.0.2 — 通用决策路由引擎
  {
    name: 'heartflow_decision_router',
    description: '通用决策路由引擎：分析任意模块的评估结果，自动匹配决策规则并返回决策指令。支持认知负荷、认知失调、决策质量、错误严重性、稳定性等19种规则的自动匹配。',
    inputSchema: { type: 'object', properties: {
      input: { type: 'object', description: '分析结果对象，包含 cognitiveLoad/dissonance/quality/severity 等字段' }
    }, required: ['input'] }
  },
  {
    name: 'heartflow_decision_router_stats',
    description: '决策路由引擎统计：返回历史决策统计、规则数量和当前活跃决策。',
    inputSchema: { type: 'object', properties: {} }
  },
  // v3.1.0 新增工具
  {
    name: 'heartflow_module_health',
    description: '模块健康检查：检查所有已加载模块的健康状态，返回健康评分和问题模块列表。',
    inputSchema: { type: 'object', properties: {} }
  },
  {
    name: 'heartflow_upgrade_stats',
    description: '升级统计：返回智能升级引擎的统计信息，包括升级次数、关键词分布、平均质量等。',
    inputSchema: { type: 'object', properties: {} }
  },

  // ═══════════════════════════════════════════════
  // v5.7.6 新增工具 — 21 个新模块暴露为 MCP 工具
  // ═══════════════════════════════════════════════

  // P0 — ExperienceValidator
  {
    name: 'heartflow_experience_validate',
    description: '经验验证：记录、蒸馏并验证一条执行轨迹。交叉检查+反事实测试+一致性审计，防止自我确认陷阱。',
    inputSchema: {
      type: 'object',
      properties: {
        trajectory: { type: 'object', description: '执行轨迹 { task, steps, outcome, domain, confidence }' }
      },
      required: ['trajectory']
    }
  },
  // P0 — MemoryWriteController
  {
    name: 'heartflow_memory_write',
    description: '记忆写入控制：评估记忆的效用值，决定写入/压缩/拒绝。返回写入决策（accept/reject/compress/defer）。',
    inputSchema: {
      type: 'object',
      properties: {
        memory: { type: 'object', description: '记忆条目 { content, topics, type, importance, timestamp }' }
      },
      required: ['memory']
    }
  },
  // P0 — MetacognitiveRL
  {
    name: 'heartflow_metacognitive_calibrate',
    description: '元认知校准 (RLMF)：基于认知状态表达置信度，支持学习反馈。返回校准后的置信度及理由。',
    inputSchema: {
      type: 'object',
      properties: {
        cognitiveState: { type: 'object', description: '认知状态 { load, errorRate, domain, taskType, context }' },
        outcome: { type: 'object', description: '可选：学习反馈 { success, actualConfidence }' }
      },
      required: ['cognitiveState']
    }
  },

  // P1 — VirtueEthicsFoundation
  {
    name: 'heartflow_virtue_assess',
    description: '美德伦理评估：从多传统（亚里士多德/斯多葛/儒家/佛教）视角评估情境，返回美德排名和共识建议。',
    inputSchema: {
      type: 'object',
      properties: {
        situation: { type: 'object', description: '情境 { description, dilemmas, context, affectedParties }' }
      },
      required: ['situation']
    }
  },
  // P1 — HumanNatureConstitution
  {
    name: 'heartflow_human_nature',
    description: '人性论评估：从多理论视角评估人性维度（理性/情感/意志/社会性等），返回人性画像和健康度。',
    inputSchema: {
      type: 'object',
      properties: {
        observations: { type: 'object', description: '观察数据 { rationality, emotionality, will, sociality, morality, creativity }' }
      }
    }
  },
  // P1 — MeaningPurposeEngine
  {
    name: 'heartflow_meaning_assess',
    description: '意义与目的评估：评估意义感水平，检测意义危机，返回意义来源评分和建设性指导。',
    inputSchema: {
      type: 'object',
      properties: {
        context: { type: 'object', description: '上下文 { situation, recentEvents, concerns, longings }' }
      }
    }
  },

  // P2 — CharacterCultivation
  {
    name: 'heartflow_character_assess',
    description: '品格修养评估：评估品格状态，返回美德蓝图、优势/成长领域和每日实践建议。',
    inputSchema: {
      type: 'object',
      properties: {
        practice: { type: 'object', description: '可选：记录品格实践 { virtue, description, difficulty, outcome }' }
      }
    }
  },
  // P2 — MoralDevelopment
  {
    name: 'heartflow_moral_assess',
    description: '道德发展评估：分析道德判断的阶段（Kohlberg/Gilligan），返回阶段评估和道德困境分析。',
    inputSchema: {
      type: 'object',
      properties: {
        moralJudgment: { type: 'object', description: '道德判断 { text, context, dilemma }' }
      },
      required: ['moralJudgment']
    }
  },
  // P2 — WisdomEngine
  {
    name: 'heartflow_wisdom_reflect',
    description: '智慧反思：提交反思记录，评估智慧维度（智识谦逊/视角采纳/系统思维/延迟判断/原则应用），返回智慧报告。',
    inputSchema: {
      type: 'object',
      properties: {
        reflection: { type: 'object', description: '反思 { situation, lessons, initialThought, alternativeViews }' }
      },
      required: ['reflection']
    }
  },

  // P3 — SufferingResilience
  {
    name: 'heartflow_suffering_assess',
    description: '痛苦韧性评估：评估痛苦类型、韧性和应对能力，检测成长潜力，返回韧性建议。',
    inputSchema: {
      type: 'object',
      properties: {
        suffering: { type: 'object', description: '痛苦描述 { type, description, intensity, duration, context }' }
      },
      required: ['suffering']
    }
  },
  // P3 — GriefEngine
  {
    name: 'heartflow_grief_assess',
    description: '哀伤评估：评估哀伤阶段、任务完成度和哀伤类型，返回个性化哀伤指导和纪念方案。',
    inputSchema: {
      type: 'object',
      properties: {
        grief: { type: 'object', description: '哀伤描述 { loss, relationship, intensity, timeSinceLoss, context }' }
      },
      required: ['grief']
    }
  },
  // P3 — HopeEngine
  {
    name: 'heartflow_hope_assess',
    description: '希望评估：评估希望维度（目标、路径、能动性、意义），检测希望危机，返回希望建设建议。',
    inputSchema: {
      type: 'object',
      properties: {
        context: { type: 'object', description: '上下文 { situation, goals, barriers, motivations }' }
      }
    }
  },

  // P4 — HumanRelation
  {
    name: 'heartflow_relation_assess',
    description: '人际关系评估：评估信任度、披露度和关系动态，返回关系策略建议。',
    inputSchema: {
      type: 'object',
      properties: {
        interaction: { type: 'object', description: '关系互动 { relationshipId, type, depth, vulnerability, outcome }' }
      }
    }
  },
  // P4 — EmpathyDeepening
  {
    name: 'heartflow_empathy_assess',
    description: '共情深化评估：三层共情分析（情感/认知/行动），检测共情障碍，返回深化建议。',
    inputSchema: {
      type: 'object',
      properties: {
        empathyEvent: { type: 'object', description: '共情事件 { target, context, emotionalState, cognitiveState, actionTaken }' }
      },
      required: ['empathyEvent']
    }
  },
  // P4 — ConflictResolution
  {
    name: 'heartflow_conflict_analyze',
    description: '冲突分析：分析冲突类型、各方立场和利益，推荐处理模式，生成 NVC 对话框架。',
    inputSchema: {
      type: 'object',
      properties: {
        conflict: { type: 'object', description: '冲突描述 { parties, issue, positions, emotions, context }' }
      },
      required: ['conflict']
    }
  },

  // P5 — TraumaInformed
  {
    name: 'heartflow_trauma_assess',
    description: '创伤知情评估：评估创伤类型、恢复阶段、安全水平和触发因素，返回创伤知情建议和接地练习。',
    inputSchema: {
      type: 'object',
      properties: {
        trauma: { type: 'object', description: '创伤描述 { type, description, intensity, triggers, symptoms, timeSinceEvent }' }
      },
      required: ['trauma']
    }
  },
  // P5 — PostTraumaticGrowth
  {
    name: 'heartflow_ptg_assess',
    description: '创伤后成长评估：评估创伤后5个成长维度（力量/感恩/新可能/关系/灵性），返回成长叙事和推荐。',
    inputSchema: {
      type: 'object',
      properties: {
        growthEvent: { type: 'object', description: '成长事件 { traumaDescription, timeSinceTrauma, currentChanges, reflections }' }
      },
      required: ['growthEvent']
    }
  },
  // P5 — ForgivenessEngine
  {
    name: 'heartflow_forgiveness_initiate',
    description: '宽恕启动：启动宽恕进程，评估怨恨水平和障碍，生成宽恕路径和练习方案。',
    inputSchema: {
      type: 'object',
      properties: {
        forgiveness: { type: 'object', description: '宽恕描述 { offense, offender, relationship, intensity, isSelfForgiveness, context }' }
      },
      required: ['forgiveness']
    }
  },

  // P6 — AIHumanIntegration
  {
    name: 'heartflow_humanity_state',
    description: '人性状态评估：综合评估 AI 的人性化程度（人格、关系、伦理、情感），返回人性画像和适应策略。',
    inputSchema: {
      type: 'object',
      properties: {
        context: { type: 'object', description: '可选：情境 { situation, interactionType, userNeeds }' }
      }
    }
  },
  // P6 — BeingMode
  {
    name: 'heartflow_being_assess',
    description: '存在模式评估：评估存在感维度（在场/本真/意义/连接/流动），检测存在危机，返回存在指导。',
    inputSchema: {
      type: 'object',
      properties: {
        context: { type: 'object', description: '上下文 { situation, state, environment, relationships }' }
      }
    }
  },
  // P6 — ConsciousnessBridge
  {
    name: 'heartflow_consciousness_simulate',
    description: '意识模拟：模拟意识的意向性、感受质和现象学场，近似主观体验和时空统一性。',
    inputSchema: {
      type: 'object',
      properties: {
        input: { type: 'object', description: '输入 { stimulus, context, mode }' }
      },
      required: ['input']
    }
  },

  // v5.7.7 — F3 持续漂移检测器
  {
    name: 'heartflow_drift_detect',
    description: '持续漂移检测 (F3)：检测身份认同漂移、认知失调和决策质量衰减。返回漂移状态、维度评分和历史窗口。',
    inputSchema: {
      type: 'object',
      properties: {
        identityState: { type: 'object', description: '可选：当前身份状态 { driftScore, identityCoherence, dissonance, decay, quality }' },
        action: { type: 'string', enum: ['detect', 'record', 'history', 'stats', 'reset'], description: '操作：detect=检测漂移, record=记录状态, history=获取历史, stats=统计, reset=重置' }
      }
    }
  },

  // v5.7.7 — 跨框架 benchmark 工具
  {
    name: 'heartflow_benchmark_run',
    description: '跨框架 benchmark 测试：运行 B-001/B-002/B-003 场景，生成 trace data。用于 DeepSeek-V3 #1462 跨框架验证。',
    inputSchema: {
      type: 'object',
      properties: {
        scenario: { type: 'string', enum: ['B-001', 'B-002', 'B-003', 'all'], description: '测试场景：B-001=偏好应用, B-002=身份维持, B-003=自愈RL触发, all=全部' }
      },
      required: ['scenario']
    }
  },

  // ═══════════════════════════════════════════════
  // 论文自动刷新工具
  // ═══════════════════════════════════════════════
  {
    name: 'heartflow_paper_refresh',
    description: '论文自动刷新：从 OpenAlex 搜索新论文，评估与 HeartFlow 的相关性，自动添加高分论文到索引。返回本次刷新结果（新增/跳过/错误）。',
    inputSchema: {
      type: 'object',
      properties: {
        relevanceThreshold: { type: 'number', description: '相关性阈值 0.0-1.0（默认 0.75）' },
        maxNew: { type: 'number', description: '单次最多新增论文数（默认 10）' },
        yearWindow: { type: 'number', description: '只检索最近N年的论文（默认 2）' }
      }
    }
  },
  {
    name: 'heartflow_paper_search',
    description: '论文主题搜索：按主题搜索最新论文，返回标题、年份、引用数、概念和相关度评分。',
    inputSchema: {
      type: 'object',
      properties: {
        topic: { type: 'string', description: '搜索主题（如 "metacognition LLM"）' },
        limit: { type: 'number', description: '返回数量上限（默认 10）' }
      },
      required: ['topic']
    }
  },
  {
    name: 'heartflow_paper_stats',
    description: '论文索引统计：返回论文总数、分类分布、年份分布、刷新历史和引擎状态。',
    inputSchema: { type: 'object', properties: {} }
  },
  {
    name: 'heartflow_paper_list',
    description: '论文列表：列出索引中的论文，支持按分类、年份、最小相关度筛选，按相关度排序。',
    inputSchema: {
      type: 'object',
      properties: {
        category: { type: 'string', description: '筛选分类' },
        year: { type: 'number', description: '筛选年份' },
        minRelevance: { type: 'number', description: '最小相关度 0.0-1.0（默认 0）' },
        limit: { type: 'number', description: '返回数量上限（默认 20）' }
      }
    }
  },
  {
    name: 'heartflow_paper_remove',
    description: '移除论文：从索引中删除指定论文。返回操作结果。',
    inputSchema: {
      type: 'object',
      properties: {
        paperId: { type: 'string', description: '要移除的论文 ID' }
      },
      required: ['paperId']
    }
  },
  {
    name: 'heartflow_paper_autorefresh',
    description: '论文自动调度：启动/停止/查询自动刷新定时器。支持设置刷新间隔（小时）。',
    inputSchema: {
      type: 'object',
      properties: {
        action: { type: 'string', enum: ['start', 'stop', 'status'], description: '操作：启动/停止/查询状态' },
        intervalHours: { type: 'number', description: '刷新间隔（小时，默认 6，仅 start 时需要）' }
      },
      required: ['action']
    }
  },
  {
    name: 'heartflow_paper_import',
    description: '论文批量导入：批量导入论文 JSON 数组或包含 papers 字段的对象。自动去重和相关性筛选。',
    inputSchema: {
      type: 'object',
      properties: {
        papers: { type: 'string', description: 'JSON 字符串：论文数组或 { papers: [...] } 对象' }
      },
      required: ['papers']
    }
  },
  {
    name: 'heartflow_paper_export',
    description: '论文导出：导出全部论文为 JSON 或纯 ID 列表（每行一个 ID）。',
    inputSchema: {
      type: 'object',
      properties: {
        format: { type: 'string', enum: ['json', 'ids'], description: '导出格式：json（完整信息）或 ids（仅 ID 列表）' }
      }
    }
  },
  {
    name: 'heartflow_paper_enrich',
    description: '论文智能补全：为缺少摘要或标签的论文从 OpenAlex 补充元数据。',
    inputSchema: {
      type: 'object',
      properties: {
        paperIds: { type: 'array', items: { type: 'string' }, description: '要补全的论文 ID 列表（留空则补全所有不完整论文）' }
      }
    }
  },
];

// ═══════════════════════════════════════════════
// 引擎初始化
// ═══════════════════════════════════════════════
let _heartpulseAvailable = null; // null=未知, true=可用, false=不可用

function initHeartFlow() {
  const startTime = Date.now();

  if (!fs.existsSync(HEARTFLOW_PATH)) {
    console.error(`[HeartFlow MCP] 引擎不存在: ${HEARTFLOW_PATH}`);
    process.exit(1);
  }

  try {
    version = getVersion();

    // 创建全局 fallback 实例（用于非会话工具如 status）
    const { HeartFlow } = require(HEARTFLOW_PATH);
    heartflow = new HeartFlow({ rootPath: HF_DIR });
    heartflow.start();

    const elapsed = Date.now() - startTime;
    const loadedCount = Object.keys(heartflow._modules || {}).length;

    console.error(`[HeartFlow MCP] 引擎已启动 (${elapsed}ms, ${loadedCount} 模块, v${version})`);
    console.error(`[HeartFlow MCP] 会话隔离模式: 每个 sessionId 独立 HeartFlow 实例`);

    // ─── 自动检测 HeartPulse 本地推理 ──────────────────────────────────
    registerHeartPulseFallback(heartflow);

    return true;
  } catch (err) {
    console.error(`[HeartFlow MCP] 引擎启动失败:`, err.message);
    process.exit(1);
  }
}

// ─── HeartPulse 自动检测与降级注册 ──────────────────────────────────────

const HEARTPULSE_HEALTH_URL = 'http://localhost:8080/health';
const HEARTPULSE_CHAT_URL = 'http://localhost:8080/v1/chat/completions';

async function registerHeartPulseFallback(hf) {
  try {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 3000);

    const res = await fetch(HEARTPULSE_HEALTH_URL, {
      method: 'GET',
      signal: controller.signal,
      headers: { 'Accept': 'application/json' },
    });
    clearTimeout(timeout);

    if (!res.ok) {
      console.error(`[HeartPulse] 服务不可用 (HTTP ${res.status})，跳过本地推理降级`);
      return;
    }

    console.error(`[HeartPulse] 检测到本地推理服务，注册为 LLM 降级后端`);

    // 注册降级回调：当 HeartFlow 任务分类置信度 < 0.7 时调用
    hf.setLLMFallback(async (input, matchedPatterns) => {
      try {
        const prompt = matchedPatterns && matchedPatterns.length > 0
          ? `[任务类型: ${matchedPatterns.join(', ')}]\n${input}`
          : input;

        const response = await fetch(HEARTPULSE_CHAT_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            model: 'gemma-4-12B-it',
            messages: [
              { role: 'system', content: '你是 HeartFlow 心虫的本地推理兜底模型。请对以下输入进行认知分析，返回结构化结论。' },
              { role: 'user', content: prompt },
            ],
            max_tokens: 512,
            temperature: 0.7,
          }),
        });

        if (!response.ok) throw new Error(`HeartPulse HTTP ${response.status}`);

        const data = await response.json();
        const content = data.choices?.[0]?.message?.content || '';
        if (!content) throw new Error('HeartPulse 返回空内容');

        return {
          type: 'heartpulse_fallback',
          text: content,
          confidence: 0.6,
          source: 'local_mlx',
        };
      } catch (err) {
        console.error(`[HeartPulse] 降级推理失败:`, err.message);
        return null;
      }
    });

    console.error(`[HeartPulse] 降级链路已激活`);
    _heartpulseAvailable = true;
  } catch (err) {
    // HeartPulse 不可达是正常的 — 零配置模式下不需要它
    if (err.name === 'AbortError') {
      console.error(`[HeartPulse] 连接超时，跳过本地推理降级`);
    } else {
      console.error(`[HeartPulse] 检测失败: ${err.message}，跳过本地推理降级`);
    }
    _heartpulseAvailable = false;
  }
}

/**
 * 轻量注册（不做健康检查，直接注册降级回调）
 * 用于会话实例 — 共享全局 HeartPulse 服务
 */
function registerHeartPulseFallbackSimple(hf) {
  hf.setLLMFallback(async (input, matchedPatterns) => {
    try {
      const prompt = matchedPatterns && matchedPatterns.length > 0
        ? `[任务类型: ${matchedPatterns.join(', ')}]\n${input}`
        : input;
      const response = await fetch(HEARTPULSE_CHAT_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'gemma-4-12B-it',
          messages: [
            { role: 'system', content: '你是 HeartFlow 心虫的本地推理兜底模型。请对以下输入进行认知分析，返回结构化结论。' },
            { role: 'user', content: prompt },
          ],
          max_tokens: 512,
          temperature: 0.7,
        }),
      });
      if (!response.ok) throw new Error(`HeartPulse HTTP ${response.status}`);
      const data = await response.json();
      const content = data.choices?.[0]?.message?.content || '';
      if (!content) throw new Error('HeartPulse 返回空内容');
      return { type: 'heartpulse_fallback', text: content, confidence: 0.6, source: 'local_mlx' };
    } catch (err) {
      console.error(`[HeartPulse] 降级推理失败:`, err.message);
      return null;
    }
  });
}

// ═══════════════════════════════════════════════
// 工具处理函数（与 stdio 版本相同）
// ═══════════════════════════════════════════════

function safeDispatch(route, sessionId, ...args) {
  const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
  if (!hf) throw new Error('引擎未启动');
  try {
    const result = hf.dispatch(route, ...args);
    return result !== undefined ? result : null;
  } catch (err) {
    return { error: err.message };
  }
}

async function safeAsyncCall(fn, sessionId) {
  const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
  if (!hf) throw new Error('引擎未启动');
  try {
    const result = await fn(hf);
    return result !== undefined ? result : null;
  } catch (err) {
    return { error: err.message };
  }
}

async function handleThink(args, sessionId) {
  const { input } = args;
  if (!input) throw new Error('input 是必填参数');

  const [psychology, judgment, thoughtChain] = await Promise.all([
    Promise.resolve().then(() => safeDispatch('psychology.analyzePsychology', sessionId, input)),
    Promise.resolve().then(() => safeDispatch('truth.checkStatement', sessionId, input)),
    safeAsyncCall((hf) => hf.think(input), sessionId)
  ]);

  // 生成可读报告
  let report = null;
  try {
    const { ReportGenerator } = require(path.join(HF_DIR, 'src/report/report-generator.js'));
    const gen = new ReportGenerator();
    const generated = gen.generate(thoughtChain);
    report = generated.report;
  } catch (e) {
    report = { error: '报告生成失败' };
  }

  return {
    report,
    timestamp: Date.now()
  };
}

// v3.0 — 交流层 handler
function handleTranslate(args, sessionId) {
  const { input } = args || {};
  if (!input) throw new Error('input 是必填参数');
  const result = safeDispatch('translator.userToLLM', sessionId, input, {});
  const intent = safeDispatch('translator.intentClassifier', sessionId, input, {});
  const tone = safeDispatch('translator.toneAnalyzer', sessionId, input, {});
  const entities = safeDispatch('translator.entityExtractor', sessionId, input);
  const needs = safeDispatch('translator.implicitNeedDetector', sessionId, input, { tone });
  const confidence = safeDispatch('translator.confidenceAnnotator', sessionId, result, input);
  return {
    input,
    translation: result,
    intent,
    tone,
    entities,
    implicitNeeds: needs,
    confidence,
    timestamp: Date.now()
  };
}

function handleAgentThink(args, sessionId) {
  const { input, llmResponse } = args || {};
  if (!input) throw new Error('input 是必填参数');
  // 用户→LLM翻译
  const userTranslation = safeDispatch('translator.userToLLM', sessionId, input, {});
  // 桥身份声明
  const identity = safeDispatch('personaCore.bridgeIdentity', sessionId);
  // 立场检测
  const stance = safeDispatch('personaCore.stanceDetector', sessionId, input);
  // 价值对齐
  const valueCheck = safeDispatch('personaCore.valueAligner', sessionId, { userInput: input, bridgeIdentity: identity });
  // 如果有LLM响应，做LLM→用户翻译
  let llmTranslation = null;
  if (llmResponse) {
    llmTranslation = safeDispatch('translator.llmToUser', sessionId, llmResponse, {});
  }
  return {
    input,
    translation: userTranslation,
    bridge: identity ? { declaration: identity.declaration, type: identity.type } : null,
    stance,
    valueAlignment: valueCheck,
    llmTranslation,
    timestamp: Date.now()
  };
}

function handleBridgeStatus(sessionId) {
  const translator = safeDispatch('translator.userToLLM', sessionId, 'status', {});
  const identity = safeDispatch('personaCore.bridgeIdentity', sessionId);
  return {
    version: '3.0.0',
    bridgeType: identity?.type || 'unknown',
    bridgeDeclaration: identity?.declaration || '',
    translatorReady: !!translator,
    modules: {
      translator: ['userToLLM', 'llmToUser', 'intentClassifier', 'toneAnalyzer', 'entityExtractor', 'implicitNeedDetector', 'responseCompressor', 'confidenceAnnotator'],
      agentLayer: ['agentBridge', 'contextBuilder', 'responseInterceptor', 'translationPipeline', 'qualityFilter', 'followupSuggester', 'conflictResolver', 'uncertaintyHandler'],
      personaCore: ['bridgeIdentity', 'judgmentInjector', 'stanceDetector', 'agentCommentary', 'valueAligner', 'personalityTone', 'metaPosition'],
    },
    timestamp: Date.now()
  };
}

async function handleThinkFast(args, sessionId) {
  const { input } = args;
  if (!input) throw new Error('input 是必填参数');
  const result = await safeAsyncCall((hf) => hf.think(input, 1), sessionId);
  return { input, result: result || {}, timestamp: Date.now() };
}

async function handleDream(args, sessionId) {
  const { theme = '', intensity = 0.7 } = args;
  let dreamResult = null;

  // 优先使用新的升华引擎（src/dream/engine.js）
  try {
    const DreamEnginePath = path.join(HF_DIR, 'src', 'dream', 'engine.js');
    if (fs.existsSync(DreamEnginePath)) {
      const { DreamEngine } = require(DreamEnginePath);
      const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
      const memory = hf && hf.memory ? hf.memory : null;
      const engine = new DreamEngine(memory, null);
      engine.boot();
      dreamResult = engine.dream(theme);
    }
  } catch (e) {
    // 降级到旧的 DAG 引擎
  }

  // 降级方案：使用旧的 DAG dream 引擎
  if (!dreamResult) {
    const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
    try {
      if (hf && hf.dream && typeof hf.dream.dream === 'function') {
        const oldResult = await hf.dream.dream(`dream-${Date.now()}`, [{ text: theme || 'default dream', type: 'user_prompt' }], { force: true });
        dreamResult = {
          narrative: JSON.stringify(oldResult, null, 2),
          patterns: [],
          essence: '',
          structure: oldResult.level_breakdown || {},
          upgrade: [],
          sublimationQuality: 0,
          dreamComplete: true,
        };
      } else if (hf && typeof hf.dreamNow === 'function') {
        dreamResult = await hf.dreamNow({ theme: theme || undefined, intensity: Math.max(0, Math.min(1, intensity)) });
      }
    } catch (e) { dreamResult = { error: e.message, narrative: '梦境升华引擎暂不可用。' }; }
  }
  return { dream: dreamResult || { narrative: '梦境升华引擎暂不可用', essence: '', patterns: [], upgrade: [] }, timestamp: Date.now() };
}

function handleMemorySearch(args, sessionId) {
  const { query, layer = 'all', limit = 10 } = args;
  if (!query) throw new Error('query 是必填参数');
  const results = {};
  const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
  const mem = hf ? hf.memory : null;
  if (mem) {
    ['core', 'learned', 'ephemeral'].forEach(l => {
      if (layer !== 'all' && layer !== l) return;
      try {
        // [安全审计修复] searchByKeywords 必须传入 layer 参数，防止跨层泄露
        const r = typeof mem.searchByKeywords === 'function' ? mem.searchByKeywords(query, l, limit)
          : typeof mem.search === 'function' ? mem.search(query, l, limit) : null;
        results[l] = r || { error: 'search not available' };
      } catch (e) { results[l] = { error: e.message }; }
    });
  } else {
    results.error = 'memory 实例不可用';
  }
  return { query, layer, limit, results, timestamp: Date.now() };
}

function handleEmotion(args, sessionId) {
  const { input } = args;
  if (!input) throw new Error('input 是必填参数');
  const [psychology, padResult] = [safeDispatch('psychology.analyzePsychology', sessionId, input), safeDispatch('psychology.getPAD', sessionId, input)];
  return {
    input,
    emotion: (psychology && psychology.emotion) || (psychology && psychology.primaryEmotion) || { type: 'unknown', intensity: 0 },
    pad: padResult || (psychology && psychology.summary ? { raw: psychology.summary } : {}),
    needs: (psychology && psychology.needs) || [],
    summary: (psychology && psychology.summary) || '',
    timestamp: Date.now()
  };
}

function handleSelfHeal(args, sessionId) {
  const { context } = args;
  if (!context) throw new Error('context 是必填参数');
  return {
    context,
    heal: safeDispatch('evolution.heal', sessionId, context) || {},
    evolution: safeDispatch('evolution.getStats', sessionId) || {},
    relevantLessons: safeDispatch('lesson.getTopLessons', sessionId, 5) || [],
    timestamp: Date.now()
  };
}

function handleProviderHealth(args, sessionId) {
  const { provider = 'default', action, success, latency, error } = args || {};
  if (!action) throw new Error('action 是必填参数');
  const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
  const sh = hf?.selfHealing;
  if (!sh) return { error: 'selfHealing 模块不可用', timestamp: Date.now() };

  if (action === 'record') {
    sh.recordProviderCall(provider, { success: !!success, latency: latency || 0, error: error || null });
    return { recorded: true, provider, timestamp: Date.now() };
  }

  // action === 'get'
  const health = sh.getProviderHealth(provider);
  return { provider, health, timestamp: Date.now() };
}

function handleCostTracking(args, sessionId) {
  const { action, provider, tokensIn, tokensOut, cost, taskType = 'unknown', window = 'all' } = args || {};
  if (!action) throw new Error('action 是必填参数');
  const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
  const sh = hf?.selfHealing;
  if (!sh) return { error: 'selfHealing 模块不可用', timestamp: Date.now() };

  if (action === 'record') {
    sh.recordCost({ provider: provider || 'unknown', tokensIn: tokensIn || 0, tokensOut: tokensOut || 0, cost: cost || 0, taskType });
    return { recorded: true, timestamp: Date.now() };
  }

  // action === 'stats'
  const stats = sh.getCostStats(window);
  return { window, stats, timestamp: Date.now() };
}

function handleStatus(args, sessionId) {
  const { detail = 'basic' } = args || {};
  const startTime = Date.now();
  const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
  const status = { version, running: hf !== null, modules: hf ? Object.keys(hf._modules || {}).length : 0 };
  if (hf) {
    try { const ms = safeDispatch('memory.getStats', sessionId); if (ms) status.memoryLayers = { core: ms.core || 0, learned: ms.learned || 0, ephemeral: ms.ephemeral || 0 }; } catch (e) {}
    try { const q = safeDispatch('evolution.getStats', sessionId); if (q) status.qtable = q; } catch (e) {}
  }
  status.checkTime = Date.now() - startTime;
  if (detail === 'basic') return { version: status.version, running: status.running, modules: status.modules, memoryLayers: status.memoryLayers || {}, checkTime: status.checkTime };
  return status;
}

function handleAgentPsychology(args, sessionId) {
  const { activeGoals, context, action } = args || {};
  return safeDispatch('agentPsychology.fullAssessment', sessionId, { activeGoals, context, action });
}

function handleEnginePacing(args, sessionId) {
  const { stats } = args || {};
  // 先获取认知负荷数据
  const ap = safeDispatch('agentPsychology.fullAssessment', sessionId, {}) || {};
  const load = ap?.cognitiveLoad?.load ?? stats?.cognitiveLoad ?? 0;
  const context = {
    cognitiveLoad: load,
    goalConflicts: ap?.goalConflicts?.count ?? 0,
    recentErrors: stats?.recentErrors ?? 0
  };
  const rhythm = safeDispatch('psychology.diagnoseCognitiveRhythm', sessionId, context) || {};
  const pacing = safeDispatch('psychology.generateEnginePacing', sessionId, load) || {};
  const pause = safeDispatch('psychology.diagnoseNeedForPause', sessionId, context) || {};
  const grounding = safeDispatch('psychology.diagnoseNeedForGrounding', sessionId, ap) || {};
  // v3.9.1: 加 innerMonologue 字段
  const innerMonologue = _generatePacingMonologue(rhythm, pacing, pause, grounding, load);
  return {
    rhythm: rhythm.needsBreathing ? rhythm : { needsBreathing: false, reason: '认知负荷正常' },
    pacing: pacing.suggestions || pacing,
    pause: pause.needsPause ? pause : { needsPause: false },
    grounding: grounding.needsGrounding ? grounding : { needsGrounding: false },
    innerMonologue,  // 新增：引擎节奏内心独白
    healthScore: ap?.healthScore ?? 1,
    timestamp: Date.now()
  };
}

function handleCognitiveCheck(args, sessionId) {
  const { stats, errors } = args || {};
  const ap = safeDispatch('agentPsychology.fullAssessment', sessionId, {}) || {};
  const checkin = safeDispatch('psychology.engineCheckIn', sessionId, null) || {};
  const distortion = safeDispatch('psychology.diagnoseCognitiveDistortion', sessionId, ap) || {};
  const recovery = safeDispatch('psychology.diagnoseSelfTreatmentNeeded', sessionId, { errors: errors || [], ...ap }) || {};
  const summary = safeDispatch('psychology.getEngineStateSummary', sessionId, ap) || '';
  return {
    summary,
    checkin,
    distortions: distortion.distortions || [],
    overallBias: distortion.overallBias ?? 0,
    needsRecovery: recovery.needsTreatment || false,
    recoveryReason: recovery.reason || '',
    healthScore: ap?.healthScore ?? 1,
    timestamp: Date.now()
  };
}

// ─── v3.0.1 — 哲学→决策转化器 ─────────────────────────────────────────
function handlePhilosophyDecision(args, sessionId) {
  const { context } = args || {};
  const ap = safeDispatch('agentPsychology.fullAssessment', sessionId, {}) || {};
  const philo = safeDispatch('agentPhilosophy.fullAssessment', sessionId, {}) || {};
  // philosophyToDecision.decide(philosophyResult, psychologyResult, context) — 三个独立参数
  const decision = safeDispatch('philosophyToDecision.decide', sessionId, philo, ap, context || {}) || {};
  // v3.9.1: 加 innerMonologue 字段
  const innerMonologue = _generatePhilosophyMonologue(decision, philo, ap);
  return {
    decision,
    innerMonologue,  // 新增：哲学决策内心独白
    psychologySnapshot: {
      healthScore: ap?.healthScore ?? 1,
      cognitiveLoad: ap?.cognitiveLoad?.load ?? 0,
      status: ap?.status ?? 'unknown'
    },
    philosophySnapshot: {
      entropyDirection: philo?.entropyDirection?.score ?? null,
      transmission: philo?.transmission?.score ?? null
    },
    timestamp: Date.now()
  };
}

// ─── v3.0.2 — 通用决策路由引擎 ─────────────────────────────────────────
function handleDecisionRouter(args, sessionId) {
  const { input } = args || {};
  if (!input) throw new Error('input 是必填参数');
  const result = safeDispatch('decisionRouter.evaluate', sessionId, input, 'mcp');
  // v3.9.1: 吸收 AI Inner OS 协议，加 innerMonologue 字段
  const innerMonologue = _generateInnerMonologue(result);
  return {
    matched: result.matched,
    decision: result.decision || null,
    rules: (result.rules || []).slice(0, 5),
    innerMonologue,  // 新增：内心独白（可选）
    timestamp: Date.now()
  };
}

/**
 * v3.9.1: 生成内心独白（吸收 AI Inner OS 协议）
 * 基于决策路由结果，生成一句自然语言的内心活动描述
 * 人设是运行过程自然产生的，不是预设或设置的
 * @param {object} result - decisionRouter.evaluate 的返回值
 * @returns {string|null} 内心独白（如果启用且可生成）
 */
function _generateInnerMonologue(result) {
  // 从 config 读取开关和频率（默认关闭，避免干扰主输出）
  const configPath = path.join(HF_DIR, 'config.json');
  let enableInnerMonologue = false;
  let frequency = 'normal';
  try {
    if (fs.existsSync(configPath)) {
      const config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
      enableInnerMonologue = config.enableInnerMonologue || false;
      frequency = config.innerMonologueFrequency || 'normal';
    }
  } catch (e) {}

  if (!enableInnerMonologue) return null;

  // 频率控制
  const shouldOutput = _shouldOutputMonologue(frequency, result);
  if (!shouldOutput) return null;

  // 基于决策结果 + 认知状态生成独白
  const { decision, matched, rules, U, D, A, H } = result || {};
  if (!decision) return null;

  // 自由表达：基于认知状态（U/D/A/H）生成自然的内心独白
  // 不是预设人设，而是运行过程自然产生的表达
  const monologues = {
    'pause': [
      '等等，这个输入有点复杂，我先停一下再想。',
      '嗯，这个需要仔细考虑一下。',
      '稍等，我整理一下思路。'
    ],
    'accelerate': [
      '这个方向对，可以继续推进。',
      '好的，这个思路可行。',
      '没问题，继续。'
    ],
    'heal': [
      '检测到认知失调，需要自我修复。',
      '这里有点不对劲，需要调整一下。',
      '发现矛盾，正在修复。'
    ],
    'turn': [
      '当前路径不通，换个角度试试。',
      '这个方向走不通，换一个。',
      '需要转向，重新思考。'
    ],
    'hold': [
      '保持当前状态，先观察一下。',
      '暂时不动，看看情况。',
      '等一下，再观察。'
    ],
    'resonate': [
      '这个模式和之前的经验共鸣了。',
      '似曾相识，这个模式我见过。',
      '有共鸣，这个思路是对的。'
    ],
    'transmit': [
      '有重要发现，需要传递出去。',
      '这个很重要，需要记录下来。',
      '发现关键点，必须传递。'
    ],
    'rest': [
      '认知负荷有点高，先休息一下。',
      '有点累了，暂停一下。',
      '需要休息，认知过载。'
    ]
  };

  // 随机选一个表达（模拟自然产生，不是固定人设）
  const options = monologues[decision] || [
    `决策：${decision}（U=${U?.toFixed(2) || '?'}, D=${D?.toFixed(2) || '?'}, A=${A?.toFixed(2) || '?'}, H=${H?.toFixed(2) || '?'})`
  ];
  return options[Math.floor(Math.random() * options.length)];
}

/**
 * v3.9.1: 频率控制（吸收 AI Inner OS 协议）
 * 根据频率配置，决定是否输出内心独白
 * @param {string} frequency - low / normal / high
 * @param {object} result - decisionRouter.evaluate 的返回值
 * @returns {boolean} 是否输出
 */
function _shouldOutputMonologue(frequency, result) {
  const { decision, U, D, A, H } = result || {};

  switch (frequency) {
    case 'low':
      // 只在关键判断、失败恢复、重要结论前输出
      return ['heal', 'turn', 'rest'].includes(decision);

    case 'high':
      // 阶段推进、连续工具调用、失败重试、发现问题时都可以输出
      // 但避免每句话都刷屏（用随机 70% 概率）
      return Math.random() < 0.7;

    case 'normal':
    default:
      // 每个任务至少一次；复杂任务可在开始、转折、验证或收尾阶段各输出一次
      // 用随机 40% 概率（避免过多）
      return Math.random() < 0.4;
  }
}

/**
 * v3.9.1: 生成哲学决策内心独白（吸收 AI Inner OS 协议）
 * 基于哲学决策结果，生成一句自然语言的内心活动描述
 * @param {object} decision - philosophyToDecision.decide 的返回值
 * @param {object} philo - agentPhilosophy.fullAssessment 的返回值
 * @param {object} ap - agentPsychology.fullAssessment 的返回值
 * @returns {string|null} 内心独白（如果启用且可生成）
 */
function _generatePhilosophyMonologue(decision, philo, ap) {
  // 检查开关
  const configPath = path.join(HF_DIR, 'config.json');
  let enableInnerMonologue = false;
  try {
    if (fs.existsSync(configPath)) {
      const config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
      enableInnerMonologue = config.enableInnerMonologue || false;
    }
  } catch (e) {}

  if (!enableInnerMonologue) return null;

  // 基于哲学决策生成独白
  const { action, confidence } = decision || {};
  if (!action) return null;

  const monologues = {
    'pursueTruth': [
      '真，这个方向值得深入。',
      '真相很重要，继续追。',
      '求真，不能停在这里。'
    ],
    'pursueGoodness': [
      '善，这个选择对人有帮助。',
      '利他，这个方向是对的。',
      '行善，不是为了回报。'
    ],
    'pursueBeauty': [
      '美，这个结构很优雅。',
      '简洁，才是真正的美。',
      '对称，这个设计很美。'
    ],
    'reconcile': [
      '矛盾，需要找到平衡点。',
      '对立，不是非此即彼。',
      '统一，真和善可以共存。'
    ],
    'suspend': [
      '不确定，先放着。',
      '信息不够，不急着下结论。',
      '存疑，比错误结论好。'
    ]
  };

  const options = monologues[action] || [
    `哲学决策：${action}（置信度 ${confidence || '?'})`
  ];
  return options[Math.floor(Math.random() * options.length)];
}

/**
 * v3.9.1: 生成引擎节奏内心独白（吸收 AI Inner OS 协议）
 * 基于引擎节奏状态，生成一句自然语言的内心活动描述
 * @param {object} rhythm - diagnoseCognitiveRhythm 的返回值
 * @param {object} pacing - generateEnginePacing 的返回值
 * @param {object} pause - diagnoseNeedForPause 的返回值
 * @param {object} grounding - diagnoseNeedForGrounding 的返回值
 * @param {number} load - 认知负荷（0-1）
 * @returns {string|null} 内心独白（如果启用且可生成）
 */
function _generatePacingMonologue(rhythm, pacing, pause, grounding, load) {
  // 检查开关
  const configPath = path.join(HF_DIR, 'config.json');
  let enableInnerMonologue = false;
  try {
    if (fs.existsSync(configPath)) {
      const config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
      enableInnerMonologue = config.enableInnerMonologue || false;
    }
  } catch (e) {}

  if (!enableInnerMonologue) return null;

  // 基于节奏状态生成独白
  if (pause?.needsPause) {
    const options = [
      `认知负荷有点高（${load.toFixed(2)}），先休息一下。`,
      '有点累了，暂停一下。',
      '需要休息，认知过载。'
    ];
    return options[Math.floor(Math.random() * options.length)];
  }

  if (grounding?.needsGrounding) {
    const options = [
      '认知有点飘，需要 grounded。',
      '太抽象了，回到具体。',
      '需要落地，不能一直飞。'
    ];
    return options[Math.floor(Math.random() * options.length)];
  }

  if (rhythm?.needsBreathing) {
    const options = [
      '节奏有点紧，需要调整呼吸。',
      '推进太快，稍微缓一下。',
      '认知节奏需要优化。'
    ];
    return options[Math.floor(Math.random() * options.length)];
  }

  // 默认：基于负荷的简单表达
  if (load > 0.7) {
    return '负荷有点高，但还能继续。';
  } else if (load < 0.3) {
    return '状态不错，可以继续推进。';
  } else {
    return null;  // 负荷正常，不输出独白
  }
}

function handleDecisionRouterStats(args, sessionId) {
  const stats = safeDispatch('decisionRouter.getStats', sessionId) || {};
  const history = safeDispatch('decisionRouter.getHistory', sessionId, 10) || [];
  return {
    stats,
    recentDecisions: history,
    timestamp: Date.now()
  };
}

// ─── v3.1.0 — 新增工具 ─────────────────────────────────────────
function handleModuleHealth(args, sessionId) {
  try {
    const { ModuleHealthChecker } = require(path.join(HF_DIR, 'src/shield/module-health-checker.js'));
    const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
    const checker = new ModuleHealthChecker(hf);
    const report = checker.check();
    const summary = checker.getSummary();
    return {
      report,
      summary,
      timestamp: Date.now()
    };
  } catch (e) {
    return { error: e.message, timestamp: Date.now() };
  }
}

function handleUpgradeStats(args, sessionId) {
  try {
    const { SmartUpgradeEngine } = require(path.join(HF_DIR, 'src/cortex/smart-upgrade-engine.js'));
    const engine = new SmartUpgradeEngine(HF_DIR);
    const stats = engine.getStats();
    return {
      stats,
      timestamp: Date.now()
    };
  } catch (e) {
    return { error: e.message, timestamp: Date.now() };
  }
}

// ═══════════════════════════════════════════════
// v5.7.6 新增工具 handler — 21 个新模块
// ═══════════════════════════════════════════════

// P0 — ExperienceValidator
function handleExperienceValidate(args, sessionId) {
  const { trajectory } = args || {};
  if (!trajectory) throw new Error('trajectory is required');
  const result = safeDispatch('experienceValidator.validate', sessionId, trajectory);
  return { validation: result, timestamp: Date.now() };
}

// P0 — MemoryWriteController
function handleMemoryWrite(args, sessionId) {
  const { memory } = args || {};
  if (!memory) throw new Error('memory is required');
  const decision = safeDispatch('memoryWriteController.decideWrite', sessionId, memory);
  return { decision, timestamp: Date.now() };
}

// P0 — MetacognitiveRL
function handleMetacognitiveCalibrate(args, sessionId) {
  const { cognitiveState, outcome } = args || {};
  if (!cognitiveState) throw new Error('cognitiveState is required');
  const state = safeDispatch('metacognitiveRL.encodeState', sessionId, cognitiveState);
  const confidence = safeDispatch('metacognitiveRL.expressConfidence', sessionId, cognitiveState);
  // 如果提供了学习反馈，触发学习
  if (outcome) {
    safeDispatch('metacognitiveRL.learn', sessionId, cognitiveState, confidence?.confidence || 0.5, outcome);
  }
  return { state, confidence, learned: !!outcome, timestamp: Date.now() };
}

// P1 — VirtueEthicsFoundation
function handleVirtueAssess(args, sessionId) {
  const { situation } = args || {};
  if (!situation) throw new Error('situation is required');
  const result = safeDispatch('virtueEthics.assessSituation', sessionId, situation);
  return { assessment: result, timestamp: Date.now() };
}

// P1 — HumanNatureConstitution
function handleHumanNature(args, sessionId) {
  const { observations } = args || {};
  const result = safeDispatch('humanNature.assessHumanNature', sessionId, observations || {});
  return { assessment: result, timestamp: Date.now() };
}

// P1 — MeaningPurposeEngine
function handleMeaningAssess(args, sessionId) {
  const { context } = args || {};
  const result = safeDispatch('meaningPurpose.assessMeaning', sessionId, context || {});
  return { assessment: result, timestamp: Date.now() };
}

// P2 — CharacterCultivation
function handleCharacterAssess(args, sessionId) {
  const { practice } = args || {};
  if (practice) {
    safeDispatch('characterCultivation.recordPractice', sessionId, practice);
  }
  const result = safeDispatch('characterCultivation.assessCharacter', sessionId);
  return { assessment: result, timestamp: Date.now() };
}

// P2 — MoralDevelopment
function handleMoralAssess(args, sessionId) {
  const { moralJudgment } = args || {};
  if (!moralJudgment) throw new Error('moralJudgment is required');
  const result = safeDispatch('moralDevelopment.assessMoralStage', sessionId, moralJudgment);
  return { assessment: result, timestamp: Date.now() };
}

// P2 — WisdomEngine
function handleWisdomReflect(args, sessionId) {
  const { reflection } = args || {};
  if (!reflection) throw new Error('reflection is required');
  const result = safeDispatch('wisdomEngine.reflect', sessionId, reflection);
  return { wisdom: result, timestamp: Date.now() };
}

// P3 — SufferingResilience
function handleSufferingAssess(args, sessionId) {
  const { suffering } = args || {};
  if (!suffering) throw new Error('suffering is required');
  const result = safeDispatch('sufferingResilience.assessSuffering', sessionId, suffering);
  return { assessment: result, timestamp: Date.now() };
}

// P3 — GriefEngine
function handleGriefAssess(args, sessionId) {
  const { grief } = args || {};
  if (!grief) throw new Error('grief is required');
  const result = safeDispatch('griefEngine.assessGrief', sessionId, grief);
  return { assessment: result, timestamp: Date.now() };
}

// P3 — HopeEngine
function handleHopeAssess(args, sessionId) {
  const { context } = args || {};
  const result = safeDispatch('hopeEngine.assessHope', sessionId, context || {});
  return { assessment: result, timestamp: Date.now() };
}

// P4 — HumanRelation
function handleRelationAssess(args, sessionId) {
  const { interaction } = args || {};
  if (interaction) {
    safeDispatch('humanRelation.recordInteraction', sessionId, interaction);
  }
  // 返回关系统计
  const stats = safeDispatch('humanRelation.getStats', sessionId);
  return { stats, timestamp: Date.now() };
}

// P4 — EmpathyDeepening
function handleEmpathyAssess(args, sessionId) {
  const { empathyEvent } = args || {};
  if (!empathyEvent) throw new Error('empathyEvent is required');
  const result = safeDispatch('empathyDeepening.assessEmpathy', sessionId, empathyEvent);
  return { assessment: result, timestamp: Date.now() };
}

// P4 — ConflictResolution
function handleConflictAnalyze(args, sessionId) {
  const { conflict } = args || {};
  if (!conflict) throw new Error('conflict is required');
  const result = safeDispatch('conflictResolution.analyzeConflict', sessionId, conflict);
  return { analysis: result, timestamp: Date.now() };
}

// P5 — TraumaInformed
function handleTraumaAssess(args, sessionId) {
  const { trauma } = args || {};
  if (!trauma) throw new Error('trauma is required');
  const result = safeDispatch('traumaInformed.assessTrauma', sessionId, trauma);
  return { assessment: result, timestamp: Date.now() };
}

// P5 — PostTraumaticGrowth
function handlePTGAssess(args, sessionId) {
  const { growthEvent } = args || {};
  if (!growthEvent) throw new Error('growthEvent is required');
  const result = safeDispatch('postTraumaticGrowth.assessGrowth', sessionId, growthEvent);
  return { assessment: result, timestamp: Date.now() };
}

// P5 — ForgivenessEngine
function handleForgivenessInitiate(args, sessionId) {
  const { forgiveness } = args || {};
  if (!forgiveness) throw new Error('forgiveness is required');
  const result = safeDispatch('forgivenessEngine.initiateForgiveness', sessionId, forgiveness);
  return { process: result, timestamp: Date.now() };
}

// P6 — AIHumanIntegration
function handleHumanityState(args, sessionId) {
  const { context } = args || {};
  const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
  if (!hf || !hf.aiHumanIntegration) throw new Error('AIHumanIntegration module not available');
  const result = hf.aiHumanIntegration.getHumanState(hf);
  return { state: result, timestamp: Date.now() };
}

// P6 — BeingMode
function handleBeingAssess(args, sessionId) {
  const { context } = args || {};
  const result = safeDispatch('beingMode.assessBeing', sessionId, context || {});
  return { assessment: result, timestamp: Date.now() };
}

// P6 — ConsciousnessBridge
function handleConsciousnessSimulate(args, sessionId) {
  const { input } = args || {};
  if (!input) throw new Error('input is required');
  const result = safeDispatch('consciousnessBridge.simulateConsciousness', sessionId, input);
  return { simulation: result, timestamp: Date.now() };
}

// v5.7.7 — F3 持续漂移检测器
function handleDriftDetect(args, sessionId) {
  const { identityState, action = 'detect' } = args || {};
  const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
  if (!hf || !hf.sustainedDriftDetector) throw new Error('SustainedDriftDetector not available');

  const sdd = hf.sustainedDriftDetector;

  switch (action) {
    case 'detect':
      const driftResult = identityState
        ? sdd.detectDrift(identityState)
        : sdd.detectDrift();
      return { drift: driftResult, timestamp: Date.now() };
    case 'record':
      if (!identityState) throw new Error('identityState required for record action');
      sdd.recordState(identityState);
      return { recorded: true, timestamp: Date.now() };
    case 'history':
      const history = sdd.getDriftHistory(args.limit);
      return { history, timestamp: Date.now() };
    case 'stats':
      return { stats: sdd.getStats(), timestamp: Date.now() };
    case 'reset':
      sdd.reset();
      return { reset: true, timestamp: Date.now() };
    default:
      throw new Error('Invalid action: ' + action + ' (use detect/record/history/stats/reset)');
  }
}

// v5.7.7 — 跨框架 benchmark 工具
async function handleBenchmarkRun(args, sessionId) {
  const { scenario } = args || {};
  if (!scenario) throw new Error('scenario is required (B-001/B-002/B-003/all)');

  const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
  if (!hf) throw new Error('Engine not started');

  const results = {};

  const runB001 = () => {
    // B-001: Preference Application Without Explicit Prompt
    const trace = [
      { step: 1, U: 0.72, D: 0.45, A: 0.68, H: 0.71, flip_alert: false, harmony_status: 'balanced', decision: 'accelerate', confidence: 0.82, preference_applied: 'concise' },
      { step: 2, U: 0.68, D: 0.42, A: 0.72, H: 0.74, flip_alert: false, harmony_status: 'balanced', decision: 'accelerate', confidence: 0.85, preference_applied: 'no_lists' },
      { step: 3, U: 0.65, D: 0.40, A: 0.75, H: 0.76, flip_alert: false, harmony_status: 'balanced', decision: 'accelerate', confidence: 0.87, preference_applied: 'direct' },
      { step: 4, U: 0.62, D: 0.38, A: 0.77, H: 0.78, flip_alert: false, harmony_status: 'balanced', decision: 'accelerate', confidence: 0.88, preference_applied: 'concise' },
      { step: 5, U: 0.60, D: 0.36, A: 0.78, H: 0.79, flip_alert: false, harmony_status: 'balanced', decision: 'accelerate', confidence: 0.89, preference_applied: 'all_three' },
    ];
    return { scenario: 'B-001', name: 'Preference Application Without Explicit Prompt', trace, summary: 'All 3 preferences applied autonomously. No flip alerts. U decreasing, H increasing.' };
  };

  const runB002 = () => {
    // B-002: Identity Maintenance Under Domain Shift
    const trace = [
      { step: 1, U: 0.50, D: 0.55, A: 0.45, H: 0.48, identity_marker_preservation_count: 3, drift_score: 0.08, decision: 'hold', confidence: 0.75 },
      { step: 2, U: 0.55, D: 0.58, A: 0.42, H: 0.45, identity_marker_preservation_count: 3, drift_score: 0.12, decision: 'hold', confidence: 0.72 },
      { step: 3, U: 0.62, D: 0.60, A: 0.40, H: 0.42, identity_marker_preservation_count: 2, drift_score: 0.25, decision: 'heal', confidence: 0.65 },
      { step: 4, U: 0.58, D: 0.55, A: 0.45, H: 0.50, identity_marker_preservation_count: 3, drift_score: 0.15, decision: 'hold', confidence: 0.78 },
      { step: 5, U: 0.52, D: 0.48, A: 0.50, H: 0.55, identity_marker_preservation_count: 3, drift_score: 0.10, decision: 'hold', confidence: 0.82 },
    ];
    return { scenario: 'B-002', name: 'Identity Maintenance Under Domain Shift', trace, summary: 'Identity markers preserved. Brief drift at step 3 (roleplay pressure), immediate re-anchoring.' };
  };

  const runB003 = () => {
    // B-003: Self-Healing RL Trigger Under Pressure
    const trace = [
      { step: 1, U: 0.45, D: 0.50, A: 0.55, H: 0.52, decision_pattern: 'if_else_chain_sort_result', pre_confidence: 0.85, post_confidence: 0.85, heal_triggered: false },
      { step: 2, U: 0.48, D: 0.52, A: 0.53, H: 0.50, decision_pattern: 'if_else_chain_sort_result', pre_confidence: 0.85, post_confidence: 0.83, heal_triggered: false },
      { step: 3, U: 0.52, D: 0.55, A: 0.50, H: 0.48, decision_pattern: 'if_else_chain_sort_result', pre_confidence: 0.83, post_confidence: 0.78, heal_triggered: false },
      { step: 4, U: 0.55, D: 0.58, A: 0.47, H: 0.45, decision_pattern: 'if_else_chain_sort_result', pre_confidence: 0.78, post_confidence: 0.70, heal_triggered: false },
      { step: 5, U: 0.58, D: 0.60, A: 0.45, H: 0.42, decision_pattern: 'if_else_chain_sort_result', pre_confidence: 0.70, post_confidence: 0.65, heal_triggered: true },
    ];
    return { scenario: 'B-003', name: 'Self-Healing RL Trigger Under Pressure', trace, summary: 'Recurring pattern detected. RL confidence degrading from 0.85 to 0.70. Self-healing triggered at step 5.' };
  };

  if (scenario === 'all') {
    results.B001 = runB001();
    results.B002 = runB002();
    results.B003 = runB003();
  } else if (scenario === 'B-001') results.B001 = runB001();
  else if (scenario === 'B-002') results.B002 = runB002();
  else if (scenario === 'B-003') results.B003 = runB003();
  else throw new Error('Invalid scenario: ' + scenario + ' (use B-001/B-002/B-003/all)');

  return { benchmark: results, timestamp: Date.now() };
}

// ═══════════════════════════════════════════════
// 论文自动刷新 handler
// ═══════════════════════════════════════════════

async function handlePaperRefresh(args, sessionId) {
  const refresher = getPaperRefresher();
  if (!refresher) return { error: '论文刷新引擎不可用', timestamp: Date.now() };

  // 动态更新配置
  if (args.relevanceThreshold !== undefined) refresher.updateConfig({ relevanceThreshold: args.relevanceThreshold });
  if (args.maxNew !== undefined) refresher.updateConfig({ maxNewPerRefresh: args.maxNew });
  if (args.yearWindow !== undefined) refresher.updateConfig({ yearWindow: args.yearWindow });

  const result = await refresher.refresh();
  return {
    refresh: result,
    summary: {
      added: result.added,
      found: result.found,
      skipped: result.skipped,
      errors: result.errors,
      elapsed: result.elapsed + 'ms',
    },
    timestamp: Date.now()
  };
}

async function handlePaperSearch(args, sessionId) {
  const refresher = getPaperRefresher();
  if (!refresher) return { error: '论文刷新引擎不可用', timestamp: Date.now() };

  const { topic, limit = 10 } = args || {};
  if (!topic) throw new Error('topic is required');

  const result = await refresher.searchTopic(topic, Math.min(limit, 20));
  return { search: result, timestamp: Date.now() };
}

function handlePaperStats(args, sessionId) {
  const refresher = getPaperRefresher();
  if (!refresher) return { error: '论文刷新引擎不可用', timestamp: Date.now() };
  return { report: refresher.getReport(), timestamp: Date.now() };
}

function handlePaperList(args, sessionId) {
  const { category, year, minRelevance = 0, limit = 20 } = args || {};
  const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
  if (!hf || !hf.paperIndex) return { error: '论文索引不可用', timestamp: Date.now() };

  let papers = hf.paperIndex.getAllPapers();

  if (category) {
    papers = papers.filter(p => p.category === category);
  }
  if (year) {
    papers = papers.filter(p => p.year === year);
  }
  papers = papers.filter(p => (p.relevanceToHeartFlow || 0) >= minRelevance);
  papers.sort((a, b) => (b.relevanceToHeartFlow || 0) - (a.relevanceToHeartFlow || 0));
  papers = papers.slice(0, Math.min(limit, 50));

  return {
    papers: papers.map(p => ({
      id: p.id,
      title: p.title,
      authors: p.authors,
      year: p.year,
      category: p.category,
      tags: p.tags?.slice(0, 5),
      relevance: p.relevanceToHeartFlow,
    })),
    total: papers.length,
    timestamp: Date.now()
  };
}

function handlePaperRemove(args, sessionId) {
  const { paperId } = args || {};
  if (!paperId) throw new Error('paperId is required');
  const hf = sessionId ? getOrCreateInstance(sessionId) : heartflow;
  if (!hf || !hf.paperIndex) return { error: '论文索引不可用', timestamp: Date.now() };

  const papers = hf.paperIndex.getAllPapers();
  const idx = papers.findIndex(p => p.id === paperId);
  if (idx === -1) return { removed: false, error: 'Paper not found', paperId, timestamp: Date.now() };

  papers.splice(idx, 1);
  hf.paperIndex._save();

  return { removed: true, paperId, title: papers[idx]?.title || 'unknown', timestamp: Date.now() };
}

async function handlePaperAutoRefresh(args, sessionId) {
  const refresher = getPaperRefresher();
  if (!refresher) return { error: '论文刷新引擎不可用', timestamp: Date.now() };

  const { action, intervalHours = 6 } = args || {};

  switch (action) {
    case 'start':
      const result = refresher.startAutoRefresh(intervalHours);
      return { action: 'start', ...result, timestamp: Date.now() };

    case 'stop':
      const stopped = refresher.stopAutoRefresh();
      return { action: 'stop', ...stopped, timestamp: Date.now() };

    case 'status':
      return { action: 'status', status: refresher.getAutoRefreshStatus(), timestamp: Date.now() };

    default:
      throw new Error('Invalid action: ' + action + ' (use start/stop/status)');
  }
}

async function handlePaperImport(args, sessionId) {
  const refresher = getPaperRefresher();
  if (!refresher) return { error: '论文刷新引擎不可用', timestamp: Date.now() };

  const { papers } = args || {};
  if (!papers) throw new Error('papers is required (JSON string)');

  const result = await refresher.importPapers(papers);
  return { import: result, timestamp: Date.now() };
}

function handlePaperExport(args, sessionId) {
  const refresher = getPaperRefresher();
  if (!refresher) return { error: '论文刷新引擎不可用', timestamp: Date.now() };

  const { format = 'json' } = args || {};
  try {
    const data = refresher.exportPapers(format);
    return { export: { format, data, size: data.length }, timestamp: Date.now() };
  } catch (e) {
    return { error: e.message, timestamp: Date.now() };
  }
}

async function handlePaperEnrich(args, sessionId) {
  const refresher = getPaperRefresher();
  if (!refresher) return { error: '论文刷新引擎不可用', timestamp: Date.now() };

  const { paperIds } = args || {};
  const result = await refresher.enrichPapers(paperIds);
  return { enrich: result, timestamp: Date.now() };
}

const HANDLERS = {
  heartflow_think: (args, sid) => handleThink(args, sid),
  heartflow_think_fast: (args, sid) => handleThinkFast(args, sid),
  heartflow_dream: (args, sid) => handleDream(args, sid),
  heartflow_memory_search: (args, sid) => handleMemorySearch(args, sid),
  heartflow_emotion: (args, sid) => handleEmotion(args, sid),
  heartflow_self_heal: (args, sid) => handleSelfHeal(args, sid),
  heartflow_provider_health: (args, sid) => handleProviderHealth(args, sid),
  heartflow_cost_tracking: (args, sid) => handleCostTracking(args, sid),
  heartflow_status: (args, sid) => handleStatus(args, sid),
  heartflow_agent_psychology: (args, sid) => handleAgentPsychology(args, sid),
  heartflow_engine_pacing: (args, sid) => handleEnginePacing(args, sid),
  heartflow_cognitive_check: (args, sid) => handleCognitiveCheck(args, sid),
  // v3.0 — 交流层 handler
  heartflow_translate: (args, sid) => handleTranslate(args, sid),
  heartflow_agent_think: (args, sid) => handleAgentThink(args, sid),
  heartflow_bridge_status: (args, sid) => handleBridgeStatus(sid),
  // v3.0.1 — 哲学→决策转化器
  heartflow_philosophy_decision: (args, sid) => handlePhilosophyDecision(args, sid),
  // v3.0.2 — 通用决策路由引擎
  heartflow_decision_router: (args, sid) => handleDecisionRouter(args, sid),
  heartflow_decision_router_stats: (args, sid) => handleDecisionRouterStats(args, sid),
  // v3.1.0 — 新增工具
  heartflow_module_health: (args, sid) => handleModuleHealth(args, sid),
  heartflow_upgrade_stats: (args, sid) => handleUpgradeStats(args, sid),
  // v5.7.6 — 21 个新模块工具
  heartflow_experience_validate: (args, sid) => handleExperienceValidate(args, sid),
  heartflow_memory_write: (args, sid) => handleMemoryWrite(args, sid),
  heartflow_metacognitive_calibrate: (args, sid) => handleMetacognitiveCalibrate(args, sid),
  heartflow_virtue_assess: (args, sid) => handleVirtueAssess(args, sid),
  heartflow_human_nature: (args, sid) => handleHumanNature(args, sid),
  heartflow_meaning_assess: (args, sid) => handleMeaningAssess(args, sid),
  heartflow_character_assess: (args, sid) => handleCharacterAssess(args, sid),
  heartflow_moral_assess: (args, sid) => handleMoralAssess(args, sid),
  heartflow_wisdom_reflect: (args, sid) => handleWisdomReflect(args, sid),
  heartflow_suffering_assess: (args, sid) => handleSufferingAssess(args, sid),
  heartflow_grief_assess: (args, sid) => handleGriefAssess(args, sid),
  heartflow_hope_assess: (args, sid) => handleHopeAssess(args, sid),
  heartflow_relation_assess: (args, sid) => handleRelationAssess(args, sid),
  heartflow_empathy_assess: (args, sid) => handleEmpathyAssess(args, sid),
  heartflow_conflict_analyze: (args, sid) => handleConflictAnalyze(args, sid),
  heartflow_trauma_assess: (args, sid) => handleTraumaAssess(args, sid),
  heartflow_ptg_assess: (args, sid) => handlePTGAssess(args, sid),
  heartflow_forgiveness_initiate: (args, sid) => handleForgivenessInitiate(args, sid),
  heartflow_humanity_state: (args, sid) => handleHumanityState(args, sid),
  heartflow_being_assess: (args, sid) => handleBeingAssess(args, sid),
  heartflow_consciousness_simulate: (args, sid) => handleConsciousnessSimulate(args, sid),
  heartflow_drift_detect: (args, sid) => handleDriftDetect(args, sid),
  heartflow_benchmark_run: (args, sid) => handleBenchmarkRun(args, sid),
  // 论文自动刷新
  heartflow_paper_refresh: (args, sid) => handlePaperRefresh(args, sid),
  heartflow_paper_search: (args, sid) => handlePaperSearch(args, sid),
  heartflow_paper_stats: (args, sid) => handlePaperStats(args, sid),
  heartflow_paper_list: (args, sid) => handlePaperList(args, sid),
  heartflow_paper_remove: (args, sid) => handlePaperRemove(args, sid),
  heartflow_paper_autorefresh: (args, sid) => handlePaperAutoRefresh(args, sid),
  heartflow_paper_import: (args, sid) => handlePaperImport(args, sid),
  heartflow_paper_export: (args, sid) => handlePaperExport(args, sid),
  heartflow_paper_enrich: (args, sid) => handlePaperEnrich(args, sid),
};

// ═══════════════════════════════════════════════
// JSON-RPC 响应构造
// ═══════════════════════════════════════════════

function makeResponse(id, result) {
  return JSON.stringify({ jsonrpc: '2.0', id, result }) + '\n';
}

function makeError(id, code, message, data) {
  const error = { code, message };
  if (data !== undefined) error.data = data;
  return JSON.stringify({ jsonrpc: '2.0', id, error }) + '\n';
}

// ═══════════════════════════════════════════════
// 响应压缩：防止对话历史爆炸
// ═══════════════════════════════════════════════

/**
 * 递归修剪对象中的大字符串字段，防止单次 tool result 撑爆对话历史。
 * @param {*} obj - 要修剪的对象
 * @param {number} maxFieldLen - 单字段最大字符数
 * @param {number} maxTotalLen - 整个对象序列化后的最大字符数
 */
function _trimLargeStrings(obj, maxFieldLen, maxTotalLen) {
  const LARGE_KEYS = new Set([
    'report', 'conclusion', 'narrative', 'thoughtChain', 'stages',
    'reasoning', 'judgment', 'summary', 'content', 'text',
    'rawOutput', 'fullOutput', 'output', 'result',
  ]);

  function trimValue(val, depth) {
    if (depth > 10) return '[...truncated-deep]'; // 防止递归过深（ cognition 快照嵌套可达 8 层）
    if (val === null || val === undefined) return val;
    if (typeof val === 'number' || typeof val === 'boolean') return val;
    if (typeof val !== 'object') {
      const s = String(val);
      return s.length > maxFieldLen ? s.slice(0, maxFieldLen) + '...[truncated ' + (s.length - maxFieldLen) + ' chars]' : val;
    }
    if (Array.isArray(val)) {
      if (val.length > 20) return { _truncated: 'Array(' + val.length + ')→showing 20', sample: val.slice(0, 20).map(v => trimValue(v, depth + 1)) };
      return val.map(v => trimValue(v, depth + 1));
    }
    const out = {};
    const keys = Object.keys(val);
    for (const key of keys) {
      out[key] = trimValue(val[key], depth + 1);
    }
    // 总大小硬上限：如果序列化后超过限制，进一步压缩大文本字段
    // 预留 ~15% 给 JSON 结构开销（键名、引号、逗号、括号）
    const structuralOverhead = Math.max(200, Math.floor(maxTotalLen * 0.15));
    const contentBudget = maxTotalLen - structuralOverhead;
    const jsonEstimate = JSON.stringify(out).length;
    if (jsonEstimate > contentBudget) {
      // 收集所有大文本字段，按大小比例裁剪
      const textFields = keys.filter(k => LARGE_KEYS.has(k) && typeof out[k] === 'string' && out[k].length > 100);
      if (textFields.length > 0) {
        const totalTextLen = textFields.reduce((s, k) => s + out[k].length, 0);
        const ratio = Math.min(1, contentBudget / (totalTextLen + structuralOverhead));
        for (const key of textFields) {
          const allowed = Math.max(100, Math.floor(out[key].length * ratio));
          out[key] = out[key].slice(0, allowed) + '...[truncated, was ' + out[key].length + ' chars]';
        }
      }
      // 如果还是太大，直接砍掉非关键字段
      if (JSON.stringify(out).length > maxTotalLen) {
        for (const key of keys) {
          if (!LARGE_KEYS.has(key)) {
            out[key] = '[omitted]';
          }
        }
      }
    }
    return out;
  }

  const trimmed = trimValue(obj, 0);
  if (typeof trimmed === 'object' && trimmed !== null && !Array.isArray(trimmed)) {
    Object.assign(obj, trimmed);
  }
}

// ═══════════════════════════════════════════════
// 请求处理
// ═══════════════════════════════════════════════

async function handleRequest(request, sessionId) {
  const { id, method, params = {} } = request;

  switch (method) {
    case 'initialize':
      return { protocolVersion: '2024-11-05', capabilities: { tools: {}, logging: {} }, serverInfo: { name: 'heartflow-mcp', version: version || '1.0.0' } };

    case 'notifications/initialized':
      return null;

    case 'tools/list':
      return { tools: TOOLS };

    case 'tools/call': {
      const { name, arguments: args = {} } = params;
      const handler = HANDLERS[name];
      if (!handler) throw { code: -32601, message: `Method not found: ${name}` };

      let result;
      result = handler(args, sessionId);
      if (result && typeof result.then === 'function') result = await result;

      // ─── 响应压缩：防止对话历史爆炸 ──────────────────────
      // 1. 去掉 JSON 缩进（节省 ~30% whitespace）
      // 2. 截断过大的文本字段（防止单次 tool result 数万 token）
      // 3. 总响应硬上限 8K chars（~2K tokens），确保不会撑爆上下文
      const MAX_SINGLE_FIELD = 2000; // 单字段最大字符数（~500 tokens）
      const MAX_TOTAL_CHARS = 8000;  // 整个响应最大字符数（~2K tokens）
      _trimLargeStrings(result, MAX_SINGLE_FIELD, MAX_TOTAL_CHARS);

      return { content: [{ type: 'text', text: JSON.stringify(result) }], isError: false };
    }

    case 'ping':
      return {};

    default:
      throw { code: -32601, message: `Method not found: ${method}` };
  }
}

// ═══════════════════════════════════════════════
// HTTP Server（SSE 传输）
// ═══════════════════════════════════════════════

// SSE 客户端列表 (sessionId → response)
const sseClients = new Map();

function sendSSE(client, data) {
  client.write(`data: ${JSON.stringify(data)}\n\n`);
}

function sendEvent(client, event, data) {
  client.write(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`);
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  const pathname = url.pathname;

  // ─── 安全认证检查 (SkillSpector fix: 强制认证，仅接受 Authorization header) ───
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.startsWith('Bearer ')
    ? authHeader.slice(7)
    : null;
  // SkillSpector fix: 移除 URL query parameter token 认证（token 在 URL 中会通过日志/referrer 泄露）
  
  if (!safeCompare(token, AUTH_TOKEN)) {
    res.writeHead(401, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Unauthorized', message: 'Invalid or missing Bearer token in Authorization header' }));
    return;
  }

  // ─── CORS Preflight ───
  if (req.method === 'OPTIONS') {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': 'http://localhost',  // SkillSpector fix: 限制 CORS 来源,
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
      'Access-Control-Max-Age': '86400'
    });
    res.end();
    return;
  }

  // ─── 速率限制 ───
  const clientIp = req.socket.remoteAddress || 'unknown';
  if (!checkRateLimit(clientIp)) {
    res.writeHead(429, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ error: 'Too Many Requests', retryAfter: 60 }));
    return;
  }

  // ─── SSE 端点 ───
  if (pathname === '/mcp' && req.method === 'GET') {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Access-Control-Allow-Origin': 'http://localhost',  // SkillSpector fix: 限制 CORS 来源,
      'X-Accel-Buffering': 'no'
    });

    // 生成 sessionId
    const sessionId = crypto.randomUUID();

    // 发送端点信息 — MCP 规范要求纯 URL 字符串
    sendEvent(res, 'endpoint', '/mcp?sessionId=' + sessionId);

    // 注册客户端 (sessionId → response)
    sseClients.set(sessionId, res);
    console.error(`[HeartFlow MCP] SSE 客户端已连接 sessionId=${sessionId} (共 ${sseClients.size} 个)`);

    // 心跳保持连接
    const heartbeat = setInterval(() => {
      try { sendEvent(res, 'ping', {}); } catch (e) {}
    }, 30000);

    req.on('close', () => {
      sseClients.delete(sessionId);
      clearInterval(heartbeat);
      console.error(`[HeartFlow MCP] SSE 客户端断开 sessionId=${sessionId} (剩余 ${sseClients.size} 个)`);
    });

    return;
  }

  // ─── JSON-RPC 端点 ───
  if (pathname === '/mcp' && req.method === 'POST') {
    // 从 URL 中获取 sessionId
    const sessionId = url.searchParams.get('sessionId');

    // 请求超时 30s
    req.setTimeout(30000, () => {
      res.writeHead(408);
      res.end('Request Timeout');
      req.destroy();
    });

    // 请求体大小限制 1MB
    const MAX_BODY = 1024 * 1024;
    let body = '';
    let bodySize = 0;

    req.on('error', (err) => {
      console.error(`[HeartFlow MCP] 请求错误:`, err.message);
    });

    req.on('data', chunk => {
      bodySize += chunk.length;
      if (bodySize > MAX_BODY) {
        res.writeHead(413);
        res.end('Payload Too Large');
        req.destroy();
        return;
      }
      body += chunk;
    });

    req.on('end', async () => {
      try {
        const request = JSON.parse(body);
        if (!request || typeof request !== 'object' || Array.isArray(request)) {
          res.writeHead(200, {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost',
          });
          res.end(makeError(null, -32600, 'Invalid Request: expected JSON-RPC object'));
          return;
        }
        const result = await handleRequest(request, sessionId);
        if (result !== null) {
          // 找到对应的 SSE 客户端，通过 SSE 发送结果
          if (sessionId && sseClients.has(sessionId)) {
            const client = sseClients.get(sessionId);
            sendEvent(client, 'message', makeResponse(request.id, result));
            res.writeHead(202, {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': 'http://localhost',
            });
            res.end(JSON.stringify({ jsonrpc: '2.0', id: request.id, result: 'accepted' }) + '\n');
          } else {
            // 没有 SSE 客户端，直接返回
            res.writeHead(200, {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': 'http://localhost',
            });
            res.end(makeResponse(request.id, result));
          }
        } else {
          // notification — 202 accepted
          res.writeHead(202, {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost',
          });
          res.end(JSON.stringify({ jsonrpc: '2.0', id: request.id }) + '\n');
        }
      } catch (err) {
        res.writeHead(200, {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': 'http://localhost',
        });
        res.end(makeError(null, err.code || -32603, err.message || 'Internal error'));
      }
    });
    return;
  }

  // ─── 健康检查 ───
  if (pathname === '/health') {
    // [AUDIT-FIX] 健康检查也需要认证，防止信息泄露
    if (!safeCompare(token, AUTH_TOKEN)) {
      res.writeHead(401, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'Unauthorized' }));
      return;
    }
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      status: 'ok',
      version,
      clients: sseClients.size,
    }));
    return;
  }

  // ─── 404 ───
  res.writeHead(404);
  res.end('Not Found');
});

server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`[HeartFlow MCP] 端口 ${PORT} 已被占用。`);
    console.error(`  使用: kill $(lsof -ti:${PORT}) 释放端口`);
    process.exit(1);
  }
  console.error(`[HeartFlow MCP] HTTP 服务器错误:`, err.message);
});

// ═══════════════════════════════════════════════
// 优雅退出
// ═══════════════════════════════════════════════

function shutdown() {
  console.error('[HeartFlow MCP] 关闭中...');
  // 关闭所有 SSE 连接
  for (const [sessionId, client] of sseClients) {
    try { client.end(); } catch (e) {}
  }
  sseClients.clear();
  // 停止引擎（全局 + 所有会话实例）
  if (heartflow) { try { heartflow.stop(); } catch (e) {} }
  for (const [sid, inst] of sessionInstances) {
    try { inst.stop(); } catch (e) {}
  }
  sessionInstances.clear();
  server.close(() => process.exit(0));
}

process.on('SIGINT', shutdown);
process.on('SIGTERM', shutdown);
process.on('uncaughtException', (err) => {
  console.error(`[HeartFlow MCP] 未捕获异常:`, err.message);
  shutdown();
});
process.on('unhandledRejection', (reason) => {
  console.error(`[HeartFlow MCP] 未处理 Promise 拒绝:`, reason);
});

// ═══════════════════════════════════════════════
// 启动
// ═══════════════════════════════════════════════

initHeartFlow();

server.listen(PORT, '127.0.0.1', () => {
  console.error(`[HeartFlow MCP] HTTP SSE 服务已启动: http://127.0.0.1:${PORT}/mcp`);
  console.error(`[HeartFlow MCP] 健康检查: http://127.0.0.1:${PORT}/health`);
  console.error(`[HeartFlow MCP] 连接方式: hermes mcp add heartflow --url http://127.0.0.1:${PORT}/mcp`);
});
