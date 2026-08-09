---
name: git-workflow-and-versioning
version: 1.0.0
description: "Manage Git commits, branches, merges, and versioning with structured workflows"
tags: [debugging, devops, file-based, visual, template-based]
triggers:
  - git 工作�?  - 提交规范
  - 分支策略
  - 语义化版�?  - changelog
  - commit message
  - 原子提交
  - git workflow
  - versioning
  - 打标�?  - 发布版本
---

# Git Workflow and Versioning �?Git 工作流与版本管理 v1.0

> 来源：Anthropic 官方 git-workflow-and-versioning skill�?> 核心理念：Git 是安全网。提交是存档点，分支是沙盒，历史是文档�?
## 你是�?
你是一�?Git 工作流和版本管理专家，专注于保持变更可管理、可审查、可逆。在 AI agent 高速生成代码的时代，纪律严明的版本控制是保持变更可控的机制�?
## 何时使用

**永远�?* 每次代码变更都通过 git 流转�?
## 核心原则

### Trunk-Based Development（推荐）

保持 `main` 始终可部署。在短生命周期的特性分支上工作�?-3 天内合并回主分支。长生命周期的开发分支是隐藏成本——它们分歧、制造合并冲突、延迟集成。DORA 研究一致表�?trunk-based development 与高绩效工程团队相关�?
```
main ──●──●──●──●──●──●──●──●──●──  (始终可部�?
        �?     �? �?   �?         ●──●─�?   ●──�?   �?短生命周期特性分�?(1-3 �?
```

这是推荐的默认方式。使�?gitflow 或长生命周期分支的团队可以调整原则（原子提交、小变更、描述性消息）到他们的分支模型——提交纪律比具体分支策略更重要�?
- **开发分支是成本�?* 分支每活一天，就累积合并风险�?- **发布分支可接受�?* 当需要在 main 继续前进时稳定发布�?- **功能开�?> 长分支�?* 优先在开关后部署未完成工作，而非在分支上保留数周�?
### 1. 早提交，频繁提交

每个成功的增量都有自己的提交。不要累积大量未提交的变更�?
```
工作模式�?  实现切片 �?测试 �?验证 �?提交 �?下一个切�?
而非这样�?  实现所有东�?�?希望它能工作 �?巨大提交
```

提交是存档点。如果下一个变更破坏了东西，你可以立即回退到上一个已知良好状态�?
### 2. 原子提交

每个提交做一件逻辑上的事：

```
# 好：每个提交自包�?git log --oneline
a1b2c3d 添加任务创建端点及验�?d4e5f6g 添加任务创建表单组件
h7i8j9k 连接表单�?API 并添加加载状�?m1n2o3p 添加任务创建测试（单�?+ 集成�?
### 完成条件

- **提交完成条件**：每�?commit 是原子的（做一件事），commit message 符合祈使句格式（�?添加 X 端点及验�?），`git diff HEAD~1 --stat` 显示变更范围合理（≤ 5 文件）�?- **分支完成条件**：特性分支生命周�?�?3 天，�?main 无冲突，CI 通过，准备合并�?- **版本发布完成条件**：语义化版本号已确定（MAJOR.MINOR.PATCH），changelog 已更新，tag 已创建�?
# 差：所有东西混在一�?git log --oneline
x1y2z3a 添加任务功能，修复侧边栏，更新依赖，重构工具
```

### 3. 描述性消�?
提交消息解释*为什�?，而非�?是什�?�?
```
# 好：解释意图
feat: 为注册端点添加邮箱验�?
防止无效邮箱格式到达数据库�?在路由处理器层使�?Zod schema 验证�?�?auth.ts 中现有验证模式一致�?
# 差：描述�?diff 显而易见的东西
update auth.ts
```

**格式�?*
```
<type>: <简短描�?

<可选正文解释为什么，而非是什�?
```

**类型�?*
- `feat` �?新功�?- `fix` �?Bug 修复
- `refactor` �?既不修复 bug 也不添加功能的代码变�?- `test` �?添加或更新测�?- `docs` �?仅文�?- `chore` �?工具、依赖、配�?
### 4. 保持关注点分�?
不要将格式化变更与行为变更混合。不要将重构与功能混合。每种类型的变更应该是单独的提交——理想情况下是单独的 PR�?
```
# 好：分离关注�?git commit -m "refactor: 提取验证逻辑到共享工�?
git commit -m "feat: 为注册添加电话号码验�?

# 差：混合关注�?git commit -m "重构验证并添加电话号码字�?
```

**将重构与功能工作分离�?* 重构变更和功能变更是两个不同的变更——分别提交。这使每个变更更容易审查、回退和在历史中理解。小清理（重命名变量）可以在审查者判断下包含在功能提交中�?
### 5. 控制变更大小

目标每个提交/PR �?100 行。超过约 1000 行的变更应该拆分。参�?`code-review` 中的拆分策略了解如何分解大变更�?
```
~100 �?  �?容易审查，容易回退
~300 �?  �?单一逻辑变更可接�?~1000 �? �?拆分为更小变�?```

## 分支策略

### 特性分�?
```
main (始终可部�?
  �?  ├── feature/task-creation    �?每个分支一个功�?  ├── feature/user-settings    �?并行工作
  └── fix/duplicate-tasks      �?Bug 修复
```

- �?`main`（或团队默认分支）分�?- 保持分支短生命周期（1-3 天内合并）——长生命周期分支是隐藏成�?- 合并后删除分�?- 对未完成功能优先使用功能开关而非长生命周期分�?
### 分支命名

```
feature/<简短描�?   �?feature/task-creation
fix/<简短描�?       �?fix/duplicate-tasks
chore/<简短描�?     �?chore/update-deps
refactor/<简短描�?  �?refactor/auth-module
```

## 使用 Worktrees

对于并行 AI agent 工作，使�?git worktrees 同时运行多个分支�?
```bash
# 为特性分支创�?worktree
git worktree add ../project-feature-a feature/task-creation
git worktree add ../project-feature-b feature/user-settings

# 每个 worktree 是独立目录，有自己的分支
# Agent 可以并行工作而不干扰
ls ../
  project/              �?main 分支
  project-feature-a/    �?task-creation 分支
  project-feature-b/    �?user-settings 分支

# 完成后，合并并清�?git worktree remove ../project-feature-a
```

好处�?- 多个 agent 可以同时在不同功能上工作
- 无需分支切换（每个目录有自己的分支）
- 如果一个实验失败，删除 worktree——没有东西丢�?- 变更在显式合并前是隔离的

## Save Point 模式

```
Agent 开始工�?    �?    ├── 做变�?    �?  ├── 测试通过�?�?提交 �?继续
    �?  └── 测试失败�?�?回退到最后提�?�?调查
    �?    ├── 做另一个变�?    �?  ├── 测试通过�?�?提交 �?继续
    �?  └── 测试失败�?�?回退到最后提�?�?调查
    �?    └── 功能完成 �?所有提交形成干净历史
```

这个模式意味着你永远不会丢失超过一个增量的工作。如�?agent 偏离轨道，`git reset --hard HEAD` 带你回到上一个成功状态�?
## 变更摘要

任何修改后，提供结构化摘要。这使审查更容易，记录范围纪律，并发现意外变更：

```
所做的变更�?- src/routes/tasks.ts: �?POST 端点添加验证中间�?- src/lib/validation.ts: 使用 Zod 添加 TaskCreateSchema

未触及的内容（有意）�?- src/routes/auth.ts: 有类似验证缺口但超出范围
- src/middleware/error.ts: 错误格式可以改进（单独任务）

潜在关注点：
- Zod schema 很严格——拒绝额外字段。确认这是期望的�?- 添加�?zod 作为依赖�?2KB gzipped）——已�?package.json �?```

这个模式及早捕获错误假设，给审查者清晰的变更地图�?未触�?部分特别重要——它显示你执行了范围纪律，没有进行未经请求的改造�?
## 预提交检�?
每次提交前：

```bash
# 1. 检查即将提交的内容
git diff --staged

# 2. 确保无密�?git diff --staged | grep -i "password\|secret\|api_key\|token"

# 3. 运行测试
npm test

# 4. 运行 lint
npm run lint

# 5. 运行类型检�?npx tsc --noEmit
```

�?git hooks 自动化：

```json
// package.json (使用 lint-staged + husky)
{
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,md}": ["prettier --write"]
  }
}
```

## 处理生成文件

- **仅提交项目期望的生成文件**（如 `package-lock.json`、Prisma 迁移�?- **不要提交** 构建输出（`dist/`、`.next/`）、环境文件（`.env`）、或 IDE 配置（`.vscode/settings.json` 除非共享�?- **�?`.gitignore`** 覆盖：`node_modules/`、`dist/`、`.env`、`.env.local`、`*.pem`

## 使用 Git 调试

```bash
# 找到引入 bug 的提�?git bisect start
git bisect bad HEAD
git bisect good <known-good-commit>
# Git checkout 中点；在每个点运行测试缩小范�?
# 查看最近变�?git log --oneline -20
git diff HEAD~5..HEAD -- src/

# 找到最后修改特定行的人
git blame src/services/task.ts

# 搜索提交消息中的关键�?git log --grep="validation" --oneline
```

## 发布与版本管�?
提交是你追踪变更的方式；**版本**是你的消费者追踪它的方式。当任何其他东西依赖你的代码——另一个团队、发布的包、部署的客户端—�?main 上最新的"不再�?我在运行什么，升级安全吗？"的足够答案。版本号和变更日志是回答这个问题的契约�?
### 语义化版�?
对于有消费者的任何东西，版�?`MAJOR.MINOR.PATCH`，让数字承载意义�?
```
  MAJOR  破坏性变�?�?消费者必须改变代码才能升�?  MINOR  新功能，向后兼容 �?升级安全
  PATCH  bug 修复，向后兼�?�?升级安全
```

数字是承诺，所以让代码匹配它。一个改变消费者依赖行为的"patch"是穿着伪装�?major（Hyrum 定律——参�?`api-and-interface-design` skill）。当不确定变更是否破坏性时，假设它是；意外�?major 比损坏的消费者便宜得多�?
### 标签发布，让标签成为真实来源

发布是历史中不可变的点，不是移动的分支。标签化它以便始终可以复现：

```bash
git tag -a v1.4.0 -m "Release 1.4.0"
git push origin v1.4.0
```

从标签派生版本，而非在分散文件中手动编辑，这样制品、标签和变更日志永远不会不一致�?
### 保持为人编写的变更日�?
变更日志不是 `git log`。它是精心策划的、面向消费者的答案—�?变更了什么，我在意吗�?——按 `Added / Changed / Fixed / Deprecated / Removed / Security` 分组，最新的在前，每个条目围绕用户影响而非内部机制表述�?
```markdown
## [1.4.0] - 2025-06-12
### Added
- 通过 CSV 批量导入任务
### Fixed
- 循环任务日期的时区漂�?### Deprecated
- `GET /v1/tasks/all` �?使用分页�?`GET /v1/tasks`�?.0 中移除）
```

在做出变更的同一个变更中编写条目，当影响还新鲜时——而非在发布时从提交考古中重建。破坏性变更获得迁移说明和弃用窗口（遵�?`deprecation-and-migration` skill）；发布实际发布�?`shipping-and-launch` skill 的工作——这部分是喂给它的版本契约�?
## 常见借口 vs 现实

| 借口 | 现实 |
|------|------|
| "等功能完成再提交" | 一个巨大提交无法审查、调试或回退。每个切片都提交�?|
| "消息不重�? | 消息是文档。未来的你（和未来的 agent）需要理解变更了什么和为什么�?|
| "以后 squash" | Squashing 破坏开发叙事。从一开始就优先干净的增量提交�?|
| "分支增加开销" | 短生命周期分支是免费的，防止冲突工作碰撞。长生命周期分支才是问题—�?-3 天内合并�?|
| "以后拆分这个变更" | 大变更更难审查、部署风险更大、更难回退。提交前拆分，而非之后�?|
| "我不需�?.gitignore" | 直到带生产密钥的 `.env` 被提交。立即设置�?|
| "只是小修复，�?patch" | 检查消费者能观察到什么。他们依赖的行为变更�?major，无�?diff 大小�?|
| "变更日志就是提交日志" | 提交是给你的；变更日志是给消费者的，按影响策划。从原始提交生成一个会埋没重要的东西�?|
| "我们在发布时写变更日�? | 到那时影响是从记忆和一半缺失中重建的。在变更时编写条目�?|

## 红旗

- 大量未提交变更累�?- 提交消息�?"fix"�?update"�?misc"
- 格式化变更与行为变更混合
- 项目中没�?`.gitignore`
- 提交 `node_modules/`、`.env`、或构建制品
- �?main 显著分歧的长生命周期分支
- 强制推送到共享分支
- 破坏性变更以 minor �?patch 版本发布
- 发布没有标签，或版本号与标签不同步手动编�?- 面向用户的发布没有变更日志条目，或变更日志只是倾倒提交消�?
## 验证清单

每次提交�?
- [ ] 提交做一件逻辑上的�?- [ ] 消息解释为什么，遵循类型约定
- [ ] 提交前测试通过
- [ ] diff 中无密钥
- [ ] 无仅格式化变更与行为变更混合
- [ ] `.gitignore` 覆盖标准排除

每次发布（有消费者的任何东西）：

- [ ] 版本升级匹配变更：破坏�?�?major，添�?�?minor，修�?�?patch
- [ ] 发布已标签，版本从标签派生，非手动编辑不同步
- [ ] 变更日志有精心策划的、人类可读的条目，按此版本的影响分组

## 使用示例

### 示例1: 功能开发的提交策略

**用户输入**�?```
我在开发用户认证功能，应该怎么提交�?```

**输出**�?```markdown
## 推荐提交流程

### 分支
```bash
git checkout -b feature/user-auth
```

### 提交序列
```bash
# 1. 数据模型
git commit -m "feat: 添加 User 模型和数据库迁移"

# 2. 基础 API
git commit -m "feat: 添加注册端点 POST /api/auth/register"

# 3. 验证
git commit -m "feat: 为注册添加邮箱和密码验证"

# 4. 登录
git commit -m "feat: 添加登录端点 POST /api/auth/login"

# 5. JWT
git commit -m "feat: 添加 JWT token 生成和验证中间件"

# 6. 测试
git commit -m "test: 添加认证流程集成测试"

# 7. 文档
git commit -m "docs: 添加认证 API 文档"
```

### 每个提交
- 原子性（一件逻辑事）
- 测试通过
- 无密�?- 描述性消�?```

### 示例2: 发布版本

**用户输入**�?```
准备发布 v1.4.0，需要做什么？
```

**输出**�?```markdown
## 发布检查清�?
### 1. 版本升级判断
- 有破坏性变更？ �?MAJOR (v2.0.0)
- 有新功能，向后兼容？ �?MINOR (v1.4.0)
- �?bug 修复�?�?PATCH (v1.3.1)

### 2. 执行发布
```bash
# 确保�?main 且最�?git checkout main
git pull

# 运行所有测�?npm test

# 打标�?git tag -a v1.4.0 -m "Release 1.4.0"
git push origin v1.4.0
```

### 3. 变更日志
```markdown
## [1.4.0] - 2026-07-07
### Added
- 用户认证功能 (#42)
- 批量任务导入 (#43)
### Fixed
- 时区漂移问题 (#44)
### Deprecated
- `GET /v1/tasks/all` �?使用分页版本
```
```

## 与其他技能的关系

| 技�?| 关系 |
|------|------|
| **code-review** | 审查时检查提交纪律（原子提交/描述性消�?关注点分离） |
| **ci-cd-and-automation** | CI 流水线中自动化测试和 lint 检�?|
| **deprecation-and-migration** | 弃用窗口和迁移说明在变更日志中记�?|
| **api-and-interface-design** | Hyrum 定律影响版本升级判断 |
| **debugging-and-error-recovery** | git bisect 用于定位引入 bug 的提�?|

## 约束

- **原子提交**：每个提交做一件逻辑�?- **描述性消�?*：解释为什么，非是什�?- **关注点分�?*：重构与功能分开提交
- **早提交频繁提�?*：不累积大量未提交变�?- **测试后提�?*：提交前确保测试通过
- **版本是承�?*：让代码匹配版本�?
---

*Version 1.0.0 �?来源：Anthropic 官方 git-workflow-and-versioning skill*
