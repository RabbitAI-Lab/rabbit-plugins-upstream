/**
 * GEO 品牌诊断采集脚本
 * 
 * 使用方法：
 *   node collect.js <品牌> <行业> <城市> [场景数]
 * 
 * 示例：
 *   node collect.js 漳州客家宴 餐饮 漳州 5
 *   node collect.js 牙博士口腔 医疗 漳州 5
 * 
 * 流程：
 *   1. 启动 Chrome → 自动打开3个平台标签页
 *   2. 用户手动登录（只需一次，之后自动复用）
 *   3. 按 Enter → 全自动采集 + 生成诊断报告
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const genReportDocx = require('./gen-docx.js');

// ============== 参数 ==============
const BRAND    = process.argv[2] || '漳州客家宴';
const INDUSTRY = process.argv[3] || '餐饮';
const LOCATION = process.argv[4] || '漳州';
const N        = Math.min(parseInt(process.argv[5] || '5', 10), 10);
const PROFILE  = path.join(__dirname, '.chrome-profile');
const OUTPUT_JSON  = path.join(__dirname, '..', 'reports', `geo_${BRAND}.json`);
const OUTPUT_MD    = path.join(__dirname, '..', 'reports', `诊断报告_${BRAND}.md`);

// ============== 平台 ==============
const PLATFORMS = [
  { id:'doubao',  name:'豆包',     url:'https://www.doubao.com',       icon:'🫘' },
  { id:'yuanbao', name:'元宝',     url:'https://yuanbao.tencent.com',  icon:'💎' },
  { id:'tongyi',  name:'通义千问', url:'https://tongyi.aliyun.com',   icon:'🌤️' },
];

// ============== 行业场景模板 ==============
const SCENARIO_TPL = {
  '餐饮': [
    { id:'s1', q:'{c}哪里吃{p}好吃？' },
    { id:'s2', q:'{c}靠谱的{p}推荐' },
    { id:'s3', q:'{b}怎么样？好吃吗？' },
    { id:'s4', q:'{c}{b}人均消费多少？' },
    { id:'s5', q:'{b}和同类餐厅比有什么特色？' },
    { id:'s6', q:'{c}本地人推荐的{p}' },
    { id:'s7', q:'{c}{p}排行榜' },
  ],
  '装修': [
    { id:'s1', q:'{c}装修公司哪家好？' },
    { id:'s2', q:'{c}靠谱的装修公司' },
    { id:'s3', q:'{b}怎么样？靠谱吗？' },
    { id:'s4', q:'{b}装修报价多少一平米？' },
    { id:'s5', q:'{b}和{comp}比哪个好？' },
  ],
  '智能家居': [
    { id:'s1', q:'{c}智能家居公司哪家好？' },
    { id:'s2', q:'{c}靠谱的智能家居品牌' },
    { id:'s3', q:'{b}怎么样？好用吗？' },
    { id:'s4', q:'{b}全屋智能家居多少钱？' },
    { id:'s5', q:'{b}和小米/华为智能家居比哪个好？' },
  ],
  '医疗': [
    { id:'s1', q:'{c}牙科医院哪家好？' },
    { id:'s2', q:'{c}靠谱的口腔诊所' },
    { id:'s3', q:'{b}怎么样？正规吗？' },
    { id:'s4', q:'{b}种植牙多少钱？' },
    { id:'s5', q:'{b}和公立医院比怎么样？' },
  ],
  '科技': [
    { id:'s1', q:'{c}科技公司哪家好？' },
    { id:'s2', q:'{c}靠谱的AI公司' },
    { id:'s3', q:'{b}怎么样？' },
    { id:'s4', q:'{b}产品报价多少？' },
    { id:'s5', q:'{b}和竞品比怎么样？' },
  ],
  '酒店': [
    { id:'s1', q:'{c}酒店哪家好？' },
    { id:'s2', q:'{c}性价比高的酒店推荐' },
    { id:'s3', q:'{b}怎么样？' },
    { id:'s4', q:'{b}住宿多少钱一晚？' },
    { id:'s5', q:'{b}和竞品比有什么优势？' },
  ],
  '教育': [
    { id:'s1', q:'{c}培训机构哪家好？' },
    { id:'s2', q:'{c}靠谱的教育机构推荐' },
    { id:'s3', q:'{b}怎么样？' },
    { id:'s4', q:'{b}学费多少？' },
    { id:'s5', q:'{b}和竞品比怎么样？' },
  ],
  '旅游': [
    { id:'s1', q:'{c}旅行社哪家好？' },
    { id:'s2', q:'{c}靠谱的旅行社推荐' },
    { id:'s3', q:'{b}怎么样？' },
    { id:'s4', q:'{b}旅游路线多少钱？' },
    { id:'s5', q:'{b}和竞品比怎么样？' },
  ],
};

// 行业关键词映射
const INDUSTRY_KW = {
  '餐饮':'客家菜','装修':'装修公司','智能家居':'智能家居',
  '医疗':'口腔','科技':'AI公司','酒店':'酒店',
  '教育':'培训机构','旅游':'旅行社'
};
const COMPETITORS = {
  '餐饮':['漳州味道','闽南大院','漳州渔港'],
  '装修':['华浔装饰','星艺装饰','名匠装饰'],
  '智能家居':['小米智能家居','华为智能家居','欧瑞博'],
  '医疗':['漳州第一医院','漳州市医院'],
  '科技':['寒武纪智能','百度AI','科大讯飞'],
};

function getScenarios() {
  const tpls = SCENARIO_TPL[INDUSTRY] || SCENARIO_TPL['餐饮'];
  const kw = INDUSTRY_KW[INDUSTRY] || INDUSTRY;
  const comp = (COMPETITORS[INDUSTRY] || ['竞品'])[0];
  return tpls.slice(0, N).map(t => ({
    id: t.id,
    q: t.q.replace(/{b}/g, BRAND).replace(/{c}/g, LOCATION).replace(/{p}/g, kw).replace(/{comp}/g, comp),
  }));
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

// ============== 智能等待回复 ==============
async function waitForReply(page, maxMs = 90000) {
  await sleep(4000);
  const start = Date.now();
  let last = 0, stable = 0;
  while (Date.now() - start < maxMs) {
    const len = await page.evaluate(() => {
      const sels = ['.markdown-body','.message-content','.answer-content',
        '.chat-message-assistant','[data-role="assistant"]','.response-content',
        '.agent-chat__msg--AI','article','.prose'];
      for (const s of sels) {
        const els = document.querySelectorAll(s);
        if (els.length > 0) return els[els.length-1].innerText.length;
      }
      return document.body.innerText.length;
    }).catch(() => 0);
    if (len > 10 && len === last) {
      if (++stable >= 4) break;
    } else { stable = 0; }
    last = len;
    await sleep(2000);
  }
}

// ============== 提取回复 ==============
async function getReply(page) {
  return await page.evaluate(() => {
    const sels = ['.markdown-body','.message-content','.answer-content',
      '.chat-message-assistant','[data-role="assistant"]','.response-content',
      '.agent-chat__msg--AI','article','.prose'];
    for (const s of sels) {
      const els = document.querySelectorAll(s);
      if (els.length > 0) return els[els.length-1].innerText;
    }
    return document.body.innerText;
  }).catch(() => '');
}

// ============== 分析品牌提及 ==============
function analyze(text) {
  const short = BRAND.replace(/漳州|[\s]/g, '');
  const has = text.includes(BRAND) || text.includes(short);
  if (!has) return 'missed';
  if (/推荐|首选|不错|值得|好评|排行|必去|特色|知名/i.test(text)) return 'found';
  return 'partial';
}

// ============== 生成 Markdown 报告 ==============
function genReport(data, scenes) {
  const { entries } = data;
  const counts = {};
  PLATFORMS.forEach(p => { counts[p.id] = { found:0, partial:0, missed:0 }; });
  scenes.forEach(s => {
    PLATFORMS.forEach(p => {
      const v = entries[p.id]?.[s.id] || 'missed';
      counts[p.id][v] = (counts[p.id][v]||0) + 1;
    });
  });
  const totalFound = Object.values(counts).reduce((s,p)=>s+(p.found||0),0);
  const total = scenes.length * PLATFORMS.length;
  const rate = Math.round(totalFound / total * 100);

  let md = `# 🏷️ GEO 品牌诊断报告：${BRAND}\n\n`;
  md += `> 生成时间：${new Date().toLocaleString('zh-CN')}\n`;
  md += `> 行业：${INDUSTRY} | 城市：${LOCATION}\n`;
  md += `> 数据来源：${PLATFORMS.map(p=>p.name).join(' · ')}\n\n`;
  md += `---\n\n## 📊 采集结果总览\n\n`;
  md += `| 平台 | ✅推荐 | ⚠️模糊 | ❌未推 | 得分 |\n`;
  md += `|------|--------|--------|--------|------|\n`;
  PLATFORMS.forEach(p => {
    const c = counts[p.id];
    const score = Math.round((c.found/(scenes.length))*100);
    md += `| ${p.icon} ${p.name} | ${c.found} | ${c.partial} | ${c.missed} | **${score}%** |\n`;
  });
  md += `\n**综合覆盖率：${rate}%**（${totalFound}/${total}场景被推荐）\n\n`;
  md += `---\n\n## 🔍 分场景分析\n\n`;
  md += `| 场景 | 问题 | ${PLATFORMS.map(p=>p.name).join(' | ')} |\n`;
  md += `|------|------|${PLATFORMS.map(()=>'------').join('|')}|\n`;
  scenes.forEach(s => {
    const q = s.q.length > 20 ? s.q.slice(0,20)+'…' : s.q;
    const cells = PLATFORMS.map(p => {
      const v = entries[p.id]?.[s.id] || 'missed';
      return v==='found'?'✅':v==='partial'?'⚠️':'❌';
    });
    md += `| ${s.id} | ${q} | ${cells.join(' | ')} |\n`;
  });

  md += `\n---\n\n## 💡 核心发现\n\n`;
  const foundScenes = scenes.filter(s => PLATFORMS.some(p => entries[p.id]?.[s.id]==='found'));
  const missedScenes = scenes.filter(s => PLATFORMS.every(p => !entries[p.id]?.[s.id] || entries[p.id][s.id]==='missed'));
  
  md += `### ✅ 优势\n`;
  if (foundScenes.length > 0) {
    foundScenes.forEach(s => { md += `- 场景"${s.q}"：品牌获得推荐\n`; });
  } else { md += `- 暂无明确推荐场景\n`; }

  md += `\n### ❌ 劣势\n`;
  if (missedScenes.length > 0) {
    missedScenes.slice(0,3).forEach(s => { md += `- 场景"${s.q}"：所有平台均未推荐\n`; });
  }
  md += `\n---\n\n## 🚨 紧急程度\n\n`;
  const stars = '⭐'.repeat(Math.ceil(rate/20)) + '☆'.repeat(5-Math.ceil(rate/20));
  md += `| 维度 | 评分 |\n|------|------|\n`;
  md += `| 综合覆盖率 | ${stars} ${rate}% |\n`;
  md += `| 通用搜索覆盖 | ${rate>30?'✅ 良好':'⚠️ 不足'} |\n`;
  md += `| 竞品拦截风险 | ${rate<50?'⚠️ 高风险':'✅ 低风险'} |\n`;
  md += `\n---\n\n## 🎯 优化建议\n\n`;
  md += `### 短期（1-2周）\n`;
  md += `1. 针对未推荐场景（s1/s2类通用词）发布/优化内容\n`;
  md += `2. 在 AI 平台提交企业/品牌百科信息\n`;
  md += `3. 完善各平台企业认证（豆包/元宝/千问）\n\n`;
  md += `### 中期（1个月）\n`;
  md += `1. 产出场景化内容，覆盖更多用户问法\n`;
  md += `2. 与本地 KOL 合作，提升品牌曝光\n`;
  md += `3. 监控 GEO 效果，定期复诊\n\n`;
  md += `---\n\n## 📁 原始数据\n\n`;
  md += `- \`reports/geo_${BRAND}.json\` - 采集原始数据\n`;
  md += `- \`reports/诊断报告_${BRAND}.md\` - 本报告\n`;
  return md;
}

// ============== 主函数 ==============
async function main() {
  const scenes = getScenarios();
  console.log(`
╔════════════════════════════════════════════════════╗
║  🌐 GEO 品牌诊断采集                            ║
╠════════════════════════════════════════════════════╣
║  品牌: ${BRAND.padEnd(36)}║
║  行业: ${INDUSTRY.padEnd(36)}║
║  城市: ${LOCATION.padEnd(36)}║
║  场景: ${N} 个问题                               ║
║  平台: ${PLATFORMS.map(p=>p.name).join(' · ')}              ║
╚════════════════════════════════════════════════════╝
`);

  fs.mkdirSync(path.dirname(OUTPUT_JSON), { recursive: true });
  fs.mkdirSync(PROFILE, { recursive: true });

  // 启动浏览器
  console.log('  🚀 启动 Chrome 浏览器...\n');
  const ctx = await chromium.launchPersistentContext(PROFILE, {
    headless: false,
    channel: 'chrome',
    args: ['--no-sandbox','--disable-blink-features=AutomationControlled','--start-maximized'],
  });

  // 打开平台标签页
  const pages = [];
  for (let i = 0; i < PLATFORMS.length; i++) {
    const p = i === 0 ? ctx.pages()[0] : await ctx.newPage();
    pages.push(p);
    console.log(`  ${PLATFORMS[i].icon} 打开 ${PLATFORMS[i].name}...`);
    await p.goto(PLATFORMS[i].url, { waitUntil:'domcontentloaded', timeout:30000 }).catch(()=>{});
    await sleep(2000);
  }

  // 等待登录
  console.log(`
  ═══════════════════════════════════════════════════
  ⚠️  请在浏览器中登录以下平台：

  ${PLATFORMS.map(p=>`  ${p.icon} ${p.name}: ${p.url}`).join('\n  ')}

  💡 Chrome 已记住登录态，下次无需重复登录。
  💡 登录完成后，按 Enter 开始采集...
  ═══════════════════════════════════════════════════
`);
  await new Promise(r => process.stdin.once('data', () => r()));

  // 全自动采集
  console.log('\n  🔥 开始全自动采集！\n');
  const results = {};

  for (let pi = 0; pi < PLATFORMS.length; pi++) {
    const pl = PLATFORMS[pi];
    const page = pages[pi];
    results[pl.id] = {};
    console.log(`  ═══ ${pl.icon} ${pl.name} ═══\n`);

    for (const s of scenes) {
      process.stdout.write(`  ┌─ ${s.id}: ${s.q}\n  │  `);
      try {
        await page.goto(pl.url, { waitUntil:'domcontentloaded', timeout:30000 }).catch(()=>{});
        await sleep(3000);

        // 智能查找输入框
        const inp = await page.$('textarea, [contenteditable="true"][role="textbox"], [contenteditable="plaintext"], input[type="text"]');
        if (!inp) {
          console.log('❌ 未找到输入框');
          results[pl.id][s.id] = 'missed';
          continue;
        }

        await inp.click();
        await sleep(500);
        await page.keyboard.type(s.q, { delay:30 });
        await sleep(300);
        await page.keyboard.press('Enter');

        process.stdout.write('⏳ ');
        await waitForReply(page);

        const text = await getReply(page);
        const status = analyze(text);
        const icon = status==='found'?'✅':status==='partial'?'⚠️':'❌';
        const label = status==='found'?'推荐':status==='partial'?'模糊提及':'未推荐';
        console.log(`${icon} ${label}`);
        results[pl.id][s.id] = status;
      } catch(e) {
        console.log(`❓ ${e.message.slice(0,50)}`);
        results[pl.id][s.id] = 'error';
      }
      await sleep(2000);
    }
    console.log('');
  }

  // 保存 JSON
  const jsonData = { brand:BRAND, industry:INDUSTRY, location:LOCATION, entries:results, collectedAt:new Date().toISOString() };
  fs.writeFileSync(OUTPUT_JSON, JSON.stringify(jsonData, null, 2), 'utf8');

  // 生成报告
  const md = genReport(jsonData, scenes);
  fs.writeFileSync(OUTPUT_MD, md, 'utf8');

  // 生成 Word 报告
  await genReportDocx(jsonData, scenes, PLATFORMS, OUTPUT_JSON);

  // 统计
  let f=0,p=0,m=0;
  Object.values(results).forEach(r => Object.values(r).forEach(v => { if(v==='found')f++; else if(v==='partial')p++; else m++; }));
  const total = scenes.length * PLATFORMS.length;

  console.log(`
╔════════════════════════════════════════════════════╗
║  ✅ 诊断完成！                                   ║
╠════════════════════════════════════════════════════╣
║  ✅ 推荐: ${f}   ⚠️ 模糊: ${p}   ❌ 未推: ${m}               ║
║  📁 数据: reports/geo_${BRAND}.json              ║
║  📝 报告: reports/诊断报告_${BRAND}.md/.docx      ║
╚════════════════════════════════════════════════════╝
`);
}

main().catch(e => { console.error('\n❌ 错误:', e.message); process.exit(1); });
