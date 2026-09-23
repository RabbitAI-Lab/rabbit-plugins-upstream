"""
RDF to JSONL Converter.

Converts RDF graph (from Turtle/RDF/XML) back to domain-kit JSONL format.
Designed for lossless round-trip: JSONL -> RDF -> JSONL should preserve all data.
"""

import json
import logging
from typing import Optional, List, Dict, Any, Tuple
from collections import defaultdict

from rdflib import Graph, URIRef, Literal, BNode, XSD
from rdflib.namespace import RDF, RDFS, SKOS, OWL

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from phase0.namespace import NamespaceManager
from phase0.models import Entity, Relation
from .schema_mapping import SchemaMapper

logger = logging.getLogger(__name__)


class RdfToJsonlConverter:
    """
    Converts RDF graph back to JSONL format.
    
    Usage:
        converter = RdfToJsonlConverter()
        entities, relations = converter.convert("input.ttl")
        # Write to files
        converter.write_jsonl(entities, "entities.jsonl")
        converter.write_jsonl(relations, "relations.jsonl")
    """

    def __init__(self, ns_manager: Optional[NamespaceManager] = None,
                 schema_mapper: Optional[SchemaMapper] = None):
        self.ns = ns_manager or NamespaceManager()
        self.mapper = schema_mapper or SchemaMapper(self.ns)

    def convert(self, rdf_path: str, format: str = "turtle") -> Tuple[List[Dict], List[Dict]]:
        """
        Convert an RDF file to JSONL records.
        
        Args:
            rdf_path: Path to RDF file (Turtle, RDF/XML, etc.)
            format: RDF serialization format
            
        Returns:
            Tuple of (entity_records, relation_records)
        """
        graph = Graph()
        graph.parse(rdf_path, format=format)
        return self.convert_graph(graph)

    def convert_graph(self, graph: Graph) -> Tuple[List[Dict], List[Dict]]:
        """
        Convert an RDF graph to JSONL records.
        
        Returns:
            Tuple of (entity_records, relation_records)
        """
        self.ns.bind_to_graph(graph)

        # Collect entity data
        entities = self._extract_entities(graph)
        relations = self._extract_relations(graph)

        return entities, relations

    def _extract_entities(self, graph: Graph) -> List[Dict[str, Any]]:
        """Extract all entities from the graph."""
        entities = []

        # Find all typed resources (ignore ontology header, classes)
        entity_uris = set()
        for s, p, o in graph.triples((None, RDF.type, None)):
            if isinstance(s, URIRef) and isinstance(o, URIRef):
                # Skip OWL ontology and class declarations
                if o == OWL.Ontology or o == OWL.Class:
                    continue
                if o == RDF.Statement:
                    continue  # Skip reified statements
                entity_uris.add(s)

        for entity_uri in entity_uris:
            try:
                record = self._entity_from_graph(graph, entity_uri)
                if record:
                    entities.append(record)
            except Exception as e:
                logger.warning(f"Failed to extract entity {entity_uri}: {e}")

        return entities

    def _entity_from_graph(self, graph: Graph, uri: URIRef) -> Optional[Dict[str, Any]]:
        """Reconstruct a JSONL entity record from RDF triples."""
        # Extract entity ID from URI
        entity_id = str(uri).split("/")[-1]

        # Get type
        entity_type = "Unknown"
        for _, _, o in graph.triples((uri, RDF.type, None)):
            if isinstance(o, URIRef) and str(o).startswith(str(self.ns.class_ns)):
                entity_type = str(o).split("/")[-1]
                break

        # Get name (rdfs:label)
        name = ""
        for _, _, o in graph.triples((uri, RDFS.label, None)):
            if isinstance(o, Literal):
                name = str(o)
                break

        # Get description (rdfs:comment)
        description = ""
        for _, _, o in graph.triples((uri, RDFS.comment, None)):
            if isinstance(o, Literal):
                description = str(o)
                break

        # Get tags (skos:altLabel)
        tags = []
        for _, _, o in graph.triples((uri, SKOS.altLabel, None)):
            if isinstance(o, Literal):
                tags.append(str(o))

        # Get confidence
        confidence = 1.0
        for _, _, o in graph.triples((uri, self.ns.property_uri("confidence"), None)):
            if isinstance(o, Literal):
                try:
                    confidence = float(o)
                except (ValueError, TypeError):
                    pass

        # Get provenance
        provenance = {}
        for _, _, o in graph.triples((uri, self.ns.property_uri("provenance"), None)):
            if isinstance(o, Literal):
                try:
                    provenance = json.loads(str(o))
                except json.JSONDecodeError:
                    provenance = {"raw": str(o)}

        # Get version
        version = 1
        for _, _, o in graph.triples((uri, self.ns.property_uri("version"), None)):
            if isinstance(o, Literal):
                try:
                    version = int(o)
                except (ValueError, TypeError):
                    pass

        # Get created_at
        created_at = ""
        for _, _, o in graph.triples((uri, self.ns.property_uri("created_at"), None)):
            if isinstance(o, Literal):
                created_at = str(o)

        # Collect remaining properties into entity dict
        entity_data: Dict[str, Any] = {}
        if name:
            entity_data["name"] = name
        if description:
            entity_data["description"] = description

        # Known predicates to skip (already handled)
        skip_predicates = {
            str(RDF.type), str(RDFS.label), str(RDFS.comment),
            str(SKOS.altLabel),
            str(self.ns.property_uri("confidence")),
            str(self.ns.property_uri("provenance")),
            str(self.ns.property_uri("version")),
            str(self.ns.property_uri("created_at")),
        }

        # Collect other properties
        property_map: Dict[str, List[str]] = defaultdict(list)
        for p, o in graph.predicate_objects(uri):
            p_str = str(p)
            if p_str in skip_predicates:
                continue
            if isinstance(o, Literal):
                # Reverse-map predicate to field name
                field_name = self.mapper.reverse_map_predicate(p_str)
                if field_name is None:
                    # Extract local name from URI
                    field_name = p_str.split("/")[-1].split("#")[-1]
                property_map[field_name].append(str(o))

        for field_name, values in property_map.items():
            if len(values) == 1:
                entity_data[field_name] = values[0]
            else:
                entity_data[field_name] = values

        return {
            "id": entity_id,
            "entity_type": entity_type,
            "entity": entity_data,
            "provenance": provenance,
            "tags": tags,
            "created_at": created_at,
            "version": version,
        }

    def _extract_relations(self, graph: Graph) -> List[Dict[str, Any]]:
        """Extract relations from the graph (non-RDF.type, non-property triples)."""
        relations = []
        relation_id_counter = 0

        # Known property predicates (not relations)
        property_predicates = {
            str(RDF.type), str(RDFS.label), str(RDFS.comment),
            str(SKOS.altLabel), str(OWL.Ontology),
        }
        # Add all dk-prop: predicates
        for prefix, ns_uri in self.ns.get_all_bindings().items():
            if prefix == "dk-prop":
                property_predicates.add(str(ns_uri).rstrip("/"))

        # Find relation-type predicates (dk-rel:)
        rel_prefix = str(self.ns.relation_ns)
        
        # Also check reified statements for confidence annotations
        reified_confidence: Dict[Tuple[str, str, str], float] = {}
        for s, p, o in graph.triples((None, RDF.type, RDF.Statement)):
            subj = pred = obj = None
            conf = 1.0
            for _, _, v in graph.triples((s, RDF.subject, None)):
                subj = str(v)
            for _, _, v in graph.triples((s, RDF.predicate, None)):
                pred = str(v)
            for _, _, v in graph.triples((s, RDF.object, None)):
                obj = str(v)
            for _, _, v in graph.triples((s, self.ns.property_uri("confidence"), None)):
                try:
                    conf = float(v)
                except (ValueError, TypeError):
                    pass
            if subj and pred and obj:
                reified_confidence[(subj, pred, obj)] = conf

        for s, p, o in graph.triples((None, None, None)):
            if not (isinstance(s, URIRef) and isinstance(o, URIRef) and isinstance(p, URIRef)):
                continue
            p_str = str(p)
            # Only process dk-rel: predicates
            if not p_str.startswith(rel_prefix):
                continue

            from_id = str(s).split("/")[-1]
            to_id = str(o).split("/")[-1]
            relation_type = p_str.split("/")[-1]

            # Check for reified confidence
            confidence = reified_confidence.get((str(s), p_str, str(o)), 1.0)

            relation_id_counter += 1
            relations.append({
                "id": f"rel_{relation_id_counter:04d}",
                "from_id": from_id,
                "to_id": to_id,
                "relation_type": relation_type,
                "confidence": confidence,
                "provenance": {},
                "created_at": "",
            })

        return relations

    def write_jsonl(self, records: List[Dict], output_path: str) -> int:
        """Write records to a JSONL file. Returns count of records written."""
        count = 0
        with open(output_path, "w", encoding="utf-8") as f:
            for record in records:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                count += 1
        return count
