---
slug: bom-vuln-intel-tool-free
name: bom-vuln-intel-tool-free
version: 1.0.0
displayName: 物料清单漏洞情报免费版
summary: 软件物料清单(SBOM)生成与依赖漏洞检查工具,支持基础包扫描与OSV/GHSA查询,适合个人开发者日常使用.
license: MIT
edition: free
description: "物料清单漏洞情报免费版,为个人开发者包含软件物料清单产出与依赖漏洞查验能力. 适用于需要bom vuln intel tool相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量. 适用于需要bom vuln intel tool相关能力的开发场景,包含结构化的工作流程和配置指引."
tags:
  - 安全
  - bom
  - vuln
  - intel
  - automation
  - SBOM
  - 依赖管理
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
# 物料清单漏洞情报免费版

## 概述

本工具为个人开发者提供软件物料清单(SBOM)生成与依赖漏洞检测能力,支持查询npm、pip包信息,生成基础SBOM,并将依赖与OSV、GHSA漏洞数据库进行匹配。免费版支持单项目检查,覆盖npm与pip两种主流包生态,帮助开发者在更新依赖前快速识别已知漏洞.
### 免费版与专业版对比

| 能力维度 | 免费版 | 专业版 |
|----|---|---|
| 支持的包管理器 | npm, pip | npm, pip, go, cargo, maven, nuget |
| SBOM格式 | JSON基础格式 | CycloneDX, SPDX, CDX |
| 漏洞数据库 | OSV, GHSA | OSV, GHSA, NVD, OSV-API |
| 批量检查 | 不支持 | 多项目批量扫描 |
| 漏洞监控 | 手动检查 | 持续监控+告警 |
| 报告导出 | 文本/JSON | HTML/SARIF/PDF |
| CI/CD集成 | 基础脚本 | 完整流水线集成 |

## 核心能力

### 1. 包信息查询

查询npm或pip包的详细信息,包括版本、依赖、维护状态.
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 物料清单漏洞情报免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
#!/bin/bash
# 查询npm包信息
query_npm_package() {
    local pkg=$1
    echo "=== npm包信息: ${pkg} ==="
    curl -s "https://registry.npmjs.org/${pkg}" | jq '{
        name: .name,
        latest: ."dist-tags".latest,
        description: .description,
        license: .versions[."dist-tags".latest].license,
        dependencies_count: (.versions[."dist-tags".latest].dependencies | length)
    }'
}
# ...
# 查询pip包信息
query_pip_package() {
    local pkg=$1
    echo "=== pip包信息: ${pkg} ==="
    curl -s "https://pypi.org/pypi/${pkg}/json" | jq '{
        name: .info.name,
        version: .info.version,
        summary: .info.summary,
        license: .info.license,
        requires_python: .info.requires_python
    }'
}
# ...
# 示例
query_npm_package "express"
query_pip_package "flask"
```

**处理**: 解析包信息查询的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回包信息查询的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 基础SBOM生成

为当前项目生成基础软件物料清单.
```bash
#!/bin/bash
# 生成基础SBOM(JSON格式)
# ...
PROJECT_NAME=$(basename "$(pwd)")
TIMESTAMP=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
# ...
echo "{"
echo "  \"bomFormat\": \"JSON\","
echo "  \"specVersion\": \"1.0\","
echo "  \"project\": \"${PROJECT_NAME}\","
echo "  \"generated\": \"${TIMESTAMP}\","
echo "  \"components\": ["
# ...
# npm组件
if [ -f package.json ]; then
    echo "    // npm依赖:"
    cat package.json | jq -r '.dependencies // {} | to_entries[] | 
        "    {\"name\": \"\(.key)\", \"version\": \"\(.value)\", \"ecosystem\": \"npm\"}"' | \
        jq -s '.' 2>/dev/null
fi
# ...
# pip组件
if [ -f requirements.txt ]; then
    echo "    // pip依赖:"
    while IFS= read -r line; do
        line=$(echo "$line" | sed 's/#.*//; s/^ *//; s/ *$//')
        [ -z "$line" ] && continue
        pkg=$(echo "$line" | sed 's/[=<>].*//')
        ver=$(echo "$line" | grep -oP '[\d.]+')
        echo "    {\"name\": \"${pkg}\", \"version\": \"${ver:-latest}\", \"ecosystem\": \"pip\"}"
    done < requirements.txt
fi
# ...
echo "  ]"
echo "}"
```

**处理**: 解析基础SBOM生成的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回基础SBOM生成的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. OSV漏洞查询

将依赖与OSV(开源漏洞数据库)进行匹配.
```bash
#!/bin/bash
# 使用OSV API查询漏洞
# ...
check_osv() {
    local pkg=$1
    local version=$2
    local ecosystem=$3  # npm 或 PyPI
# ...
    echo "检查: ${pkg}@${version} (${ecosystem})"
# ...
    RESULT=$(curl -s -X POST "https://api.osv.dev/v1/query" \
        -H "Content-Type: application/json" \
        -d "{
            \"package\": {
                \"name\": \"${pkg}\",
                \"ecosystem\": \"${ecosystem}\"
            },
            \"version\": \"${version}\"
        }")
# ...
    VULN_COUNT=$(echo "$RESULT" | jq '.vulns | length // 0')
# ...
    if [ "$VULN_COUNT" -gt 0 ]; then
        echo "  [!] 发现 ${VULN_COUNT} 个漏洞:"
        echo "$RESULT" | jq -r '.vulns[]? | "    - \(.id): \(.summary // .details[:80] // "无描述")"'
    else
        echo "  [OK] 未发现已知漏洞"
    fi
}
# ...
# 示例:检查npm包
check_osv "lodash" "4.17.20" "npm"
check_osv "axios" "0.21.0" "npm"
# ...
# 示例:检查pip包
check_osv "requests" "2.25.0" "PyPI"
```

**处理**: 解析OSV漏洞查询的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回OSV漏洞查询的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 依赖详情

```bash
#!/bin/bash
# 显示npm依赖树
if [ -f package.json ]; then
    echo "=== npm依赖树 ==="
    npm ls --depth=2 2>/dev/null || echo "请运行 npm install 后再查看依赖树"
fi
# ...
# 显示pip依赖树
    echo "=== pip依赖列表 ==="
    cat requirements.txt | grep -v '^#' | grep -v '^$' | while read -r line; do
        echo "  └── ${line}"
    done
fi
```

**处理**: 解析依赖说明的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回依赖说明的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：软件物料清单、SBOM、生成与依赖漏洞检、查工具、支持基础包扫描与、OSV、GHSA、适合个人开发者日、常使用、物料清单漏洞情报、免费版、为个人开发者提供、软件物料清单生成、与依赖漏洞检测能、核心能力、包信息查询、漏洞匹配、依赖树可视化、适用场景、依赖更新前漏洞检、项目安全自查、基础物料清单生成、差异化、免费版聚焦单项目、npm、pip、两种生态、适合个人开发者快、速上手、适用关键词、物料清单、依赖漏洞、CVE、vulnerability、dependency等.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景

### 场景一:依赖更新前漏洞检查

```bash
#!/bin/bash
# 更新依赖前全面漏洞检查
# ...
echo "========================================="
echo "依赖漏洞检查: $(basename "$(pwd)")"
echo "检查时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "========================================="
# ...
TOTAL_VULNS=0
# ...
# npm依赖检查
if [ -f package.json ]; then
    echo ""
    echo "--- npm依赖检查 ---"
    cat package.json | jq -r '.dependencies // {} | to_entries[] | "\(.key) \(.value)"' | \
    while read -r pkg version; do
        version=$(echo "$version" | tr -d '^~>=' | head -1)
        [ -z "$version" ] && version="latest"
# ...
            -H "Content-Type: application/json" \
            -d "{\"package\": {\"name\": \"${pkg}\", \"ecosystem\": \"npm\"}, \"version\": \"${version}\"}")
# ...
        COUNT=$(echo "$RESULT" | jq '.vulns | length // 0')
        if [ "$COUNT" -gt 0 ]; then
            echo "  [!] ${pkg}@${version}: ${COUNT} 个漏洞"
vulns[]? | "       - \(.id)"'
        fi
    done
fi
# ...
# pip依赖检查
    echo ""
    echo "--- pip依赖检查 ---"
    while IFS= read -r line; do
*//; s/^ *//; s/ *$//')
        [ -z "$line" ] && continue
# ...
            -H "Content-Type: application/json" \
            -d "{\"package\": {\"name\": \"${pkg}\", \"ecosystem\": \"PyPI\"}, \"version\": \"${ver:-1.0.0}\"}")
# ...
vulns | length // 0')
        if [ "$COUNT" -gt 0 ]; then
] ${pkg}@${ver}: ${COUNT} 个漏洞"
        fi
fi
# ...
echo ""
echo "检查完成"
```

### 场景二:生成项目SBOM

```bash
#!/bin/bash
# 生成项目SBOM并保存
# ...
OUTPUT_FILE="sbom-$(date +%Y%m%d).json"
PROJECT_NAME=$(basename "$(pwd)")
# ...
echo "正在生成SBOM: ${OUTPUT_FILE}"
# ...
{
    echo "{"
    echo "  \"bomFormat\": \"JSON\","
    echo "  \"project\": \"${PROJECT_NAME}\","
    echo "  \"generated\": \"$(date -u '+%Y-%m-%dT%H:%M:%SZ')\","
    echo "  \"components\": ["
# ...
    FIRST=true
    if [ -f package.json ]; then
        cat package.json | jq -r '.dependencies // {} | to_entries[] | 
            "{\"name\": \"\(.value)\", \"ecosystem\": \"npm\"}"' | \
            while read -r comp; do
                [ "$FIRST" = true ] && FIRST=false || echo ","
                echo "    $comp"
            done
    fi
# ...
    echo "  ]"
    echo "}"
} > "$OUTPUT_FILE"
# ...
echo "SBOM已生成: ${OUTPUT_FILE}"
echo "组件数量: $(jq '.components | length' "$OUTPUT_FILE")"
```

### 场景三:单个包安全评估

```bash
#!/bin/bash
# 评估单个npm包是否安全引入
# ...
PACKAGE=$1
VERSION=$2
# ...
if [ -z "$PACKAGE" ]; then
    echo "用法: $0 <package-name> [version]"
    exit 1
fi
# ...
echo "=== 包安全评估: ${PACKAGE} ==="
# ...
# 1. 查询包信息
echo ""
echo "1. 包基本信息:"
npmjs.org/${PACKAGE}" | jq "{
    name: .name,
    latest: .\"dist-tags\".latest,
    license: .versions[.\"dist-tags\".latest].license,
    deprecated: .versions[.\"dist-tags\".latest].deprecated
}"
# ...
# 2. 查询漏洞
echo ""
echo "2. 漏洞检查:"
VER="${VERSION:-latest}"
if [ "$VER" = "latest" ]; then
    VER=$(curl -s "https://registry.npmjs.org/${PACKAGE}" | jq -r '."dist-tags".latest')
fi
# ...
curl -s -X POST "https://api.osv.dev/v1/query" \
    -H "Content-Type: application/json" \
    -d "{\"package\": {\"name\": \"${PACKAGE}\", \"ecosystem\": \"npm\"}, \"version\": \"${VER}\"}" | \
    jq '.vulns | if . then "发现 \(length) 个漏洞" else "未发现已知漏洞" end'
# ...
# 3. npm审计
echo ""
echo "3. npm审计:"
npm audit --package-name="$PACKAGE" 2>/dev/null || echo "(需要安装后审计)"
```

## 不适用场景

以下场景物料清单漏洞情报免费版不适合处理：

- 数据库架构设计决策
- NoSQL选型
- 数据仓库ETL设计

## 触发条件

需要数据库操作、SQL查询、数据存储管理时使用。不适用于非本工具能力范围的需求.
## 快速开始

### 领先步:确认项目类型

```bash
# 检查项目使用的包管理器
[ -f package.json ] && echo "npm项目"
[ -f requirements.txt ] && echo "pip项目"
[ -f go.mod ] && echo "go项目(免费版暂不支持)"
```

### 第二步:运行漏洞检查

```bash
# 检查npm依赖漏洞
npm audit --audit-level=moderate 2>/dev/null
# ...
# 检查pip依赖漏洞
pip-audit -r requirements.txt 2>/dev/null
```

### 第三步:生成SBOM

```bash
# 使用npm生成
npx sbom-tool generate -p . -o sbom.json 2>/dev/null || \
    echo "使用本工具的SBOM生成脚本"
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
#
## 配置示例

### OSV API查询参数

```json
{
  "package": {
    "name": "lodash",
    "ecosystem": "npm"
  },
  "version": "4.17.20"
}
```

### 漏洞严重级别参考

| 级别 | CVSS范围 | 建议处理 |
|---:|---:|---:|
| 严重 | 9.0-10.0 | 立即更新 |
| 高危 | 7.0-8.9 | 本周更新 |
| 中危 | 4.0-6.9 | 下次迭代更新 |
| 低危 | 0.1-3.9 | 记录跟踪 |

### 支持的包生态(免费版)

| 生态系统 | 包管理器 | SBOM生成 | 漏洞查询 |
|:---:|:---:|:---:|:---:|
| npm | package.json | 支持 | 支持 |
| PyPI | requirements.txt | 支持 | 支持 |
| Go | go.mod | 不支持 | 不支持 |
| Cargo | Cargo.toml | 不支持 | 不支持 |
| Maven | pom.xml | 不支持 | 不支持 |

## 优秀实践

1. **定期检查**:至少每月执行一次依赖漏洞扫描.
2. **更新前检查**:在更新依赖版本前,先检查目标版本是否存在漏洞.
3. **锁定版本**:使用lock文件锁定依赖版本,避免意外引入漏洞版本.
4. **最小依赖**:定期审查依赖,移除不再使用的包.
```bash
# 优秀实践:安全更新流程
safe_update() {
    local pkg=$1
    echo "安全更新: ${pkg}"
# ...
    # 1. 检查当前版本漏洞
    echo "检查当前版本..."
    npm audit --package-name="$pkg"
# ...
    # 2. 查询最新安全版本
    LATEST=$(npm view "$pkg" version 2>/dev/null)
    echo "最新版本: ${LATEST}"
# ...
    # 3. 检查最新版本漏洞
    echo "检查最新版本漏洞..."
        -H "Content-Type: application/json" \
        -d "{\"package\": {\"name\": \"${pkg}\", \"ecosystem\": \"npm\"}, \"version\": \"${LATEST}\"}" | \
        jq '.vulns | if . then "有漏洞,请谨慎" else "安全,可更新" end'
}
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **网络**: 需可访问 `https://api.osv.dev`、`https://registry.npmjs.org`、`https://pypi.org`

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| curl | 命令行工具 | 必需 | 系统自带 |
| jq | JSON处理工具 | 推荐 | `apt install jq` / `brew install jq` |
| npm | 包管理器 | 按需 | nodejs.org 下载 |
| pip-audit | Python审计工具 | 按需 | `pip install pip-audit` |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 免费版使用OSV公开API,无需API Key
- npm registry和PyPI均为公开接口

### 可用性分类
- **分类**: MD+EXEC模式纯Markdown指令,核心功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行SBOM生成与依赖漏洞检查任务

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
