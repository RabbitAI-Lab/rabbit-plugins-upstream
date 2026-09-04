"""
Namespace Manager.

Manages RDF namespace prefixes and URI generation for the domain-kit ontology.
Ensures consistent URI patterns across all phases.
"""

from typing import Dict, Optional
from rdflib import Namespace, URIRef, Graph
from rdflib.namespace import RDF, RDFS, OWL, XSD, SKOS


# Base URI for domain-kit ontology
DOMAIN_KIT_BASE = "https://domain-kit.midea.com/ontology/"

# Custom namespace for domain-kit entities and relations
DK = Namespace(DOMAIN_KIT_BASE)
DK_ENTITY = Namespace(f"{DOMAIN_KIT_BASE}entity/")
DK_REL = Namespace(f"{DOMAIN_KIT_BASE}relation/")
DK_PROP = Namespace(f"{DOMAIN_KIT_BASE}property/")
DK_CLASS = Namespace(f"{DOMAIN_KIT_BASE}class/")


class NamespaceManager:
    """
    Manages RDF namespaces and URI generation.
    
    Provides:
    - Consistent namespace prefix binding
    - URI generation for entities, relations, and classes
    - Prefix resolution
    """

    def __init__(self, base_uri: str = DOMAIN_KIT_BASE):
        self.base_uri = base_uri
        self.dk = Namespace(base_uri)
        self.entity_ns = Namespace(f"{base_uri}entity/")
        self.relation_ns = Namespace(f"{base_uri}relation/")
        self.prop_ns = Namespace(f"{base_uri}property/")
        self.class_ns = Namespace(f"{base_uri}class/")

        # Standard namespace bindings
        self._bindings: Dict[str, Namespace] = {
            "dk": self.dk,
            "dk-entity": self.entity_ns,
            "dk-rel": self.relation_ns,
            "dk-prop": self.prop_ns,
            "dk-class": self.class_ns,
            "rdf": RDF,
            "rdfs": RDFS,
            "owl": OWL,
            "xsd": XSD,
            "skos": SKOS,
        }

    def bind_to_graph(self, graph: Graph) -> None:
        """Bind all namespaces to an RDF graph."""
        for prefix, ns in self._bindings.items():
            graph.bind(prefix, ns)

    def entity_uri(self, entity_id: str) -> URIRef:
        """Generate URI for an entity."""
        return URIRef(f"{self.entity_ns}{entity_id}")

    def class_uri(self, class_name: str) -> URIRef:
        """Generate URI for an entity class/type."""
        return URIRef(f"{self.class_ns}{class_name}")

    def relation_uri(self, relation_type: str) -> URIRef:
        """Generate URI for a relation type."""
        return URIRef(f"{self.relation_ns}{relation_type}")

    def property_uri(self, property_name: str) -> URIRef:
        """Generate URI for a property."""
        return URIRef(f"{self.prop_ns}{property_name}")

    def get_prefix(self, uri: str) -> Optional[str]:
        """Find the prefix for a given URI."""
        for prefix, ns in self._bindings.items():
            if uri.startswith(str(ns)):
                return prefix
        return None

    def compact_uri(self, uri: str) -> str:
        """Convert a full URI to compact (prefixed) form."""
        # Sort by namespace length (longest first) to avoid partial matches
        sorted_bindings = sorted(
            self._bindings.items(),
            key=lambda x: len(str(x[1])),
            reverse=True,
        )
        for prefix, ns in sorted_bindings:
            ns_str = str(ns)
            if uri.startswith(ns_str):
                local = uri[len(ns_str):]
                return f"{prefix}:{local}"
        return uri

    def get_all_bindings(self) -> Dict[str, str]:
        """Return all prefix -> namespace URI mappings."""
        return {prefix: str(ns) for prefix, ns in self._bindings.items()}

    def add_custom_namespace(self, prefix: str, uri: str) -> None:
        """Register a custom namespace."""
        self._bindings[prefix] = Namespace(uri)
