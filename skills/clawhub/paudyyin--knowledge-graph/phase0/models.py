"""
Unified data model definitions.

Defines the core data structures that bridge JSONL storage and RDF representation:
- Entity: A knowledge node (device, template, constraint, etc.)
- Relation: A typed edge between two entities
- Property: A key-value attribute on an entity or relation
- EntityType: Metadata about a category of entities
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from enum import Enum
from datetime import datetime


class PropertyType(Enum):
    """Supported property data types."""
    STRING = "string"
    FLOAT = "float"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    URI = "uri"
    LIST = "list"  # homogeneous list of strings
    OBJECT = "object"  # nested dict


@dataclass
class Property:
    """A single key-value attribute."""
    key: str
    value: Any
    data_type: PropertyType = PropertyType.STRING
    required: bool = False

    def to_rdf_literal(self) -> str:
        """Convert value to RDF-compatible string."""
        if self.data_type == PropertyType.LIST:
            return ",".join(str(v) for v in self.value) if isinstance(self.value, list) else str(self.value)
        return str(self.value)

    @classmethod
    def from_jsonl_value(cls, key: str, value: Any) -> "Property":
        """Infer Property from a JSONL value."""
        if isinstance(value, bool):
            return cls(key=key, value=value, data_type=PropertyType.BOOLEAN)
        elif isinstance(value, int):
            return cls(key=key, value=value, data_type=PropertyType.INTEGER)
        elif isinstance(value, float):
            return cls(key=key, value=value, data_type=PropertyType.FLOAT)
        elif isinstance(value, list):
            return cls(key=key, value=value, data_type=PropertyType.LIST)
        elif isinstance(value, dict):
            return cls(key=key, value=value, data_type=PropertyType.OBJECT)
        else:
            return cls(key=key, value=str(value), data_type=PropertyType.STRING)


@dataclass
class EntityType:
    """Metadata for a category of entities."""
    name: str
    description: str = ""
    fields: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    # Mapping to OWL class URI (set by namespace manager)
    owl_class_uri: Optional[str] = None

    def get_required_fields(self) -> List[str]:
        return [k for k, v in self.fields.items() if v.get("required", False)]

    def validate_entity(self, data: Dict[str, Any]) -> List[str]:
        """Validate entity data against this type. Returns list of error messages."""
        errors = []
        for field_name in self.get_required_fields():
            if field_name not in data or data[field_name] is None:
                errors.append(f"Missing required field: {field_name}")
        return errors


@dataclass
class Entity:
    """
    Unified entity representation.
    
    This is the canonical in-memory format that converts to/from both
    JSONL records and RDF triples.
    """
    id: str
    entity_type: str
    name: str
    description: str = ""
    properties: Dict[str, Property] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    confidence: float = 1.0
    provenance: Dict[str, Any] = field(default_factory=dict)
    created_at: str = ""
    version: int = 1

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

    def to_jsonl_record(self) -> Dict[str, Any]:
        """Convert to JSONL storage format."""
        entity_data = {}
        for key, prop in self.properties.items():
            entity_data[key] = prop.value

        # Add standard fields
        entity_data["name"] = self.name
        if self.description:
            entity_data["description"] = self.description

        return {
            "id": self.id,
            "entity_type": self.entity_type,
            "entity": entity_data,
            "provenance": self.provenance,
            "tags": self.tags,
            "created_at": self.created_at,
            "version": self.version,
        }

    @classmethod
    def from_jsonl_record(cls, record: Dict[str, Any]) -> "Entity":
        """Create Entity from a JSONL record."""
        entity_data = record.get("entity", {})
        name = entity_data.pop("name", record.get("id", "unknown"))
        description = entity_data.pop("description", "")

        properties = {}
        for key, value in entity_data.items():
            properties[key] = Property.from_jsonl_value(key, value)

        return cls(
            id=record["id"],
            entity_type=record.get("entity_type", "Unknown"),
            name=name,
            description=description,
            properties=properties,
            tags=record.get("tags", []),
            confidence=record.get("provenance", {}).get("confidence", 1.0),
            provenance=record.get("provenance", {}),
            created_at=record.get("created_at", ""),
            version=record.get("version", 1),
        )


@dataclass
class Relation:
    """
    Unified relation representation.
    
    A typed, directed edge between two entities.
    """
    id: str
    from_id: str
    to_id: str
    relation_type: str
    confidence: float = 1.0
    provenance: Dict[str, Any] = field(default_factory=dict)
    properties: Dict[str, Property] = field(default_factory=dict)
    created_at: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

    def to_jsonl_record(self) -> Dict[str, Any]:
        """Convert to JSONL storage format."""
        return {
            "id": self.id,
            "from_id": self.from_id,
            "to_id": self.to_id,
            "relation_type": self.relation_type,
            "confidence": self.confidence,
            "provenance": self.provenance,
            "created_at": self.created_at,
        }

    @classmethod
    def from_jsonl_record(cls, record: Dict[str, Any]) -> "Relation":
        """Create Relation from a JSONL record."""
        return cls(
            id=record["id"],
            from_id=record["from_id"],
            to_id=record["to_id"],
            relation_type=record["relation_type"],
            confidence=record.get("confidence", 1.0),
            provenance=record.get("provenance", {}),
            created_at=record.get("created_at", ""),
        )
