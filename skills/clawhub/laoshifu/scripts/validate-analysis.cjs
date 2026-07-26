#!/usr/bin/env node
'use strict';

const fs = require('node:fs');

function readJson(path) {
  return JSON.parse(fs.readFileSync(path, 'utf8').replace(/^\uFEFF/, ''));
}

function parseArgs() {
  const args = {};
  for (const value of process.argv.slice(2)) {
    const match = value.match(/^--([^=]+)=(.*)$/);
    if (match) args[match[1]] = match[2];
  }
  return args;
}

function requireObject(value, path) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) throw new Error(`${path} 必须是对象`);
}

function requireArray(value, length, path) {
  if (!Array.isArray(value) || value.length !== length) throw new Error(`${path} 必须恰好有 ${length} 项`);
}

function requireEvidenceIds(value, validIds, path) {
  if (!Array.isArray(value) || value.length === 0) throw new Error(`${path}.evidence_ids 至少需要一个证据 ID`);
  for (const id of value) if (!validIds.has(id)) throw new Error(`${path} 引用了不存在的 evidence ID: ${id}`);
}

function scanStrings(value, path = '$', output = []) {
  if (typeof value === 'string') output.push([path, value]);
  else if (Array.isArray(value)) value.forEach((item, index) => scanStrings(item, `${path}[${index}]`, output));
  else if (value && typeof value === 'object') Object.entries(value).forEach(([key, item]) => scanStrings(item, `${path}.${key}`, output));
  return output;
}

function validateStrongLanguage(value, evidenceById, path = '$') {
  if (Array.isArray(value)) {
    value.forEach((item, index) => validateStrongLanguage(item, evidenceById, `${path}[${index}]`));
    return;
  }
  if (!value || typeof value !== 'object') return;

  const ids = Object.entries(value)
    .filter(([key, item]) => key.endsWith('evidence_ids') && Array.isArray(item))
    .flatMap(([, item]) => item);
  const hasStrongPhrase = Object.entries(value)
    .some(([, item]) => typeof item === 'string' && /我敢肯定|相信我/.test(item));
  if (hasStrongPhrase) {
    const selected = ids.map(id => evidenceById.get(id)).filter(Boolean);
    const bazi = selected.filter(item => item.system === 'bazi' && item.confidence === 'high');
    const ziwei = selected.filter(item => item.system === 'ziwei' && item.confidence === 'high');
    const sharedDomain = bazi.some(left => ziwei.some(right => left.domain === right.domain));
    if (!sharedDomain) {
      throw new Error(`${path} 使用强肯定语气，但没有同领域的八字与紫微高强度证据`);
    }
    if (selected.some(item => item.domain === 'health' || item.domain === 'timing')) {
      throw new Error(`${path} 的健康或时间判断不得使用强肯定语气`);
    }
  }
  Object.entries(value).forEach(([key, item]) => validateStrongLanguage(item, evidenceById, `${path}.${key}`));
}

function validateAnalysis(chart, analysis) {
  if (chart.schemaVersion !== 'bazi-ziwei-chart.v2') throw new Error('命盘 schemaVersion 不是 bazi-ziwei-chart.v2');
  const validIds = new Set((chart.interpretation?.evidence || []).map(item => item.id));
  const evidenceById = new Map((chart.interpretation?.evidence || []).map(item => [item.id, item]));
  if (!validIds.size) throw new Error('命盘没有 interpretation.evidence');

  requireObject(analysis.meta, 'meta');
  requireEvidenceIds(analysis.meta.evidence_ids, validIds, 'meta');
  requireObject(analysis.axes, 'axes');
  requireEvidenceIds(analysis.axes.bazi_evidence_ids, validIds, 'axes.bazi');
  requireEvidenceIds(analysis.axes.ziwei_evidence_ids, validIds, 'axes.ziwei');
  requireArray(analysis.strengths, 3, 'strengths');
  requireArray(analysis.weaknesses, 3, 'weaknesses');
  analysis.strengths.forEach((item, index) => requireEvidenceIds(item.evidence_ids, validIds, `strengths[${index}]`));
  analysis.weaknesses.forEach((item, index) => requireEvidenceIds(item.evidence_ids, validIds, `weaknesses[${index}]`));
  requireEvidenceIds(analysis.section_01?.evidence_ids, validIds, 'section_01');
  requireEvidenceIds(analysis.section_02?.evidence_ids, validIds, 'section_02');

  requireObject(analysis.dim, 'dim');
  for (const key of ['career','wealth','marriage','children','family','health']) {
    requireObject(analysis.dim[key], `dim.${key}`);
    requireEvidenceIds(analysis.dim[key].evidence_ids, validIds, `dim.${key}`);
    if (!['verdict-yes','verdict-partial','verdict-no'].includes(analysis.dim[key].verdict_class)) {
      throw new Error(`dim.${key}.verdict_class 无效`);
    }
  }

  requireArray(analysis.conflicts, 3, 'conflicts');
  analysis.conflicts.forEach((item, index) => requireEvidenceIds(item.evidence_ids, validIds, `conflicts[${index}]`));
  requireObject(analysis.final, 'final');
  requireArray(analysis.final.nodes, 5, 'final.nodes');
  requireArray(analysis.final.risks, 3, 'final.risks');
  requireArray(analysis.final.leverage, 2, 'final.leverage');
  requireArray(analysis.final.advice, 4, 'final.advice');
  analysis.final.nodes.forEach((item, index) => requireEvidenceIds(item.evidence_ids, validIds, `final.nodes[${index}]`));
  analysis.final.risks.forEach((item, index) => requireEvidenceIds(item.evidence_ids, validIds, `final.risks[${index}]`));
  analysis.final.leverage.forEach((item, index) => requireEvidenceIds(item.evidence_ids, validIds, `final.leverage[${index}]`));

  const forbidden = /置信度|注定|必然发财|必然离婚|必得重病|绝对会|克死/;
  const violation = scanStrings(analysis).find(([, value]) => forbidden.test(value));
  if (violation) throw new Error(`${violation[0]} 包含禁用或宿命化措辞: ${violation[1]}`);
  validateStrongLanguage(analysis, evidenceById);
  return { evidenceCount: validIds.size };
}

function main() {
  const args = parseArgs();
  if (args.internal !== 'true') throw new Error('旧技术分析仅限内部审计；必须显式传 --internal=true，且不得交付给用户');
  if (!args.chart || !args.analysis) throw new Error('用法: --chart=chart.json --analysis=analysis.json');
  const chart = readJson(args.chart);
  const analysis = readJson(args.analysis);
  const result = validateAnalysis(chart, analysis);
  process.stdout.write(`analysis.json 校验通过：${result.evidenceCount} 个可用证据 ID\n`);
}

if (require.main === module) {
  try {
    main();
  } catch (error) {
    process.stderr.write(`分析校验失败：${error instanceof Error ? error.message : String(error)}\n`);
    process.exitCode = 1;
  }
}

module.exports = { validateAnalysis };
