"""
JSONL to RDF Converter.

Converts domain-kit JSONL storage (entities.jsonl + relations.jsonl)
into RDF graph (Turtle format).
"""

import json
import logging
from pathlib import Path
from typing import Optional, List, Dict, Any

from rdflib import Graph, URIRef, Literal, BNode, XSD
from rdflib.namespace import RDF, RDFS, SKOS, OWL

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from phase0.namespace import NamespaceManager
from phase0.models import Entity, Relation
from .schema_mapping import SchemaMapper

logger = logging.getLogger(__name__)


class JsonlToRdfConverter:
    """
    Converts JSONL entities and relations into an RDF graph.
    
    Usage:
        converter = JsonlToRdfConverter()
        graph = converter.convert("path/to/entities.jsonl", "path/to/relations.jsonl")
        graph.serialize("output.ttl", format="turtle")
    """

    def __init__(self, ns_manager: Optional[NamespaceManager] = None,
                 schema_mapper: Optional[SchemaMapper] = None):
        self.ns = ns_manager or NamespaceManager()
        self.mapper = schema_mapper or SchemaMapper(self.ns)

    def convert(self, entities_path: str, relations_path: str) -> Graph:
        """
        Convert JSONL files to RDF graph.
        
        Args:
            entities_path: Path to entities.jsonl
            relations_path: Path to relations.jsonl
            
        Returns:
            rdflib.Graph with all entities and relations as triples
        """
        graph = Graph()
        self.ns.bind_to_graph(graph)

        # Add ontology header
        self._add_ontology_header(graph)

        # Convert entities
        entities = self._load_jsonl(entities_path)
        entity_count = 0
        for record in entities:
            try:
                self._convert_entity(graph, record)
                entity_count += 1
            except Exception as e:
                logger.warning(f"Failed to convert entity {record.get('id', '?')}: {e}")

        # Convert relations
        relations = self._load_jsonl(relations_path)
        relation_count = 0
        for record in relations:
            try:
                self._convert_relation(graph, record)
                relation_count += 1
            except Exception as e:
                logger.warning(f"Failed to convert relation {record.get('id', '?')}: {e}")

        logger.info(f"Converted {entity_count} entities, {relation_count} relations")
        return graph

    def convert_entities_only(self, entities: List[Dict[str, Any]]) -> Graph:
        """Convert a list of entity dicts to RDF graph (no file I/O)."""
        graph = Graph()
        self.ns.bind_to_graph(graph)
        self._add_ontology_header(graph)
        for record in entities:
            self._convert_entity(graph, record)
        return graph

    def convert_from_objects(self, entities: List[Dict], relations: List[Dict]) -> Graph:
        """Convert from in-memory entity/relation dicts."""
        graph = Graph()
        self.ns.bind_to_graph(graph)
        self._add_ontology_header(graph)
        for record in entities:
            self._convert_entity(graph, record)
        for record in relations:
            self._convert_relation(graph, record)
        return graph

    def _add_ontology_header(self, graph: Graph) -> None:
        """Add ontology metadata triples."""
        ont_uri = URIRef(self.ns.base_uri)
        graph.add((ont_uri, RDF.type, OWL.Ontology))
        graph.add((ont_uri, RDFS.label, Literal("Domain-Kit Ontology", lang="en")))
        graph.add((ont_uri, RDFS.comment, Literal(
            "OWL ontology for industrial automation domain knowledge", lang="en")))

    def _convert_entity(self, graph: Graph, record: Dict[str, Any]) -> None:
        """Convert a single JSONL entity record to RDF triples."""
        entity_id = record["id"]
        entity_type = record.get("entity_type", "Unknown")
        entity_data = record.get("entity", {})

        # Subject URI
        subject = self.ns.entity_uri(entity_id)

        # rdf:type
        class_uri = self.ns.class_uri(entity_type)
        graph.add((subject, RDF.type, class_uri))

        # Declare the class
        graph.add((class_uri, RDF.type, OWL.Class))
        graph.add((class_uri, RDFS.label, Literal(entity_type)))

        # Name -> rdfs:label
        name = entity_data.get("name", entity_data.get("title", entity_data.get("rule", entity_data.get("model", ""))))
        if name:
            graph.add((subject, RDFS.label, Literal(str(name), lang="zh")))

        # Description -> rdfs:comment
        desc = entity_data.get("description", entity_data.get("content", entity_data.get("rationale", "")))
        if desc:
            graph.add((subject, RDFS.comment, Literal(str(desc))))

        # Tags -> skos:altLabel (multiple triples)
        tags = record.get("tags", [])
        for tag in tags:
            graph.add((subject, SKOS.altLabel, Literal(str(tag))))

        # Confidence -> custom property
        confidence = record.get("provenance", {}).get("confidence")
        if confidence is not None:
            graph.add((subject, self.ns.property_uri("confidence"),
                       Literal(float(confidence), datatype=XSD.float)))

        # Provenance -> serialized JSON
        provenance = record.get("provenance", {})
        if provenance:
            graph.add((subject, self.ns.property_uri("provenance"),
                       Literal(json.dumps(provenance, ensure_ascii=False))))

        # Version
        version = record.get("version", 1)
        graph.add((subject, self.ns.property_uri("version"),
                   Literal(int(version), datatype=XSD.integer)))

        # Created at
        created_at = record.get("created_at", "")
        if created_at:
            graph.add((subject, self.ns.property_uri("created_at"),
                       Literal(created_at, datatype=XSD.dateTime)))

        # Remaining entity fields as custom properties
        skip_fields = {"name", "description", "title", "content", "rule", "rationale", "model"}
        for field_name, value in entity_data.items():
            if field_name in skip_fields:
                continue
            self._add_property(graph, subject, field_name, value)

    def _add_property(self, graph: Graph, subject: URIRef, field_name: str, value: Any) -> None:
        """Add a single property as RDF triple(s)."""
        pred = self.mapper.get_predicate_for_field(field_name)
        if pred is None:
            pred = self.ns.property_uri(field_name)

        if isinstance(value, list):
            for item in value:
                graph.add((subject, pred, Literal(str(item))))
        elif isinstance(value, dict):
            # Serialize nested objects as JSON string
            graph.add((subject, pred, Literal(json.dumps(value, ensure_ascii=False))))
        elif isinstance(value, bool):
            graph.add((subject, pred, Literal(value, datatype=XSD.boolean)))
        elif isinstance(value, int):
            graph.add((subject, pred, Literal(value, datatype=XSD.integer)))
        elif isinstance(value, float):
            graph.add((subject, pred, Literal(value, datatype=XSD.float)))
        else:
            graph.add((subject, pred, Literal(str(value))))

    def _convert_relation(self, graph: Graph, record: Dict[str, Any]) -> None:
        """Convert a JSONL relation record to an RDF triple."""
        from_id = record["from_id"]
        to_id = record["to_id"]
        relation_type = record["relation_type"]

        subject = self.ns.entity_uri(from_id)
        obj = self.ns.entity_uri(to_id)
        predicate = self.mapper.get_relation_predicate(relation_type)

        graph.add((subject, predicate, obj))

        # Add confidence as reified statement annotation
        confidence = record.get("confidence")
        if confidence is not None and confidence != 1.0:
            # Use a blank node for reification
            bnode = BNode()
            graph.add((bnode, RDF.type, RDF.Statement))
            graph.add((bnode, RDF.subject, subject))
            graph.add((bnode, RDF.predicate, predicate))
            graph.add((bnode, RDF.object, obj))
            graph.add((bnode, self.ns.property_uri("confidence"),
                       Literal(float(confidence), datatype=XSD.float)))

    def _load_jsonl(self, path: str) -> List[Dict[str, Any]]:
        """Load records from a JSONL file."""
        records = []
        filepath = Path(path)
        if not filepath.exists():
            logger.warning(f"File not found: {path}")
            return records
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        records.append(json.loads(line))
                    except json.JSONDecodeError as e:
                        logger.warning(f"Invalid JSON line: {e}")
        return records
