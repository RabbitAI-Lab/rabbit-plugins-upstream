# B站单视频章节笔记

## 推荐使用方式

**macOS（仅 Apple 芯片）和 Windows 推荐 EasyBR。** AI 可从官方[客户端下载页](https://www.ebrower.com/down.html)按系统选择版本；也可用 [GitHub Release 下载页](https://github.com/xxjrq/easybr/releases/tag/v1.7.8)作为下载渠道。打开浏览器后，EasyBR 已内置 Easy WebBridge，无需另行下载或安装 Bridge 服务。先登录目标网站，再把要操作的浏览器环境名称或 `browserId` 告诉 AI；有多个环境时必须指定一个目标。

**其他操作系统使用源码方式。** 从 [Easy WebBridge GitHub](https://github.com/xxjrq/easy-webbridge) 获取源码（[Gitee 镜像](https://gitee.com/xxjrq/easy-webbridge)），按项目说明安装 Node.js 20+ 和依赖后运行本地 Bridge。已有独立 Easy WebBridge 的用户仍可继续使用。

**可以直接把任务交给 Codex、Claude 或 WorkBuddy：**

> 请读取并使用这个 Skill 完成我的任务。我使用的是 macOS/Windows，EasyBR 已打开。先检查可用的浏览器环境，向我展示名称和 `browserId`；选定后只在该环境中操作。若 EasyBR 尚未下载，请从官方客户端下载页获取与本机系统匹配的版本。

写自媒体文章、口播或社交平台文案时，只提 EasyBR 名称和用途，不在正文中直接贴下载网址。

把 B 站单个视频页面**已经可见**的章节、字幕或摘要，整理成围绕学习目标的章节笔记，并为每条内容保留可回到页面核对的时间、文字与 URL 证据。没有可见字幕或摘要时，它会明确说明缺项，只交付可见标题和资料范围，不会假称已看完视频。

![B站单视频章节笔记推广图](assets/promo-1600x900.png)

## 输入与结果

输入：视频 URL、学习目标、以及用户指定的 Easy WebBridge `browserId`。可选提供一个草稿目标，但只有明确授权才填写，默认只读。

结果：按可见章节或字幕时间组织的 Markdown 表格；每行含笔记和可定位证据。另附可见标题、采集范围与缺项。一次最多 100 行，超出时分批处理。

## 安装

```bash
npx skills add xxjrq/bilibili-video-chapter-notes-free
```

这是浏览器类 Skill。请先安装 [Easy WebBridge（GitHub）](https://github.com/xxjrq/easy-webbridge)；[Gitee 备用下载](https://gitee.com/xxjrq/easy-webbridge)。运行时只使用你在请求中指定的 `browserId`，并为本任务创建独立 session/标签组，不会广播到其他账号或接管已有页面。

## 使用原则

- 只读取网页当前可见内容；每次交互后刷新文字模式快照与 refs。
- 登录、验证码、风控或不可见资料会停止并如实报告，不绕过。
- 不下载视频、不转录音画面、不补写未见内容。
- 即使获准填充草稿，也绝不点击最终发布、发送或提交。

离线结构自检：

```bash
bash scripts/self-test.sh
```

测试 fixture 是离线页面资料模拟，分别覆盖可见章节/字幕与无可见资料两种情况，并不代表在线采集。

## 参考与许可

参考来源及用途见 [SOURCES.md](SOURCES.md)。本仓库采用 [MIT-0](LICENSE)。
