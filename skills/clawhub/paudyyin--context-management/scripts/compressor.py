"""
Context Compressor - 五策略上下文压缩引擎

在长任务中智能压缩上下文，减少 token 消耗 40-60%。

Usage:
    from compressor import ContextCompressor
    
    compressor = ContextCompressor(max_tokens=128000)
    messages, stats = compressor.check_and_compress(messages)
"""

import sys
import os

# 确保可以导入同目录的 strategies
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from strategies import (
    TimeBasedCleanup,
    ConversationSummarizer,
    ObservationMasker,
    StructuredNoteExtractor,
    SubAgentDelegator,
)


class ContextCompressor:
    """
    五策略上下文压缩引擎。
    
    当 token 使用超过阈值（默认 80%）时，按顺序应用五个策略：
    1. 基于时间清理 - 清理超时的工具输出
    2. 对话摘要 - 压缩旧对话
    3. 观察遮蔽 - 遮蔽旧工具输出详情
    4. 结构化笔记 - 提取关键信息
    5. 子Agent委托 - 预留
    
    Args:
        max_tokens: 最大 token 数，默认 128000
        threshold_ratio: 触发压缩的阈值比例，默认 0.8
        time_cleanup_minutes: 时间清理的超时分钟数，默认 5
        summary_threshold: 对话摘要的消息数阈值，默认 20
        observation_keep: 观察遮蔽保留的最近工具输出数，默认 10
        tool_threshold: 子Agent委托的工具数阈值，默认 10
    """

    def __init__(
        self,
        max_tokens=128000,
        threshold_ratio=0.8,
        time_cleanup_minutes=5,
        summary_threshold=20,
        observation_keep=10,
        tool_threshold=10,
    ):
        self.max_tokens = max_tokens
        self.threshold_ratio = threshold_ratio

        self.strategies = [
            TimeBasedCleanup(minutes=time_cleanup_minutes),
            ConversationSummarizer(threshold=summary_threshold),
            ObservationMasker(keep_recent=observation_keep),
            StructuredNoteExtractor(),
            SubAgentDelegator(tool_threshold=tool_threshold),
        ]

    def check_and_compress(self, messages: list) -> tuple:
        """
        检查并触发压缩。
        
        Args:
            messages: 消息列表（OpenAI 格式）
            
        Returns:
            (压缩后消息列表, 压缩统计 dict)
            
        统计 dict 包含:
            - before_tokens: 压缩前 token 数
            - after_tokens: 压缩后 token 数
            - strategies_applied: 应用的策略名称列表
            - reduction_percent: 压缩率百分比
            - messages_before: 压缩前消息数
            - messages_after: 压缩后消息数
        """
        current_tokens = self.estimate_tokens(messages)
        threshold = int(self.max_tokens * self.threshold_ratio)

        stats = {
            "before_tokens": current_tokens,
            "after_tokens": current_tokens,
            "strategies_applied": [],
            "reduction_percent": 0.0,
            "messages_before": len(messages),
            "messages_after": len(messages),
            "threshold": threshold,
        }

        if current_tokens > threshold:
            for strategy in self.strategies:
                messages, applied = strategy.apply(messages)
                if applied:
                    stats["strategies_applied"].append(strategy.name)

        stats["after_tokens"] = self.estimate_tokens(messages)
        stats["messages_after"] = len(messages)

        if stats["before_tokens"] > 0:
            stats["reduction_percent"] = (
                1 - stats["after_tokens"] / stats["before_tokens"]
            ) * 100

        return messages, stats

    def estimate_tokens(self, messages: list) -> int:
        """
        估算 token 数。
        
        使用简单启发式：4 字符 ≈ 1 token。
        这是一个粗略估计，实际 token 数取决于分词器。
        
        Args:
            messages: 消息列表
            
        Returns:
            估算的 token 数
        """
        total_chars = sum(len(msg.get("content", "")) for msg in messages)
        return total_chars // 4

    def force_compress(self, messages: list) -> tuple:
        """
        强制执行压缩（忽略阈值检查）。
        
        用于需要主动压缩的场景。
        
        Returns:
            (压缩后消息列表, 压缩统计 dict)
        """
        stats = {
            "before_tokens": self.estimate_tokens(messages),
            "after_tokens": 0,
            "strategies_applied": [],
            "reduction_percent": 0.0,
            "messages_before": len(messages),
            "messages_after": len(messages),
            "threshold": 0,
            "forced": True,
        }

        for strategy in self.strategies:
            messages, applied = strategy.apply(messages)
            if applied:
                stats["strategies_applied"].append(strategy.name)

        stats["after_tokens"] = self.estimate_tokens(messages)
        stats["messages_after"] = len(messages)

        if stats["before_tokens"] > 0:
            stats["reduction_percent"] = (
                1 - stats["after_tokens"] / stats["before_tokens"]
            ) * 100

        return messages, stats

    def get_status(self, messages: list) -> dict:
        """
        获取当前上下文状态（不执行压缩）。
        
        Returns:
            状态 dict，包含 token 估算、阈值、建议等
        """
        current_tokens = self.estimate_tokens(messages)
        threshold = int(self.max_tokens * self.threshold_ratio)

        return {
            "current_tokens": current_tokens,
            "max_tokens": self.max_tokens,
            "threshold": threshold,
            "usage_percent": (current_tokens / self.max_tokens * 100) if self.max_tokens > 0 else 0,
            "needs_compression": current_tokens > threshold,
            "message_count": len(messages),
        }


if __name__ == "__main__":
    # 演示用法
    import time

    # 创建测试消息
    test_messages = []

    # 添加一些旧的工具输出（超过5分钟）
    for i in range(30):
        test_messages.append({
            "role": "tool",
            "content": f"工具输出内容 {i} " + "x" * 200,
            "name": f"tool_{i % 5}",
            "timestamp": time.time() - 600,  # 10分钟前
        })

    # 添加最近的消息
    for i in range(20):
        test_messages.append({
            "role": "user" if i % 2 == 0 else "assistant",
            "content": f"最近的消息 {i} " + "y" * 100,
        })

    # 运行压缩
    compressor = ContextCompressor(max_tokens=1000)  # 低阈值以便触发
    compressed, stats = compressor.check_and_compress(test_messages)

    print(f"压缩前: {stats['before_tokens']} tokens, {stats['messages_before']} 条消息")
    print(f"压缩后: {stats['after_tokens']} tokens, {stats['messages_after']} 条消息")
    print(f"压缩率: {stats['reduction_percent']:.1f}%")
    print(f"应用策略: {stats['strategies_applied']}")
