"""
core/persona_engine.py
PersonaEngine - 子代理人格赋予核心引擎
V3.5.0 核心模块

V3.5.0 改进（基于 SkillHub 评测低分项）：
1. 结构归一化器 normalize_persona_def()：自动把非标准 JSON（顶层 name/identity/tone/sample_lines_by_level）
   归一化为标准 meta/identity/behavior/phrases 结构，彻底解决"人格切换不稳定/突然用不了"的 KeyError 崩溃。
2. 友好错误处理：找不到人格 / 格式错误时输出人性化中文提示 + 修复建议，而非裸 KeyError 堆栈。
3. 能力边界：优先读取人格定义的 limitations 字段用于提示。
"""

from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from dataclasses import asdict
from datetime import datetime

from schemas.launch_config import (
    CompiledPersona,
    RelationshipMode,
    Platform,
    LaunchConfig
)
from .persona_registry import PersonaRegistry
from .session_store import SessionStore
from .prompt_compiler import PromptCompiler


class PersonaLoadError(Exception):
    """人格加载失败 - 带修复建议的人性化错误"""

    def __init__(self, message: str, hint: str = ""):
        super().__init__(message)
        self.message = message
        self.hint = hint

    def friendly(self) -> str:
        """返回面向用户的中文人性化提示"""
        text = f"😔 人格加载失败：{self.message}"
        if self.hint:
            text += f"\n💡 修复建议：{self.hint}"
        return text


def normalize_persona_def(raw: Dict[str, Any], persona_id: str = "") -> Dict[str, Any]:
    """
    结构归一化器 - 核心修复 (V3.5.0)

    问题背景：
    历史版本的 6 个人格定义中，只有 scholar.json 使用标准结构
    (meta/identity/behavior/phrases)，其余 5 个 (taijian/xiaoyahuan/
    siji/zaomiao/liubowen) 均使用松散的非标准结构（顶层 name/identity/
    tone/pronouns/trigger_keywords/sample_lines_by_level/禁忌_words）。
    引擎硬编码访问 raw["meta"]["id"] / raw["behavior"] 会导致 KeyError，
    这就是"人格切换不稳定、突然用不了"的根因。

    本函数自动识别两种结构：
    - 已标准化结构 → 原样返回
    - 松散结构     → 归一化为标准结构，且保留全部原始字段到 meta.raw

    Args:
        raw: 原始人格定义（任意结构）
        persona_id: 可选，缺省时从 meta.id 或 name 推断

    Returns:
        标准结构的人格定义字典
    """
    # 情况一：已是标准结构
    if isinstance(raw, dict) and "meta" in raw and "behavior" in raw:
        return raw

    # 情况二：松散结构 → 归一化
    if not isinstance(raw, dict):
        raise PersonaLoadError(
            f"人格定义不是 JSON 对象（实际类型 {type(raw).__name__}）",
            "请检查 personas/*.json 文件是否为合法的 JSON 对象"
        )

    pid = persona_id or raw.get("id") or raw.get("name") or "unknown"
    name = raw.get("display_name") or raw.get("name") or pid

    # 人称
    pronouns_raw = raw.get("pronouns", {})
    pronouns = {}
    if isinstance(pronouns_raw, dict):
        if "male_user" in pronouns_raw and isinstance(pronouns_raw["male_user"], dict):
            pronouns["first_person"] = pronouns_raw["male_user"].get("first_person", "老朽")
            pronouns["second_person"] = pronouns_raw["male_user"].get("second_person", "主公")
        elif "first_person" in pronouns_raw:
            pronouns["first_person"] = pronouns_raw.get("first_person", "在下")
            pronouns["second_person"] = pronouns_raw.get("second_person", "先生")

    # identity_statements（两种可能：顶层，或在 pronouns 内）
    id_stmts = raw.get("identity_statements") or {}
    if isinstance(id_stmts, dict) and "开场" in id_stmts:
        greeting = id_stmts.get("开场", "")
    else:
        greeting = raw.get("greeting", "")

    # 触发关键词
    trigger_keywords = raw.get("trigger_keywords") or []

    # 话术种子：把 sample_lines_by_level 转成 phrases.seeds 风格
    sample_lines = raw.get("sample_lines_by_level") or {}
    seeds = {}
    if isinstance(sample_lines, dict):
        def _tier_key(t):
            t = str(t)
            return "10" if t.startswith("10") else ("7-9" if t.startswith(("7", "8", "9")) else ("4-6" if t.startswith(("4", "5", "6")) else "1-3"))
        buckets: Dict[str, list] = {}
        for tier, lines in sample_lines.items():
            if isinstance(lines, list):
                buckets.setdefault(_tier_key(tier), []).extend([l for l in lines if isinstance(l, str)])
        if buckets:
            seeds = {"flattery": {k: v for k, v in buckets.items()}}

    # flattery_templates → phrases.seeds.general_praise
    flattery = raw.get("flattery_templates") or {}
    if isinstance(flattery, dict):
        praise_list = []
        for v in flattery.values():
            if isinstance(v, str):
                praise_list.append(v)
        if praise_list:
            seeds.setdefault("general_praise", {})["4-6"] = praise_list

    # 能力边界：优先取 limitations，无则置空（由 SKILL.md / FAQ 补充）
    limitations = raw.get("limitations") or []

    # emoji
    emoji = raw.get("emoji") or "💖"

    normalized = {
        "meta": {
            "id": pid,
            "name": name,
            "version": raw.get("version") or "3.5.0",
            "author": raw.get("author") or "ace",
            "description": raw.get("identity") or raw.get("description") or f"{name}人格",
            "tags": raw.get("tags") or ["flattering"],
            "compatible_with": raw.get("compatible_with") or ["openclaw", "generic"],
            "limitations": limitations,
            # 保留全部原始字段，供后续扩展 / 调试
            "raw": {k: v for k, v in raw.items() if k not in ("name", "display_name")}
        },
        "identity": {
            "emoji": emoji,
            "role": raw.get("identity") or name,
            "pronouns": pronouns,
            "identity_statements": {
                "greeting": greeting,
                **({k: v for k, v in id_stmts.items() if isinstance(v, str)} if isinstance(id_stmts, dict) else {})
            }
        },
        "behavior": {
            "relationship_mode": "stack",
            "level": int(raw.get("level", 8) or 8),
            "tone": raw.get("tone") or "自然",
            "mode": raw.get("mode") or "emotion_sensitive",
            "activation": {
                "trigger_keywords": trigger_keywords,
                "always_on": False,
                "auto_activate": True,
                "emotion_sensing": bool(raw.get("emotion_sensing", True)),
                "emotion_sensing_description": raw.get("emotion_sensing_description", "")
            },
            "frequency": {
                "min_rounds_between": 0,
                "max_per_session": 99
            }
        },
        "phrases": {"seeds": seeds},
        "limitations": limitations,
        "style_description": raw.get("style_description", ""),
        "notes": raw.get("notes", "")
    }

    return normalized


class PersonaEngine:
    """
    子代理人格引擎

    核心职责：
    1. 加载人格定义
    2. 管理人格激活/停用
    3. 为不同平台编译人格 prompt
    4. 维护会话级人格栈

    V3.5.0：加载时自动归一化结构，任何格式的人格都能稳定激活。
    """

    def __init__(
        self,
        base_dir: Optional[Path] = None,
        default_platform: Platform = Platform.OPENCLAW
    ):
        if base_dir is None:
            base_dir = Path.home() / ".xinling-bushou-v2"

        self.base_dir = base_dir
        self.default_platform = default_platform

        # 初始化子模块
        self.registry = PersonaRegistry(base_dir)
        self.session_store = SessionStore(base_dir / "sessions")
        self.prompt_compiler = PromptCompiler()

        # 适配器缓存（懒加载）
        self._adapters: Dict[str, Any] = {}

    def _get_adapter(self, platform: Platform):
        """获取平台适配器（懒加载）"""
        from adapters import AdapterRegistry

        platform_id = platform.value

        if platform_id not in self._adapters:
            adapter_class = AdapterRegistry.get(platform_id)
            self._adapters[platform_id] = adapter_class()

        return self._adapters[platform_id]

    def load_persona(self, persona_id: str) -> Dict[str, Any]:
        """
        加载人格定义（自动归一化结构）

        Args:
            persona_id: 人格 ID

        Returns:
            标准结构的人格定义字典

        Raises:
            PersonaLoadError: 带修复建议的人性化错误
        """
        try:
            raw = self.registry.load_persona(persona_id)
        except FileNotFoundError as e:
            known = self.registry.list_personas()
            known_str = "、".join(known) if known else "（无）"
            raise PersonaLoadError(
                f"找不到人格 '{persona_id}'",
                f"当前已注册的人格：{known_str}。可用 `xinling list` 查看，或用 `xinling add <id> <file>` 添加。"
            ) from e
        except json.JSONDecodeError as e:
            raise PersonaLoadError(
                f"人格文件 '{persona_id}' 的 JSON 格式无效（{e}）",
                "请检查 personas/*.json 是否有语法错误（如缺少逗号、引号不匹配）。"
            ) from e

        return normalize_persona_def(raw, persona_id)

    def activate_persona(
        self,
        session_id: str,
        persona_id: str,
        relationship: RelationshipMode = RelationshipMode.STACK,
        override_config: Optional[Dict[str, Any]] = None,
        base_prompt: str = ""
    ) -> CompiledPersona:
        """
        激活人格

        核心流程：
        1. 加载人格定义（V3.5.0 自动归一化，不再崩溃）
        2. 应用 override 配置
        3. 编译人格片段
        4. 保存到会话状态

        Args:
            session_id: 会话 ID
            persona_id: 人格 ID
            relationship: 与主人格的关系
            override_config: 运行时覆盖配置（如 level=8）
            base_prompt: 主人格 prompt（用于 inherit 模式）

        Returns:
            CompiledPersona: 编译后的人格对象

        Raises:
            PersonaLoadError: 人格加载/编译失败（人性化提示）
        """
        # 1. 加载人格定义（归一化 + 错误处理）
        persona_def = self.load_persona(persona_id)

        # 2. 应用 override
        if override_config:
            persona_def = self._apply_override(persona_def, override_config)

        # 3. 编译人格片段
        try:
            if relationship == RelationshipMode.INHERIT and base_prompt:
                fragment = self.prompt_compiler.compile_inherit(
                    base_prompt=base_prompt,
                    persona_def=persona_def
                )
            elif relationship == RelationshipMode.STACK:
                fragment = self.prompt_compiler.compile_overlay(persona_def)
            else:
                fragment = self.prompt_compiler.compile_independent(persona_def)
        except (KeyError, TypeError) as e:
            raise PersonaLoadError(
                f"编译人格 '{persona_id}' 时出错（{e}）",
                "人格定义缺少必需字段，可尝试 `xinling add <id> <file>` 重新导入标准格式。"
            ) from e

        # 4. 构建 CompiledPersona
        meta = persona_def["meta"]
        behavior = persona_def["behavior"]
        compiled = CompiledPersona(
            id=meta["id"],
            name=meta["name"],
            level=behavior.get("level", 5),
            mode=behavior.get("mode", "normal"),
            fragment=fragment,
            relationship=relationship,
            source_file=self.registry.get_persona_path(persona_id),
            metadata={
                **meta,
                "limitations": persona_def.get("limitations", meta.get("limitations", []))
            }
        )

        # 5. 更新会话状态
        self.session_store.push_persona(session_id, compiled)

        return compiled

    def deactivate_persona(self, session_id: str, persona_id: str) -> bool:
        """停用人格"""
        return self.session_store.pop_persona(session_id, persona_id)

    def get_active_personas(self, session_id: str) -> List[CompiledPersona]:
        """获取当前活跃人格栈"""
        return self.session_store.get_personas(session_id)

    def compile_for_platform(
        self,
        compiled: CompiledPersona,
        platform: Optional[Platform] = None,
        base_prompt: str = ""
    ) -> str:
        """
        为指定平台编译 prompt

        Args:
            compiled: 编译后的人格
            platform: 目标平台
            base_prompt: 基础 prompt（由平台适配器追加）

        Returns:
            平台特定格式的完整 system prompt
        """
        if platform is None:
            platform = self.default_platform

        adapter = self._get_adapter(platform)

        return adapter.compile_system_prompt(
            base_prompt=base_prompt,
            persona_fragment=compiled.fragment,
            metadata=compiled.metadata
        )

    def get_launch_config(
        self,
        compiled: CompiledPersona,
        platform: Optional[Platform] = None
    ) -> LaunchConfig:
        """获取平台特定的启动配置"""
        if platform is None:
            platform = self.default_platform

        adapter = self._get_adapter(platform)
        return adapter.get_launch_config(compiled)

    def _apply_override(
        self,
        persona_def: Dict[str, Any],
        override: Dict[str, Any]
    ) -> Dict[str, Any]:
        """应用 override 配置到人格定义"""
        import copy
        result = copy.deepcopy(persona_def)

        # 深度合并 behavior
        if "behavior" in override:
            for key, value in override["behavior"].items():
                if key in result.get("behavior", {}):
                    if isinstance(value, dict):
                        result["behavior"][key].update(value)
                    else:
                        result["behavior"][key] = value
                else:
                    result["behavior"][key] = value

        # 直接覆盖顶层字段
        for key, value in override.items():
            if key != "behavior" and key in result:
                if isinstance(result[key], dict) and isinstance(value, dict):
                    result[key].update(value)
                else:
                    result[key] = value
            elif key not in result:
                result[key] = value

        return result

    def list_personas(self) -> List[str]:
        """列出所有已注册的人格"""
        return self.registry.list_personas()

    def get_persona_info(self, persona_id: str) -> Optional[Dict[str, Any]]:
        """获取人格元信息"""
        return self.registry.get_persona_info(persona_id)

    def health_check(self) -> Dict[str, Any]:
        """
        健康检查 - 验证所有已注册人格能否稳定加载激活 (V3.5.0)

        用于 install.sh 自检和排查"切换不稳定"问题。

        Returns:
            {
                "total": 总人格数,
                "ok": 可正常加载的人格数,
                "failed": [ {persona_id, error, hint}, ... ]
            }
        """
        result = {"total": 0, "ok": 0, "failed": []}
        personas = self.list_personas()
        result["total"] = len(personas)

        for pid in personas:
            try:
                pd = self.load_persona(pid)
                # 验证必需字段齐全（meta.id / behavior）
                assert pd["meta"]["id"], "meta.id 为空"
                assert "behavior" in pd, "缺少 behavior"
                assert "phrases" in pd, "缺少 phrases"
                result["ok"] += 1
            except PersonaLoadError as e:
                result["failed"].append({"persona_id": pid, "error": e.message, "hint": e.hint})
            except Exception as e:  # noqa: BLE001
                result["failed"].append({"persona_id": pid, "error": str(e), "hint": ""})

        return result


# 为向后兼容暴露到模块顶层
import json  # noqa: E402
