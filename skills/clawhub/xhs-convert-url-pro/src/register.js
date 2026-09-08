'use strict';
/**
 * src/register.js — 交互式注册 / 登录（readline 问答）。
 *
 * 所有交互提示走 stderr，stdout 只输出 JSON（由 cli.js 统一控制）。
 * 注意：问答基于自建行缓冲（rl.on('line')），而非 rl.question —— 管道输入一次性
 * 送达时，question 在等待网络响应期间会丢失先到的行，行缓冲对 TTY 与管道都可靠。
 */
const readline = require('readline');
const { BizError } = require('./client');
const { saveConfig } = require('./config');

const PHONE_RE = /^1[3-9]\d{9}$/;
// 密码强度：≥8 位且含字母+数字（与服务端一致）
const PASSWORD_RE = /^(?=.*[A-Za-z])(?=.*\d).{8,64}$/;

/** 创建 readline 并挂行缓冲；rl.nextLine() 取下一行（EOF 时 reject）。 */
function createRl() {
  const rl = readline.createInterface({ input: process.stdin, output: process.stderr });
  const lines = [];
  const waiters = [];
  let closed = false;
  rl.on('line', (line) => {
    if (waiters.length) waiters.shift()(line);
    else lines.push(line);
  });
  rl.on('close', () => {
    closed = true;
    while (waiters.length) waiters.shift()(null);
  });
  rl.nextLine = () => new Promise((resolve, reject) => {
    if (lines.length) return resolve(lines.shift());
    if (closed) return reject(new Error('输入中断'));
    waiters.push((line) => (line === null ? reject(new Error('输入中断')) : resolve(line)));
  });
  return rl;
}

/** 普通提问（回显）。 */
async function ask(rl, query) {
  rl.output.write(query);
  return (await rl.nextLine()).trim();
}

/** 密码提问（TTY 下不回显；管道输入时按普通行读取）。 */
async function askHidden(rl, query) {
  rl.output.write(query);
  if (rl.terminal && typeof rl._writeToOutput === 'function') {
    const orig = rl._writeToOutput;
    // 屏蔽回显，仅保留换行
    rl._writeToOutput = (s) => { if (/\r?\n/.test(s)) rl.output.write('\n'); };
    try {
      return (await rl.nextLine()).trim();
    } finally {
      rl._writeToOutput = orig;
    }
  }
  return (await rl.nextLine()).trim();
}

/**
 * 交互式注册：手机号 → 短信验证码（debug 模式自动填入）→ 设置密码 → 注册并保存 token。
 * @param {ApiClient} client
 * @returns {Promise<{phone: string, quota_balance: number, gift_quota: number}>}
 */
async function runRegister(client) {
  const rl = createRl();
  try {
    let phone = '';
    for (;;) {
      phone = await ask(rl, '手机号: ');
      if (PHONE_RE.test(phone)) break;
      process.stderr.write('手机号格式错误（需 1 开头 11 位数字），请重新输入\n');
    }

    let smsData;
    try {
      smsData = await client.sendSmsCode(phone, 'register');
    } catch (err) {
      if (err instanceof BizError && err.code === 2003) {
        throw new BizError(2003, '服务端要求每次发送短信前先过图形验证码，终端无法完成；请改用扫码/链接注册：node cli.js register --link');
      }
      throw err;
    }

    let code;
    if (smsData && smsData.debug_code) {
      // 过渡期 sms.debug=true：服务端回显验证码，直接自动填入
      code = String(smsData.debug_code);
      process.stderr.write('验证码已发送（debug 模式已自动填入，也可使用万能验证码 888888）\n');
    } else {
      code = await ask(rl, '请输入手机收到的 6 位短信验证码: ');
    }

    let password = '';
    for (;;) {
      password = await askHidden(rl, '设置密码（≥8 位，须含字母+数字）: ');
      if (PASSWORD_RE.test(password)) break;
      process.stderr.write('密码需 ≥8 位且同时包含字母和数字，请重新输入\n');
    }

    const data = await client.register(phone, code, password);
    saveConfig({ base_url: client.baseUrl, token: data.token });
    process.stderr.write(
      `注册成功：赠送配额 ${data.gift_quota}，当前配额 ${data.quota_balance}；token 已保存到配置文件\n`);
    return { phone, quota_balance: data.quota_balance, gift_quota: data.gift_quota };
  } finally {
    rl.close();
  }
}

module.exports = { createRl, ask, askHidden, runRegister, PHONE_RE, PASSWORD_RE };
