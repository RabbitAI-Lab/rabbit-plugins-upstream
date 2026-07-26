# 环境预检

流程开始前依次执行以下检查。任何一步失败，先尝试自动修复；无法修复则阻断流程并明确报告。

## 1. CLI 依赖检查

### ee-cli

**检查是否安装**：

```bash
command -v ee-cli >/dev/null 2>&1 && echo "installed" || echo "missing"
```

**未安装** → 主动执行：

```bash
npm install -g --registry=http://npm.devops.xiaohongshu.com:7001 @xhs/ee-cli
```

若全局安装权限报错，回退到用户目录：

```bash
npm install -g --registry=http://npm.devops.xiaohongshu.com:7001 --prefix ~/.npm-global @xhs/ee-cli
export PATH="$HOME/.npm-global/bin:$PATH"
```

**版本检查（主动，如已安装）**：

```bash
CURRENT=$(ee-cli version 2>&1 | awk '{print $2}')
LATEST=$(npm view @xhs/ee-cli version --registry=http://npm.devops.xiaohongshu.com:7001 2>/dev/null)
[ "$CURRENT" != "$LATEST" ] && echo "outdated: $CURRENT → $LATEST"
```

**非最新 → 主动执行升级**：

```bash
ee-cli upgrade
```

### hi-cli（用于 hi-docs 报告同步）

**检查是否安装**：

```bash
command -v hi >/dev/null 2>&1 && echo "installed" || echo "missing"
```

**未安装** → 主动执行：

```bash
npm install -g --registry=http://npm.devops.xiaohongshu.com:7001 @xhs/hi-cli
```

**版本检查（主动，如已安装）**：

```bash
CURRENT=$(hi --version 2>/dev/null | awk '{print $NF}')
LATEST=$(npm view @xhs/hi-cli version --registry=http://npm.devops.xiaohongshu.com:7001 2>/dev/null)
[ "$CURRENT" != "$LATEST" ] && echo "outdated: $CURRENT → $LATEST"
```

**非最新 → 主动执行升级**：

```bash
npm install -g --registry=http://npm.devops.xiaohongshu.com:7001 @xhs/hi-cli@latest
```

### git

**检查是否安装**：

```bash
command -v git >/dev/null 2>&1 && echo "installed" || echo "missing"
```

未安装则报错阻断（git 应由操作系统提供，本 skill 不代装）。

## 2. 认证检查

### SSO Token

**检查是否存在**：

```bash
[ -f ~/.token/sso_token.json ] && echo "exists" || echo "missing"
```

**不存在或命令返回 401** → 引导用户：

> "SSO Token 不存在/已过期，请执行 `ee-cli login` 完成 SSO 登录后回复'继续'。"

## 3. Skill 依赖检查

依赖三个 skill：`pingcode-assistant-pro`、`yunxiao-assistant`、`hi-docs`。

**检查是否可用**：查看 `available-skills` 列表（AI 从 system-reminder 中可见）。

**未安装 / 非最新 → 主动执行升级**（`clawhub update` 会自动装或升到最新）：

```bash
clawhub update pingcode-assistant-pro
clawhub update yunxiao-assistant
clawhub update hi-docs
```

若 `clawhub update` 报错（比如网络/权限问题）→ 停止流程，把原始错误呈现给用户，让用户手动排查后重试。

## 4. REDoc 报告归档目录配置

**检查配置文件**：

```bash
[ -f ~/.claude/e2e-delivery/config.json ] && cat ~/.claude/e2e-delivery/config.json
```

**未配置** → 询问用户：

> "首次使用本 skill，请提供 REDoc 报告归档父目录 shortcutId（如 `1e66598189d60b0db7bbd02401c1983f`）。"

用户提供后写入：

```bash
mkdir -p ~/.claude/e2e-delivery
echo '{"redocParentId": "<用户提供的 shortcutId>"}' > ~/.claude/e2e-delivery/config.json
```

## 预检结果

预检全部通过 → 进入流程主体。
任一项无法自动修复 → 停止流程，向用户输出未通过项和修复建议。
