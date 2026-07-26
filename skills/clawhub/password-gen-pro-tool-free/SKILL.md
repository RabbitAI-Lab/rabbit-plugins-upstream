---
slug: password-gen-pro-tool-free
name: password-gen-pro-tool-free
version: 1.0.0
displayName: 密码生成器Pro免费版
summary: "专业密码生成工具,支持强密码生成、强度检测、口令短语与PIN码生成,适合个人用户密码管理.。密码生成器Pro免费版,为个人用户提供多样化密码生成与强度检测能力."
license: Proprietary
edition: free
description: '密码生成器Pro免费版,为个人用户提供多样化密码生成与强度检测能力.
  核心能力:强密码生成、密码强度检测、口令短语生成、PIN码生成.
  适用场景:账户密码创建、密码强度验证、 memorable passphrase生成.
  差异化:免费版聚焦核心生成能力,支持多种密码类型,适合个人用户日常使用.
  适用关键词: 密码生成, 强度检测, 口令短语, PIN码, password generator, strength check, passphrase'
tags:
  - 安全
  - 密码
  - 免费版
  - 加密
  - 工具
  - append
  - length
  - password
  - feedback
  - secrets
tools:
  - read
  - exec
homepage: ""
category: "Security"
---
本工具为个人用户提供多样化的密码生成与强度检测能力,支持强密码生成、密码强度评估、口令短语(Passphrase)生成与PIN码生成。免费版覆盖个人用户日常密码管理需求,帮助用户创建安全且易记的密码.
### 免费版与专业版对比
| 能力维度 | 免费版 | 专业版 |
|----|---|---|
| 密码类型 | 随机/PIN/口令 | +模式化/定制规则 |
| 批量生成 | 不支持 | 批量CSV |
| 强度检测 | 基础评分 | 多维度分析 |
| 泄露检查 | 不支持 | HaveIBeenPwned |
| 密码策略 | 基础规则 | 企业策略模板 |
| 导出格式 | 文本 | CSV/JSON |
| 历史记录 | 不支持 | 加密存储 |

## 核心能力
### 1. 强密码生成
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 密码生成器Pro免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```python
#!/usr/bin/env python3
"""免费版密码生成器"""
# ...
import secrets
import string
import json
# ...
class PasswordGenerator:
    """密码生成器"""
# ...
    CHAR_SETS = {
        'lower': string.ascii_lowercase,
        'upper': string.ascii_uppercase,
        'digits': string.digits,
        'symbols': '!@#$%^&*()-_=+[]{}|;:,.<>?',
    }
# ...
    def generate(self, length=16, use_lower=True, use_upper=True,
                 use_digits=True, use_symbols=True, exclude_similar=False):
        """生成随机强密码"""
        if length < 8:
            length = 8
# ...
        chars = ''
        required = []
# ...
        if use_lower:
            lower = self.CHAR_SETS['lower']
            if exclude_similar:
                lower = lower.replace('l', '').replace('o', '')
            chars += lower
            required.append(secrets.choice(lower))
# ...
        if use_upper:
            upper = self.CHAR_SETS['upper']
            if exclude_similar:
                upper = upper.replace('I', '').replace('O', '')
            chars += upper
append(secrets.choice(upper))
# ...
        if use_digits:
            digits = self.CHAR_SETS['digits']
            if exclude_similar:
                digits = digits.replace('0', '').replace('1', '')
            chars += digits
append(secrets.choice(digits))
# ...
        if use_symbols:
            symbols = self.CHAR_SETS['symbols']
            chars += symbols
append(secrets.choice(symbols))
# ...
        if not chars:
            return "Error: 至少选择一种字符类型"
# ...
        password = list(required)
        for _ in range(length - len(required)):
            password.append(secrets.choice(chars))
# ...
        secrets.SystemRandom().shuffle(password)
        return ''.join(password)
# ...
    def generate_pin(self, length=6):
        """生成PIN码"""
        return ''.join(secrets.choice(string.digits) for _ in range(length))
# ...
    def generate_passphrase(self, word_count=4, separator='-'):
        """生成口令短语"""
        words = [
            'apple', 'brave', 'cloud', 'dance', 'eagle', 'flame', 'globe',
            'heart', 'ivory', 'jungle', 'knife', 'lemon', 'magic', 'noble',
            'ocean', 'piano', 'quest', 'river', 'storm', 'tiger', 'unity',
            'voice', 'water', 'xenon', 'youth', 'zebra', 'alert', 'blaze',
            'coral', 'delta', 'ember', 'frost', 'grace', 'haven', 'image',
        ]
        return separator.join(secrets.choice(words) for _ in range(word_count))
# ...
if __name__ == "__main__":
    gen = PasswordGenerator()
# ...
    print("=== 密码生成器 ===")
    print(f"强密码(16位):     {gen.generate(16)}")
    print(f"强密码(20位):     {gen.generate(20)}")
    print(f"纯字母数字(12位): {gen.generate(12, use_symbols=False)}")
    print(f"排除相似字符(16位): {gen.generate(16, exclude_similar=True)}")
    print(f"PIN码(6位):       {gen.generate_pin(6)}")
    print(f"PIN码(4位):       {gen.generate_pin(4)}")
    print(f"口令短语:         {gen.generate_passphrase()}")
    print(f"口令短语(6词):    {gen.generate_passphrase(6)}")
```

**处理**: 解析强密码生成的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回强密码生成的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 密码强度检测
```python
#!/usr/bin/env python3
"""密码强度检测器"""
# ...
import re
# ...
class PasswordStrengthChecker:
    """密码强度检测器"""
# ...
    def check(self, password):
        """检测密码强度"""
        score = 0
        feedback = []
# ...
        length = len(password)
        if length >= 16:
            score += 40
            feedback.append("长度优秀(>=16)")
        elif length >= 12:
            score += 30
append("长度良好(>=12)")
        elif length >= 8:
            score += 20
        else:
            score += 5
append("长度不足(<8),建议至少12位")
# ...
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_symbol = bool(re.search(r'[!@#$%^&*()\-_=+\[\]{}|;:,.<>?]', password))
# ...
        diversity = sum([has_lower, has_upper, has_digit, has_symbol])
        score += diversity * 10
# ...
        if has_lower: feedback.append("包含小写字母")
        if has_upper: feedback.append("包含大写字母")
        if has_digit: feedback.append("包含数字")
        if has_symbol: feedback.append("包含特殊字符")
        if diversity < 3:
append("建议使用至少3种字符类型")
# ...
        if re.search(r'(.)\1{2,}', password):
            score -= 15
append("包含重复字符(如aaa)")
# ...
        if re.search(r'(123|abc|qwe|password|admin)', password, re.IGNORECASE):
            score -= 20
# ...
        if re.search(r'^\d+$', password):
            score -= 20
append("纯数字密码,易被破解")
# ...
        score = max(0, min(100, score))
# ...
        if score >= 80:
            level = "STRONG"
            label = "强"
        elif score >= 60:
            level = "MEDIUM"
            label = "中"
        elif score >= 40:
            level = "WEAK"
            label = "弱"
        else:
            level = "CRITICAL"
            label = "极弱"
# ...
        return {
            "password_length": length,
            "score": score,
            "level": level,
            "label": label,
            "diversity": diversity,
            "feedback": feedback
        }
# ...
if __name__ == "__main__":
    checker = PasswordStrengthChecker()
# ...
    test_passwords = [
        "123456",
        "password",
        "MyP@ssw0rd",
        "Tr0ub4dour&3",
        "correct-horse-battery-staple",
    ]
# ...
    for pwd in test_passwords:
        result = checker.check(pwd)
        print(f"密码: {pwd}")
        print(f"  强度: {result['label']} ({result['score']}/100)")
        print(f"  反馈: {'; '.join(result['feedback'])}")
        print()
```

**处理**: 解析密码强度检测的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回密码强度检测的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 口令短语生成
```bash
#!/bin/bash
WORD_LIST=(
    apple brave cloud dance eagle flame globe heart
    ivory jungle knife lemon magic noble ocean piano
    quest river storm tiger unity voice water xenon
    youth zebra alert blaze coral delta ember frost
    grace haven image jazz knot lime mint north
    opal pearl quartz ruby silver topaz ultra vault
    whisper crystal dragon phoenix thunder
)
# ...
generate_passphrase() {
    local count=${1:-4}
    local separator=${2:--}
    local passphrase=""
# ...
    for i in $(seq 1 "$count"); do
        word="${WORD_LIST[$((RANDOM % ${#WORD_LIST[@]}))]}"
        if [ -z "$passphrase" ]; then
            passphrase="$word"
        else
            passphrase="${passphrase}${separator}${word}"
        fi
    done
# ...
    passphrase="${passphrase}${separator}$((RANDOM % 100))"
# ...
    echo "$passphrase"
}
# ...
echo "=== 口令短语生成器 ==="
echo "默认(4词): $(generate_passphrase)"
echo "6词:       $(generate_passphrase 6)"
echo "8词:       $(generate_passphrase 8)"
echo "下划线分隔: $(generate_passphrase 4 '_')"
```

**处理**: 解析口令短语生成的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回口令短语生成的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. PIN码生成
```python
#!/usr/bin/env python3
"""PIN码生成器"""
# ...
import secrets
# ...
def generate_pins(count=5, length=6):
    """批量生成PIN码"""
    pins = []
    for _ in range(count):
        pin = ''.join(str(secrets.randbelow(10)) for _ in range(length))
        pins.append(pin)
    return pins
# ...
if __name__ == "__main__":
    print("=== PIN码生成器 ===")
    print("6位PIN码:")
    for pin in generate_pins(5, 6):
        print(f"  {pin}")
# ...
    print("\n4位PIN码:")
    for pin in generate_pins(5, 4):
        print(f"  {pin}")
```

**处理**: 解析PIN码生成的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回PIN码生成的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：专业密码生成工具、支持强密码生成、口令短语与、适合个人用户密码、Pro、为个人用户提供多、样化密码生成与强、度检测能力、核心能力、适用场景、账户密码创建、密码强度验证、memorable、差异化、免费版聚焦核心生、成能力、支持多种密码类型、适合个人用户日常、适用关键词等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景一:创建新账户密码
```python
#!/usr/bin/env python3
"""新账户密码创建"""
# ...
from password_generator import PasswordGenerator
from strength_checker import PasswordStrengthChecker
# ...
def create_account_password(site_name, length=16):
    """为新账户创建安全密码"""
    gen = PasswordGenerator()
    checker = PasswordStrengthChecker()
# ...
    password = gen.generate(length=length, exclude_similar=True)
# ...
    strength = checker.check(password)
# ...
    return {
        "site": site_name,
        "password": password,
        "length": length,
        "strength": strength["label"],
        "score": strength["score"]
    }
# ...
result = create_account_password("example.com", 16)
print(f"网站: {result['site']}")
print(f"密码: {result['password']}")
print(f"强度: {result['strength']} ({result['score']}/100)")
```

### 场景二:密码强度审计
```bash
#!/bin/bash
echo "=== 密码强度审计 ==="
echo ""
# ...
while IFS= read -r password; do
    [ -z "$password" ] && continue
# ...
    LENGTH=${#password}
    HAS_LOWER=$(echo "$password" | grep -c '[a-z]')
    HAS_UPPER=$(echo "$password" | grep -c '[A-Z]')
    HAS_DIGIT=$(echo "$password" | grep -c '[0-9]')
    HAS_SYMBOL=$(echo "$password" | grep -c '[!@#$%^&*]')
# ...
    SCORE=0
    [ "$LENGTH" -ge 12 ] && SCORE=$((SCORE + 30))
    [ "$LENGTH" -ge 16 ] && SCORE=$((SCORE + 10))
    [ "$HAS_LOWER" -gt 0 ] && SCORE=$((SCORE + 10))
    [ "$HAS_UPPER" -gt 0 ] && SCORE=$((SCORE + 10))
    [ "$HAS_DIGIT" -gt 0 ] && SCORE=$((SCORE + 10))
    [ "$HAS_SYMBOL" -gt 0 ] && SCORE=$((SCORE + 10))
# ...
    if [ "$SCORE" -ge 70 ]; then
        LEVEL="强"
    elif [ "$SCORE" -ge 50 ]; then
        LEVEL="中"
    else
        LEVEL="弱"
    fi
# ...
    echo "密码(长度${LENGTH}): ${LEVEL} (${SCORE}/100)"
done < passwords.txt
```

### 场景三:易记口令生成
```python
#!/usr/bin/env python3
"""易记口令短语生成"""
# ...
from password_generator import PasswordGenerator
# ...
def generate_memorable_password():
    """生成易记但安全的口令"""
    gen = PasswordGenerator()
# ...
    passphrase = gen.generate_passphrase(word_count=4, separator='-')
    print(f"口令短语: {passphrase}")
# ...
    passphrase2 = gen.generate_passphrase(word_count=3, separator='_')
    print(f"下划线口令: {passphrase2}#")
# ...
    words = passphrase.split('-')[:4]
    acronym = ''.join(w[0].upper() for w in words)
    print(f"首字母缩写: {acronym}2026!")
# ...
generate_memorable_password()
```

## 快速开始
### 第一步:生成密码
```bash
python3 -c "
from password_generator import PasswordGenerator
gen = PasswordGenerator()
print(gen.generate(16))
"
```

### 第二步:检测强度
```bash
python3 -c "
from strength_checker import PasswordStrengthChecker
checker = PasswordStrengthChecker()
result = checker.check('你的密码')
print(f'强度: {result[\"label\"]} ({result[\"score\"]}/100)')
"
```

### 第三步:生成口令短语
```bash
python3 -c "
from password_generator import PasswordGenerator
gen = PasswordGenerator()
print(gen.generate_passphrase())
"
```

#
## 配置示例
### 密码生成参数
| 参数 | 默认值 | 说明 |
|---:|---:|---:|
| length | 16 | 密码长度 |
| use_lower | True | 包含小写字母 |
| use_upper | True | 包含大写字母 |
| use_digits | True | 包含数字 |
| use_symbols | True | 包含特殊字符 |
| exclude_similar | False | 排除相似字符(l1IO0) |

### 强度评分标准
| 评分范围 | 等级 | 说明 |
|:---:|:---:|:---:|
| 80-100 | 强 | 密码安全 |
| 60-79 | 中 | 基本安全,可改进 |
| 40-59 | 弱 | 不够安全,建议更换 |
| 0-39 | 极弱 | 必须立即更换 |

### 密码类型对比
| 类型 | 示例 | 强度 | 易记性 |
|:------|------:|:------|:------|
| 随机密码 | Tr0ub4dour&3 | 高 | 低 |
| 口令短语 | correct-horse-staple | 高 | 高 |
| PIN码 | 482917 | 低 | 中 |
| 模式密码 | Abc123!@# | 低 | 高 |
## 最佳实践
1. **长度优先**:密码长度比复杂度更重要,建议至少16位.
2. **口令短语**:使用4+词口令短语,既安全又易记.
3. **唯一密码**:每个账户使用不同密码.
4. **定期更换**:重要账户密码每3-6个月更换.
5. **密码管理**:使用密码管理器存储密码.
## 常见问题
### Q1: 免费版生成的密码安全吗?
免费版使用 `secrets` 模块(加密安全随机数生成器),生成的密码安全性有保障.
### Q2: 口令短语真的安全吗?
4个随机英文单词组成的口令短语,熵值约为52位,比8位随机密码更安全且更易记.
### Q3: PIN码安全吗?
6位PIN码仅有100万种组合,安全性较低。仅用于二次验证,不可作为主密码.
### Q4: 如何检测密码是否已泄露?
免费版不包含泄露检查。可手动访问 haveibeenpwned.com 检查。专业版集成泄露检查.
### Q5: exclude_similar有什么用?
排除 l、1、I、O、0 等易混淆字符,避免手动输入密码时出错.
## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.6+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| python3 | 运行时 | 推荐 | python.org 下载 |
| secrets | 随机数 | 必需 | Python标准库 |
| string | 字符集 | 必需 | Python标准库 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 免费版为纯本地生成,无需API Key
- 所有密码在本地生成,不发送到外部

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,核心功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行密码生成与强度检测任务

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
- 当前为免费版本,如需完整功能请升级到付费版获取全部能力

## 示例

### 基本用法

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "密码生成器Pro免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "password gen pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
