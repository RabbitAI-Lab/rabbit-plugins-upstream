---
name: browser-use
description: |
  Browser automation for web scraping, data collection, and interactive tasks.
  Activate when user asks to browse websites, collect data from pages, click through
  search results, or any task requiring browser interaction.
  OpenClaw uses standard Playwright MCP tools (desktop_* from cu MCP server).
---

# Browser Automation — 浏览器自动化

> Migrated from DuMate's dumate-browser-use patterns.
> Uses OpenClaw's MCP browser tools (playwright MCP + desktop_* from cu MCP server).

---

## 工具映射

| DuMate playwright-cli | OpenClaw MCP | 说明 |
|---------------------|-------------|------|
| `snapshot` | `desktop_screenshot` | 获取页面截图 |
| `click <ref>` | `desktop_left_click [x,y]` | 点击坐标 |
| `fill <ref> "text"` | `desktop_type` | 输入文字 |
| `mousewheel` | `desktop_scroll` | 滚动页面 |
| `goto <url>` | playwright navigate | 导航到URL |
| `tab-list` | `desktop_window_list` | 列出窗口 |
| `screenshot` | `desktop_screenshot` | 截图 |
| `eval` | playwright run-code | 执行JS |

> **坐标获取**：每次 `desktop_screenshot` 后，截图上每个可交互元素都有 `[x,y]` 坐标（0-1000 归一化）。点击前先截图确认元素位置。

---

## 核心工作流

```
1. 截图确认页面 → desktop_screenshot
2. 找到目标坐标 → 点击 / 输入
3. 等待加载 → desktop_wait
4. 截图验证结果 → desktop_screenshot
5. 发现新内容 → 重复
```

---

## 登录 & 验证码检测

当 screenshot 显示登录表单、验证码、滑块验证时：

1. **立即停止所有自动化操作**
2. 通知用户："检测到页面需要登录/验证，请在浏览器中完成操作，完成后回复 **'已完成'** 继续任务。"
3. 等待用户回复"已完成"
4. 重新截图确认登录已通过
5. 继续后续自动化步骤

**绝对禁止：**
- 尝试自动填入用户名/密码绕过登录
- 刷新页面或重新导航来"绕过"登录
- 在检测到登录墙后继续自动化操作

---

## 分页策略

> **必须先读取** `${_SKILL_DIR}/references/pagination.md` 了解分页类型后再执行。

### 识别分页类型

从 screenshot 底部判断：

| 类型 | 识别信号 | 翻页方式 |
|------|---------|---------|
| **无限滚动** | 底部无分页控件，内容随滚动增加 | `desktop_scroll` 滚动 |
| **页码分页** | 有页码数字、"下一页"/"Next"/">"按钮 | 点击按钮坐标 |
| **加载更多按钮** | 有"加载更多"/"Load more"按钮 | 点击按钮坐标 |

### 常见网站分页类型

| 网站 | 分页类型 | 翻页方式 |
|------|---------|---------|
| 淘宝搜索 | 页码分页 | 点击"下一页" |
| 京东搜索 | 页码分页 | 点击"下一页" |
| 小红书 | 无限滚动 | 滚动加载 |
| 抖音 | 无限滚动 | 滚动加载 |
| 百度搜索 | 页码分页 | 点击"下一页" |
| 知乎 | 页码分页 | 点击"下一页" |
| 亚马逊 | 页码分页 | 点击"下一页" |

### 翻页后验证

翻页后必须截图确认：
1. URL 变化（`page=X`）或内容增加
2. "下一页"按钮是否 still 可点击（若消失/disabled = 最后一页）
3. 内容实际变化（不只是等待）

---

## 视频 / 大型 SPA 页面

当页面 URL 包含视频域名（youtube.com、bilibili.com、douyin.com 等）或 screenshot 中出现 `<video>` 标签时：

**禁止**使用 `navigate` + `waitForLoadState('networkidle')` — 视频流持续加载会超时。

正确做法：
1. 先截图确认当前页面
2. 使用 `desktop_wait` 等待元素出现，或 `sleep` 简单等待
3. 若需要导航到视频，用 `desktop_scroll` 滚动确认内容

**大型电商/社交 SPA 页面** 也禁止 `networkidle`，用 `domcontentloaded` 或 `waitForSelector` 替代。

---

## 滚动策略

| 场景 | 命令 | 说明 |
|------|------|------|
| 向下滚动 | `desktop_scroll 0 500` | 归一化坐标，向下500 |
| 向上滚动 | `desktop_scroll 0 -500` | 向上500 |
| 点击"加载更多" | `desktop_left_click [x,y]` | 先截图找坐标 |
| 滚动到底部 | `desktop_scroll 0 1000` × 3次 | 确认无更多内容 |

---

## 批量数据提取

### 流程

```
1. 截图确认页面加载
2. 用 Playwright MCP 提取数据（如 run-code）
3. 截图确认
4. 翻页
5. 重复
```

### 翻页成功判断

| 类型 | 成功信号 | 失败信号 |
|------|---------|---------|
| 无限滚动 | 内容增加，新元素出现 | 连续滚动内容不变 |
| 页码分页 | URL变化，内容更新 | "下一页"按钮消失/disabled |
| 加载更多 | 新内容加载，按钮仍可见 | "已加载全部"出现 |

### 大量翻页建议

- 每 5-10 页暂停几秒，避免触发反爬
- 用 `desktop_wait 2000` 等待内容加载
- 记录已翻页数，到达目标后停止

---

## 坐标系统说明

OpenClaw 桌面控制使用 **归一化坐标（0-1000）**：
- 左上角：`[0, 0]`
- 中心：`[500, 500]`
- 右下角：`[1000, 1000]`

坐标相对于**当前截图内容**，不是绝对像素。

### 获取坐标的步骤

```
1. desktop_screenshot  → 获取当前页面截图
2. 根据截图中的元素位置判断坐标
3. desktop_left_click [x, y]  → 点击目标位置
```

### 常见坐标参考

| 区域 | 坐标 | 说明 |
|------|------|------|
| 页面顶部导航栏 | [500, 50] | 通常居中偏上 |
| 搜索框 | [500, 200] | 页面中上部 |
| 页面底部 | [500, 950] | 居中偏下 |
| 右侧边栏 | [850, 500] | 居中偏右 |

> **实际坐标必须从截图判断**，上述仅供参考。

---

## 错误处理

| 错误 | 原因 | 解决 |
|------|------|------|
| 找不到元素 | 页面未加载完成 | `desktop_wait` 或 `desktop_screenshot` 重试 |
| 点击没反应 | 元素被遮挡或不可见 | `desktop_scroll` 滚动到元素可见后再点 |
| 页面卡住 | SPA 等待 networkidle | 用 `waitForSelector` 或固定 `sleep` |
| 登录墙 | 需要登录态 | 通知用户手动完成登录 |
| 内容不变 | 分页方式错误 | 检查分页类型，换翻页方式 |

---

## Recovery Flow

浏览器操作异常时：

```
1. desktop_screenshot  → 确认当前页面状态
2. 重新截图定位目标元素
3. 重试操作
4. 若仍失败，通知用户问题并停止
```

---

## 工具使用示例

### 导航到网站并截图
```
playwright navigate https://www.baidu.com
desktop_screenshot
```

### 找到并点击搜索框
```
# 从截图判断搜索框大约在 [500, 200]
desktop_left_click 500 200
desktop_type "搜索内容"
desktop_key Enter
desktop_screenshot
```

### 翻页
```
# 从截图找到"下一页"按钮坐标，如 [800, 900]
desktop_left_click 800 900
desktop_wait 2000
desktop_screenshot
```

### 滚动加载
```
desktop_scroll 0 500
desktop_wait 1500
desktop_screenshot
```

### 提取页面文本（用 playwright run-code）
```
playwright run-code "async page => { return await page.textContent('body'); }"
```

---

## 注意事项

1. **每次操作后截图验证** — 不要假设操作成功，必须截图确认
2. **先识别分页类型再翻页** — 读 `${_SKILL_DIR}/references/pagination.md`
3. **登录检测优先级最高** — 检测到立即停止并通知用户
4. **视频/SPA 页面不用 networkidle** — 会超时
5. **坐标从截图判断** — 不要硬编码绝对坐标
6. **大量翻页要暂停** — 避免反爬