---
name: "browser-automation"
description: "浏览器自动化：网页操作/填表/截图/数据抓取/文件上传/登录/Claude Chrome扩展整合"
user-invocable: true
metadata:
  openclaw:
    emoji: "🌐"
    tags: ["browser", "automation", "playwright", "selenium"]
---

# Browser Automation v2.0

## 双引擎

| 场景 | Playwright | Selenium |
|------|-----------|----------|
| 快速无头 | ✅ 首选 | ❌ 重 |
| 持久会话 | ⚠️ | ✅ 首选 |
| 复杂交互 | ✅ | ✅ |
| 反爬对抗 | ⚠️ | ✅ |

---

## 核心操作

### 导航+交互
click/type/select/hover/drag/scroll/等待加载

### 表单
文本输入(含中文)/下拉框/文件上传(WebP压缩)/提交

### 截图
全屏/区域/元素/PDF导出(png/jpeg/webp)

### 数据抓取
结构化提取/表格导出/无限滚动/分页

### Session
Cookie保存加载/登录复用/多账号切换

---

## 反爬策略
UA伪装/随机延迟/无头检测处理/Proxy/滑块人工介入

---

## 安全
遵守robots.txt/控制频率/不恶意使用。
