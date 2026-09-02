"""
Protégé-compatible export module.

Exports the domain-kit knowledge graph in formats compatible with Protégé:
- Turtle (.ttl) - recommended
- RDF/XML (.rdf)
- N-Triples (.nt)
"""

import logging
from pathlib import Path
from typing import Optional

from rdflib import Graph

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from phase0.namespace import NamespaceManager

logger = logging.getLogger(__name__)


class ProtegeExporter:
    """
    Export knowledge graph in Protégé-compatible formats.
    
    Usage:
        exporter = ProtegeExporter(graph)
        exporter.export_turtle("output.ttl")
        exporter.export_rdfxml("output.rdf")
    """

    SUPPORTED_FORMATS = {
        "turtle": ".ttl",
        "xml": ".rdf",
        "pretty-xml": ".rdf",
        "n3": ".n3",
        "nt": ".nt",
        "ntriples": ".nt",
    }

    def __init__(self, graph: Optional[Graph] = None,
                 ns_manager: Optional[NamespaceManager] = None):
        self.graph = graph or Graph()
        self.ns = ns_manager or NamespaceManager()
        self.ns.bind_to_graph(self.graph)

    def set_graph(self, graph: Graph) -> None:
        """Update the graph to export."""
        self.graph = graph
        self.ns.bind_to_graph(graph)

    def export(self, output_path: str, format: str = "turtle") -> str:
        """
        Export graph to file.
        
        Args:
            output_path: Output file path
            format: Serialization format (turtle, xml, pretty-xml, n3, nt)
            
        Returns:
            Path to the exported file
        """
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        self.graph.serialize(destination=str(path), format=format)
        logger.info(f"Exported graph to {path} ({format}, {len(self.graph)} triples)")
        return str(path)

    def export_turtle(self, output_path: str) -> str:
        """Export as Turtle (.ttl) - recommended for Protégé."""
        if not output_path.endswith(".ttl"):
            output_path += ".ttl"
        return self.export(output_path, format="turtle")

    def export_rdfxml(self, output_path: str) -> str:
        """Export as RDF/XML (.rdf)."""
        if not output_path.endswith(".rdf"):
            output_path += ".rdf"
        return self.export(output_path, format="pretty-xml")

    def export_ntriples(self, output_path: str) -> str:
        """Export as N-Triples (.nt)."""
        if not output_path.endswith(".nt"):
            output_path += ".nt"
        return self.export(output_path, format="nt")

    def to_turtle_string(self) -> str:
        """Export graph as Turtle string."""
        return self.graph.serialize(format="turtle")

    def get_graph_summary(self) -> dict:
        """Get a summary of the graph contents."""
        from rdflib.namespace import RDF, RDFS
        from rdflib import URIRef

        class_counts = {}
        for s, p, o in self.graph.triples((None, RDF.type, None)):
            if isinstance(o, URIRef):
                class_name = str(o).split("/")[-1].split("#")[-1]
                class_counts[class_name] = class_counts.get(class_name, 0) + 1

        return {
            "total_triples": len(self.graph),
            "unique_subjects": len(set(self.graph.subjects())),
            "unique_predicates": len(set(self.graph.predicates())),
            "unique_objects": len(set(self.graph.objects())),
            "class_counts": class_counts,
        }
