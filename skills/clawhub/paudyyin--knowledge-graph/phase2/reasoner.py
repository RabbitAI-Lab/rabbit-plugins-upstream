"""
Domain-Kit Reasoner.

Provides RDFS / OWL Lite / OWL RL reasoning over the domain-kit knowledge graph.
Uses owlrl for standard reasoning, with incremental reasoning support.
"""

import hashlib
import logging
import time
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL

from owlrl import DeductiveClosure, OWLRL_Semantics, RDFS_Semantics

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from phase0.namespace import NamespaceManager

logger = logging.getLogger(__name__)

# Reasoning level constants
RDFS = "rdfs"
OWL_LITE = "owl_lite"
OWL_RL = "owl_rl"


class DomainKitReasoner:
    """
    OWL reasoner for domain-kit knowledge graph.
    
    Supports three reasoning levels:
    - rdfs: Class hierarchy, property inheritance (fast)
    - owl_lite: Simple constraints, cardinality (medium)
    - owl_rl: Full OWL RL rule reasoning (slow)
    
    Usage:
        reasoner = DomainKitReasoner(reasoning_level="rdfs")
        reasoner.load_ontology("ontology.ttl")
        reasoner.load_data_from_graph(data_graph)
        reasoner.reason()
        results = reasoner.query("SELECT ?s ?p ?o WHERE {...}")
    """

    def __init__(self, reasoning_level: str = "rdfs"):
        """
        Initialize reasoner.
        
        Args:
            reasoning_level: "rdfs" | "owl_lite" | "owl_rl"
        """
        if reasoning_level not in (RDFS, OWL_LITE, OWL_RL):
            raise ValueError(f"Invalid reasoning level: {reasoning_level}. Use 'rdfs', 'owl_lite', or 'owl_rl'")
        
        self.level = reasoning_level
        self.ns = NamespaceManager()
        
        # Graphs
        self.ontology_graph = Graph()  # TBox (ontology/schema)
        self.data_graph = Graph()      # ABox (instance data)
        self.inferred_graph = Graph()  # Inferred triples
        
        # State
        self._reasoned = False
        self._reasoning_time_ms = 0.0
        self._triple_count_before = 0
        self._triple_count_after = 0
        
        # Cache
        self._cache: Dict[str, Any] = {}

    def load_ontology(self, ontology_path: str, format: str = "turtle") -> None:
        """Load ontology definition (TBox)."""
        self.ontology_graph.parse(ontology_path, format=format)
        self.ns.bind_to_graph(self.ontology_graph)
        logger.info(f"Loaded ontology from {ontology_path} ({len(self.ontology_graph)} triples)")

    def load_ontology_from_string(self, turtle_str: str) -> None:
        """Load ontology from a Turtle string."""
        self.ontology_graph.parse(data=turtle_str, format="turtle")
        self.ns.bind_to_graph(self.ontology_graph)

    def load_data(self, data_graph: Graph) -> None:
        """Load instance data (ABox)."""
        self.data_graph = data_graph
        self.ns.bind_to_graph(self.data_graph)
        self._reasoned = False
        logger.info(f"Loaded data graph ({len(self.data_graph)} triples)")

    def load_data_from_jsonl(self, entities_path: str, relations_path: str) -> Graph:
        """Load data from JSONL files via Phase 1 converter."""
        from phase1.jsonl_to_rdf import JsonlToRdfConverter
        converter = JsonlToRdfConverter(self.ns)
        graph = converter.convert(entities_path, relations_path)
        self.load_data(graph)
        return graph

    def reason(self, incremental: bool = False) -> Graph:
        """
        Execute reasoning.
        
        Args:
            incremental: If True, only process new triples since last run
            
        Returns:
            Graph with inferred triples added
        """
        start_time = time.time()

        # Build combined graph
        combined = Graph()
        self.ns.bind_to_graph(combined)
        for t in self.ontology_graph:
            combined.add(t)
        for t in self.data_graph:
            combined.add(t)
        if incremental and self._reasoned:
            for t in self.inferred_graph:
                combined.add(t)

        self._triple_count_before = len(combined)

        # Select semantics class based on level
        if self.level == RDFS:
            closure_cls = RDFS_Semantics
        else:
            # owl_lite and owl_rl both use OWL RL semantics
            closure_cls = OWLRL_Semantics

        # Run reasoning
        try:
            DeductiveClosure(
                closure_cls,
                axiomatic_triples=False,
                datatype_axioms=False,
            ).expand(combined)
        except Exception as e:
            logger.error(f"Reasoning failed: {e}")
            # Fall back to RDFS
            if self.level != RDFS:
                logger.info("Falling back to RDFS reasoning")
                combined2 = Graph()
                self.ns.bind_to_graph(combined2)
                for t in self.ontology_graph:
                    combined2.add(t)
                for t in self.data_graph:
                    combined2.add(t)
                DeductiveClosure(
                    RDFS_Semantics,
                    axiomatic_triples=False,
                    datatype_axioms=False,
                ).expand(combined2)
                combined = combined2

        self._triple_count_after = len(combined)
        self._reasoning_time_ms = (time.time() - start_time) * 1000

        # Store inferred triples (those not in original data)
        self.inferred_graph = Graph()
        self.ns.bind_to_graph(self.inferred_graph)
        original_subjects = set(self.data_graph.subjects())
        for t in combined:
            if t not in self.data_graph and t not in self.ontology_graph:
                self.inferred_graph.add(t)

        self._reasoned = True
        logger.info(
            f"Reasoning complete ({self.level}): "
            f"{self._triple_count_before} -> {self._triple_count_after} triples "
            f"({self._triple_count_after - self._triple_count_before} inferred) "
            f"in {self._reasoning_time_ms:.1f}ms"
        )

        return combined

    def get_inferred_triples(self) -> List[Tuple]:
        """Get all inferred triples."""
        return list(self.inferred_graph)

    def get_reasoning_stats(self) -> Dict[str, Any]:
        """Get reasoning statistics."""
        return {
            "level": self.level,
            "reasoned": self._reasoned,
            "triples_before": self._triple_count_before,
            "triples_after": self._triple_count_after,
            "triples_inferred": self._triple_count_after - self._triple_count_before,
            "reasoning_time_ms": self._reasoning_time_ms,
        }

    def query(self, sparql: str) -> Any:
        """
        Execute SPARQL query against the reasoned graph.
        
        Returns:
            rdflib query result
        """
        combined = Graph()
        for t in self.ontology_graph:
            combined.add(t)
        for t in self.data_graph:
            combined.add(t)
        for t in self.inferred_graph:
            combined.add(t)
        return combined.query(sparql)

    def get_combined_graph(self) -> Graph:
        """Get the combined graph (ontology + data + inferred)."""
        combined = Graph()
        self.ns.bind_to_graph(combined)
        for t in self.ontology_graph:
            combined.add(t)
        for t in self.data_graph:
            combined.add(t)
        for t in self.inferred_graph:
            combined.add(t)
        return combined

    def find_implied_relations(self, entity_id: str) -> List[Dict[str, str]]:
        """Find all relations implied for an entity after reasoning."""
        entity_uri = self.ns.entity_uri(entity_id)
        results = []
        
        combined = self.get_combined_graph()
        for s, p, o in combined.triples((entity_uri, None, None)):
            if str(p).startswith(str(self.ns.relation_ns)):
                results.append({
                    "from": entity_id,
                    "relation": str(p).split("/")[-1],
                    "to": str(o).split("/")[-1],
                    "inferred": (s, p, o) in self.inferred_graph,
                })
        for s, p, o in combined.triples((None, None, entity_uri)):
            if str(p).startswith(str(self.ns.relation_ns)):
                results.append({
                    "from": str(s).split("/")[-1],
                    "relation": str(p).split("/")[-1],
                    "to": entity_id,
                    "inferred": (s, p, o) in self.inferred_graph,
                })
        return results


class IncrementalReasoner:
    """
    Incremental reasoner that avoids full re-reasoning on small changes.
    
    Tracks file hashes and only re-reasons when data changes.
    """

    def __init__(self, base_reasoner: DomainKitReasoner):
        self.base = base_reasoner
        self._last_hash: Optional[str] = None
        self._last_combined_graph: Optional[Graph] = None

    def compute_hash(self, *file_paths: str) -> str:
        """Compute a hash of the input files."""
        hasher = hashlib.md5()
        for path in sorted(file_paths):
            try:
                with open(path, "rb") as f:
                    for chunk in iter(lambda: f.read(8192), b""):
                        hasher.update(chunk)
            except FileNotFoundError:
                pass
        return hasher.hexdigest()

    def has_changed(self, *file_paths: str) -> bool:
        """Check if any input file has changed since last reasoning."""
        current_hash = self.compute_hash(*file_paths)
        if current_hash != self._last_hash:
            return True
        return False

    def incremental_reason(self, entities_path: str, relations_path: str) -> Graph:
        """
        Perform incremental reasoning.
        
        Only re-reasons if files have changed since last run.
        """
        if self._last_hash is not None and not self.has_changed(entities_path, relations_path):
            logger.info("No changes detected, skipping reasoning")
            return self.base.get_combined_graph()

        # Full reload and reason
        self.base.load_data_from_jsonl(entities_path, relations_path)
        result = self.base.reason()
        
        self._last_hash = self.compute_hash(entities_path, relations_path)
        self._last_combined_graph = result
        return result

    def force_reason(self, entities_path: str, relations_path: str) -> Graph:
        """Force full reasoning regardless of changes."""
        self._last_hash = None
        return self.incremental_reason(entities_path, relations_path)
