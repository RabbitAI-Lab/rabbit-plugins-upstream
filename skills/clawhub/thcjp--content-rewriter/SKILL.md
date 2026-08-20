---
name: content-rewriter
description: "LLM内容改写器(v25.0合并content-dedup)，语义改写+SimHash去重检测，支持8平台风格适配+24h滑窗跨平台内容去重。同平台汉明距离≤3拦截，跨平台≤5告警。触发:内容改写/跨平台差异化/同质化处理/内容发布前去重检查/跨平台分发前检测/内容同质化防控"
version: 2.0.0
author: JueJin
tools: [read, exec]
dependencies: [content-publisher]
metadata:
  requires:
    config: []
    bins: ["python"]
    env: []
    os: ["win32", "linux", "darwin"]
  category: anti-ban
  priority: P1
  def_records: [DEF-76]
  source_doc: docs/design/34_防封防降权升级方案_v1.1.md
---

<!-- v25.0合并说明: content-dedup已合并到content-rewriter(来源:R75.5 Skill去重)。dedup的SimHash检测功能作为"detect"动作保留，原content-dedup目录已删除。 -->

# LLM内容改写器（含SimHash去重检测）

## 使用场景

解决跨平台内容同质化风险。相同内容直接多平台发布会被平台检测为搬运/重复内容，导致降权。本Skill提供两个action：

1. **rewrite(改写)**: 对内容进行LLM/本地语义改写，保持核心信息不变但改变表达方式
2. **detect(检测)**: SimHash指纹去重检测，发布前检查内容是否与24h内历史内容重复

### 防控场景
- 内容发布前同平台24h去重检查(detect)
- 多平台分发前跨平台相似度检测(detect)
- 跨平台内容同质化改写(rewrite)
- 防止触发小红书"同质笔记>3次标记搬运"规则

## 工作流

### action=rewrite (内容改写)

1. 接收原始内容和目标平台
   - 输入: content(原始内容) + platform(目标平台) + use_llm(可选)
   - 验证: 内容非空,平台在支持列表内
2. 选择改写模式
   - LLM模式: 调用9Router进行语义改写(高质量,~500-1000 tokens/次)
   - 本地模式: 同义替换(0 Token,适合简单内容)
3. 生成改写提示词
   - 根据平台风格配置生成提示词
   - 平台风格: 知乎(专业理性)/小红书(活泼种草)/抖音(口语化)等8种
4. 执行改写
   - LLM模式: 通过openclaw gateway调用9Router
   - 本地模式: 同义替换(推荐->分享/好用->实用等)
5. 返回改写结果
   - 输出: original + rewritten + platform + mode

### action=detect (SimHash去重检测)

1. **接收内容**: text + platform + content_id
2. **计算SimHash**: 字符bigram分词 -> MD5哈希 -> 64位加权指纹
3. **加载历史**: 读取24h内指纹记录(data/content_fingerprints/simhash_history.json)
4. **比对检测**:
   - 同平台: 汉明距离<=3 -> 拦截(block)
   - 跨平台: 汉明距离<=5 -> 告警(warning)
   - 无匹配 -> 通过(pass)
5. **保存指纹**: 写入历史记录(保留7天)
6. **返回结果**: status(pass/warning/block) + 汉明距离 + 匹配记录

### SimHash算法说明
- **分词**: 字符bigram(无需jieba依赖，兼容中英文)
- **哈希**: MD5取前8字节作为64位hash
- **指纹**: 64位加权向量二值化
- **比对**: 汉明距离(XOR后1的个数)
- **窗口**: 24小时滑动窗口

### 阈值依据(来源:34_防封防降权升级方案v1.0)

| 检测类型 | 汉明距离阈值 | 动作 | 平台规则依据 |
|:---------|:-------------|:-----|:-------------|
| 同平台重复 | <=3 | 拦截发布 | 小红书同质笔记>3次标记搬运 |
| 跨平台相似 | <=5 | 告警但放行 | 抖音像素级帧比对+暗水印 |
| 无重复 | >5 | 通过 | - |

## 输入格式

### rewrite输入

```json
{
  "action": "rewrite",
  "content": "推荐一个好用的AI工具，可以快速生成文案",
  "platform": "xiaohongshu",
  "use_llm": false
}
```

### detect输入

```json
{
  "action": "detect",
  "text": "待检测的文本内容",
  "platform": "douyin",
  "content_id": "content_001"
}
```

| 字段 | 类型 | 必填 | 说明 |
|:-----|:-----|:----:|:-----|
| action | string | 否 | rewrite(默认)/detect |
| content | string | rewrite必填 | 原始内容 |
| text | string | detect必填 | 待检测文本(>=2字符) |
| platform | string | 是 | 目标平台 |
| use_llm | bool | 否 | 是否用LLM改写(默认false) |
| content_id | string | 否 | 内容ID(detect用，默认时间戳) |

## 输出格式

### rewrite输出

```json
{
  "success": true,
  "data": {
    "original": "推荐一个好用的AI工具...",
    "rewritten": "安利一个实用的AI工具...",
    "platform": "xiaohongshu",
    "mode": "local"
  },
  "error": null,
  "code": "REWRITE_OK"
}
```

### detect输出

```json
{
  "success": true,
  "data": {
    "status": "pass",
    "code": "DEDUP_PASS",
    "message": "无重复",
    "fingerprint": 1234567890,
    "min_same_platform_distance": null,
    "min_cross_platform_distance": null,
    "threshold_block": 3,
    "threshold_warning": 5,
    "window_hours": 24
  },
  "error": null,
  "code": null
}
```

| 字段(detect) | 类型 | 说明 |
|:-----|:-----|:-----|
| status | string | pass/warning/block |
| code | string | DEDUP_PASS/DEDUP_WARN_CROSS/DEDUP_BLOCK_SAME |
| fingerprint | int | 64位SimHash指纹 |
| min_same_platform_distance | int\|null | 同平台最小汉明距离 |
| min_cross_platform_distance | int\|null | 跨平台最小汉明距离 |

## 平台风格配置(rewrite)

| 平台 | 风格 | 语气 | 长度 |
|:-----|:-----|:-----|:-----|
| zhihu | 专业理性 | 客观分析 | 中长文 |
| xiaohongshu | 活泼种草 | 亲切分享 | 短文+emoji |
| douyin | 口语化 | 直接有力 | 短文案 |
| weibo | 简洁观点 | 犀利 | 短文 |
| juejin | 技术深度 | 专业分享 | 中长文 |
| csdn | 技术教程 | 详细讲解 | 长文 |
| bilibili | 趣味科普 | 轻松 | 中短文 |
| xianyu | 商品卖点 | 吸引购买 | 短文案 |

## 异常处理

| 错误码 | 场景 | 处理 |
|:-------|:-----|:-----|
| REWRITE_VAL_ERR | 内容为空/平台未知 | 返回JSON+exit(1) |
| REWRITE_FALLBACK | LLM调用失败 | 降级本地同义替换 |
| REWRITE_ERR | 其他异常 | 返回JSON+exit(2) |
| DEDUP_VAL_ERR | text为空(detect) | 返回JSON+exit(1) |
| DEDUP_ERR | 内部异常(detect) | 返回JSON+exit(2) |
| DEDUP_BLOCK_SAME | 同平台重复(detect) | 拦截发布，建议改写 |
| DEDUP_WARN_CROSS | 跨平台相似(detect) | 告警但放行，建议差异化 |

## 集成点

### content-publisher步骤3.4.5+3.4.6

发布前先调用detect动作执行SimHash去重检测，对warning/block内容调用rewrite动作改写后再重新检测。

```
步骤3.4.5 内容去重检查:
  - 调用 content-rewriter scripts/simhash_dedup.py (action=detect)
  - status=block -> 拦截发布，返回CP-ERR-08
  - status=warning -> 记录日志，继续发布
  - status=pass -> 继续发布流程

步骤3.4.6 内容改写差异化:
  - 调用 scripts/content_rewriter.py (action=rewrite)
  - 改写后重新执行3.4.5去重检查
```

### 与content-orchestrator集成

content-orchestrator已有的4维度差异化检查是语义层检查，本Skill的detect动作是指纹层检查，两者互补不冲突(R31合规:不降级现有优化)。

## 示例

```bash
# detect模式 - SimHash去重检测
echo '{"text":"AI代写文案服务介绍","platform":"douyin","content_id":"test-001"}' | python scripts/simhash_dedup.py

# rewrite模式 - 本地改写
echo '{"content":"推荐好用的AI工具","platform":"xiaohongshu"}' | python scripts/content_rewriter.py

# rewrite模式 - LLM改写
echo '{"content":"推荐好用的AI工具","platform":"zhihu","use_llm":true}' | python scripts/content_rewriter.py
```

## 历史版本

| 版本 | 日期 | 变更 |
|:-----|:-----|:-----|
| v2.0.0 | 2026-07-22 | v25.0合并content-dedup: 新增detect动作(SimHash去重检测+24h滑窗+同平台<=3拦截/跨平台<=5告警)，原content-dedup目录已删除(R75.5 Skill去重) |
| v1.0.0 | 2026-06-17 | 初始版本: 8平台风格适配+LLM/本地双模式+降级机制 |
