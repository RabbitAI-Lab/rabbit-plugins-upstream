---
name: "xhs-ops"
description: "小红书运营管理：竞品监控/博主追踪/飞书通知/热门趋势发现/内容策略/自动化定时"
user-invocable: true
metadata:
  openclaw:
    emoji: "📊"
    tags: ["xiaohongshu", "operations", "monitoring", "competitor", "feishu"]
---

# XHS Ops v2.0

## 定位
运营执行层。数据→`xhs-data`，分析→`xhs-research`。

---

## 竞品监控

### 配置
```javascript
const ACCOUNTS = [
  { name: '竞品A', id: '用户ID' },
  { name: '竞品B', id: '用户ID' },
];
```

### 运行
```bash
node src/main.js
```

自动采集+去重+解析(标题/正文/商品/直播)。

---

## 飞书通知

```
📕 {博主} 发布新笔记
**{标题}** - {摘要}
👍{likes} 📁{collects} 💬{comments}
🔗 [查看原文](link)
```

---

## 定时运行
```bash
6 14 * * * node src/main.js   # 14:06
6 18 * * * node src/main.js   # 18:06
6 21 * * * node src/main.js   # 21:06
```

分时段频率：08-18每5min / 18-24每10min / 00-08暂停

---

## 热门趋势
热搜榜+推荐流 → 识别上升话题 → 新博主发现

---

## 内容策略
基于数据反推：
- 什么类型易爆
- 什么时段效果好
- 什么标题/封面高点击率

---

## 浏览器管理
```bash
google-chrome --remote-debugging-port=9223 \
  --user-data-dir="$HOME/xhs-monitor/data/browser" \
  "https://www.xiaohongshu.com/"
```
扫码后保持打开，自动复用会话。定期检查登录状态。

---

## 安全
降频防风控，仅供个人运营。
