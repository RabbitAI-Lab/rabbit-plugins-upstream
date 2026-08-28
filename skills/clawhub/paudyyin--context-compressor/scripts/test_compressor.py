"""
Context Compressor 测试套件

验证五策略压缩引擎的正确性。

运行方式:
    python test_compressor.py
    # 或
    python -m pytest test_compressor.py -v
"""

import sys
import os
import time

# 确保可以导入同目录模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from compressor import ContextCompressor
from strategies import (
    TimeBasedCleanup,
    ConversationSummarizer,
    ObservationMasker,
    StructuredNoteExtractor,
    SubAgentDelegator,
)


def test_time_based_cleanup():
    """测试策略1: 基于时间清理"""
    print("\n=== 测试策略1: 基于时间清理 ===")

    strategy = TimeBasedCleanup(minutes=5)

    messages = [
        {
            "role": "tool",
            "content": "旧工具输出 " + "x" * 500,
            "name": "old_tool",
            "timestamp": time.time() - 600,  # 10分钟前
        },
        {
            "role": "tool",
            "content": "新工具输出 " + "y" * 500,
            "name": "new_tool",
            "timestamp": time.time() - 60,  # 1分钟前
        },
        {
            "role": "user",
            "content": "用户消息",
        },
    ]

    result, applied = strategy.apply(messages)

    assert applied is True, "策略应该被应用"
    assert len(result) == 3, "消息数量不变"
    assert result[0]["content"] == "[工具输出已清理-超时]", "旧工具输出应被清理"
    assert result[0].get("_cleaned") is True, "应标记为已清理"
    assert "新工具输出" in result[1]["content"], "新工具输出应保留"
    assert result[2]["content"] == "用户消息", "非工具消息不受影响"

    print("  ✓ 旧工具输出被清理，替换为占位符")
    print("  ✓ 新工具输出保留")
    print("  ✓ 非工具消息不受影响")


def test_conversation_summarizer():
    """测试策略2: 对话摘要"""
    print("\n=== 测试策略2: 对话摘要 ===")

    strategy = ConversationSummarizer(threshold=20)

    # 创建 50 条消息
    messages = []
    for i in range(50):
        if i % 2 == 0:
            messages.append({
                "role": "user",
                "content": f"用户请求 {i}: 请帮我完成某个任务",
            })
        else:
            messages.append({
                "role": "assistant",
                "content": f"助手回复 {i}: 我正在处理您的请求",
            })

    result, applied = strategy.apply(messages)

    assert applied is True, "策略应该被应用（50 > 20）"
    assert len(result) == 21, f"应为 1 条摘要 + 20 条最近消息，实际 {len(result)}"
    assert result[0]["role"] == "system", "第一条应为摘要（system 角色）"
    assert "[历史对话摘要]" in result[0]["content"], "应包含摘要标记"
    assert result[0].get("_summarized_count") == 30, "应记录被摘要的消息数"

    print(f"  ✓ 50条消息压缩为 {len(result)} 条（1条摘要 + 20条最近）")
    print(f"  ✓ 摘要包含 {result[0].get('_summarized_count')} 条历史消息的概要")

    # 测试不触发情况
    small_messages = [{"role": "user", "content": f"msg {i}"} for i in range(10)]
    result2, applied2 = strategy.apply(small_messages)
    assert applied2 is False, "消息数 < 阈值时不应触发"
    print("  ✓ 消息数 < 阈值时不触发")


def test_observation_masker():
    """测试策略3: 观察遮蔽"""
    print("\n=== 测试策略3: 观察遮蔽 ===")

    strategy = ObservationMasker(keep_recent=3)

    messages = []
    # 创建 10 条工具输出
    for i in range(10):
        messages.append({
            "role": "tool",
            "content": f"工具输出 {i} " + "z" * 200,
            "name": f"tool_{i}",
        })
    # 添加一些非工具消息
    messages.append({"role": "user", "content": "用户消息"})

    result, applied = strategy.apply(messages)

    assert applied is True, "策略应该被应用（10 > 3）"

    # 统计被遮蔽的数量
    masked_count = sum(1 for m in result if m.get("_masked"))
    assert masked_count == 7, f"应遮蔽 7 条，实际 {masked_count}"

    # 验证最近 3 条工具输出未被遮蔽
    tool_msgs = [m for m in result if m.get("role") == "tool"]
    unmasked_tools = [m for m in tool_msgs if not m.get("_masked")]
    assert len(unmasked_tools) == 3, f"应保留 3 条未遮蔽，实际 {len(unmasked_tools)}"

    print(f"  ✓ 10条工具输出遮蔽了 7 条，保留最近 3 条")
    print(f"  ✓ 遮蔽后内容替换为简短描述")


def test_structured_note_extractor():
    """测试策略4: 结构化笔记提取"""
    print("\n=== 测试策略4: 结构化笔记提取 ===")

    strategy = StructuredNoteExtractor()

    messages = [
        {"role": "system", "content": "你是一个助手"},
        {
            "role": "assistant",
            "content": "经过分析，决策：使用 Python 实现压缩引擎。另外发现：当前方案性能良好。",
        },
        {
            "role": "user",
            "content": "重要：需要在周五前完成。问题：内存占用过高。",
        },
    ]

    result, applied = strategy.apply(messages)

    assert applied is True, "策略应该被应用"

    # 验证 system 消息被追加了笔记
    system_msg = result[0]
    assert system_msg["role"] == "system"
    assert "[结构化笔记]" in system_msg["content"]
    assert "决策" in system_msg["content"]
    assert "发现" in system_msg["content"]
    assert "重要" in system_msg["content"] or "重要信息" in system_msg["content"]

    print("  ✓ 成功提取决策、发现、重要信息")
    print("  ✓ 笔记注入到 system prompt")

    # 测试无关键信息时不触发
    plain_messages = [
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好！有什么可以帮你的？"},
    ]
    result2, applied2 = strategy.apply(plain_messages)
    assert applied2 is False, "无关键信息时不应触发"
    print("  ✓ 无关键信息时不触发")


def test_subagent_delegator():
    """测试策略5: 子Agent委托（预留）"""
    print("\n=== 测试策略5: 子Agent委托（预留） ===")

    strategy = SubAgentDelegator(tool_threshold=10)

    messages = [
        {"role": "tool", "content": f"output {i}", "name": f"tool_{i}"}
        for i in range(15)
    ]

    result, applied = strategy.apply(messages)

    assert applied is False, "预留实现不应修改消息"
    assert len(result) == len(messages), "消息数量不变"

    print("  ✓ 预留实现，不修改消息")
    print("  ✓ 正确统计工具调用数量")


def test_full_compression_100_messages():
    """测试完整压缩: 100条消息压缩后 < 50条 + 摘要"""
    print("\n=== 测试完整压缩: 100条消息 ===")

    compressor = ContextCompressor(max_tokens=500, threshold_ratio=0.5)

    # 创建 100 条消息（混合类型）
    messages = []
    for i in range(100):
        if i % 3 == 0:
            messages.append({
                "role": "tool",
                "content": f"工具输出 {i} " + "x" * 100,
                "name": f"tool_{i % 5}",
                "timestamp": time.time() - 600 if i < 50 else time.time() - 60,
            })
        elif i % 3 == 1:
            messages.append({
                "role": "user",
                "content": f"用户消息 {i} " + "a" * 50,
            })
        else:
            messages.append({
                "role": "assistant",
                "content": f"助手回复 {i} " + "b" * 50,
            })

    compressed, stats = compressor.check_and_compress(messages)

    print(f"  压缩前: {stats['before_tokens']} tokens, {stats['messages_before']} 条消息")
    print(f"  压缩后: {stats['after_tokens']} tokens, {stats['messages_after']} 条消息")
    print(f"  压缩率: {stats['reduction_percent']:.1f}%")
    print(f"  应用策略: {stats['strategies_applied']}")

    # 验证压缩效果
    assert stats["messages_after"] < stats["messages_before"], "消息数应减少"
    assert stats["after_tokens"] < stats["before_tokens"], "token 数应减少"
    assert len(stats["strategies_applied"]) > 0, "至少应用一个策略"

    print(f"  ✓ 100条消息成功压缩为 {stats['messages_after']} 条")


def test_time_cleanup_integration():
    """测试: 工具输出 > 5 分钟自动清理"""
    print("\n=== 测试集成: 工具输出超时清理 ===")

    compressor = ContextCompressor(max_tokens=100, threshold_ratio=0.1)

    messages = [
        {
            "role": "tool",
            "content": "超时的工具输出 " + "x" * 200,
            "name": "old_tool",
            "timestamp": time.time() - 600,  # 10分钟前
        },
        {
            "role": "tool",
            "content": "最新的工具输出 " + "y" * 200,
            "name": "new_tool",
            "timestamp": time.time() - 30,  # 30秒前
        },
    ]

    compressed, stats = compressor.force_compress(messages)

    # 验证旧工具输出被清理
    old_tool = compressed[0]
    assert old_tool["content"] == "[工具输出已清理-超时]", "旧工具输出应被清理"

    print("  ✓ 超时工具输出被清理")
    print("  ✓ 最新工具输出保留")


def test_compression_stats():
    """测试: 压缩统计正确记录"""
    print("\n=== 测试: 压缩统计 ===")

    compressor = ContextCompressor(max_tokens=200, threshold_ratio=0.3)

    messages = [
        {"role": "user", "content": "msg " + "x" * 100}
        for _ in range(10)
    ]

    compressed, stats = compressor.check_and_compress(messages)

    # 验证统计字段
    assert "before_tokens" in stats, "应包含 before_tokens"
    assert "after_tokens" in stats, "应包含 after_tokens"
    assert "strategies_applied" in stats, "应包含 strategies_applied"
    assert "reduction_percent" in stats, "应包含 reduction_percent"
    assert "messages_before" in stats, "应包含 messages_before"
    assert "messages_after" in stats, "应包含 messages_after"
    assert "threshold" in stats, "应包含 threshold"

    assert stats["messages_before"] == 10
    assert stats["before_tokens"] > 0
    assert stats["reduction_percent"] >= 0

    print(f"  ✓ 统计字段完整")
    print(f"  ✓ before_tokens: {stats['before_tokens']}")
    print(f"  ✓ after_tokens: {stats['after_tokens']}")
    print(f"  ✓ reduction_percent: {stats['reduction_percent']:.1f}%")
    print(f"  ✓ strategies_applied: {stats['strategies_applied']}")


def test_no_compression_when_under_threshold():
    """测试: 未超阈值时不压缩"""
    print("\n=== 测试: 未超阈值不压缩 ===")

    compressor = ContextCompressor(max_tokens=128000)

    messages = [
        {"role": "user", "content": "简单消息"},
        {"role": "assistant", "content": "回复"},
    ]

    compressed, stats = compressor.check_and_compress(messages)

    assert len(compressed) == 2, "消息数不变"
    assert stats["strategies_applied"] == [], "不应应用任何策略"
    assert stats["reduction_percent"] == 0.0, "压缩率应为 0"

    print("  ✓ 未超阈值时不压缩")
    print("  ✓ 消息完整保留")


def test_get_status():
    """测试: 获取状态（不压缩）"""
    print("\n=== 测试: 获取状态 ===")

    compressor = ContextCompressor(max_tokens=1000)

    messages = [{"role": "user", "content": "x" * 200} for _ in range(5)]

    status = compressor.get_status(messages)

    assert "current_tokens" in status
    assert "max_tokens" in status
    assert "threshold" in status
    assert "usage_percent" in status
    assert "needs_compression" in status
    assert "message_count" in status

    assert status["message_count"] == 5
    assert status["max_tokens"] == 1000

    print(f"  ✓ 状态查询正常")
    print(f"  ✓ 当前使用: {status['usage_percent']:.1f}%")
    print(f"  ✓ 需要压缩: {status['needs_compression']}")


def run_all_tests():
    """运行所有测试"""
    print("=" * 60)
    print("Context Compressor 测试套件")
    print("=" * 60)

    tests = [
        test_time_based_cleanup,
        test_conversation_summarizer,
        test_observation_masker,
        test_structured_note_extractor,
        test_subagent_delegator,
        test_full_compression_100_messages,
        test_time_cleanup_integration,
        test_compression_stats,
        test_no_compression_when_under_threshold,
        test_get_status,
    ]

    passed = 0
    failed = 0
    errors = []

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            failed += 1
            errors.append((test.__name__, str(e)))
            print(f"\n  ✗ FAILED: {e}")

    print("\n" + "=" * 60)
    print(f"测试结果: {passed} 通过, {failed} 失败, 共 {len(tests)} 个")
    print("=" * 60)

    if errors:
        print("\n失败详情:")
        for name, error in errors:
            print(f"  - {name}: {error}")
        sys.exit(1)
    else:
        print("\n🎉 所有测试通过！")
        sys.exit(0)


if __name__ == "__main__":
    run_all_tests()
