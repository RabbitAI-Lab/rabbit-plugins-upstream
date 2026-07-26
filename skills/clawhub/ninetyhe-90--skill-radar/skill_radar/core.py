"""
Core routing engine — framework-agnostic pure logic.
No I/O, no file access, no dependencies beyond stdlib + regex.
"""

import re
from dataclasses import dataclass, field
from typing import Optional


# ─── Data Structures ─────────────────────────────────────────────────────────

@dataclass
class RoutingConfig:
    """Routing declaration for a single skill."""
    name: str
    keywords: list[str] = field(default_factory=list)
    patterns: list[str] = field(default_factory=list)
    intents: list[str] = field(default_factory=list)
    anti_patterns: list[str] = field(default_factory=list)
    anti_keywords: list[str] = field(default_factory=list)
    priority: int = 50
    weight_overrides: dict[str, float] = field(default_factory=dict)
    context: dict = field(default_factory=dict)
    mode: str = "any"  # any | all | threshold
    threshold_ratio: float = 0.5
    exclusive_with: list[str] = field(default_factory=list)
    requires_skills: list[str] = field(default_factory=list)


@dataclass
class RouterWeights:
    """Global scoring weights."""
    keyword: float = 0.30
    pattern: float = 0.25
    intent: float = 0.15
    anti: float = 1.0
    context: float = 0.15
    priority: float = 0.15


@dataclass
class ThresholdConfig:
    """Threshold strategy configuration."""
    strategy: str = "gap"   # fixed | top-k | gap | pattern-gate
    theta: float = 0.30
    k: int = 3
    delta: float = 0.15


@dataclass
class ScoringResult:
    """Scoring result for a single skill."""
    skill_name: str
    total_score: float
    keyword_score: float
    pattern_score: float
    intent_score: float
    context_score: float
    priority_score: float
    excluded: bool = False
    exclude_reason: str = ""
    matched_keywords: list[str] = field(default_factory=list)
    matched_patterns: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "skill": self.skill_name,
            "score": self.total_score,
            "keyword_score": self.keyword_score,
            "pattern_score": self.pattern_score,
            "intent_score": self.intent_score,
            "context_score": self.context_score,
            "priority_score": self.priority_score,
            "excluded": self.excluded,
            "exclude_reason": self.exclude_reason,
            "matched_keywords": self.matched_keywords,
            "matched_patterns": self.matched_patterns,
        }


# ─── Core Router ─────────────────────────────────────────────────────────────

class SkillRouter:
    """
    Declarative skill routing engine.

    Framework-agnostic: takes a query string, returns scored skill matches.
    No file I/O, no network calls — pure computation.
    """

    def __init__(
        self,
        weights: Optional[RouterWeights] = None,
        threshold: Optional[ThresholdConfig] = None,
    ):
        self.weights = weights or RouterWeights()
        self.threshold = threshold or ThresholdConfig()
        self.skills: list[RoutingConfig] = []

    def register_skill(self, config: RoutingConfig):
        """Register a skill's routing configuration."""
        self.skills.append(config)

    def route(self, query: str, context: Optional[dict] = None) -> list[ScoringResult]:
        """
        Route a query to matching skills.

        Args:
            query: User input text
            context: Optional environment context (file_types, workspace_hints, etc.)

        Returns:
            List of ScoringResult sorted by score descending, filtered by threshold.
        """
        context = context or {}
        results: list[ScoringResult] = []

        for skill in self.skills:
            result = self._score_skill(query, skill, context)
            results.append(result)

        results.sort(key=lambda r: (not r.excluded, r.total_score), reverse=True)
        return self._apply_threshold(results)

    def route_all(self, query: str, context: Optional[dict] = None) -> list[ScoringResult]:
        """Route without threshold filtering — returns all scores for debugging."""
        context = context or {}
        results = []
        for skill in self.skills:
            results.append(self._score_skill(query, skill, context))
        results.sort(key=lambda r: (not r.excluded, r.total_score), reverse=True)
        return results

    def _score_skill(self, query: str, skill: RoutingConfig, context: dict) -> ScoringResult:
        """Score a single skill against the query."""

        # Anti-pattern hard exclusion
        for ap in skill.anti_patterns:
            try:
                if re.search(ap, query, re.IGNORECASE):
                    return ScoringResult(
                        skill_name=skill.name, total_score=0.0,
                        keyword_score=0.0, pattern_score=0.0, intent_score=0.0,
                        context_score=0.0, priority_score=0.0,
                        excluded=True, exclude_reason=f"anti_pattern: {ap}",
                    )
            except re.error:
                if ap.lower() in query.lower():
                    return ScoringResult(
                        skill_name=skill.name, total_score=0.0,
                        keyword_score=0.0, pattern_score=0.0, intent_score=0.0,
                        context_score=0.0, priority_score=0.0,
                        excluded=True, exclude_reason=f"anti_pattern (text): {ap}",
                    )

        # Keyword scoring
        matched_keywords = []
        if skill.keywords:
            for kw in skill.keywords:
                if kw.lower() in query.lower():
                    matched_keywords.append(kw)
            if skill.mode == "all":
                keyword_score = 1.0 if len(matched_keywords) == len(skill.keywords) else 0.0
            elif skill.mode == "threshold":
                ratio = len(matched_keywords) / len(skill.keywords)
                keyword_score = 1.0 if ratio >= skill.threshold_ratio else ratio
            else:  # "any"
                keyword_score = min(len(matched_keywords) / len(skill.keywords), 1.0)
        else:
            keyword_score = 0.0

        # Pattern scoring
        matched_patterns = []
        if skill.patterns:
            for pat in skill.patterns:
                try:
                    if re.search(pat, query, re.IGNORECASE):
                        matched_patterns.append(pat)
                except re.error:
                    continue
            pattern_score = 1.0 if matched_patterns else 0.0
        else:
            pattern_score = 0.0

        # Intent scoring (simplified tag-based)
        intent_score = 0.0
        if skill.intents:
            intent_keywords = set()
            for intent in skill.intents:
                parts = intent.replace(".", " ").replace("_", " ").split()
                intent_keywords.update(parts)
            if intent_keywords:
                hits = sum(1 for ik in intent_keywords if ik.lower() in query.lower())
                intent_score = min(hits / len(intent_keywords), 1.0)

        # Context scoring
        context_score = 0.0
        if skill.context:
            signals, conditions = 0, 0
            if "file_types" in skill.context and "file_types" in context:
                conditions += 1
                if set(skill.context["file_types"]) & set(context.get("file_types", [])):
                    signals += 1
            if "workspace_hints" in skill.context and "workspace_hints" in context:
                conditions += 1
                skill_hints = {h.lower() for h in skill.context["workspace_hints"]}
                user_hints = {h.lower() for h in context.get("workspace_hints", [])}
                if skill_hints & user_hints:
                    signals += 1
            if conditions > 0:
                context_score = signals / conditions

        # Priority scoring
        priority_score = skill.priority / 100.0

        # Anti-keyword soft penalty
        anti_penalty = 0.0
        if skill.anti_keywords:
            hits = sum(1 for ak in skill.anti_keywords if ak.lower() in query.lower())
            anti_penalty = min(hits * 0.15, 0.5)

        # Weighted sum
        w = RouterWeights(**{**vars(self.weights), **skill.weight_overrides})
        total = (
            w.keyword * keyword_score
            + w.pattern * pattern_score
            + w.intent * intent_score
            + w.context * context_score
            + w.priority * priority_score
            - anti_penalty
        )
        total = max(0.0, min(1.0, total))

        return ScoringResult(
            skill_name=skill.name,
            total_score=round(total, 4),
            keyword_score=round(keyword_score, 4),
            pattern_score=round(pattern_score, 4),
            intent_score=round(intent_score, 4),
            context_score=round(context_score, 4),
            priority_score=round(priority_score, 4),
            matched_keywords=matched_keywords,
            matched_patterns=matched_patterns,
        )

    def _apply_threshold(self, results: list[ScoringResult]) -> list[ScoringResult]:
        """Apply threshold strategy to filter results."""
        active = [r for r in results if not r.excluded]
        if not active:
            return []

        s = self.threshold.strategy
        if s == "fixed":
            return [r for r in active if r.total_score >= self.threshold.theta]
        elif s == "top-k":
            return active[:self.threshold.k]
        elif s == "gap":
            if len(active) < 2:
                return active if active[0].total_score >= self.threshold.theta else []
            gap = active[0].total_score - active[1].total_score
            if gap >= self.threshold.delta:
                return [active[0]]
            return [r for r in active if r.total_score >= self.threshold.theta]
        elif s == "pattern-gate":
            gated = [r for r in active if r.matched_patterns]
            return gated if gated else [r for r in active if r.total_score >= self.threshold.theta]
        else:
            return active[:self.threshold.k]
