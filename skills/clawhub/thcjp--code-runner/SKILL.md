---
slug: "code-runner"
name: "code-runner"
version: 1.0.1
displayName: "代码执行工具专业版"
summary: "企业级PTY代码执行,支持批量任务、并发执行、执行审计与CI/CD集成"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队与企业的高级代码执行工具,在免费版基础上扩展批量执行、并发管理、执行审计等能力。核心能力:
  - 批量任务执行与并发管理
  - 执行日志审计与结果追踪
  - CI/CD 流水线集成
  - 自定义应答规则与执行策略
  - 多用户隔离与权限管理

  适用场景:
  - 企业级批量代码处理
  - CI/CD 流水线自动化
  - 多项目并行开发与测试

  差异化:
  - 兼容免费版全部能力,无缝升级
  - 支持批量并发与任务编排
  - 提供执行审计与日志追踪
  - 优先技术支持与更新通道
tags:
  - 开发工具
  - 代码执行
  - 企业级
  - 批量处理
  - CI/CD集成
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# 代码执行工具专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

### 1. 批量任务执行
```python
from code_runner import run_batch_tasks
# ...
tasks = [
    {
        "workdir": "/path/to/auth-service",
        "prompt": "实现 JWT 认证,添加单元测试",
        "priority": "high"
    },
    {
        "workdir": "/path/to/order-service",
        "prompt": "添加订单状态机,包含测试",
        "priority": "medium"
    },
    {
        "workdir": "/path/to/payment-service",
        "prompt": "集成第三方支付网关",
        "priority": "medium"
    }
]
# ...
results = run_batch_tasks(tasks, max_concurrent=3)
```- 验证返回数据的完整性和格式正确性
- 参考`CI/CD 集成`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`批量任务执行`的配置文档进行参数调优
### 2. 并发管理与任务编排
| 功能 | 说明 |
|:-----|:-----|
| 并发控制 | 可配置最大并发数(默认 3) |
| 优先级队列 | 高优先级任务优先执行 |
| 依赖编排 | 任务间可配置依赖关系 |
| 失败重试 | 自动重试失败任务 |
| 超时管理 | 每个任务独立超时配置 |

```python
# 依赖说明
pipeline = [
    {"id": "schema", "prompt": "创建数据库 Schema", "depends_on": []},
    {"id": "dal", "prompt": "实现数据访问层", "depends_on": ["schema"]},
    {"id": "logic", "prompt": "编写业务逻辑", "depends_on": ["dal"]},
    {"id": "api", "prompt": "添加 API 端点", "depends_on": ["logic"]},
    {"id": "test", "prompt": "运行集成测试", "depends_on": ["api"]}
]
# ...
results = run_pipeline(pipeline, max_concurrent=2)
```

**输入**: 用户提供并发管理与任务编排所需的指令和必要参数.
### 3. 执行日志审计
```python
# 审计配置
audit_config = {
    "enabled": True,
    "log_dir": ".code-runner/logs/",
    "capture_stdout": True,
    "capture_stderr": True,
    "track_changes": True,
    "retention_days": 90
}
```

审计记录包含:

| 记录项 | 说明 |
|---:|---:|
| 任务 ID | 唯一标识 |
| 执行时间 | 开始/结束时间 |
| 执行用户 | 以哪个用户运行 |
| 任务描述 | 自然语言描述 |
| 执行结果 | 成功/失败/超时 |
| 变更文件 | 修改了哪些文件 |
| 输出日志 | stdout/stderr 完整记录 |
| 执行耗时 | 总耗时(秒) |

### 4. CI/CD 集成
```yaml
# 示例
pipeline:
  - stage: code-execution
    jobs:
      - name: run-development
        script: |
          python3 -m code_runner \
            --workdir $PROJECT_DIR \
            --prompt "实现新功能并添加测试" \
            --user ci-runner \
            --timeout 600 \
            --audit
      - name: run-tests
        depends_on: run-development
        script: |
          python3 -m code_runner \
            --workdir $PROJECT_DIR \
            --prompt "运行全量测试套件,报告结果" \
            --user ci-runner \
            --timeout 300
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `ci/cd_集成` 选项
- 处理流程: 接收输入 -> 执行CI/CD 集成 -> 返回结果
- 输入: 用户提供CI/CD 集成所需的参数和指令
- 输出: 返回CI/CD 集成的处理结果,包含执行状态码、结果数据和执行日志

### 5. 自定义应答规则
```python
# 扩展自动应答规则
custom_responses = {
    b'Do you want to': b'y\n',
    b'Are you sure': b'y\n',
    b'Continue?': b'y\n',
    b'Press Enter to continue': b'\n',
    b'Enter password': os.environ.get('EXEC_PASSWORD', '').encode() + b'\n',
    b'Select option': b'1\n'  # 选择优秀个选项
}
```

**输入**: 用户提供自定义应答规则所需的指令和必要参数.
**处理**: 解析自定义应答规则的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回自定义应答规则的处理结果,包含执行状态码、结果数据和执行日志.
#
## 适用场景

### 场景一: 企业级批量代码处理
对多个微服务模块批量执行开发任务.
```python
from code_runner import run_batch_tasks
# ...
# 批量处理微服务
services = ["auth", "order", "payment", "notification", "user"]
tasks = [
    {
        "workdir": f"/projects/microservices/{svc}",
        "prompt": f"为 {svc} 服务添加健康检查端点和单元测试",
        "priority": "medium",
        "timeout": 300
    }
    for svc in services
]
# ...
results = run_batch_tasks(tasks, max_concurrent=3)
# ...
# 生成汇总报告
for task_id, result in results.items():
    status = "成功" if result.success else "失败"
    print(f"{task_id}: {status} (耗时 {result.duration}秒)")
```

输出示例:

```text
批量执行报告
=====================================
任务总数: 5
成功: 4
失败: 1
总耗时: 812 秒
# ...
详情:
auth-service:        成功 (耗时 156秒)
order-service:       成功 (耗时 198秒)
payment-service:     成功 (耗时 175秒)
notification-service:成功 (耗时 142秒)
user-service:        失败 (超时,建议增加超时或拆分任务)
# ...
审计日志: .code-runner/logs/batch-20260718-143000.log
```

### 场景二: CI/CD 流水线自动化
在 CI/CD 流水线中自动执行代码任务.
```bash
#!/bin/bash
# CI/CD 流水线脚本
# 1. 执行开发任务
python3 -m code_runner \
  --workdir $CI_PROJECT_DIR \
  --prompt "根据 PR 描述实现功能,添加测试" \
  --user ci-runner \
  --timeout 600 \
  --audit
# ...
# 2. 运行测试
python3 -m code_runner \
  --workdir $CI_PROJECT_DIR \
  --prompt "运行全量测试,报告通过率和失败详情" \
  --user ci-runner \
  --timeout 300
# ...
# 3. 代码审查
python3 -m code_runner \
  --workdir $CI_PROJECT_DIR \
  --prompt "审查代码变更,输出审查报告" \
  --user ci-runner \
  --timeout 300
```

### 场景三: 多项目并行开发
多个项目同步开发,统一管理与追踪.
```python
# 多项目并行开发
projects = [
    {"name": "frontend", "workdir": "/projects/frontend-app"},
    {"name": "backend", "workdir": "/projects/backend-api"},
    {"name": "mobile", "workdir": "/projects/mobile-app"}
]
# ...
tasks = [
    {
        "workdir": p["workdir"],
        "prompt": f"审查 {p['name']} 项目代码,生成质量报告",
        "tag": p["name"]
    }
    for p in projects
]
# ...
results = run_batch_tasks(tasks, max_concurrent=3)
# ...
# 按项目汇总
for p in projects:
    result = results.get(p["name"])
    if result and result.success:
        print(f"{p['name']}: 审查完成,评分 {result.score}")
```

## 使用流程

### 优秀步: 安装与配置
```bash
# 安装依赖
pip install code-runner-pro
# ...
# 初始化配置
mkdir -p .code-runner/{logs,reports,configs}
# ...
cat > .code-runner/config.json << 'EOF'
{
  "edition": "pro",
  "execution": {
    "max_concurrent": 3,
    "default_timeout": 300,
    "retry_count": 2,
    "default_user": "code-runner"
  },
  "audit": {
    "enabled": true,
    "log_dir": ".code-runner/logs/",
    "capture_output": true,
    "track_changes": true,
    "retention_days": 90
  }
}
EOF
```

### 第二步: 执行批量任务
```python
from code_runner import run_batch_tasks
# ...
tasks = [
    {"workdir": "/projects/app1", "prompt": "添加健康检查端点"},
    {"workdir": "/projects/app2", "prompt": "添加健康检查端点"},
    {"workdir": "/projects/app3", "prompt": "添加健康检查端点"}
]
# ...
results = run_batch_tasks(tasks, max_concurrent=3)
```

### 第三步: 查看审计报告
```bash
# 查看最新审计报告
cat .code-runner/logs/latest-audit.log
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | code-runner处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Linux / macOS(Unix-like 环境)
- **Python**: 3.8 或更高版本
- **权限**: root 或 sudo(用户切换需要)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| Python 3.8+ | 运行时 | 必需 | python.org |
| 代码 CLI | CLI 工具 | 必需 | `npm install -g @anthropic-ai/claude-code` |
| LLM API | API | 必需 | 由代码 CLI 内置 LLM 提供 |
| pty 模块 | Python 标准库 | 必需 | Python 自带 |
| psutil(可选) | Python 库 | 资源监控推荐 | `pip install psutil` |

### API Key 配置
```bash
# 代码 CLI 认证
export ANTHROPIC_API_KEY="your-api-key"
# ...
# 工具配置
export CODE_RUNNER_USER="code-runner"
export CODE_RUNNER_TIMEOUT="600"
export CODE_RUNNER_AUDIT="true"
```

### 可用性分类
- **分类**: MD+EXEC+SCRIPT+AUDIT(Markdown 指令 + 命令行执行 + Python 脚本 + 审计日志)
- **说明**: 通过自然语言指令驱动 Agent 批量执行编程任务,支持 CI/CD 集成与执行审计
- **离线可用**: 否,代码 CLI 需要连接 LLM API

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100
# ...
检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100
# ...
检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100
# ...
检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过
# ...
改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 常见问题

### Q1: 专业版是否兼容免费版的 API?
完全兼容。专业版的 `run_code_task` 函数与免费版签名一致,免费版代码无需修改即可运行.
### Q2: 并发执行时资源不够怎么办?
降低并发度或增加超时时间。监控 CPU 和内存使用,避免资源耗尽:

```python
# 动态调整并发度
import psutil
cpu_usage = psutil.cpu_percent()
max_concurrent = 5 if cpu_usage < 70 else 2
```

### Q3: CI/CD 中如何安全存储凭据?
使用 CI/CD 平台的密钥管理功能,不要在代码中硬编码:

```yaml
variables:
  ANTHROPIC_API_KEY: $CI_SECRETS_API_KEY
```

### Q4: 审计日志占用空间太大怎么办?
配置日志保留策略与压缩:

```json
{
  "audit": {
    "retention_days": 90,
    "compress_after_days": 7,
    "max_size_mb": 500
  }
}
# ...
# ...
## 已知限制
# ...
- 每次请求仅处理单一任务,不支持批量并发
- 
- 和网络环境
# ...