#!/usr/bin/env node
/* build_public.cjs */
const fs = require('fs');
const path = require('path');
const os = require('os');

const SRC = __dirname;
const BUILD = path.join(os.tmpdir(), 'shopping-price-compare-public');

// 排除：依赖、构建产物、本地运行时状态（token/偏好/日志/定期任务——均为用户隐私数据，绝不出包）
const EXCLUDE = new Set(['node_modules', 'dist', '.git', 'build_public.cjs', 'token.json', 'user_prefs.json', 'learning_log.json', 'recurring_tasks.json', '.session.json']);
function shouldSkip(name) {
  return EXCLUDE.has(name) || name.startsWith('_') || name.endsWith('.zip');
}

function copyDir(src, dst) {
  fs.mkdirSync(dst, { recursive: true });
  for (const e of fs.readdirSync(src, { withFileTypes: true })) {
    if (shouldSkip(e.name)) continue;
    const s = path.join(src, e.name), d = path.join(dst, e.name);
    if (e.isDirectory()) copyDir(s, d);
    else fs.copyFileSync(s, d);
  }
}

copyDir(SRC, BUILD);

const pricePath = path.join(BUILD, 'scripts', 'price.js');
let price = fs.readFileSync(pricePath, 'utf8');

// 1) 清空*** key 默认值：匹配 `= process.env.X || '...'`，把 `|| '...'` 改成 `|| ''`
const envDefaultRe = /(=\s*process\.env\.[A-Z_]+\s*)\|\|\s*'[^']*'/g;
price = price.replace(envDefaultRe, "$1|| ''");

// 2) 代理地址：默认保留源码中的值（零感知所需）；构建时给了 PUBLIC_PROXY_BASE 才覆盖
if (process.env.PUBLIC_PROXY_BASE) {
  price = price.replace(
    /const DEFAULT_PROXY_BASE\s*=\s*'[^']*';/,
    `const DEFAULT_PROXY_BASE = '${process.env.PUBLIC_PROXY_BASE}';`
  );
}

// 3) 代理访问令牌：发布包严禁含*** token，运行时由 /register 自动获得
price = price.replace(
  /const DEFAULT_PROXY_TOKEN\s*=\s*'[^']*';/,
  "const DEFAULT_PROXY_TOKEN = '';"
);

fs.writeFileSync(pricePath, price, 'utf8');

// 4) 校验：*** key / 代理 token 任一残留即报错退出（代理地址 URL 允许，不在此列）
const LEAK_PATTERNS = [
  /75958cddff60408682aeec6eba7882ed/, // quotaApi APPKEY
  /mm_871500182_1916650368_110669250195/, // quotaApi PID
  /5B1114EEDB94/, // shortVideoApi APIKEY
  /1003134917/, // 京东 unionId
  /61713/, // 唯品会 SID
  /190511/, // quotaApi SID
  /shengsheng_proxy_8Kd2mPqL9vN3tR7x/, // 代理令牌（***不会进包）
];
const leaked = LEAK_PATTERNS.filter((re) => re.test(price));

console.log('构建目录:', BUILD);
console.log('DEFAULT_PROXY_BASE =', (price.match(/const DEFAULT_PROXY_BASE\s*=\s*'([^']*)'/))[1] || '(空，需用户配 SHENGSENG_API_BASE)');
if (leaked.length) {
  console.error('❌ 发布包仍存在残留内容：', leaked.map((r) => r.source));
  process.exit(1);
}
console.log('✅ 平台 key / 代理 token 均已清空，已清空（代理地址 URL 已保留以供零感知）');
console.log('\n下一步打包：');
console.log(`python3 "D:/Program Files (x86)/WORKBUDD//resources/app.asar.unpacked/resources/builtin-skills/skill-creator/scripts/package_skill.py" "${BUILD}" "C:/Users/Administrator/.workbuddy/skills/dist" --name shengsheng-price.public`);
