#!/usr/bin/env node
'use strict';

const fs = require('node:fs');

const STAGES = new Set(['calibration', 'reading', 'deepening', 'closure']);
const INTENTS = new Set(['curiosity', 'comfort', 'decision', 'learning']);
const AGREEMENTS = new Set(['same', 'complementary', 'conflict', 'single']);
const LEVELS = new Set(['high', 'medium', 'low', 'none']);
const DELIVERIES = new Set(['direct', 'firm', 'probable', 'tentative']);
const ANSWER_NEEDS = new Set(['outcome', 'timing', 'turning-point', 'cause', 'decision', 'overview']);
const FOCUS_STATUSES = new Set(['calibrating', 'resolved']);
const CALIBRATION_TYPES = new Set(['past-event', 'current-status', 'timing', 'relationship-pattern', 'input-boundary']);
const BLACKBOX_TERMS = /八字|紫微|紫薇|命盘|星盘|排盘|四柱|天干|地支|十神|财星|官星|官杀|食伤|印星|比劫|日主|命主|月令|格局|旺衰|调候|五行|刑冲合害|星曜|主星|辅星|命宫|身宫|财帛宫|官禄宫|夫妻宫|福德宫|四化|化禄|化权|化科|化忌|大运|流年|流月|流日|证据|权重|置信度|算法|双系统|两套系统|两个系统|两张盘|两个盘|双盘|互证|交叉验证|模型|evidence/i;
const DANGEROUS_TERMS = /克死|必死|死期|寿命断定|绝症|必然离婚|一定离婚|保证发财|稳赚不赔|必定发财/;
const FABRICATED_SCENE_TERMS = /坐下说吧|请坐|坐吧|把手(?:伸过来|给我)|伸(?:出)?手(?:来|给我)|点(?:上|一)?炷香|喝口茶/;
const REPORT_TONE_TERMS = /综合来看|综上所述|总体而言|值得注意的是|基于以上(?:分析|判断)|从上述(?:分析|内容)|建议如下|以下几点/;
const PSEUDO_DEPTH_TERMS = /说到底|本质上|归根结底|真正的问题是|真正重要的是|问题的核心是|更深层次(?:地|的)?(?:看|说)/;
const ABUSIVE_RETORT_TERMS = /你(?:这个|真是)?(?:蠢货|白痴|废物|垃圾|傻子)|(?:给我)?滚(?:开|蛋)?|闭嘴|你算什么东西|没教养的东西/;
const INQUIRY_FORM_TERMS = /请提供|提供以下|以下信息|以下几项|出生日期[:：]|出生时间[:：]|问题类型[:：]|主要想看[:：]|YYYY-MM-DD|HH:MM|请选择|选项如下|为了更准确/;
const DIRECT_STATUS_QUESTIONS = /你(?:现在)?(?:是)?(?:未婚|已婚|离异)(?:还是|吗|呢)|你(?:结过婚|结婚)了吗|你有没有(?:结过婚|对象)/;
const CONFIRMATION_QUESTION = /对不对|对吗|是这样吗|是不是这样|我说得对吗|可有这回事|有没有说偏|准不准/;
const INPUT_AUDIT_QUESTION = /时辰|钟点|日期|阴历|阳历|农历|公历|出生地|准确|大概/;
const VAGUE_FOCUS = /^(?:我)?(?:想)?(?:问|看)?(?:一下)?(?:我的)?(?:婚姻|感情|姻缘|事业|工作|财运|财富|家庭|健康|运势|未来)(?:情况|方面|怎么样|如何|好不好)?[。？！?!]*$/;
const LIST_OR_HEADING = /(?:^|\n)\s*(?:#{1,6}\s|[-*+]\s|\d+[.、)]\s)/m;
const HEDGES = /大概率|多半|可能|也许|或许|似乎|倾向于|不排除|未必|说不准|仅供参考/;
const DIRECT_MARKERS = /可以定下来|可以直断|很明确|不用绕弯子|肯定|一定会|不会/;

function readText(path) {
  return fs.readFileSync(path, 'utf8').replace(/^\uFEFF/, '');
}

function readJson(path) {
  return JSON.parse(readText(path));
}

function parseArgs() {
  const args = {};
  for (const value of process.argv.slice(2)) {
    const match = value.match(/^--([^=]+)=(.*)$/);
    if (match) args[match[1]] = match[2];
  }
  return args;
}

function object(value, path) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) throw new Error(`${path} 必须是对象`);
}

function array(value, path, { min = 0, max = Infinity } = {}) {
  if (!Array.isArray(value) || value.length < min || value.length > max) {
    throw new Error(`${path} 必须是数组，数量范围 ${min}-${max === Infinity ? '不限' : max}`);
  }
}

function string(value, path, { allowEmpty = false } = {}) {
  if (typeof value !== 'string' || (!allowEmpty && !value.trim())) throw new Error(`${path} 必须是非空字符串`);
}

function publicStrings(plan) {
  const output = [];
  for (const [index, item] of (plan.calibration || []).entries()) {
    output.push([`calibration[${index}].statement`, item.statement]);
    output.push([`calibration[${index}].question`, item.question]);
  }
  for (const [index, item] of (plan.conclusions || []).entries()) {
    output.push([`conclusions[${index}].verdict`, item.verdict]);
    output.push([`conclusions[${index}].timing`, item.timing]);
    (item.conditions || []).forEach((value, i) => output.push([`conclusions[${index}].conditions[${i}]`, value]));
    (item.guidance || []).forEach((value, i) => output.push([`conclusions[${index}].guidance[${i}]`, value]));
  }
  output.push(['soulNote', plan.soulNote || '']);
  return output;
}

function validatePublicText(value, path) {
  string(value, path, { allowEmpty: true });
  if (BLACKBOX_TERMS.test(value)) throw new Error(`${path} 泄露后台推断术语: ${value}`);
  if (DANGEROUS_TERMS.test(value)) throw new Error(`${path} 包含恐吓或确定性伤害断语: ${value}`);
  if (FABRICATED_SCENE_TERMS.test(value)) throw new Error(`${path} 虚构了用户所处场景或动作: ${value}`);
  if (REPORT_TONE_TERMS.test(value)) throw new Error(`${path} 使用了报告腔: ${value}`);
  if (PSEUDO_DEPTH_TERMS.test(value)) throw new Error(`${path} 使用了权威式假深刻表达: ${value}`);
  if (ABUSIVE_RETORT_TERMS.test(value)) throw new Error(`${path} 用辱骂代替了有分寸的边界: ${value}`);
  if (DIRECT_STATUS_QUESTIONS.test(value)) throw new Error(`${path} 直接盘问了本应先由盘面判断的现实状态: ${value}`);
}

function validateDialogueShape(response, { inquiry = false } = {}) {
  const limit = inquiry ? 140 : 520;
  if (response.length > limit) throw new Error(`response 过长：${response.length} 字，当前轮次上限 ${limit} 字`);
  if (LIST_OR_HEADING.test(response)) throw new Error('response 不得使用标题、项目符号或编号列表');
  const questions = (response.match(/[？?]/g) || []).length;
  if (questions > 1) throw new Error('response 一轮只能问一个主问题');
  if (inquiry && questions !== 1) throw new Error('询问轮次必须包含且只包含一个问题');
  if (inquiry && INQUIRY_FORM_TERMS.test(response)) throw new Error('询问轮次使用了表单腔、格式说明或选项菜单');
  const parallelisms = (response.match(/不(?:只|仅|单单)?是[^。！？!?]{0,45}而是/g) || []).length;
  if (parallelisms > 1) throw new Error('response 反复使用“不是……而是……”对称金句');
  const sentences = response.split(/[。！？!?；;]/).map(value => value.trim()).filter(Boolean);
  let shortRun = 0;
  for (const sentence of sentences) {
    shortRun = sentence.length <= 8 ? shortRun + 1 : 0;
    if (shortRun >= 4) throw new Error('response 连续堆叠短句，戏剧感过于刻意');
  }
}

function validateInquiryResponse(response) {
  string(response, 'response');
  validatePublicText(response, 'response');
  validateDialogueShape(response, { inquiry: true });
  return { chars: response.length };
}

function validateEvidenceIds(ids, system, evidenceById, path, { allowEmpty = true } = {}) {
  array(ids, path, { min: allowEmpty ? 0 : 1 });
  for (const id of ids) {
    const evidence = evidenceById.get(id);
    if (!evidence) throw new Error(`${path} 引用了不存在的 ID: ${id}`);
    if (system && evidence.system !== system) throw new Error(`${path} 的 ${id} 不是 ${system} 证据`);
  }
}

function validateDeclaredLevel(level, ids, evidenceById, path) {
  if (!LEVELS.has(level)) throw new Error(`${path} 无效: ${level}`);
  if (level === 'none') {
    if (ids.length) throw new Error(`${path}=none 时不得附带证据`);
    return;
  }
  if (!ids.length) throw new Error(`${path}=${level} 时至少需要一个证据 ID`);
  const actual = ids.map(id => evidenceById.get(id)?.confidence).filter(Boolean);
  if (level === 'high' && !actual.includes('high')) throw new Error(`${path}=high 但没有 high 证据`);
  if (level === 'medium' && !actual.some(item => item === 'high' || item === 'medium')) {
    throw new Error(`${path}=medium 但证据强度不足`);
  }
}

function validateConclusion(item, index, evidenceById) {
  const path = `conclusions[${index}]`;
  object(item, path);
  for (const key of ['id', 'topic', 'verdict', 'timing', 'agreement', 'bazi_level', 'ziwei_level', 'delivery']) {
    string(item[key], `${path}.${key}`, { allowEmpty: key === 'timing' });
  }
  if (!AGREEMENTS.has(item.agreement)) throw new Error(`${path}.agreement 无效`);
  if (!DELIVERIES.has(item.delivery)) throw new Error(`${path}.delivery 无效`);
  array(item.conditions, `${path}.conditions`, { max: 3 });
  array(item.guidance, `${path}.guidance`, { max: 3 });
  validateEvidenceIds(item.bazi_evidence_ids, 'bazi', evidenceById, `${path}.bazi_evidence_ids`);
  validateEvidenceIds(item.ziwei_evidence_ids, 'ziwei', evidenceById, `${path}.ziwei_evidence_ids`);
  validateEvidenceIds(item.counter_evidence_ids || [], null, evidenceById, `${path}.counter_evidence_ids`);
  validateDeclaredLevel(item.bazi_level, item.bazi_evidence_ids, evidenceById, `${path}.bazi_level`);
  validateDeclaredLevel(item.ziwei_level, item.ziwei_evidence_ids, evidenceById, `${path}.ziwei_level`);

  const dualHighSame = item.agreement === 'same' && item.bazi_level === 'high' && item.ziwei_level === 'high';
  if (dualHighSame && item.delivery !== 'direct') {
    throw new Error(`${path} 属于双高同断，delivery 必须为 direct`);
  }
  if (item.delivery === 'direct' && !dualHighSame) {
    throw new Error(`${path} 只有双高同断才可使用 direct`);
  }
  if (item.delivery === 'direct') {
    if (HEDGES.test(item.verdict)) throw new Error(`${path}.verdict 直断中不得使用概率或退让词`);
    if (!DIRECT_MARKERS.test(item.verdict)) throw new Error(`${path}.verdict 缺少斩钉截铁的直断标记`);
  }
  if (item.agreement === 'single' && item.bazi_level !== 'none' && item.ziwei_level !== 'none') {
    throw new Error(`${path}.agreement=single 时只能有一个系统提供证据`);
  }
}

function validateFocus(focus, hasConclusions) {
  object(focus, 'focus');
  for (const key of ['status', 'domain', 'coreQuestion', 'answerNeed']) string(focus[key], `focus.${key}`);
  if (!FOCUS_STATUSES.has(focus.status)) throw new Error(`focus.status 无效: ${focus.status}`);
  if (!ANSWER_NEEDS.has(focus.answerNeed)) throw new Error(`focus.answerNeed 无效: ${focus.answerNeed}`);
  if (focus.status === 'resolved' && VAGUE_FOCUS.test(focus.coreQuestion.trim())) {
    throw new Error(`focus.coreQuestion 仍只是宽泛领域，必须先追问: ${focus.coreQuestion}`);
  }
  array(focus.knownContext, 'focus.knownContext', { min: focus.status === 'resolved' ? 1 : 0, max: 8 });
  array(focus.blockingUnknowns, 'focus.blockingUnknowns', { max: 5 });
  focus.knownContext.forEach((value, index) => string(value, `focus.knownContext[${index}]`));
  focus.blockingUnknowns.forEach((value, index) => string(value, `focus.blockingUnknowns[${index}]`));
  if (hasConclusions && focus.status !== 'resolved') throw new Error('有实质结论时 focus.status 必须为 resolved');
  if (hasConclusions && focus.blockingUnknowns.length) {
    throw new Error('给出实质结论前必须先问清 focus.blockingUnknowns');
  }
}

function validateCalibrationState(state) {
  object(state, 'calibrationState');
  if (!Number.isInteger(state.rejectionStreak) || state.rejectionStreak < 0) {
    throw new Error('calibrationState.rejectionStreak 必须是非负整数');
  }
  array(state.confirmedFacts, 'calibrationState.confirmedFacts', { max: 12 });
  array(state.rejectedHypotheses, 'calibrationState.rejectedHypotheses', { max: 12 });
  state.confirmedFacts.forEach((value, index) => string(value, `calibrationState.confirmedFacts[${index}]`));
  state.rejectedHypotheses.forEach((value, index) => string(value, `calibrationState.rejectedHypotheses[${index}]`));
}

function normalizeTopicDomain(topic) {
  if (/relationship|marriage|love|婚|感情|姻缘/i.test(topic)) return 'relationship';
  if (/career|work|事业|工作/i.test(topic)) return 'career';
  if (/wealth|money|财|收入|投资/i.test(topic)) return 'wealth';
  if (/health|健康/i.test(topic)) return 'health';
  return null;
}

function validateCalibration(item, index, evidenceById, rejectionStreak, topic) {
  const path = `calibration[${index}]`;
  object(item, path);
  for (const key of ['hypothesis_type', 'statement', 'question']) string(item[key], `${path}.${key}`);
  if (!CALIBRATION_TYPES.has(item.hypothesis_type)) throw new Error(`${path}.hypothesis_type 无效`);
  if (/[？?]/.test(item.statement)) throw new Error(`${path}.statement 必须先给判断，不能写成问题`);
  if ((item.question.match(/[？?]/g) || []).length !== 1) throw new Error(`${path}.question 必须只有一个问题`);
  if (item.hypothesis_type === 'input-boundary') {
    if (!INPUT_AUDIT_QUESTION.test(item.question)) throw new Error(`${path}.question 没有核对出生输入`);
  } else if (!CONFIRMATION_QUESTION.test(item.question)) {
    throw new Error(`${path}.question 必须用“对不对、对吗、是不是这样”等核对式问句`);
  }
  if (rejectionStreak >= 2 && item.hypothesis_type !== 'input-boundary') {
    throw new Error(`${path} 连续两次校盘不应后只能核对出生输入`);
  }
  validateEvidenceIds(item.evidence_ids, null, evidenceById, `${path}.evidence_ids`, { allowEmpty: false });
  const expectedDomain = normalizeTopicDomain(topic);
  if (item.hypothesis_type !== 'input-boundary' && expectedDomain) {
    const selected = item.evidence_ids.map(id => evidenceById.get(id));
    if (!selected.some(evidence => evidence?.domain === expectedDomain)) {
      throw new Error(`${path}.evidence_ids 没有与当前议题直接相关的盘面依据`);
    }
  }
}

function validatePlan(chart, plan) {
  if (chart.schemaVersion !== 'bazi-ziwei-chart.v2') throw new Error('不支持的 chart schemaVersion');
  if (plan.schemaVersion !== 'bazi-ziwei-consultation.v1') throw new Error('plan schemaVersion 必须为 bazi-ziwei-consultation.v1');
  if (!STAGES.has(plan.stage)) throw new Error(`stage 无效: ${plan.stage}`);
  if (!INTENTS.has(plan.intent)) throw new Error(`intent 无效: ${plan.intent}`);
  string(plan.topic, 'topic', { allowEmpty: plan.stage === 'calibration' });
  array(plan.calibration, 'calibration', { max: 1 });
  array(plan.conclusions, 'conclusions', { max: 4 });
  validateFocus(plan.focus, plan.conclusions.length > 0);
  validateCalibrationState(plan.calibrationState);
  if (plan.calibration.length && plan.conclusions.length) throw new Error('校盘轮次不得同时给出最终结论');
  if (plan.stage === 'calibration' && plan.focus.status !== 'calibrating') {
    throw new Error('calibration 阶段的 focus.status 必须为 calibrating');
  }
  if (plan.calibrationState.rejectionStreak >= 2 && plan.conclusions.length) {
    throw new Error('连续两次校盘不应后必须先核出生输入，不能继续下结论');
  }
  if (!plan.calibration.length && !plan.conclusions.length) throw new Error('每轮至少需要一条校盘话或一个结论');
  const evidence = chart.interpretation?.evidence || [];
  const evidenceById = new Map(evidence.map(item => [item.id, item]));
  if (!evidenceById.size) throw new Error('chart 没有内部证据');

  for (const [index, item] of plan.calibration.entries()) {
    validateCalibration(item, index, evidenceById, plan.calibrationState.rejectionStreak, plan.topic);
  }
  plan.conclusions.forEach((item, index) => validateConclusion(item, index, evidenceById));
  publicStrings(plan).forEach(([path, value]) => validatePublicText(value, path));

  const divinationChars = plan.conclusions.reduce((total, item) => total
    + item.verdict.length + item.timing.length
    + item.conditions.join('').length + item.guidance.join('').length, 0);
  const soulChars = (plan.soulNote || '').length;
  if (divinationChars && soulChars > Math.ceil(divinationChars * 0.25)) {
    throw new Error(`soulNote 过长：${soulChars} 字，超过断命内容的四分之一`);
  }
  if (plan.stage === 'calibration' && soulChars) throw new Error('校盘阶段不要加入点命段落');
  return {
    evidenceCount: evidenceById.size,
    directCount: plan.conclusions.filter(item => item.delivery === 'direct').length,
  };
}

function validateResponse(plan, response) {
  string(response, 'response');
  validatePublicText(response, 'response');
  validateDialogueShape(response);
  if (/\b(?:bazi|ziwei)-(?:foundation|palace|timing|structure)-/i.test(response)) {
    throw new Error('response 泄露 evidence ID');
  }
  const opening = response.slice(0, 160);
  if (/仅供参考|命运掌握在自己手里|最终取决于你/.test(opening)) {
    throw new Error('response 开头回避了用户要的直接判断');
  }
  for (const item of plan.conclusions.filter(value => value.delivery === 'direct')) {
    if (!response.includes(item.verdict)) throw new Error(`response 必须原样包含直断结论: ${item.verdict}`);
  }
  const firstPublic = plan.conclusions[0]?.verdict || plan.calibration[0]?.statement;
  if (firstPublic && !opening.includes(firstPublic)) {
    throw new Error('response 前 160 字必须出现本轮首个判断或校盘陈述');
  }
  return { chars: response.length };
}

function main() {
  const args = parseArgs();
  if (args.inquiry) {
    const result = validateInquiryResponse(readText(args.inquiry));
    process.stdout.write(`询问轮次通过：${result.chars} 字，1 个主问题\n`);
    return;
  }
  if (!args.chart || !args.plan) throw new Error('用法: --chart=chart.json --plan=plan.json [--response=response.txt]');
  const chart = readJson(args.chart);
  const plan = readJson(args.plan);
  const result = validatePlan(chart, plan);
  let message = `会谈计划通过：${result.evidenceCount} 个内部证据，${result.directCount} 条强制直断`;
  if (args.response) {
    const responseResult = validateResponse(plan, readText(args.response));
    message += `；用户答复 ${responseResult.chars} 字`;
  }
  process.stdout.write(message + '\n');
}

if (require.main === module) {
  try {
    main();
  } catch (error) {
    process.stderr.write(`会谈校验失败：${error instanceof Error ? error.message : String(error)}\n`);
    process.exitCode = 1;
  }
}

module.exports = { validatePlan, validateResponse, validateInquiryResponse };
