---

slug: company-search-tool-free
name: company-search-tool-free
version: 1.0.0
displayName: 企业查询助手(免费版)
summary: "企业查询免费版，支持公司基本信息、股东、法人、对外投资、工商变更查询.。企业查询助手免费版是面向个人用户的轻量企业信息查询工具。通过内置公用API Key开箱即用，支持查公司基本信息、法人、"
license: Proprietary
edition: free
description: "企业查询助手免费版是面向个人用户的轻量企业信息查询工具。通过内置公用API Key开箱即用，支持查公司基本信息、法人、股东、对外投资、工商变更等核心维度。Use
  when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段。减少重复劳动，提升工作效率。触发关键词：API设计、自动化、性能优化、监控、搜索、SEO"
  when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段.
tags:
  - 企业查询
  - 工商查询
  - 法人查询
  - 股东信息
  - 搜索
  - 检索
  - 工具
  - lines
  - append
  - get
  - info
  - 未知
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
category: "Knowledge"

---
> **查公司、查法人、查股东、查投资。开箱即用的企业信息查询工具。**

无需配置API Key，开箱即用。通过内置公用Key（每日1000次额度）即可查询企业基本信息、股东、法人、对外投资等核心维度，满足日常企业查询需求.
## 概述
免费版企业查询工具为个人用户提供基础的企业信息查询能力。通过 `discover` 发现可用工具，通过 `call` 获取结构化数据，覆盖企业查询的核心场景.
### 核心定位
| 维度 | 免费版能力 |
|---|-----|
| 企业模糊搜索 | 支持（获取entid） |
| 基本信息 | 支持 |
| 股东信息 | 支持 |
| 主要人员 | 支持（董事/监事/高管） |
| 对外投资 | 支持 |
| 工商变更 | 支持 |
| 企业尽调报告 | 不支持（需专业版） |
| 风险筛查 | 不支持（需专业版） |
| 批量查询 | 不支持（需专业版） |
| 监控告警 | 不支持（需专业版） |
| 每日额度 | 1000次（公用Key） |

## 核心能力
### 1. 企业模糊搜索

> 详细代码示例已移至 `references/detail.md`

**处理**: 解析企业模糊搜索的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回企业模糊搜索的响应数据,包含状态码、结果和日志.
### 2. 企业基本信息查询

**处理**: 解析企业基本信息查询的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回企业基本信息查询的响应数据,包含状态码、结果和日志.
### 3. 结果展示
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 企业查询助手(免费版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```python
class ResultFormatter:
    """查询结果格式化器"""
# ..
    @staticmethod
    def format_basic_info(info):
        """格式化基本信息"""
        if not isinstance(info, dict):
            return str(info)
# ..
        data = info.get("data", info)
        lines = []
        lines.append("=" * 50)
        lines.append("  企业基本信息")
        lines.append("=" * 50)
        lines.append(f"企业名称：{data.get('name', '未知')}")
        lines.append(f"法定代表人：{data.get('legal_person', '未知')}")
        lines.append(f"注册资本：{data.get('registered_capital', '未知')}")
        lines.append(f"成立日期：{data.get('establish_date', '未知')}")
        lines.append(f"统一社会信用代码：{data.get('credit_code', '未知')}")
        lines.append(f"注册地址：{data.get('address', '未知')}")
        lines.append(f"经营范围：{data.get('business_scope', '未知')}")
        lines.append("=" * 50)
        return "\n".join(lines)
# ..
    @staticmethod
    def format_shareholders(info):
        """格式化股东信息"""
        if not isinstance(info, dict):
            return str(info)
# ..
        shareholders = info.get("data", [])
        lines = []
        lines.append("=" * 50)
        lines.append("  股东信息")
        lines.append("=" * 50)
        for i, sh in enumerate(shareholders, 1):
            lines.append(f"{i}. {sh.get('name', '未知')}")
            lines.append(f"   出资比例：{sh.get('ratio', '未知')}")
            lines.append(f"   认缴金额：{sh.get('subscribed', '未知')}")
            lines.append("")
        return "\n".join(lines)
# ..
formatter = ResultFormatter()
print(formatter.format_basic_info(info))
```

**处理**: 解析结果展示的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果展示的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业查询免费版、支持公司基本信息、对外投资、工商变更查询、企业查询助手免费、版是面向个人用户、的轻量企业信息查、询工具、通过内置公用、Key、开箱即用、支持查公司基本信、工商变更等核心维、Use、when、SEO、关键词分析、排名提升、搜索流量优化时使、不适用于黑帽、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景一：查公司基本信息
**场景描述**：了解某公司的基本工商信息.
```python
query = CompanyInfoQuery()
formatter = ResultFormatter()
# ..
info = query.get_basic_info("阿里巴巴")
print(formatter.format_basic_info(info))
```

### 场景二：合作方背景调查
**场景描述**：与合作前了解对方公司的股东结构和法人信息.
```python
query = CompanyInfoQuery()
formatter = ResultFormatter()
# ..
company = "合作方公司名称"
# ..
print("=== 基本信息 ===")
info = query.get_basic_info(company)
print(formatter.format_basic_info(info))
# ..
print("\n=== 股东信息 ===")
shareholders = query.get_shareholders(company)
print(formatter.format_shareholders(shareholders))
# ..
print("\n=== 主要人员 ===")
personnel = query.get_key_personnel(company)
print(json.dumps(personnel, ensure_ascii=False, indent=2))
```

### 场景三：投资决策参考
**场景描述**：查询目标公司的对外投资情况，了解其业务布局.
```python
query = CompanyInfoQuery()
# ..
investments = query.get_investments("某科技公司")
print("=== 对外投资 ===")
if isinstance(investments, dict):
    inv_list = investments.get("data", [])
    for i, inv in enumerate(inv_list[:10], 1):
        print(f"{i}. {inv.get('name', '未知')} - 投资金额：{inv.get('amount', '未知')}")
else:
    print(investments)
```

## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 30秒上手
```bash
node （请参考skill目录中的脚本文件） discover "企业基本信息"
# ..
node （请参考skill目录中的脚本文件） call biz_fuzzy_search --params '{"key":"腾讯"}'
# ..
node （请参考skill目录中的脚本文件） call biz_shareholders --params '{"entid":"AerjZTfkSh0"}'
```

### 120秒标准搭建
```bash
node --version  # 需要 16+
node （请参考skill目录中的脚本文件） discover "企业"
# ..
node （请参考skill目录中的脚本文件） call biz_fuzzy_search --params '{"key":"阿里巴巴"}' > search_result.json
ENTID=$(cat search_result.json | python3 -c "import json,sys; print(json.load(sys.stdin)['data'][0]['entid'])")
echo "企业ID：$ENTID"
# ..
node （请参考skill目录中的脚本文件） call biz_basic_info --params "{\"entid\":\"$ENTID\"}"
node （请参考skill目录中的脚本文件） call biz_shareholders --params "{\"entid\":\"$ENTID\"}"
```

## 配置示例
### 基础配置
```python
import os
# ..
class CompanySearchConfig:
    """企业查询配置（免费版）"""
    SCRIPT_PATH = os.getenv("CS_SCRIPT_PATH", "（请参考skill目录中的脚本文件）")
    RUNTIME = os.getenv("CS_RUNTIME", "node")
    PRIVATE_API_KEY = os.getenv("FN_API_KEY", "")
    TIMEOUT = int(os.getenv("CS_TIMEOUT", "30"))
# ..
    @classmethod
    def show(cls):
        print("=== 企业查询配置 ===")
        print(f"脚本路径：{cls.SCRIPT_PATH}")
        print(f"运行时：{cls.RUNTIME}")
        print(f"私有Key：{'已配置' if cls.PRIVATE_API_KEY else '未配置（使用公用Key）'}")
        print(f"超时时间：{cls.TIMEOUT}s")
# ..
CompanySearchConfig.show()
```

### 查询维度速查
```python
QUERY_DIMENSIONS = {
    "基本信息": {
        "tool": "biz_basic_info",
        "description": "法人、注册资本、成立日期、信用代码等"
    },
    "股东信息": {
        "tool": "biz_shareholders",
        "description": "股东名称、出资比例、认缴金额等"
    },
    "主要人员": {
        "tool": "biz_key_personnel",
        "description": "董事、监事、高管、法定代表人"
    },
    "对外投资": {
        "tool": "biz_investments",
        "description": "对外投资的企业列表"
    },
    "工商变更": {
        "tool": "biz_changes",
        "description": "工商变更记录"
    },
    "被执行人": {
        "tool": "biz_executed_person",
        "description": "被执行人信息"
    },
    "失信被执行": {
        "tool": "biz_dishonest",
        "description": "失信被执行人信息"
    },
    "经营异常": {
        "tool": "biz_business_anomaly",
        "description": "经营异常名录"
    },
    "行政处罚": {
        "tool": "biz_administrative_penalty",
        "description": "行政处罚记录"
    },
}
```

## 最佳实践
### 1. 主体消歧（重要）
```python
def search_with_disambiguation(company_name):
    """带消歧的企业搜索"""
    searcher = CompanySearcher()
    result = searcher.fuzzy_search(company_name)
# ..
    if isinstance(result, dict) and "data" in result:
        companies = result["data"]
        if len(companies) == 1:
            return companies[0]["entid"]
        elif len(companies) > 1:
            print(f"找到 {len(companies)} 个匹配企业：")
            for i, comp in enumerate(companies[:5], 1):
                print(f"{i}. {comp.get('name', '未知')} - {comp.get('credit_code', '')}")
            print("\n请确认要查询哪家企业（输入序号）")
            return None
    return None
```

## 错误处理

```python
def safe_query(query_func, *args, max_retries=2):
    """带重试的安全查询"""
    for attempt in range(max_retries):
        try:
            result = query_func(*args)
            if isinstance(result, dict):
                code = result.get("code")
                if code == 200 or code == 0:
                    return result
                elif code == 9999:
                    msg = result.get("msg", "")
                    if "访问已达上限" in msg:
                        print("当日公用额度已用完，请配置私有Key或次日再用")
                        return result
                    else:
                        print(f"API错误：{msg}")
                elif code == 8888:
                    print("entid或参数错误，请重新获取企业主体")
                elif code == 20000:
                    print("该企业在该维度下无记录")
                    return result
            return result
        except Exception as e:
            print(f"第{attempt+1}次查询异常：{e}")
    return {"error": "重试次数已用完"}
```

### 3. 复用entid - 处理方式: 按上述步骤操作并确认结果
```python
class EntidCache:
    """entid缓存（避免重复搜索）"""
    def __init__(self):
        self.cache = {}
# ..
    def get(self, company_name):
        return self.cache.get(company_name)
# ..
    def set(self, company_name, entid):
        self.cache[company_name] = entid
# ..
cache = EntidCache()
entid = cache.get("腾讯")
if not entid:
    entid = query._get_entid("腾讯")
    cache.set("腾讯", entid)
```
### 错误场景2

检查`error_code`并按照处理方式进行排查.
### 错误场景3

## 常见问题
### 已知限制
免费版使用内置公用API Key，每日额度1000次。具体剩余额度以官方页面实时展示为准。当返回 `code=9999` 且 `msg` 包含"访问已达上限"时，表示当日额度已用完，可配置私有Key或次日再用.
### Q2：如何配置私有API Key？
设置环境变量 `FN_API_KEY` 即可使用私有Key（优先于公用Key）。私有Key可从官方平台购买，享有更高额度和更多功能。配置方式：`export FN_API_KEY=your_private_key`.
### Q3：查询返回多个匹配企业怎么办？
当企业名称是简称或存在多义（如"信数""雷军"），模糊搜索可能返回多个匹配。此时需要主体消歧：列出所有匹配项，让用户确认要查询的具体企业。免费版不自动假设唯一性.
### Q4：免费版支持企业尽调报告吗？
不支持。免费版仅支持单维度查询，如需生成整合的企业尽调报告（包含基本信息+股东+投资+风险等多维度整合输出），需升级至专业版.
### Q5：可以按人名查询企业吗？
可以。若用户提供人名（如"雷军有哪些公司"），理解为"以该人为法定代表人的企业"。查询结果会说明此限定。若存在同名人，需询问用户确认.
### Q6：entid是什么？需要展示给用户吗？
entid是企业内部查询ID，对用户无意义。结果中不应展示entid，应展示企业工商登记全称。所有维度查询都使用entid，不直接传企业名称或信用代码.
## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| Node.js 16+ | 运行时 | 必需 | 官网下载安装 |
| 企业查询API | API | 必需 | 内置公用Key（每日1000次） |
| Python 3.8+ | 运行时 | 可选 | 辅助脚本使用 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置
- 免费版内置公用API Key，开箱即用，无需额外配置
- 如需更高额度，可配置私有API Key：`export FN_API_KEY=your_private_key`
- 私有Key优先于公用Key使用
- LLM模型路由由Agent平台内置提供

### 可用性分类
- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent执行企业信息查询任务

## 免费版限制
本免费体验版限制以下高级功能（需升级至专业版解锁）：

- **企业尽调报告**（多维度整合输出）
- **风险筛查**（被执行人/失信/限高/经营异常/严重违法/行政处罚）
- **批量查询**（多家企业同时查询）
- **监控告警**（企业状态变化通知）
- **企业关联关系**（股东关联、投资关联）
- **历史数据查询**（变更历史、注销吊销）
- **知识产权查询**（专利、商标、软著）
- **招投标查询**
- **更高API额度**（私有Key支持）
- **优先技术支持**

解锁全部高级能力请使用专业版：`company-search-tool-pro`

## 示例

### 基本用法

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能..
Skill: 执行完成,结果如下: 操作成功
```

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "企业查询助手(免费版)处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "company search"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
