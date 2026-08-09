"""Tests for Phase 4: SPARQL Query Engine."""

import pytest
import time
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from phase4.query_engine import SPARQLQueryEngine, QueryResult, QueryTemplate
from phase0.namespace import NamespaceManager
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, SKOS


@pytest.fixture
def query_graph():
    """Create a graph with test data for query testing."""
    ns = NamespaceManager()
    g = Graph()
    ns.bind_to_graph(g)

    # Add entities
    for i in range(10):
        entity = ns.entity_uri(f"dev{i:03d}")
        g.add((entity, RDF.type, ns.class_uri("Device")))
        g.add((entity, RDFS.label, Literal(f"Device {i}")))
        g.add((entity, RDFS.comment, Literal(f"Test device number {i}")))
        g.add((entity, SKOS.altLabel, Literal(f"DEV{i}")))

    for i in range(5):
        tpl = ns.entity_uri(f"tpl{i:03d}")
        g.add((tpl, RDF.type, ns.class_uri("CodeTemplate")))
        g.add((tpl, RDFS.label, Literal(f"Template {i}")))

    # Add some relations
    for i in range(5):
        g.add((ns.entity_uri(f"tpl{i:03d}"), ns.relation_uri("depends_on"),
               ns.entity_uri(f"dev{i:03d}")))

    return g


@pytest.fixture
def engine(query_graph):
    return SPARQLQueryEngine(graph=query_graph)


class TestSPARQLQueryEngine:
    """Test SPARQL query execution."""

    def test_basic_query(self, engine):
        result = engine.execute("SELECT ?s WHERE { ?s ?p ?o } LIMIT 5")
        assert result.success is True
        assert result.row_count == 5

    def test_type_query(self, engine):
        result = engine.execute("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX dk-class: <https://domain-kit.midea.com/ontology/class/>
            SELECT ?s WHERE { ?s rdf:type dk-class:Device }
        """)
        assert result.success is True
        assert result.row_count == 10

    def test_invalid_query(self, engine):
        result = engine.execute("INVALID SPARQL")
        assert result.success is False
        assert result.error is not None

    def test_execute_template(self, engine):
        result = engine.execute_template("find_entity_by_name", name="Device 1")
        assert result.success is True
        assert result.row_count >= 1

    def test_execute_template_by_type(self, engine):
        result = engine.execute_template("find_entity_by_type", type="Device", limit="20")
        assert result.success is True
        assert result.row_count == 10

    def test_unknown_template(self, engine):
        result = engine.execute_template("nonexistent_template")
        assert result.success is False

    def test_list_templates(self, engine):
        templates = engine.list_templates()
        assert len(templates) >= 5
        names = [t["name"] for t in templates]
        assert "find_entity_by_name" in names
        assert "find_entity_by_type" in names

    def test_find_entities(self, engine):
        result = engine.find_entities(name_filter="Device")
        assert result.success is True
        assert result.row_count >= 1

    def test_find_entities_by_type(self, engine):
        result = engine.find_entities(entity_type="CodeTemplate")
        assert result.success is True
        assert result.row_count == 5

    def test_get_statistics(self, engine):
        result = engine.get_statistics()
        assert result.success is True
        assert result.row_count >= 1

    def test_performance_tracking(self, engine):
        engine.execute("SELECT ?s WHERE { ?s ?p ?o } LIMIT 1")
        engine.execute("SELECT ?s WHERE { ?s ?p ?o } LIMIT 1")
        stats = engine.get_performance_stats()
        assert stats["total_queries"] == 2
        assert stats["average_time_ms"] >= 0


class TestQueryPerformance:
    """Test query performance requirements (<500ms average)."""

    def test_query_under_500ms(self, query_graph):
        engine = SPARQLQueryEngine(graph=query_graph)
        times = []
        for _ in range(100):
            start = time.time()
            result = engine.execute("SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 50")
            elapsed = (time.time() - start) * 1000
            times.append(elapsed)
        
        avg_time = sum(times) / len(times)
        assert avg_time < 500, f"Average query time {avg_time:.1f}ms exceeds 500ms limit"


class TestQueryResult:
    """Test QueryResult model."""

    def test_success_result(self):
        r = QueryResult(success=True, query="SELECT ...", bindings=[{"s": "x"}], row_count=1)
        assert bool(r) is True
        assert len(r) == 1

    def test_empty_result(self):
        r = QueryResult(success=True, query="SELECT ...", bindings=[], row_count=0)
        assert bool(r) is False
        assert len(r) == 0

    def test_failed_result(self):
        r = QueryResult(success=False, query="BAD", error="Syntax error")
        assert bool(r) is False
        assert r.error is not None

    def test_to_dicts(self):
        r = QueryResult(success=True, query="SELECT ...",
                       bindings=[{"s": "x", "p": "y"}], row_count=1)
        dicts = r.to_dicts()
        assert len(dicts) == 1
        assert dicts[0]["s"] == "x"


class TestCustomTemplate:
    """Test custom template registration."""

    def test_register_and_use(self, query_graph):
        engine = SPARQLQueryEngine(graph=query_graph)
        template = QueryTemplate(
            name="custom_test",
            description="Custom test query",
            sparql_template="SELECT ?s WHERE { ?s ?p ?o } LIMIT ${limit}",
            parameters=["limit"],
        )
        engine.register_template(template)
        result = engine.execute_template("custom_test", limit="3")
        assert result.success is True
        assert result.row_count == 3
