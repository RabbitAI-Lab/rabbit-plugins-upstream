# learnings/ — 站点经验积累

ego-lite Windows 会在每次成功操作后把经验写入对应域名的 `.md` 文件。
Agent 下次遇到相同站点时自动读取，跳过已知的坑。

## 格式

```markdown
# github.com

## 已知问题
- 登录框在 iframe 中，snapshot 会显示 iframe 前缀
- 点击 "New issue" 按钮有时在 shadow DOM 内，但 CDP AX 树能获取

## 成功模式
- 点击 `@N [link] "Issues"` 前需要先等待页面加载完成
- `fillInput` 对 GitHub 输入框工作正常（不需要特殊处理）

## 快捷操作
- 翻页：用 `await pressKey('End')` 滚动到底部
- 搜索：GitHub 搜索框 role=textbox，name="Search"
```

## 如何工作

Agent 脚本中调用 `learn(site, note)` 会追加到对应文件。
以后遇到同站点，Agent 自动读取经验文件。
