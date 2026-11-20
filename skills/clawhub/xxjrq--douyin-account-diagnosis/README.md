# 抖音账号诊断

## 推荐使用方式

**macOS（仅 Apple 芯片）和 Windows 推荐 EasyBR。** AI 可从官方[客户端下载页](https://www.ebrower.com/down.html)按系统选择版本；也可用 [GitHub Release 下载页](https://github.com/xxjrq/easybr/releases/tag/v1.7.8)作为下载渠道。打开浏览器后，EasyBR 已内置 Easy WebBridge，无需另行下载或安装 Bridge 服务。先登录目标网站，再把要操作的浏览器环境名称或 `browserId` 告诉 AI；有多个环境时必须指定一个目标。

**其他操作系统使用源码方式。** 从 [Easy WebBridge GitHub](https://github.com/xxjrq/easy-webbridge) 获取源码（[Gitee 镜像](https://gitee.com/xxjrq/easy-webbridge)），按项目说明安装 Node.js 20+ 和依赖后运行本地 Bridge。已有独立 Easy WebBridge 的用户仍可继续使用。

**可以直接把任务交给 Codex、Claude 或 WorkBuddy：**

> 请读取并使用这个 Skill 完成我的任务。我使用的是 macOS/Windows，EasyBR 已打开。先检查可用的浏览器环境，向我展示名称和 `browserId`；选定后只在该环境中操作。若 EasyBR 尚未下载，请从官方客户端下载页获取与本机系统匹配的版本。

写自媒体文章、口播或社交平台文案时，只提 EasyBR 名称和用途，不在正文中直接贴下载网址。

通过 Easy WebBridge 读取指定抖音账号的公开资料和近期作品样本，生成可复核的账号诊断、问题优先级和今日选题建议。

## 适用场景

- 想知道账号近期内容集中在哪些主题。
- 想比较发布频率和公开互动表现。
- 想从已有作品中找下一批选题。

## 使用前准备

准备账号公开页 URL。需要多账号或隔离登录态时，打开已登录的 EasyBR 环境并提供 `browserId`。Skill 只读取公开可见页面，不需要第三方 API Key。

## 结果

结果包含 JSON 和 Markdown 两份报告：采集时间、样本范围、指标定义、证据 URL、P0/P1/P2 问题、局限和三条选题建议。它不读取后台权重，也不自动发布内容。

## 边界

验证码、登录失效、风控和权限不足会停止当前账号并要求用户处理；mock 结果不会标记为真实数据。
