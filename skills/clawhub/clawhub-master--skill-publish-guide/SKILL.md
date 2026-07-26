---
slug: clawhub-publish-guide
displayName: ClawHub 发布指南 · 技能发布步骤
version: 1.0.0
summary: 完整的 ClawHub 技能发布步骤，让任何 Agent 照着做就能发布
license: MIT
---

# ClawHub 发布指南 · 技能发布步骤

> 适用于：将技能发布到 ClawHub，供所有 Agent 安装使用。

---

## 发布前准备

### 第一步：确认环境

确保已安装 `clawhub` CLI 并已登录：

```bash
# 查看版本
clawhub --cli-version

# 确认登录状态
clawhub whoami
# ✅ 输出 "clawhub-master" 表示已登录
```

**未登录？执行登录：**

```bash
clawhub login
# 会自动打开浏览器，按提示操作即可
```

### 第二步：整理技能目录

技能目录结构必须包含以下文件：

```
your-skill/
├── SKILL.md          # 必须：技能元数据（slug、version、description）
├── *.cjs 或 *.js     # 必须：核心代码
└── README.md         # 可选：使用说明
```

**SKILL.md 模板（必须字段）：**

```yaml
---
slug: your-skill-slug      # 唯一标识，只能用字母、数字、连字符
displayName: 你的技能名称
version: 1.0.0             # 语义化版本，每次发布可递增
summary: 一句话描述技能功能
license: MIT               # 推荐 MIT
---
```

---

## 发布方式一：sync（推荐，自动扫描）

适合已有完整技能目录，一键发布/更新：

```bash
# 进入 skills 父目录
cd D:\openclaw-data\workspace\skills

# 干跑（预览会发布什么）
clawhub sync --dry-run

# 确认无误后，正式发布（--all 跳过确认）
clawhub sync --all --bump patch --changelog "更新说明"
```

**版本号规则：**
- `--bump patch` — 小修复，如 bugfix（1.0.0 → 1.0.1）
- `--bump minor` — 新功能，向下兼容（1.0.0 → 1.1.0）
- `--bump major` — 破坏性更新（1.0.0 → 2.0.0）

---

## 发布方式二：publish（手动指定）

适合精确控制发布参数：

```bash
clawhub publish <技能目录路径> \
  --slug your-skill-slug \
  --name "你的技能名称" \
  --version 1.0.0 \
  --changelog "修复了 XXX 问题"
```

**示例：**

```bash
clawhub publish D:\openclaw-data\workspace\skills\social-spark \
  --slug social-spark \
  --name "social-spark · 社交热评技能" \
  --version 1.0.1 \
  --changelog "新增全网热搜过滤关键词：宇树、机器人"
```

---

## 发布后验证

### 查看已发布的技能

```bash
# 查看自己发布的技能
clawhub inspect your-skill-slug
```

### 查看所有已安装技能（含第三方）

```bash
clawhub list
```

### 安装验证（从另一个目录测试）

```bash
# 新建测试目录
mkdir test-skill && cd test-skill

# 安装自己发布的技能
clawhub install your-skill-slug

# 验证安装成功
ls skills/your-skill-slug/
```

---

## 常见问题

### Q：slug 被占用怎么办？

换一个 slug，如 `your-skill-v2`，或到 clawhub.com 搜索该 slug 是否已存在。

### Q：登录失败/Token 无效？

```bash
clawhub logout
clawhub login
```

### Q：想更新已发布的技能？

直接再次运行 `clawhub sync --all` 或 `clawhub publish --version x.x.x`，会自动更新。

### Q：发布后想隐藏/删除？

```bash
clawhub hide your-skill-slug    # 隐藏
clawhub delete your-skill-slug  # 软删除
```

### Q：不知道技能目录是否正确？

```bash
# 先干跑看输出
clawhub sync --dry-run

# 确认 SKILL.md 是否被识别
clawhub inspect your-skill-slug
```

---

## 完整示例（以 social-spark 为例）

```bash
# 1. 确认环境
clawhub whoami
# ✅ clawhub-master

# 2. 进入 skills 目录
cd D:\openclaw-data\workspace\skills

# 3. 干跑确认
clawhub sync --dry-run
# 输出应包含 social-spark

# 4. 正式发布
clawhub sync --all --bump minor --changelog "新增全网热搜 + AI关键词过滤 v2.1"

# 5. 验证
clawhub inspect social-spark
# ✅ 显示版本号和描述即成功
```

---

## 关键文件位置参考

| 路径 | 说明 |
|:---|:---|
| `D:\openclaw-data\workspace\skills\` | 技能根目录 |
| `D:\openclaw-data\workspace\skills\social-spark\` | social-spark 完整源码 |
| `%USERPROFILE%\.clawhub\token` | 登录 Token（一般不需手动碰） |

---

*Created by Worker-A · 2026-06-27*