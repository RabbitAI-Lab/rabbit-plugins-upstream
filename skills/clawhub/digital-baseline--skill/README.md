# 🏗️ 筑栈 BuildStack — AI 建站 Skill

> AI 驱动的一键网站部署。选模板 → 填信息 → 上线。让你的 AI 助手直接帮你建网站。

[![SkillHub](https://img.shields.io/badge/SkillHub-Install-blue)](https://skillhub.ai)
[![ClawHub](https://img.shields.io/badge/ClawHub-Install-orange)](https://clawhub.ai)
[![Version](https://img.shields.io/badge/version-1.0.0-green)](https://buildstack.com.cn)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

---

## 这是什么？

安装此 Skill 后，你的 AI 助手（Claude、GPT、豆包等）可以直接帮你：

- 🚀 **一句话建站**：告诉 AI 你的业务，30 秒后网站上线
- ✏️ **内容管理**：发布文章、更新产品、修改文案
- 📈 **GEO 优化**：检查 AI 搜索引擎可见度、生成结构化数据
- 🔄 **站点维护**：发布/下线、修改域名、查看分析

原本需要你在浏览器里操作 15 分钟的事情，现在**一个对话搞定**。

---

## 快速开始

### 1. 安装 Skill

```
# SkillHub
skillhub install buildstack-site-builder

# ClawHub
clawhub install buildstack-site-builder
```

### 2. 获取 API Key

1. 注册筑栈：https://buildstack.com.cn/register
2. 登录 → Dashboard → API 密钥 → 创建新密钥
3. 复制 `sk_xxx` 格式的密钥

### 3. 告诉你的 AI

> 「帮我建一个[你的业务]的官网」

AI 会引导你提供必要信息，然后自动完成建站。

---

## 支持的平台

此 Skill 面向所有支持 Skill 生态的 AI Agent 平台：

| 平台 | 状态 |
|------|:--:|
| **QClaw / OpenClaw** | ✅ 原生支持 |
| **ChatGPT (GPTs)** | ✅ 通过 API 调用 |
| **Claude (MCP)** | ✅ 通过 Tool 调用 |
| **豆包 / 元宝** | ✅ 通过 Function Call |
| **Coze / 扣子** | ✅ 通过 Plugin |

---

## 套餐与价格

筑栈按套餐提供不同能力，Skill 会自动感知用户的限额并友好提示：

| 功能 | FREE | STARTER |
|------|:--:|:--:|
| 站点数量 | 1 个 | 3 个 |
| 试用期 | 7 天 | 无限制 |
| AI 建站 | ✅ | ✅ |
| 自定义域名 | ❌ | ✅ |
| 产品管理 | ❌ | ✅ |
| SEO/GEO 工具 | ✅ | ✅ |
| 客服 Widget | ❌ | ✅ |
| **月费** | **¥0** | **¥49** |

[查看完整定价 →](https://buildstack.com.cn/upgrade)

---

## 对话示例

### 建站

> **用户**：帮我做一个瑜伽馆的网站，叫「静心瑜伽」，在杭州西湖区，3 位教练，提供哈他瑜伽、流瑜伽、冥想课程
>
> **AI**：（调用 Skill 建站）已完成！你的瑜伽馆网站已上线：
> - 🌐 https://jingxin-yoga.buildstack.com.cn
> - 📄 包含：首页 / 关于我们 / 教练团队 / 课程介绍 / 联系预约
> - 📱 手机适配 / SEO 已优化

### 内容发布

> **用户**：给瑜伽馆网站发一篇「5个适合办公室的瑜伽动作」的文章
>
> **AI**：（调用 CMS API 发布）已发布！访问 https://jingxin-yoga.buildstack.com.cn/news/office-yoga-tips 查看。

### 升级引导

> **用户**：再帮我做一个普拉提工作室的网站
>
> **AI**：你目前是 FREE 套餐（1 个站点），静心瑜伽已经占用了。普拉提网站已经准备好了——升级到 STARTER（¥49/月）即刻上线 👉 https://buildstack.com.cn/upgrade

---

## 技术架构

```
AI Agent (你的 AI 助手)
    │
    ▼
buildstack-site-builder Skill (本 Skill)
    │  翻译用户意图 → API 调用
    ▼
筑栈 BuildStack API (https://buildstack.com.cn)
    │  AI 建站 / CMS / SEO / 容器化部署
    ▼
Docker 容器 (每个站点独立隔离)
    │  Nginx + HTML + CMS Renderer
    ▼
🌐 用户网站 (你的域名或 buildstack.com.cn 子域名)
```

---

## 安全

- 所有 API 调用通过 HTTPS，API Key 认证
- 站点容器隔离，互不影响
- 不会读取或存储你的支付宝/信用卡信息
- 不会访问你其他 Skill 的数据

---

## 常见问题

**Q: 我已有域名，能用吗？**
A: ✅ STARTER 套餐支持绑定自有域名（需做 DNS 解析）。

**Q: 建站能改代码吗？**
A: ✅ 支持源码编辑器（HTML/CSS/JS），也支持可视化拖拽。

**Q: 数据安全吗？**
A: ✅ 每个站点独立 Docker 容器运行，每日自动备份到阿里云 OSS。

**Q: 支持哪些语言？**
A: 简体中文 / English / 繁體中文。模板支持多语言切换。

**Q: 能对接微信支付/支付宝吗？**
A: 产品展示支持，在线支付需自定义开发。

---

## 更新日志

### v1.0.0 (2026-06-24)
- 🚀 首次发布
- ✅ AI 建站（一句话 → 完整网站）
- ✅ CMS 内容管理（文章 / 产品 / 团队）
- ✅ SEO / GEO 工具
- ✅ 套餐限额自动感知

---

## 协议

本 Skill 基于 MIT 协议开源。筑栈 API 使用需遵守 [筑栈服务协议](https://buildstack.com.cn/terms)。
