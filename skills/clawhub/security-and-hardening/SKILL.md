---
name: security-and-hardening
version: 1.0.0
description: "Threat-model and harden applications against security vulnerabilities"
tags: [security, hardening, owasp, threat-model, input-validation, authentication, ssrf, xss, llm-security]
---

# Security and Hardening

## Overview

安全优先的开发实践。将每个外部输入视为敌意的，每个密钥视为神圣的，每个授权检查视为强制的。安全不是一个阶段——它是每一行涉及用户数据、认证或外部系统的代码的约束�?
## When to Use

- 构建任何接受用户输入的功�?- 实现认证或授�?- 存储或传输敏感数�?- 与外�?API 或服务集�?- 添加文件上传、webhook 或回�?- 处理支付�?PII 数据

---

## Process: Threat Model First

没有威胁模型的控制是猜测。加固前，花5分钟像攻击者一样思考：

1. **映射信任边界�?* 不可信数据在哪里跨越进入系统？HTTP 请求、表单字段、文件上传、webhook、第三方 API、消息队列，以及 **LLM 输出**。每个边界都是攻击面�?
2. **命名资产�?* 什么值得窃取或破坏？凭据、PII、支付数据、管理员操作、资金转移�?
3. **对每个边界运�?STRIDE** �?快速视角，不是仪式�?
| 威胁 | 提问 | 典型缓解 |
|------|------|----------|
| **S**poofing（伪装） | 能有人冒充用�?服务吗？ | 认证、签名验�?|
| **T**ampering（篡改） | 数据能在传输或存储中被改变吗�?| 完整性检查、参数化查询、HTTPS |
| **R**epudiation（抵赖） | 行为能事后被否认吗？ | 安全事件审计日志 |
| **I**nformation disclosure（信息泄露） | 数据能泄露吗�?| 加密、字段白名单、通用错误 |
| **D**enial of service（拒绝服务） | 能被压垮吗？ | 速率限制、输入大小上限、超�?|
| **E**levation of privilege（权限提升） | 用户能获得不该有的权限吗�?| 授权检查、最小权�?|

4. **在用例旁边写滥用用例�?* 对每个功能问"我会如何误用它？"——然后让这成为你的第一个测试�?
如果你无法命名功能的信任边界，你还没准备好加固它。这�?OWASP **A04: Insecure Design** �?大多数违规始于设计，而非代码�?
**完成条件**：已输出威胁模型文档，包含信任边界图、资产清单、每个边界的 STRIDE 分析、至�?1 个滥用用例�?
---

## The Three-Tier Boundary System

### Always Do（无条件执行�?
- **验证所有外部输�?*在系统边界（API 路由、表单处理器�?- **参数化所有数据库查询** �?永远不要将用户输入拼接到 SQL
- **编码输出**防止 XSS（使用框架自动转义，不要绕过�?- **使用 HTTPS** 进行所有外部通信
- **哈希密码**使用 bcrypt/scrypt/argon2（永远不要存储明文）
- **设置安全�?*（CSP, HSTS, X-Frame-Options, X-Content-Type-Options�?- **使用 httpOnly, secure, sameSite cookies** 管理会话
- **运行 `npm audit`**（或等效工具）每次发布前

### Ask First（需要人类批准）

- 添加新认证流程或更改认证逻辑
- 存储新类别的敏感数据（PII、支付信息）
- 添加新的外部服务集成
- 更改 CORS 配置
- 添加文件上传处理�?- 修改速率限制或节�?- 授予提升权限或角�?
### Never Do（绝不做�?
- **永远不要提交密钥**到版本控制（API 密钥、密码、令牌）
- **永远不要记录敏感数据**（密码、令牌、完整信用卡号）
- **永远不要信任客户端验�?*作为安全边界
- **永远不要禁用安全�?*为了方便
- **永远不要使用 `eval()` �?`innerHTML`** 与用户提供的数据
- **永远不要存储会话**在客户端可访问的存储（localStorage 用于 auth 令牌�?- **永远不要暴露堆栈跟踪**或内部错误详情给用户

---

## OWASP Top 10 Prevention Patterns

### Injection（SQL, NoSQL, OS Command�?
```typescript
// BAD: SQL injection via string concatenation
const query = `SELECT * FROM users WHERE id = '${userId}'`;

// GOOD: Parameterized query
const user = await db.query('SELECT * FROM users WHERE id = $1', [userId]);

// GOOD: ORM with parameterized input
const user = await prisma.user.findUnique({ where: { id: userId } });
```

### Broken Authentication

```typescript
// Password hashing
import { hash, compare } from 'bcrypt';

const SALT_ROUNDS = 12;
const hashedPassword = await hash(plaintext, SALT_ROUNDS);
const isValid = await compare(plaintext, hashedPassword);

// Session management
app.use(session({
  secret: process.env.SESSION_SECRET,  // From environment, not code
  resave: false,
  saveUninitialized: false,
  cookie: {
    httpOnly: true,     // Not accessible via JavaScript
    secure: true,       // HTTPS only
    sameSite: 'lax',    // CSRF protection
    maxAge: 24 * 60 * 60 * 1000,  // 24 hours
  },
}));
```

### Cross-Site Scripting (XSS)

```typescript
// BAD: Rendering user input as HTML
element.innerHTML = userInput;

// GOOD: Use framework auto-escaping (React does this by default)
return <div>{userInput}</div>;

// If you MUST render HTML, sanitize first
import DOMPurify from 'dompurify';
const clean = DOMPurify.sanitize(userInput);
```

### Broken Access Control

```typescript
// Always check authorization, not just authentication
app.patch('/api/tasks/:id', authenticate, async (req, res) => {
  const task = await taskService.findById(req.params.id);

  // Check that the authenticated user owns this resource
  if (task.ownerId !== req.user.id) {
    return res.status(403).json({
      error: { code: 'FORBIDDEN', message: 'Not authorized to modify this task' }
    });
  }

  // Proceed with update
  const updated = await taskService.update(req.params.id, req.body);
  return res.json(updated);
});
```

### Security Misconfiguration

```typescript
// Security headers (use helmet for Express)
import helmet from 'helmet';
app.use(helmet());

// Content Security Policy
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'"],
    styleSrc: ["'self'", "'unsafe-inline'"],  // Tighten if possible
    imgSrc: ["'self'", 'data:', 'https:'],
    connectSrc: ["'self'"],
  },
}));

// CORS �?restrict to known origins
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS?.split(',') || 'http://localhost:3000',
  credentials: true,
}));
```

### Sensitive Data Exposure

```typescript
// Never return sensitive fields in API responses
function sanitizeUser(user: UserRecord): PublicUser {
  const { passwordHash, resetToken, ...publicFields } = user;
  return publicFields;
}

// Use environment variables for secrets
const API_KEY = process.env.STRIPE_API_KEY;
if (!API_KEY) throw new Error('STRIPE_API_KEY not configured');
```

### Server-Side Request Forgery (SSRF)

任何时候服务器获取用户影响�?URL �?webhook�?�?URL 导入"、图片代理、链接预�?�?攻击者可以将它指向内部服务（云元数据、`localhost`、私�?IP）�?
```typescript
// BAD: fetch whatever the user gives you
await fetch(req.body.webhookUrl);

// GOOD: allowlist scheme + host, reject if ANY resolved IP is private, forbid redirects
import { lookup } from 'node:dns/promises';
import ipaddr from 'ipaddr.js';

const ALLOWED_HOSTS = new Set(['hooks.example.com']);

async function assertSafeUrl(raw: string): Promise<URL> {
  const url = new URL(raw);
  if (url.protocol !== 'https:') throw new Error('https only');
  if (!ALLOWED_HOSTS.has(url.hostname)) throw new Error('host not allowed');
  // Resolve ALL records; a single private/reserved address fails the check.
  const addrs = await lookup(url.hostname, { all: true });
  if (addrs.some((a) => ipaddr.parse(a.address).range() !== 'unicast')) {
    throw new Error('private/reserved IP');
  }
  return url;
}

await fetch(await assertSafeUrl(req.body.webhookUrl), { redirect: 'error' });
```

`range() !== 'unicast'` 检查覆盖环回、链路本�?`169.254.169.254`（云元数据，#1 SSRF 目标）、私有和唯一本地范围�?IPv4 �?IPv6�?
**注意 �?这仍�?TOCTOU 缺口�?* `fetch` 在检查后再次解析 DNS，所以使用短 TTL 记录的攻击者可以在验证和连接之间重绑定到内�?IP。对于高风险面，解析一次并连接到固�?IP，或在前端放置过滤代理�?
---

## Input Validation Patterns

### Schema Validation at Boundaries

```typescript
import { z } from 'zod';

const CreateTaskSchema = z.object({
  title: z.string().min(1).max(200).trim(),
  description: z.string().max(2000).optional(),
  priority: z.enum(['low', 'medium', 'high']).default('medium'),
  dueDate: z.string().datetime().optional(),
});

// Validate at the route handler
app.post('/api/tasks', async (req, res) => {
  const result = CreateTaskSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(422).json({
      error: {
        code: 'VALIDATION_ERROR',
        message: 'Invalid input',
        details: result.error.flatten(),
      },
    });
  }
  // result.data is now typed and validated
  const task = await taskService.create(result.data);
  return res.status(201).json(task);
});
```

### File Upload Safety

```typescript
// Restrict file types and sizes
const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp'];
const MAX_SIZE = 5 * 1024 * 1024; // 5MB

function validateUpload(file: UploadedFile) {
  if (!ALLOWED_TYPES.includes(file.mimetype)) {
    throw new ValidationError('File type not allowed');
  }
  if (file.size > MAX_SIZE) {
    throw new ValidationError('File too large (max 5MB)');
  }
  // Don't trust the file extension �?check magic bytes if critical
}
```

---

## Triaging npm audit Results

不是所有审计发现都需要立即行动。使用这个决策树�?
```
npm audit reports a vulnerability
├── Severity: critical or high
�?  ├── Is the vulnerable code reachable in your app?
�?  �?  ├── YES --> Fix immediately (update, patch, or replace the dependency)
�?  �?  └── NO (dev-only dep, unused code path) --> Fix soon, but not a blocker
�?  └── Is a fix available?
�?      ├── YES --> Update to the patched version
�?      └── NO --> Check for workarounds, consider replacing the dependency, or add to allowlist with a review date
├── Severity: moderate
�?  ├── Reachable in production? --> Fix in the next release cycle
�?  └── Dev-only? --> Fix when convenient, track in backlog
└── Severity: low
    └── Track and fix during regular dependency updates
```

### Supply-Chain Hygiene

`npm audit` 捕获已知 CVE；它不会捕获恶意�?typosquatted 包。还要：

- **提交 lockfile** 并在 CI 中使�?`npm ci`（不�?`npm install`）�?可重现构建，无静默版本漂�?- **添加新依赖前审查** �?维护、下载量，以及它们是否真正值得
- **警惕 `postinstall` 脚本** 在不熟悉的包�?�?它们在安装时运行任意代码
- **注意 typosquats** �?`cross-env` vs `crossenv`，`react-dom` vs `reactdom`

---

## Rate Limiting

```typescript
import rateLimit from 'express-rate-limit';

// General API rate limit
app.use('/api/', rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100,                   // 100 requests per window
  standardHeaders: true,
  legacyHeaders: false,
}));

// Stricter limit for auth endpoints
app.use('/api/auth/', rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 10,  // 10 attempts per 15 minutes
}));
```

---

## Secrets Management

```
.env files:
  ├── .env.example  �?Committed (template with placeholder values)
  ├── .env          �?NOT committed (contains real secrets)
  └── .env.local    �?NOT committed (local overrides)

.gitignore must include:
  .env
  .env.local
  .env.*.local
  *.pem
  *.key
```

**提交前总是检查：**
```bash
# Check for accidentally staged secrets
git diff --cached | grep -i "password\|secret\|api_key\|token"
```

**如果密钥被提交，轮换它�?* 删除行或重写历史不够 �?假设它在到达远程的那一刻就被泄露了。先撤销并重新颁发密钥，然后从历史中清除�?
---

## Securing AI / LLM Features

如果你的应用调用 LLM �?聊天机器人、摘要器、代理、RAG �?它继承了新的攻击面。映射到 [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/llm-top-10/)�?
- **将所有模型输出视为不可信输入 (LLM05: Improper Output Handling)�?* 永远不要�?LLM 输出直接传入 `eval`、SQL、shell、`innerHTML` 或文件路径。像验证原始用户输入一样验证和编码它�?
- **假设提示可以被劫�?(LLM01: Prompt Injection)�?* 上下文窗口中的不可信文本 �?用户消息、获取的网页、PDF �?可以携带指令。系统提示不是安全边界；在代码中强制执行权限，而非在提示中�?
- **保持密钥和其他用户数据不在提示中 (LLM02 / LLM07)�?* 上下文中的任何内容都可以被回显。不要把 API 密钥、跨租户数据或完整系统提示放在模型可以重复的地方�?
- **约束工具和代理权�?(LLM06: Excessive Agency)�?* 将工具范围限定为最小，对破坏性或不可逆操作要求确认，并验证每个工具参数�?
- **绑定消费 (LLM10: Unbounded Consumption)�?* 上限令牌、请求速率和循�?递归深度，使精心设计的输入不会产生高昂费用或挂起系统�?
- **隔离检索数�?(LLM08: Vector and Embedding Weaknesses)�?* �?RAG 中，将向量存储视为信任边界：按租户分区嵌入，使一个用户无法检索另一个用户的数据，并在索引前验证文档，使中毒内容无法引导答案�?
```typescript
// BAD: trusting model output as a command or as markup
const sql = await llm.generate(`Write SQL for: ${userQuestion}`);
await db.query(sql);                                   // arbitrary query execution
container.innerHTML = await llm.reply(userMessage);   // stored XSS, via the model

// GOOD: model output is data �?parse defensively, then validate, then encode
let intent;
try {
  intent = CommandSchema.parse(JSON.parse(await llm.replyJson(userMessage)));
} catch {
  throw new ValidationError('unexpected model output'); // JSON.parse or schema failed
}
await runAllowlistedAction(intent.action, intent.params);
container.textContent = await llm.reply(userMessage);
```

---

## Security Review Checklist

```markdown
### Authentication
- [ ] Passwords hashed with bcrypt/scrypt/argon2 (salt rounds �?12)
- [ ] Session tokens are httpOnly, secure, sameSite
- [ ] Login has rate limiting
- [ ] Password reset tokens expire

### Authorization
- [ ] Every endpoint checks user permissions
- [ ] Users can only access their own resources
- [ ] Admin actions require admin role verification

### Input
- [ ] All user input validated at the boundary
- [ ] SQL queries are parameterized
- [ ] HTML output is encoded/escaped
- [ ] Server-side URL fetches are allowlisted (no SSRF to internal services)

### Data
- [ ] No secrets in code or version control
- [ ] Sensitive fields excluded from API responses
- [ ] PII encrypted at rest (if applicable)

### Infrastructure
- [ ] Security headers configured (CSP, HSTS, etc.)
- [ ] CORS restricted to known origins
- [ ] Dependencies audited for vulnerabilities
- [ ] Error messages don't expose internals

### Supply Chain
- [ ] Lockfile committed; CI installs with `npm ci`
- [ ] New dependencies reviewed (maintenance, downloads, postinstall scripts)

### AI / LLM (if used)
- [ ] Model output treated as untrusted (no eval/SQL/innerHTML/shell)
- [ ] Secrets and other users' data kept out of prompts
- [ ] Tool/agent permissions scoped; destructive actions require confirmation
```

---

## Common Rationalizations

| 借口 | 现实 |
|------|------|
| "这是内部工具，安全不重要" | 内部工具会被攻破。攻击者针对最弱环节�?|
| "我们稍后添加安全" | 安全改造比内置�?0倍。现在就添加�?|
| "没人会尝试利用这�? | 自动化扫描器会发现它。隐晦安全不是安全�?|
| "框架处理安全" | 框架提供工具，不是保证。你仍需要正确使用它们�?|
| "这只是原�? | 原型变成生产。从第一天开始的安全习惯�?|
| "威胁建模在这里过�? | 5分钟�?我会如何攻击这个�?防止设计缺陷，没有控制能修补�?|
| "这只�?LLM 输出，只是文�? | 那个"文本"可以�?SQL 语句、脚本标签或 shell 命令。像任何不可信输入一样对待它�?|

---

## Red Flags

- 用户输入直接传递到数据库查询、shell 命令�?HTML 渲染
- 源代码或提交历史中的密钥
- 没有认证或授权检查的 API 端点
- 缺失 CORS 配置或通配�?(`*`) �?- 认证端点没有速率限制
- 堆栈跟踪或内部错误暴露给用户
- 已知严重漏洞的依�?- 服务器获取用户提供的 URL 没有白名单（SSRF�?- LLM/模型输出传入查询、DOM、shell �?`eval`
- 密钥、PII 或完整系统提示放�?LLM 上下文窗口中

---

## Verification

实现安全相关代码后：

- [ ] `npm audit` 显示无严重或高漏�?- [ ] 源代码或 git 历史中无密钥
- [ ] 所有用户输入在系统边界验证
- [ ] 每个受保护端点检查认证和授权
- [ ] 响应中存在安全头（用浏览�?DevTools 检查）
- [ ] 错误响应不暴露内部详�?- [ ] 认证端点有速率限制
- [ ] 服务器端 URL 获取针对白名单验证（�?SSRF�?- [ ] LLM/模型输出在使用前验证和编码（如有 AI 功能�?
---

## See Also

- `debugging-and-error-recovery` �?错误处理与安全输�?- `ci-cd-and-automation` �?CI/CD 安全�?- `skill-vetter` �?技能安全审�?