"""Tests for Phase 5: Hybrid Query Engine."""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from phase5.hybrid_query import HybridQueryEngine
from phase4.query_engine import SPARQLQueryEngine
from phase0.namespace import NamespaceManager
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, SKOS


@pytest.fixture
def hybrid_graph():
    """Create a graph for hybrid query testing."""
    ns = NamespaceManager()
    g = Graph()
    ns.bind_to_graph(g)

    # Add devices (both Device and PLC types)
    am600 = ns.entity_uri("am600")
    g.add((am600, RDF.type, ns.class_uri("PLC")))
    g.add((am600, RDF.type, ns.class_uri("Device")))
    g.add((am600, RDFS.label, Literal("AM600 PLC")))
    g.add((am600, RDFS.comment, Literal("Midea AM600 PLC controller")))
    g.add((am600, SKOS.altLabel, Literal("AM600")))
    g.add((am600, SKOS.altLabel, Literal("PLC")))

    h5u = ns.entity_uri("h5u")
    g.add((h5u, RDF.type, ns.class_uri("PLC")))
    g.add((h5u, RDF.type, ns.class_uri("Device")))
    g.add((h5u, RDFS.label, Literal("H5U PLC")))
    g.add((h5u, SKOS.altLabel, Literal("H5U")))

    # Add templates
    tpl = ns.entity_uri("tpl001")
    g.add((tpl, RDF.type, ns.class_uri("CodeTemplate")))
    g.add((tpl, RDFS.label, Literal("ConveyorControl")))
    g.add((tpl, RDFS.comment, Literal("Conveyor belt control template")))

    # Add constraints
    con = ns.entity_uri("con001")
    g.add((con, RDF.type, ns.class_uri("Constraint")))
    g.add((con, RDFS.label, Literal("MemoryLimit")))
    g.add((con, RDFS.comment, Literal("Program size limit 500KB")))

    # Add class labels for type listing
    g.add((ns.class_uri("Device"), RDFS.label, Literal("Device")))
    g.add((ns.class_uri("PLC"), RDFS.label, Literal("PLC")))
    g.add((ns.class_uri("CodeTemplate"), RDFS.label, Literal("CodeTemplate")))
    g.add((ns.class_uri("Constraint"), RDFS.label, Literal("Constraint")))

    return g


@pytest.fixture
def hybrid_engine(hybrid_graph):
    ns = NamespaceManager()
    qe = SPARQLQueryEngine(graph=hybrid_graph, ns_manager=ns)
    return HybridQueryEngine(query_engine=qe, ns_manager=ns)


class TestHybridQueryEngine:
    """Test hybrid query engine."""

    def test_find_devices_query(self, hybrid_engine):
        result = hybrid_engine.query("查找所有设备")
        assert result["success"] is True
        assert result["row_count"] >= 1

    def test_find_specific_device(self, hybrid_engine):
        result = hybrid_engine.query("查找AM600设备")
        assert result["success"] is True
        # Should find AM600 via SPARQL or keyword
        assert result["row_count"] >= 1

    def test_find_templates_query(self, hybrid_engine):
        result = hybrid_engine.query("查找代码模板")
        assert result["success"] is True
        assert result["row_count"] >= 1

    def test_statistics_query(self, hybrid_engine):
        result = hybrid_engine.query("统计设备数量")
        assert result["success"] is True

    def test_list_types_query(self, hybrid_engine):
        result = hybrid_engine.query("有哪些类型")
        assert result["success"] is True

    def test_keyword_fallback(self, hybrid_engine):
        """Test that keyword fallback works for unmatched patterns."""
        result = hybrid_engine.query("ConveyorControl")
        assert result["success"] is True
        assert result["method"] in ("sparql", "keyword")

    def test_no_results(self, hybrid_engine):
        result = hybrid_engine.query("xyznonexistent123")
        # May or may not find results, but should not crash
        assert "success" in result
        assert "method" in result

    def test_query_logging(self, hybrid_engine):
        hybrid_engine.query("查找设备")
        hybrid_engine.query("查找模板")
        log = hybrid_engine.get_query_log()
        assert len(log) >= 2

    def test_accuracy_stats(self, hybrid_engine):
        hybrid_engine.query("查找设备")
        stats = hybrid_engine.get_accuracy_stats()
        assert stats["total"] >= 1


class TestNLPatterns:
    """Test NL pattern matching."""

    def test_device_pattern(self, hybrid_engine):
        intent, extracted = hybrid_engine._classify_intent("查找所有PLC设备")
        assert intent == "find_devices"

    def test_template_pattern(self, hybrid_engine):
        intent, extracted = hybrid_engine._classify_intent("找代码模板")
        assert intent == "find_templates"

    def test_constraint_pattern(self, hybrid_engine):
        intent, extracted = hybrid_engine._classify_intent("查找约束规范")
        assert intent == "find_constraints"

    def test_statistics_pattern(self, hybrid_engine):
        intent, extracted = hybrid_engine._classify_intent("统计数量")
        assert intent == "statistics"

    def test_types_pattern(self, hybrid_engine):
        intent, extracted = hybrid_engine._classify_intent("有哪些类型")
        assert intent == "list_types"

    def test_name_extraction_quoted(self):
        from phase5.hybrid_query import _extract_name
        name = _extract_name('查找"AM600"设备')
        assert name == "AM600"

    def test_name_extraction_identifier(self):
        from phase5.hybrid_query import _extract_name
        name = _extract_name("查找AM600设备")
        assert name == "AM600"
