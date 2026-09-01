"""Tests for Phase 0-6 integration."""

import pytest
import json
import tempfile
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from phase0.models import Entity, Relation
from phase0.registry import EntityTypeRegistry
from phase0.namespace import NamespaceManager
from phase1.jsonl_to_rdf import JsonlToRdfConverter
from phase1.rdf_to_jsonl import RdfToJsonlConverter
from phase2.reasoner import DomainKitReasoner
from phase3.rules import BusinessRuleEngine
from phase4.query_engine import SPARQLQueryEngine
from phase5.hybrid_query import HybridQueryEngine
from phase6.export import ProtegeExporter
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS


class TestFullPipeline:
    """Integration test: full pipeline from JSONL to query."""

    @pytest.fixture
    def pipeline_data(self, tmp_path):
        """Create test JSONL data."""
        entities = [
            {
                "id": "int_dev001",
                "entity_type": "PLC",
                "entity": {"name": "AM600", "model": "AM600", "memory_limit": 512},
                "provenance": {"confidence": 0.98},
                "tags": ["AM600", "PLC"],
                "created_at": "2026-07-12T10:00:00",
                "version": 1,
            },
            {
                "id": "int_tpl001",
                "entity_type": "CodeTemplate",
                "entity": {"name": "ConveyorControl", "language": "ST",
                           "content": "PROGRAM ...", "description": "Conveyor control"},
                "provenance": {"confidence": 1.0},
                "tags": ["ST", "conveyor"],
                "created_at": "2026-07-12T10:00:00",
                "version": 1,
            },
            {
                "id": "int_con001",
                "entity_type": "Constraint",
                "entity": {"name": "MemLimit", "rule": "Max 500KB", "severity": "critical"},
                "provenance": {"confidence": 0.9},
                "tags": ["AM600"],
                "created_at": "2026-07-12T10:00:00",
                "version": 1,
            },
        ]
        relations = [
            {
                "id": "int_rel001",
                "from_id": "int_tpl001",
                "to_id": "int_dev001",
                "relation_type": "depends_on",
                "confidence": 1.0,
                "provenance": {},
                "created_at": "2026-07-12T10:00:00",
            },
            {
                "id": "int_rel002",
                "from_id": "int_con001",
                "to_id": "int_dev001",
                "relation_type": "applies_to",
                "confidence": 1.0,
                "provenance": {},
                "created_at": "2026-07-12T10:00:00",
            },
        ]

        entities_path = str(tmp_path / "entities.jsonl")
        relations_path = str(tmp_path / "relations.jsonl")

        with open(entities_path, "w", encoding="utf-8") as f:
            for e in entities:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
        with open(relations_path, "w", encoding="utf-8") as f:
            for r in relations:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

        return entities_path, relations_path, entities, relations

    def test_full_pipeline(self, pipeline_data):
        """Test: JSONL -> RDF -> Reason -> Query -> Export."""
        entities_path, relations_path, entities, relations = pipeline_data
        ns = NamespaceManager()

        # Phase 1: Convert JSONL to RDF
        converter = JsonlToRdfConverter(ns_manager=ns)
        data_graph = converter.convert(entities_path, relations_path)
        assert len(data_graph) > 0

        # Phase 2: Reason
        reasoner = DomainKitReasoner(reasoning_level="rdfs")
        ontology_path = os.path.join(os.path.dirname(__file__), "..", "phase2", "ontology.ttl")
        if os.path.exists(ontology_path):
            reasoner.load_ontology(ontology_path)
        reasoner.load_data(data_graph)
        combined = reasoner.reason()
        assert len(combined) > len(data_graph)

        # Phase 4: Query
        query_engine = SPARQLQueryEngine(graph=combined, ns_manager=ns)
        result = query_engine.find_entities(name_filter="AM600")
        assert result.success is True

        # Phase 5: Hybrid query
        hybrid = HybridQueryEngine(query_engine=query_engine, ns_manager=ns)
        hybrid.set_graph(combined)
        hybrid_result = hybrid.query("查找AM600")
        assert hybrid_result["success"] is True

        # Phase 6: Export
        exporter = ProtegeExporter(graph=combined, ns_manager=ns)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = exporter.export_turtle(os.path.join(tmpdir, "pipeline_test"))
            assert os.path.exists(path)
            # Verify re-importable
            g2 = Graph()
            g2.parse(path, format="turtle")
            assert len(g2) > 0

    def test_roundtrip_integrity(self, pipeline_data):
        """Test that JSONL -> RDF -> JSONL preserves data."""
        entities_path, relations_path, orig_entities, orig_relations = pipeline_data
        ns = NamespaceManager()

        # Forward
        converter = JsonlToRdfConverter(ns_manager=ns)
        graph = converter.convert(entities_path, relations_path)

        # Reverse
        reverse = RdfToJsonlConverter(ns_manager=ns)
        entities_out, relations_out = reverse.convert_graph(graph)

        # Verify counts match
        assert len(entities_out) == len(orig_entities)
        assert len(relations_out) == len(orig_relations)

        # Verify IDs preserved
        orig_ids = {e["id"] for e in orig_entities}
        out_ids = {e["id"] for e in entities_out}
        assert orig_ids == out_ids
