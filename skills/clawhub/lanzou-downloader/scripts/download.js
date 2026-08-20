/**
 * 蓝奏云下载器 - 纯 Node.js 实现，零外部依赖，纯本地解析（不调用任何第三方服务）
 * 用法: node download.js <蓝奏云分享链接> [输出文件路径] [密码] [--select 目标...] [--sub-pwd 子文件夹密码]
 *   密码可选，若不提供且链接需要密码，会报错提示
 *   文件夹分享自动识别（蓝奏云分享仅含单层文件，子文件夹不参与分享；t==1 推广条目自动跳过）
 *   --select 支持文件名精确匹配 / * 通配符 / 多目标逗号分隔
 */

const https = require('https');
const http = require('http');
const fs = require('fs');
const vm = require('vm');
const url = require('url');
const path = require('path');
const zlib = require('zlib');

// ─── 工具函数 ───────────────────────────────────────────────

/** 去除 JavaScript 注释（块注释和行注释） */
function stripJsComments(code) {
  return code
    .replace(/\/\*[\s\S]*?\*\//g, '')  // 去除 /* ... */
    .replace(/\/\/.*$/gm, '');          // 去除 //
}

function request(method, targetUrl, opts = {}) {
  const { cookieJar = {}, body, redirectCount = 0, encoding = null } = opts;
  if (redirectCount > 8) return Promise.reject(new Error('重定向次数过多'));

  return new Promise((resolve, reject) => {
    const u = new URL(targetUrl);
    const mod = u.protocol === 'https:' ? https : http;
    const headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
      ...opts.headers,
    };

    // 组装 Cookie
    const mergedCookies = { ...cookieJar };
    if (headers['Cookie']) {
      headers['Cookie'].split(';').forEach(p => {
        const eq = p.indexOf('=');
        if (eq > 0) mergedCookies[p.substring(0, eq).trim()] = p.substring(eq + 1).trim();
      });
    }
    const cookieStr = Object.entries(mergedCookies).map(([k,v]) => `${k}=${v}`).join('; ');
    if (cookieStr) headers['Cookie'] = cookieStr;

    if (body) {
      headers['Content-Length'] = Buffer.byteLength(body);
    }

    const reqOpts = {
      hostname: u.hostname,
      port: u.port || (u.protocol === 'https:' ? 443 : 80),
      path: u.pathname + u.search,
      method,
      headers,
      rejectUnauthorized: false,
    };

    const req = mod.request(reqOpts, (res) => {
      // 解析 set-cookie
      const setCookies = res.headers['set-cookie'];
      if (setCookies) {
        setCookies.forEach(c => {
          const semi = c.indexOf(';');
          const pair = semi > 0 ? c.substring(0, semi) : c;
          const eq = pair.indexOf('=');
          if (eq > 0) mergedCookies[pair.substring(0, eq).trim()] = pair.substring(eq + 1).trim();
        });
      }

      // 处理重定向
      if ([301, 302, 303, 307, 308].includes(res.statusCode) && res.headers.location) {
        const loc = new URL(res.headers.location, targetUrl).href;
        return resolve(request(method, loc, { ...opts, cookieJar: mergedCookies, redirectCount: redirectCount + 1 }));
      }

      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => {
        let raw = Buffer.concat(chunks);
        const ce = res.headers['content-encoding'];
        if (ce === 'gzip') raw = zlib.gunzipSync(raw);
        else if (ce === 'deflate') raw = zlib.inflateSync(raw);

        let text = raw.toString('utf8');

        // 非文本内容检测
        if (text.length > 0 && text.length < raw.length * 0.8) {
          text = '';
        }

        resolve({
          status: res.statusCode,
          headers: res.headers,
          body: text,
          raw,
          cookies: mergedCookies,
          url: targetUrl,
        });
      });
    });

    req.on('error', reject);
    req.setTimeout(30000, () => { req.destroy(); reject(new Error('请求超时')); });
    if (body) req.write(body);
    req.end();
  });
}

function streamDownload(targetUrl, filePath, opts = {}) {
  return new Promise((resolve, reject) => {
    const baseHeaders = {
      'User-Agent': 'Mozilla/5.0',
      'Accept': '*/*',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Referer': opts.referer || '',
    };

    const doAttempt = (attempt) => {
      const followRedirect = (url, redirects) => {
        if (redirects > 8) return Promise.reject(new Error('重定向次数过多'));
        const u = new URL(url);
        const mod = u.protocol === 'https:' ? https : http;
        // 重定向后（可能跳到 CDN 如 webgetstore.com），清除跨域 Referer 防防盗链断流
        const hdrs = { ...baseHeaders };
        if (redirects > 0) delete hdrs['Referer'];
        return new Promise((res, rej) => {
          const r = mod.request({
            hostname: u.hostname,
            port: u.port || (u.protocol === 'https:' ? 443 : 80),
            path: u.pathname + u.search,
            method: 'GET',
            headers: hdrs,
            rejectUnauthorized: false,
          }, (rs) => res(rs));
          r.on('error', rej);
          r.setTimeout(15000, () => { r.destroy(); rej(new Error('超时')); });
          r.end();
        }).then((rs) => {
          if ([301, 302, 303, 307, 308].includes(rs.statusCode) && rs.headers.location) {
            return followRedirect(new URL(rs.headers.location, url).href, redirects + 1);
          }
          return rs;
        });
      };

      followRedirect(targetUrl, 0).then((resp) => {
        if (resp.statusCode >= 400) throw new Error(`下载失败: HTTP ${resp.statusCode}`);
        const total = parseInt(resp.headers['content-length'] || '0', 10);
        let written = 0;
        const file = fs.createWriteStream(filePath);
        return new Promise((res, rej) => {
          const onError = (e) => { file.destroy(); rej(e); };
          resp.on('error', onError);
          resp.on('aborted', () => onError(new Error('连接被服务器中断')));
          file.on('error', onError);
          resp.on('data', (c) => { written += c.length; });
          file.on('finish', () => {
            if (total > 0 && written !== total) {
              file.destroy();
              rej(new Error(`下载不完整: 期望 ${total} 字节, 实际 ${written} 字节`));
              return;
            }
            res(written);
          });
          resp.pipe(file);
        });
      }).then((size) => {
        resolve(size);
      }).catch((e) => {
        if (attempt < 3) {
          console.log(`    ⚠ 下载中断 (${e.message})，自动重试 ${attempt + 1}/3 ...`);
          return doAttempt(attempt + 1);
        }
        reject(e);
      });
    };

    doAttempt(0);
  });
}

// ─── 密码处理 ───────────────────────────────────────────────

/**
 * 检测页面是否需要密码，如果需要则提交密码并获取真实下载地址
 * @returns {{ needsPwd: boolean, fullDownUrl: string | null, fileName: string | null, error: string | null }}
 */
async function handlePassword(lanzouUrl, cookies, body, password) {
  const hasPwd = body.includes('passwddiv');
  if (!hasPwd) return { needsPwd: false, fullDownUrl: null, fileName: null, error: null };

  if (!password) {
    return { needsPwd: true, fullDownUrl: null, fileName: null, error: '此链接需要密码，请在命令中提供密码参数' };
  }

  console.log('\n[3/6] 检测到密码保护，提交密码...');

  // 提取 fid
  const fidMatch = body.match(/ajaxm\.php\?file=(\d+)/);
  if (!fidMatch) return { needsPwd: true, fullDownUrl: null, fileName: null, error: '无法提取文件 ID' };
  const fid = fidMatch[1];
  console.log(`  fid: ${fid}`);

  // 提取 kdns
  const kdnsMatch = body.match(/var\s+kdns\s*=\s*(\d+)/);
  const kdns = kdnsMatch ? kdnsMatch[1] : '1';
  console.log(`  kdns: ${kdns}`);

  // 提取 sign（去除 JS 注释后匹配）
  const downPStart = body.indexOf('function down_p()');
  const downPEnd = body.indexOf('</script>', downPStart);
  let downPBody = body.substring(downPStart, downPEnd);
  downPBody = stripJsComments(downPBody);

  const signMatch = downPBody.match(/sign':'([^']+)'/);
  if (!signMatch) return { needsPwd: true, fullDownUrl: null, fileName: null, error: '无法提取 sign 参数' };
  const sign = signMatch[1];
  console.log(`  sign: ${sign.substring(0, 16)}...`);

  // POST 密码
  const pwdUrl = new URL(`/ajaxm.php?file=${fid}`, lanzouUrl).href;
  const postData = new URLSearchParams({
    action: 'downprocess',
    sign: sign,
    kd: kdns,
    p: password,
  }).toString();

  console.log(`  提交密码到: ${pwdUrl}`);
  const pwdResp = await request('POST', pwdUrl, {
    cookieJar: cookies,
    headers: {
      'Referer': lanzouUrl,
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-Requested-With': 'XMLHttpRequest',
    },
    body: postData,
  });

  try {
    const json = JSON.parse(pwdResp.body);
    console.log(`  服务器响应: zt=${json.zt}`);

    if (json.zt !== 1) {
      return { needsPwd: true, fullDownUrl: null, fileName: null, error: `密码错误或验证失败: ${json.inf || '未知原因'}` };
    }

    const dom = json.dom.replace(/\\\//g, '/');
    const fileUrl = json.url.replace(/\\\//g, '/');
    const fullDownUrl = dom + '/file/' + fileUrl;
    const fileName = json.inf || null;

    console.log(`  文件名: ${fileName}`);
    console.log(`  下载地址: ${fullDownUrl.substring(0, 80)}...`);

    return { needsPwd: true, fullDownUrl, fileName, error: null };
  } catch (e) {
    console.error('  密码响应:', pwdResp.body.substring(0, 300));
    return { needsPwd: true, fullDownUrl: null, fileName: null, error: `密码验证响应解析失败: ${e.message}` };
  }
}

// ─── 文件夹分享下载（本地解析，嵌套递归）────────────────────

/** 执行反爬 JS，计算 acw_sc__v2 并合并进 cookieJar */
function computeAcw(body, cookieJar) {
  const scriptMatch = body.match(/<script>([\s\S]*?)<\/script>/);
  if (!scriptMatch || !body.includes('arg1=')) return cookieJar;
  const fakeDoc = { cookie: '', location: { reload: () => {} } };
  const ctx = vm.createContext({ document: fakeDoc, Date, console: { log: () => {}, error: () => {}, warn: () => {} } });
  try { vm.runInContext(scriptMatch[1], ctx, { timeout: 5000 }); } catch (e) {}
  if (fakeDoc.cookie) {
    const parts = fakeDoc.cookie.split(';')[0].split('=');
    if (parts.length >= 2) cookieJar[parts[0].trim()] = parts.slice(1).join('=').trim();
  }
  return cookieJar;
}

/** 带反爬自动重试的请求：响应为反爬页时计算 cookie 重试一次 */
async function reqWithAcw(method, url, opts = {}) {
  let resp = await request(method, url, opts);
  if (resp.body.includes('arg1=')) {
    const newCookies = computeAcw(resp.body, { ...opts.cookieJar });
    resp = await request(method, url, { ...opts, cookieJar: newCookies });
    if (resp.body.includes('arg1=')) throw new Error(`反爬未通过: ${url.substring(0, 60)}`);
  }
  return resp;
}

/**
 * 从 iframe 页 JS 中提取实际 ajax 接口路径（$.ajax({ url: '...' })）。
 * 不同域名/版本的蓝奏云 ajax 地址不一定是 /ajaxm.php，写死会返回 zt=0。
 * 找不到时回退 /ajaxm.php。
 */
function extractAjaxPath(iframeBody) {
  const cleaned = stripJsComments(iframeBody);
  const m1 = cleaned.match(/\$\.ajax\(\s*\{[^}]*?url\s*:\s*['"]([^'"]+)['"]/);
  if (m1 && m1[1]) return m1[1];
  const m2 = cleaned.match(/url\s*:\s*['"]([^'"]*ajax[^'"]*)['"]/);
  if (m2 && m2[1]) return m2[1];
  return '/ajaxm.php';
}

/** 解析文件夹内单个文件的直链并下载 */
async function downloadFile(fileId, baseOrigin, cookies, outPath) {
  try {
    const pageUrl = `${baseOrigin}/${fileId}`;
    const resp = await reqWithAcw('GET', pageUrl, { cookieJar: cookies });
    const body = resp.body;
    if (body.includes('arg1=')) throw new Error(`文件 ${fileId}: 反爬未通过`);
    const fnM = body.match(/src="([^"]*\/fn\?[^"]+)"/);
    if (!fnM) throw new Error(`文件 ${fileId}: 未找到下载入口`);
    const fnPath = fnM[1];
    // 提取真实 fid（POST 下载地址时使用）
    const fidMatch = body.match(/var\s+fid\s*=\s*(\d+)/);
    const fid = fidMatch ? fidMatch[1] : null;
    const fnResp = await reqWithAcw('GET', `${baseOrigin}${fnPath}`, { cookieJar: resp.cookies, headers: { 'Referer': pageUrl } });
    const fnBody = fnResp.body;
    const wpM = fnBody.match(/var\s+wp_sign\s*=\s*'([^']+)'/);
    const adM = fnBody.match(/var\s+ajaxdata\s*=\s*'([^']+)'/);
    const kdM = fnBody.match(/var\s+kdns\s*=\s*(\d+)/);
    if (!wpM || !adM) throw new Error(`文件 ${fileId}: fn 页参数提取失败`);
    const postData = new URLSearchParams({
      action: 'downprocess', websignkey: adM[1], signs: adM[1],
      sign: wpM[1], websign: '', kd: kdM ? kdM[1] : '1', ves: '1',
    }).toString();
    // ajax 接口路径从 fn 页 JS 动态提取（写死 /ajaxm.php 在某些域名会 zt=0）
    const ajaxUrl = new URL(extractAjaxPath(fnBody), baseOrigin);
    ajaxUrl.searchParams.set('file', fid || '0');
    const ajax = await reqWithAcw('POST', ajaxUrl.href, {
      cookieJar: fnResp.cookies,
      headers: {
        'Referer': `${baseOrigin}${fnPath}`, 'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded', 'X-Requested-With': 'XMLHttpRequest',
      },
      body: postData,
    });
    let json;
    try { json = JSON.parse(ajax.body); } catch (e) { throw new Error(`文件 ${fileId}: ajax 响应非 JSON`); }
    if (json.zt !== 1) throw new Error(`文件 ${fileId}: zt=${json.zt} ${json.inf || ''}`);
    const dom = json.dom.replace(/\\\//g, '/');
    const fileUrl = json.url.replace(/\\\//g, '/');
    const fullUrl = dom + '/file/' + fileUrl;
    const size = await streamDownload(fullUrl, outPath, { referer: fullUrl });
    return { name: json.inf || String(fileId), size };
  } catch (e) {
    throw e;
  }
}

// ─── 文件夹分享（嵌套递归 + 选择性下载）────────────────────

/** 从文件夹分享页 HTML 提取 filemoreajax 参数（fid/uid/puid/t/k） */
function extractFolderParams(body) {
  const fidM = body.match(/filemoreajax\.php\?file=(\d+)/);
  const uidM = body.match(/'uid':'(\d+)'/);
  const puidM = body.match(/'puid':'([^']+)'/);
  const tM = body.match(/var\s+\w+\s*=\s*'(\d{8,})'/);
  const kM = body.match(/var\s+\w+\s*=\s*'([a-f0-9]{32})'/);
  return {
    fid: fidM ? fidM[1] : null,
    uid: uidM ? uidM[1] : '',
    puid: puidM ? puidM[1] : '',
    t: tM ? tM[1] : '',
    k: kM ? kM[1] : '',
  };
}

/** 清理列表项名称（去 HTML 标签） */
function cleanItemName(n) {
  return (n.name_all || '').replace(/<[^>]+>/g, '').trim();
}

/** 正则转义（用于通配符匹配） */
function escapeRegExp(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

/** 匹配 --select 段与列表条目（按 id 短码 / 名称 / * 通配符） */
function matchItem(item, seg) {
  if (!seg) return false;
  if (item.id === seg) return true;
  const name = cleanItemName(item);
  if (name === seg) return true;
  if (seg.includes('*')) {
    const re = new RegExp('^' + seg.split('*').map(escapeRegExp).join('.*') + '$');
    return re.test(name) || re.test(item.id);
  }
  return false;
}

/**
 * 列出文件夹某一层（filemoreajax，自动翻页）。
 * @returns {{ files: Array, folders: Array }} t==0 为文件、t==1 为子文件夹
 */
async function listFolder(baseOrigin, referer, params, cookies, pwd) {
  const PAGE_SIZE = 50;
  const all = [];
  let page = 1;
  while (page <= 50) {
    const postData = new URLSearchParams({
      lx: '2', fid: params.fid, uid: params.uid, puid: params.puid,
      pg: String(page), rep: '0', t: params.t, k: params.k, up: '1', ls: '1', pwd: pwd || '',
    }).toString();
    let listJson;
    try {
      const listResp = await reqWithAcw('POST', `${baseOrigin}/filemoreajax.php?file=${params.fid}`, {
        cookieJar: cookies,
        headers: {
          'Referer': referer, 'Accept': 'application/json, text/javascript, */*; q=0.01',
          'Content-Type': 'application/x-www-form-urlencoded', 'X-Requested-With': 'XMLHttpRequest',
        },
        body: postData,
      });
      listJson = JSON.parse(listResp.body);
      if (String(listJson.zt) !== '1') throw new Error(`zt=${listJson.inf || '未知'}`);
    } catch (e) {
      if (page === 1) throw e;
      console.log(`  第 ${page} 页获取失败 (${e.message})，停止翻页`);
      break;
    }
    const items = (listJson.text || []).filter(n => n.id && n.id !== '-1');
    all.push(...items);
    if (items.length < PAGE_SIZE) break;
    page++;
  }
  return { files: all.filter(n => n.t != 1), folders: all.filter(n => n.t == 1) };
}

/**
 * 递归收集要下载的文件（支持嵌套子文件夹）。
 * @param {string} baseOrigin 分享域名源
 * @param {string} folderUrl  当前文件夹页面 URL
 * @param {Object} cookies    cookie jar
 * @param {string} body       当前文件夹页面 HTML
 * @param {string} pwd        当前文件夹密码
 * @param {string} subPwd     --sub-pwd 子文件夹密码（全局）
 * @param {Array|null} select --select 目标路径数组（如 ['b00XXXXXXX/ima.zip','分*.zip']）
 * @param {Array} results     收集结果 [{id,name,relDir,size}]
 * @param {string} relDir     相对输出根目录
 * @param {number} depth      递归深度保护
 */
async function collectFolder(baseOrigin, folderUrl, cookies, body, pwd, subPwd, select, results, relDir, depth) {
  if (depth > 10) throw new Error('嵌套层级过深（>10 层），停止递归');
  const params = extractFolderParams(body);
  if (!params.fid) throw new Error('未找到文件夹 ID');
  const list = await listFolder(baseOrigin, folderUrl, params, cookies, pwd);

  // select 目标拆段：'a/b.zip' -> ['a','b.zip']
  const selSegs = (select || []).map(s => s.split('/').filter(Boolean));

  // ── 文件（t==0）：匹配末级目标 ──
  for (const f of list.files) {
    if (select && !selSegs.some(segs => segs.length === 1 && matchItem(f, segs[0]))) continue;
    results.push({ id: f.id, name: cleanItemName(f) || f.id, relDir, size: f.size || '' });
  }

  // ── 子文件夹（t==1）──
  // 蓝奏云分享只含单层文件，子文件夹不参与分享（alist 官方文档确认）。
  // 列表中的 t==1 条目是蓝奏云插入的推广/广告内容（页面 JS 标记为 s_ad 推广），一律跳过不下载。
  for (const folder of list.folders) {
    const fname = cleanItemName(folder) || folder.id;
    console.log(`  ⏭ 跳过推广条目: ${fname}`);
  }
}

/** 文件夹分享：递归解析 → 选择性下载 */
async function folderDownload(lanzouUrl, cookies, body, password, outputPath, selectTargets, subPwd) {
  const baseOrigin = new URL(lanzouUrl).origin;
  console.log('\n[3/6] 检测到文件夹分享，解析文件列表...');
  if (!password && body.includes('passwddiv')) throw new Error('此文件夹需要密码，请提供密码参数');

  const results = [];
  await collectFolder(baseOrigin, lanzouUrl, cookies, body, password || '', subPwd, selectTargets, results, '', 0);

  if (!results.length) throw new Error('没有匹配到任何文件（检查 --select 目标是否正确）');
  const mode = selectTargets ? '选择性' : '全部';
  console.log(`  [${mode}] 共 ${results.length} 个文件:`);
  results.forEach(r => console.log(`    - ${r.relDir ? r.relDir + '/' : ''}${r.name} (${r.size})`));

  const outDir = outputPath || path.join(process.cwd(), 'lanzou_folder');
  fs.mkdirSync(outDir, { recursive: true });

  let ok = 0, fail = 0;
  for (const f of results) {
    const dir = path.join(outDir, f.relDir);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    const safeName = f.name.replace(/[\\/:*?"<>|]/g, '_');
    const outFile = path.join(dir, safeName);
    console.log(`\n  ▶ ${f.relDir ? f.relDir + '/' : ''}${f.name} ...`);
    try {
      const info = await downloadFile(f.id, baseOrigin, cookies, outFile);
      console.log(`    ✅ 完成 (${(info.size / 1048576).toFixed(1)} MB)`);
      ok++;
    } catch (e) {
      console.log(`    ❌ 失败: ${e.message}`);
      fail++;
    }
  }
  console.log(`\n✅ 文件夹下载完成: ${ok} 成功, ${fail} 失败`);
  console.log(`   输出目录: ${outDir}`);
  return outDir;
}

// ─── 主流程 ──────────────────────────────────────────────────


async function download(lanzouUrl, outputPath = null, password = null, selectTargets = null, subPwd = null) {
  console.log(`蓝奏云下载器启动`);
  console.log(`链接: ${lanzouUrl}`);
  if (password) console.log(`密码: ${'*'.repeat(password.length)}`);

  // Step 1: 访问分享页
  console.log('\n[1/5] 访问分享页...');
  let resp = await request('GET', lanzouUrl);
  console.log(`  状态: ${resp.status}, 大小: ${resp.body.length} 字节`);

  let cookies = resp.cookies;
  let body = resp.body;

  // Step 2: JS 反爬验证
  if (body.includes('arg1=')) {
    console.log('\n[2/5] 检测到 JS 反爬验证，计算 cookie...');
    const arg1Match = body.match(/var arg1='([^']+)'/);
    if (!arg1Match) throw new Error('无法提取 arg1');
    const arg1 = arg1Match[1];
    console.log(`  arg1: ${arg1.substring(0, 8)}... (${arg1.length} 字符)`);

    const scriptMatch = body.match(/<script>([\s\S]*?)<\/script>/);
    if (!scriptMatch) throw new Error('无法提取 JS 脚本');

    const fakeDoc = { cookie: '', location: { reload: () => {} } };
    const ctx = vm.createContext({
      document: fakeDoc,
      Date: Date,
      console: { log: () => {}, error: () => {}, warn: () => {} },
    });

    vm.runInContext(scriptMatch[1], ctx, { timeout: 5000 });

    if (fakeDoc.cookie) {
      const parts = fakeDoc.cookie.split(';')[0].split('=');
      if (parts.length >= 2) {
        cookies[parts[0].trim()] = parts.slice(1).join('=').trim();
        console.log(`  acw_sc__v2: ${cookies['acw_sc__v2']?.substring(0, 12)}...`);
      }
    } else {
      throw new Error('JS 执行后未获取到 cookie');
    }

    resp = await request('GET', lanzouUrl, { cookieJar: cookies });
    body = resp.body;
    console.log(`  重试后状态: ${resp.status}, 大小: ${body.length} 字节`);
  } else {
    console.log('\n[2/5] 无需 JS 反爬');
  }

  // Step 3: 文件夹分享检测（lx=2 目录，嵌套递归 + 选择性下载）
  if (body.includes('filemoreajax')) {
    return await folderDownload(lanzouUrl, cookies, body, password, outputPath, selectTargets, subPwd);
  }

  // Step 3: 密码处理（如果需要）
  let fullDownUrl = null;
  let fileName = null;

  try {
    const pwdResult = await handlePassword(lanzouUrl, cookies, body, password);
    if (pwdResult.error) throw new Error(pwdResult.error);
    if (pwdResult.fullDownUrl) {
      // 密码流程：直接跳到下载
      fullDownUrl = pwdResult.fullDownUrl;
      fileName = pwdResult.fileName;
    } else {
      // 无密码流程：继续解析 iframe
      console.log('\n[3/5] 解析下载页...');
      const iframeMatch = body.match(/<iframe[^>]*src=["']([^"']*)["']/i);
      if (!iframeMatch) throw new Error('未找到 iframe 下载入口');
      const iframeSrc = iframeMatch[1];
      console.log(`  iframe: ${iframeSrc.substring(0, 50)}...`);

      const fidMatch = body.match(/var\s+fid\s*=\s*(\d+)/);
      const fid = fidMatch ? fidMatch[1] : null;
      console.log(`  fid: ${fid}`);

      const titleMatch = body.match(/<title>([^<]+)<\/title>/);
      fileName = titleMatch ? titleMatch[1].replace(' - 蓝奏云', '').trim() : null;
      if (fileName) console.log(`  文件: ${fileName}`);

      // Step 4: 请求 iframe 获取 AJAX 参数（带反爬自动重试，iframe 页也可能有 arg1= 反爬）
      console.log('\n[4/5] 请求 AJAX 参数...');
      const iframeUrl = new URL(iframeSrc, resp.url).href;
      const iframeResp = await reqWithAcw('GET', iframeUrl, {
        cookieJar: cookies,
        headers: { 'Referer': resp.url },
      });

      const iframeBody = iframeResp.body;
      const ajaxMatch = iframeBody.match(/var\s+ajaxdata\s*=\s*'([^']*)'/);
      const signMatch = iframeBody.match(/var\s+wp_sign\s*=\s*'([^']*)'/);
      const kdnsMatch = iframeBody.match(/var\s+kdns\s*=\s*(\d+)/);

      if (!ajaxMatch || !signMatch) throw new Error('无法提取 AJAX 参数');
      const ajaxdata = ajaxMatch[1];
      const wpSign = signMatch[1];
      const kdns = kdnsMatch ? parseInt(kdnsMatch[1]) : 1;
      console.log(`  ajaxdata: ${ajaxdata}, kdns: ${kdns}`);

      // POST 获取真实下载地址（ajax 路径从 iframe JS 动态提取，不写死 /ajaxm.php）
      const ajaxUrl = new URL(extractAjaxPath(iframeBody), resp.url);
      ajaxUrl.searchParams.set('file', fid || '0');
      const postData = new URLSearchParams({
        action: 'downprocess',
        websignkey: ajaxdata,
        signs: ajaxdata,
        sign: wpSign,
        websign: '',
        kd: String(kdns),
        ves: '1',
      }).toString();

      const ajaxResp = await request('POST', ajaxUrl.href, {
        cookieJar: iframeResp.cookies,
        headers: {
          'Referer': iframeUrl,
          'Accept': 'application/json, text/javascript, */*; q=0.01',
          'Content-Type': 'application/x-www-form-urlencoded',
          'X-Requested-With': 'XMLHttpRequest',
        },
        body: postData,
      });

      let ajaxBody = ajaxResp.body;
      try {
        const json = JSON.parse(ajaxBody);
        console.log(`  zt: ${json.zt}, dom: ${json.dom}`);

        if (json.zt !== 1) throw new Error(`服务器返回 zt=${json.zt}（非成功状态）`);

        const dom = json.dom.replace(/\\\//g, '/');
        const fileUrl = json.url.replace(/\\\//g, '/');
        fullDownUrl = dom + '/file/' + fileUrl;
        console.log(`  下载地址: ${fullDownUrl.substring(0, 80)}...`);
      } catch (e) {
        console.error('  AJAX 响应:', ajaxBody.substring(0, 500));
        throw new Error(`解析下载地址失败: ${e.message}`);
      }
    }
  } catch (e) {
    throw e;
  }

  // Step 5: 流式下载
  const targetFile = outputPath || path.join(process.cwd(), fileName || 'download.zip');
  const dir = path.dirname(targetFile);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

  console.log(`\n[5/5] 下载文件 → ${targetFile}`);
  const size = await streamDownload(fullDownUrl, targetFile, {
    referer: lanzouUrl,
  });

  const sizeMB = (size / (1024 * 1024)).toFixed(1);
  console.log(`\n✅ 下载完成: ${path.basename(targetFile)} (${sizeMB} MB)`);
  console.log(`   路径: ${targetFile}`);
  return targetFile;
}

// ─── 入口 ────────────────────────────────────────────────────

const args = process.argv.slice(2);
if (args.length < 1 || !args.some(a => !a.startsWith('--'))) {
  console.error('用法: node download.js <蓝奏云链接> [输出文件路径] [密码] [--select 目标1,目标2] [--sub-pwd 子文件夹密码]');
  console.error('  密码可选，若链接需要密码而未提供，会报错提示');
  console.error('  --select: 只下载指定文件/子文件夹，支持相对路径(子文件夹/文件)、* 通配符，逗号分隔多个');
  console.error('    示例: --select "ima.plus-skill-v1.0.8.zip"  --select "b00XXXXXXX/*.zip"  --select "*.pdf,子文件夹/xxx.zip"');
  console.error('  --sub-pwd: 嵌套子文件夹的密码（子文件夹可能使用独立密码）');
  process.exit(1);
}

let inputUrl = null, outputFile = null, password = null, selectTargets = null, subPwd = null;
const positional = [];
for (let i = 0; i < args.length; i++) {
  const a = args[i];
  if (a === '--select') {
    selectTargets = (args[++i] || '').split(',').map(s => s.trim()).filter(Boolean);
  } else if (a === '--sub-pwd') {
    subPwd = args[++i] || null;
  } else {
    positional.push(a);
  }
}
inputUrl = positional[0];
outputFile = positional[1] || null;
password = positional[2] || null;

if (selectTargets) console.log(`--select: ${selectTargets.join(', ')}`);
if (subPwd) console.log(`--sub-pwd: ${'*'.repeat(subPwd.length)}`);

download(inputUrl, outputFile, password, selectTargets, subPwd).catch(err => {
  console.error(`\n❌ 错误: ${err.message}`);
  process.exit(1);
});
