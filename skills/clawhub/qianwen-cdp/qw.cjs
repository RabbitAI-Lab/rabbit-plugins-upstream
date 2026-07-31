'use strict';
/**
 * qw.cjs — 千问浏览器原生 CDP 驱动（绕过 agent-browser 的 --cdp 限制）
 *
 * 关键结论（已验证）：
 *   千问对已存在的页面 target 做外部 CDP 调用会静默/挂死，但用 browser 级 WS
 *   调 Target.createTarget 自己新建的页面 target 完全可控（Runtime/DOM/Input 均可用）。
 *   因此本工具一律「自建新 tab」来驱动，登录态由真实 profile 保留。
 *
 * 用法：
 *   node qw.cjs ensure                      确保千问 CDP 实例在跑（无则拉起真实 profile @9666）
 *   node qw.cjs open <url>                  新建 tab 并导航，输出 targetId
 *   node qw.cjs navigate <id> <url>         已有 tab 导航
 *   node qw.cjs eval <id> <js表达式>        执行 JS，输出返回值
 *   node qw.cjs snapshot <id> [selector]    取页面简化快照（文本/链接/输入）
 *   node qw.cjs click <id> <css选择器>      点击元素
 *   node qw.cjs type <id> <css选择器> <文本> 向输入框填入文本
 *   node qw.cjs screenshot <id> [out.png]   截图
 *   node qw.cjs list                        列出当前所有 target
 *   node qw.cjs close <id>                  关闭 tab
 *   node qw.cjs relaunch                    实例挂掉时：taskkill + 重拉 9666
 *
 * 环境变量（均可选，不设置则用默认值）：
 *   QW_EXE      千问可执行文件路径
 *   QW_PROFILE  千问用户数据目录（含登录态）
 *   QW_CDP_PORT CDP 调试端口（默认 9666）
 */

// WebSocket 依赖：优先用本地安装的 ws，找不到则回退到 xbrowser 自带的（兼容原机）
let WebSocket;
try {
  WebSocket = require('ws');
} catch {
  WebSocket = require('C:/Users/SZTSY/.workbuddy/skills/xbrowser/scripts/src/node_modules/ws');
}

const http = require('http');
const fs = require('fs');

const QW_EXE = process.env.QW_EXE
  || 'C:\\Users\\SZTSY\\AppData\\Local\\Programs\\QianwenApp\\qianwen.exe';
const QW_PROFILE = process.env.QW_PROFILE
  || 'C:/Users/SZTSY/AppData/Local/Qianwen/User Data';
const CDP_PORT = parseInt(process.env.QW_CDP_PORT || '9666', 10);
const PROBE_TIMEOUT = 12000;

// ---------------------------------------------------------------------------
function httpGet(path) {
  return new Promise((resolve, reject) => {
    const req = http.get({ host: '127.0.0.1', port: CDP_PORT, path, timeout: 4000 }, (res) => {
      let d = '';
      res.on('data', (c) => (d += c));
      res.on('end', () => { try { resolve(JSON.parse(d)); } catch (e) { reject(e); } });
    });
    req.on('error', reject);
    req.on('timeout', () => { req.destroy(); reject(new Error('http timeout ' + path)); });
  });
}

function newWs(url) {
  return new Promise((resolve, reject) => {
    const ws = new WebSocket(url);
    ws.on('open', () => resolve(ws));
    ws.on('error', reject);
  });
}

// 在指定 ws 上发 CDP 命令并等待结果
function cdp(ws, method, params = {}, timeout = 10000) {
  return new Promise((resolve, reject) => {
    const id = Math.floor(Math.random() * 1e9);
    const timer = setTimeout(() => { ws.removeListener('message', onMsg); reject(new Error('cdp timeout: ' + method)); }, timeout);
    const onMsg = (raw) => {
      let m; try { m = JSON.parse(raw); } catch { return; }
      if (m.id === id) { clearTimeout(timer); ws.removeListener('message', onMsg); resolve(m); }
    };
    ws.on('message', onMsg);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

// 同 cdp，但返回 m.result（多数 CDP 命令的结果都嵌在 result 里）
function cdpR(ws, method, params = {}, timeout = 10000) {
  return cdp(ws, method, params, timeout).then((m) => m.result);
}

async function getBrowserWs() {
  const ver = await httpGet('/json/version');
  return newWs(ver.webSocketDebuggerUrl);
}

async function getTargetWs(targetId) {
  const list = await httpGet('/json/list');
  const t = list.find((x) => x.id === targetId);
  if (!t || !t.webSocketDebuggerUrl) throw new Error('找不到 target ' + targetId + ' 的 ws');
  return newWs(t.webSocketDebuggerUrl);
}

// ---------------------------------------------------------------------------
// 确保千问 CDP 实例在跑（真实 profile，固定端口）
async function ensureInstance() {
  try {
    await httpGet('/json/version');
    return { ok: true, alreadyUp: true };
  } catch {
    // 没在跑 → 拉起（不在此处杀进程，交给调用方/人工）
    const { spawn } = require('child_process');
    const child = spawn(QW_EXE, [
      '--remote-debugging-port=' + CDP_PORT,
      '--user-data-dir=' + QW_PROFILE,
      '--no-first-run', '--no-default-browser-check',
    ], { detached: true, stdio: 'ignore' });
    child.unref();
    // 等待 CDP 就绪
    const deadline = Date.now() + PROBE_TIMEOUT;
    while (Date.now() < deadline) {
      try { await httpGet('/json/version'); return { ok: true, alreadyUp: false, launched: true }; }
      catch { await new Promise((r) => setTimeout(r, 500)); }
    }
    throw new Error('千问拉起后 CDP 未在 ' + PROBE_TIMEOUT + 'ms 内就绪');
  }
}

// 新建 tab 并导航，返回 targetId
async function openTab(url) {
  const bws = await getBrowserWs();
  const { targetId } = await cdpR(bws, 'Target.createTarget', { url });
  bws.close();
  // 等待加载
  await new Promise((r) => setTimeout(r, 2500));
  return targetId;
}

async function navigate(targetId, url) {
  const tws = await getTargetWs(targetId);
  await cdp(tws, 'Page.enable');
  await cdp(tws, 'Page.navigate', { url });
  tws.close();
  await new Promise((r) => setTimeout(r, 2500));
}

async function evalJS(targetId, expr) {
  const tws = await getTargetWs(targetId);
  await cdp(tws, 'Runtime.enable');
  const r = await cdpR(tws, 'Runtime.evaluate', { expression: expr, returnByValue: true });
  tws.close();
  return r;
}

// 简化快照：标题 + 可见文本片段 + 链接 + 输入框
async function snapshot(targetId, selector) {
  const tws = await getTargetWs(targetId);
  await cdp(tws, 'Runtime.enable');
  const expr = `
  (function(){
    var root = ${selector ? `document.querySelector(${JSON.stringify(selector)})` : 'document.body'};
    if(!root) return {error:'no element'};
    var text = (root.innerText||'').replace(/\\s+/g,' ').trim().slice(0,2000);
    var links = [].slice.call(root.querySelectorAll('a')).slice(0,30).map(function(a){return {t:a.innerText.trim().slice(0,60), h:a.href};});
    var inputs = [].slice.call(root.querySelectorAll('input,textarea')).slice(0,20).map(function(i){return {type:i.type||i.tagName, name:i.name||i.id, placeholder:i.placeholder||'', value:i.value||''};});
    return {title:document.title, text:text, links:links, inputs:inputs};
  })()`;
  const r = await cdp(tws, 'Runtime.evaluate', { expression: expr, returnByValue: true });
  tws.close();
  return r.result;
}

async function click(targetId, selector) {
  const tws = await getTargetWs(targetId);
  await cdp(tws, 'Runtime.enable');
  const expr = `
  (function(){
    var el = document.querySelector(${JSON.stringify(selector)});
    if(!el) return {ok:false, error:'no element '+${JSON.stringify(selector)}};
    el.scrollIntoView({block:'center'});
    var r = el.getBoundingClientRect();
    return {ok:true, x:r.x+r.width/2, y:r.y+r.height/2};
  })()`;
  const r = await cdpR(tws, 'Runtime.evaluate', { expression: expr, returnByValue: true });
  tws.close();
  if (!r || !r.value || !r.value.ok) return r;
  const { x, y } = r.value;
  // 用 Input 域点击坐标（需重连开启 Input）
  const tws2 = await getTargetWs(targetId);
  await cdp(tws2, 'Input.enable');
  await cdp(tws2, 'Input.dispatchMouseEvent', { type: 'mousePressed', x, y, button: 'left', clickCount: 1 });
  await cdp(tws2, 'Input.dispatchMouseEvent', { type: 'mouseReleased', x, y, button: 'left', clickCount: 1 });
  tws2.close();
  await new Promise((res) => setTimeout(res, 800));
  return { ok: true, x, y };
}

async function typeText(targetId, selector, text) {
  const tws = await getTargetWs(targetId);
  await cdp(tws, 'Runtime.enable');
  const focusExpr = `
  (function(){
    var el = document.querySelector(${JSON.stringify(selector)});
    if(!el) return {ok:false};
    el.focus(); el.value=''; return {ok:true};
  })()`;
  await cdp(tws, 'Runtime.evaluate', { expression: focusExpr, returnByValue: true });
  tws.close();
  const tws2 = await getTargetWs(targetId);
  await cdp(tws2, 'Input.enable');
  for (const ch of text) {
    await cdp(tws2, 'Input.insertText', { text: ch });
  }
  tws2.close();
  await new Promise((res) => setTimeout(res, 300));
  return { ok: true };
}

async function screenshot(targetId, out) {
  const tws = await getTargetWs(targetId);
  await cdp(tws, 'Page.enable');
  const r = await cdpR(tws, 'Page.captureScreenshot', { format: 'png', captureBeyondViewport: true });
  tws.close();
  const data = r.data;
  const file = out || ('qw_shot_' + targetId + '.png');
  fs.writeFileSync(file, Buffer.from(data, 'base64'));
  return { ok: true, file };
}

async function listTargets() {
  return httpGet('/json/list');
}

async function closeTab(targetId) {
  const bws = await getBrowserWs();
  await cdp(bws, 'Target.closeTarget', { targetId });
  bws.close();
  return { ok: true };
}

// ---------------------------------------------------------------------------
async function main() {
  const [cmd, ...args] = process.argv.slice(2);
  let out;
  switch (cmd) {
    case 'ensure': out = await ensureInstance(); break;
    case 'relaunch':
      // 实例挂掉/锁住时：杀掉占用真实 profile 的千问主进程（WpkService 孤儿杀不掉就留着），再拉起
      try { require('child_process').execSync('taskkill /F /IM qianwen.exe', { stdio: 'ignore' }); } catch {}
      await new Promise((r) => setTimeout(r, 2500));
      out = await ensureInstance();
      break;
    case 'open': out = { targetId: await openTab(args[0]) }; break;
    case 'navigate': await navigate(args[0], args[1]); out = { ok: true }; break;
    case 'eval': out = await evalJS(args[0], args.slice(1).join(' ')); break;
    case 'snapshot': out = await snapshot(args[0], args[1]); break;
    case 'click': out = await click(args[0], args[1]); break;
    case 'type': out = await typeText(args[0], args[1], args.slice(2).join(' ')); break;
    case 'screenshot': out = await screenshot(args[0], args[1]); break;
    case 'list': out = await listTargets(); break;
    case 'close': out = await closeTab(args[0]); break;
    default: out = { error: 'unknown command: ' + cmd }; break;
  }
  console.log(JSON.stringify(out, null, 2));
}

main().catch((e) => { console.error('ERR', e.message || e); process.exit(1); });
