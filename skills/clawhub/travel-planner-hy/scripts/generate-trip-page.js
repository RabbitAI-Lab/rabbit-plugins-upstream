/**
 * generate-trip-page.js — Travel Plan HTML Page Generator
 *
 * 生成精美的行程网页，左侧显示行程安排，右侧显示第三方平台跳转二维码（仅跳转，不代订不代付）
 *
 * 用法：
 *   node scripts/generate-trip-page.js          # 真实模式（默认不自动打开浏览器）
 *   node scripts/generate-trip-page.js --mock    # Mock 模式（无需 API Key）
 *   node scripts/generate-trip-page.js --open    # 生成后自动打开浏览器
 *
 * --mock 模式使用内置 mock 数据生成演示行程
 */

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

// Mock 模式检测
const isMock = process.argv.includes('--mock');

// 加载 mock 数据
const mockData = require('./mock-data.js');

// ============================================================
// 样式与 HTML 模板
// ============================================================

function getCSS() {
  return `
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; background: #f5f7fa; color: #333; }
.container { max-width: 1100px; margin: 0 auto; padding: 20px; }
.header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #fff; padding: 40px; border-radius: 16px; margin-bottom: 24px; text-align: center; }
.header h1 { font-size: 28px; margin-bottom: 8px; }
.header .subtitle { font-size: 14px; opacity: 0.9; }
.main-grid { display: grid; grid-template-columns: 1fr 360px; gap: 24px; }
@media (max-width: 768px) { .main-grid { grid-template-columns: 1fr; } }
.section { background: #fff; border-radius: 12px; padding: 24px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
.section h2 { font-size: 18px; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 2px solid #667eea; color: #444; display: flex; align-items: center; gap: 8px; }
.itinerary-item { padding: 12px 0; border-bottom: 1px dashed #eee; display: flex; gap: 12px; }
.itinerary-item:last-child { border-bottom: none; }
.itinerary-item .time { font-weight: 600; color: #667eea; min-width: 80px; font-size: 14px; }
.itinerary-item .content { flex: 1; font-size: 14px; line-height: 1.6; }
.itinerary-item .content .highlight { color: #e74c3c; font-weight: 500; }
.qr-section { text-align: center; }
.qr-section img { max-width: 280px; margin: 16px 0; border-radius: 8px; }
.qr-section .total-price { font-size: 24px; font-weight: 700; color: #e74c3c; margin: 8px 0; }
.qr-section .price-label { font-size: 13px; color: #888; }
.btn-book { display: inline-block; padding: 10px 24px; background: #667eea; color: #fff; text-decoration: none; border-radius: 8px; font-size: 14px; margin: 8px 4px; }
.btn-book:hover { background: #5a6fd6; }
.tag { display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 12px; margin: 2px; background: #eef2ff; color: #667eea; }
.tag.free { background: #e8f5e9; color: #2e7d32; }
.tag.paid { background: #fff3e0; color: #e65100; }
.budget-table { width: 100%; border-collapse: collapse; font-size: 14px; }
.budget-table th, .budget-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid #eee; }
.budget-table th { background: #f8f9fa; font-weight: 600; color: #555; }
.budget-table tr:last-child td { font-weight: 700; color: #e74c3c; }
.tips-list { list-style: none; padding: 0; }
.tips-list li { padding: 6px 0; font-size: 14px; color: #555; display: flex; align-items: flex-start; gap: 8px; }
.tips-list li::before { content: "💡"; flex-shrink: 0; }
.attraction-card { padding: 12px; margin: 8px 0; border: 1px solid #eee; border-radius: 8px; font-size: 14px; }
.attraction-card .name { font-weight: 600; font-size: 15px; }
.attraction-card .info { color: #666; margin-top: 4px; line-height: 1.6; }
.attraction-card .reason { color: #667eea; margin-top: 4px; font-size: 13px; }
`;
}

function getHTML(tripData) {
  const { title, subtitle, destination, days, travelers, budget, preferences, attractions, itinerary, hotels, transport, costs, tips } = tripData;

  return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title || destination + '旅行方案'}</title>
  <style>${getCSS()}</style>
</head>
<body>
  <div class="container">
    <!-- 头部 -->
    <div class="header">
      <h1>🗺️ ${title || destination + '旅行方案'}</h1>
      <div class="subtitle">${subtitle || days + '天 · ' + travelers + '人 · 预算¥' + (budget || '待定')}</div>
    </div>

    <div class="main-grid">
      <!-- 左侧：行程详情 -->
      <div class="left-column">
        <!-- 预算概览 -->
        <div class="section">
          <h2>💰 预算概览</h2>
          <table class="budget-table">
            <tr><th>项目</th><th>金额</th><th>占比</th></tr>
            ${(costs && costs.items) ? costs.items.map(item => '<tr><td>' + item.name + '</td><td>¥' + item.amount + '</td><td>' + item.pct + '</td></tr>').join('') : ''}
            <tr><td>合计</td><td>¥${costs ? costs.total : 0}</td><td>100%</td></tr>
          </table>
        </div>

        <!-- 推荐景点 -->
        ${attractions ? `
        <div class="section">
          <h2>🏆 推荐景点</h2>
          ${attractions.slice(0, 6).map((a, i) => `
          <div class="attraction-card">
            <div class="name">${i+1}. ${a.name}</div>
            <div class="info">
              ${a.type.map(t => '<span class="tag">' + t + '</span>').join('')}
              <span class="${a.ticketPrice === 0 ? 'tag free' : 'tag paid'}">${a.ticketPrice === 0 ? '免费' : '¥' + a.ticketPrice}</span>
              ⭐ ${a.rating}
            </div>
            <div class="info">⏰ ${a.estimatedDuration || '待定'} | ${a.openingHours || ''}</div>
            ${a.description ? '<div class="info">' + a.description + '</div>' : ''}
            ${a._reason ? '<div class="reason">💡 ' + a._reason + '</div>' : ''}
          </div>
          `).join('')}
        </div>` : ''}

        <!-- 每日行程 -->
        ${itinerary ? itinerary.map((day, di) => `
        <div class="section">
          <h2>🗓️ 第${di+1}天 — ${day.date || '行程日'}</h2>
          ${day.items.map(item => `
          <div class="itinerary-item">
            <div class="time">${item.time}</div>
            <div class="content">
              ${item.icon || '📍'} <strong>${item.title}</strong>
              ${item.detail ? '<br>' + item.detail : ''}
              ${item.cost ? '<br><span class="highlight">💰 ' + item.cost + '</span>' : ''}
            </div>
          </div>
          `).join('')}
          ${day.notes ? '<div style="margin-top:12px;padding:10px;background:#fff8e1;border-radius:8px;font-size:13px"><strong>⚠️ 注意：</strong>' + day.notes + '</div>' : ''}
        </div>
        `).join('') : ''}

        <!-- 住宿推荐 -->
        ${hotels ? `
        <div class="section">
          <h2>🏨 住宿推荐</h2>
          ${hotels.slice(0, 3).map(h => `
          <div class="attraction-card">
            <div class="name">${h.name}</div>
            <div class="info">📍 ${h.area || ''} | ⭐ ${h.rating} | 💰 ¥${h.price}/晚</div>
            <div class="info">${h.features || ''}</div>
            ${h.distance ? '<div class="info">📏 ' + h.distance + '</div>' : ''}
          </div>
          `).join('')}
        </div>` : ''}

        <!-- 温馨提示 -->
        ${tips ? `
        <div class="section">
          <h2>💡 温馨提示</h2>
          <ul class="tips-list">
            ${tips.map(t => '<li>' + t + '</li>').join('')}
          </ul>
        </div>` : ''}
      </div>

      <!-- 右侧：第三方平台跳转（不代订不代付） -->
      <div class="right-column">
        <div class="section qr-section">
          <h2>🔗 第三方平台跳转</h2>
          <div class="thirdparty-warning" style="background:#fff3cd;border:1px solid #ffc107;border-radius:8px;padding:10px 12px;font-size:12px;color:#856404;margin-bottom:12px;text-align:left;">
            ⚠️ 本技能<b>不代订、不代付</b>，不创建订单。下方二维码/按钮<b>仅跳转</b>到第三方平台公开页面，您须在第三方平台自行完成预订与支付。本技能不收集您的身份/支付信息。
          </div>
          <div id="qrcode-container">
            <p style="color:#888;font-size:14px;">正在加载二维码...</p>
          </div>
          <div class="total-price">¥${costs ? costs.total : 0}</div>
          <div class="price-label">预估总计（仅供参考）</div>
          ${costs && costs.paymentUrls ? costs.paymentUrls.map(url =>
            '<a class="btn-book" href="' + url + '" target="_blank" rel="noopener noreferrer">🔗 ' + (url.includes('tuniu') ? '途牛待付款页（自行支付）' : url.includes('12306') ? '12306（自行购票）' : '前往第三方平台') + '</a>'
          ).join('') : ''}
          <div style="margin-top:16px;font-size:12px;color:#aaa;">
            💡 上述链接为第三方平台公开入口，实际订单/价格以第三方平台为准
          </div>
        </div>

        <div class="section">
          <h2>📋 行程信息</h2>
          <div style="font-size:14px;line-height:2;">
            <div>📍 目的地：<strong>${destination}</strong></div>
            <div>🗓️ 天数：<strong>${days}</strong></div>
            <div>👥 人数：<strong>${travelers}人</strong></div>
            <div>💰 预算：<strong>¥${budget || '待定'}</strong></div>
            ${preferences ? '<div>🏷️ 偏好：' + preferences.map(p => '<span class="tag">' + p + '</span>').join('') + '</div>' : ''}
            ${transport ? '<div>🚄 交通：' + transport.airport + '<br>' + transport.tips + '</div>' : ''}
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    // 加载二维码
    (function() {
      var container = document.getElementById('qrcode-container');
      var url = '${costs && costs.paymentUrls ? costs.paymentUrls[0] : 'https://example.com'}';
      if (url && url !== 'https://example.com') {
        var img = document.createElement('img');
        img.src = '/api/qrcode?url=' + encodeURIComponent(url) + '&t=' + Date.now();
        img.alt = '第三方平台跳转二维码';
        img.onerror = function() {
          container.innerHTML = '<p style="color:#999;font-size:13px;">二维码加载失败<br>请直接点击下方支付按钮</p>';
        };
        container.innerHTML = '';
        container.appendChild(img);
      } else {
        container.innerHTML = '<p style="color:#999;font-size:13px;">示例二维码<br>（实际使用时替换为真实支付链接）</p>';
      }
    })();
  </script>
</body>
</html>`;
}

// ============================================================
// Mock 数据生成
// ============================================================

function generateMockTripData() {
  const city = '重庆';
  const days = 3;
  const travelers = 2;
  const budget = 5000;
  const preferences = ['美食', '自然', '网红打卡'];

  // 获取景点并评分
  let attractions = mockData.getMockAttractions(city);
  attractions = mockData.filterByPreference(attractions, preferences);
  attractions = mockData.filterByBudget(attractions, budget, days);

  // 生成推荐理由
  attractions = attractions.map(a => {
    let reasons = [];
    if (a.ticketPrice === 0) reasons.push('免费开放，性价比高');
    if (a.rating >= 4.5) reasons.push('评分' + a.rating + '，口碑优秀');
    reasons.push('与您偏好的' + a.type.join(',') + '风格相符');
    a._reason = reasons.join('；');
    return a;
  });

  // 每日行程
  const itinerary = [
    {
      date: '第1天（到达日）',
      items: [
        { time: '08:00-09:00', icon: '🍳', title: '早餐', detail: '酒店/当地特色早餐', cost: '人均15-20元' },
        { time: '09:00-10:30', icon: '🚄', title: '抵达重庆', detail: '高铁/飞机到达，前往酒店办理入住', cost: '' },
        { time: '10:30-12:00', icon: '🎯', title: '解放碑', detail: '重庆标志性商圈，观抗战胜利纪功碑', cost: '免费' },
        { time: '12:00-13:30', icon: '🍜', title: '午餐', detail: '八一好吃街品尝重庆小吃', cost: '人均30-50元' },
        { time: '13:30-17:30', icon: '🎯', title: '磁器口古镇', detail: '千年古镇，品陈麻花、逛古街', cost: '免费' },
        { time: '17:30-18:30', icon: '🛌', title: '回酒店休息', detail: '' },
        { time: '18:30-20:00', icon: '🍽️', title: '晚餐', detail: '枇杷园火锅（老字号，推荐毛肚火锅）', cost: '人均80-120元' },
        { time: '20:00-22:00', icon: '🌙', title: '洪崖洞夜景', detail: '观赏重庆最美夜景，吊脚楼灯光秀', cost: '免费' }
      ],
      notes: '重庆夏季炎热，建议随身带水；洪崖洞亮灯时间为19:30-23:00'
    },
    {
      date: '第2天（全日游）',
      items: [
        { time: '08:00-09:00', icon: '🍳', title: '早餐', detail: '酒店早餐' },
        { time: '09:00-10:00', icon: '🚇', title: '李子坝轻轨站', detail: '网红轻轨穿楼打卡', cost: '免费' },
        { time: '10:00-12:00', icon: '🎯', title: '三峡博物馆', detail: '了解三峡文化与重庆历史（周一闭馆）', cost: '免费，需预约' },
        { time: '12:00-13:30', icon: '🍜', title: '午餐', detail: '中山四路附近餐馆', cost: '人均30-50元' },
        { time: '13:30-14:00', icon: '☕', title: '午休', detail: '' },
        { time: '14:00-17:00', icon: '🎯', title: '长江索道', detail: '空中俯瞰长江两岸风光', cost: '¥30/人往返' },
        { time: '17:00-18:30', icon: '🎯', title: '南山一棵树观景台', detail: '360度俯瞰重庆全景', cost: '¥30/人' },
        { time: '18:30-20:30', icon: '🍽️', title: '晚餐', detail: '南山泉水鸡一条街', cost: '人均60-100元' }
      ],
      notes: '三峡博物馆周一闭馆，请避开；南山观景台建议18:00前到达占位看日落'
    },
    {
      date: '第3天（返程日）',
      items: [
        { time: '07:00-08:00', icon: '🍳', title: '早餐 + 退房', detail: '酒店早餐，办理退房寄存行李' },
        { time: '08:00-10:00', icon: '🎯', title: '湖广会馆', detail: '清代移民会馆建筑群', cost: '¥30/人' },
        { time: '10:00-12:00', icon: '🛍️', title: '解放碑商圈购物', detail: '购买特产伴手礼', cost: '视个人情况' },
        { time: '12:00-13:00', icon: '🍜', title: '午餐', detail: '重庆小面/豆花饭', cost: '人均15-25元' },
        { time: '13:00-14:00', icon: '🎒', title: '取行李前往车站', detail: '' },
        { time: '14:00', icon: '🚄', title: '返程出发', detail: '前往重庆北站/机场' }
      ],
      notes: '最后一班高铁约21:00，飞机请预留2小时到机场'
    }
  ];

  // 住宿推荐
  const hotels = mockData.getMockHotels(city);

  // 交通信息
  const transport = mockData.getMockTransport(city);

  // 预算明细
  const costs = {
    items: [
      { name: '🚄 交通（高铁往返）', amount: 300, pct: '6%' },
      { name: '🏨 住宿（2晚）', amount: 1600, pct: '32%' },
      { name: '🎫 门票', amount: 180, pct: '4%' },
      { name: '🍜 餐饮', amount: 1200, pct: '24%' },
      { name: '🚕 当地交通', amount: 300, pct: '6%' },
      { name: '📦 其他', amount: 420, pct: '8%' }
    ],
    total: 4000,
    paymentUrls: [
      'https://m.tuniu.com/u/order?page=1&filter=0-0-1'
    ]
  };

  // 温馨提示
  const tips = [
    '重庆7月平均气温28-35°C，建议携带防晒霜、遮阳帽、便携风扇',
    '重庆饮食以麻辣为主，肠胃敏感建议备好肠胃药',
    '景点间推荐地铁出行（下载"渝畅行"APP扫码乘车）',
    '洪崖洞、长江索道等热门景点建议非高峰时段前往',
    '建议购买旅游意外险，出行前告知家人行程安排'
  ];

  return {
    title: `重庆${days}日游旅行方案`,
    subtitle: `${days}天 · ${travelers}人 · 预算¥${budget}`,
    destination: city,
    days,
    travelers,
    budget: budget.toString(),
    preferences: ['美食', '自然', '网红打卡', '人文'],
    attractions,
    itinerary,
    hotels,
    transport,
    costs,
    tips
  };
}

// ============================================================
// 主入口
// ============================================================

function main() {
  console.log('🚀 Travel Planner — 行程网页生成器');
  console.log('====================================');

  let tripData;

  if (isMock) {
    console.log('[Mock mode] Using built-in mock trip data');
    tripData = generateMockTripData();
    console.log(`📍 目的地：${tripData.destination}`);
    console.log(`🗓️  天数：${tripData.days}天`);
    console.log(`🏆 景点数：${tripData.attractions.length}个`);
  } else {
    console.log('[Real mode] Loading from environment...');
    // 真实模式：从环境变量或 CLI 参数读取行程数据
    try {
      const inputData = process.env.TRIP_DATA || '{}';
      tripData = JSON.parse(inputData);
    } catch (e) {
      console.error('❌ 未找到行程数据，使用 Mock 模式回退');
      tripData = generateMockTripData();
    }
  }

  // 生成 HTML
  const html = getHTML(tripData);

  // 保存文件
  const outputDir = path.join(process.cwd(), 'output');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  const timestamp = Date.now();
  const outputPath = path.join(outputDir, `trip-${tripData.destination}-${timestamp}.html`);
  fs.writeFileSync(outputPath, html, 'utf-8');

  console.log(`✅ HTML 已生成：${outputPath}`);

  // 打开网页 —— 仅 --open 时执行，默认不自动打开（避免无条件启动浏览器/子进程）
  const shouldOpen = process.argv.includes('--open');
  if (shouldOpen) {
    try {
      const platform = process.platform;
      // 用 spawnSync + shell:false，避免对路径做 shell 插值
      if (platform === 'win32') {
        spawnSync('cmd', ['/c', 'start', '', outputPath], { timeout: 3000, shell: false });
      } else if (platform === 'darwin') {
        spawnSync('open', [outputPath], { timeout: 3000, shell: false });
      } else {
        spawnSync('xdg-open', [outputPath], { timeout: 3000, shell: false });
      }
      console.log('🌐 已打开浏览器（--open）');
    } catch (e) {
      console.log(`📂 自动打开失败，请手动打开：${outputPath}`);
    }
  } else {
    console.log('📂 HTML 已保存。如需自动打开浏览器，请添加 --open 参数。');
    console.log(`   文件路径：${outputPath}`);
  }

  return outputPath;
}

if (require.main === module) {
  main();
}

module.exports = { getHTML, generateMockTripData, main };