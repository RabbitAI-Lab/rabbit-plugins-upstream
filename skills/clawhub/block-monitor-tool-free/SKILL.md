---
slug: block-monitor-tool-free
name: block-monitor-tool-free
version: 1.0.0
displayName: 内容验证网关免费版
summary: "AI生成内容验证与策略检查工具,支持黑白名单管理、内容分类与基础策略执行,适合个人开发者内容审核.。内容验证网关免费版,为个人开发者提供AI生成内容的验证与策略管理能力."
license: MIT
edition: free
description: "内容验证网关免费版,为个人开发者包含AI产出内容的验证与策略管控能力. 适用于需要block monitor tool相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量. 适用于需要block monitor tool相关能力的开发场景,包含结构化的工作流程和配置指引."
tags:
  - 安全
  - block
  - monitor
  - automation
  - productivity
  - 内容验证
  - 策略管理
  - 免费版
  - 监控
  - 运维
tools:
  - read
  - exec
homepage: ""
category: "Operations"
pricing_tier: free

---
本工具为AI应用开发者提供内容验证与策略管理能力,在AI生成内容输出前执行策略检查,通过黑白名单机制过滤不当内容。免费版支持基础策略检查、内容分类标记与验证结果记录,适合个人开发者对AI输出进行基础内容审核.
### 免费版与专业版对比
| 能力维度 | 免费版 | 专业版 |
|----|---|---|
| 策略类型 | 黑白名单 | +正则+语义+上下文 |
| 规则数量 | 最多50条 | 无限制 |
| 批量验证 | 不支持 | 批量处理 |
| 实时监控 | 不支持 | 实时拦截+告警 |
| 审计日志 | 基础记录 | 完整审计链 |
| 多语言支持 | 中文+英文 | 20+语言 |
| API集成 | 基础 | 完整REST API |

## 核心能力
### 1. 内容策略检查
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 内容验证网关免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```python
#!/usr/bin/env python3
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ...
result = "操作完成"
"""免费版内容策略检查引擎"""
import re
import json
from datetime import datetime
class ContentPolicyChecker:
    """内容策略检查器"""
    def __init__(self):
        self.blocklist = set()
        self.allowlist = set()
        self.patterns = []
        self.load_rules()
    def load_rules(self):
        """加载规则文件"""
        try:
            with open("blocklist.txt", "r", encoding="utf-8") as f:
                self.blocklist = set(line.strip().lower() for line in f if line.strip())
        except FileNotFoundError:
        try:
            with open("allowlist.txt", "r", encoding="utf-8") as f:
allowlist = set(line.strip().strip())
        except FileNotFoundError:
    def check_content(self, content):
        """检查内容是否合规"""
        result = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "content_length": len(content),
            "passed": True,
            "violations": []
        }
        content_lower = content.lower()
        for term in self.blocklist:
            if term in content_lower:
                result["violations"].append({
                    "type": "blocklist",
                    "term": term,
                    "severity": "HIGH"
                })
                result["passed"] = False
        if not result["passed"]:
                if term in content_lower:
                    result["violations"] = [
                        v for v in result["violations"]
                        if v["term"] not in content_lower or term == v["term"]
                    ]
        sensitive_patterns = [
            (r'\b\d{3}-\d{2}-\d{4}\b', "SSN格式", "CRITICAL"),
            (r'\b\d{16}\b', "信用卡号格式", "CRITICAL"),
            (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', "邮箱地址", "MEDIUM"),
            (r'\b\d{3}\.\d{3}\.\d{3}\.\d{3}\b', "IP地址", "MEDIUM"),
        ]
        for pattern, desc, severity in sensitive_patterns:
            matches = re.findall(pattern, content)
            if matches:
                    "type": "pattern",
                    "description": desc,
                    "count": len(matches),
                    "severity": severity
                })
                if severity in ["CRITICAL", "HIGH"]:
                    result["passed"] = False
        return result
if __name__ == "__main__":
    checker = ContentPolicyChecker()
    test_content = "这是一段测试内容,包含敏感词和 user@example.com 邮箱地址"
    result = checker.check_content(test_content)
    print(json.dumps(result, indent=2, ensure_ascii=False))
```

**处理**: 解析内容策略检查的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回内容策略检查的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 黑白名单管理
```bash
#!/bin/bash
RULES_DIR="./rules"
mkdir -p "$RULES_DIR"
# ...
add_blocklist() {
    local term=$1
    echo "$term" >> "${RULES_DIR}/blocklist.txt"
    sort -u "${RULES_DIR}/blocklist.txt" -o "${RULES_DIR}/blocklist.txt"
    echo "已添加到黑名单: ${term}"
}
# ...
add_allowlist() {
    local term=$1
    echo "$term" >> "${RULES_DIR}/allowlist.txt"
    sort -u "${RULES_DIR}/allowlist.txt" -o "${RULES_DIR}/allowlist.txt"
    echo "已添加到白名单: ${term}"
}
# ...
list_rules() {
    echo "=== 黑名单 ==="
    [ -f "${RULES_DIR}/blocklist.txt" ] && cat "${RULES_DIR}/blocklist.txt" || echo "(空)"
    echo ""
    echo "=== 白名单 ==="
    [ -f "${RULES_DIR}/allowlist.txt" ] && cat "${RULES_DIR}/allowlist.txt" || echo "(空)"
}
# ...
remove_term() {
    local term=$1
    local file=$2
    sed -i "/^${term}$/d" "${RULES_DIR}/${file}"
    echo "已移除: ${term}"
}
# ...
echo "初始化规则目录..."
add_blocklist "密码"
add_blocklist "信用卡"
add_blocklist "身份证号"
add_allowlist "密码学"  # 白名单豁免
list_rules
```

**处理**: 解析黑白名单管理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回黑白名单管理的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 内容分类标记
```python
#!/usr/bin/env python3
"""内容分类标记工具"""
# ...
import re
# ...
class ContentClassifier:
    """内容分类器"""
# ...
    CATEGORIES = {
        "personal_info": {
            "patterns": [
                (r'\b\d{3}-\d{2}-\d{4}\b', "SSN"),
                (r'\b\d{17}[\dXx]\b', "中国身份证号"),
\d{3}\.\d{3}\.\d{3}\b', "IP地址"),
_%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', "邮箱"),
            ],
            "label": "个人信息"
        },
        "financial": {
            "patterns": [
                (r'\b\d{16}\b', "信用卡号"),
                (r'\b\d{3}\s?\d{3}\s?\d{3}\s?\d{3}\b', "信用卡号(带空格)"),
                (r'CVV|CVC|安全码', "安全码"),
            ],
            "label": "金融信息"
        },
        "credentials": {
            "patterns": [
                (r'password\s*[:=]\s*\S+', "密码"),
                (r'api[_-]?key\s*[:=]\s*\S+', "API密钥"),
                (r'secret\s*[:=]\s*\S+', "密钥"),
                (r'token\s*[:=]\s*\S+', "令牌"),
            ],
            "label": "凭证信息"
        },
        "code": {
            "patterns": [
                (r'function\s+\w+\s*\(', "JavaScript函数"),
                (r'def\s+\w+\s*\(', "Python函数"),
                (r'class\s+\w+', "类定义"),
            ],
            "label": "代码片段"
        }
    }
# ...
    def classify(self, content):
        """分类内容"""
        classifications = []
# ...
        for category, config in self.CATEGORIES.items():
            matches = []
            for pattern, desc in config["patterns"]:
                found = re.findall(pattern, content, re.IGNORECASE)
                if found:
                    matches.append({
                        "type": desc,
                        "count": len(found),
                        "sample": found[0][:50] if found else ""
                    })
# ...
            if matches:
                classifications.append({
                    "category": category,
                    "label": config["label"],
                    "matches": matches
                })
# ...
        return classifications
# ...
if __name__ == "__main__":
    import json
    classifier = ContentClassifier()
# ...
    test = "用户的邮箱是 test@example.com,password=123456"
    result = classifier.classify(test)
    print(json.dumps(result, indent=2, ensure_ascii=False))
```

**处理**: 解析内容分类标记的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回内容分类标记的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 验证结果记录
```bash
#!/bin/bash
LOG_DIR="./logs"
mkdir -p "$LOG_DIR"
LOG_FILE="${LOG_DIR}/verification_$(date '+%Y%m%d').log"
# ...
log_verification() {
    local content_preview=$1
    local result=$2
    local timestamp=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
# ...
    echo "[${timestamp}] Result: ${result} | Preview: ${content_preview}" >> "$LOG_FILE"
}
# ...
view_today_log() {
    echo "=== 今日验证日志 ==="
    [ -f "$LOG_FILE" ] && cat "$LOG_FILE" || echo "今日暂无日志"
}
# ...
stats_log() {
    echo "=== 验证统计 ==="
    TOTAL=$(wc -l < "$LOG_FILE" 2>/dev/null || echo "0")
    PASSED=$(grep -c "step_done" "$LOG_FILE" 2>/dev/null || echo "0")
    FAILED=$(grep -c "FAIL" "$LOG_FILE" 2>/dev/null || echo "0")
    echo "  总验证次数: ${TOTAL}"
    echo "  通过: ${PASSED}"
    echo "  拒绝: ${FAILED}"
}
```

**处理**: 解析验证结果记录的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回验证结果记录的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：生成内容验证与策、略检查工具、支持黑白名单管理、内容分类与基础策、略执行、适合个人开发者内、容审核、内容验证网关免费、为个人开发者提供、生成内容的验证与、策略管理能力、核心能力、适用场景、输出内容审核、敏感内容过滤、内容发布前验证、差异化、免费版聚焦基础策、支持单规则管理、适合个人项目快速、适用关键词、内容验证、内容审核等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景一:AI输出内容审核
```python
#!/usr/bin/env python3
"""AI输出内容审核流程"""
# ...
import json
# ...
def audit_ai_output(content, checker):
    """审核AI生成的内容"""
check_content(content)
# ...
    if result["passed"]:
        return {
            "decision": "ALLOW",
            "message": "内容通过验证",
            "violations": 0
        }
    else:
        violations = result["violations"]
        critical = [v for v in violations if v.get("severity") == "CRITICAL"]
# ...
        if critical:
            return {
                "decision": "BLOCK",
                "message": f"内容包含严重违规: {len(critical)}项",
                "violations": len(violations)
            }
        else:
            return {
                "decision": "REVIEW",
                "message": f"内容需要人工审核: {len(violations)}项违规",
                "violations": len(violations)
            }
# ...
from content_policy import ContentPolicyChecker
# ...
checker = ContentPolicyChecker()
ai_output = "AI生成的内容..."
decision = audit_ai_output(ai_output, checker)
print(json.dumps(decision, indent=2, ensure_ascii=False))
```bash
# 在此执行相关操作
echo "操作完成"
```bash
#!/bin/bash
INPUT_FILE=$1
OUTPUT_FILE="${1%.txt}_filtered.txt"
# ...
echo "=== 敏感信息过滤 ==="
echo "输入: ${INPUT_FILE}"
echo "输出: ${OUTPUT_FILE}"
echo ""
# ...
BLOCKLIST=$(cat rules/blocklist.txt 2>/dev/null)
# ...
CONTENT=$(cat "$INPUT_FILE")
FILTERED="$CONTENT"
# ...
for term in $BLOCKLIST; do
    FILTERED=$(echo "$FILTERED" | sed "s/${term}/***REDACTED***/gi")
done
# ...
echo "$FILTERED" > "$OUTPUT_FILE"
# ...
REPLACEMENTS=$(diff "$INPUT_FILE" "$OUTPUT_FILE" | grep -c "REDACTED" || echo "0")
echo "过滤完成: 替换了 ${REPLACEMENTS} 处敏感内容"
```bash
# 在此执行相关操作
echo "操作完成"
```bash
#!/bin/bash
CONTENT_FILE=$1
# ...
echo "=== 发布前内容检查 ==="
echo ""
# ...
echo "--- 1. 策略检查 ---"
python3 -c "
import json
from content_policy import ContentPolicyChecker
# ...
checker = ContentPolicyChecker()
with open('${CONTENT_FILE}', 'r') as f:
    content = f.read()
# ...
result = checker.check_content(content)
print(json.dumps(result, indent=2, ensure_ascii=False))
# ...
if not result['passed']:
    print('\n[!] 内容未通过验证,请修正后发布')
    exit(1)
else:
    print('\n[OK] 内容通过验证')
"
# ...
echo ""
echo "--- 2. 敏感信息检查 ---"
grep -in "password\|secret\|key.*=\|token" "$CONTENT_FILE" | head -5 || echo "  未发现敏感信息"
# ...
echo ""
echo "=== 检查完成 ==="
```bash
# 在此执行相关操作
echo "操作完成"
```bash
mkdir -p rules
echo "敏感词1" > rules/blocklist.txt
echo "敏感词2" >> rules/blocklist.txt
```bash
# 在此执行相关操作
echo "操作完成"
```python
from content_policy import ContentPolicyChecker
# ...
checker = ContentPolicyChecker()
result = checker.check_content("要检查的内容")
print("通过" if result["passed"] else "拒绝")
```bash
# 在此执行相关操作
echo "操作完成"
```bash
cat logs/verification_$(date '+%Y%m%d').log
```

## 配置示例
### 规则文件格式
| 文件 | 格式 | 说明 |
|---:|---:|---:|
| blocklist.txt | 每行一个词条 | 黑名单,匹配则拒绝 |
| allowlist.txt | 每行一个词条 | 白名单,豁免黑名单 |
| patterns.json | JSON数组 | 正则模式规则 |

### 敏感信息检测模式
| 模式名称 | 正则表达式 | 严重级别 |
|:---:|:---:|:---:|
| SSN | `\d{3}-\d{2}-\d{4}` | CRITICAL |
| 信用卡 | `\d{16}` | CRITICAL |
| 身份证 | `\d{17}[\dXx]` | CRITICAL |
| 邮箱 | `[A-Za-z0-9._%+-]+@...` | MEDIUM |
| IP地址 | `\d{3}\.\d{3}\.\d{3}\.\d{3}` | MEDIUM |
| 密码 | `password\s*[:=]\s*\S+` | HIGH |

## 优秀实践
1. **最小黑名单**:仅添加必要的黑名单词条,避免过度过滤.
2. **白名单豁免**:对合法包含敏感词的内容使用白名单豁免.
3. **分级处理**:CRITICAL直接拒绝,HIGH人工审核,MEDIUM记录日志.
4. **定期更新**:根据业务需求定期更新黑白名单规则.
5. **日志留痕**:所有验证结果记录日志,便于追溯审计.
## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+(使用Python检查引擎时需要)

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| python3 | 运行时环境 | 推荐 | python.org 下载 |
| grep | 文本搜索 | 必需 | 系统自带 |
| sed | 文本处理 | 推荐 | 系统自带 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 免费版为纯本地处理,无需API Key
- 规则文件存储在本地,不发送内容到外部

### 可用性分类
- **分类**: MD+EXEC模式纯Markdown指令,核心功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行内容验证与策略管理任务

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
- 当前为免费版本,如需完整功能请升级到付费版获取全部能力
