#!/usr/bin/env node
/**
 * zentao-login.js — 启动 Playwright 浏览器 + 登录禅道，输出 WS endpoint
 *
 * 用法:
 *   node zentao-login.js [--account=wyhe] [--password=***] [--zentao-url=http://zentao.gxatek.com:20080] [--port=9224]
 *
 * 输出 (stdout):
 *   WS=ws://localhost:{port}/devtools/browser/{id}
 *   PID={pid}
 *
 * 此脚本保持运行直到被 kill，期间 browser 持续可用。
 * 其他脚本通过 WS endpoint + chromium.connectOverCDP() 复用同一 browser session。
 */

const { chromium } = require('playwright');
const http = require('http');

function parseArgs() {
  const args = process.argv.slice(2);
  const config = {
    account: 'wyhe',
    password: '',
    zentaoUrl: 'http://zentao.gxatek.com:20080',
    port: 9224,
  };
  for (const arg of args) {
    if (arg.startsWith('--account=')) config.account = arg.split('=')[1];
    if (arg.startsWith('--password=')) config.password = arg.split('=')[1];
    if (arg.startsWith('--zentao-url=')) config.zentaoUrl = arg.split('=')[1];
    if (arg.startsWith('--port=')) config.port = parseInt(arg.split('=')[1], 10);
  }

  // 从配置文件读取密码（如果命令行未提供）
  if (!config.password) {
    const fs = require('fs');
    const path = require('path');
    const home = process.env.USERPROFILE || process.env.HOME;
    const workspaceDirs = [
      path.join(home, '.openclaw-auto-bug-analyze', 'workspace'),
      path.join(home, '.openclaw', 'workspace'),
    ];
    for (const dir of workspaceDirs) {
      const configPath = path.join(dir, 'bug-analyzer-config.json');
      if (fs.existsSync(configPath)) {
        const cfg = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
        if (cfg.zentao) {
          config.account = config.account || cfg.zentao.account;
          config.password = config.password || cfg.zentao.password;
          config.zentaoUrl = config.zentaoUrl || cfg.zentao.url;
        }
        break;
      }
    }
  }

  return config;
}

async function getWsEndpoint(port) {
  return new Promise((resolve, reject) => {
    const url = `http://localhost:${port}/json/version`;
    http.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => (data += chunk));
      res.on('end', () => {
        try {
          const json = JSON.parse(data);
          resolve(json.webSocketDebuggerUrl);
        } catch (e) {
          reject(new Error(`解析 CDP 响应失败: ${data}`));
        }
      });
    }).on('error', (e) => {
      reject(new Error(`无法连接 CDP (端口 ${port}): ${e.message}`));
    });
  });
}

async function main() {
  const config = parseArgs();

  if (!config.password) {
    console.error('[ERROR] 密码未提供，请通过 --password 参数或配置文件提供');
    process.exit(1);
  }

  console.error(`[INFO] 启动浏览器 (端口 ${config.port})...`);

  const browser = await chromium.launch({
    headless: true,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      `--remote-debugging-port=${config.port}`,
    ],
  });

  const context = await browser.newContext();
  const page = await context.newPage();

  try {
    console.error(`[INFO] 登录禅道: ${config.zentaoUrl}`);
    await page.goto(`${config.zentaoUrl}/user-login.html`, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.fill('#account', config.account);
    await page.fill('input[name="password"]', config.password);
    await page.click('#submit');
    await page.waitForTimeout(3000);

    // 检查登录是否成功
    const currentUrl = page.url();
    if (currentUrl.includes('user-login')) {
      const error = await page.$('.alert-danger, .help-block');
      let errorText = '未知错误';
      if (error) {
        errorText = (await error.textContent()).trim();
      }
      console.error(`[ERROR] 登录失败: ${errorText}`);
      await browser.close();
      process.exit(1);
    }
  } catch (err) {
    console.error(`[ERROR] 登录异常: ${err.message}`);
    await browser.close();
    process.exit(1);
  }

  // 获取 WS endpoint
  let wsEndpoint;
  try {
    wsEndpoint = await getWsEndpoint(config.port);
  } catch (e) {
    console.error(`[ERROR] 获取 WS endpoint 失败: ${e.message}`);
    await browser.close();
    process.exit(1);
  }

  // 输出到 stdout
  console.log(`WS=${wsEndpoint}`);
  console.log(`PID=${process.pid}`);

  console.error('[INFO] 浏览器已启动并登录成功');
  console.error(`[INFO] WS endpoint: ${wsEndpoint}`);
  console.error('[INFO] 保持运行中...按 Ctrl+C 或 kill 此进程关闭');

  // 保持进程运行
  process.on('SIGINT', async () => {
    console.error('[INFO] 收到 SIGINT，关闭浏览器...');
    await browser.close();
    process.exit(0);
  });

  process.on('SIGTERM', async () => {
    console.error('[INFO] 收到 SIGTERM，关闭浏览器...');
    await browser.close();
    process.exit(0);
  });

  // 防止进程退出
  await new Promise(() => {});
}

main().catch(async (err) => {
  console.error(`[ERROR] ${err.message}`);
  process.exit(1);
});
