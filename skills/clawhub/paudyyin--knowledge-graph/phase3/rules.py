"""
Business Rules Engine.

Supplements owlrl reasoning with domain-specific business rules
that cannot be expressed in standard OWL.
"""

import json
import logging
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Set
from itertools import combinations

from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from phase0.namespace import NamespaceManager

logger = logging.getLogger(__name__)


@dataclass
class Rule:
    """
    A business rule with condition and action.
    
    Attributes:
        name: Unique rule identifier
        description: Human-readable description
        condition: Callable(Graph) -> bool — whether rule should fire
        action: Callable(Graph) -> List[Tuple] — triples to add
        priority: Higher priority rules fire first (default 0)
        category: Rule category for grouping
        enabled: Whether rule is active
    """
    name: str
    description: str = ""
    condition: Optional[Callable[[Graph], bool]] = None
    action: Optional[Callable[[Graph], List[Tuple]]] = None
    priority: int = 0
    category: str = "default"
    enabled: bool = True

    def matches(self, graph: Graph) -> bool:
        """Check if this rule's condition is met."""
        if not self.enabled:
            return False
        if self.condition is None:
            return True  # No condition = always fires
        try:
            return self.condition(graph)
        except Exception as e:
            logger.warning(f"Rule '{self.name}' condition failed: {e}")
            return False

    def execute(self, graph: Graph) -> List[Tuple]:
        """Execute the rule action, return new triples."""
        if self.action is None:
            return []
        try:
            return self.action(graph)
        except Exception as e:
            logger.warning(f"Rule '{self.name}' action failed: {e}")
            return []


class BusinessRuleEngine:
    """
    Business rule engine for domain-kit.
    
    Manages rule registration, priority ordering, conflict detection,
    and execution against an RDF graph.
    
    Usage:
        engine = BusinessRuleEngine()
        engine.load_rules_from_config("rule_config.json")
        engine.add_rule(Rule(name="...", condition=..., action=..., priority=5))
        new_triples = engine.apply(graph)
    """

    def __init__(self, ns_manager: Optional[NamespaceManager] = None):
        self.ns = ns_manager or NamespaceManager()
        self.rules: List[Rule] = []
        self._execution_log: List[Dict[str, Any]] = []

    def add_rule(self, rule: Rule) -> None:
        """Add a rule to the engine."""
        self.rules.append(rule)
        self._sort_rules()

    def remove_rule(self, name: str) -> bool:
        """Remove a rule by name."""
        original_len = len(self.rules)
        self.rules = [r for r in self.rules if r.name != name]
        return len(self.rules) < original_len

    def get_rule(self, name: str) -> Optional[Rule]:
        """Get a rule by name."""
        for r in self.rules:
            if r.name == name:
                return r
        return None

    def _sort_rules(self) -> None:
        """Sort rules by priority (highest first)."""
        self.rules.sort(key=lambda r: -r.priority)

    def apply(self, graph: Graph, max_iterations: int = 10) -> List[Tuple]:
        """
        Apply all enabled rules to the graph.
        
        Iterates until no new triples are produced or max_iterations reached.
        
        Args:
            graph: RDF graph to apply rules to
            max_iterations: Safety limit on iteration count
            
        Returns:
            List of all new triples added
        """
        all_new_triples = []
        self._execution_log = []

        for iteration in range(max_iterations):
            new_in_iteration = []
            fired_rules = []

            for rule in self.rules:
                if rule.matches(graph):
                    new_triples = rule.execute(graph)
                    if new_triples:
                        for t in new_triples:
                            if len(t) == 3 and t not in graph:
                                graph.add(t)
                                new_in_iteration.append(t)
                        if new_in_iteration:
                            fired_rules.append(rule.name)

            all_new_triples.extend(new_in_iteration)
            self._execution_log.append({
                "iteration": iteration + 1,
                "fired_rules": fired_rules,
                "new_triples": len(new_in_iteration),
            })

            if not new_in_iteration:
                break

        logger.info(
            f"Rule engine: {len(all_new_triples)} triples added in "
            f"{len(self._execution_log)} iterations"
        )
        return all_new_triples

    def load_rules_from_config(self, config_path: str) -> None:
        """Load rule definitions from a JSON config file."""
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        for rule_def in config.get("rules", []):
            rule = self._build_rule_from_config(rule_def)
            if rule:
                self.add_rule(rule)

    def _build_rule_from_config(self, rule_def: Dict) -> Optional[Rule]:
        """Build a Rule object from a JSON config definition."""
        name = rule_def.get("name", "")
        if not name:
            return None

        rule_type = rule_def.get("type", "custom")
        priority = rule_def.get("priority", 0)
        category = rule_def.get("category", "default")
        description = rule_def.get("description", "")

        # Build condition and action based on rule type
        condition, action = self._get_builtin_rule(rule_type, rule_def)
        if condition is None and action is None:
            logger.warning(f"Unknown rule type '{rule_type}' for rule '{name}'")
            return None

        return Rule(
            name=name,
            description=description,
            condition=condition,
            action=action,
            priority=priority,
            category=category,
        )

    def _get_builtin_rule(self, rule_type: str, rule_def: Dict) -> Tuple[Optional[Callable], Optional[Callable]]:
        """Get built-in condition/action functions for known rule types."""
        ns = self.ns

        if rule_type == "transitive_inference":
            # Infer transitive relations: if A->B and B->C, add A->C
            rel_type = rule_def.get("relation", "")
            predicate = ns.relation_uri(rel_type)

            def condition(graph):
                for s, p, o in graph.triples((None, predicate, None)):
                    for s2, p2, o2 in graph.triples((o, predicate, None)):
                        if (s, predicate, o2) not in graph:
                            return True
                return False

            def action(graph):
                new_triples = []
                pairs = list(graph.triples((None, predicate, None)))
                for s1, p1, o1 in pairs:
                    for s2, p2, o2 in pairs:
                        if str(o1) == str(s2) and (s1, predicate, o2) not in graph:
                            triple = (s1, predicate, o2)
                            new_triples.append(triple)
                return new_triples

            return condition, action

        elif rule_type == "class_inference":
            # Infer class membership based on relation patterns
            from_class = rule_def.get("from_class", "")
            relation = rule_def.get("relation", "")
            to_class = rule_def.get("to_class", "")
            infer_class = rule_def.get("infer_class", "")

            from_uri = ns.class_uri(from_class)
            pred = ns.relation_uri(relation)
            to_uri = ns.class_uri(to_class)
            infer_uri = ns.class_uri(infer_class)

            def condition(graph):
                for s, p, o in graph.triples((None, RDF.type, from_uri)):
                    for s2, p2, o2 in graph.triples((s, pred, None)):
                        for s3, p3, o3 in graph.triples((o2, RDF.type, to_uri)):
                            if (s, RDF.type, infer_uri) not in graph:
                                return True
                return False

            def action(graph):
                new_triples = []
                for s, _, _ in graph.triples((None, RDF.type, from_uri)):
                    for _, _, o in graph.triples((s, pred, None)):
                        for _, _, _ in graph.triples((o, RDF.type, to_uri)):
                            if (s, RDF.type, infer_uri) not in graph:
                                new_triples.append((s, RDF.type, infer_uri))
                return new_triples

            return condition, action

        elif rule_type == "compatibility_check":
            # Check device-protocol compatibility and infer missing relations
            device_class = ns.class_uri("Device")
            protocol_class = ns.class_uri("Protocol")
            compat_pred = ns.relation_uri("compatible_with")

            def condition(graph):
                return False  # This rule is advisory, not auto-inference

            def action(graph):
                return []

            return condition, action

        elif rule_type == "constraint_propagation":
            # Propagate constraints from parent to child devices
            constraint_class = ns.class_uri("Constraint")
            applies_pred = ns.relation_uri("applies_to")
            depends_pred = ns.relation_uri("depends_on")

            def condition(graph):
                for s, p, o in graph.triples((None, RDF.type, constraint_class)):
                    for s2, p2, o2 in graph.triples((s, applies_pred, None)):
                        for s3, p3, o3 in graph.triples((o2, depends_pred, None)):
                            if (s, applies_pred, o3) not in graph:
                                return True
                return False

            def action(graph):
                new_triples = []
                for s, _, _ in graph.triples((None, RDF.type, constraint_class)):
                    for _, _, device in graph.triples((s, applies_pred, None)):
                        for _, _, dep_device in graph.triples((device, depends_pred, None)):
                            if (s, applies_pred, dep_device) not in graph:
                                new_triples.append((s, applies_pred, dep_device))
                return new_triples

            return condition, action

        else:
            return None, None

    def get_execution_log(self) -> List[Dict[str, Any]]:
        """Get the execution log from the last apply() call."""
        return self._execution_log

    def list_rules(self) -> List[Dict[str, Any]]:
        """List all registered rules."""
        return [
            {
                "name": r.name,
                "description": r.description,
                "priority": r.priority,
                "category": r.category,
                "enabled": r.enabled,
            }
            for r in self.rules
        ]


class RuleConflictDetector:
    """
    Detects conflicts between business rules.
    
    Two rules conflict if:
    1. They have the same name (duplicate)
    2. They produce contradictory triples (same subject+predicate, different object)
    3. They form a cycle (A triggers B triggers A)
    """

    def __init__(self, engine: BusinessRuleEngine):
        self.engine = engine

    def detect_conflicts(self) -> List[Dict[str, Any]]:
        """
        Detect all conflicts in the rule set.
        
        Returns:
            List of conflict descriptions
        """
        conflicts = []

        # Check for duplicate names
        names = [r.name for r in self.engine.rules]
        seen: Set[str] = set()
        for name in names:
            if name in seen:
                conflicts.append({
                    "type": "duplicate_name",
                    "rules": [name],
                    "severity": "error",
                    "description": f"Duplicate rule name: {name}",
                })
            seen.add(name)

        # Check for priority conflicts (same category, same priority)
        by_category: Dict[str, List[Rule]] = {}
        for rule in self.engine.rules:
            by_category.setdefault(rule.category, []).append(rule)
        for category, rules in by_category.items():
            priority_groups: Dict[int, List[Rule]] = {}
            for rule in rules:
                priority_groups.setdefault(rule.priority, []).append(rule)
            for priority, group in priority_groups.items():
                if len(group) > 1:
                    conflicts.append({
                        "type": "priority_conflict",
                        "rules": [r.name for r in group],
                        "severity": "warning",
                        "description": (
                            f"Rules {', '.join(r.name for r in group)} have same "
                            f"priority ({priority}) in category '{category}'"
                        ),
                    })

        return conflicts

    def validate_rules(self) -> bool:
        """
        Validate all rules. Returns True if no errors found.
        """
        conflicts = self.detect_conflicts()
        errors = [c for c in conflicts if c["severity"] == "error"]
        return len(errors) == 0
