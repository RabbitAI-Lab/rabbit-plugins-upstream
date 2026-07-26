#!/usr/bin/env node

const BASE_URL = 'https://clip2.md/api/v1';
const CONFIG_DIR = require('path').join(require('os').homedir(), '.clip2md');
const CONFIG_FILE = require('path').join(CONFIG_DIR, 'config.json');

function loadConfig() {
  try {
    return JSON.parse(require('fs').readFileSync(CONFIG_FILE, 'utf-8'));
  } catch {
    return null;
  }
}

function saveConfig(config) {
  require('fs').mkdirSync(CONFIG_DIR, { recursive: true });
  require('fs').writeFileSync(CONFIG_FILE, JSON.stringify(config, null, 2));
}

async function request(method, path, body = null) {
  const config = loadConfig();
  if (!config?.token) {
    console.error('未配置 token。请先运行: node clip2md.js config <your_token>');
    process.exit(1);
  }

  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${config.token}`,
  };

  const options = { method, headers };
  if (body) options.body = JSON.stringify(body);

  const res = await fetch(`${BASE_URL}${path}`, options);

  if (res.status === 401) {
    console.error('Token 已过期或无效。请重新运行: node clip2md.js config <your_token>');
    process.exit(1);
  }

  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    console.error(`请求失败 (${res.status}): ${err.detail || res.statusText}`);
    process.exit(1);
  }

  return res.json();
}

async function cmdConfig(token) {
  if (!token) {
    console.error('用法: node clip2md.js config <token>');
    process.exit(1);
  }
  saveConfig({ token });
  console.log('Token 已保存到 ~/.clip2md/config.json');
}

async function cmdClip(url) {
  if (!url) {
    console.error('用法: node clip2md.js clip <url>');
    process.exit(1);
  }

  console.log(`正在剪藏: ${url}`);
  const task = await request('POST', '/tasks', { url });
  console.log(`任务已提交 (ID: ${task.id}, 状态: ${task.status})`);

  // 查询额度
  try {
    const user = await request('GET', '/auth/me');
    console.log(`剩余额度: 每日 ${user.daily_quota} 次, 永久 ${user.permanent_quota} 次`);
  } catch {}
}

async function cmdQuota() {
  const user = await request('GET', '/auth/me');
  console.log(`每日额度: ${user.daily_quota} 次`);
  console.log(`永久额度: ${user.permanent_quota} 次`);
}

// 主入口
const args = process.argv.slice(2);
const cmd = args[0];

switch (cmd) {
  case 'config':
    cmdConfig(args[1]);
    break;
  case 'clip':
    cmdClip(args[1]);
    break;
  case 'quota':
    cmdQuota();
    break;
  default:
    console.log(`clip2md - 网页剪藏工具

用法:
  node clip2md.js config <token>   配置认证 token
  node clip2md.js clip <url>       剪藏网页链接
  node clip2md.js quota            查询剩余额度`);
    process.exit(1);
}
