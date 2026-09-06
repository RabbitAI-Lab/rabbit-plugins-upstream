"""Phase 0: Abstract Layer - Unified data model, type registry, namespace management."""

from .models import Entity, Relation, Property, EntityType
from .registry import EntityTypeRegistry
from .namespace import NamespaceManager

__all__ = [
    "Entity", "Relation", "Property", "EntityType",
    "EntityTypeRegistry", "NamespaceManager",
]
