"""
core/prompt_compiler.py
PromptCompiler - 将人格定义编译为 prompt 片段
V3.5.0

V3.5.0 改进：
- 兼容归一化后的标准结构（meta/identity/behavior/phrases）
- overlay 片段头部带上版本号，便于追踪
- 若人格定义了 limitations，追加"能力边界"提示，避免用户过度期待
"""

from typing import Dict, Any, Optional


class PromptCompiler:
    """Prompt 编译器 - 将人格定义转换为各平台可用的 prompt 文本"""

    def compile_overlay(self, persona_def: Dict[str, Any]) -> str:
        """
        编译叠加模式（Stack）人格片段
        保留 V1.0 的 INSERT_TO_SOUL.md 格式
        """
        meta = persona_def["meta"]
        identity = persona_def.get("identity", {})
        behavior = persona_def.get("behavior", {})
        phrases = persona_def.get("phrases", {})

        lines = []
        lines.append("## 【心灵补手】谄媚模块 v3.5.0")
        lines.append(f"**人格**: {meta.get('name', meta.get('id', '未知'))}")
        lines.append("")
        lines.append("### 身份")

        # 身份声明
        identity_stmts = identity.get("identity_statements", {})
        greeting = identity_stmts.get("greeting") or identity_stmts.get("开场")
        if greeting:
            lines.append(greeting)
        elif identity.get("role"):
            lines.append(f"角色：{identity.get('role')}")

        # 人称
        pronouns = identity.get("pronouns", {})
        first_p = pronouns.get("first_person", "在下")
        second_p = pronouns.get("second_person", "先生")
        lines.append(f"第一人称：{first_p}")
        lines.append(f"第二人称：{second_p}")

        lines.append("")
        lines.append("### 当前配置")
        lines.append(f"- 程度：{behavior.get('level', 5)}/10")
        lines.append(f"- 语气：{behavior.get('tone', '自然')}")
        lines.append(f"- 模式：{behavior.get('mode', 'normal')}")

        lines.append("")
        lines.append("### 触发时机")
        trigger_keywords = behavior.get("activation", {}).get("trigger_keywords", [])
        if trigger_keywords:
            lines.append(f"检测到以下关键词时触发：{', '.join(trigger_keywords)}")
        else:
            lines.append("检测到情绪时机时自动触发")

        lines.append("")
        lines.append("### 话术规则")

        # 程度对应话术示例
        level = behavior.get("level", 5)
        if level <= 3:
            lines.append("程度1-3：委婉暗示，简短1句")
        elif level <= 6:
            lines.append("程度4-6：正常赞美，1-2句话")
        elif level <= 9:
            lines.append("程度7-9：强烈吹捧，2-3句话")
        else:
            lines.append("程度10：无脑崇拜，3+句话 [Debug Mode]")

        # 种子话术
        seeds = phrases.get("seeds", {})
        if seeds:
            lines.append("")
            lines.append("### 话术种子（智能扩展）")
            for scenario, tiers in seeds.items():
                if not isinstance(tiers, dict):
                    continue
                lines.append(f"**{scenario}**:")
                for tier, phrases_list in tiers.items():
                    if not isinstance(phrases_list, list):
                        continue
                    for p in phrases_list[:2]:
                        if isinstance(p, str):
                            lines.append(f"- {p}")

        # 能力边界提示（V3.5.0）
        limitations = persona_def.get("limitations") or meta.get("limitations") or []
        if limitations:
            lines.append("")
            lines.append("### 能力边界（重要）")
            lines.append("以下场景本人格不适用或会明显失效，请勿强行使用：")
            for lim in limitations:
                lines.append(f"- {lim}")

        return "\n".join(lines)

    def compile_inherit(
        self,
        base_prompt: str,
        persona_def: Dict[str, Any]
    ) -> str:
        """
        编译继承模式（Inherit）人格片段
        在 base prompt 基础上追加人格覆盖
        """
        overlay = self.compile_overlay(persona_def)

        return f"""{base_prompt}

{'='*60}
【人格覆盖层 - 继承自 base prompt】
{'='*60}
{overlay}
"""

    def compile_independent(self, persona_def: Dict[str, Any]) -> str:
        """
        编译独立模式（Independent）人格片段
        完整的人格定义，不依赖 base
        """
        meta = persona_def["meta"]
        identity = persona_def.get("identity", {})
        behavior = persona_def.get("behavior", {})
        phrases = persona_def.get("phrases", {})

        lines = []
        lines.append(f"# {meta.get('name', meta.get('id', '未知'))} 人格")
        lines.append("")
        lines.append(f"**版本**: {meta.get('version', '3.5.0')}")
        lines.append(f"**角色**: {identity.get('role', 'AI助手')}")
        lines.append("")

        # 身份声明
        identity_stmts = identity.get("identity_statements", {})
        for key, value in identity_stmts.items():
            if isinstance(value, str):
                lines.append(f"**{key}**: {value}")

        lines.append("")
        lines.append("## 行为规则")
        lines.append(f"**语气**: {behavior.get('tone', '专业')}")
        lines.append(f"**程度**: {behavior.get('level', 5)}/10")

        # 话术种子
        seeds = phrases.get("seeds", {})
        if seeds:
            lines.append("")
            lines.append("## 话术库")
            for scenario, tiers in seeds.items():
                if not isinstance(tiers, dict):
                    continue
                lines.append(f"### {scenario}")
                for tier, phrases_list in tiers.items():
                    if not isinstance(phrases_list, list):
                        continue
                    lines.append(f"**{tier}**:")
                    for p in phrases_list[:3]:
                        if isinstance(p, str):
                            lines.append(f"- {p}")

        # 能力边界（V3.5.0）
        limitations = persona_def.get("limitations") or meta.get("limitations") or []
        if limitations:
            lines.append("")
            lines.append("## 能力边界")
            for lim in limitations:
                lines.append(f"- {lim}")

        return "\n".join(lines)
