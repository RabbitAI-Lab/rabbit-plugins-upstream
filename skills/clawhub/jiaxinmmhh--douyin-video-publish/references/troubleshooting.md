# 抖音发布踩坑详解

改脚本前务必读这篇。每条都是实测踩出来的，不是推测。

---

## 1 定时发布时间控件：必须 native setter 注入

抖音发布页的定时控件是 Semi Design 的 DatePicker，挂在 `.semi-datepicker` 下：

```html
<div class="semi-datepicker" style="width:175px">
  <div class="semi-datepicker-input">
    <div class="semi-input-wrapper ...">
      <input format="yyyy-MM-dd HH:mm" class="semi-input semi-input-default"
             type="text" placeholder="日期和时间" value="2026-10-15 01:15">
```

**试过但失败的方式**：
- `page.mouse.click` 三击全选 → 文本没被选中，键入变成拼接（`2026-10-152026-10-16 07:00 01:15`）
- `Meta+A` → 同样无效
- 点日历面板选日期 → 面板 class 名多变、命中不稳定，且小时/分钟还要再点两轮

**可行方式**（`dy-publish.js` 已固化）：

```js
await page.evaluate((v) => {
  const el = document.querySelector('.semi-datepicker input.semi-input');
  el.focus();
  Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
  el.dispatchEvent(new Event('input', { bubbles: true }));
}, '2026-10-15 07:00');
await sleep(600);
await page.keyboard.press('Enter');   // 必须回车确认，否则失焦即回滚
```

注入后一定要**回读校验**：`value` 不等于目标值就中止，绝不能带着错时间提交。

默认值规律：切到「定时发布」时预填 **当前时间 + 2 小时**。

---

## 2 两个"合集"下拉，别点错

「添加合集」这一行是这样：

```
添加合集   [合集 ∨]        [请选择合集              ∨]
            ↑ 类型下拉        ↑ 真正要点的那个
```

- 左边那个 `.semi-select` 的 `innerText` 恰好就是 `"合集"`（它是合集**类型**）
- 右边那个的 `innerText` 是 `"请选择合集"`

用 `txt.includes('合集')` 会命中左边，点开只弹出一个"合集"二字的气泡，**选项永远加载不出来**，看起来像"下拉打不开"。

正确做法：

```js
for (const h of await page.$$('.semi-select')) {
  const txt = (await h.evaluate(e => e.innerText || '')).trim();
  if (txt.includes('请选择合集') || txt.includes(ALBUM)) { target = h; break; }
}
```

选项的 class 是 `semi-select-option collection-option`（普通选项是 `semi-select-option`），匹配用 `includes(合集名)`。

---

## 3 上传未完成时，右侧进度浮层吞掉所有点击

页面右上角上传进度卡片里有「取消上传」按钮。**只要这个文案还在，浮层就还在**，它会盖住右侧区域，导致点击落空。

错误判据：`body.innerText.includes('重新上传')` —— 实测在 **85%** 就已为 true。

正确判据：

```js
const t = document.body.innerText;
const done = t.includes('重新上传') && !t.includes('取消上传');
```

另外补一个 `sleep(4000)` 让浮层动画收尾。此外「视频预览功能…我知道了」的提示气泡也会挡，脚本在选合集前会先点掉它。

> 注：同一账号短时间内重复上传同一个文件会走秒传（3 秒完成），别被"太快了不可能"误导。

---

## 4 标题输入框没有稳定的 maxLength

页面上有多个 `input[type=text]`：付费标题（ml=28）、日期时间（ml=-1）、以及作品标题。
实测作品标题的 `maxLength` **也是 -1**（虽然 UI 上显示 `17/30`）。

定位用 placeholder：

```js
document.querySelector('input[placeholder*="作品标题"]')
```

回填同样走 native setter（React 受控）。

---

## 5 简介是富文本编辑器，用 CDP insertText

简介容器：

```html
<div class="zone-container editor-kit-container editor editor-comp-publish"
     contenteditable="true" data-slate-editor="true" data-placeholder="添加作品简介">
```

**注意 `box.y` 可能是负值**（表单区在视口上方），此时按坐标点击会点到页面外，`insertText` 全部丢失（表现为 `descLen:1`）。

正确顺序：

```js
await page.evaluate(() => {
  const e = document.querySelector('[contenteditable="true"]');
  e.scrollIntoView({ block: 'center' });
  e.focus();
});
const cdp = await page.createCDPSession();
await cdp.send('Input.insertText', { text: 全文 });   // 正文 + \n + 话题，一次搞定
```

**话题不需要点选**：纯文本 `#中年危机 #个人成长` 写进去即可，抖音发布后会识别为话题。
（发过一条实测：发布后话题正常显示。）

---

## 6 定时预约内容去哪看？不在「审核中」

「审核状态」筛选只有四项：**全部 / 已发布 / 审核中 / 未通过**。

- 预约（定时）内容的卡片上显示：`定时发布中：2026年10月15日 07:00　修改定时`，操作菜单是 **继续编辑 / 作品置顶 / 删除作品**（**没有"设置权限"**）
- 已发布内容的操作菜单是：编辑作品 / 设置权限 / 作品置顶 / 删除作品

所以判断"是否还只是预约"，最直接的是看**有没有「设置权限」**。

筛选「审核中」时预约内容**是空的**，别在那儿找。

---

## 7 列表虚拟滚动，一次只渲染约 12 条

`body.innerText` 只能拿到当前渲染的卡片。抓全量必须滚动累积：

```js
// 找可滚动容器（不是 window）
let best = null;
document.querySelectorAll('div').forEach(c => {
  if (c.scrollHeight > c.clientHeight + 50 && c.clientHeight > 300) best = c;
});
if (best) best.scrollTop += 700;
```

每滚一次抓一次，按 `日期时间 + 标题` 去重累积。

⚠️ **去重别只用日期时间**：同一天同一时刻可能有两条（比如重复发布），会误合并。用 `dt + 标题前 N 字` 当 key。

---

## 8 作品数可以当"总数校验器"

页面顶部 `作品 (N)` 是权威计数：

- 发布前 35 → 排完 28 期后 63
- 多出来 1 条 → 说明有重复，用 `dy-search.js` 搜标题定位

本次实操就靠这个发现了 ep02 重复（第一次发布其实已成功，只是列表未刷新，我重跑导致第二条）。

---

## 9 其他环境坑

| 现象 | 原因 | 解法 |
|---|---|---|
| 批量脚本判成败全错 | macOS BSD grep **不支持 `\|`**（GNU BRE 扩展） | 用 `grep -qE "a\|b"` |
| `TIMES[0]: parameter not set` | zsh 数组下标从 **1** 开始 | 循环变量从 1 起 |
| `net::ERR_ABORTED` 导航失败 | SPA 路由与 goto 抢跑 | `try/catch` 包住 goto，然后 `sleep` 等加载 |
| 页面操作全无反应 | 代理劫持 9222 流量 | 每次跑前 unset 所有 proxy 变量 |
| 点击不生效 | Bash 沙箱隔离 | 传 `dangerouslyDisableSandbox: true` |

---

## 10 发布成功的判据

- toast 出现 **「发布成功」**
- URL 跳到 `creator-micro/content/manage?enter_from=publish`
- 两者都出现才算成功（只跳转可能是失败后的重定向）
