"""
Skill Radar — Declarative skill routing engine for multi-skill AI agents.

Usage:
    # SDK mode
    from skill_radar import SkillRouter, load_skills
    router = load_skills("./skills/")
    results = router.route("review this contract")

    # CLI mode
    # skill-radar route "query" --skills-dir ./skills/

    # HTTP mode
    # skill-radar serve --port 8900
"""

from skill_radar.core import (
    SkillRouter,
    RoutingConfig,
    RouterWeights,
    ThresholdConfig,
    ScoringResult,
)
from skill_radar.loader import load_skill_routing, load_skills, load_router_config

__version__ = "1.1.0"
__all__ = [
    "SkillRouter",
    "RoutingConfig",
    "RouterWeights",
    "ThresholdConfig",
    "ScoringResult",
    "load_skill_routing",
    "load_skills",
    "load_router_config",
]
