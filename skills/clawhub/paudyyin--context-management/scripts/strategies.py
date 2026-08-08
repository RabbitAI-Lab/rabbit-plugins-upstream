"""
五策略上下文压缩实现

策略1: TimeBasedCleanup - 基于时间清理旧工具输出
策略2: ConversationSummarizer - 对话摘要
策略3: ObservationMasker - 观察遮蔽
策略4: StructuredNoteExtractor - 结构化笔记提取
策略5: SubAgentDelegator - 子Agent委托（预留）
"""

import time
import re
from typing import Tuple


class Strategy:
    """策略基类"""
    name = "base"

    def apply(self, messages: list) -> Tuple[list, bool]:
        """
        应用策略到消息列表。
        
        Args:
            messages: 消息列表，每条消息为 dict
            
        Returns:
            (处理后的消息列表, 是否实际应用了策略)
        """
        raise NotImplementedError


class TimeBasedCleanup(Strategy):
    """
    策略1: 基于时间清理
    
    删除超过指定时间的工具输出，保留消息结构。
    替换内容为 "[工具输出已清理-超时]"。
    
    需要消息包含 timestamp 字段（Unix 时间戳）。
    如果没有 timestamp，跳过该消息。
    """
    name = "time_cleanup"

    def __init__(self, minutes=5):
        self.minutes = minutes

    def apply(self, messages: list) -> Tuple[list, bool]:
        cutoff = time.time() - (self.minutes * 60)
        applied = False
        result = []

        for msg in messages:
            # 只处理 tool 角色的消息，或有 tool_call_id 的消息
            is_tool_output = (
                msg.get("role") == "tool"
                or msg.get("tool_call_id") is not None
            )

            if is_tool_output and msg.get("timestamp") and msg["timestamp"] < cutoff:
                # 保留消息结构，替换内容
                cleaned_msg = msg.copy()
                cleaned_msg["content"] = "[工具输出已清理-超时]"
                cleaned_msg["_cleaned"] = True
                result.append(cleaned_msg)
                applied = True
            else:
                result.append(msg)

        return result, applied


class ConversationSummarizer(Strategy):
    """
    策略2: 对话摘要
    
    当消息数超过阈值时，对旧消息生成摘要，
    保留最近 threshold 条消息 + 摘要消息。
    
    摘要以 system 消息形式注入到消息列表开头。
    """
    name = "conversation_summary"

    def __init__(self, threshold=20):
        self.threshold = threshold

    def apply(self, messages: list) -> Tuple[list, bool]:
        if len(messages) <= self.threshold:
            return messages, False

        # 分离旧消息和最近消息
        old_messages = messages[:-self.threshold]
        recent_messages = messages[-self.threshold:]

        # 生成摘要
        summary_parts = []
        user_topics = []
        assistant_actions = []
        tool_results = []

        for msg in old_messages:
            role = msg.get("role", "unknown")
            content = msg.get("content", "")

            if not content or content == "[工具输出已清理-超时]":
                continue

            if role == "user":
                # 提取用户请求的主题（取前100字符）
                topic = content[:100].strip()
                if len(content) > 100:
                    topic += "..."
                user_topics.append(topic)
            elif role == "assistant":
                # 提取助手执行的动作
                action = content[:100].strip()
                if len(content) > 100:
                    action += "..."
                assistant_actions.append(action)
            elif role == "tool":
                # 简要记录工具结果
                tool_name = msg.get("name", "unknown_tool")
                tool_results.append(f"{tool_name}")

        # 构建摘要文本
        if user_topics:
            summary_parts.append(f"用户请求({len(user_topics)}条): " + "; ".join(user_topics[:5]))
            if len(user_topics) > 5:
                summary_parts[-1] += f" ...等{len(user_topics)}条"

        if assistant_actions:
            summary_parts.append(f"助手操作({len(assistant_actions)}条): " + "; ".join(assistant_actions[:5]))
            if len(assistant_actions) > 5:
                summary_parts[-1] += f" ...等{len(assistant_actions)}条"

        if tool_results:
            unique_tools = list(set(tool_results))
            summary_parts.append(f"使用工具({len(tool_results)}次): " + ", ".join(unique_tools[:10]))

        summary_text = "[历史对话摘要] " + " | ".join(summary_parts) if summary_parts else "[历史对话摘要] 无重要内容"

        # 构建新的消息列表
        summary_msg = {
            "role": "system",
            "content": summary_text,
            "_is_summary": True,
            "_summarized_count": len(old_messages),
        }

        # 检查是否已有摘要，如果有则合并
        result = [summary_msg] + recent_messages
        return result, True


class ObservationMasker(Strategy):
    """
    策略3: 观察遮蔽
    
    隐藏旧工具输出的详细内容，保留工具调用记录。
    模型知道执行了什么工具，但不占用 token。
    
    保留最近 keep_recent 条工具输出不被遮蔽。
    """
    name = "observation_mask"

    def __init__(self, keep_recent=10):
        self.keep_recent = keep_recent

    def apply(self, messages: list) -> Tuple[list, bool]:
        # 从后往前找工具输出，保留最近 keep_recent 条
        tool_indices = []
        for i, msg in enumerate(messages):
            if msg.get("role") == "tool" or msg.get("tool_call_id"):
                # 跳过已经被清理的
                if msg.get("content") != "[工具输出已清理-超时]":
                    tool_indices.append(i)

        if len(tool_indices) <= self.keep_recent:
            return messages, False

        # 需要遮蔽的工具输出索引（除了最近 keep_recent 条）
        indices_to_mask = set(tool_indices[:-self.keep_recent])

        if not indices_to_mask:
            return messages, False

        result = []
        applied = False

        for i, msg in enumerate(messages):
            if i in indices_to_mask:
                masked_msg = msg.copy()
                tool_name = msg.get("name", "unknown")
                original_len = len(msg.get("content", ""))
                masked_msg["content"] = f"[工具输出已遮蔽: {tool_name}, 原始{original_len}字符]"
                masked_msg["_masked"] = True
                result.append(masked_msg)
                applied = True
            else:
                result.append(msg)

        return result, applied


class StructuredNoteExtractor(Strategy):
    """
    策略4: 结构化笔记提取
    
    扫描消息中的关键信息（决策、结论、重要发现），
    提取后注入到 system prompt 中。
    
    提取后，原始消息中的对应内容会被标记但保留（不删除）。
    """
    name = "structured_notes"

    # 关键信息模式
    PATTERNS = [
        (r"(?:决策|决定|结论|确定)[：:]\s*(.+?)(?:\n|$)", "decision"),
        (r"(?:发现|结果|输出)[：:]\s*(.+?)(?:\n|$)", "finding"),
        (r"(?:重要|关键|注意)[：:]\s*(.+?)(?:\n|$)", "important"),
        (r"(?:错误|问题|bug|缺陷)[：:]\s*(.+?)(?:\n|$)", "issue"),
        (r"(?:方案|计划|策略)[：:]\s*(.+?)(?:\n|$)", "plan"),
    ]

    def apply(self, messages: list) -> Tuple[list, bool]:
        notes = []

        for msg in messages:
            content = msg.get("content", "")
            role = msg.get("role", "")

            # 只从 assistant 和 user 消息中提取
            if role not in ("assistant", "user"):
                continue

            for pattern, note_type in self.PATTERNS:
                matches = re.findall(pattern, content, re.IGNORECASE)
                for match in matches:
                    match = match.strip()
                    if match and len(match) > 5:  # 过滤太短的匹配
                        notes.append({
                            "type": note_type,
                            "content": match[:200],  # 限制长度
                            "source_role": role,
                        })

        if not notes:
            return messages, False

        # 构建结构化笔记
        notes_by_type = {}
        for note in notes:
            t = note["type"]
            if t not in notes_by_type:
                notes_by_type[t] = []
            notes_by_type[t].append(note["content"])

        type_labels = {
            "decision": "决策",
            "finding": "发现",
            "important": "重要信息",
            "issue": "问题/错误",
            "plan": "方案/计划",
        }

        notes_parts = []
        for note_type, items in notes_by_type.items():
            label = type_labels.get(note_type, note_type)
            unique_items = list(dict.fromkeys(items))[:5]  # 去重，最多5条
            notes_parts.append(f"{label}: " + "; ".join(unique_items))

        notes_text = "[结构化笔记] " + " | ".join(notes_parts)

        # 查找现有的 system 消息，追加笔记
        result = []
        notes_injected = False

        for msg in messages:
            if msg.get("role") == "system" and not notes_injected:
                # 追加到现有 system 消息
                new_msg = msg.copy()
                existing = new_msg.get("content", "")
                new_msg["content"] = existing + "\n" + notes_text
                result.append(new_msg)
                notes_injected = True
            else:
                result.append(msg)

        if not notes_injected:
            # 没有 system 消息，创建一个新的
            result.insert(0, {
                "role": "system",
                "content": notes_text,
            })

        return result, True


class SubAgentDelegator(Strategy):
    """
    策略5: 子Agent委托（预留）
    
    当工具调用数量超过阈值时，建议将复杂任务委托给子 Agent。
    当前为预留实现，不实际修改消息。
    
    未来扩展：
    - 分析工具调用模式
    - 识别可委托的子任务
    - 生成子 Agent 任务描述
    """
    name = "subagent_delegate"

    def __init__(self, tool_threshold=10):
        self.tool_threshold = tool_threshold

    def apply(self, messages: list) -> Tuple[list, bool]:
        # 统计工具调用数量
        tool_calls = sum(
            1 for msg in messages
            if msg.get("role") == "tool" or msg.get("tool_call_id")
        )

        # 预留：目前不实际修改消息
        # 未来可以在此处实现子 Agent 委托逻辑
        if tool_calls > self.tool_threshold:
            # 预留标记，不实际执行
            pass

        return messages, False
