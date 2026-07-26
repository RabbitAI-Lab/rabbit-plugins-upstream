"""
Skill loading utilities — reads routing declarations from filesystem.
"""

from pathlib import Path
from typing import Optional

from skill_radar.core import RoutingConfig, RouterWeights, ThresholdConfig, SkillRouter

try:
    import yaml
except ImportError:
    yaml = None


def _ensure_yaml():
    if yaml is None:
        raise ImportError("PyYAML is required: pip install pyyaml")


def load_skill_routing(skill_dir: Path) -> Optional[RoutingConfig]:
    """Load routing config from a skill directory."""
    _ensure_yaml()

    skill_md = skill_dir / "SKILL.md"
    routing_yaml = skill_dir / "routing.yaml"

    routing_data = None
    skill_name = skill_dir.name

    # Priority: standalone routing.yaml
    if routing_yaml.exists():
        with open(routing_yaml, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if data and "routing" in data:
                routing_data = data["routing"]
                skill_name = data.get("name", skill_dir.name)
            elif data and "keywords" in data:
                routing_data = data

    # Fallback: SKILL.md frontmatter
    if routing_data is None and skill_md.exists():
        with open(skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    fm = yaml.safe_load(parts[1])
                    if fm:
                        skill_name = fm.get("name", skill_dir.name)
                        metadata = fm.get("metadata", {})
                        if isinstance(metadata, dict) and "routing" in metadata:
                            routing_data = metadata["routing"]
                except (yaml.YAMLError, Exception):
                    pass

    if routing_data is None:
        return None

    return RoutingConfig(
        name=skill_name,
        keywords=routing_data.get("keywords", []),
        patterns=routing_data.get("patterns", []),
        intents=routing_data.get("intents", []),
        anti_patterns=routing_data.get("anti_patterns", []),
        anti_keywords=routing_data.get("anti_keywords", []),
        priority=routing_data.get("priority", 50),
        weight_overrides=routing_data.get("weight_overrides", {}),
        context=routing_data.get("context", {}),
        mode=routing_data.get("mode", "any"),
        threshold_ratio=routing_data.get("threshold_ratio", 0.5),
        exclusive_with=routing_data.get("exclusive_with", []),
        requires_skills=routing_data.get("requires_skills", []),
    )


def load_skills(skills_dir: str | Path, config_path: Optional[str | Path] = None) -> SkillRouter:
    """
    Convenience function: load all skills from a directory and return a ready router.

    Usage:
        router = load_skills("./skills/")
        results = router.route("review this contract")
    """
    skills_dir = Path(skills_dir)
    weights, threshold = load_router_config(Path(config_path)) if config_path else (RouterWeights(), ThresholdConfig())

    router = SkillRouter(weights=weights, threshold=threshold)

    if skills_dir.exists():
        for skill_path in sorted(skills_dir.iterdir()):
            if skill_path.is_dir() and not skill_path.name.startswith("."):
                config = load_skill_routing(skill_path)
                if config:
                    router.register_skill(config)

    return router


def load_router_config(config_path: Path) -> tuple[RouterWeights, ThresholdConfig]:
    """Load system-level router configuration."""
    _ensure_yaml()

    weights = RouterWeights()
    threshold = ThresholdConfig()

    if config_path and config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if data and "router" in data:
            r = data["router"]
            if "weights" in r:
                w = r["weights"]
                weights = RouterWeights(
                    keyword=w.get("keyword", 0.30),
                    pattern=w.get("pattern", 0.25),
                    intent=w.get("intent", 0.15),
                    anti=w.get("anti", 1.0),
                    context=w.get("context", 0.15),
                    priority=w.get("priority", 0.15),
                )
            if "threshold_strategy" in r:
                threshold.strategy = r["threshold_strategy"]
            if "threshold_params" in r:
                tp = r["threshold_params"]
                threshold.theta = tp.get("theta", 0.30)
                threshold.k = tp.get("k", 3)
                threshold.delta = tp.get("delta", 0.15)

    return weights, threshold
