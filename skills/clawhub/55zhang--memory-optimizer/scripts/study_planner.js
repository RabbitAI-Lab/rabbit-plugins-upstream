#!/usr/bin/env node
'use strict';
/**
 * 记忆与学习优化器 - 备考阶段增强版（Node.js）
 * 基于遗忘曲线与间隔复习科学，生成个性化学习与复习计划
 * 与 sleep-optimizer 同系列：循证科学 + 生活阶段适配 + 可视化报告
 */

// ==================== 工具函数 ====================

function esc(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function pyRound(x, digits) {
  const factor = Math.pow(10, digits);
  const scaled = x * factor;
  const fl = Math.floor(scaled);
  const frac = scaled - fl;
  let r;
  if (Math.abs(frac - 0.5) < 1e-9) {
    r = fl % 2 === 0 ? fl : fl + 1;
  } else {
    r = Math.round(scaled);
  }
  return (r / factor).toFixed(digits);
}

function pyFloatStr(x) {
  return Number.isInteger(x) ? x.toFixed(1) : String(x);
}

const BLOCK = '█';
const SHADE = '░';
const DOT = '·';

/** 遗忘曲线保留率：R(t) = e^(-t/S)，S 为记忆强度（天） */
function retention(t, S) {
  return Math.exp(-t / S) * 100;
}

// ==================== 科学常量 ====================
// 科学依据：
// - 遗忘曲线 (Ebbinghaus, 1885)
// - 间隔效应/最佳间隔约为记忆保持期10-20% (Cepeda et al., 2008, PNAS)
// - 间隔复习与测试效应为高效学习技术 (Dunlosky et al., 2013, Psychological Science in the Public Interest)
// - 检索练习优于概念图 (Karpicke & Blunt, 2011, Science)
// - 睡眠记忆巩固 (Rasch & Born, 2013, Physiological Reviews, IF 37.3)

/** 备考阶段配置（记忆/学习适配版） */
const STAGE_CONFIGS = {
  daily_study: {
    name: '日常学习',
    daily_hours: [2, 4],
    description: '上课期间保持学习节奏，对抗日常遗忘',
    challenges: ['内容分散', '课后遗忘快', '缺乏系统复习'],
    recommendations: [
      '当天内容当天晚复习（睡前30分钟回顾，利用睡眠巩固）',
      '每周末对本周内容做一次综合检索练习',
      '每章学完立即自测，不要等考前才翻书'
    ],
    review_ratio: 0.3,
    special: '每周日安排 1 小时周回顾'
  },
  midterm: {
    name: '期中备考',
    daily_hours: [3, 5],
    description: '考前2-4周启动，覆盖前半学期内容',
    challenges: ['复习范围不清', '时间分配失衡', '前摄抑制'],
    recommendations: [
      '考前3周开始间隔复习，不要考前3天突击',
      '按章节制作检索式笔记（用自己的话重写）',
      '考前2天回归知识框架图，查漏补缺'
    ],
    review_ratio: 0.4,
    special: '考前2天：快速过一遍错题与框架'
  },
  final_review: {
    name: '期末复习周',
    daily_hours: [4, 8],
    description: '短期高强度复习，多科目并行',
    challenges: ['多科目同时复习', '时间紧迫', '记忆超载'],
    recommendations: [
      '睡前1小时复习重点，利用睡眠巩固记忆（Rasch & Born 2013）',
      '多科目采用交错复习，避免单科连坐4小时',
      '睡眠优先：连续熬夜会破坏记忆巩固，避免连续<6小时',
      '考前一天回归框架图，不再学新内容'
    ],
    review_ratio: 0.45,
    special: '考前3天：全科目快速回顾，不再深入新难点'
  },
  exam_week: {
    name: '考试周',
    daily_hours: [3, 6],
    description: '考试期间保持状态，配合考试节奏',
    challenges: ['考试焦虑', '科目衔接紧', '状态波动'],
    recommendations: [
      '每场考试间只做错题与要点快速回顾',
      '保证7小时以上睡眠（可联动 sleep-optimizer 技能）',
      '午间小睡15-20分钟恢复警觉性'
    ],
    review_ratio: 0.5,
    special: '考试日早上：只过一遍自己的要点卡片'
  },
  postgraduate_prep: {
    name: '考研备考',
    daily_hours: [6, 10],
    description: '长期高强度备考，记忆巩固是关键',
    challenges: ['战线长', '记忆负荷极大', '后期疲劳'],
    recommendations: [
      '间隔复习是核心武器：按1-3-7-15-31天滚动复习',
      '每周一次全科模考（检索练习强化提取）',
      '睡前1小时复习当日重点（睡眠巩固）',
      '固定作息减少决策疲劳，睡眠勿压缩至6小时以下'
    ],
    review_ratio: 0.4,
    special: '每月末：全科综合自测+调整下月计划'
  },
  civil_service_prep: {
    name: '考公备考',
    daily_hours: [5, 8],
    description: '行测申论高强度训练，题海与积累并重',
    challenges: ['题量大', '常识积累面广', '申论素材记忆'],
    recommendations: [
      '行测：刷题后当天整理错题本，隔天重做错题',
      '申论素材：利用碎片时间间隔记忆，睡前回顾金句',
      '模考作息与真实考试同步，训练生物钟'
    ],
    review_ratio: 0.35,
    special: '每周：一次完整模考+错题统计分析'
  },
  certificate_prep: {
    name: '证书备考（四六级/教资/计算机等）',
    daily_hours: [2, 5],
    description: '目标明确的中短期备考',
    challenges: ['听力/词汇遗忘快', '与课业时间冲突', '动力波动'],
    recommendations: [
      '词汇用间隔复习APP或自制卡片，每天固定时段',
      '听力材料精听+跟读，睡前重听当日材料',
      '考前1个月进入真题刷题阶段'
    ],
    review_ratio: 0.4,
    special: '碎片时间：排队/通勤时做轻量回顾'
  },
  skill_study: {
    name: '技能学习（编程/语言/乐器）',
    daily_hours: [1, 3],
    description: '长期技能习得，程序性记忆需要间隔练习',
    challenges: ['进步缓慢期', '练习枯燥', '遗忘与生疏'],
    recommendations: [
      '间隔练习优于集中练习：每天短时练习优于周末长时间',
      '每次练习结束前做一次"不看资料复现"',
      '睡前回想当日练习要点（睡眠对程序记忆巩固重要）'
    ],
    review_ratio: 0.25,
    special: '每周：一次综合项目/曲目串联练习'
  },
  thesis_research: {
    name: '论文/科研',
    daily_hours: [3, 6],
    description: '文献阅读与写作并行，深度理解优先',
    challenges: ['文献量大', '概念易混', '写作输出困难'],
    recommendations: [
      '每篇文献读完写3行摘要（用自己的话=精细加工）',
      '概念性内容用间隔复习对抗遗忘',
      '写作分块进行，每块结束回顾结构'
    ],
    review_ratio: 0.2,
    special: '每周末：回顾本周文献笔记并交叉关联'
  },
  vacation_study: {
    name: '假期自学',
    daily_hours: [2, 4],
    description: '假期保持学习节律，适度充电',
    challenges: ['作息混乱', '动力不足', '开学遗忘'],
    recommendations: [
      '固定每日学习时段，与假期作息差异<2小时',
      '开学前3-5天逐步恢复学习节奏',
      '假期学的内容开学后第一周安排一次系统复习'
    ],
    review_ratio: 0.3,
    special: '开学前1周：复盘假期所学并建立索引'
  }
};

/** 掌握程度 -> (记忆强度S天, 学习时间系数) */
const MASTERY = {
  '了解': { s: 3, mult: 1.0 },
  '熟悉': { s: 5, mult: 1.5 },
  '掌握': { s: 7, mult: 2.5 },
  '精通': { s: 10, mult: 3.5 }
};

/** 内容量单位 -> 每单位基础学习小时 */
const UNIT_HOURS = {
  '章': 2.5,
  '节': 1.5,
  '页': 0.15,
  '词': 0.03,
  '套题': 2.0,
  '讲': 1.8
};

/** 间隔复习时间表（天，扩张式） */
const INTERVALS = [1, 3, 7, 15, 31, 60];

/** 高效学习策略清单（附科学依据） */
const STRATEGIES = [
  ['检索练习（自测）', '合上书本回忆比重复阅读有效得多', 'Roediger & Karpicke, 2006, Psychological Science；Karpicke & Blunt, 2011, Science（检索练习优于概念图）'],
  ['间隔复习', '按 1-3-7-15-31 天滚动复习，对抗遗忘曲线', 'Cepeda et al., 2006, Psychological Bulletin；最佳间隔≈保持期10-20%（Cepeda et al., 2008, PNAS）'],
  ['交错练习', '不同科目/题型交替学习，而非单科长时间', 'Rohrer & Taylor, 2007, Instructional Science'],
  ['自我解释', '用自己的话重述要点，建立精细加工', 'Dunlosky et al., 2013, Psychological Science in the Public Interest（高实用性技术）'],
  ['睡眠巩固', '睡前复习重点，睡眠中完成记忆巩固', 'Rasch & Born, 2013, Physiological Reviews (IF 37.3)'],
  ['避免低效技巧', '划线、重读、摘要属于低实用性技术，谨慎使用', 'Dunlosky et al., 2013（对比 10 种学习技术的元分析）']
];

// ==================== 任务解析与调度 ====================

/**
 * 规范化单个任务（校验字段并补默认值）
 */
function normalizeTask(raw, i) {
  if (!raw.name) throw new Error(`任务${i + 1}缺少 name`);
  const units = Number(raw.units);
  if (!(units > 0)) throw new Error(`任务「${raw.name}」的 units 必须是正数`);
  if (!UNIT_HOURS[raw.unit_type]) throw new Error(`任务「${raw.name}」的单位「${raw.unit_type}」无效，可选：${Object.keys(UNIT_HOURS).join('/')}`);
  if (!MASTERY[raw.mastery]) throw new Error(`任务「${raw.name}」的掌握度「${raw.mastery}」无效，可选：${Object.keys(MASTERY).join('/')}`);
  const known = raw.known !== undefined ? Math.max(0, Math.min(1, Number(raw.known))) : 0;
  const examDays = raw.exam_days !== undefined ? Math.max(1, Math.round(Number(raw.exam_days))) : null;
  return {
    id: i + 1,
    name: String(raw.name),
    units,
    unit_type: raw.unit_type,
    mastery: raw.mastery,
    s: MASTERY[raw.mastery].s,
    mult: MASTERY[raw.mastery].mult,
    learn_hours: Math.round(units * UNIT_HOURS[raw.unit_type] * MASTERY[raw.mastery].mult * 10) / 10,
    known,
    exam_days: examDays,
    review_hours: 0,
    learn_day: null,
    review_days: []
  };
}

/**
 * 解析任务列表 JSON
 * 字段：name 名称, units 内容量, unit_type 单位(章/节/页/词/套题/讲),
 *       mastery 掌握度(了解/熟悉/掌握/精通), exam_days 距考试天数(可选), known 初始熟悉度0-1(可选)
 */
function parseTasks(json) {
  const arr = JSON.parse(json);
  if (!Array.isArray(arr) || arr.length === 0) throw new Error('任务列表必须是非空数组');
  return arr.map((t, i) => normalizeTask(t, i));
}

/**
 * 学习排程：按考试临近度与内容量排序，任务可跨天拆分填充每日新学容量
 * 返回 { assignments: [{day, task, hours}], overloaded: [task] }
 */
function scheduleLearning(tasks, days, capPerDay) {
  const order = [...tasks].sort((a, b) => {
    const da = a.exam_days || days;
    const db = b.exam_days || days;
    if (da !== db) return da - db;
    return b.learn_hours - a.learn_hours;
  });
  const remaining = Array.from({ length: days + 1 }, () => capPerDay); // 下标1..days
  const assignments = [];
  const overloaded = [];
  for (const t of order) {
    let need = t.learn_hours;
    const startIdx = assignments.length;
    let day = 1;
    let firstDay = null;
    while (need > 0.01 && day <= days) {
      if (remaining[day] > 0.01) {
        const take = Math.min(need, remaining[day]);
        remaining[day] = Math.round((remaining[day] - take) * 100) / 100;
        need = Math.round((need - take) * 100) / 100;
        assignments.push({ day, task: t, hours: Math.round(take * 10) / 10 });
        if (firstDay === null) firstDay = day;
      }
      day++;
    }
    if (need > 0.01) {
      // 放不下：回滚该任务的已排部分，标记超载
      assignments.splice(startIdx);
      overloaded.push(t);
    } else {
      t.learn_day = firstDay;
    }
  }
  return { assignments, overloaded };
}

/** 复习排程：任务学习日后按扩张间隔安排复习，不晚于考试日 */
function scheduleReviews(tasks, days) {
  for (const t of tasks) {
    if (!t.learn_day) continue;
    const cap = t.exam_days || days;
    // 复习≈30%学习时长，但单次不超过1.5h（避免单次复习过长破坏间隔分布）
    const reviewHours = Math.min(1.5, Math.round(t.learn_hours * 0.3 * 10) / 10);
    t.review_hours = reviewHours;
    let acc = t.learn_day;
    for (const iv of INTERVALS) {
      const day = t.learn_day + iv;
      if (day > cap) break;
      t.review_days.push(day);
    }
    // 考前3天集中回顾（若考试日>3天且未覆盖）
    if (cap > 3 && !t.review_days.includes(cap - 3)) t.review_days.push(cap - 3);
    t.review_days.sort((a, b) => a - b);
  }
}

/** 每日负载平衡：复习任务若使当日总时长超限，顺延到后续有容量的日子 */
function balanceDailyLoad(assignments, tasks, days, hours) {
  const learnLoad = new Map();
  for (const a of assignments) learnLoad.set(a.day, (learnLoad.get(a.day) || 0) + a.hours);
  const reviewItems = [];
  for (const t of tasks) {
    for (const rd of (t.review_days || [])) reviewItems.push({ task: t, day: rd });
  }
  reviewItems.sort((a, b) => a.day - b.day);
  tasks.forEach((t) => { t.review_days = []; });
  const remaining = Array.from({ length: days + 2 }, (_, d) => {
    if (d === 0) return 0;
    return Math.max(0, hours - (learnLoad.get(d) || 0));
  });
  let dropped = 0;
  for (const item of reviewItems) {
    let d = item.day;
    const cap = item.task.exam_days || days;
    while (d <= cap && remaining[d] < item.task.review_hours) d++;
    if (d <= cap) {
      remaining[d] -= item.task.review_hours;
      item.task.review_days.push(d);
    } else {
      dropped++; // 放不下则跳过该次复习
    }
  }
  tasks.forEach((t) => t.review_days.sort((a, b) => a - b));
  return dropped;
}

// ==================== 可视化（ASCII） ====================

/** ① 记忆保留率预测（以"掌握"级材料为例，S=7天） */
function renderForgettingChart() {
  const S = 7;
  const pts = [
    ['第1天', 1, retention(1, S)],
    ['第3天', 3, retention(3, S)],
    ['第7天', 7, retention(7, S)],
    ['第15天', 15, retention(15, S)],
    ['第31天', 31, retention(31, S)]
  ];
  const width = 12;
  const lines = [
    '#### ① 记忆保留率预测（以"掌握"级材料为例，S=7天）',
    '无复习按遗忘曲线 R(t)=e^(-t/7) 衰减；间隔复习在保留率≈87%时及时复习（1-3-7-15-31天）'
  ];
  for (const [label, day, noRev] of pts) {
    const bNo = Math.max(0, Math.min(width, Math.round((noRev / 100) * width)));
    const bYes = Math.max(0, Math.min(width, Math.round((86.7 / 100) * width)));
    const dayTag = `第${String(day).padStart(2, ' ')}天`;
    lines.push(`${dayTag}  无复习 [${BLOCK.repeat(bNo)}${SHADE.repeat(width - bNo)}] ${pyRound(noRev, 0)}%  间隔复习 [${BLOCK.repeat(bYes)}${SHADE.repeat(width - bYes)}] ~87%`);
  }
  lines.push('');
  return lines.join('\n');
}

/** ② 复习调度甘特图（每任务一行） */
function renderReviewGantt(tasks, days) {
  const width = Math.min(days, 40);
  const lines = ['#### ② 复习调度计划（学=新学，复=复习，·=无安排）'];
  for (const t of tasks) {
    if (!t.learn_day) continue;
    const cells = [];
    for (let d = 1; d <= width; d++) {
      if (d === t.learn_day) cells.push('学');
      else if (t.review_days.includes(d)) cells.push('复');
      else cells.push(DOT);
    }
    let axis = '';
    for (let d = 1; d <= width; d++) {
      if (d % 10 === 0) axis += '0';
      else if (d % 10 === 5) axis += '5';
      else axis += ' ';
    }
    const revStr = t.review_days.length ? `复习日: ${t.review_days.join(',')}` : '（考试日临近，仅新学）';
    lines.push(`${t.name.padEnd(6)}[${cells.join('')}]  ${revStr}`);
    lines.push(`      ${axis}`);
  }
  lines.push('（日轴为第1天起的备考进度；"5/10..."为天数十位/个位标记）');
  lines.push('');
  return lines.join('\n');
}

/** ③ 每日学习计划（前14天） */
function renderDailyPlan(assignments, tasks, days, hours) {
  const learnByDay = new Map();
  const reviewByDay = new Map();
  for (const a of assignments) {
    if (!learnByDay.has(a.day)) learnByDay.set(a.day, []);
    learnByDay.get(a.day).push(a);
  }
  for (const t of tasks) {
    for (const rd of t.review_days) {
      if (!reviewByDay.has(rd)) reviewByDay.set(rd, []);
      reviewByDay.get(rd).push(t);
    }
  }
  const showDays = Math.min(days, 14);
  const lines = ['#### ③ 每日学习计划（前' + showDays + '天，每日可用 ' + pyFloatStr(hours) + 'h）'];
  for (let d = 1; d <= showDays; d++) {
    const learn = learnByDay.get(d) || [];
    const review = reviewByDay.get(d) || [];
    const learnStr = learn.map((a) => `${a.task.name} ${pyFloatStr(a.hours)}h`).join('、') || '——';
    const reviewStr = review.map((t) => `${t.name} ${pyFloatStr(t.review_hours)}h`).join('、') || '——';
    const total = Math.round((learn.reduce((s, a) => s + a.hours, 0) + review.reduce((s, t) => s + t.review_hours, 0)) * 10) / 10;
    const warn = total > hours ? ' ⚠️超时' : '';
    lines.push(`第${d}天 [学] ${learnStr} | [复] ${reviewStr} | 合计 ${pyFloatStr(total)}h${warn}`);
  }
  if (days > 14) lines.push(`（第${showDays + 1}-${days}天的复习安排见上方甘特图）`);
  lines.push('');
  return lines.join('\n');
}

/** ④ 备考阶段分析 */
function renderStageAnalysis(config) {
  if (!config) return '';
  return `## 备考阶段分析：${config.name}

### 阶段特征
${config.description}

### 当前挑战
${config.challenges.map((c) => '- ' + c).join('\n')}

### 推荐投入
- **每日学习时长**: ${config.daily_hours[0]}-${config.daily_hours[1]} 小时
- **复习占比**: ${Math.round(config.review_ratio * 100)}%（每日时间中用于对抗遗忘的复习比例）
- **阶段策略**: ${config.special}

### 阶段特定建议
${config.recommendations.map((r) => '- ' + r).join('\n')}
`;
}

/** ⑤ 高效学习策略清单 */
function renderStrategies() {
  const lines = ['## 高效学习策略清单（附科学依据）'];
  for (const [name, desc, cite] of STRATEGIES) {
    lines.push(`- **${name}**：${desc}（${cite}）`);
  }
  lines.push('');
  return lines.join('\n');
}

/** ⑥ 睡眠联动提示 */
function renderSleepTips() {
  return `## 记忆巩固与睡眠联动（呼应 sleep-optimizer 技能）

- **睡前1小时复习重点**：睡眠中的慢波睡眠与纺锤波参与记忆巩固（Rasch & Born, 2013）
- **保证 ≥6-7 小时睡眠**：连续熬夜会显著削弱次日记忆提取
- **早起后30分钟回顾**：睡眠后"离线重放"效应最活跃，晨间快速回顾性价比最高
- **午睡 ≤20 分钟**：午间小睡提升下午学习效率，但过长会带来睡眠惯性
- 睡眠安排可直接使用同系列的 sleep-optimizer 技能生成

`;
}

// ==================== SVG 图表 ====================

function renderSvgChart(tasks, days, hours, config, assignments) {
  const W = 760;
  const H = 680;
  const pad = 45;
  const stageName = config ? config.name : '通用';
  const S = MASTERY['掌握'].s; // 曲线示例用"掌握"级
  const plotDays = Math.max(10, Math.min(days, 45));
  const plotW = W - 2 * pad;
  const plotH = 220;
  const xOf = (d) => pad + (d / plotDays) * plotW;
  const yOf = (pct) => pad + 30 + (1 - pct / 100) * plotH;

  // 无复习曲线
  const noCurve = [];
  for (let d = 0; d <= plotDays; d++) noCurve.push(`${xOf(d).toFixed(1)},${yOf(retention(d, S)).toFixed(1)}`);
  // 间隔复习曲线（阶梯）
  const yesPts = [{ d: 0, v: 100 }];
  let acc = 0, sCur = S;
  for (const iv of INTERVALS) {
    acc += iv;
    if (acc > plotDays) break;
    yesPts.push({ d: acc, v: retention(iv, sCur) });
    yesPts.push({ d: acc, v: 100 });
    sCur *= 2;
  }
  if (yesPts[yesPts.length - 1].d < plotDays) {
    const last = yesPts[yesPts.length - 1];
    const endV = retention(plotDays - last.d, sCur);
    yesPts.push({ d: plotDays, v: endV });
  }
  const yesCurve = yesPts.map((p) => `${xOf(p.d).toFixed(1)},${yOf(p.v).toFixed(1)}`).join(' ');

  // 复习甘特（SVG）
  const ganttY = 320;
  const ganttH = tasks.length * 26;
  const ganttW = W - 2 * pad;
  const ganttTasks = tasks.filter((t) => t.learn_day);
  const ganttRows = ganttTasks
    .map((t, i) => {
      const y = ganttY + i * 26;
      const marks = t.review_days
        .filter((d) => d <= plotDays)
        .map((d) => `<rect x="${(xOf(d) - 2).toFixed(1)}" y="${y}" width="4" height="14" rx="1" fill="#4a90d9"/>`)
        .join('');
      const learnX = t.learn_day ? xOf(t.learn_day) : pad;
      return `<text x="${pad}" y="${y + 11}" font-size="11" fill="#333">${esc(t.name)}</text>
  <rect x="${pad + 90}" y="${y}" width="${ganttW - 90}" height="14" rx="2" fill="#f0f0f0"/>
  <rect x="${learnX.toFixed(1)}" y="${y}" width="4" height="14" rx="1" fill="#e05656"/>${marks}`;
    })
    .join('\n  ');

  // 每日时长（前7天）
  const learnByDay = new Map();
  const reviewByDay = new Map();
  for (const a of assignments) {
    learnByDay.set(a.day, (learnByDay.get(a.day) || 0) + a.hours);
  }
  for (const t of tasks) {
    for (const rd of t.review_days) reviewByDay.set(rd, (reviewByDay.get(rd) || 0) + t.review_hours);
  }
  const barY = 560;
  const barW = (plotW - 6 * 8) / 7;
  const maxTotal = Math.max(hours, ...Array.from({ length: 7 }, (_, i) => (learnByDay.get(i + 1) || 0) + (reviewByDay.get(i + 1) || 0)), 1);
  let dayBars = '';
  for (let i = 0; i < 7; i++) {
    const d = i + 1;
    const lh = learnByDay.get(d) || 0;
    const rh = reviewByDay.get(d) || 0;
    const x = pad + i * (barW + 8);
    const lhH = (lh / maxTotal) * 70;
    const rhH = (rh / maxTotal) * 70;
    dayBars += `<rect x="${x.toFixed(1)}" y="${(barY + 70 - lhH).toFixed(1)}" width="${barW.toFixed(1)}" height="${lhH.toFixed(1)}" fill="#4a90d9"/>
  <rect x="${x.toFixed(1)}" y="${(barY + 70 - lhH - rhH).toFixed(1)}" width="${barW.toFixed(1)}" height="${rhH.toFixed(1)}" fill="#f0a030"/>
  <text x="${(x + barW / 2).toFixed(1)}" y="${barY + 88}" font-size="10" fill="#666" text-anchor="middle">D${d}</text>`;
  }

  const totalLearn = tasks.reduce((s, t) => s + t.learn_hours, 0);
  const totalReview = tasks.reduce((s, t) => s + t.review_hours, 0);

  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="${W}" height="${H}" fill="#ffffff"/>
  <text x="${pad}" y="30" font-size="18" font-weight="bold" fill="#222">个性化记忆优化报告 · 可视化图表</text>
  <text x="${pad}" y="52" font-size="13" fill="#666">备考阶段：${esc(stageName)}　|　备考周期 ${days} 天　|　每日可用 ${pyFloatStr(hours)}h　|　任务 ${tasks.length} 项（总学习 ${pyFloatStr(totalLearn)}h）</text>

  <!-- ① 遗忘曲线 -->
  <text x="${pad}" y="90" font-size="14" font-weight="bold" fill="#333">① 遗忘曲线与间隔复习效果（"掌握"级材料，S=7天）</text>
  <line x1="${pad}" y1="${yOf(0)}" x2="${pad + plotW}" y2="${yOf(0)}" stroke="#ccc"/>
  <line x1="${pad}" y1="${yOf(100)}" x2="${pad}" y2="${yOf(0)}" stroke="#ccc"/>
  ${[0, 25, 50, 75, 100].map((p) => `<text x="${pad - 6}" y="${yOf(p) + 4}" font-size="10" fill="#888" text-anchor="end">${p}%</text>`).join('\n  ')}
  <polyline points="${noCurve.join(' ')}" fill="none" stroke="#e05656" stroke-width="2" stroke-dasharray="6,4"/>
  <polyline points="${yesCurve}" fill="none" stroke="#3ba55d" stroke-width="2.5"/>
  <text x="${pad + 20}" y="${yOf(retention(Math.max(5, Math.floor(plotDays * 0.5)), S))}" font-size="11" fill="#e05656">无复习（遗忘曲线）</text>
  <text x="${pad + plotW - 130}" y="${yOf(96)}" font-size="11" fill="#3ba55d">间隔复习（1-3-7-15-31天）</text>
  ${Array.from({ length: 6 }, (_, i) => i * 2).map((d) => `<text x="${xOf(d).toFixed(1)}" y="${yOf(0) + 16}" font-size="10" fill="#888" text-anchor="middle">${d}</text>`).join('\n  ')}
  <text x="${pad + plotW / 2}" y="${yOf(0) + 32}" font-size="10" fill="#888" text-anchor="middle">天数</text>

  <!-- ② 复习甘特 -->
  <text x="${pad}" y="${ganttY - 12}" font-size="14" font-weight="bold" fill="#333">② 复习调度甘特图（红=新学，蓝=复习）</text>
  ${ganttRows}

  <!-- ③ 每日时长 -->
  <text x="${pad}" y="${barY - 14}" font-size="14" font-weight="bold" fill="#333">③ 前7天每日学习时长分配（蓝=新学，橙=复习）</text>
  ${dayBars}
  <text x="${pad + 60}" y="${barY + 110}" font-size="11" fill="#555">虚线=无复习时记忆衰减；实线=按扩张间隔复习后保留率回升</text>
  <text x="${pad}" y="${H - 16}" font-size="11" fill="#999">科学依据：Ebbinghaus 1885；Cepeda et al. 2006/2008；Roediger &amp; Karpicke 2006；Karpicke &amp; Blunt 2011 (Science)；Dunlosky et al. 2013；Rasch &amp; Born 2013。本图表仅供参考，不能替代专业指导。</text>
</svg>
`;
}

// ==================== 报告生成 ====================

function generateReport(opts) {
  const { tasks, days, hours, stage, config } = opts;

  // 调度
  const capPerDay = Math.max(1, hours * 0.55); // 55%时间用于新学，其余给复习与休息
  const { assignments, overloaded } = scheduleLearning(tasks, days, capPerDay);
  scheduleReviews(tasks, days);
  const droppedReviews = balanceDailyLoad(assignments, tasks, days, hours);

  // 指标
  const totalLearn = tasks.reduce((s, t) => s + t.learn_hours, 0);
  const scheduledLearn = assignments.reduce((s, a) => s + a.hours, 0);
  const totalReview = tasks.reduce((s, t) => s + t.review_hours * t.review_days.length, 0);
  const totalCapacity = days * capPerDay;

  const riskLines = [];
  if (scheduledLearn < totalLearn - 0.01) {
    riskLines.push(`[!] 计划过载：总学习量 ${pyFloatStr(totalLearn)}h 超过 ${days} 天容量 ${pyFloatStr(totalCapacity)}h，${overloaded.map((t) => `「${t.name}」`).join('')}未能排入，建议压缩内容/提高每日时长/延长备考期`);
  }
  if (config && hours < config.daily_hours[0]) {
    riskLines.push(`[!] 每日 ${pyFloatStr(hours)}h 低于「${config.name}」推荐下限 ${config.daily_hours[0]}h，注意保证睡眠与休息`);
  }
  if (riskLines.length === 0) riskLines.push('[OK] 计划在容量范围内，可执行');
  if (droppedReviews > 0) {
    riskLines.push(`[!] 有 ${droppedReviews} 次复习因容量不足被顺延后仍无法安放，建议适当增加每日时长`);
  }

  // 每任务复习点说明
  const taskLines = tasks.map((t) => {
    if (!t.learn_day) return `- ${t.name}：未排入计划（超载或时间不足）`;
    const rev = t.review_days.length ? `，复习日：${t.review_days.join('、')}` : '（考前时间不足，建议至少安排1次复习）';
    return `- **${t.name}**（${t.mastery}级，${pyFloatStr(t.learn_hours)}h）：第${t.learn_day}天起新学${rev}`;
  });

  const report = `
# 个性化记忆优化报告

## 一、学习概况评估

- **备考阶段**：${config ? config.name : '通用'}
- **备考周期**：${days} 天　|　**每日可用**：${pyFloatStr(hours)} 小时
- **任务**：${tasks.length} 项　|　**总学习量**：${pyFloatStr(totalLearn)} 小时　|　**预计总复习量**：约 ${pyFloatStr(totalReview)} 小时
- **风险评估**：
${riskLines.map((r) => '  ' + r).join('\n')}

### 记忆可视化

${renderForgettingChart()}
${renderReviewGantt(tasks, days)}

## 二、任务排程明细

${taskLines.join('\n')}

${config ? renderStageAnalysis(config) : ''}
${renderDailyPlan(assignments, tasks, days, hours)}
${renderStrategies()}
${renderSleepTips()}
## 注意事项

- 本计划基于遗忘曲线（Ebbinghaus 1885）与间隔效应（Cepeda et al. 2006）的简化模型，实际间隔可按个人遗忘速度微调
- 复习时请使用**主动回忆**（合书自测），而非重读——检索练习的记忆效果显著优于重复阅读（Karpicke & Blunt, 2011, Science）
- 记忆效果高度依赖睡眠质量与时长，连续熬夜会抵消复习收益；睡眠安排建议配合 sleep-optimizer 技能
- 本工具为学习策略参考，不能替代教师指导与个人学习节奏

---
*科学依据：Ebbinghaus (1885) 遗忘曲线；Roediger & Karpicke (2006, Psychological Science) 测试效应；Cepeda et al. (2006, Psychological Bulletin；2008, PNAS) 间隔效应；Karpicke & Blunt (2011, Science) 检索练习；Dunlosky et al. (2013, Psychological Science in the Public Interest) 学习技术评估；Rasch & Born (2013, Physiological Reviews) 睡眠记忆巩固；Bjork (1994) 期望困难*
`;
  return { report, assignments, tasks };
}

// ==================== 命令行入口 ====================

function printError(msg) {
  console.error(`错误: ${msg}`);
}

function main() {
  const ALLOWED_KEYS = ['stage', 'days', 'hours', 'tasks', 'output'];
  const args = process.argv.slice(2);
  const opts = {};
  for (let i = 0; i < args.length; i++) {
    const a = args[i];
    if (a.startsWith('--')) {
      let key = a.slice(2);
      let value;
      const eq = key.indexOf('=');
      if (eq !== -1) { value = key.slice(eq + 1); key = key.slice(0, eq); }
      else {
        value = args[++i];
        if (value === undefined) { printError(`参数 --${key} 缺少值`); process.exit(1); }
      }
      if (!ALLOWED_KEYS.includes(key)) { printError(`未知参数: --${key}`); process.exit(1); }
      opts[key] = value;
    } else {
      printError(`未知参数: ${a}`);
      process.exit(1);
    }
  }

  if (!opts.stage || !opts.days || !opts.hours) {
    printError('--stage、--days、--hours 为必填参数');
    process.exit(1);
  }
  if (!STAGE_CONFIGS[opts.stage]) {
    printError(`未知备考阶段: ${opts.stage}。可选: ${Object.keys(STAGE_CONFIGS).join(', ')}`);
    process.exit(1);
  }
  const days = parseInt(opts.days, 10);
  const hours = parseFloat(opts.hours);
  if (!(days > 0 && days <= 365)) { printError('--days 需为 1-365 之间的整数'); process.exit(1); }
  if (!(hours > 0 && hours <= 16)) { printError('--hours 需为 0-16 之间的小时数'); process.exit(1); }

  let tasksJson = null;
  if (opts.tasks) {
    let raw = opts.tasks;
    if (raw.startsWith('@')) {
      try { raw = require('fs').readFileSync(raw.slice(1), 'utf8'); }
      catch (e) { printError(`无法读取任务文件: ${e.message}`); process.exit(1); }
    }
    tasksJson = raw;
  }

  let tasks;
  try {
    tasks = tasksJson ? parseTasks(tasksJson) : [
      { name: '普通心理学', units: 6, unit_type: '章', mastery: '掌握', known: 0.2, exam_days: null },
      { name: '实验心理学', units: 4, unit_type: '章', mastery: '熟悉', known: 0.3, exam_days: null },
      { name: '认知心理学', units: 5, unit_type: '章', mastery: '掌握', known: 0.1, exam_days: null }
    ].map((t, i) => normalizeTask(t, i));
  } catch (e) {
    printError(e.message);
    process.exit(1);
  }

  const { report, assignments } = generateReport({ tasks, days, hours, stage: opts.stage, config: STAGE_CONFIGS[opts.stage] });
  process.stdout.write(report + '\n');
  if (opts.output) {
    const fs = require('fs');
    fs.writeFileSync(opts.output, report, 'utf8');
    const svg = renderSvgChart(tasks, days, hours, STAGE_CONFIGS[opts.stage], assignments);
    fs.writeFileSync(opts.output.replace(/\.md$/i, '') + '.chart.svg', svg, 'utf8');
  }
}

main();
