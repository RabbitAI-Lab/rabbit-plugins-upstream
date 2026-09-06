"""Tests for Phase 6: Visualization / Protégé Export."""

import pytest
import tempfile
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from phase6.export import ProtegeExporter
from phase0.namespace import NamespaceManager
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL


@pytest.fixture
def export_graph():
    """Create a graph for export testing."""
    ns = NamespaceManager()
    g = Graph()
    ns.bind_to_graph(g)

    # Add ontology header
    ont = URIRef(ns.base_uri)
    g.add((ont, RDF.type, OWL.Ontology))

    # Add a class
    device_class = ns.class_uri("Device")
    g.add((device_class, RDF.type, OWL.Class))
    g.add((device_class, RDFS.label, Literal("Device")))

    # Add an instance
    am600 = ns.entity_uri("am600")
    g.add((am600, RDF.type, device_class))
    g.add((am600, RDFS.label, Literal("AM600 PLC")))

    return g


class TestProtegeExporter:
    """Test Protégé export functionality."""

    def test_export_turtle(self, export_graph):
        exporter = ProtegeExporter(graph=export_graph)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = exporter.export_turtle(os.path.join(tmpdir, "test"))
            assert path.endswith(".ttl")
            assert os.path.exists(path)
            # Read and verify content
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            assert "AM600" in content
            assert "Device" in content

    def test_export_rdfxml(self, export_graph):
        exporter = ProtegeExporter(graph=export_graph)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = exporter.export_rdfxml(os.path.join(tmpdir, "test"))
            assert path.endswith(".rdf")
            assert os.path.exists(path)

    def test_export_ntriples(self, export_graph):
        exporter = ProtegeExporter(graph=export_graph)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = exporter.export_ntriples(os.path.join(tmpdir, "test"))
            assert path.endswith(".nt")
            assert os.path.exists(path)

    def test_to_turtle_string(self, export_graph):
        exporter = ProtegeExporter(graph=export_graph)
        turtle_str = exporter.to_turtle_string()
        assert "AM600" in turtle_str
        assert len(turtle_str) > 0

    def test_graph_summary(self, export_graph):
        exporter = ProtegeExporter(graph=export_graph)
        summary = exporter.get_graph_summary()
        assert summary["total_triples"] > 0
        assert summary["unique_subjects"] > 0
        assert "class_counts" in summary

    def test_roundtrip_export_import(self, export_graph):
        """Test that exported Turtle can be re-imported."""
        exporter = ProtegeExporter(graph=export_graph)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "roundtrip.ttl")
            exporter.export_turtle(path)
            
            # Re-import
            g2 = Graph()
            g2.parse(path, format="turtle")
            
            # Should have same number of triples
            assert len(g2) == len(export_graph)

    def test_protege_compatible(self, export_graph):
        """Verify the export has proper ontology header for Protégé."""
        exporter = ProtegeExporter(graph=export_graph)
        turtle_str = exporter.to_turtle_string()
        # Protégé expects owl:Ontology declaration
        assert "Ontology" in turtle_str or "owl:" in turtle_str
