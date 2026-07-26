# Pagination Strategy — 分页策略

翻页前必须先**识别页面的分页类型**，选择正确的翻页方式。错误的方式会导致无法加载新内容。

---

## 步骤 1：识别分页类型

从 snapshot 判断页面使用哪种分页方式：

| 类型 | 识别信号 | 翻页方式 |
|------|---------|---------|
| **无限滚动** | 底部有"加载更多"或无分页控件，内容随滚动增加 | `mousewheel` 滚动 |
| **页码分页** | 底部有页码数字（1, 2, 3...）、"下一页"/"Next"/">"按钮 | 点击页码或"下一页"按钮 |
| **加载更多按钮** | 底部有"加载更多"/"Load more"/"查看更多"按钮 | 点击该按钮 |
| **瀑布流** | 电商/社交媒体卡片布局，无明确分页 | 滚动到底部检查是否加载新内容 |

### 常见网站分页类型

| 网站 | 分页类型 | 翻页方式 |
|------|---------|---------|
| 淘宝搜索 | 页码分页 | 点击页码或"下一页" |
| 京东搜索 | 页码分页 | 点击页码或"下一页" |
| 小红书 | 无限滚动 | 滚动加载 |
| 抖音 | 无限滚动 | 滚动加载 |
| 百度搜索 | 页码分页 | 点击页码 |
| 微博 | 页码分页 | 点击页码 |
| 知乎 | 页码分页 | 点击页码 |
| 亚马逊 | 页码分页 | 点击页码 |
| B站 | 页码分页 | 点击页码或"下一页" |

---

## 步骤 2：执行翻页

### 类型 A：无限滚动 / 瀑布流

```bash
source "${_SKILL_DIR}/scripts/session-header.sh"

# 向下滚动
playwright-cli mousewheel 0 800

# 等待加载后重新获取快照
sleep 2 && playwright-cli snapshot && _pw_snap
```

**注意**：如果滚动多次后内容不再增加，可能是页码分页网站，检查底部是否有"下一页"按钮。

### 类型 B：页码分页

```bash
source "${_SKILL_DIR}/scripts/session-header.sh"

# 从 snapshot 找到"下一页"、">"、">>"、"Next"按钮的 ref
playwright-cli click <ref>   # 例如: playwright-cli click e42

# 等待页面加载
sleep 2 && playwright-cli snapshot && _pw_snap
```

**备选方式**：点击具体页码

```bash
# 直接点击页码数字（如 "2"、"3"、"下一页"）
playwright-cli click <ref>
sleep 2 && playwright-cli snapshot && _pw_snap
```

### 类型 C：加载更多按钮

```bash
source "${_SKILL_DIR}/scripts/session-header.sh"

# 从 snapshot 找到"加载更多"/"Load more"/"查看更多"按钮
playwright-cli click <ref>

# 等待新内容加载
sleep 2 && playwright-cli snapshot && _pw_snap
```

---

## 步骤 3：判断翻页成功

| 分页类型 | 成功信号 | 失败信号 |
|---------|---------|---------|
| 无限滚动 | snapshot 内容增加，出现新元素 | 滚动后内容不变，出现"没有更多了" |
| 页码分页 | URL 变化（`page=X`），内容更新 | "下一页"按钮 disabled 或消失 |
| 加载更多 | 新内容加载，按钮仍可点击 | 出现"已加载全部"，按钮消失 |

### 检查翻页成功的代码

```bash
# 方法1：检查 URL 变化（适用于页码分页）
playwright-cli eval "window.location.href"

# 方法2：记录内容数量对比
# 翻页前记录元素数量，翻页后对比是否变化

# 方法3：检查"下一页"按钮状态
# 如果按钮变成 disabled 或消失，说明已到最后一页
```

---

## 常见问题排查

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 一直滚动但不加载新内容 | 是页码分页，不是无限滚动 | 检查 snapshot 底部是否有页码/下一页按钮，改为点击 |
| 点击下一页没反应 | 按钮可能是 disabled 或需要等待 | 先 `sleep 1` 再点击，或滚动到底部让按钮可见 |
| 翻页后内容相同 | 页面是 AJAX 加载，URL 不变 | 用 `waitForSelector` 等待新内容加载 |
| 不知道还有没有下一页 | 检查"下一页"按钮状态 | 点击前先判断按钮是否 disabled |
| 页码按钮被遮挡 | 页面需要滚动到分页区域 | 先 `mousewheel 0 800` 滚动到底部 |
| 点击页码后跳转到首页 | 可能未登录或触发了反爬 | 检查是否需要登录，降低操作频率 |

---

## 最佳实践

### 1. 翻页前先判断类型

```bash
# 步骤1：获取快照，检查分页控件
playwright-cli snapshot && _pw_snap

# 步骤2：从 snapshot 判断分页类型
# - 看到 "下一页" / "Next" / ">" / 页码数字 → 页码分页
# - 看到 "加载更多" / "Load more" → 加载更多按钮
# - 底部无分页控件 → 可能是无限滚动

# 步骤3：选择正确的翻页方式
```

### 2. 翻页后验证

```bash
# 翻页后必须重新 snapshot 确认内容变化
playwright-cli click <next_page_ref>
sleep 2 && playwright-cli snapshot && _pw_snap

# 如果内容未变化，可能翻页失败，换一种方式
```

### 3. 到达最后一页的判断

```bash
# 页码分页：检查"下一页"按钮状态
# - 按钮消失 → 已到最后一页
# - 按钮 disabled（灰色） → 已到最后一页

# 无限滚动：检查是否出现提示
# - "没有更多了" / "已显示全部" → 已到最后一页
# - 连续滚动2次内容不变 → 可能已到最后一页
```

### 4. 大量翻页时的建议

```bash
# 每翻几页后适当等待，避免触发反爬
for i in {1..5}; do
    playwright-cli click <next_page_ref>
    sleep 3  # 适当延长等待时间
    playwright-cli snapshot && _pw_snap
done
```

---

## 示例：京东搜索翻页

```bash
source "${_SKILL_DIR}/scripts/session-header.sh"

# 1. 搜索并获取快照
_pw_open "https://search.jd.com/Search?keyword=手机"
playwright-cli snapshot && _pw_snap

# 2. 检查分页类型：京东是页码分页
# 从 snapshot 找到"下一页"按钮的 ref（通常是 ">" 或 "下一页" 文字）

# 3. 点击下一页
playwright-cli click <ref>  # 例如 e50 是下一页按钮

# 4. 等待加载并验证
sleep 2 && playwright-cli snapshot && _pw_snap

# 5. 检查 URL 或内容是否变化
playwright-cli eval "window.location.href"
# 应该看到 page=2 或类似参数
```

---

## 示例：淘宝搜索翻页

```bash
source "${_SKILL_DIR}/scripts/session-header.sh"

# 1. 搜索并获取快照
_pw_open "https://s.taobao.com/search?q=手机"
playwright-cli snapshot && _pw_snap

# 2. 检查分页类型：淘宝是页码分页
# 从 snapshot 找到页码数字或"下一页"按钮

# 3. 滚动到底部让分页控件可见
playwright-cli mousewheel 0 800
sleep 1 && playwright-cli snapshot && _pw_snap

# 4. 点击下一页
playwright-cli click <ref>

# 5. 等待加载
sleep 2 && playwright-cli snapshot && _pw_snap
```

---

## 示例：无限滚动页面

```bash
source "${_SKILL_DIR}/scripts/session-header.sh"

# 持续滚动加载内容
for i in {1..10}; do
    # 记录当前内容数量
    playwright-cli snapshot && _pw_snap

    # 滚动
    playwright-cli mousewheel 0 800
    sleep 2

    # 获取新快照，检查内容是否增加
    playwright-cli snapshot && _pw_snap

    # 如果内容不再增加，退出循环
    # 判断方式：元素数量不变，或出现"没有更多了"
done
```

---

## 示例：页码分页（使用 JavaScript 点击）

当 snapshot 中的 ref 不稳定时，可以使用 JavaScript 直接点击分页按钮：

### 检查分页按钮状态

```bash
# 通用模板：检查下一页按钮是否存在且可点击
playwright-cli eval "() => {
  // 根据实际页面修改选择器
  const nextBtn = document.querySelector('<下一页按钮选择器>');
  if (!nextBtn) return { hasNext: false, reason: 'button not found' };
  // 检查禁用状态（根据实际页面修改类名或属性）
  if (nextBtn.classList.contains('<禁用类名>') || nextBtn.disabled) {
    return { hasNext: false, reason: 'button disabled' };
  }
  return { hasNext: true };
}"
```

### 点击下一页

```bash
source "${_SKILL_DIR}/scripts/session-header.sh"

# 通用模板：使用 JavaScript 点击下一页
playwright-cli eval "() => {
  const nextBtn = document.querySelector('<下一页按钮选择器>');
  if (nextBtn && !nextBtn.classList.contains('<禁用类名>')) {
    nextBtn.click();
    return { clicked: true };
  }
  return { clicked: false, reason: 'button disabled or not found' };
}"

# 等待页面加载
sleep 3 && playwright-cli snapshot && _pw_snap
```

---

## 示例：批量翻页提取数据

```bash
source "${_SKILL_DIR}/scripts/session-header.sh"

# 导航到目标页面
_pw_open "<目标URL>"
playwright-cli snapshot && _pw_snap

# 批量翻页
for page in {1..20}; do
  echo "=== Page ${page} ==="

  # 1. 提取当前页数据（根据实际页面修改选择器）
  data=$(playwright-cli eval "() => {
    const results = [];
    // 修改为实际页面中的列表项选择器
    const items = document.querySelectorAll('<列表项选择器>');
    items.forEach(item => {
      // 修改为实际需要提取的字段
      const title = item.querySelector('<标题选择器>')?.textContent.trim();
      const link = item.querySelector('<链接选择器>')?.href;
      if (title && link) {
        results.push({ title, link });
      }
    });
    return JSON.stringify(results);
  }")
  echo "$data"

  # 2. 检查是否有下一页
  has_next=$(playwright-cli eval "() => {
    const nextBtn = document.querySelector('<下一页按钮选择器>');
    // 检查按钮存在且未禁用
    if (!nextBtn) return 'false';
    if (nextBtn.classList.contains('<禁用类名>') || nextBtn.disabled) return 'false';
    return 'true';
  }")

  if [ "$has_next" = "false" ]; then
    echo "Reached last page"
    break
  fi

  # 3. 点击下一页
  playwright-cli eval "() => {
    document.querySelector('<下一页按钮选择器>').click();
  }"

  # 4. 等待加载
  sleep 3 && playwright-cli snapshot && _pw_snap
done
```

### 注意事项

1. **选择器获取**：先 `snapshot` 查看页面结构，找到实际的分页元素选择器
2. **等待时间**：复杂页面使用 `sleep 3` 或更长，确保内容加载完成
3. **滚动到底部**：如果分页控件不可见，先 `mousewheel 0 1000` 滚动
4. **反爬检测**：连续翻页过多可能触发验证，每 5-10 页暂停几秒