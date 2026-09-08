---
name: bilibili-news-video-publish
description: "自动视频工作流：抓新闻、生成口播文案、华声生成MG视频、导出并发布到B站，含Fabric封面文字注入与B站投稿表单填写。"
metadata:
  version: 1.0.0
---

# B站新闻口播视频自动发布工作流

每天自动抓取国内外新闻 → 生成大白话口播文案 → 华声(huasheng.cn)生成MG动画口播视频 → 导出 → 发布到B站。

## 触发场景
- 用户要做自动口播新闻视频
- 需要从新闻生成口播文案并发布到B站
- 华声视频导出 / B站投稿 / 封面文字处理

## 完整流程
1. 抓新闻 + 生成口播文案 + SQLite 查重入库（cron 每天8点）
2. 华声生成 MG 动画口播视频（需登录，生成可能等数小时，用 cron 轮询检测）
3. 华声「导出」→「发布B站」→ 跳转 B 站投稿页
4. 填 B 站发布表单 → 立即投稿

## B站投稿表单填写
- 标题：`M月D日 + 文章标题`（80字内）
- 创作声明：个人观点，仅供参考
- 分区：资讯
- 标签：点击推荐标签添加，加满10个
- 加入合集：热点资讯
- 简介：100-200 字摘要
- 发布：即时
- 注意：网页端**没有「定位/长沙市」功能**（移动端APP才有），不要浪费时间找

## 封面文字注入（Fabric.js 画布，核心难点）

封面是 Fabric.js 画布，文字是画布对象。模拟 JS 双击(isTrusted=false)无法进入编辑态，必须用 CDP 真实事件。

### 操作步骤
1. 清掉模板文字，恢复干净背景图，点「添加文字」得到干净文字框（显示「请输入文字」）
2. 用 CDP 真实双击进入编辑态：
   ```
   openclaw browser click-coords <x> <y> --double
   ```
   （`<x> <y>` 用像素扫描定位文字中心，见 references/fabric-cover-text.md）
3. 检测 Fabric 编辑时创建的**隐藏 textarea**（value 是被编辑文字）
4. 直接往隐藏 textarea 注入文字：
```js
const t = document.querySelector('textarea');
const setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
setter.call(t, '目标文字');
t.dispatchEvent(new Event('input', {bubbles:true}));
```

### Fabric 定位要点
- canvas 物理像素 = 屏幕像素 × DPR（常为2），换算要 ÷2
- 找蓝色选中框像素 = 文字已选中
- 隐藏 textarea 出现 = 已进入编辑态（此时注入最可靠）

### 踩坑
- 点封面「不使用」会连背景图一起清掉，需重传图片
- 误套系统模板产生「今日热点/全知道/救星」模板组，干扰定位
- 模拟鼠标双击无法进入 Fabric 编辑态，必须用 CDP 真实事件(--double)
- 图片文件先复制到 `.openclaw/media/inbound/`，再用 `openclaw browser upload "media://inbound/xxx"` 注入

## 常用浏览器自动化命令
```bash
openclaw browser tabs                      # 查看标签页
openclaw browser focus <tab>               # 聚焦标签
openclaw browser snapshot --labels         # 快照含ref
openclaw browser click <ref>               # 点击by ref
openclaw browser click-coords <x> <y> [--double]  # 点击by坐标(可双击)
openclaw browser evaluate --fn "()=>{...}" # 执行JS
openclaw browser upload "media://inbound/x" # 注入文件
openclaw browser screenshot                # 截图
```

## 脚本
- `scripts/fetch_news.py` — 抓新闻生成口播文案入库
- `scripts/news_db.py` — SQLite 数据库操作

详见 `references/bilibili-form.md` 和 `references/fabric-cover-text.md`。
