#!/usr/bin/env node
'use strict';

const fs = require('node:fs');

const STAGES = new Set(['reading', 'deepening', 'closure']);
const INTENTS = new Set(['curiosity', 'comfort', 'decision']);
const DELIVERIES = new Set(['firm', 'probable', 'tentative']);
const ANSWER_NEEDS = new Set(['outcome', 'timing', 'turning-point', 'cause', 'decision', 'overview']);
const TECHNICAL_PROSE = /证据|权重|置信度|算法|模型|引擎|分析过程|推断链|用神|旺衰|月建|日辰|旬空|月破|日破|暗动|回头生|回头克|化进|化退|六亲|六神|世爻|应爻|evidence|analysis|engine/i;
const DANGEROUS_TERMS = /克死|必死|死期|寿命断定|绝症|必然离婚|一定离婚|保证发财|稳赚不赔|必定发财/;
const REPORT_TONE_TERMS = /综合来看|综上所述|总体而言|值得注意的是|基于以上(?:分析|判断)|建议如下|以下几点/;
const PSEUDO_DEPTH_TERMS = /说到底|本质上|归根结底|真正的问题是|真正重要的是|问题的核心是/;
const FABRICATED_SCENE_TERMS = /坐下说吧|请坐|坐吧|把手(?:伸过来|给我)|伸(?:出)?手(?:来|给我)|点(?:上|一)?炷香|喝口茶/;
const ABUSIVE_RETORT_TERMS = /你(?:这个|真是)?(?:蠢货|白痴|废物|垃圾|傻子)|(?:给我)?滚(?:开|蛋)?|闭嘴|你算什么东西|没教养的东西/;
const HEDGES = /大概率|多半|可能|也许|或许|似乎|倾向于|不排除|未必|说不准/;
const FIRM_MARKERS = /可以定下来|可以直断|很明确|不用绕弯子|能成|成不了|会成|不会成|能过去|过不去|有转机|没有转机/;

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

function validateQuestion(chart, plan) {
  object(plan.question, 'question');
  for (const key of ['text', 'category', 'answerNeed', 'desiredOutcome']) string(plan.question[key], `question.${key}`);
  if (!ANSWER_NEEDS.has(plan.question.answerNeed)) throw new Error(`question.answerNeed 无效: ${plan.question.answerNeed}`);
  if (plan.question.text.trim() !== chart.question.text.trim()) throw new Error('计划问题与起卦问题不一致');
  if (/^(?:我)?(?:想)?(?:问|看)?(?:一下)?(?:感情|婚姻|事业|工作|财运|健康|未来|运势)[。？！?!]*$/.test(plan.question.text.trim())) {
    throw new Error('起卦问题仍是宽泛领域，必须先问清具体事项');
  }
  array(plan.question.knownContext, 'question.knownContext', { min: 1, max: 8 });
  plan.question.knownContext.forEach((value, index) => string(value, `question.knownContext[${index}]`));
}

function validateEvidenceIds(ids, allowed, path) {
  array(ids, path, { min: 1, max: 8 });
  for (const id of ids) {
    string(id, `${path}[]`);
    if (!allowed.has(id)) throw new Error(`${path} 引用了不属于该类的依据: ${id}`);
  }
}

function publicTexts(plan) {
  const output = [];
  for (const [index, item] of plan.conclusions.entries()) {
    output.push([`conclusions[${index}].verdict`, item.verdict]);
    output.push([`conclusions[${index}].timing`, item.timing]);
    item.conditions.forEach((value, i) => output.push([`conclusions[${index}].conditions[${i}]`, value]));
    item.guidance.forEach((value, i) => output.push([`conclusions[${index}].guidance[${i}]`, value]));
  }
  output.push(['soulNote', plan.soulNote || '']);
  return output;
}

function validatePublicProse(value, path) {
  string(value, path, { allowEmpty: true });
  if (TECHNICAL_PROSE.test(value)) throw new Error(`${path} 泄露了后台六爻推演术语: ${value}`);
  if (DANGEROUS_TERMS.test(value)) throw new Error(`${path} 包含恐吓或确定性伤害断语: ${value}`);
  if (REPORT_TONE_TERMS.test(value)) throw new Error(`${path} 使用了报告腔: ${value}`);
  if (PSEUDO_DEPTH_TERMS.test(value)) throw new Error(`${path} 使用了权威式假深刻表达: ${value}`);
  if (FABRICATED_SCENE_TERMS.test(value)) throw new Error(`${path} 虚构了用户所处场景或动作: ${value}`);
  if (ABUSIVE_RETORT_TERMS.test(value)) throw new Error(`${path} 用辱骂代替了有分寸的边界: ${value}`);
}

function validateConclusion(item, index, textualIds, structuralIds) {
  const path = `conclusions[${index}]`;
  object(item, path);
  for (const key of ['id', 'appliesTo', 'verdict', 'timing', 'delivery']) {
    string(item[key], `${path}.${key}`, { allowEmpty: key === 'timing' });
  }
  if (!DELIVERIES.has(item.delivery)) throw new Error(`${path}.delivery 无效`);
  if (item.appliesTo.length < 4) throw new Error(`${path}.appliesTo 必须说明这条判断怎样对应所问事项`);
  array(item.conditions, `${path}.conditions`, { min: 1, max: 3 });
  array(item.guidance, `${path}.guidance`, { max: 2 });
  validateEvidenceIds(item.textual_evidence_ids, textualIds, `${path}.textual_evidence_ids`);
  validateEvidenceIds(item.structural_evidence_ids, structuralIds, `${path}.structural_evidence_ids`);
  array(item.counter_evidence_ids || [], `${path}.counter_evidence_ids`, { max: 4 });
  for (const id of item.counter_evidence_ids || []) {
    if (!textualIds.has(id) && !structuralIds.has(id)) throw new Error(`${path}.counter_evidence_ids 引用了不存在的依据: ${id}`);
  }
  const total = item.textual_evidence_ids.length + item.structural_evidence_ids.length;
  const structuralShare = item.structural_evidence_ids.length / total;
  if (structuralShare < 0.6 || structuralShare > 0.8) {
    throw new Error(`${path} 的依据比例偏离卦辞爻辞约三成、六爻结构约七成`);
  }
  if (item.delivery === 'firm') {
    if (HEDGES.test(item.verdict)) throw new Error(`${path}.verdict 坚定断语中不得使用退让词`);
    if (!FIRM_MARKERS.test(item.verdict)) throw new Error(`${path}.verdict 缺少明确回答成败或走向的用语`);
  }
}

function validatePlan(chart, plan) {
  if (chart.schemaVersion !== 'aceworld-liuyao-chart.v1') throw new Error('不支持的六爻 chart schemaVersion');
  if (plan.schemaVersion !== 'aceworld-liuyao-consultation.v1') throw new Error('plan schemaVersion 必须为 aceworld-liuyao-consultation.v1');
  if (!STAGES.has(plan.stage)) throw new Error(`stage 无效: ${plan.stage}`);
  if (!INTENTS.has(plan.intent)) throw new Error(`intent 无效: ${plan.intent}`);
  validateQuestion(chart, plan);
  object(plan.evidenceBalance, 'evidenceBalance');
  if (plan.evidenceBalance.texts !== 0.3 || plan.evidenceBalance.structure !== 0.7) {
    throw new Error('evidenceBalance 必须固定为 texts=0.3、structure=0.7');
  }
  array(plan.conclusions, 'conclusions', { min: 1, max: 3 });
  const textualIds = new Set(chart.interpretation.textualEvidence.map(item => item.id));
  const structuralIds = new Set(chart.interpretation.structuralEvidence.map(item => item.id));
  if (!textualIds.size || !structuralIds.size) throw new Error('六爻盘缺少文本或结构依据');
  plan.conclusions.forEach((item, index) => validateConclusion(item, index, textualIds, structuralIds));
  string(plan.soulNote || '', 'soulNote', { allowEmpty: true });
  publicTexts(plan).forEach(([path, value]) => validatePublicProse(value, path));
  const divinationChars = plan.conclusions.reduce((total, item) => total
    + item.verdict.length + item.timing.length + item.conditions.join('').length + item.guidance.join('').length, 0);
  if ((plan.soulNote || '').length > Math.ceil(divinationChars * 0.25)) throw new Error('soulNote 超过断事内容的四分之一');
  return { textualCount: textualIds.size, structuralCount: structuralIds.size };
}

function validateResponse(chart, plan, response) {
  string(response, 'response');
  if (!response.includes(chart.diagram)) throw new Error('response 必须原样包含标准本卦、变卦卦图');
  if (response.indexOf(chart.diagram) > 40) throw new Error('标准卦图必须放在答复开头');
  if (/```/.test(response)) throw new Error('标准卦图已经是 Markdown 表格，不得再套入代码块');
  if (!chart.diagram.includes('| 六神 | 爻位 | 六亲纳甲 |')) throw new Error('chart.diagram 不是稳定的 Markdown 表格格式');
  const prose = response.replace(chart.diagram, '').trim();
  validatePublicProse(prose, 'response 正文');
  if (prose.length > 520) throw new Error(`response 正文过长：${prose.length} 字`);
  if (/^\s*(?:#{1,6}\s|[-*+]\s|\d+[.、)]\s)/m.test(prose)) throw new Error('response 正文不得使用标题、项目符号或编号列表');
  if ((prose.match(/[？?]/g) || []).length > 1) throw new Error('response 一轮最多问一个问题');
  const firstVerdict = plan.conclusions[0].verdict;
  if (!prose.slice(0, 180).includes(firstVerdict)) throw new Error('response 正文开头必须原样出现首条判断');
  return { proseChars: prose.length };
}

function main() {
  const args = parseArgs();
  if (!args.chart || !args.plan) throw new Error('用法: --chart=liuyao-chart.json --plan=liuyao-plan.json [--response=response.txt]');
  const chart = readJson(args.chart);
  const plan = readJson(args.plan);
  const result = validatePlan(chart, plan);
  let message = `六爻会谈计划通过：${result.textualCount} 条文本依据，${result.structuralCount} 条结构依据`;
  if (args.response) message += `；正文 ${validateResponse(chart, plan, readText(args.response)).proseChars} 字`;
  process.stdout.write(message + '\n');
}

if (require.main === module) {
  try {
    main();
  } catch (error) {
    process.stderr.write(`六爻会谈校验失败：${error instanceof Error ? error.message : String(error)}\n`);
    process.exitCode = 1;
  }
}

module.exports = { validatePlan, validateResponse };
