---
name: dawn-code-master
description: >
  Dawn Code Master v5.0 — 综合编码技能，整合了focused-fix、PR review、规格驱动开发、API设计审查、
  E2E测试、去AI味写作、自评系统等30+ GitHub顶级编码技能的最佳实践。
  写代码、修bug、审PR、做设计，按这个来。
metadata:
  version: 5.0.0
  sources:
    - focused-fix (alirezarezvani/claude-skills)
    - pr-review-expert (alirezarezvani/claude-skills)
    - spec-driven-workflow (alirezarezvani/claude-skills)
    - api-design-reviewer (alirezarezvani/claude-skills)
    - api-test-suite-builder (alirezarezvani/claude-skills)
    - self-eval (alirezarezvani/claude-skills)
    - skill-tester (alirezarezvani/claude-skills)
    - mcp-server-builder (alirezarezvani/claude-skills)
    - e2e-skills (voidmatcha/e2e-skills)
    - avoid-ai-writing (conorbronsdon/avoid-ai-writing)
    - cc-skills-golang (samber/cc-skills-golang)
    - agentic-stack (codejunkie99/agentic-stack)
    - antigravity-skills (krishnakanthb13)
    - codebase-onboarding / migration-architect / ci-cd-pipeline-builder
    - performance-profiler / database-designer / sql-database-assistant
    - observability-designer / ship-gate / tech-debt-tracker
    - changelog-generator / dependency-auditor / git-worktree-manager
    - monorepo-navigator / rag-architect / agent-designer / agent-workflow-designer
    - dawn-code-master v4.0 (本地)
  dawn:
    requires:
      bins: [python, node, pwsh, git]
    permissions:
      - exec: [python, node, ruff, black, pytest, pwsh, git]
      - filesystem: [read/write workspace]
---

# Dawn Code Master v5.0

**30+ GitHub顶级编码技能 → 1个综合技能。** 写代码、修bug、审PR、做设计，按这个来。

---

## 目录

1. [写代码铁律](#1-写代码铁律)
2. [修复Bug流程（focused-fix）](#2-修复bug流程focused-fix)
3. [PR审查清单（pr-review-expert）](#3-pr审查清单pr-review-expert)
4. [规格驱动开发（spec-driven-workflow）](#4-规格驱动开发spec-driven-workflow)
5. [API设计审查](#5-api设计审查)
6. [E2E测试暗坑检测](#6-e2e测试暗坑检测)
7. [去AI味写作检查（avoid-ai-writing）](#7-去ai味写作检查avoid-ai-writing)
8. [自评系统（self-eval）](#8-自评系统self-eval)
9. [代码迁移指南（migration-architect）](#9-代码迁移指南migration-architect)
10. [CI/CD流水线构建](#10-cicd流水线构建)
11. [数据库设计](#11-数据库设计)
12. [MCP服务器构建](#12-mcp服务器构建)
13. [可观测性设计](#13-可观测性设计)
14. [发布门禁](#14-发布门禁)
15. [技术债务追踪](#15-技术债务追踪)
16. [每种语言速查](#16-每种语言速查)

---

## 1. 写代码铁律

### 提交前必查清单

```
[ ] py_compile / tsc / go build — 语法干净
[ ] pytest / npm test / go test — 全绿
[ ] 所有公开函数有类型提示
[ ] 没有裸 except / 没有 any
[ ] 没有硬编码密钥
[ ] f-string / 模板字面量 — 不用 format() 或 %
[ ] pathlib / fs 路径 — 不用 os.path
[ ] 所有公开API有文档字符串
[ ] 没有函数超过30行
[ ] PowerShell: 完整路径用于 cron argv
```

### 文件结构铁律

```
每个文件不超过300行。
每个函数不超过30行。
每个函数只做一件事。
```

### 错误处理铁律

```
所有异步操作必须有错误处理。
所有网络请求必须超时。
所有用户输入必须验证。
所有外部依赖必须假设会失败。
```

### 命名铁律

```
Python: snake_case, 类用 PascalCase
TypeScript: camelCase, 类/类型用 PascalCase
Go: camelCase, 导出用大写开头
PowerShell: 动-名 格式，如 Get-Item
```

---

## 2. 修复Bug流程（focused-fix）

**铁律：** 不跑完前三阶段，不给修。

```
NO FIXES WITHOUT COMPLETING SCOPE → TRACE → DIAGNOSE FIRST
```

### Phase 1: SCOPE — 划定范围

1. 确认哪个功能/模块需要修
2. 找出主文件夹和所有文件
3. 读每个文件，理解用途
4. 输出功能清单

```
FEATURE SCOPE:
  主路径: src/features/auth/
  入口文件: [被其他地方引用的文件]
  内部文件: [仅本功能使用的文件]
  总文件数: N
  总行数: N
```

### Phase 2: TRACE — 映射依赖

**入向（本功能引用了什么）：**
- 每个import追溯到源文件
- 验证源文件存在
- 验证导出的实体存在
- 检查环境变量、配置文件、数据库模型、API端点

**出向（谁引用了本功能）：**
- 搜索整个代码库中引用本功能的文件
- 验证它们引用的实体确实存在
- 检查是否使用了正确的API

```
DEPENDENCY MAP:
  入向依赖:
    src/lib/db.ts → auth/repository.ts (getUserById)
    src/lib/jwt.ts → auth/service.ts (signToken)
    process.env.JWT_SECRET → auth/service.ts
  出向依赖:
    src/app/api/login/route.ts → import { login } from auth/service
    src/middleware.ts → import { verifyToken } from auth/service
```

### Phase 3: DIAGNOSE — 全面诊断

**代码质量检查：**
- [ ] 每个import能解析到真实文件
- [ ] 没有循环依赖
- [ ] 类型在边界处一致（没有 any）
- [ ] 函数复杂度合理（< 10 McCabe）
- [ ] 没有 TODO/FIXME/HACK 注释

**运行时检查：**
- [ ] 环境变量已设置
- [ ] 数据库迁移已更新
- [ ] API端点返回预期的形状

**测试检查：**
- [ ] 运行所有相关测试
- [ ] 记录每个失败及其完整输出
- [ ] 检查测试覆盖率缺口

**风险标签：**
| 风险 | 标准 |
|------|------|
| HIGH | 公开API/中断接口契约/DB schema/安全逻辑/3+调用者 |
| MED | 内部模块有测试/共享工具/配置 |
| LOW | 隔离文件/测试/单用途辅助函数 |

### Phase 4: FIX — 系统修复

按顺序修复：
1. **依赖先修** — 修复损坏的import、缺失包、版本错误
2. **类型次修** — 修复功能边界处的类型不匹配
3. **逻辑三修** — 修复实际业务逻辑bug
4. **测试四修** — 为每个修复创建或修复测试
5. **集成最后** — 验证功能端到端

**规则：**
- 一次只修一个
- 每个修复后运行相关测试
- 如果修复破坏了其他东西，停下来
- 修复3个以上创建新问题 → 停！架构问题，不是bug集合

### Phase 5: VERIFY — 验证

1. 运行功能目录下所有测试
2. 运行引用本功能的文件中的所有测试
3. 运行完整测试套件
4. 总结所有变更

```
FOCUSED FIX COMPLETE:
  功能: auth
  修改文件: 4
  修复总数: 7
  测试: 23/23 通过
  回归: 0

  变更:
    1. auth/service.ts — 修复token签名参数顺序
    2. auth/repository.ts — 添加用户查询空值检查
    3. auth/middleware.ts — 修复async错误处理
    4. auth/types.ts — 对齐UserResponse与DB schema
```

---

## 3. PR审查清单（pr-review-expert）

### 30+项检查清单

**第一步：获取上下文**
```bash
gh pr diff <PR_NUMBER> --name-only
gh pr view <PR_NUMBER> --json title,body,labels,assignees,milestone
gh pr diff <PR_NUMBER> > /tmp/pr.diff
```

**第二步：爆炸半径分析**
- [ ] 哪些文件导入/依赖变更的文件？
- [ ] 变更跨越了服务边界吗？
- [ ] 共享契约（类型、接口、schema）被修改了吗？

**爆炸半径严重程度：**
| 级别 | 标准 |
|------|------|
| CRITICAL | 共享库、DB模型、auth中间件、API契约 |
| HIGH | 被3+项目使用的服务、共享配置、环境变量 |
| MEDIUM | 单个服务内部变更、工具函数 |
| LOW | UI组件、测试文件、文档 |

**第三步：安全扫描**
- [ ] SQL注入（原始SQL字符串拼接）
- [ ] 硬编码密钥（password/secret/api_key/token）
- [ ] XSS向量（dangerouslySetInnerHTML/innerHTML）
- [ ] 认证绕过（bypass/skip auth/noauth）
- [ ] 不安全哈希算法（md5/sha1）
- [ ] eval/exec 调用
- [ ] 原型污染（__proto__/constructor）
- [ ] 路径遍历风险

**第四步：测试覆盖率delta**
- [ ] 新功能没有测试 → 标记
- [ ] 删了测试没删代码 → 标记
- [ ] 覆盖率下降 >5% → 阻止合并
- [ ] 认证/支付路径要求100%覆盖率

**第五步：破坏性变更检测**
- [ ] API端点被移除或重命名
- [ ] 响应结构变化
- [ ] 字段被移除或重命名
- [ ] 字段类型变更
- [ ] 新增必填字段
- [ ] DB schema迁移

**第六步：性能影响**
- [ ] N+1查询
- [ ] 包体积回归
- [ ] 内存分配变化

---

## 4. 规格驱动开发（spec-driven-workflow）

**铁律：**
```
NO CODE WITHOUT AN APPROVED SPEC.
NO EXCEPTIONS. NO "QUICK PROTOTYPES." NO "I'LL DOCUMENT IT LATER."
```

### 规格格式（9个强制章节）

| # | 章节 | 关键规则 |
|---|------|----------|
| 1 | 标题和元数据 | 作者、日期、状态（草稿/审查中/已批准/已替代）、审查者 |
| 2 | 上下文 | 为什么这个功能存在。2-4段，有证据（指标、工单） |
| 3 | 功能需求 | RFC 2119关键词（MUST/SHOULD/MAY）。编号FR-N。每个原子化可测试 |
| 4 | 非功能需求 | 性能、安全、可访问性、可扩展性、可靠性 — 都有可测量阈值 |
| 5 | 验收标准 | Given/When/Then格式。每个AC引用至少一个FR-*或NFR-* |
| 6 | 边界情况 | 编号EC-N。覆盖每个外部依赖的故障模式 |
| 7 | API契约 | TypeScript风格接口。覆盖成功和错误响应 |
| 8 | 数据模型 | 表格格式：字段、类型、约束。需求中的每个实体必须有模型 |
| 9 | 超出范围 | 明确排除的内容及原因。防止范围蔓延 |

### 6阶段工作流

**Phase 1:** 收集需求 → 能2分钟解释清楚
**Phase 2:** 写规格 → 9个章节全部填满
**Phase 3:** 验证规格 → 80+分，自查清单全过
**Phase 4:** 生成测试 → 每个AC变成测试用例，初始全红
**Phase 5:** 实现 → 一次一个AC，确保无回归
**Phase 6:** 自审 → 自己审查自己的实现

### 停止自主执行的规则

遇到以下情况必须停并问：
1. 范围蔓延 — 实现需要规格里没有的东西
2. 歧义 >30% — 无法从规格确定正确行为
3. 破坏性变更 — 改变API契约/DB schema/公开接口
4. 安全隐患 — 影响认证/授权/加密/PII
5. 性能未知 — 无法测量或保证性能阈值

---

## 5. API设计审查

### REST命名规范

```
✓ 好例子:
  /api/v1/users
  /api/v1/user-profiles
  /api/v1/orders/123/line-items

✗ 坏例子:
  /api/v1/getUsers
  /api/v1/user_profiles
  /api/v1/orders/123/lineItems
```

### HTTP方法使用

| 方法 | 用途 | 幂等 |
|------|------|------|
| GET | 获取资源 | 是 |
| POST | 创建资源 | 否 |
| PUT | 替换资源 | 是 |
| PATCH | 部分更新 | 否 |
| DELETE | 删除资源 | 是 |

### 设计评分（5维度）

| 维度 | 权重 | 检查内容 |
|------|------|----------|
| 一致性 | 30% | 命名、响应模式、结构一致性 |
| 文档质量 | 20% | 文档完整性和清晰度 |
| 安全性 | 20% | 认证、授权、安全头 |
| 可用性 | 15% | 易用性、可发现性、开发者体验 |
| 性能 | 15% | 缓存、分页、效率模式 |

---

## 6. E2E测试暗坑检测

### 常见silent-pass模式

```
// ❌ 总是通过的假断言
expect(page.getByText('Welcome')).toBeDefined();    // Locator 永远不为 undefined
expect(page.locator('.badge')).not.toBeNull();        // Locator 永远不为 null

// ✅ 正确的断言
await expect(page.getByText('Welcome')).toBeVisible();
await expect(page.locator('.badge')).toHaveText('New');
```

### 24个反模式检测（P0/P1/P2）

**P0（立即修复）：**
- `toBeDefined()` / `not.toBeNull()` 用于 Locator
- 遗忘的 `it.only` / `test.only`
- 空catch块：`try {} catch(e) {}`
- 未await的异步操作

**P1（应该修复）：**
- 固定时间 `page.waitForTimeout(3000)`
- 快照测试无阈值
- `page.waitFor()` 无超时参数
- 测试间共享可变状态

**P2（建议修复）：**
- 过长的测试（>50行）
- 硬编码URL
- 重复的setup代码
- 无error场景测试

---

## 7. 去AI味写作检查（avoid-ai-writing）

### 57种AI写作模式检测

**Tier 1（永远标记）：**
| 词 | 替换 |
|----|------|
| leverage | use |
| utilize | use |
| implement | build / add / create |
| nevertheless | but / yet |
| furthermore | and / also |
| commence | start |
| endeavor | try |
| notwithstanding | despite |
| subsequently | then / later |
| moreover | also / and |

**Tier 2（聚类时标记）：**
| 词 | 替换 |
|----|------|
| robust | reliable / solid |
| seamless | smooth / clean |
| optimize | speed up / improve |
| facilitate | help / enable |
| leverage | use |
| granular | detailed / fine |
| holistic | complete / full |
| ecosystem | system / platform |
| paradigm | model / approach |
| actionable | useful / practical |

**Tier 3（高密度时标记）：**
| 词/短语 | 替换 |
|---------|------|
| cutting-edge | modern / recent |
| state-of-the-art | best available |
| game-changer | big change |
| best-in-class | good / top |
| the integration of | [直接说] |
| a deep dive into | [直接说] |
| in the realm of | in |
| a wealth of | many / plenty |
| decentralized compute | [直接说] |
| leverage best practices | [直接说] |

### 三模式检测

- **重写模式** — 标记并重写，两遍检测
- **检测模式** — 只标记不改
- **编辑模式** — 在文件中有针对性地修改

### 检测流程

```
1. 第一遍：标记所有Tier 1词汇 + 聚类Tier 2 + 高密度Tier 3
2. 结构检测：检查hashtag、空泛名词列表、预测性结论
3. 节奏检查：检查句子长度均匀性
4. 第二遍：重读重写结果，捕获漏网之鱼
5. 输出：标记问题 + 原文引用 + 修改建议 + 变更摘要
```

---

## 8. 自评系统（self-eval）

### 两轴评分

**轴1：任务难度（Low/Medium/High）**
- Low — 安全、熟悉、常规。没有真正的失败风险
- Medium — 有意义的工作，有新颖性或挑战性
- High — 有野心、不熟悉或高风险

**轴2：执行质量（Poor/Adequate/Strong）**
- Poor — 重大失败、不完整、错误输出
- Adequate — 完成但有缺口、走捷径
- Strong — 执行得当、彻底、高质量输出

### 评分矩阵

| | Poor Exec | Adequate Exec | Strong Exec |
|---|:---:|:---:|:---:|
| **Low Ambition** | 1 | 2 | 2 |
| **Medium Ambition** | 2 | 3 | 4 |
| **High Ambition** | 2 | 4 | 5 |

### 强制反方论证

在写最终评分前，必须写：
1. **更低分的理由** — 为什么可能更低？
2. **更高分的理由** — 为什么可能更高？
3. **解决** — 重新评估，给出最终评分

### 防通胀检测

检查 `.self-eval-scores.jsonl` 历史记录：
- 最近5次中4+次相同 → 标记通胀
- 连续3次4分 → 要求更严格的评估

---

## 9. 代码迁移指南（migration-architect）

### 迁移策略

| 策略 | 风险 | 适用场景 |
|------|------|----------|
| 直接替换 | 高 | 小模块，有完整测试覆盖 |
| 并行运行 | 中 | 核心功能，需要回滚能力 |
| 逐步迁移 | 低 | 大型系统，逐模块切换 |
| 抽象层 | 低 | 需要长期同时维护两个版本 |

### 迁移流程

1. **盘点** — 扫描所有使用旧代码的地方
2. **影响分析** — 每个使用点的影响修正
3. **兼容层** — 需要时提供向后兼容
4. **迁移执行** — 按依赖关系排序
5. **验证** — 每个迁移点独立验证
6. **清理** — 删除旧代码和兼容层

---

## 10. CI/CD流水线构建

### 流水线阶段

```
1. Lint → 代码风格检查
2. Type check → 类型检查（tsc / mypy / go vet）
3. Unit test → 单元测试
4. Integration test → 集成测试
5. Build → 构建
6. Security scan → 安全扫描（SAST / dependency check）
7. Deploy → 部署（staging → production）
```

### 门禁规则

| 阶段 | 门禁 | 操作 |
|------|------|------|
| Lint | 0 errors | 阻塞 |
| Unit test | 100% pass | 阻塞 |
| Coverage | ≥80% | 阻塞 |
| Security scan | 0 critical/high | 阻塞 |
| Build | 成功 | 阻塞 |

---

## 11. 数据库设计

### 设计原则

```
1. 表名：复数名词（users, orders, products）
2. 主键：id（UUID或自增）
3. 时间戳：created_at, updated_at
4. 软删除：deleted_at（可选）
5. 索引：覆盖所有查询条件
6. 外键：显式定义，有ON DELETE策略
7. 迁移：始终向前兼容
```

### 性能检查清单

- [ ] 查询使用了索引吗？
- [ ] N+1查询问题？
- [ ] 连接数量合理？
- [ ] 分页正确（游标 > OFFSET）？
- [ ] 事务范围正确？

---

## 12. MCP服务器构建

### OpenAPI → MCP 映射

```bash
python3 scripts/openapi_to_mcp.py \
  --input openapi.json \
  --server-name my-service \
  --language python \
  --output-dir ./out
```

### MCP设计原则

```
1. 工具名 = 动+名（getUser, createOrder）
2. 每个工具一个明确职责
3. Schema即文档（描述字段必填）
4. 错误响应标准化
5. 版本管理，向后兼容
```

---

## 13. 可观测性设计

### 三大支柱

| 支柱 | 工具 | 检查内容 |
|------|------|----------|
| 日志 | 结构化日志 | 关键路径有日志，日志级别正确 |
| 指标 | 业务指标 | 延迟、错误率、吞吐量 |
| 追踪 | 分布式追踪 | 跨服务调用链完整 |

### 健康检查端点

```
GET /health — 基础存活检查
GET /health/ready — 就绪检查（依赖都可用）
GET /health/debug — 调试信息（仅内部）
```

---

## 14. 发布门禁（ship-gate）

### 发布前检查清单

```
[ ] 所有测试通过
[ ] 代码审查完成并批准
[ ] 没有P0/P1安全漏洞
[ ] CHANGELOG已更新
[ ] 版本号已更新（semver）
[ ] 数据库迁移向前兼容
[ ] 回滚计划已制定
[ ] 监控告警已配置
[ ] 文档已更新
[ ] 性能基准已检查
```

---

## 15. 技术债务追踪

### 债务分类

| 类型 | 示例 | 优先级 |
|------|------|--------|
| 架构 | 循环依赖、上帝类 | HIGH |
| 代码质量 | 长函数、重复代码 | MED |
| 测试 | 低覆盖率、无集成测试 | HIGH |
| 文档 | 过期文档、无API文档 | LOW |
| 基础设施 | 陈旧依赖、手动部署 | MED |

### 债务条目标准格式

```
- [ ] 类型: [架构/代码/测试/文档/基础设施]
      位置: [文件路径:行号]
      描述: [一句话描述问题]
      影响: [为什么需要修复]
      预估: [修复时间估计]
      创建: [日期]
```

---

## 16. 每种语言速查

### Python
```python
# 类型提示
def greet(name: str) -> str:
    return f"Hello, {name}"

# 错误处理
try:
    result = await async_func()
except TimeoutError:
    logger.error("timeout")
    raise
except Exception as e:
    logger.exception("unexpected error", exc_info=e)
    raise

# 路径处理
from pathlib import Path
config = Path("config.yaml")
if not config.exists():
    raise FileNotFoundError(f"config not found: {config}")
```

### TypeScript
```typescript
// 类型定义
interface User {
  id: string;
  name: string;
  email: string;
  createdAt: Date;
}

// 错误处理
async function fetchUser(id: string): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  }
  return response.json();
}

// 路径处理
import path from 'node:path';
const configPath = path.resolve(process.cwd(), 'config.yaml');
```

### Go
```go
// 接口定义
type UserService interface {
    GetUser(ctx context.Context, id string) (*User, error)
    CreateUser(ctx context.Context, user *User) error
}

// 错误处理
func (s *Service) GetUser(ctx context.Context, id string) (*User, error) {
    user, err := s.repo.FindByID(ctx, id)
    if err != nil {
        return nil, fmt.Errorf("get user %s: %w", id, err)
    }
    return user, nil
}
```

### PowerShell
```powershell
# 函数定义
function Get-User {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$UserId
    )
    # 实现
}

# 错误处理
try {
    $result = Invoke-RestMethod -Uri $url -ErrorAction Stop
} catch {
    Write-Error "Failed to fetch: $_"
    throw
}
```

---

## 附录：快速参考

### 什么时候用什么

| 场景 | 使用 |
|------|------|
| 写新代码 | 规格驱动开发 → 写规格 → 生成测试 → 实现 |
| 修bug | focused-fix 5阶段流程 |
| 审PR | PR审查清单（30+项） |
| 设计API | API设计审查 + 评分 |
| 写测试 | E2E暗坑检测 + 测试覆盖率 |
| 做迁移 | 迁移架构流程 |
| 设CI/CD | CI/CD流水线构建 |
| 设数据库 | 数据库设计原则 |
| 建MCP | MCP服务器构建 |
| 发版本 | 发布门禁检查清单 |
| 修技术债 | 债务追踪格式 |
| 自评 | 两轴自评系统 |
| 去AI味 | 去AI写作检查 |

### 永远不要做

1. 不划范围就修bug
2. 不写规格就写代码
3. 不审PR就合并
4. 不跑测试就提交
5. 不写CHANGELOG就发版
6. 不评估影响就改API
7. 不诚实地自评
8. 不检查AI味就发出去
