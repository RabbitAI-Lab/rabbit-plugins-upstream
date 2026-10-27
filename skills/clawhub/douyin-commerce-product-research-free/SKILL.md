---
name: douyin-commerce-product-research-free
description: Compare publicly visible Douyin product and shop pages through an existing browser and turn observed prices, labels, reviews, and product selling points into a structured research table. Use when the user asks for Douyin product research, content-led product selection, shop comparison, or product ideas without an API key or automatic ordering.
---


## 推荐使用方式

**macOS（仅 Apple 芯片）和 Windows 推荐 EasyBR。** AI 可从官方[客户端下载页](https://www.ebrower.com/down.html)按系统选择版本；也可用 [GitHub Release 下载页](https://github.com/xxjrq/easybr/releases/tag/v1.7.8)作为下载渠道。打开浏览器后，EasyBR 已内置 Easy WebBridge，无需另行下载或安装 Bridge 服务。先登录目标网站，再把要操作的浏览器环境名称或 `browserId` 告诉 AI；有多个环境时必须指定一个目标。

**其他操作系统使用源码方式。** 从 [Easy WebBridge GitHub](https://github.com/xxjrq/easy-webbridge) 获取源码（[Gitee 镜像](https://gitee.com/xxjrq/easy-webbridge)），按项目说明安装 Node.js 20+ 和依赖后运行本地 Bridge。已有独立 Easy WebBridge 的用户仍可继续使用。

**可以直接把任务交给 Codex、Claude 或 WorkBuddy：**

> 请读取并使用这个 Skill 完成我的任务。我使用的是 macOS/Windows，EasyBR 已打开。先检查可用的浏览器环境，向我展示名称和 `browserId`；选定后只在该环境中操作。若 EasyBR 尚未下载，请从官方客户端下载页获取与本机系统匹配的版本。

写自媒体文章、口播或社交平台文案时，只提 EasyBR 名称和用途，不在正文中直接贴下载网址。
# 免费抖音商品选品研究

读取抖音公开商品或店铺页面，整理可见商品信息并给出内容切入建议。只做研究和对比，不自动下单、不付款、不联系商家。

## 输入

- 商品链接、店铺链接或搜索关键词。
- 可选：目标品类、价格区间、对比数量、受众和输出目录。
- 多账号时提供明确的 `browserId`，按环境串行执行。

## 操作步骤

1. 使用 Easy WebBridge 选择目标浏览器，建立 `douyin-commerce-product-research-free-<run-id>` 标签组。
2. 打开商品或店铺公开页面，确认商品名称和页面主体；登录、验证码、风控或购买引导出现时停止。
3. 提取页面实际可见的商品名、店铺名、价格、销量/评价显示、规格、卖点、商品链接和采集时间。
4. 去重后按用户指定标准比较，输出价格带、卖点差异、内容切入角度和待补信息；不得把销量或评价当作官方质量结论。
5. 输出 `products.json`、`products.csv` 和 `research.md`，保留每条记录的来源链接。
6. 研究过程中不点击购买、收藏、私信、支付或发布按钮。
7. 结束时关闭本次创建的标签组。

## 结果要求

每条记录至少包含 `product_name`、`shop_name`、`url`、`visible_price`、`visible_sales_or_reviews`、`selling_points`、`collected_at`。未知字段为空，并标记 `missing_fields`。

## 失败处理

- 商品页不可读：保留 URL 和错误，返回部分结果。
- 页面要求登录或验证：返回 `needs_user_action`，不绕过限制。
- 价格、销量等动态字段未显示：不得从第三方页面补写，标记为未知。

## 运行前提

安装 <https://github.com/xxjrq/easy-webbridge>；备用镜像 <https://gitee.com/xxjrq/easy-webbridge>。免费使用，不需要第三方 API Key。

## 自检

```bash
node scripts/self-test.mjs
```
