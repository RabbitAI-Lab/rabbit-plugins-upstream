"""
Schema Mapping Configuration.

Defines the mapping between JSONL fields and RDF properties.
This is the bridge configuration that drives both conversion directions.
"""

from typing import Dict, Any, Optional
from rdflib import URIRef, Literal, XSD
from rdflib.namespace import RDF, RDFS, SKOS

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from phase0.namespace import NamespaceManager


# Mapping from JSONL entity fields to RDF predicates
ENTITY_FIELD_MAPPING = {
    # Standard fields
    "name": {
        "predicate": "rdfs:label",
        "datatype": XSD.string,
        "required": True,
    },
    "description": {
        "predicate": "rdfs:comment",
        "datatype": XSD.string,
        "required": False,
    },
    "tags": {
        "predicate": "skos:altLabel",
        "datatype": XSD.string,
        "required": False,
        "is_list": True,
    },
    # Provenance fields (stored as properties on the entity node)
    "confidence": {
        "predicate": "dk-prop:confidence",
        "datatype": XSD.float,
        "required": False,
    },
    "provenance": {
        "predicate": "dk-prop:provenance",
        "datatype": XSD.string,
        "required": False,
        "serialize": "json",  # serialize as JSON string
    },
}

# Mapping for relation types to RDF predicate URIs
RELATION_TYPE_MAPPING = {
    "applies_to": "dk-rel:applies_to",
    "generates": "dk-rel:generates",
    "depends_on": "dk-rel:depends_on",
    "compatible_with": "dk-rel:compatible_with",
    "used_in": "dk-rel:used_in",
    "has_parameter": "dk-rel:has_parameter",
    "causes": "dk-rel:causes",
    "dispatches_to": "dk-rel:dispatches_to",
}


class SchemaMapper:
    """
    Schema mapping manager.
    
    Resolves field names to RDF predicates and datatypes,
    and provides reverse mapping for RDF -> JSONL conversion.
    """

    def __init__(self, ns_manager: Optional[NamespaceManager] = None):
        self.ns = ns_manager or NamespaceManager()
        self._entity_mapping = dict(ENTITY_FIELD_MAPPING)
        self._relation_mapping = dict(RELATION_TYPE_MAPPING)
        # Custom field mappings (for non-standard entity fields)
        self._custom_field_mappings: Dict[str, Dict[str, Any]] = {}

    def get_predicate_for_field(self, field_name: str) -> Optional[URIRef]:
        """Get the RDF predicate URI for a JSONL field name."""
        # Check standard mapping first
        if field_name in self._entity_mapping:
            return self._resolve_predicate(self._entity_mapping[field_name]["predicate"])
        # Check custom mappings
        if field_name in self._custom_field_mappings:
            return self._resolve_predicate(self._custom_field_mappings[field_name]["predicate"])
        # Fall back to generating a property URI
        return self.ns.property_uri(field_name)

    def get_datatype_for_field(self, field_name: str) -> Optional[Any]:
        """Get the XSD datatype for a JSONL field."""
        if field_name in self._entity_mapping:
            return self._entity_mapping[field_name].get("datatype")
        if field_name in self._custom_field_mappings:
            return self._custom_field_mappings[field_name].get("datatype")
        return XSD.string

    def is_list_field(self, field_name: str) -> bool:
        """Check if a field should produce multiple RDF triples."""
        if field_name in self._entity_mapping:
            return self._entity_mapping[field_name].get("is_list", False)
        if field_name in self._custom_field_mappings:
            return self._custom_field_mappings[field_name].get("is_list", False)
        return False

    def get_relation_predicate(self, relation_type: str) -> URIRef:
        """Get the RDF predicate for a relation type."""
        if relation_type in self._relation_mapping:
            return self._resolve_predicate(self._relation_mapping[relation_type])
        # Fall back to generating a relation URI
        return self.ns.relation_uri(relation_type)

    def reverse_map_predicate(self, predicate_uri: str) -> Optional[str]:
        """Reverse lookup: RDF predicate -> JSONL field name."""
        for field_name, mapping in self._entity_mapping.items():
            resolved = self._resolve_predicate(mapping["predicate"])
            if str(resolved) == predicate_uri:
                return field_name
        for field_name, mapping in self._custom_field_mappings.items():
            resolved = self._resolve_predicate(mapping["predicate"])
            if str(resolved) == predicate_uri:
                return field_name
        return None

    def register_custom_field(self, field_name: str, predicate: str,
                              datatype=None, is_list: bool = False) -> None:
        """Register a custom field mapping."""
        self._custom_field_mappings[field_name] = {
            "predicate": predicate,
            "datatype": datatype or XSD.string,
            "is_list": is_list,
        }

    def _resolve_predicate(self, predicate_str: str) -> URIRef:
        """Resolve a prefixed predicate string to a URIRef."""
        if ":" in predicate_str:
            prefix, local = predicate_str.split(":", 1)
            bindings = self.ns.get_all_bindings()
            if prefix in bindings:
                return URIRef(f"{bindings[prefix]}{local}")
        return URIRef(predicate_str)

    def get_all_entity_mappings(self) -> Dict[str, Dict]:
        """Return all entity field mappings (standard + custom)."""
        result = dict(self._entity_mapping)
        result.update(self._custom_field_mappings)
        return result

    def get_all_relation_mappings(self) -> Dict[str, str]:
        """Return all relation type mappings."""
        return dict(self._relation_mapping)
