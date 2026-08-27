"""Tests for Phase 0: Abstract Layer."""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from phase0.models import Entity, Relation, Property, PropertyType, EntityType
from phase0.registry import EntityTypeRegistry
from phase0.namespace import NamespaceManager


class TestProperty:
    """Test Property data model."""

    def test_string_property(self):
        p = Property(key="name", value="AM600", data_type=PropertyType.STRING)
        assert p.to_rdf_literal() == "AM600"

    def test_float_property(self):
        p = Property(key="confidence", value=0.95, data_type=PropertyType.FLOAT)
        assert p.to_rdf_literal() == "0.95"

    def test_list_property(self):
        p = Property(key="tags", value=["ST", "LD", "FBD"], data_type=PropertyType.LIST)
        assert p.to_rdf_literal() == "ST,LD,FBD"

    def test_from_jsonl_value_string(self):
        p = Property.from_jsonl_value("name", "test")
        assert p.data_type == PropertyType.STRING

    def test_from_jsonl_value_int(self):
        p = Property.from_jsonl_value("count", 42)
        assert p.data_type == PropertyType.INTEGER

    def test_from_jsonl_value_float(self):
        p = Property.from_jsonl_value("score", 3.14)
        assert p.data_type == PropertyType.FLOAT

    def test_from_jsonl_value_bool(self):
        p = Property.from_jsonl_value("active", True)
        assert p.data_type == PropertyType.BOOLEAN

    def test_from_jsonl_value_list(self):
        p = Property.from_jsonl_value("tags", ["a", "b"])
        assert p.data_type == PropertyType.LIST

    def test_from_jsonl_value_dict(self):
        p = Property.from_jsonl_value("meta", {"key": "val"})
        assert p.data_type == PropertyType.OBJECT


class TestEntityType:
    """Test EntityType model."""

    def test_create_entity_type(self):
        et = EntityType(name="Device", description="Test device")
        assert et.name == "Device"
        assert et.description == "Test device"

    def test_required_fields(self):
        et = EntityType(
            name="Device",
            fields={
                "name": {"type": "string", "required": True},
                "model": {"type": "string", "required": True},
                "desc": {"type": "string", "required": False},
            },
        )
        required = et.get_required_fields()
        assert "name" in required
        assert "model" in required
        assert "desc" not in required

    def test_validate_entity_valid(self):
        et = EntityType(
            name="Device",
            fields={"name": {"type": "string", "required": True}},
        )
        errors = et.validate_entity({"name": "AM600"})
        assert len(errors) == 0

    def test_validate_entity_missing_required(self):
        et = EntityType(
            name="Device",
            fields={"name": {"type": "string", "required": True}},
        )
        errors = et.validate_entity({})
        assert len(errors) > 0
        assert "name" in errors[0]


class TestEntity:
    """Test Entity model."""

    def test_create_entity(self):
        e = Entity(id="test001", entity_type="Device", name="AM600")
        assert e.id == "test001"
        assert e.entity_type == "Device"
        assert e.name == "AM600"

    def test_to_jsonl_record(self):
        e = Entity(
            id="test001",
            entity_type="Device",
            name="AM600",
            description="Test PLC",
            tags=["PLC", "AM600"],
        )
        e.properties["model"] = Property.from_jsonl_value("model", "AM600")
        record = e.to_jsonl_record()
        assert record["id"] == "test001"
        assert record["entity_type"] == "Device"
        assert record["entity"]["name"] == "AM600"
        assert record["entity"]["model"] == "AM600"
        assert "PLC" in record["tags"]

    def test_from_jsonl_record(self):
        record = {
            "id": "test001",
            "entity_type": "Device",
            "entity": {"name": "AM600", "model": "AM600"},
            "provenance": {"confidence": 0.98},
            "tags": ["PLC"],
            "created_at": "2026-07-12T10:00:00",
            "version": 1,
        }
        e = Entity.from_jsonl_record(record)
        assert e.id == "test001"
        assert e.name == "AM600"
        assert "model" in e.properties

    def test_roundtrip(self):
        """Entity -> JSONL -> Entity should preserve data."""
        original = Entity(
            id="round001",
            entity_type="Constraint",
            name="Test Constraint",
            description="A test constraint",
            tags=["test"],
            provenance={"confidence": 0.9},
        )
        original.properties["severity"] = Property.from_jsonl_value("severity", "critical")
        
        record = original.to_jsonl_record()
        restored = Entity.from_jsonl_record(record)
        
        assert restored.id == original.id
        assert restored.entity_type == original.entity_type
        assert restored.name == original.name


class TestRelation:
    """Test Relation model."""

    def test_create_relation(self):
        r = Relation(id="rel001", from_id="e1", to_id="e2", relation_type="depends_on")
        assert r.from_id == "e1"
        assert r.to_id == "e2"
        assert r.relation_type == "depends_on"

    def test_to_jsonl_record(self):
        r = Relation(id="rel001", from_id="e1", to_id="e2",
                     relation_type="depends_on", confidence=0.8)
        record = r.to_jsonl_record()
        assert record["from_id"] == "e1"
        assert record["confidence"] == 0.8

    def test_from_jsonl_record(self):
        record = {
            "id": "rel001",
            "from_id": "e1",
            "to_id": "e2",
            "relation_type": "applies_to",
            "confidence": 1.0,
            "provenance": {},
        }
        r = Relation.from_jsonl_record(record)
        assert r.relation_type == "applies_to"


class TestEntityTypeRegistry:
    """Test EntityTypeRegistry."""

    def test_default_types_loaded(self):
        registry = EntityTypeRegistry()
        types = registry.list_entity_types()
        assert "Device" in types
        assert "CodeTemplate" in types
        assert "Constraint" in types
        assert "Protocol" in types
        assert "BestPractice" in types
        # v2.0 new types
        assert "Scenario" in types
        assert "Parameter" in types
        assert "Failure" in types

    def test_default_relation_types(self):
        registry = EntityTypeRegistry()
        rel_types = registry.list_relation_types()
        assert "applies_to" in rel_types
        assert "depends_on" in rel_types
        assert "compatible_with" in rel_types
        assert "used_in" in rel_types
        assert "causes" in rel_types

    def test_register_custom_type(self):
        registry = EntityTypeRegistry()
        custom = EntityType(name="CustomType", description="Custom")
        registry.register_entity_type(custom)
        assert "CustomType" in registry.list_entity_types()

    def test_validate_entity(self):
        registry = EntityTypeRegistry()
        errors = registry.validate_entity("Device", {"name": "AM600", "model": "AM600"})
        assert len(errors) == 0

    def test_validate_entity_missing_field(self):
        registry = EntityTypeRegistry()
        errors = registry.validate_entity("Device", {})
        assert len(errors) > 0

    def test_unknown_type_validation(self):
        registry = EntityTypeRegistry()
        errors = registry.validate_entity("NonExistent", {})
        assert "Unknown" in errors[0]


class TestNamespaceManager:
    """Test NamespaceManager."""

    def test_entity_uri(self):
        ns = NamespaceManager()
        uri = ns.entity_uri("test123")
        assert "entity/test123" in str(uri)

    def test_class_uri(self):
        ns = NamespaceManager()
        uri = ns.class_uri("Device")
        assert "class/Device" in str(uri)

    def test_relation_uri(self):
        ns = NamespaceManager()
        uri = ns.relation_uri("depends_on")
        assert "relation/depends_on" in str(uri)

    def test_property_uri(self):
        ns = NamespaceManager()
        uri = ns.property_uri("confidence")
        assert "property/confidence" in str(uri)

    def test_bind_to_graph(self):
        from rdflib import Graph
        ns = NamespaceManager()
        g = Graph()
        ns.bind_to_graph(g)
        # Check that prefixes are bound
        prefixes = dict(g.namespaces())
        assert "dk" in prefixes or "dk-entity" in prefixes

    def test_compact_uri(self):
        ns = NamespaceManager()
        full_uri = "https://domain-kit.midea.com/ontology/entity/test123"
        compact = ns.compact_uri(full_uri)
        assert "dk-entity:test123" == compact

    def test_custom_namespace(self):
        ns = NamespaceManager()
        ns.add_custom_namespace("ex", "http://example.org/")
        bindings = ns.get_all_bindings()
        assert "ex" in bindings
