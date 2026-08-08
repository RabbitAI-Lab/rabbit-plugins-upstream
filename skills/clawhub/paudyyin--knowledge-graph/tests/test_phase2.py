"""Tests for Phase 2: Basic Reasoning."""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from phase2.reasoner import DomainKitReasoner, IncrementalReasoner, RDFS, OWL_LITE, OWL_RL
from phase0.namespace import NamespaceManager
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL


@pytest.fixture
def sample_ontology():
    """Create a sample ontology in Turtle format."""
    return """
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix dk-class: <https://domain-kit.midea.com/ontology/class/> .
@prefix dk-rel: <https://domain-kit.midea.com/ontology/relation/> .

dk-class:Device a owl:Class ;
    rdfs:label "Device" .

dk-class:PLC a owl:Class ;
    rdfs:subClassOf dk-class:Device ;
    rdfs:label "PLC" .

dk-class:WCSDevice a owl:Class ;
    rdfs:subClassOf dk-class:Device ;
    rdfs:label "WCSDevice" .

dk-class:CodeTemplate a owl:Class ;
    rdfs:label "CodeTemplate" .

dk-class:Protocol a owl:Class ;
    rdfs:label "Protocol" .

dk-rel:depends_on a owl:ObjectProperty, owl:TransitiveProperty ;
    rdfs:label "depends_on" .

dk-rel:compatible_with a owl:ObjectProperty, owl:SymmetricProperty ;
    rdfs:label "compatible_with" .
"""


@pytest.fixture
def sample_data(ns_manager):
    """Create sample instance data."""
    ns = ns_manager
    g = Graph()
    ns.bind_to_graph(g)

    # Instance data
    am600 = ns.entity_uri("am600")
    plc_template = ns.entity_uri("tpl001")
    protocol = ns.entity_uri("modbus")

    g.add((am600, RDF.type, ns.class_uri("PLC")))
    g.add((am600, RDFS.label, Literal("AM600 PLC")))

    g.add((plc_template, RDF.type, ns.class_uri("CodeTemplate")))
    g.add((plc_template, RDFS.label, Literal("ConveyorControl")))
    g.add((plc_template, ns.relation_uri("depends_on"), am600))

    g.add((protocol, RDF.type, ns.class_uri("Protocol")))
    g.add((protocol, RDFS.label, Literal("Modbus")))
    g.add((am600, ns.relation_uri("compatible_with"), protocol))

    return g


@pytest.fixture
def ns_manager():
    return NamespaceManager()


class TestDomainKitReasoner:
    """Test the DomainKitReasoner."""

    def test_create_reasoner_rdfs(self):
        r = DomainKitReasoner(reasoning_level="rdfs")
        assert r.level == "rdfs"

    def test_create_reasoner_owl_lite(self):
        r = DomainKitReasoner(reasoning_level="owl_lite")
        assert r.level == "owl_lite"

    def test_create_reasoner_invalid(self):
        with pytest.raises(ValueError):
            DomainKitReasoner(reasoning_level="invalid")

    def test_load_ontology_from_string(self, sample_ontology):
        r = DomainKitReasoner()
        r.load_ontology_from_string(sample_ontology)
        assert len(r.ontology_graph) > 0

    def test_rdfs_reasoning_subclass(self, sample_ontology, sample_data):
        """Test that RDFS reasoning infers subclass membership."""
        r = DomainKitReasoner(reasoning_level="rdfs")
        r.load_ontology_from_string(sample_ontology)
        r.load_data(sample_data)
        combined = r.reason()

        ns = NamespaceManager()
        am600 = ns.entity_uri("am600")
        # AM600 is a PLC, PLC is a subclass of Device
        # So AM600 should also be inferred as a Device
        device_type = ns.class_uri("Device")
        types = [str(o) for s, p, o in combined.triples((am600, RDF.type, None))]
        assert any("Device" in t for t in types), f"Expected Device type, got: {types}"

    def test_reasoning_stats(self, sample_ontology, sample_data):
        r = DomainKitReasoner(reasoning_level="rdfs")
        r.load_ontology_from_string(sample_ontology)
        r.load_data(sample_data)
        r.reason()
        stats = r.get_reasoning_stats()
        assert stats["reasoned"] is True
        assert stats["triples_inferred"] >= 0
        assert stats["reasoning_time_ms"] >= 0

    def test_query_after_reasoning(self, sample_ontology, sample_data):
        r = DomainKitReasoner(reasoning_level="rdfs")
        r.load_ontology_from_string(sample_ontology)
        r.load_data(sample_data)
        r.reason()
        results = r.query("SELECT ?s WHERE { ?s ?p ?o } LIMIT 10")
        assert results is not None

    def test_get_combined_graph(self, sample_ontology, sample_data):
        r = DomainKitReasoner()
        r.load_ontology_from_string(sample_ontology)
        r.load_data(sample_data)
        r.reason()
        combined = r.get_combined_graph()
        assert len(combined) > len(sample_data)

    def test_owl_lite_reasoning(self, sample_ontology, sample_data):
        r = DomainKitReasoner(reasoning_level="owl_lite")
        r.load_ontology_from_string(sample_ontology)
        r.load_data(sample_data)
        combined = r.reason()
        assert len(combined) > 0

    def test_symmetric_property(self, sample_ontology, sample_data):
        """Test that symmetric property inference works."""
        r = DomainKitReasoner(reasoning_level="owl_lite")
        r.load_ontology_from_string(sample_ontology)
        r.load_data(sample_data)
        combined = r.reason()

        ns = NamespaceManager()
        am600 = ns.entity_uri("am600")
        protocol = ns.entity_uri("modbus")
        compat = ns.relation_uri("compatible_with")

        # AM600 compatible_with Modbus should imply Modbus compatible_with AM600
        reverse = list(combined.triples((protocol, compat, am600)))
        assert len(reverse) > 0, "Symmetric property inference failed"


class TestIncrementalReasoner:
    """Test incremental reasoning."""

    def test_hash_computation(self, tmp_path):
        # Create test files
        f1 = tmp_path / "test.txt"
        f1.write_text("hello")
        
        r = DomainKitReasoner()
        ir = IncrementalReasoner(r)
        h1 = ir.compute_hash(str(f1))
        assert len(h1) == 32  # MD5 hex

        # Same content = same hash
        h2 = ir.compute_hash(str(f1))
        assert h1 == h2

    def test_change_detection(self, tmp_path):
        f1 = tmp_path / "test.txt"
        f1.write_text("hello")
        
        r = DomainKitReasoner()
        ir = IncrementalReasoner(r)
        
        assert ir.has_changed(str(f1)) is True  # First time
        
        # Simulate last hash
        ir._last_hash = ir.compute_hash(str(f1))
        assert ir.has_changed(str(f1)) is False  # No change
        
        # Modify file
        f1.write_text("world")
        assert ir.has_changed(str(f1)) is True  # Changed
