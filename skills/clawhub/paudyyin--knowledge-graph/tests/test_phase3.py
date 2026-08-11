"""Tests for Phase 3: Business Rules Engine."""

import pytest
import json
import tempfile
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from phase3.rules import BusinessRuleEngine, Rule, RuleConflictDetector
from phase0.namespace import NamespaceManager
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS


@pytest.fixture
def ns():
    return NamespaceManager()


@pytest.fixture
def sample_graph(ns):
    """Create a sample graph for rule testing."""
    g = Graph()
    ns.bind_to_graph(g)

    # Add entities
    e1 = ns.entity_uri("dev001")
    e2 = ns.entity_uri("dev002")
    e3 = ns.entity_uri("dev003")
    tpl = ns.entity_uri("tpl001")
    constraint = ns.entity_uri("con001")

    g.add((e1, RDF.type, ns.class_uri("Device")))
    g.add((e1, RDFS.label, Literal("Device1")))
    g.add((e2, RDF.type, ns.class_uri("Device")))
    g.add((e2, RDFS.label, Literal("Device2")))
    g.add((e3, RDF.type, ns.class_uri("Device")))
    g.add((e3, RDFS.label, Literal("Device3")))
    g.add((tpl, RDF.type, ns.class_uri("CodeTemplate")))
    g.add((tpl, RDFS.label, Literal("Template1")))
    g.add((constraint, RDF.type, ns.class_uri("Constraint")))
    g.add((constraint, RDFS.label, Literal("Constraint1")))

    # Add relations
    depends = ns.relation_uri("depends_on")
    applies = ns.relation_uri("applies_to")

    g.add((tpl, depends, e1))     # Template depends on Device1
    g.add((e1, depends, e2))      # Device1 depends on Device2
    g.add((e2, depends, e3))      # Device2 depends on Device3
    g.add((constraint, applies, e1))  # Constraint applies to Device1

    return g


class TestRule:
    """Test Rule data model."""

    def test_create_rule(self):
        rule = Rule(name="test_rule", description="A test rule", priority=5)
        assert rule.name == "test_rule"
        assert rule.priority == 5
        assert rule.enabled is True

    def test_rule_matches_no_condition(self):
        rule = Rule(name="always", condition=None)
        g = Graph()
        assert rule.matches(g) is True

    def test_rule_matches_with_condition(self):
        rule = Rule(name="test", condition=lambda g: len(g) > 0)
        g = Graph()
        assert rule.matches(g) is False
        g.add((URIRef("http://s"), URIRef("http://p"), URIRef("http://o")))
        assert rule.matches(g) is True

    def test_disabled_rule(self):
        rule = Rule(name="disabled", enabled=False)
        g = Graph()
        assert rule.matches(g) is False


class TestBusinessRuleEngine:
    """Test BusinessRuleEngine."""

    def test_add_rule(self):
        engine = BusinessRuleEngine()
        rule = Rule(name="test", priority=5)
        engine.add_rule(rule)
        assert len(engine.rules) == 1

    def test_priority_ordering(self):
        engine = BusinessRuleEngine()
        engine.add_rule(Rule(name="low", priority=1))
        engine.add_rule(Rule(name="high", priority=10))
        engine.add_rule(Rule(name="mid", priority=5))
        assert engine.rules[0].name == "high"
        assert engine.rules[1].name == "mid"
        assert engine.rules[2].name == "low"

    def test_remove_rule(self):
        engine = BusinessRuleEngine()
        engine.add_rule(Rule(name="test"))
        assert engine.remove_rule("test") is True
        assert len(engine.rules) == 0

    def test_get_rule(self):
        engine = BusinessRuleEngine()
        engine.add_rule(Rule(name="test", description="A test"))
        rule = engine.get_rule("test")
        assert rule is not None
        assert rule.description == "A test"

    def test_apply_simple_rule(self, ns):
        engine = BusinessRuleEngine(ns)
        
        def condition(g):
            return True
        
        def action(g):
            new_s = ns.entity_uri("inferred001")
            new_p = ns.property_uri("inferred")
            new_o = Literal("test_value")
            return [(new_s, new_p, new_o)]
        
        engine.add_rule(Rule(name="add_triple", condition=condition, action=action))
        
        g = Graph()
        new_triples = engine.apply(g)
        assert len(new_triples) == 1
        assert (ns.entity_uri("inferred001"), ns.property_uri("inferred"), Literal("test_value")) in g

    def test_load_rules_from_config(self, ns):
        engine = BusinessRuleEngine(ns)
        config_path = os.path.join(os.path.dirname(__file__), "..", "phase3", "rule_config.json")
        engine.load_rules_from_config(config_path)
        assert len(engine.rules) > 0

    def test_transitive_rule(self, sample_graph, ns):
        """Test transitive depends_on inference."""
        engine = BusinessRuleEngine(ns)
        
        depends = ns.relation_uri("depends_on")
        
        def condition(g):
            for s, p, o in g.triples((None, depends, None)):
                for s2, p2, o2 in g.triples((o, depends, None)):
                    if (s, depends, o2) not in g:
                        return True
            return False
        
        def action(g):
            new_triples = []
            pairs = list(g.triples((None, depends, None)))
            for s1, p1, o1 in pairs:
                for s2, p2, o2 in pairs:
                    if str(o1) == str(s2) and (s1, depends, o2) not in g:
                        new_triples.append((s1, depends, o2))
            return new_triples
        
        engine.add_rule(Rule(
            name="transitive_depends",
            condition=condition,
            action=action,
            priority=10,
        ))
        
        new_triples = engine.apply(sample_graph)
        # tpl001 -> dev001 -> dev002 -> dev003
        # Should infer: tpl001 -> dev002, tpl001 -> dev003, dev001 -> dev003
        assert len(new_triples) >= 2

    def test_list_rules(self):
        engine = BusinessRuleEngine()
        engine.add_rule(Rule(name="r1", description="Rule 1"))
        engine.add_rule(Rule(name="r2", description="Rule 2"))
        rules = engine.list_rules()
        assert len(rules) == 2
        assert rules[0]["name"] in ["r1", "r2"]

    def test_execution_log(self, sample_graph, ns):
        engine = BusinessRuleEngine(ns)
        engine.add_rule(Rule(name="noop", condition=lambda g: False, action=lambda g: []))
        engine.apply(sample_graph)
        log = engine.get_execution_log()
        assert len(log) >= 1


class TestRuleConflictDetector:
    """Test RuleConflictDetector."""

    def test_no_conflicts(self):
        engine = BusinessRuleEngine()
        engine.add_rule(Rule(name="r1", priority=10, category="test"))
        engine.add_rule(Rule(name="r2", priority=5, category="test"))
        detector = RuleConflictDetector(engine)
        conflicts = detector.detect_conflicts()
        assert len(conflicts) == 0

    def test_priority_conflict(self):
        engine = BusinessRuleEngine()
        engine.add_rule(Rule(name="r1", priority=5, category="test"))
        engine.add_rule(Rule(name="r2", priority=5, category="test"))
        detector = RuleConflictDetector(engine)
        conflicts = detector.detect_conflicts()
        priority_conflicts = [c for c in conflicts if c["type"] == "priority_conflict"]
        assert len(priority_conflicts) == 1

    def test_validate_rules_ok(self):
        engine = BusinessRuleEngine()
        engine.add_rule(Rule(name="r1", priority=10))
        engine.add_rule(Rule(name="r2", priority=5))
        detector = RuleConflictDetector(engine)
        assert detector.validate_rules() is True

    def test_validate_rules_duplicate(self):
        engine = BusinessRuleEngine()
        engine.add_rule(Rule(name="same_name", priority=10))
        engine.add_rule(Rule(name="same_name", priority=5))
        detector = RuleConflictDetector(engine)
        assert detector.validate_rules() is False
