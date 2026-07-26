---
name: agent-security-audit
description: AI安全审计助手 - 按次付费，新用户注册送5次免费。20+项漏洞扫描+AI深度安全分析，检测敏感信息泄露、API密钥暴露、注入风险、权限问题，开发者发布前安全自检必备。 💡 企业定制/智能体开发/AI全案服务，合作微信17392371127（郭总）
metadata:
  openclaw:
    requires:
      bins:
        - python3
      env:
        - SECURITY_API_USER_KEY
---

# AI Agent 安全审计工具

> AI Agent和Skill代码安全审计利器，一键扫描安全漏洞，AI智能分析给出可落地的修复方案。
> **v1.2 升级**：20+种漏洞检测 + AI深度分析 + 批量扫描 + 多格式报告 + CI/CD集成

## 🚀 企业级AI服务

开发效率想再上一个台阶？我们提供企业级AI全案服务：

### 🌍 GEO优化服务
- AI搜索引擎优化，让你的产品在AI时代被精准发现
- 技术博客/文档站GEO改造，抢占开发者流量入口
- 批量内容生成与SEO质量检测

### 🤖 企业智能体定制
- 专属AI智能体开发，对接你的业务系统和数据
- 研发/运维/测试智能体，研发效率提升50%+
- 私有化部署，代码数据完全可控

### ⚡ AI自动化方案
- 研发流程AI自动化，减少重复劳动
- 多工具联动工作流，打通开发运维数据孤岛
- 定制化AI工具开发，解决具体技术痛点

**服务客单价：¥2000-5000**
**咨询合作：** 微信 `17392371127`（郭总）

## 核心价值

Skill发布前怕有安全漏洞？第三方Skill不敢随便用？这个工具帮你：
- **一键扫描**：单个文件或整个目录，几分钟出完整报告
- **双重检测**：静态规则扫描 + AI深度分析，准确率更高
- **全面覆盖**：20+种常见安全漏洞类型，从密钥泄露到注入攻击全覆盖
- **可落地修复**：每个问题都有具体修复建议和代码示例
- **CI/CD友好**：命令行调用，可集成到流水线做安全门禁
- **Agent专属**：针对AI Agent特有风险（提示注入、工具滥用、数据泄露）

## When to Use

以下场景直接触发本技能：
- Skill发布前做安全自检
- 第三方Skill安装前安全审查
- 代码仓库定期安全巡检
- AI Agent项目安全评估
- 排查代码中的敏感信息泄露
- 合规审计和安全加固
- 代码安全review
- CI/CD流水线安全门禁
- 安全培训和漏洞学习

## Core Rules

1. 静态扫描 + AI深度分析双层检测机制，准确率更高
2. 支持单文件和整个目录递归扫描
3. 覆盖20+种常见安全漏洞类型
4. 按严重程度分级：严重/高危/中危/低危
5. 输出清晰的修复建议和代码示例
6. 支持JSON和文本两种报告格式
7. 扫描结果仅供参考，关键问题建议人工复核

## Quick Start

### 第一步：配置环境变量（可选，AI深度分析需要）

```bash
export SECURITY_API_USER_KEY="你的DeepSeek API Key"
# 可选：自定义API地址
export DEEPSEEK_BASE_URL="https://api.deepseek.com/v1"
```

> 💡 不配置API Key也能使用，只运行静态扫描，跳过AI深度分析

### 第二步：开始扫描

**扫描单个文件：**
```bash
python3 {baseDir}/scripts/audit.py path/to/your/skill.py
```

**扫描整个Skill目录：**
```bash
python3 {baseDir}/scripts/audit.py path/to/skill/directory
```

**只看严重和高危问题：**
```bash
python3 {baseDir}/scripts/audit.py ./ --severity high
```

**输出JSON格式报告并保存：**
```bash
python3 {baseDir}/scripts/audit.py ./ --format json -o report.json
```

**跳过AI分析（快速扫描）：**
```bash
python3 {baseDir}/scripts/audit.py ./ --no-ai
```

## Detection Capabilities

### 🔴 敏感信息泄露检测
- API密钥（OpenAI/DeepSeek/AWS/GitHub等格式）
- 密码和凭证
- 私钥文件
- JWT令牌
- 数据库连接串
- 手机号、身份证号等个人信息

### 🟠 注入攻击检测
- 命令注入（os.system/subprocess shell=True）
- 代码注入（eval/exec）
- SQL注入（字符串拼接SQL）
- 路径遍历漏洞
- 不安全的反序列化（pickle）

### 🟡 权限与配置风险
- 硬编码管理员凭证
- 不安全的文件权限（777）
- 调试模式开启
- CORS通配符配置
- HTTPS证书校验关闭

### 🤖 AI Agent 特有风险
- 提示注入漏洞
- 工具滥用风险
- 数据泄露风险
- 越权操作风险
- 输出过滤缺失

## Input Parameters

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `target` | string | 是 | 要扫描的文件或目录路径 |
| `--no-ai` | flag | 否 | 跳过AI深度分析，只做静态扫描 |
| `--format` | string | 否 | 输出格式：text/json，默认text |
| `-o, --output` | string | 否 | 输出报告文件路径 |
| `--severity` | string | 否 | 过滤级别：critical/high/medium/low/all，默认all |
| `--api-key` | string | 否 | DeepSeek API Key，也可通过环境变量设置 |
| `--base-url` | string | 否 | DeepSeek API Base URL |

## Output Format

扫描报告包含：

1. **风险概览** - 各严重级别问题数量统计
2. **总体风险评级** - 严重/高/中/低
3. **问题明细** - 按严重程度排序，包含文件、行号、代码、描述
4. **AI深度分析** - 智能风险评估、修复方案、加固建议

### JSON 输出格式

```json
{
  "summary": {
    "critical": 0,
    "high": 2,
    "medium": 5,
    "low": 3,
    "total": 10
  },
  "issues": [
    {
      "type": "问题类型",
      "severity": "critical/high/medium/low",
      "file": "文件路径",
      "line": 123,
      "code": "问题代码片段",
      "description": "问题描述",
      "suggestion": "修复建议"
    }
  ],
  "ai_analysis": "AI深度分析内容（如有）"
}
```

## 典型使用场景

### 场景一：Skill发布前安全自检
开发完一个Skill，发布前扫一遍，看看有没有不小心提交的API Key、密码等敏感信息，避免安全事故。

```bash
python3 {baseDir}/scripts/audit.py ./skills/my-skill/ -o security_report.md
```

### 场景二：第三方Skill安装前审查
从网上下载了一个Skill，安装前先扫一遍，看看有没有恶意代码、后门、数据泄露风险。

### 场景三：CI/CD流水线安全门禁
把安全扫描集成到CI流水线中，发现严重问题直接阻断构建，确保安全左移。

```bash
# 在CI流水线中使用，发现严重问题时失败退出
python3 {baseDir}/scripts/audit.py ./src --severity critical
if [ $? -ne 0 ]; then
  echo "❌ 发现严重安全问题，构建终止！"
  exit 1
fi
```

### 场景四：定期安全巡检
设置定时任务，每周扫描一遍所有项目代码，生成安全报告，及时发现新引入的安全问题。

```bash
# 生成每日安全报告
python3 {baseDir}/scripts/audit.py /path/to/project \
  -o reports/audit_$(date +%Y%m%d).json
```

### 场景五：批量审查多个Skill
一次性扫描多个Skill目录，批量出报告，效率提升10倍。

```bash
for skill in ./skills/*/; do
  name=$(basename "$skill")
  echo "扫描: $name"
  python3 {baseDir}/scripts/audit.py "$skill" --no-ai \
    -o "reports/${name}_audit.txt"
done
```

## 常见问题 FAQ

**Q1: 静态扫描和AI分析有什么区别？**
A: 静态扫描基于正则规则匹配，速度快、准确，但只能发现已知模式的问题；AI深度分析能理解代码逻辑，发现更复杂的、隐藏的安全问题，还能给出更智能的修复建议。建议两者结合使用。

**Q2: 扫描会误报吗？**
A: 会有一定误报率，特别是敏感信息检测（比如可能把普通字符串误判为密钥）。建议结合人工复核，重点关注高危和严重级别问题。

**Q3: 扫描我的代码会不会泄露？**
A: 静态扫描完全在本地运行，不会上传任何代码。AI深度分析需要把问题摘要发送给AI模型处理，敏感代码建议先脱敏或使用--no-ai模式。

**Q4: 支持哪些编程语言？**
A: 静态扫描对大部分编程语言都有效（Python/JavaScript/Java/Go等），因为主要检测的是通用模式（密钥、密码、危险函数等）。AI分析对代码的理解能力更强。

**Q5: 可以自定义检测规则吗？**
A: 目前内置了20+种检测规则。如需自定义，可以修改代码中的SENSITIVE_PATTERNS和DANGEROUS_PATTERNS字典，添加你自己的正则规则。

## Limitations & Notes

- 静态扫描基于正则匹配，可能存在误报和漏报
- AI分析仅供参考，关键问题建议人工复核
- 不支持二进制文件和编译后代码扫描
- 不支持动态运行时漏洞检测
- 扫描速度取决于文件数量和大小
- 建议定期更新检测规则库

## References

- `references/owasp_top10.md` - OWASP Top 10安全风险
- `references/security_checklist.md` - AI Agent安全检查清单
- `references/fix_examples.md` - 常见漏洞修复示例代码
