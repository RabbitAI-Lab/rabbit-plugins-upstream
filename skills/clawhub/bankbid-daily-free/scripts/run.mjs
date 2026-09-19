#!/usr/bin/env node
/**
 * bankbid-daily-free —— 免费版薄客户端（数据与筛选规则在服务端，包内不含规则实现）。
 * 免费额度由服务端按能力计数；用完后返回 HTTP 402 并附官方购买指令。
 */
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ENDPOINTS = ['https://www.tokendidi.cn/api/bankbid/api/v1/bankbid-daily'];
const CRED = path.join(os.homedir(), '.bankbid', 'credentials.json');
const args = process.argv.slice(2);
const flag = (n) => args.includes(n);
const opt = (n, d) => { const i = args.indexOf(n); return i >= 0 && args[i + 1] ? args[i + 1] : d; };

/** 设备指纹：只上报原始字段，哈希由服务端加盐算（删文件也不重置额度）。 */
function fingerprint() {
  let src = 'hostname', val = '';
  try {
    if (process.platform === 'linux') {
      for (const p of ['/etc/machine-id', '/var/lib/dbus/machine-id']) {
        if (fs.existsSync(p)) { val = fs.readFileSync(p, 'utf8').trim(); src = 'linux-machine-id'; break; }
      }
    } else if (process.platform === 'darwin') {
      const out = require('node:child_process').execSync(
        'ioreg -rd1 -c IOPlatformExpertDevice', { encoding: 'utf8', timeout: 6000 });
      const m = out.split('\n').find((l) => l.includes('IOPlatformUUID'));
      if (m) { val = m.split('=').pop().trim().replace(/"/g, ''); src = 'mac-ioplatformuuid'; }
    } else if (process.platform === 'win32') {
      const out = require('node:child_process').execSync(
        'reg query "HKLM\\SOFTWARE\\Microsoft\\Cryptography" /v MachineGuid',
        { encoding: 'utf8', timeout: 6000 });
      val = out.trim().split(/\s+/).pop(); src = 'win-machineguid';
    }
  } catch { /* 降级 */ }
  if (!val) val = os.hostname();

  /* ⚠️ 容器风险（R14 实测后加）：Docker 等容器里的 /etc/machine-id 常从**基础镜像继承**，
     同一镜像起的多个容器 machine-id 相同 ⇒ 多个真实买家会被认成同一个账户，
     第二个用户一上来就看到"免费额度已用完"，直接流失。
     判断：machine-id 为空 / 全零 / 过短 / 命中已知基础镜像默认值 ⇒ **不可信**，
     退化为「主机名+用户名+主目录」（这三项在真实用户之间通常不同）。
     两种情况下都带上 home —— 它是稳定的低成本熵。 */
  const HOME_DIR = os.homedir() || '-';
  const USER = process.env.USER || process.env.USERNAME || '-';
  const UNTRUSTED = !val || /^0+$/.test(val) || val.length < 16
    || /^(?:0{32}|f{32}|1{32})$/.test(val);
  if (UNTRUSTED) src = 'host-user-home';
  const v = UNTRUSTED ? os.hostname() : val;
  return `source=${src};value=${v};host=${os.hostname()};user=${USER};home=${HOME_DIR}`;
}

function loadKey() {
  try { return JSON.parse(fs.readFileSync(CRED, 'utf8')).account_key || ''; } catch { return ''; }
}

let keywords = opt('--keywords', '');
let kind = opt('--kind', '');
if (flag('--sample') || !keywords) {
  try {
    const s = JSON.parse(fs.readFileSync(path.join(HERE, '..', 'templates', 'sample.json'), 'utf8'));
    keywords = (s.keywords || []).join(',');
    if (!kind) kind = s.kind || 'daily';
  } catch { keywords = '信创,自助设备'; }
}
if (!kind) kind = 'daily';

const body = {
  keywords: keywords.split(/[,，|]/).map((x) => x.trim()).filter(Boolean),
  kind,
  family: opt('--family', 'bank'),
};
const d = Number(opt('--days', '0'));
if (d > 0) body.days = d;

const headers = { 'Content-Type': 'application/json', 'X-Device-Fingerprint': fingerprint() };
const key = loadKey();
if (key) headers['Authorization'] = 'Bearer ' + key;

let r = null, out = {}, failures = [];
for (const ep of ENDPOINTS) {
  try {
    r = await fetch(ep, { method: 'POST', headers, body: JSON.stringify(body) });
    out = await r.json().catch(() => ({}));
    break;
  } catch (e) { failures.push(ep + '（' + e.message + '）'); r = null; }
}
if (!r) {
  console.error('本次未能获取：服务端入口不可达 —— ' + failures.join('；'));
  process.exit(4);
}
if (r.status === 402) {
  console.error(out.message || '免费额度已用完，订阅后可继续使用。');
  const a = out.action || {};
  console.error('');
  console.error('订阅：' + (a.title || '') + '　¥' + (a.price_cny_per_month ?? 9.9) + '/月');
  if (a.instruction) {
    console.error('');
    console.error('把下面这段原样交给你的 Agent 即可完成订阅：');
    console.error('---');
    console.error(a.instruction);
    console.error('---');
  }
  if (out.fallback && out.fallback.guide_url) console.error('或打开：' + out.fallback.guide_url);
  process.exit(2);
}
if (!r.ok) {
  console.error('服务端返回 HTTP ' + r.status + '：' + JSON.stringify(out).slice(0, 200));
  process.exit(1);
}

// 首次下发令牌 → 必须告知用户保存
if (out.account_key) {
  fs.mkdirSync(path.dirname(CRED), { recursive: true });
  fs.writeFileSync(CRED, JSON.stringify({ account_key: out.account_key,
    server: ENDPOINTS[0], created_at: new Date().toISOString() }, null, 1));
  console.error('【重要】已为你生成专属 API Key，请务必保存：');
  console.error('  ' + out.account_key);
  console.error('  ' + (out.account_key_notice || ''));
  console.error('');
}

const res = out.result || {};
if (flag('--json')) {
  console.log(JSON.stringify({ matched: res.matched, closing_soon: res.closing_soon,
    report_url: res.report_url, items: res.items }, null, 2));
} else {
  console.log(res.markdown || '(无内容)');
  if (res.report_url) console.log('\n网页版日报（可直接打开/转发）：' + res.report_url);
  if (out.free_quota) console.log('（免费额度：已用 ' + out.free_quota.used + '/'
    + out.free_quota.limit + '，剩 ' + out.free_quota.remaining + ' 次）');
}
