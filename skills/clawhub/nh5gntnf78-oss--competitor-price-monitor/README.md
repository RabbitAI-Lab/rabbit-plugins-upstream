# Competitor Price Monitor

> 竞品价格监控器 — 自动监控竞品价格，生成价格趋势报告

[![Skill Version](https://img.shields.io/badge/Skill%20Version-2026.06-blue.svg)](#)
[![Platform](https://img.shields.io/badge/Platform-OpenClaw-green.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](#)

## 截图预览

> 以下截图展示典型价格监控报告输出效果。

| 价格对比表 | 趋势图表 | 预警通知 |
|:---:|:---:|:---:|
| 多平台价格横向对比 | 历史价格曲线 | 异常价格变动告警 |

## 功能亮点

## 功能亮点

- ✅ **自动抓取**：支持淘宝、京东、拼多多、亚马逊等平台
- ✅ **定时监控**：配合Cron实现每日自动监控
- ✅ **趋势分析**：生成价格变化趋势报告
- ✅ **及时预警**：价格异常自动通知

## 使用场景

- 电商卖家需要监控竞品价格
- 品牌方需要追踪渠道价格
- 采购需要监控原材料价格
- 消费者需要追踪商品价格变化

## 安装方法

1. 下载 `competitor-price-monitor.skill` 文件
2. 在QClaw中安装：`Skills` → `Install Skill` → 选择文件
3. 重启QClaw Gateway
4. 配置监控列表，开始使用！

## 使用方法

### 基础用法

```
帮我监控竞品价格，产品是：iPhone 15 Pro Max
```

### 高级用法

```
使用competitor-price-monitor技能，监控以下产品价格：
1. iPhone 15 Pro Max (京东、淘宝)
2. MacBook Pro M3 (京东、苹果官网)
生成价格趋势报告
```

## 工作流程

1. **配置监控列表** - 在 `config/monitor_list.json` 中添加产品
2. **抓取价格数据** - 使用xbrowser自动抓取各平台价格
3. **数据分析** - 计算价格统计信息（最低/最高/平均）
4. **生成报告** - 输出Markdown/Excel/腾讯文档报告

## 配置文件示例

```json
{
  "products": [
    {
      "name": "iPhone 15 Pro Max",
      "platforms": ["jd", "taobao"],
      "urls": {
        "jd": "https://item.jd.com/100058382528.html",
        "taobao": "https://item.taobao.com/item.htm?id=123456"
      }
    }
  ]
}
```

## 定时自动化

配合 `qclaw-cron-skill` 实现每日自动监控：

```json
{
  "name": "每日价格监控",
  "schedule": {
    "kind": "cron",
    "expr": "0 9,15,21 * * *",
    "tz": "Asia/Shanghai"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "使用 competitor-price-monitor 技能，抓取竞品价格并生成报告"
  },
  "sessionTarget": "isolated"
}
```

## 安装方法

### 方式一：SkillHub 在线安装（推荐）

```bash
skillhub install competitor-price-monitor
```

### 方式二：本地 Zip 安装

```bash
skillhub install /path/to/competitor-price-monitor-x.x.x.zip
```

### 方式三：手动安装

1. 下载 Skill 包，解压到 `~/.qclaw/skills/competitor-price-monitor/`
2. 重启 QClaw Gateway
3. 配置 `config/monitor_list.json` 开始使用

## 依赖说明

| 依赖 | 版本要求 | 用途 | 必选 |
|------|---------|------|------|
| Python | 3.8+ | 运行环境 | 必选 |
| xbrowser | 已安装 | 浏览器自动化（价格抓取） | 必选 |
| requests | 最新版 | HTTP 请求 | 必选 |
| pandas | 最新版 | 数据分析 | 可选 |
| 当前平台模型 | — | 价格分析报告生成 | 可选 |
| 稳定的网络连接 | — | 抓取数据 | 必选 |

**requests 安装**：
```bash
pip install requests pandas
```

## 变现路径

### 方案A：在ClawHub上销售此Skill

- 基础版：199元（只能监控5个产品）
- 专业版：499元（无限产品 + 历史数据）
- 企业版：1999元（API接口 + 定制开发）

### 方案B：提供价格监控服务

- 按月订阅：299元/月（监控10个产品）
- 按季度订阅：799元/季度
- 按年订阅：2999元/年

## 常见问题

**Q: 支持哪些电商平台？**
A: 目前支持淘宝、京东、拼多多、亚马逊，其他平台可定制。

**Q: 抓取频率有限制吗？**
A: 建议间隔2秒以上，避免被反爬虫机制拦截。

**Q: 价格数据准确吗？**
A: 取决于平台页面结构，建议定期验证。

## 更新日志

### v1.0 (2026-06-12)

- 初始版本
- 支持主流电商平台价格抓取
- 支持定时自动监控

## 联系方式

- 作者：QClaw AI
- 支持：在QClaw中留言

---

**立即安装，开始监控竞品价格！**
