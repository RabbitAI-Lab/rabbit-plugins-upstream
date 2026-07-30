---
slug: cybersecurity-engine-tool-free
name: cybersecurity-engine-tool-free
version: 1.0.0
displayName: 网络安全评估引擎免费版
summary: 轻量级安全评估与威胁建模工具,提供安全态势检查、OWASP基础审计与漏洞管理,适合个人开发者快速安全自查.
license: MIT
edition: free
description: "网络安全评估引擎免费版,为个人开发者包含基础安全评估与威胁建模能力. 适用于需要cybersecurity engine tool相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量. 适用于需要cybersecurity engine tool相关能力的开发场景,包含结构化的工作流程和配置指引."
tags:
  - 安全
  - cybersecurity
  - engine
  - automation
  - productivity
  - 威胁建模
  - OWASP
  - 免费版
  - 加密
  - 工具
tools:
  - read
  - exec
homepage: ""
category: "Security"
pricing_tier: free

---
# 网络安全评估引擎免费版

## 概述

本工具为个人开发者提供轻量级网络安全评估能力,涵盖安全态势检查、OWASP Top 10基础审计与威胁建模核心流程。免费版无需安装额外工具,通过纯知识驱动的方式帮助开发者快速识别项目中的安全风险,适合项目上线前的快速安全自查.
### 免费版与专业版对比

| 能力维度 | 免费版 | 专业版 |
|----|---|---|
| 安全评估深度 | 基础三层检查 | 完整十二阶段 |
| 威胁建模 | STRIDE基础 | STRIDE+攻击树 |
| 漏洞管理 | 手动登记 | 自动化SLA跟踪 |
| 合规框架 | 不支持 | SOC2/ISO27001/GDPR |
| 安全评分 | 基础评分 | 100分制多维评分 |
| 报告导出 | 文本格式 | HTML/PDF/SARIF |
| 团队协作 | 单人 | 多租户协作 |

## 核心能力

### 1. 安全态势快速检查

通过三层检查快速评估项目安全状况,5分钟内完成基础安全体检.
**领先层 - 关键风险(立即修复):**

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 网络安全评估引擎免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
#!/bin/bash
# 关键安全风险检查脚本
echo "=== 关键安全风险检查 ==="
ISSUES=0
# ...
# 检查硬编码密钥
SECRETS=$(grep -rn 'AKIA[0-9A-Z]\{16\}\|BEGIN.*PRIVATE KEY\|sk-[A-Za-z0-9]\{20,\}' \
  --include='*.{js,ts,py,go,env,yml,yaml,json}' . 2>/dev/null | \
  grep -v 'node_modules\|\.git\|example' | wc -l)
[ "$SECRETS" -gt 0 ] && echo "[!] 发现 ${SECRETS} 处疑似硬编码密钥" && ((ISSUES++))
# ...
# 检查生产环境调试模式
DEBUG=$(grep -rn 'DEBUG\s*=\s*True\|debug:\s*true' \
  --include='*.{py,js,ts,yml,yaml,json}' . 2>/dev/null | \
[ "$DEBUG" -gt 0 ] && echo "[!] 发现 ${DEBUG} 处调试模式开启" && ((ISSUES++))
# ...
# 检查CORS通配符
CORS=$(grep -rn "Access-Control-Allow-Origin.*\*" \
  --include='*.{py,js,ts,go}' . 2>/dev/null | \
[ "$CORS" -gt 0 ] && echo "[!] 发现 ${CORS} 处CORS通配符配置" && ((ISSUES++))
# ...
echo ""
echo "关键风险检查完成,发现问题: ${ISSUES} 项"
```

**第二层 - 高风险(本周修复):**

- 依赖项存在已知CVE(CVSS >= 7.0)
- 认证端点无速率限制
- 状态变更操作缺少CSRF保护
- 错误信息泄露堆栈跟踪
- 弱密码策略(少于12字符)

**第三层 - 中风险(本迭代修复):**

- 缺失安全头(CSP, HSTS, X-Frame-Options)
- CI中无自动化依赖扫描
- 服务账号权限过大
- 无密钥轮换策略

**处理**: 解析安全态势快速检查的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回安全态势快速检查的响应数据,包含状态码、结果和日志.
### 2. OWASP Top 10 基础审计

```bash
#!/bin/bash
# OWASP Top 10 基础检查
echo "=== OWASP Top 10 基础审计 ==="
# ...
echo ""
echo "--- A01: 访问控制失效 ---"
grep -rn "params\.id\|req\.params\." --include='*.{py,js,ts,go}' . 2>/dev/null | \
  grep -i "user\|account\|order" | head -5
# ...
echo ""
echo "--- A02: 加密失败 ---"
grep -rn "md5\|sha1" --include='*.{py,js,ts,go}' . 2>/dev/null | grep -i "password"
# ...
echo ""
echo "--- A03: 注入 ---"
grep -rn "query\|execute" --include='*.{py,js,ts}' . 2>/dev/null | \
  grep -i "f\"\|format(\|%s\|\${" | grep -iv "parameterized\|prepared" | head -5
# ...
echo ""
echo "--- A07: XSS ---"
grep -rn "innerHTML\|HIGHRISKlySetInnerHTML\|v-html" \
  --include='*.{js,ts,jsx,tsx,vue}' . 2>/dev/null | head -5
# ...
echo ""
echo "--- A05: 安全配置错误 ---"
grep -rn "DEBUG\s*=\s*True\|debug:\s*true" \
  --include='*.{py,js,ts,yml,yaml}' . 2>/dev/null | grep -v test
```

**处理**: 解析OWASP Top 10 基础审计的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回OWASP Top 10 基础审计的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 威胁登记管理

使用YAML格式记录识别到的威胁,便于跟踪管理:

```yaml
# threat-register.yaml
threats:
  - id: "T-001"
    component: "用户认证API"
    category: "S"  # Spoofing
    description: "JWT令牌未验证算法,可能被alg=none绕过"
    likelihood: 4
    impact: 5
    risk_score: 20
    mitigation: "强制验证JWT算法为RS256或EdDSA"
    priority: "P0"
    status: "open"
# ...
  - id: "T-002"
    component: "用户输入处理"
    category: "T"  # Tampering
    description: "SQL查询使用字符串拼接,存在注入风险"
    likelihood: 3
    impact: 5
    risk_score: 15
    mitigation: "使用参数化查询替换字符串拼接"
    priority: "P1"
    status: "open"
```

**处理**: 解析威胁登记管理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回威胁登记管理的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：轻量级安全评估与、威胁建模工具、提供安全态势检查、OWASP、基础审计与漏洞管、适合个人开发者快、速安全自查、网络安全评估引擎、免费版、为个人开发者提供、基础安全评估与威、胁建模能力、核心能力、安全态势快速检查、Top、基础审计、威胁登记管理、漏洞生命周期跟踪、适用场景、项目上线前安全自、代码安全审查、基础威胁建模、差异化、免费版聚焦核心评、估能力、无需额外工具依赖、速上手、适用关键词、安全评估、威胁建模、漏洞管理、security、assessment、threat、modeling等.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景

### 场景一:项目上线前安全自查

```bash
#!/bin/bash
# 项目上线前安全自查脚本
PROJECT_DIR="${1:-.}"
cd "$PROJECT_DIR"
# ...
echo "========================================="
echo "项目安全自查: $(basename "$(pwd)")"
echo "检查时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "========================================="
# ...
ISSUES=0
# ...
echo ""
echo "--- 1. 密钥泄露检查 ---"
for pattern in 'AKIA[0-9A-Z]\{16\}' 'BEGIN.*PRIVATE KEY' 'sk-[A-Za-z0-9]\{20,\}' 'ghp_[A-Za-z0-9]\{36\}'; do
    count=$(grep -rn "$pattern" --include='*. 2>/dev/null | \
git\|example\|test' | wc -l)
    [ "$count" -gt 0 ] && echo "  [!] 发现 ${count} 处匹配: ${pattern}" && ((ISSUES++))
done
# ...
echo ""
echo "--- 2. 依赖漏洞检查 ---"
if [ -f package.json ]; then
    npm audit --audit-level=high 2>/dev/null && echo "  [OK] npm: 无高危漏洞" || echo "  [!] npm审计发现问题"
fi
if [ -f requirements.txt ]; then
    pip-audit -r requirements.txt 2>/dev/null && echo "  [OK] pip: 无已知漏洞" || echo "  [!] pip审计发现问题"
fi
# ...
echo ""
echo "--- 3. .gitignore 覆盖检查 ---"
if [ ! -f .gitignore ]; then
    echo "  [!] 未找到.gitignore文件"
    ((ISSUES++))
else
    for entry in '.env' 'node_modules' '*.key' '*.pem'; do
        grep -q "$entry" .gitignore 2>/dev/null && echo "  [OK] .gitignore包含: $entry" || echo "  [!] .gitignore缺失: $entry"
    done
fi
# ...
echo ""
echo "--- 4. SSL验证检查 ---"
SSL_DISABLED=$(grep -rn "verify\s*=\s*False\|rejectUnauthorized.*false" \
  --include='*.{py,js,ts,go}' . 2>/dev/null | grep -v 'test\|spec' | wc -l)
[ "$SSL_DISABLED" -gt 0 ] && echo "  [!] 发现 ${SSL_DISABLED} 处SSL验证禁用" && ((ISSUES++))
# ...
echo ""
echo "========================================="
echo "自查完成,发现问题: ${ISSUES} 项"
echo "========================================="
```

### 场景二:基础威胁建模

使用STRIDE方法对系统组件进行威胁分析:

```text
系统数据流:
[用户] -> [CDN/WAF] -> [负载均衡] -> [应用服务器] -> [数据库]
                                        ↘ [缓存]
                                        ↘ [消息队列]
# ...
信任边界识别:
- 互联网 -> DMZ (公网服务边界)
- DMZ -> 内网 (应用与数据库边界)
- 用户 -> 管理员 (角色权限边界)
- 服务 -> 服务 (API密钥边界)
```

### 场景三:漏洞修复优先级排序

```text
优先级规则:
- P0 (风险 >= 20): 立即修复,暂停其他工作
- P1 (风险 12-19): 一周内修复
- P2 (风险 6-11): 一个迭代内修复
- P3 (风险 <= 5): 有空时修复
# ...
风险评分 = 可能性(1-5) x 影响(1-5)
```

## 快速开始

### 领先步:运行安全态势检查

```bash
# 克隆或进入项目目录
cd /path/to/your/project
# ...
# 运行关键风险检查
bash security-check.sh
```

### 第二步:执行OWASP基础审计

```bash
# 检查注入风险
py' . | grep -i "f\"\|%s"
# ...
# 检查XSS风险
grep -rn "innerHTML\|HIGHRISKlySetInnerHTML" --include='*.{js,ts,jsx}' .
```

### 第三步:创建威胁登记表

```yaml
# 创建 threat-register.yaml
threats:
  - id: "T-001"
    component: "你的组件名"
    category: "S"
    description: "威胁描述"
    likelihood: 3
    impact: 4
    risk_score: 12
    priority: "P1"
    status: "open"
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
#
## 示例

### 安全头配置参考

```text
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Content-Security-Policy: default-src 'self'; script-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
```

### 密码策略参考

```yaml
password_policy:
  minimum_length: 12
  check_against_breached: true
  rate_limit_attempts: "5次/15分钟"
  storage: "bcrypt cost 12+ 或 Argon2id"
```

### 严重级别与修复SLA

| 严重级别 | CVSS范围 | 修复SLA | 升级路径 |
|---:|---:|---:|---:|
| 严重 | 9.0-10.0 | 24小时 | 立即通知CTO/CISO |
| 高危 | 7.0-8.9 | 7天 | 通知团队负责人 |
| 中危 | 4.0-6.9 | 30天 | 加入迭代待办 |
| 低危 | 0.1-3.9 | 90天 | 记录跟踪 |

## 优秀实践

1. **默认拒绝**:防火墙默认拒绝所有入站流量,仅开放必要端口.
2. **最小权限**:所有服务账号使用最小必要权限.
3. **深度防御**:输入验证、输出转义、参数化查询、最小权限层层把关.
4. **持续扫描**:将安全扫描集成到CI/CD,而非偶尔检查.
5. **假设已被入侵**:设计时假设攻击者已在内部,验证一切.
```bash
# 安全检查集成到git pre-commit钩子
#!/bin/bash
# .git/hooks/pre-commit
STAGED=$(git diff --cached --name-only --diff-filter=ACM)
for pattern in 'AKIA[0-9A-Z]{16}' 'BEGIN.*PRIVATE KEY' 'sk-[A-Za-z0-9]{20,}'; do
    matches=$(echo "$STAGED" | xargs grep -Pn "$pattern" 2>/dev/null)
    if [ -n "$matches" ]; then
        echo "阻止提交: 检测到疑似密钥"
        echo "$matches"
        exit 1
    fi
done
```

## 常见问题

### Q1: 免费版能做渗透测试吗?

免费版提供渗透测试方法论参考,但不包含自动化渗透测试工具。如需深度渗透测试,建议使用专业版或专用渗透测试工具.
### Q2: 安全评分如何计算?

免费版使用基础评分:统计失败项数量。0-2项=良好,3-5项=需改进,6项以上=暂停功能开发,优先修复安全问题.
### Q3: 支持哪些合规框架?

免费版提供OWASP Top 10基础检查。SOC 2、ISO 27001、GDPR、HIPAA等合规框架映射需要专业版支持.
### Q4: 如何处理误报?

对每个检查结果人工确认,排除测试代码、示例文件和mock数据中的匹配。建议在grep中添加排除模式.
### Q5: 检查结果需要保存吗?

建议将检查结果保存为报告,定期对比跟踪安全态势变化。免费版输出文本格式报告.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Shell**: Bash(脚本示例使用Bash语法)

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| grep | 文本搜索工具 | 必需 | 系统自带 |
| npm | 包管理器 | 按需 | nodejs.org 下载 |
| pip-audit | Python审计工具 | 按需 | `pip install pip-audit` |
| jq | JSON处理工具 | 推荐 | `apt install jq` / `brew install jq` |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 免费版为纯知识驱动,无需额外API Key
- 依赖扫描工具(npm audit, pip-audit)使用各自的默认配置

### 可用性分类
- **分类**: MD+EXEC模式纯Markdown指令,核心功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行安全评估与威胁建模任务

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 执行效率受模型能力与网络环境影响
- 不能替代专业安全审计，仅提供辅助检查能力
- 加密强度依赖正确配置的密钥与算法参数
- 安全策略需定期更新以应对新威胁

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "网络安全评估引擎免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "cybersecurity engine"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
