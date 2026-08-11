// generation-checks.js — 生成侧回归(2026-08-06 第五轮 P3)
//
// 为什么需要它:此前 6 个测试全部覆盖**转换管线**与页面静态属性,
// 没有任何测试覆盖"访谈 → brief → 写页"这条主链路。后果是"规范写了但没被执行"
// 这一整类缺陷可以存活数轮而无人发现,实证两例:
//   ① `--text-*` 字号令牌在整个语料里**零引用** —— 字号阶只存在于文档;
//   ② 演讲档正文中位数长期钉在 22px(= 破档红线),红线被当成默认值。
// 两例都是靠临时探针偶然测出来的,不是常设机制。本测试把这类断言固化。
//
// 断言分三组:
//   A. 资产自洽 —— 模板/片段/预设本身符合设计契约(字号角色、令牌定义完整性)
//   B. 契约传导 —— brief 模板与 slides.config 模板的键能被实际加载链接受
//   C. 端到端  —— 用配置档跑一遍 validate,确认门禁对"新写的页"真的生效
//
// 用法: node test/generation-checks.js
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const SCRIPTS = path.resolve(__dirname, "..");
const ROOT = path.resolve(SCRIPTS, "..");
const CFG = require(path.join(SCRIPTS, "config", "default.config.js"));
const { resolveConfig } = require(path.join(SCRIPTS, "config", "merge.js"));
const TH = CFG.design.thresholds;

const read = (p) => fs.readFileSync(p, "utf-8");
const fails = [];
const ok = [];
const check = (cond, pass, fail) => (cond ? ok.push(pass) : fails.push(fail));

// ══ A. 资产自洽 ═══════════════════════════════════════════════════

// A1. 主题与 16 套预设必须定义完整的字号令牌集(缺一个就会静默回退)
const TOKENS = ["--text-cover", "--text-title-page", "--text-title-block", "--text-body", "--text-note", "--text-floor"];
const themeFiles = [path.join(ROOT, "assets", "theme.css"), ...fs.readdirSync(path.join(ROOT, "assets", "presets")).map((f) => path.join(ROOT, "assets", "presets", f))];
for (const f of themeFiles) {
  const src = read(f);
  const miss = TOKENS.filter((t) => !src.includes(t + ":"));
  if (miss.length) fails.push(`[A1 令牌缺失] ${path.relative(ROOT, f)} 缺 ${miss.join(", ")}`);
}
ok.push(`A1 字号令牌完整性:${themeFiles.length} 个主题文件 × ${TOKENS.length} 令牌`);

// A2. --text-body 必须落在演讲档正文区间内,且严格**高于**破档下限
//     (这是 H14 的教训:下限被当默认值 → 页面又小又平)
const themeSrc = read(path.join(ROOT, "assets", "theme.css"));
const bodyPx = parseInt((/--text-body:\s*(\d+)px/.exec(themeSrc) || [])[1], 10);
check(
  bodyPx > TH.tierBodyMin.presentation,
  `A2 --text-body = ${bodyPx}px,严格高于演讲档破档下限 ${TH.tierBodyMin.presentation}px`,
  `[A2 字号阶] --text-body = ${bodyPx}px,未高于破档下限 ${TH.tierBodyMin.presentation}px —— 下限不是默认值`
);

// A3. 片段/模板里不得出现**正文角色**的破档字号
//     口径:font-size < 档内下限 且颜色为 primary/secondary(正文色)= 破档正文;
//     tertiary/dim/accent 是注释与标签角色,只受绝对下限约束。
const assetHtml = [
  ...fs.readdirSync(path.join(ROOT, "assets")).filter((f) => f.endsWith(".html")).map((f) => path.join(ROOT, "assets", f)),
  ...fs.readdirSync(path.join(ROOT, "assets", "snippets")).filter((f) => f.endsWith(".html")).map((f) => path.join(ROOT, "assets", "snippets", f)),
];
const bodyMin = TH.tierBodyMin.presentation;
const floor = CFG.design.minBodyPx;
let a3bad = 0;
for (const f of assetHtml) {
  read(f).split("\n").forEach((line, i) => {
    const m = /font-size:(\d+)px/.exec(line);
    if (!m) return;
    const px = parseInt(m[1], 10);
    if (px < floor) {
      fails.push(`[A3 破绝对下限] ${path.relative(ROOT, f)}:${i + 1} font-size:${px}px < ${floor}px`);
      a3bad++;
      return;
    }
    const isBodyRole = /color:var\(--text-(primary|secondary)\)/.test(line);
    if (isBodyRole && px < bodyMin) {
      fails.push(`[A3 正文破档] ${path.relative(ROOT, f)}:${i + 1} 正文色文字 ${px}px < 演讲档下限 ${bodyMin}px`);
      a3bad++;
    }
  });
}
if (!a3bad) ok.push(`A3 片段/模板字号角色合规:${assetHtml.length} 个文件,无正文破档、无破绝对下限`);

// A4. 品牌层解耦(2026-08-06 P6):语义名必须是**持值**的正规名,
//     品牌名必须是**指向语义名的别名**。反了就会出现 `--lenovo-red: #0071E3 /* Apple Blue */`
//     这种名实不符 —— 16 套预设全都定义 --lenovo-red 曾是这个耦合的固化形式。
const ALIAS_PAIRS = [
  ["brand-primary", "lenovo-red"],
  ["brand-primary-dark", "lenovo-red-dark"],
  ["brand-dark", "deep-navy"],
  ["brand-dark-soft", "deep-navy-light"],
];
let a4bad = 0;
for (const f of themeFiles) {
  const src = read(f);
  const rel = path.relative(ROOT, f);
  for (const [sem, brand] of ALIAS_PAIRS) {
    const semDef = new RegExp(`--${sem}:\\s*(#[0-9A-Fa-f]{3,8}|rgb)`).test(src);
    const aliasDef = new RegExp(`--${brand}:\\s*var\\(--${sem}\\)`).test(src);
    if (!semDef) { fails.push(`[A4 品牌解耦] ${rel}: --${sem} 未持有具体色值(语义名应是正规名)`); a4bad++; }
    if (!aliasDef) { fails.push(`[A4 品牌解耦] ${rel}: --${brand} 不是 var(--${sem}) 别名(品牌名应降级为别名)`); a4bad++; }
  }
}
if (!a4bad) ok.push(`A4 品牌层解耦:${themeFiles.length} 个主题 × ${ALIAS_PAIRS.length} 对(语义名持值、品牌名为别名)`);

// ══ B. 契约传导 ═══════════════════════════════════════════════════

// B1. slides.config 模板必须能被真实加载链(merge 白名单)接受
const tplPath = path.join(ROOT, "assets", "slides.config.template.json");
try {
  const tpl = JSON.parse(read(tplPath));
  const merged = resolveConfig(tpl);
  check(
    !!merged.design.tier && !!merged.design.formProfile,
    "B1 slides.config.template.json 可被 merge 接受,且 tier/formProfile 非空",
    "[B1] 模板合并后 tier/formProfile 为空 —— 实例化后门禁会休眠"
  );
} catch (e) {
  fails.push(`[B1] slides.config.template.json 无法被 merge 接受: ${e.message}`);
}

// B2. brief 模板里承诺的参数,必须都是 slides.config 支持的键(否则 brief 写了传不下去)
const briefSrc = read(path.join(ROOT, "assets", "deck-brief.template.md"));
for (const key of ["tier", "formProfile", "airyPages"]) {
  check(
    briefSrc.includes(key) || briefSrc.includes({ tier: "档", formProfile: "形式", airyPages: "airy" }[key]),
    `B2 brief 模板覆盖 ${key}`,
    `[B2] deck-brief.template.md 未提及 ${key} —— 访谈结论无法传导到 slides.config.json`
  );
}

// B3. 缺省档必须是"开启"状态(H14 决策:默认开启 + 老页豁免)
check(
  !!CFG.design.tier && !!CFG.design.formProfile,
  `B3 缺省设计档已开启(tier=${CFG.design.tier}, formProfile=${CFG.design.formProfile})`,
  "[B3] 缺省 design 档为空 —— 新 deck 的设计门禁会静默休眠(违反 H14 决策)"
);

// ══ C. 端到端:门禁对"新写的页"真的生效 ═══════════════════════════
// 构造两个页面跑真实 validate CLI(无项目级 config → 走缺省档):
//   good = 满填 + 有结构色面 + 层级分明 + 无黑话  → 应 0 ERROR 0 WARN
//   bad  = 版面达标但内容全是企业黑话              → 应命中黑话 WARN
const tmp = fs.mkdtempSync(path.join(require("os").tmpdir(), "gen-checks-"));
const slides = path.join(tmp, "slides");
fs.mkdirSync(slides);
fs.cpSync(path.join(SCRIPTS, "test", "fixtures", "assets"), path.join(tmp, "assets"), { recursive: true });

const page = (title, blocks) => `<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<link rel="stylesheet" href="../assets/theme.css"></head><body>
<div class="slide-container" style="background:var(--off-white);">
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:100px;top:120px;width:1720px;">
    <div style="font-size:60px;font-weight:700;line-height:1.2;color:var(--charcoal);">${title}</div>
  </div>
  <div data-object="true" data-object-type="shape" style="position:absolute;left:100px;top:320px;width:1720px;height:290px;background:var(--deep-navy);"></div>
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:140px;top:360px;width:1640px;">
    <div style="font-size:32px;font-weight:700;color:var(--on-navy-text);">${blocks[0]}</div>
    <div style="font-size:26px;line-height:1.7;color:var(--on-navy-sub);margin-top:24px;">${blocks[1]}</div>
  </div>
  <div data-object="true" data-object-type="shape" style="position:absolute;left:100px;top:640px;width:1720px;height:290px;background:#EEF2F7;"></div>
  <div data-object="true" data-object-type="textbox" style="position:absolute;left:140px;top:680px;width:1640px;">
    <div style="font-size:26px;line-height:1.7;color:var(--text-primary);">${blocks[2]}</div>
  </div>
</div></body></html>`;

fs.writeFileSync(path.join(slides, "good.html"), page("试点三个月:检索提速四成", [
  "检索耗时从 11 分钟降至 6.4 分钟",
  "过期文档占比由 34% 压到 9%;确认工单月均 16 起降至 2 起,降幅 88%。",
  "口径:3 个试点部门、214 人、2026-05 至 2026-07 工单系统日志。下一步扩到 8 个部门。",
]));
fs.writeFileSync(path.join(slides, "bad.html"), page("全面深化推进机制建设", [
  "赋能生态,构建闭环",
  "持续优化,全面提升,形成合力,打造标杆。",
  "统筹推进,夯实基础,精准发力,做大做强,保驾护航。",
]));

let out = "";
try {
  out = execFileSync(process.execPath, [path.join(SCRIPTS, "validate.js"), slides], { encoding: "utf-8" });
} catch (e) {
  out = (e.stdout || "") + (e.stderr || "");
}
const seg = (name) => {
  const i = out.indexOf(`=== ${name} ===`);
  if (i < 0) return "";
  const j = out.indexOf("=== ", i + 5);
  return out.slice(i, j < 0 ? undefined : j);
};
const goodSeg = seg("good.html"), badSeg = seg("bad.html");
check(/无违规/.test(goodSeg), "C1 扎实页通过缺省档门禁(0 ERROR/0 WARN)", `[C1] 扎实页被误判:\n${goodSeg.trim()}`);
check(/黑话密度过高/.test(badSeg), "C2 空话页被语义门禁拦下", `[C2] 空话页未被拦 —— 版面达标即可蒙过门禁:\n${badSeg.trim()}`);
check(/design profile: presentation/.test(out), "C3 无项目级 config 时走缺省档 presentation", "[C3] 缺省档未生效");
fs.rmSync(tmp, { recursive: true, force: true });

// ══ D. 访谈与深化层(2026-08-06 第六轮 P6)═══════════════════════════
// 为什么需要:第五轮建的四个门禁全测版面与代码,**访谈与深化层零覆盖**。
// 实测三类缺陷可以无限存活:①计数漂移(原型数在三份文档里是 20/28/30 三个值,
// 且"20 原型"让图示组 23-30 在引用方的自我描述里不存在);②推断规则散在 7 份文件
// 且词表互不一致(Q3b 的词表在 content-deepening 内部两处就不一致);
// ③快速通道与最少交互底线两条硬规则字面直接冲突,三处三说。
const IG = read(path.join(ROOT, "reference", "interview-guide.md"));
const CD = read(path.join(ROOT, "reference", "content-deepening.md"));

// D1. 计数一致性 —— 脚本实测,再断言各文档措辞与实测一致
const counts = {
  原型: (read(path.join(ROOT, "reference", "page-archetypes.md")).match(/^### 原型 \d+/gm) || []).length,
  片段: fs.readdirSync(path.join(ROOT, "assets", "snippets")).filter((f) => f.endsWith(".html")).length,
  图标: (read(path.join(ROOT, "assets", "icons.md")).match(/^\*\*i-[a-z-]+\*\*/gm) || []).length,
  预设: fs.readdirSync(path.join(ROOT, "assets", "presets")).filter((f) => f.endsWith(".css")).length,
  问数: new Set((IG.match(/^\| Q[0-9a-z]+/gm) || []).map((s) => s.replace(/^\|\s*/, ""))).size,
  阶段: (IG.match(/^## 阶段 \d/gm) || []).length,
};
// 各文档里出现"N 原型/N 个原型"时,N 必须等于实测值(允许措辞不同,不允许数字不同)
const countClaims = [
  ["reference/narrative-skeletons.md", /(\d+)\s*个?原型/g, counts.原型],
  ["reference/creative-layouts.md", /(\d+)\s*个?原型/g, counts.原型],
  ["reference/page-archetypes.md", /page-archetypes · (\d+) 个原型/g, counts.原型],
  ["assets/snippets/INDEX.md", /(\d+)\s*个原型/g, counts.原型],
  ["assets/icons.md", /(\d+)\s*枚内联 SVG/g, counts.图标],
];
for (const [rel, re, expect] of countClaims) {
  const src = read(path.join(ROOT, rel));
  for (const m of src.matchAll(re)) {
    // 跳过历史说明段里的旧值(带"此前"/"P1 归一"字样的同一行)
    const lineStart = src.lastIndexOf("\n", m.index) + 1;
    const line = src.slice(lineStart, src.indexOf("\n", m.index));
    if (/此前|归一|旧值|三处三个数/.test(line)) continue;
    check(
      Number(m[1]) === expect,
      `D1 ${rel} 原型/图标计数 ${m[1]} = 实测 ${expect}`,
      `[D1 计数漂移] ${rel} 写 "${m[0]}",实测应为 ${expect} —— 数字散在 8 份文档措辞里,改一处必须跑 D1`
    );
  }
}
// 问数与阶段数:interview-guide 的自我声明必须与实测一致
// (Q5 是确认环节,故声明格式为 "N 问 + 1 个大纲确认环节";实测 Q 编号含 Q5,所以减 1)
const qClaim = /(\d+)\s*问\s*\+\s*1 个大纲确认环节/.exec(IG);
check(
  qClaim && Number(qClaim[1]) === counts.问数 - 1,
  `D1 访谈问数声明 ${qClaim && qClaim[1]} = 实测 ${counts.问数} 个 Q 编号 - 1(Q5 为确认环节)`,
  `[D1] interview-guide 问数声明与实测不符(声明 ${qClaim && qClaim[1]},实测 Q 编号 ${counts.问数})`
);
const sClaim = /\*\*(\d+) 阶段/.exec(IG);
check(
  sClaim && Number(sClaim[1]) === counts.阶段,
  `D1 访谈阶段数声明 ${sClaim && sClaim[1]} = 实测 ${counts.阶段}`,
  `[D1] interview-guide 阶段声明与实测不符(声明 ${sClaim && sClaim[1]},实测 ${counts.阶段} 个 "## 阶段 N")`
);
const skillQ = /(\d+) 问 \+ 1 个大纲确认环节/.exec(read(path.join(ROOT, "SKILL.md")));
check(
  skillQ && Number(skillQ[1]) === counts.问数 - 1,
  `D1 SKILL.md 问数与 interview-guide 一致(${skillQ && skillQ[1]} 问)`,
  `[D1] SKILL.md 问数声明与实测不符 —— 此前 SKILL 写 16、interview-guide 写 17`
);

// D2. 推断总表:每格取值必须 ∈ 该轴合法枚举(防总表自己漂)
// 选行必须**结构化**(按区段 + 列数),不能按取值筛 ——
// 自证时发现:若用 /演讲|混合|阅读/ 筛行,把某格改成非法值会让该行从表里"消失"
// 而不是判失败,守卫反而静默放行(D2 自身的假阴性)。
const tableSection = IG.slice(IG.indexOf("| deck 族 |"), IG.indexOf("**多轴冲突的消解规则**"));
const tableRows = tableSection
  .split("\n")
  .filter((l) => l.startsWith("| ") && l.split("|").length === 11 && !/^\| deck 族|^\|---|^\| *\*\*无信号/.test(l));
check(tableRows.length >= 10, `D2 推断总表 ${tableRows.length} 个 deck 族`, `[D2] 推断总表行数异常(${tableRows.length}),疑似表被改坏`);
const AXES = {
  Q2: ["演讲", "混合", "阅读"],
  Q3b: ["深度打磨", "标准", "快速"],
  Q8c: ["丰富", "平衡", "克制"],
};
for (const row of tableRows) {
  const cells = row.split("|").map((c) => c.trim());
  const fam = cells[1];
  // 列序:| 族 | 关键词 | Q2 | Q3b | Q4 | Q6 | Q8c | Q7 | 角色 |
  const [q2, q3b, , , q8c] = [cells[3], cells[4], cells[5], cells[6], cells[7]];
  check(AXES.Q2.some((v) => q2.includes(v)), `D2 ${fam} Q2 取值合法`, `[D2] ${fam} 的 Q2 值 "${q2}" 不在 ${AXES.Q2.join("/")} 内`);
  check(AXES.Q3b.some((v) => q3b.includes(v)), `D2 ${fam} Q3b 取值合法`, `[D2] ${fam} 的 Q3b 值 "${q3b}" 不在 ${AXES.Q3b.join("/")} 内`);
  check(AXES.Q8c.some((v) => q8c.includes(v)), `D2 ${fam} Q8c 取值合法`, `[D2] ${fam} 的 Q8c 值 "${q8c}" 不在 ${AXES.Q8c.join("/")} 内`);
}
// 分册不得再重复定义词表(单一事实源)
for (const rel of ["reference/theme-presets.md", "reference/density-tiers.md", "reference/narrative-skeletons.md"]) {
  const src = read(path.join(ROOT, rel));
  check(
    /置首规则已上移|推断总表/.test(src),
    `D2 ${rel} 已指向推断总表`,
    `[D2] ${rel} 未指向推断总表 —— 置首规则回到了分册,又变成多事实源`
  );
  check(
    !/→\s*\*\*[^*]+\*\*置首/.test(src),
    `D2 ${rel} 无残留词表`,
    `[D2] ${rel} 仍有 "→ **X**置首" 形态的词表残留,与总表会分叉`
  );
}

// D3. 依赖图必须可解析且覆盖已知依赖
const depSection = IG.slice(IG.indexOf("**依赖图**"), IG.indexOf("**重入与版本**"));
const depRows = depSection.split("\n").filter((l) => l.startsWith("| ") && !/^\| 前置答案|^\|---/.test(l));
check(depRows.length >= 8, `D3 依赖图 ${depRows.length} 条`, `[D3] 依赖图仅 ${depRows.length} 条,疑似不完备`);
for (const known of ["品牌风", "裸主题", "快速", "不用骨架", "阅读档", "零装饰"]) {
  check(
    depRows.some((r) => r.includes(known)),
    `D3 依赖图覆盖「${known}」`,
    `[D3] 依赖图缺「${known}」分支 —— 该依赖此前散在问项括号里,漏登记就会被主循环凭感觉判断`
  );
}
// 快速通道与最少交互底线不得再冲突(三处口径归一)
check(
  /跳到最少交互底线/.test(IG) && !/立即跳过剩余全部问题/.test(IG),
  "D3 快速通道口径已归一(跳到底线,不是跳过底线)",
  "[D3] 快速通道仍写「跳过剩余全部问题」,与最少交互底线(保 Q6+Q5)字面冲突"
);
check(
  /仍走 Q6 \+ Q5|仍走 Q6 色板 \+ Q5/.test(CD),
  "D3 content-deepening 快速通道与 interview-guide 一致",
  "[D3] content-deepening 的快速通道口径未与 interview-guide 归一(此前它写「保 Q5 不保 Q6」)"
);

// D4. insights 模板 ↔ brief 摘要 ↔ hedgePages 三者字段对齐
const INS = read(path.join(ROOT, "assets", "deck-insights.template.md"));
for (const field of ["洞察清单", "假设清单", "限定词", "丢弃率", "被否方向", "大纲级形式门禁", "行动方案"]) {
  check(INS.includes(field), `D4 insights 模板含「${field}」`, `[D4] deck-insights.template.md 缺「${field}」区`);
}
check(
  briefSrc.includes("deck-insights.md") && briefSrc.includes("hedgePages"),
  "D4 brief 摘要指向 insights 详档且提及 hedgePages",
  "[D4] brief 未指向 deck-insights.md 或未提 hedgePages —— 深化产物又会坍缩回一行摘要"
);
check(
  Array.isArray(CFG.design.hedgePages) && Array.isArray(CFG.design.hedgeWords) && CFG.design.hedgeWords.length > 0,
  `D4 config 有 hedgePages/hedgeWords(${CFG.design.hedgeWords.length} 个限定词)`,
  "[D4] config 缺 hedgePages/hedgeWords —— 降级论断无法落地为机器约束"
);
check(
  read(path.join(ROOT, "scripts", "validate", "layout-checks.js")).includes("needsHedge"),
  "D4 layout-checks 承接 hedgePages 检查",
  "[D4] layout-checks 未实现限定词检查 —— hedgePages 写了没人查"
);
check(
  read(path.join(ROOT, "assets", "slides.config.template.json")).includes("hedgePages"),
  "D4 slides.config 模板含 hedgePages",
  "[D4] slides.config.template.json 缺 hedgePages"
);

// D5. 委员会角色映射必须覆盖推断总表的全部 deck 族
const roleRows = tableRows.filter((r) => {
  const cells = r.split("|").map((c) => c.trim());
  return cells[9] && cells[9].length > 3;
});
check(
  roleRows.length === tableRows.length,
  `D5 委员会动态角色覆盖全部 ${tableRows.length} 个 deck 族`,
  `[D5] ${tableRows.length - roleRows.length} 个 deck 族缺动态角色 —— 会退回通用五角色(与主题无关)`
);
check(
  /2 固定 \+ 3 动态|固定 2 席/.test(CD),
  "D5 委员会已改为 2 固定 + 3 动态",
  "[D5] content-deepening 第三章仍是固定五角色 —— 与第二章的动态角色机制两套哲学并存"
);
check(
  /推断总表/.test(CD),
  "D5 第二章角色表已指向推断总表",
  "[D5] content-deepening 第二章仍有自己的角色表 —— 与第三章不对齐"
);
// 成本披露必须锚定**披露句本身**,不能只查字符串出现过 ——
// 自证时发现:正文别处提到 "13-15" 就能让宽松断言通过(D5 自身的假阴性)。
const costLine = /执行成本[^\n]*\*\*(\d+-\d+) 次 agent 调用\*\*/.exec(CD);
const costQ3b = /深度打磨\([^)]*\*\*(\d+-\d+) 次代理调用\*\*/.exec(IG);
check(
  costLine && costLine[1] === "13-15",
  `D5 content-deepening 成本披露句 = ${costLine && costLine[1]} 次`,
  `[D5] 成本披露句写 ${costLine ? costLine[1] : "缺失"} —— 应为 13-15(3-5 角色 + 5 独立 + 最多 5 交叉);此前写"约 10 次"漏算交叉评审,用户据此选档`
);
check(
  costQ3b && costQ3b[1] === "13-15",
  `D5 Q3b 成本披露 = ${costQ3b && costQ3b[1]} 次(与 content-deepening 一致)`,
  `[D5] Q3b 的成本披露与 content-deepening 不一致(Q3b: ${costQ3b ? costQ3b[1] : "缺失"})`
);

// D6. 大纲级形式门禁的阈值不得在文档里硬编码(须与 formLimits 一致)
const FL = TH.formLimits;
const gateSection = CD.slice(CD.indexOf("大纲级形式门禁"));
check(
  gateSection.includes(String(FL.balanced.ratio * 100)) && gateSection.includes(String(FL.rich.ratio * 100)),
  `D6 大纲级形式门禁阈值与 config 一致(平衡 ${FL.balanced.ratio * 100}% / 丰富 ${FL.rich.ratio * 100}%)`,
  `[D6] 大纲级形式门禁的占比阈值与 design.thresholds.formLimits 不一致(config: ${FL.balanced.ratio * 100}/${FL.rich.ratio * 100})`
);
check(
  gateSection.includes(String(FL.balanced.streak)) && gateSection.includes(String(FL.rich.streak)),
  `D6 连排阈值与 config 一致(平衡 ${FL.balanced.streak} / 丰富 ${FL.rich.streak})`,
  `[D6] 连排阈值与 config 不一致(config: ${FL.balanced.streak}/${FL.rich.streak})`
);

// ══ E. 文字盒几何(2026-08-07 胶囊对齐修复)═══════════════════════════
// 为什么需要:胶囊标签(padding 撑开尺寸 + 无 text-align)在浏览器与 preview 截图里
// **完全正常**,只有 PPTX 里文字跑到左上角。两个独立成因:
//   ① isSingleLine 用 border box 高比行高 → padding+border 把 29px 盒撑过 21×1.3 阈值
//      → 判成多行 → valign:"top",纵向不居中;
//   ② 文字盒用 border box、PPTX 的 lIns=0 → 文字从 border box 左边起排,
//      而浏览器从 content box 起排 → 左偏「左 padding + 左边框」(实测 17px)。
// preview.js 走浏览器渲染,**结构上不可能发现这类缺陷** —— 只能在 XML 层断言。
const textJs = read(path.join(ROOT, "scripts", "extract", "primitives", "text.js"));
check(
  /symmetricV/.test(textJs) && /contentH\s*<=\s*oneLineH/.test(textJs),
  "E1 单行判定按内容高(扣对称 padding+border)",
  "[E1] isSingleLine 回到 border box 口径 —— 带 padding 的单行盒会被判多行,PPTX 里纵向不居中"
);
check(
  /Math\.abs\(padT - padB\)/.test(textJs),
  "E2 纵向内缩有对称性守卫",
  "[E2] 缺对称性守卫 —— 单边 padding(如 08.html 的 padding-top:25px)会被误判为单行并上移"
);
check(
  /insetH/.test(textJs) && /rect\.x \+ padL \+ bdL/.test(textJs),
  "E3 文字盒横向内缩到 content box",
  "[E3] 缺横向内缩 —— 文字从 border box 左边起排,PPTX 里整体左偏一个左 padding"
);
check(
  /rect = \{ x:/.test(textJs),
  "E4 内缩新建 rect 对象(不改共享引用)",
  "[E4] 直接改 rect —— 它与 shape 基元共用引用,会连带改坏已 push 的形状几何"
);
check(
  /centeredAndSymmetric/.test(textJs),
  "E5 居中+对称 padding 跳过内缩(避免无谓基线扰动)",
  "[E5] 缺跳过条件 —— 居中且对称 padding 时内缩视觉等价,只会制造基线 diff"
);

// ══ 汇报 ══════════════════════════════════════════════════════════
ok.forEach((l) => console.log("✅ " + l));
if (fails.length) {
  console.error(`\n❌ 生成侧回归失败 ${fails.length} 项:`);
  fails.forEach((f) => console.error("   " + f));
  process.exit(1);
}
console.log("\n✅ 生成侧回归全过(资产自洽 + 契约传导 + 端到端门禁)");
