const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const PORT = Number(process.env.PORT) || 3456;
const HOST = '127.0.0.1';
const WEREAD_API_KEY = process.env.WEREAD_API_KEY || '';
const HTML_FILE = path.join(__dirname, 'ai-reading-companion.html');
const PID_FILE = path.join(__dirname, '.server.pid');
const DATA_DIR = process.env.WEREAD_SOCRATES_DATA_DIR || path.join(process.env.HOME || __dirname, '.weread-socrates');
const MEMORY_FILE = path.join(DATA_DIR, 'reader-memory.json');
const MAX_BODY = 64 * 1024;
const SKILL_VERSION = '1.3.1';
const DELETE_TOKEN_TTL_MS = 60 * 1000;
const deleteTokens = new Map();
const WEREAD_OFFICIAL_SKILL_VERSION = '1.0.4';

const ALLOWED_APIS = {
  '/store/search': ['keyword', 'count'],
  '/book/info': ['bookId'],
  '/book/chapterinfo': ['bookId'],
  '/book/bestbookmarks': ['bookId', 'chapterUid', 'synckey'],
  '/book/bookmarklist': ['bookId'],
  '/review/list/mine': ['bookid', 'synckey', 'count'],
};
const MIME = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'application/javascript', '.svg': 'image/svg+xml', '.png': 'image/png' };
const DEMO_BOOK = { bookId: 'demo-socrates', title: '苏格拉底的申辩', author: '柏拉图', cover: '', newRating: 91, newRatingCount: 13842, intro: '苏格拉底在雅典法庭上的自我辩护，讨论未经审视的生活、知识的边界与公民责任。' };
const DEMO_CHAPTERS = [
  { chapterUid: 1, chapterIdx: 1, level: 1, title: '申辩：真正的智慧' },
  { chapterUid: 2, chapterIdx: 2, level: 1, title: '审判：法律与良知' },
  { chapterUid: 3, chapterIdx: 3, level: 1, title: '判决：死亡与善的生活' },
];
const DEMO_MARKS = [
  { chapterUid: 1, markText: '我所知道的，就是我一无所知。', totalCount: 12800 },
  { chapterUid: 1, markText: '未经审视的生活是不值得过的。', totalCount: 9600 },
  { chapterUid: 2, markText: '重要的不是活着，而是活得好。', totalCount: 7200 },
  { chapterUid: 3, markText: '一个好人无论生前死后都不会遭遇真正的恶。', totalCount: 4300 },
];

function json(res, status, data) {
  res.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff' });
  res.end(JSON.stringify(data));
}
function readJsonBody(req, res, done) {
  let body = '';
  let rejected = false;
  req.on('data', chunk => {
    if (rejected) return;
    body += chunk;
    if (Buffer.byteLength(body, 'utf8') > MAX_BODY) {
      rejected = true;
      json(res, 413, { ok: false, error: '请求体过大' });
      req.destroy();
    }
  });
  req.on('end', () => {
    if (rejected) return;
    try { done(JSON.parse(body || '{}')); }
    catch { json(res, 400, { ok: false, error: '请求体不是合法 JSON' }); }
  });
}
function ensureDataDir() { fs.mkdirSync(DATA_DIR, { recursive: true, mode: 0o700 }); }
function readMemory() {
  ensureDataDir();
  if (!fs.existsSync(MEMORY_FILE)) return { version: 1, entries: [] };
  try {
    const value = JSON.parse(fs.readFileSync(MEMORY_FILE, 'utf8'));
    return value && Array.isArray(value.entries) ? value : { version: 1, entries: [] };
  } catch { return { version: 1, entries: [] }; }
}
function writeMemory(memory) {
  ensureDataDir();
  const temp = MEMORY_FILE + '.tmp';
  fs.writeFileSync(temp, JSON.stringify(memory, null, 2), { mode: 0o600 });
  fs.renameSync(temp, MEMORY_FILE);
  try { fs.chmodSync(MEMORY_FILE, 0o600); } catch {}
}
function cleanText(value, max) { return String(value || '').replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, '').trim().slice(0, max); }
function memoryApi(req, res, url) {
  if (req.method === 'GET') return json(res, 200, readMemory());
  if (req.method === 'POST') return readJsonBody(req, res, parsed => {
    const allowedTypes = new Set(['concept', 'stance', 'question']);
    const entry = {
      id: Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 9),
      type: allowedTypes.has(parsed.type) ? parsed.type : 'concept',
      content: cleanText(parsed.content, 2000),
      bookId: cleanText(parsed.bookId, 200), bookTitle: cleanText(parsed.bookTitle, 200), author: cleanText(parsed.author, 200),
      tags: Array.isArray(parsed.tags) ? parsed.tags.slice(0, 12).map(tag => cleanText(tag, 50)).filter(Boolean) : [],
      createdAt: new Date().toISOString(),
    };
    if (!entry.content) return json(res, 400, { ok: false, error: '内容不能为空' });
    const memory = readMemory();
    memory.entries.unshift(entry);
    memory.entries = memory.entries.slice(0, 1000);
    writeMemory(memory);
    json(res, 201, { ok: true, entry });
  });
  if (req.method === 'DELETE') {
    const memory = readMemory();
    const id = cleanText(url.searchParams.get('id'), 100);
    if (!id) {
      const token = cleanText(req.headers['x-confirm-token'], 200);
      const expiresAt = deleteTokens.get(token);
      deleteTokens.delete(token);
      if (!expiresAt || expiresAt < Date.now()) return json(res, 403, { ok: false, error: '批量删除需要有效的一次性确认 token' });
    }
    memory.entries = id ? memory.entries.filter(entry => entry.id !== id) : [];
    writeMemory(memory);
    return json(res, 200, { ok: true, count: memory.entries.length });
  }
  return json(res, 405, { ok: false, error: 'Method Not Allowed' });
}
function demoWeread(apiName) {
  if (apiName === '/store/search') return { errcode: 0, results: [{ books: [{ bookInfo: DEMO_BOOK }] }], demo: true };
  if (apiName === '/book/info') return { errcode: 0, intro: DEMO_BOOK.intro, demo: true };
  if (apiName === '/book/chapterinfo') return { errcode: 0, chapters: DEMO_CHAPTERS, demo: true };
  if (apiName === '/book/bestbookmarks') return { errcode: 0, items: DEMO_MARKS, chapters: DEMO_CHAPTERS, demo: true };
  if (apiName === '/book/bookmarklist') return { errcode: 0, chapters: DEMO_CHAPTERS, updated: DEMO_MARKS.slice(0, 2).map((item, i) => ({ type: 1, markText: item.markText, chapterUid: item.chapterUid, createTime: 1700000000 + i * 86400 })), demo: true };
  if (apiName === '/review/list/mine') return { errcode: 0, reviews: [{ review: { abstract: DEMO_MARKS[1].markText, content: '我是否真的愿意检验那些最习以为常的判断？', chapterName: DEMO_CHAPTERS[0].title, chapterUid: 1, createTime: 1700200000 } }], demo: true };
  return { errcode: -1, errmsg: 'Demo 不支持该接口' };
}
function serveFile(res, filePath) {
  const ext = path.extname(filePath);
  res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream', 'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache', 'Expires': '0', 'X-Content-Type-Options': 'nosniff', 'Content-Security-Policy': "default-src 'self'; img-src 'self' https: data:; connect-src 'self' https://i.weread.qq.com https://open.bigmodel.cn https://api.deepseek.com; style-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'" });
  fs.createReadStream(filePath).pipe(res);
}
function proxyWeread(req, res) {
  readJsonBody(req, res, parsed => {
    const apiName = parsed.api_name;
    if (!Object.prototype.hasOwnProperty.call(ALLOWED_APIS, apiName)) return json(res, 403, { errcode: -1, errmsg: '不允许的接口: ' + apiName });
    const payload = { api_name: apiName };
    for (const field of ALLOWED_APIS[apiName]) if (parsed[field] !== undefined) payload[field] = parsed[field];
    payload.skill_version = WEREAD_OFFICIAL_SKILL_VERSION;
    if (!WEREAD_API_KEY) return json(res, 200, demoWeread(apiName));
    const proxy = https.request({ hostname: 'i.weread.qq.com', path: '/api/agent/gateway', method: 'POST', headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + WEREAD_API_KEY } }, pres => {
      let data = '';
      pres.on('data', chunk => { data += chunk; if (data.length > 4 * 1024 * 1024) proxy.destroy(); });
      pres.on('end', () => { res.writeHead(pres.statusCode, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' }); res.end(data); });
    });
    proxy.on('error', err => json(res, 502, { errcode: -1, errmsg: '微信读书接口不可达: ' + err.message }));
    proxy.end(JSON.stringify(payload));
  });
}

const server = http.createServer((req, res) => {
  const host = String(req.headers.host || "").toLowerCase();
  const allowedHosts = new Set(["localhost:" + PORT, "127.0.0.1:" + PORT]);
  if (!allowedHosts.has(host)) return json(res, 403, { ok: false, error: "Host 不允许" });
  const origin = String(req.headers.origin || "");
  if (origin && origin !== "http://localhost:" + PORT && origin !== "http://127.0.0.1:" + PORT) return json(res, 403, { ok: false, error: "Origin 不允许" });
  const url = new URL(req.url, 'http://localhost:' + PORT);
  if (req.method === 'OPTIONS') { res.writeHead(204); return res.end(); }
  if (url.pathname === '/api/weread' && req.method === 'POST') return proxyWeread(req, res);
  if (url.pathname === '/api/memory') {
    try { return memoryApi(req, res, url); }
    catch { return json(res, 500, { ok: false, error: '本地记忆读写失败' }); }
  }
  if (url.pathname === '/api/memory/delete-token' && req.method === 'POST') {
    const token = crypto.randomBytes(12).toString('hex');
    deleteTokens.set(token, Date.now() + DELETE_TOKEN_TTL_MS);
    for (const [value, expiresAt] of deleteTokens) if (expiresAt < Date.now()) deleteTokens.delete(value);
    return json(res, 200, { ok: true, token, expiresInSeconds: DELETE_TOKEN_TTL_MS / 1000 });
  }
  if (url.pathname === '/api/status' || url.pathname === '/api/diagnostics') {
    let memoryWritable = true;
    try { ensureDataDir(); fs.accessSync(DATA_DIR, fs.constants.R_OK | fs.constants.W_OK); } catch { memoryWritable = false; }
    return json(res, 200, { ok: true, mode: WEREAD_API_KEY ? 'live' : 'demo', weread: !!WEREAD_API_KEY, demo: !WEREAD_API_KEY, skillVersion: SKILL_VERSION, host: HOST, port: PORT, node: process.version, memory: { writable: memoryWritable, entries: readMemory().entries.length } });
  }
  const staticFiles = new Map([
    ["/", HTML_FILE],
    ["/ai-reading-companion.html", HTML_FILE],
    ["/app.css", path.join(__dirname, "app.css")],
    ["/app.js", path.join(__dirname, "app.js")],
  ]);
  const filePath = staticFiles.get(url.pathname);
  if (filePath && fs.existsSync(filePath)) return serveFile(res, filePath);
  res.writeHead(404); res.end("Not Found");
});
server.listen(PORT, HOST, () => {
  const url = 'http://localhost:' + PORT;
  console.log('AI 伴读服务已启动 v' + SKILL_VERSION + ' → ' + url + '（仅监听本机 ' + HOST + '）');
  console.log('运行模式: ' + (WEREAD_API_KEY ? '在线模式（微信读书 Key 已配置）' : 'Demo 模式（无需 Key）'));
  console.log('Reader Memory: ' + MEMORY_FILE);
  try { fs.writeFileSync(PID_FILE, String(process.pid)); } catch {}
  const shutdown = () => { try { fs.unlinkSync(PID_FILE); } catch {} server.close(() => process.exit(0)); };
  process.on('SIGTERM', shutdown); process.on('SIGINT', shutdown);
  console.log('请在浏览器中手动打开: ' + url);
});
