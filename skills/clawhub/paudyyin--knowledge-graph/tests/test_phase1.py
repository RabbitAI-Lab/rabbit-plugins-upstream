"""Tests for Phase 1: Data Interop - JSONL <-> RDF conversion."""

import pytest
import json
import tempfile
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from phase1.jsonl_to_rdf import JsonlToRdfConverter
from phase1.rdf_to_jsonl import RdfToJsonlConverter
from phase1.schema_mapping import SchemaMapper
from phase0.namespace import NamespaceManager
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS


# Test data
SAMPLE_ENTITIES = [
    {
        "id": "entity001",
        "entity_type": "Device",
        "entity": {
            "name": "AM600 PLC",
            "model": "AM600",
            "manufacturer": "Midea",
            "supported_languages": ["ST", "LD", "FBD"],
        },
        "provenance": {"confidence": 0.98, "source_type": "manual"},
        "tags": ["PLC", "AM600"],
        "created_at": "2026-07-12T10:00:00",
        "version": 1,
    },
    {
        "id": "entity002",
        "entity_type": "CodeTemplate",
        "entity": {
            "name": "ConveyorControl",
            "language": "ST",
            "content": "PROGRAM ConveyorControl\nVAR\n  StartBtn: BOOL;\nEND_VAR",
            "description": "Basic conveyor control",
        },
        "provenance": {"confidence": 1.0},
        "tags": ["ST", "conveyor"],
        "created_at": "2026-07-12T10:00:00",
        "version": 1,
    },
    {
        "id": "entity003",
        "entity_type": "Constraint",
        "entity": {
            "name": "MemoryLimit",
            "rule": "Program size must not exceed 500KB",
            "severity": "critical",
            "scope": "All AM600 projects",
        },
        "provenance": {"confidence": 0.9},
        "tags": ["AM600", "constraint"],
        "created_at": "2026-07-12T10:00:00",
        "version": 1,
    },
]

SAMPLE_RELATIONS = [
    {
        "id": "rel001",
        "from_id": "entity002",
        "to_id": "entity001",
        "relation_type": "depends_on",
        "confidence": 1.0,
        "provenance": {},
        "created_at": "2026-07-12T10:00:00",
    },
    {
        "id": "rel002",
        "from_id": "entity003",
        "to_id": "entity001",
        "relation_type": "applies_to",
        "confidence": 0.9,
        "provenance": {},
        "created_at": "2026-07-12T10:00:00",
    },
]


@pytest.fixture
def temp_jsonl_files():
    """Create temporary JSONL files for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        entities_path = os.path.join(tmpdir, "entities.jsonl")
        relations_path = os.path.join(tmpdir, "relations.jsonl")

        with open(entities_path, "w", encoding="utf-8") as f:
            for e in SAMPLE_ENTITIES:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")

        with open(relations_path, "w", encoding="utf-8") as f:
            for r in SAMPLE_RELATIONS:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

        yield entities_path, relations_path


@pytest.fixture
def converted_graph(temp_jsonl_files):
    """Create a converted RDF graph."""
    entities_path, relations_path = temp_jsonl_files
    converter = JsonlToRdfConverter()
    return converter.convert(entities_path, relations_path)


class TestJsonlToRdf:
    """Test JSONL -> RDF conversion."""

    def test_convert_produces_graph(self, converted_graph):
        assert isinstance(converted_graph, Graph)
        assert len(converted_graph) > 0

    def test_entities_have_types(self, converted_graph):
        ns = NamespaceManager()
        # Check that entities have rdf:type
        types_found = set()
        for s, p, o in converted_graph.triples((None, RDF.type, None)):
            if "class/" in str(o):
                types_found.add(str(o).split("/")[-1])
        assert "Device" in types_found
        assert "CodeTemplate" in types_found
        assert "Constraint" in types_found

    def test_entities_have_labels(self, converted_graph):
        labels = []
        for s, p, o in converted_graph.triples((None, RDFS.label, None)):
            labels.append(str(o))
        assert "AM600 PLC" in labels
        assert "ConveyorControl" in labels

    def test_relations_as_predicates(self, converted_graph):
        ns = NamespaceManager()
        rel_pred = ns.relation_uri("depends_on")
        triples = list(converted_graph.triples((None, rel_pred, None)))
        assert len(triples) == 1

    def test_tags_as_altlabels(self, converted_graph):
        from rdflib.namespace import SKOS
        ns = NamespaceManager()
        entity_uri = ns.entity_uri("entity001")
        tags = [str(o) for s, p, o in converted_graph.triples((entity_uri, SKOS.altLabel, None))]
        assert "PLC" in tags
        assert "AM600" in tags

    def test_list_fields_expanded(self, converted_graph):
        ns = NamespaceManager()
        entity_uri = ns.entity_uri("entity001")
        # supported_languages should produce multiple triples
        lang_pred = ns.property_uri("supported_languages")
        langs = [str(o) for s, p, o in converted_graph.triples((entity_uri, lang_pred, None))]
        assert "ST" in langs
        assert "LD" in langs
        assert "FBD" in langs

    def test_convert_from_objects(self):
        converter = JsonlToRdfConverter()
        graph = converter.convert_from_objects(SAMPLE_ENTITIES, SAMPLE_RELATIONS)
        assert len(graph) > 0

    def test_ontology_header(self, converted_graph):
        from rdflib.namespace import OWL
        ontologies = list(converted_graph.triples((None, RDF.type, OWL.Ontology)))
        assert len(ontologies) == 1


class TestRdfToJsonl:
    """Test RDF -> JSONL conversion."""

    def test_convert_back(self, converted_graph):
        converter = RdfToJsonlConverter()
        entities, relations = converter.convert_graph(converted_graph)
        assert len(entities) >= 3
        assert len(relations) >= 2

    def test_entity_ids_preserved(self, converted_graph):
        converter = RdfToJsonlConverter()
        entities, _ = converter.convert_graph(converted_graph)
        ids = {e["id"] for e in entities}
        assert "entity001" in ids
        assert "entity002" in ids
        assert "entity003" in ids

    def test_entity_types_preserved(self, converted_graph):
        converter = RdfToJsonlConverter()
        entities, _ = converter.convert_graph(converted_graph)
        types = {e["entity_type"] for e in entities}
        assert "Device" in types
        assert "CodeTemplate" in types

    def test_names_preserved(self, converted_graph):
        converter = RdfToJsonlConverter()
        entities, _ = converter.convert_graph(converted_graph)
        names = {e["entity"].get("name", "") for e in entities}
        assert "AM600 PLC" in names

    def test_tags_preserved(self, converted_graph):
        converter = RdfToJsonlConverter()
        entities, _ = converter.convert_graph(converted_graph)
        all_tags = set()
        for e in entities:
            all_tags.update(e.get("tags", []))
        assert "PLC" in all_tags


class TestRoundTrip:
    """Test lossless round-trip: JSONL -> RDF -> JSONL."""

    def test_roundtrip_entity_count(self, temp_jsonl_files):
        entities_path, relations_path = temp_jsonl_files
        # Forward
        converter = JsonlToRdfConverter()
        graph = converter.convert(entities_path, relations_path)
        # Reverse
        reverse = RdfToJsonlConverter()
        entities, relations = reverse.convert_graph(graph)
        assert len(entities) == len(SAMPLE_ENTITIES)

    def test_roundtrip_relation_count(self, temp_jsonl_files):
        entities_path, relations_path = temp_jsonl_files
        converter = JsonlToRdfConverter()
        graph = converter.convert(entities_path, relations_path)
        reverse = RdfToJsonlConverter()
        _, relations = reverse.convert_graph(graph)
        assert len(relations) == len(SAMPLE_RELATIONS)

    def test_roundtrip_names(self, temp_jsonl_files):
        entities_path, relations_path = temp_jsonl_files
        converter = JsonlToRdfConverter()
        graph = converter.convert(entities_path, relations_path)
        reverse = RdfToJsonlConverter()
        entities, _ = reverse.convert_graph(graph)
        
        original_names = {e["entity"].get("name", e["entity"].get("title", "")) for e in SAMPLE_ENTITIES}
        restored_names = {e["entity"].get("name", "") for e in entities}
        # All original names should be present
        for name in original_names:
            if name:
                assert name in restored_names, f"Name '{name}' lost in round-trip"

    def test_roundtrip_via_file(self, temp_jsonl_files):
        """Test full file-based round-trip."""
        entities_path, relations_path = temp_jsonl_files
        
        with tempfile.TemporaryDirectory() as tmpdir:
            # Convert to RDF file
            converter = JsonlToRdfConverter()
            graph = converter.convert(entities_path, relations_path)
            ttl_path = os.path.join(tmpdir, "test.ttl")
            graph.serialize(ttl_path, format="turtle")
            
            # Convert back from RDF file
            reverse = RdfToJsonlConverter()
            entities_out, relations_out = reverse.convert(ttl_path, format="turtle")
            
            assert len(entities_out) == len(SAMPLE_ENTITIES)
            assert len(relations_out) == len(SAMPLE_RELATIONS)


class TestSchemaMapper:
    """Test SchemaMapper."""

    def test_get_predicate_for_standard_field(self):
        mapper = SchemaMapper()
        pred = mapper.get_predicate_for_field("name")
        assert pred is not None
        assert "label" in str(pred)

    def test_get_predicate_for_custom_field(self):
        mapper = SchemaMapper()
        pred = mapper.get_predicate_for_field("custom_field")
        assert pred is not None

    def test_get_relation_predicate(self):
        mapper = SchemaMapper()
        pred = mapper.get_relation_predicate("depends_on")
        assert "depends_on" in str(pred)

    def test_is_list_field(self):
        mapper = SchemaMapper()
        assert mapper.is_list_field("tags") is True
        assert mapper.is_list_field("name") is False

    def test_reverse_map(self):
        mapper = SchemaMapper()
        pred = mapper.get_predicate_for_field("name")
        field_name = mapper.reverse_map_predicate(str(pred))
        assert field_name == "name"
