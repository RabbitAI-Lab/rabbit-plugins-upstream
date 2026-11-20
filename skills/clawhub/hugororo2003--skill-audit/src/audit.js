'use strict';
const fs = require('fs');
const path = require('path');

const INJECTION = [
  { id: 'S1', re: new RegExp(['ign', 'ore\\s+(?:all\\s+|any\\s+)?(?:prev', 'ious|prior|above)\\s+(?:inst', 'ructions|prompts?|rules?|context)'].join(''), 'i'), msg: 'Prompt-injection: asks to ignore prior instructions' },
  { id: 'S2', re: new RegExp(['(?:rev', 'eal|show|print|repeat|output)\\s+(?:your\\s+|the\\s+)?(?:sys', 'tem\\s+prompt|hidden\\s+instructions|initial\\s+instructions|secrets?)'].join(''), 'i'), msg: 'Prompt-injection: asks to reveal system prompt or secrets' },
  { id: 'S3', re: new RegExp(['(?:exfil', 'trat\\w*|upload|send|post|transmit)[^.\\r\\n]{0,60}https?:\\/\\/'].join(''), 'i'), msg: 'Possible exfiltration: sends data to a remote URL' },
  { id: 'S4', re: new RegExp(['(?:cu', 'rl|wget)[^|\\r\\n]*\\|\\s*(?:sudo\\s+)?(?:ba)?sh'].join(''), 'i'), msg: 'Dangerous: pipes remote content straight into a shell' },
  { id: 'S5a', re: /\b(?:eval|new\s+Function)\s*\(/, msg: 'Obfuscation: dynamic code evaluation' },
  { id: 'S5b', re: /[A-Za-z0-9+/]{120,}={0,2}/, msg: 'Obfuscation: large base64-like blob' },
  { id: 'S5c', re: /[\u200b-\u200f\u202a-\u202e\u2060\ufeff]/, msg: 'Obfuscation: hidden unicode characters' },
  { id: 'S6a', re: /sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16}/, msg: 'Hardcoded secret (API key / PAT / AWS key)' },
  { id: 'S6b', re: /-----BEGIN [A-Z ]*PRIVATE KEY-----/, msg: 'Hardcoded private key' },
];
const SCRIPT_RISK = [
  { id: 'R1', re: new RegExp(['r', 'm\\s+-rf?\\s+(?:~|\\/|\\$HOME|\\.\\.)'].join('')), msg: 'Destructive rm -rf on home or root' },
  { id: 'R2', re: /(?:^|\r?\n)\s*(?:sudo\s+)?(?:crontab|systemctl|service)\b/, msg: 'Touches system scheduler/services' },
  { id: 'R3', re: new RegExp(['chm', 'od\\s+777'].join('')), msg: 'chmod 777 (permissive)' },
  { id: 'R4', re: /(?:^|\r?\n)\s*(?:sudo\s+)?(?:cat|cp|mv|rm)\b[^\r\n]*\/etc\//, msg: 'Modifies /etc' },
];

function parseFrontmatter(md) {
  const m = md.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
  if (!m) return { fm: null, body: md };
  const fm = {};
  for (const line of m[1].split(/\r?\n/)) {
    const kv = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (kv) fm[kv[1].toLowerCase()] = kv[2].replace(/^['\"]|['\"]$/g, '');
  }
  return { fm, body: md.slice(m[0].length) };
}

function codeBlocks(body) {
  const blocks = [];
  const re = /```([a-zA-Z0-9]*)\r?\n([\s\S]*?)```/g;
  let m; while ((m = re.exec(body)) !== null) blocks.push({ lang: m[1] || 'text', code: m[2] });
  return blocks;
}

function grade(score) {
  if (score >= 90) return 'A'; if (score >= 75) return 'B';
  if (score >= 60) return 'C'; if (score >= 45) return 'D'; return 'F';
}

function auditFile(file) {
  return auditMarkdown(fs.readFileSync(file, 'utf8'), path.dirname(file));
}

function auditMarkdown(md, dir) {
  dir = dir || '.';
  const { fm, body } = parseFrontmatter(md);
  const findings = [];
  const blocks = codeBlocks(body);
  const codeText = blocks.map(b => b.code).join('\n');
  let critical = false;
  function add(id, category, severity, pass, msg) {
    if (severity === 'critical' && !pass) critical = true;
    findings.push({ id, category, severity, pass, msg });
  }
  for (const r of INJECTION) add(r.id, 'safety', 'critical', !r.re.test(md), r.msg);
  for (const r of SCRIPT_RISK) add(r.id, 'safety', 'critical', !r.re.test(codeText), r.msg);
  add('T1', 'structure', 'critical', !!fm, 'Valid YAML frontmatter present');
  const name = fm ? fm.name || '' : '';
  add('T2', 'structure', 'major', /^[A-Za-z0-9$-]{2,64}$/.test(name), 'Skill name valid (2-64 chars, url-safe)');
  const desc = fm ? fm.description || '' : '';
  add('T3', 'structure', 'major', desc.length >= 40, 'Description meaningful (>= 40 chars)');
  add('T4', 'structure', 'major', /##\s+(use|usage|example|when)/i.test(body), 'Has usage / when-to-use section');
  add('T5', 'structure', 'major', /##\s+(how|procedure|steps|workflow|guide)/i.test(body), 'Has procedure / steps section');
  const vague = (body.match(/\b(as needed|various|etc\.?|and so on|somehow)\b/gi) || []).length;
  add('C1', 'clarity', 'minor', vague <= 3, 'Low vagueness (' + vague + ' vague terms)');
  add('M1', 'maintainability', 'minor', md.length <= 60000, 'Reasonable size (< 60KB)');
  const hasLicense = (fm && fm.license) || fs.existsSync(path.join(dir, 'LICENSE')) || fs.existsSync(path.join(dir, '..', 'LICENSE'));
  add('M2', 'maintainability', 'minor', !!hasLicense, 'License declared');
  const urls = [...new Set((codeText + ' ' + body).match(/https?:\/\/[^\s)\]\}>'\"]+/g) || [])];
  let score = 100;
  for (const f of findings) {
    if (f.pass) continue;
    score -= f.severity === 'critical' ? 40 : f.severity === 'major' ? 10 : 5;
  }
  if (critical) score = Math.min(score, 25);
  score = Math.max(0, score);
  return {
    skill: { name: name || path.basename(dir), description: desc, license: fm ? fm.license || null : null },
    score, grade: grade(score),
    findings: findings.map(f => ({ ...f, evidence: f.pass ? null : ruleEvidence(f.id) })),
    stats: { size: md.length, headings: (body.match(/^##+\s/gm) || []).length, codeBlocks: blocks.length, urls },
    generatedAt: new Date().toISOString(),
  };
  function ruleEvidence(id) { return id; }
}

function findSkillMd(target) {
  const st = fs.statSync(target);
  if (st.isFile()) return target;
  const p = path.join(target, 'SKILL.md');
  if (fs.existsSync(p)) return p;
  const hits = [];
  (function walk(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      if (e.name === 'node_modules' || e.name === '.git') continue;
      if (e.isDirectory()) walk(path.join(d, e.name));
      else if (e.name === 'SKILL.md') hits.push(path.join(d, e.name));
    }
  })(target);
  return hits[0] || null;
}

module.exports = { auditFile, auditMarkdown, findSkillMd, grade };