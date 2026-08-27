---
name: context-compressor
version: 1.0.0
description: "五策略上下文压缩引擎。在长任务中智能压缩上下文，减少 token 消耗 40-60%。当上下文超过阈值时自动触发压缩。"
triggers:
  - 上下文压缩
  - context compress
  - token 超限
  - 长任务压缩
---

# Context Compressor

五策略上下文压缩引擎，在长任务中智能压缩上下文，减少 token 消耗 40-60%。

## 五策略概览

| # | 策略 | 触发条件 | 效果 |
|---|------|----------|------|
| 1 | 基于时间清理 | 工具输出 > 5 分钟 | 替换为占位符，保留结构 |
| 2 | 对话摘要 | 消息数 > 20 条 | 旧消息生成摘要，保留最近 20 条 |
| 3 | 观察遮蔽 | 旧工具输出 | 隐藏内容，保留调用记录 |
| 4 | 结构化笔记 | 含决策/结论的消息 | 提取关键信息注入 system prompt |
| 5 | 子Agent委托（预留） | 工具 > 10 个 | 复杂任务交给子 Agent |

## 使用方法

```python
import sys
sys.path.insert(0, "<skill-dir>/scripts")

from compressor import ContextCompressor

compressor = ContextCompressor(max_tokens=128000)
messages, stats = compressor.check_and_compress(messages)

print(f"压缩前: {stats['before_tokens']} tokens")
print(f"压缩后: {stats['after_tokens']} tokens")
print(f"应用策略: {stats['strategies_applied']}")
print(f"压缩率: {stats['reduction_percent']:.1f}%")
```

## 消息格式

输入消息需为标准 OpenAI 格式：

```python
{
    "role": "user" | "assistant" | "system" | "tool",
    "content": "消息内容",
    "timestamp": 1234567890,  # Unix 时间戳（可选，策略1需要）
    "tool_calls": [...],       # 工具调用记录（可选）
    "tool_call_id": "xxx",     # 工具调用 ID（可选）
    "name": "tool_name"        # 工具名称（可选）
}
```

## 集成点

- **coding-framework Step 5.2**: 当 token 使用超过 80% 时自动触发
- **长任务子代理**: 在 spawn 前压缩父会话上下文
- **定期压缩**: 每 N 轮对话后检查一次

## 阈值配置

参见 `references/thresholds.md` 获取详细阈值说明。

默认阈值：
- 最大 token: 128,000
- 触发阈值: 80% (102,400 tokens)
- 时间清理: 5 分钟
- 对话摘要: 20 条
- 观察遮蔽: 保留最近 10 条工具输出

## 测试

```bash
cd <skill-dir>
python -m pytest scripts/test_compressor.py -v
# 或
python scripts/test_compressor.py
```
