"""
SPARQL Query Engine.

Provides a high-level interface for executing SPARQL queries
against the domain-kit knowledge graph, with pre-built query templates.
"""

import time
import logging
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL, SKOS

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from phase0.namespace import NamespaceManager

logger = logging.getLogger(__name__)


@dataclass
class QueryResult:
    """Structured query result."""
    success: bool
    query: str
    bindings: List[Dict[str, str]] = field(default_factory=list)
    execution_time_ms: float = 0.0
    error: Optional[str] = None
    row_count: int = 0

    def to_dicts(self) -> List[Dict[str, str]]:
        """Return results as list of dicts."""
        return self.bindings

    def __len__(self):
        return self.row_count

    def __bool__(self):
        return self.success and self.row_count > 0


@dataclass
class QueryTemplate:
    """A pre-built SPARQL query template with parameter substitution."""
    name: str
    description: str
    sparql_template: str
    parameters: List[str] = field(default_factory=list)
    category: str = "general"

    def render(self, **kwargs) -> str:
        """Render the template with parameter values."""
        result = self.sparql_template
        for param in self.parameters:
            if param in kwargs:
                result = result.replace(f"${{{param}}}", str(kwargs[param]))
        return result


# Pre-built query templates
BUILTIN_TEMPLATES = [
    QueryTemplate(
        name="find_entity_by_name",
        description="Find entities by name (partial match)",
        sparql_template="""
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX dk-class: <https://domain-kit.midea.com/ontology/class/>
            
            SELECT ?entity ?type ?name ?description WHERE {
                ?entity rdf:type ?type .
                ?entity rdfs:label ?name .
                OPTIONAL { ?entity rdfs:comment ?description }
                FILTER(CONTAINS(LCASE(?name), LCASE("${name}")))
            }
            LIMIT ${limit}
        """,
        parameters=["name", "limit"],
        category="entity",
    ),
    QueryTemplate(
        name="find_entity_by_type",
        description="Find all entities of a given type",
        sparql_template="""
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX dk-class: <https://domain-kit.midea.com/ontology/class/>
            
            SELECT ?entity ?name ?description WHERE {
                ?entity rdf:type dk-class:${type} .
                ?entity rdfs:label ?name .
                OPTIONAL { ?entity rdfs:comment ?description }
            }
            LIMIT ${limit}
        """,
        parameters=["type", "limit"],
        category="entity",
    ),
    QueryTemplate(
        name="find_relations",
        description="Find all relations for a given entity",
        sparql_template="""
            PREFIX dk-entity: <https://domain-kit.midea.com/ontology/entity/>
            PREFIX dk-rel: <https://domain-kit.midea.com/ontology/relation/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            
            SELECT ?relation ?target ?target_name WHERE {
                { dk-entity:${entity_id} ?relation ?target . }
                UNION
                { ?target ?relation dk-entity:${entity_id} . }
                FILTER(STRSTARTS(STR(?relation), "https://domain-kit.midea.com/ontology/relation/"))
                OPTIONAL { ?target rdfs:label ?target_name }
            }
        """,
        parameters=["entity_id"],
        category="relation",
    ),
    QueryTemplate(
        name="find_compatible_devices",
        description="Find devices compatible with a given protocol",
        sparql_template="""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dk-class: <https://domain-kit.midea.com/ontology/class/>
            PREFIX dk-rel: <https://domain-kit.midea.com/ontology/relation/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            
            SELECT ?device ?device_name WHERE {
                ?device rdf:type dk-class:Device .
                ?device dk-rel:compatible_with ?protocol .
                ?device rdfs:label ?device_name .
                ?protocol skos:altLabel ?tag .
                FILTER(CONTAINS(LCASE(?tag), LCASE("${protocol_name}")))
            }
        """,
        parameters=["protocol_name"],
        category="device",
    ),
    QueryTemplate(
        name="find_templates_for_device",
        description="Find code templates that depend on a device",
        sparql_template="""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dk-class: <https://domain-kit.midea.com/ontology/class/>
            PREFIX dk-entity: <https://domain-kit.midea.com/ontology/entity/>
            PREFIX dk-rel: <https://domain-kit.midea.com/ontology/relation/>
            
            SELECT ?template ?template_name ?description WHERE {
                ?template rdf:type dk-class:CodeTemplate .
                ?template dk-rel:depends_on dk-entity:${device_id} .
                ?template rdfs:label ?template_name .
                OPTIONAL { ?template rdfs:comment ?description }
            }
        """,
        parameters=["device_id"],
        category="template",
    ),
    QueryTemplate(
        name="find_constraints_for_device",
        description="Find constraints applicable to a device",
        sparql_template="""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dk-class: <https://domain-kit.midea.com/ontology/class/>
            PREFIX dk-entity: <https://domain-kit.midea.com/ontology/entity/>
            PREFIX dk-rel: <https://domain-kit.midea.com/ontology/relation/>
            
            SELECT ?constraint ?constraint_name ?description WHERE {
                ?constraint rdf:type dk-class:Constraint .
                ?constraint dk-rel:applies_to dk-entity:${device_id} .
                ?constraint rdfs:label ?constraint_name .
                OPTIONAL { ?constraint rdfs:comment ?description }
            }
        """,
        parameters=["device_id"],
        category="constraint",
    ),
    QueryTemplate(
        name="list_all_types",
        description="List all entity types and their counts",
        sparql_template="""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            
            SELECT ?type ?type_name (COUNT(?entity) AS ?count) WHERE {
                ?entity rdf:type ?type .
                ?type rdfs:label ?type_name .
                FILTER(?type != <http://www.w3.org/2002/07/owl#Ontology>)
                FILTER(?type != <http://www.w3.org/2002/07/owl#Class>)
            }
            GROUP BY ?type ?type_name
            ORDER BY DESC(?count)
        """,
        parameters=[],
        category="stats",
    ),
    QueryTemplate(
        name="graph_statistics",
        description="Get graph statistics",
        sparql_template="""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            
            SELECT (COUNT(DISTINCT ?s) AS ?entities) (COUNT(DISTINCT ?p) AS ?predicates) (COUNT(?s) AS ?triples) WHERE {
                ?s ?p ?o .
            }
        """,
        parameters=[],
        category="stats",
    ),
]


class SPARQLQueryEngine:
    """
    SPARQL query engine for domain-kit.
    
    Provides:
    - Direct SPARQL query execution
    - Pre-built query templates
    - Performance monitoring
    - Result formatting
    
    Usage:
        engine = SPARQLQueryEngine(graph)
        result = engine.execute("SELECT ?s WHERE { ?s ?p ?o } LIMIT 10")
        result = engine.execute_template("find_entity_by_name", name="AM600", limit="10")
    """

    def __init__(self, graph: Optional[Graph] = None,
                 ns_manager: Optional[NamespaceManager] = None):
        self.graph = graph or Graph()
        self.ns = ns_manager or NamespaceManager()
        self.ns.bind_to_graph(self.graph)
        
        # Query templates
        self._templates: Dict[str, QueryTemplate] = {}
        for tmpl in BUILTIN_TEMPLATES:
            self._templates[tmpl.name] = tmpl
        
        # Performance tracking
        self._query_count = 0
        self._total_time_ms = 0.0

    def set_graph(self, graph: Graph) -> None:
        """Update the query graph."""
        self.graph = graph
        self.ns.bind_to_graph(graph)

    def execute(self, sparql: str) -> QueryResult:
        """
        Execute a SPARQL query.
        
        Args:
            sparql: SPARQL query string
            
        Returns:
            QueryResult with bindings and metadata
        """
        start = time.time()
        self._query_count += 1

        try:
            results = self.graph.query(sparql)
            elapsed = (time.time() - start) * 1000
            self._total_time_ms += elapsed

            bindings = []
            if results.vars:
                var_names = [str(v) for v in results.vars]
                for row in results:
                    binding = {}
                    for var_name, val in zip(var_names, row):
                        binding[var_name] = str(val) if val is not None else ""
                    bindings.append(binding)

            return QueryResult(
                success=True,
                query=sparql,
                bindings=bindings,
                execution_time_ms=elapsed,
                row_count=len(bindings),
            )

        except Exception as e:
            elapsed = (time.time() - start) * 1000
            self._total_time_ms += elapsed
            logger.error(f"SPARQL query failed: {e}")
            return QueryResult(
                success=False,
                query=sparql,
                error=str(e),
                execution_time_ms=elapsed,
            )

    def execute_template(self, template_name: str, **kwargs) -> QueryResult:
        """
        Execute a pre-built query template.
        
        Args:
            template_name: Name of the template
            **kwargs: Template parameter values
            
        Returns:
            QueryResult
        """
        template = self._templates.get(template_name)
        if template is None:
            return QueryResult(
                success=False,
                query="",
                error=f"Unknown template: {template_name}",
            )

        # Set default limit
        if "limit" not in kwargs:
            kwargs["limit"] = "50"

        sparql = template.render(**kwargs)
        return self.execute(sparql)

    def register_template(self, template: QueryTemplate) -> None:
        """Register a custom query template."""
        self._templates[template.name] = template

    def list_templates(self) -> List[Dict[str, str]]:
        """List all available query templates."""
        return [
            {
                "name": t.name,
                "description": t.description,
                "category": t.category,
                "parameters": ", ".join(t.parameters),
            }
            for t in self._templates.values()
        ]

    def get_performance_stats(self) -> Dict[str, Any]:
        """Get query performance statistics."""
        avg_ms = self._total_time_ms / max(self._query_count, 1)
        return {
            "total_queries": self._query_count,
            "total_time_ms": round(self._total_time_ms, 2),
            "average_time_ms": round(avg_ms, 2),
        }

    def find_entities(self, name_filter: str = "", entity_type: str = "",
                      limit: int = 50) -> QueryResult:
        """High-level entity search."""
        if entity_type:
            return self.execute_template("find_entity_by_type", type=entity_type, limit=str(limit))
        elif name_filter:
            return self.execute_template("find_entity_by_name", name=name_filter, limit=str(limit))
        else:
            return self.execute_template("list_all_types")

    def find_relations_for_entity(self, entity_id: str) -> QueryResult:
        """Find all relations involving an entity."""
        return self.execute_template("find_relations", entity_id=entity_id)

    def get_statistics(self) -> QueryResult:
        """Get graph statistics."""
        return self.execute_template("graph_statistics")
