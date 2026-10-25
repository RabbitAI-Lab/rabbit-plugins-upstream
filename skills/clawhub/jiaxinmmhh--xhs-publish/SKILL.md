---
name: xhs-publish
slug: xiaohongshu-video-uploader
displayName: 小红书视频上传
version: 1.0.0
description: 小红书视频笔记的自动化上传与草稿管理。用 CDP 接管已登录的真实 Chrome，完成上传、标题正文话题填写、原创声明、合集归属，可存草稿或定时发布；支持全量覆盖核对（哪些发了、哪些在草稿箱、哪些两头都没有）与登录失效、风控判罚、草稿丢失的排障。当用户说「发小红书」「小红书草稿箱」「小红书排期」「查小红书哪些没发」时使用。
---

# 小红书视频笔记发布

通过真实 Chrome + CDP 接管已登录会话，自动发布视频笔记。

> 下面是本机实测结论（2026-09-20 验证通过，ep01 成功发布）。与通用做法冲突时以本清单为准。

## 🔴🔴 先读这条：脚本化发布会被判「AI 托管」

2026-09-22 小红书对批量定时发布的笔记做了一次集中处置，**5 条被判「未通过」**，
处置理由原文：

> 笔记存在利用AI托管进行发文/互动的内容
> 涉及利用AI工具托管运营账号的行为……平台严格禁止任何利用技术手段模拟真人、
> 进行非真实内容创作或互动的行为。
> 处置结果：**该篇笔记已不可被他人查看**

- **平台能识别出脚本化发布行为**，不只审内容。继续用 CDP 脚本批量定时发布，同样有被处置风险。
- 不是全量封杀：同期发布的仍有正常拿到阅读的，说明是概率性的风控。
- **给用户做方案时要把这个风险讲清楚**：要么改成人工在浏览器里点发布，要么接受部分笔记不可见。
- 相对安全的折中：**用脚本只做到「存草稿」**（本 skill 的 I2 节），由真人手动点发布。

## 前置条件

1. **Chrome 以调试端口启动**：`zsh /Users/jx/Downloads/.workbuddy/start-chrome-debug.sh`
   （内部 `--user-data-dir=/Users/jx/ChromeAutomation --remote-debugging-port=9222`）
2. **登录态**：`creator.xiaohongshu.com` 已登录（登录态存在该 user-data-dir 里，长期有效）
3. **跑脚本必须带 `NO_PROXY='127.0.0.1,localhost'`**，否则本机代理会拦 CDP
4. 🔴 **node 路径会漂移**（`22.22.2-3` → `-5` → `-6`…），用前先确认：
   `ls /Users/jx/.workbuddy/binaries/node/versions/*/bin/node`

```bash
cd /Users/jx/Downloads/.workbuddy/macros
NO_PROXY='127.0.0.1,localhost' \
NODE_PATH=/Users/jx/.workbuddy/binaries/node/workspace/node_modules \
/Users/jx/.workbuddy/binaries/node/versions/22.22.2-6/bin/node xhs-<脚本>.js
```

现成脚本（macros 目录）：
- `xhs-upload.js` — 上传视频并等待转码（env `VIDEO_PATH`）
- `xhs-compose.js` — 填标题 + 正文 + 逐话题精确点选（env `COPY_FILE`）
- `xhs-submit2.js` — CDP 精确定位并点击「发布」
- `xhs-publish2.js` / `xhs-open-draft.js` — 从草稿箱打开草稿
- `xhs-modal.js` / `xhs-verify2.js` — 核查发布结果

## A. 连接方式

🔴 **用 puppeteer-core，不要用 playwright 的 connectOverCDP。**
2026-10 实测：本机 Chrome 攒到 50+ target 时，`chromium.connectOverCDP` 会**握手卡死**
（ws 连上后无任何响应，30s/120s 全部超时）。puppeteer-core 同场景 **0.4s 连上**。

```js
const puppeteer = require('puppeteer-core');
const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222', protocolTimeout: 300000 });
const pages = (await browser.pages()).filter(p => p.url().includes('creator.xiaohongshu.com'));
// 断开用 browser.disconnect()，千万别 browser.close()（会关掉用户整个 Chrome）
```

API 对照：`ctx.newPage()`→`browser.newPage()`；`locator.click()`→`page.click(sel)`；
`setInputFiles`→`(await page.$(sel)).uploadFile(path)`；`ctx.newCDPSession(page)`→`page.createCDPSession()`；
`browser.contexts()[0]` 不存在，直接 `browser.pages()`。

**多标签页陷阱**：反复调试会攒出多个 creator 标签页，`find()` 可能拿到旧页面（表现为"内容填了但状态不对"）。
操作前先枚举所有页面，只保留一个，其余 `close()`。
有内容但重复的页面要先关掉，否则会在草稿箱留下两条一样的草稿。

## B. 视频上传 —— 可以用 setInputFiles（与视频号不同！）

小红书上传 input 是标准 file input：

```js
await page.locator('input.upload-input').first().setInputFiles(VIDEO_PATH);
```

31MB 视频约 5 秒传完并转码，不需要人工拖拽。轮询 `input[placeholder*="填写标题"]` 出现即代表进入编辑页。

## C. 标题 / 正文

| 字段 | 做法 |
|---|---|
| 标题 | `input[placeholder*="填写标题"]`，**React native setter + dispatch input**（直接 fill 不触发状态） |
| 正文 | `div.tiptap.ProseMirror[contenteditable="true"]`，`document.execCommand('insertText', false, 整段文本)` |

**正文必须整段一次性 insertText**：逐行 `insertParagraph` 会产生大量空段落，排版全散。
整段插入时 `\n` 被 ProseMirror 当软换行，段落间距正常。

**evaluate 传参**：Playwright 只接受 1 个参数，多值要包对象，`page.evaluate(({sel,text})=>{}, {sel,text})`，否则报 `Too many arguments`。

## D. 话题标签 —— 必须点选，且要精确匹配

正文里打 `#关键词` 只是纯文本，不点选不会变成话题链接。

**下拉结构**：`.items > .item`，每项含 `span.name`（话题名）和 `span.num`（浏览量）。

**🔴 两个坑**：
1. **鼠标点 `.item` 会残留纯文本** —— 变成 `#中年危机#中年危机[话题]#`。小红书是把 chip 插到光标处，不替换已输入的文本。
2. **键盘 `Enter` 才会替换**，但下拉默认高亮第 1 项（模糊匹配），直接回车会选错（如输入「中年危机」却得到「中年危机感」）。

**正确做法**：读候选列表 → 求精确项索引 → `ArrowDown` idx 次 → `Enter`。

```js
// 只取最后一个可见的 .items 容器，否则会混入历史遗留 DOM（索引会莫名 +50）
const candidates = await page.evaluate(() => {
  const boxes = Array.from(document.querySelectorAll('.items')).filter(b => b.offsetParent !== null);
  const box = boxes[boxes.length - 1];
  return box ? Array.from(box.querySelectorAll('.item')).map(i => {
    const n = i.querySelector('.name'); return n ? n.innerText.trim() : '';
  }) : [];
});
const idx = candidates.indexOf('#' + kw);
if (idx < 0) { /* 无此话题，跳过 */ }
for (let i = 0; i < idx; i++) { await page.keyboard.press('ArrowDown'); await sleep(150); }
await page.keyboard.press('Enter');
```

**校验**：chip 是 `<a class="tiptap-topic" data-topic='{"name":"..."}'>`，读 `JSON.parse(getAttribute('data-topic')).name` 确认是想要的那个；不符就两次 `Meta+z` 撤销重试。

## E. 合集：创建 + 加入

编辑页 → 内容设置里的「加入合集」→「创建合集」按钮（`div.collection-plugin-create`）。

弹窗（`.creator-modal-style`）：
- 合集名称 `input[placeholder*="吸引更多用户"]`，**上限 20 字**
- 合集简介 `textarea[placeholder*="介绍你的合集"]`，**上限 50 字**
- 按钮「创建并加入」

同样用 native setter 填。创建成功后该区域直接显示合集名，表示已加入当前笔记。

## F. 智能生成章节

`button.smart-generate-btn` → 弹出章节面板，进度 `正在为你智能生成章节 N%`，40 秒左右完成。
完成后出现章节列表（如 `00:00 引言 / 00:13 起源与不安 / 02:40 应对方向`）+ 「保存章节」按钮，**必须点保存才生效**。

## G. 🔴 发布按钮：闭包 shadow DOM，只能坐标点击

底部操作栏是自定义元素 **`<xhs-publish-btn>`**，属性直接给出按钮文案：

```
<xhs-publish-btn is-publish="true" is-save-draft="true"
  submit-text="发布" save-text="暂存离开"
  submit-disabled="false" submit-loading="false"></xhs-publish-btn>
```

`shadowRoot === null`、`innerHTML === ''` —— 内容在**闭包 shadow DOM** 里，`querySelectorAll` / `elementFromPoint` / `innerText` 全都拿不到，页面 `innerText` 里甚至不含"暂存"二字。

**别踩的坑**：
- `span.btn-text` 文本是"发布笔记"，但那是**左侧导航**的下拉触发器（坐标 x≈80,y≈90），点它毫无反应。
- 用 `page.mouse.click` 点 host 高度 72% 处会落到 `div.publish-page-publish-btn`（不响应点击）→ 只会静默存草稿。

**正确做法：用 CDP 穿透闭包 shadow DOM 定位按钮**

```js
const cdp = await ctx.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('Runtime.enable');
await cdp.send('DOM.getDocument', { depth: 1, pierce: true });   // 必做，否则后面扫不到

// 沿 host 水平中线扫描，找 class 含 bg-red 的按钮
const { nodeId } = await cdp.send('DOM.getNodeForLocation',
  { x, y, includeUserAgentShadowDOM: true });
const { node } = await cdp.send('DOM.describeNode', { nodeId, depth: 0, pierce: true });
// node.nodeName === 'BUTTON', attributes 含 "ce-btn bg-red aria-disabled"
```

实测坐标（视口 1470×740，host rect `[353,650,680,90]`）：
- **y 必须取 host 高度 50%**（≈695）——这里才是 `BUTTON.ce-btn.bg-red`
- 红按钮 x 范围 707~815 → 中心 **761**
- 白按钮（暂存离开）x 范围 571~679

拿到中心后用 CDP 原生鼠标事件点击：

```js
await cdp.send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: cx, y: cy, button: 'none', clickCount: 0 });
await cdp.send('Input.dispatchMouseEvent', { type: 'mousePressed', x: cx, y: cy, button: 'left', clickCount: 1 });
await sleep(90);
await cdp.send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: cx, y: cy, button: 'left', clickCount: 1 });
```

**顺带建议**：不要靠硬编码比例，每次先扫 `bg-red` 的 x 范围取中点，适配不同视口。
更好的是先扫出按钮范围再点，脚本 `xhs-submit2.js` 就是这么做的。

## G1. 原创声明

「内容设置」里 `.original-wrapper` 也是个 switch。点开后**会弹确认框**（`.d-modal`，文案
"笔记完成原创声明后，将获得以下权益…我已阅读并同意《原创声明须知》"）：

1. 勾 `.d-modal .d-checkbox`
2. 点 `.d-modal button` 里文本为「声明原创」的按钮
3. 校验 `.original-wrapper .d-switch-simulator` 变成 `checked --color-bg-primary`

不勾复选框直接点按钮无效（和视频号的原创确认框是同一套路）。

## G2. 定时发布（系列日更必须会）

「更多设置」里 `.post-time-wrapper` 是个 switch，开完后出现 `.date-picker-container input`。

- **开关状态以 `<xhs-publish-btn submit-text>` 为准**：开启后 `submit-text` 由「发布」变成「定时发布」。
  不要只用 `.d-switch-simulator` 的 class 判断（会和真实状态脱节）。
- 日期面板：`.post-time-date-picker-popover-class`（宽 470×321，日历 + 小时列 + 分钟列三段）
  - 日期：`.d-datepicker-cell.d-clickable`，文本匹配
  - 小时/分钟：面板内**无子元素**的数字叶子节点。小时列约在 `popover.x + 300~385`（元素 x≈346），分钟列在 `+385` 之后（元素 x≈415）
  - 选完按 `Escape` 收面板。

### 🔴🔴 硬上限：定时发布最远只能选 **14 天内**
- 日历上点超过「今天 + 14 天」的日期，页面弹 toast
  **「发布时间不能超过14天，已自动调整」**，日期被强制回退到第 14 天。
- 举例：今天 9/20 → 最晚只能排到 **10/4**。批量排期时，超出窗口的期数**必然失败**，
  表现为校验读到 `00:00`（时间没设上）或日期与 `EXPECT_DATE` 不符。
- **不要靠试错发现这个**：排期前先用 `今天 + 14 天` 算出截止日，超出的一律不排、等窗口滚动。
- 这时**硬校验（第 G2 节三条防线第 3 条）就是救命的**：本次 ep16(10/5) 连续两次被 `fail()` 拦下，
  **完全没有误发**。永远不要为了"让脚本跑通"而放宽提交前校验。

### 跨月翻月：箭头是「x 倒数第二个」
- 面板顶部有 4 个 `SPAN.d-icon`（className 里**没有** next/prev 方位信息），
  x 从左到右 = `[上一年, 上月, 下月, 下一年]`（实测 x≈24/48/244/268）。
- **取 x 最大的会翻年**（2026-09 → 2027-09 → 2028-09，一路错下去）。
  必须取 **x 排序后倒数第二个**才是「下月」。
- 点完要立刻复核：读面板表头 `(\d{4})年(\d{1,2})月` 换成 `year*12+month`，
  要求恰好 **+1**，否则 `fail()` 中止。
- 面板表头读法：`.post-time-date-picker-popover-class` 的 `innerText` 里匹配 `/(\d{4})\s*年\s*(\d{1,2})\s*月/`。

### 时间列 `07` 贴底边不可点：要滚的是 `.d-timepicker-timebar`
- `.d-timepicker-body` 是 `overflow: visible`（**不是**滚动容器），滚它、对它 wheel 都无效。
- 真正可滚动的是 **`.d-timepicker-timebar`**（`overflow: auto`；小时列 scrollH≈1162 / clientH≈284，
  每项约 38px；面板可见约 7 项，`07` 恰好越界）。
- 正确做法：`el.scrollIntoView({block:'center'})` 把目标项滚到列中间，再点击；
  **点击后必须读 `.date-picker-container input` 复核**，不符则最多重试 3 次，仍不符就 `fail()`。
- 注意事件委托：真正的事件容器是 `DIV.d-space`（项的包裹层）而非文本 `SPAN`。
  用 `elementsFromPoint` 确认命中栈里出现 `SPAN.d-text` 才说明位置对了。

### 键盘直接输入日期：**不可用**
`Ctrl+A` 在 `.date-picker-container input` 里不生效，输入的新值会**拼在旧值后面**，
变成 `2026-09-25 07:002026-09-21 00:44`，按 Enter 也不会解析。
不要走这条路（脚本里已默认关闭，`TYPE_DIRECT=1` 才会启用）。

### 🔴 血泪坑：脚本重复运行会把定时搞丢，然后误发

**事故**：ep03 第一次运行设好了 `2026-09-22 07:00`，第二次运行时开关已是开启态，
脚本又去点**已经选中的日期 22**，把面板 toggle 关掉了 → 时间没设成 →
而旧脚本**没有提交前校验**，照常点了提交 → **笔记被立即发布**，系列节奏被打乱。

**三条防线（缺一不可）**：
1. **幂等保护**：开头先读 `.date-picker-container input` 的值，等于目标值就整段跳过设置，绝不重复点已选中的日期。
2. **每一步前检查面板是否还开着**（`openPanel()` 最多重试 3 次），选完日期后面板可能被自动关闭。
3. **提交前硬校验，不过就中止**（`fail()` 直接抛错，不点提交）：
   - `submit-text === '定时发布'`
   - 定时值非空
   - `EXPECT_DATE` 前缀匹配
   - 含 `HOUR:MIN`
   - `submit-disabled === 'false'`

一期**只跑一次** finalize。真要重跑，靠幂等保护兜底。

## H. 发布成功的判定

页面上出现 **`发布成功 4 秒后将返回发布页 立即返回`**，编辑器消失。

**唯一可靠核验**：新开标签页访问 `https://creator.xiaohongshu.com/new/note-manager`，首条为新笔记，状态「审核中」，且**总数 +1**。
（本次：17 → 18，`08:36 审核中 真正的中年危机，是不想再证明自己 2026-09-20 08:21`）

## I. 其它注意

- 填完内容后若点了发布却没反应，先查草稿箱——很可能只是存了草稿（内容不会丢，点「编辑」重新进入即可）。
- 编辑页「更多设置」含 `公开可见` / `定时发布` 开关，定时面板在 `是否开启定时发布` 区域。
- 话题下拉浮层（`[id^=tippy-]`）会拦截指针事件。关闭方式：**点击标题输入框**（Escape 关不掉）。必要时可 `display:none` + `pointer-events:none`。

## I2. 存草稿（不发布）

### 🔴🔴 草稿存在浏览器本地，不在服务端

发布页原文：**「草稿存储于当前使用的浏览器本地，在清除浏览器数据时会被删除」**。
物理位置：`Profile 1/IndexedDB/https_creator.xiaohongshu.com_0.indexeddb.leveldb`

三条硬规则（2026-10-17 用 25 条草稿的代价换来的）：
1. **不跨浏览器**——自动化 Chrome 里的草稿，用户用自己的日常 Chrome 登录同一账号**看不到**。
   「脚本存草稿 + 真人手动发布」成立的前提是：用户在**这个自动化 Chrome 窗口**里手动发。
2. **绝不能 kill 调试 Chrome / 清缓存 / 换 `--user-data-dir`**。重启后可能
   `Creating DB ... since it was missing` → 全量归零，无回收站、无服务端副本。
3. 每批入库后立刻 `node xhs-drafts-dump.js` 留 `drafts.json`（标题 + 保存时间），这是唯一的重建依据。

**按钮文案是「暂存离开」，不是"草稿"。** 读 `xhs-publish-btn` 的属性即可确认：

```
is-publish / submit-text="发布"      -> 红色发布按钮
is-save-draft / save-text="暂存离开"  -> 白色次要按钮（要点的就是这个）
```

- `DOM.performSearch('草稿')` 返回 **0 条**（按钮在闭包 shadow DOM 里，文本搜不到），别费劲。
- 正确做法：`DOM.getNodeForLocation{includeUserAgentShadowDOM:true}` 坐标扫描：

```js
await cdp.send('DOM.getDocument', { depth: 1, pierce: true });   // 🔴 必须先建树，否则扫不到任何 button
// 扫描 xhs-publish-btn 的 rect 范围，收集 localName==='button' 且 class 含 ce-btn 的节点
```

实测布局（视口 800×600）：
| class | 含义 | x 范围 |
|---|---|---|
| `button.ce-btn.white` | **暂存离开** | 446~554 |
| `button.ce-btn.bg-red` | **发布**（禁点） | 590~698 |

两者 **y 完全相同、只差 x**，所以必须按 class 区分，并加「选到 bg-red 就 fail」的安全闸。

### 🔴 章节弹窗会锁死底部
智能章节生成失败时（"视频解析失败，可重新生成"），会留下一个
`.d-modal-mask`(z-index 999) **盖住整个底部按钮区**：
- 后续 `page.evaluate` 直接超时（300s 都不够）
- 坐标扫描全部命中 mask，找不到任何 button

先关弹窗再操作：`evaluate` 里找可见的「取消」按钮 `.click()`，
兜底 `document.querySelectorAll('.d-modal-mask,.d-modal').forEach(e=>e.remove())`。

### 推荐两步走
1. `xhs-draft-ep.js`（上传 + 标题 + 正文 + 话题 + 原创 + 合集，`NO_CHAPTER=1` 可跳过章节）
2. `xhs-save-draft.js`（关弹窗 → 原创 → 合集 → 扫描并点「暂存离开」，`DRY=1` 只扫描不点击）

```bash
EP=29 node xhs-draft-ep.js && EP=29 node xhs-save-draft.js
```

成功后提示 `草稿箱(N) | 保存成功`。草稿箱列表：发布页点「草稿箱(N)」→ 视频笔记 tab。

## I3. 读取草稿箱列表

```bash
cd /Users/jx/Downloads/.workbuddy/macros
NO_PROXY='127.0.0.1,localhost' NODE_PATH=/Users/jx/.workbuddy/binaries/node/workspace/node_modules \
  /Users/jx/.workbuddy/binaries/node/versions/22.22.2-6/bin/node xhs-draft-list.js
```

- 卡片选择器是 **`.draft-item`**，每条含标题 + 时长 + `保存于YYYY-MM-DD HH:MM:SS` + 编辑/删除
- 🔴 **草稿箱没有可用 API**：`/api/galaxy/creator/note/user/draft/list` 等全部 404，只能读 DOM

## I4. 删除草稿条目（不可逆，必须逐条确认）

脚本 `xhs-draft-del.js`，**默认 DRY，加 `DEL=1` 才真删**：

```bash
TARGET="2026-10-02 23:52:43" node xhs-draft-del.js          # DRY，只开确认气泡
TARGET="2026-10-02 23:52:43" DEL=1 node xhs-draft-del.js    # 真删
```

### 🔴 三条硬规则
1. **按「保存时间字符串」匹配，不要按标题**——标题大量重复（ep16 存过 3 次）
2. **先 `setViewport({width:1440,height:900})`**：800×600 下列表横向溢出，
   删除按钮 rect.x≈1318 超出视口，`page.mouse.click()` **静默点空**（不报错、无弹窗，极难排查）
   → 一律用 **DOM `el.click()`**，不要坐标点击
3. **逐条单独跑，不要放长循环**：4 条连跑被 SIGTERM（exit 137）打断，已删的无法回滚

### 流程
打开草稿箱抽屉 → DOM click 行内文本为「删除」的叶子节点
→ 弹 **`.draft-delete-popconfirm`**（文案「草稿删除后不可找回 / 取消 / 删除」，z-index 1001，absolute）
→ 在 popconfirm 内找文本为「删除」的叶子节点（取最后一个，「取消」在前）DOM click
→ sleep 3s → 重读 `.draft-item` 计数，校验 −1

## J. 批量排期：一键脚本

`/Users/jx/Downloads/.workbuddy/macros/xhs-run-ep.js` —— 一期一条命令跑完全流程
（上传 → 标题 → 正文 → 5 话题精确点选 → 智能章节 → 原创声明 → 合集 → 定时 → 硬校验 → CDP 提交），
单期约 2–4 分钟。

```bash
cd /Users/jx/Downloads/.workbuddy/macros
NO_PROXY='127.0.0.1,localhost' \
NODE_PATH=/Users/jx/.workbuddy/binaries/node/workspace/node_modules \
EP=05 DAY=24 EXPECT_DATE=2026-09-24 HOUR=07 MIN=00 SUBMIT=1 \
/Users/jx/.workbuddy/binaries/node/versions/22.22.2-6/bin/node xhs-run-ep.js
```

- `EP` 期号、`DAY` 日历上点的那一天、`EXPECT_DATE` 期望日期、`SUBMIT=0` 只校验不提交。
- 脚本自带幂等保护与提交前硬校验，**失败一定中止而不是降级提交**——看到 `FATAL【中止】` 就是被拦住了，去查原因，别绕过。
- 文案约定：`/Users/jx/Downloads/xip-epNN/xhs-copy.txt`，三段结构 `## 标题` / `## 正文` / `## 话题标签`。
- 批量生成/转换文案：`macros/conv-episodes.py`（从 episodes.json 转三段式）、`macros/srt-head.py`（抽字幕要点写文案）。
- 核对排期：`macros/xhs-verify-schedule.js`（先关掉未提交的草稿页，再列笔记管理列表）。

### 遇到"点不动"时的高效诊断法
不要盲试。直接读坐标和命中元素：

```js
const r = el.getBoundingClientRect();                       // 真实布局位置
document.elementsFromPoint(cx, cy);                         // 该点最上层是谁
getComputedStyle(container).overflow / scrollHeight         // 谁才是滚动容器
```

`macros/xhs-diag-*.js`（arrow / time / click / wheel / scroll / react）就是这套写法的现成模板。

### 偶发崩溃
Chrome 里页面太多（多个视频号 / chatgpt 标签）时，上传阶段可能抛
`ProtocolError: session closed`。脚本已加 `page.on('dialog', d => d.dismiss())` 兜底，重跑一次即可。

## K. 账号设置与简介（2026-10-07 核实）

### 硬限制（改之前先看，都有配额）
| 项目 | 限制 | 备注 |
|---|---|---|
| 昵称 | 2–24 字符（**汉字算 2**），**7 天 1 次** | 认证号关闭昵称编辑 |
| 简介 | **≤100 字**（汉/英/数均算 1 字），**7 天 3 次** | 全账号最值得打磨的 100 字 |
| 小红书号 | **终身仅可改 1 次** | 限未认证普通个人号；字母/数字/下划线，长度以 App 实时校验为准 |
| UID | 永久不可改 | 系统分配数字标识 |
| 头像/背景图 | 无明确次数限制 | 同样受内容规范约束 |

### 🔴 引流红线（2025-03《交易导流违规管理细则》，2026 社区规范延续）
简介 / 背景图 / 笔记 / 评论 / 私信 / 直播 **全场景**禁止：
微信、QQ、手机号、二维码、外部链接，以及「加 v」「vx」「私信我领资料」「扣 1 领取」等暗示话术。
谐音、缩写、图片水印、视频里一闪而过、大小号联动导流，均会被识别。**主页简介被明确点名。**

- 唯一官方许可的联系方式入口：**把小红书号设成微信号**（可加前缀，如 `VX_xxx`）
- 处罚阶梯：笔记下架 → 警告扣分 → 限制私信与商业权限 → 封号

### 是否开专业号
- 专业号解锁：笔记数据分析、商业合作接单、薯店
- 代价：① **没有成长等级**（成长等级显著影响流量）；② **认证后小红书号不能再改**
- 结论：起量 + 沉淀私域阶段保持普通个人号；要接商单/开店再转

### 简介写法（三段式）
1. 我是谁 / 可验证身份锚点（别写「热爱生活」这类）
2. 我给你什么（内容形式 + 领域，具体到让人知道关注后看到什么）
3. 更新频率 / 社会证明（「每天一条」比「不定期更新」转化高得多）

现成方案见 `/Users/jx/Downloads/小红书账号设置-20261007.html`（4 版可复制）。
本账号在用：**昵称「小豆｜一人公司」+ 简介 A 版（内容主线，亮《怎么活得更好》系列名）**。

## L. 读全量「已发布 / 未通过」列表（含签名翻页）

### 为什么不能靠滚动
- 笔记管理页写着「全部 26」，DOM 里 **只有 10 张 `.note-card`**
- 滚动容器是 `div.content`（**不是 window**）；改 `scrollTop` 不触发加载，
  真实 `page.mouse.wheel()` 会 `Input.dispatchMouseEvent timed out`
- 结论：读全量必须走接口

### 接口与签名
```
GET /api/galaxy/v2/creator/note/user/posted?tab=N&page=N
```
- 直接 fetch → **406 / code:-1**（缺 X-s、X-t 签名）
- ✅ 正解：页面自带 `window._webmsxyw(path)`，返回 `{X-s, X-t}`，
  配合从真实请求里抓的 `x-s-common / authorization / referer / x-b3-traceid` 即可 200
- ⚠️ 签名与 URL 绑定：**page 变了必须重新签名**，拿 page0 的签名去请求 page1 照样 406

### tab 取值
| tab | 含义 | 备注 |
|---|---|---|
| 0 | 全部 | pageSize=10，要翻 3 页 |
| 1 | 已发布 | 一页返回完（26 条里 18 条），**优先用它** |
| 2 | 审核中 | 可能返回 0 |
| 3 | 未通过 | 笔记不可被他人查看 |

### 现成脚本
- `macros/xhs-drafts-dump.js` — 抓草稿箱 → `drafts.json`
- `macros/xhs-coverage.js` — **30 期覆盖矩阵**（读 nm-caught.json + drafts.json），
  输出 已发布/未通过/草稿箱/缺失 四类统计；核对系列完整性只需跑这一个

### 典型用途：查"哪些期没发出去"
必须**三处交叉比对**：笔记管理（已发布 + 未通过）+ 草稿箱。
只看其中一处一定会漏——2026-10 那次就发现有 9 期两头都没有（定时排期没落地、草稿也没留）。

### 补录注意
- EP 传**两位数**（`02` 而不是 `2`），脚本按 `xip-ep${EP}` 拼路径
- 批处理跑的时候**别同时开别的浏览器脚本**，会互相打断
- 单期约 3 分钟（含上传转码），9 期约 27 分钟，用 `run_in_background`
