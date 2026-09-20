"""
Hybrid Query Engine.

Combines natural language -> SPARQL conversion with keyword-based fallback.
Provides a unified query interface that tries semantic search first,
then falls back to keyword matching.
"""

import re
import logging
from typing import Any, Dict, List, Optional, Tuple

from rdflib import Graph

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from phase0.namespace import NamespaceManager
from phase2.reasoner import DomainKitReasoner
from phase4.query_engine import SPARQLQueryEngine, QueryResult

logger = logging.getLogger(__name__)


# Pattern -> SPARQL template mapping for rule-based NL->SPARQL
NL_PATTERNS = [
    {
        "pattern": r"(?:找|查|搜索|查找|有哪些|有什么).*(?:设备|装置|机器)",
        "intent": "find_devices",
        "extract": lambda q: _extract_name(q),
    },
    {
        "pattern": r"(?:找|查|搜索).*(?:模板|代码|程序)",
        "intent": "find_templates",
        "extract": lambda q: _extract_name(q),
    },
    {
        "pattern": r"(?:找|查).*(?:约束|限制|规范)",
        "intent": "find_constraints",
        "extract": lambda q: _extract_name(q),
    },
    {
        "pattern": r"(?:兼容|支持).*(?:协议|通讯|通信)",
        "intent": "find_compatible",
        "extract": lambda q: _extract_protocol(q),
    },
    {
        "pattern": r"(?:依赖|需要|使用).*(?:设备|PLC)",
        "intent": "find_dependencies",
        "extract": lambda q: _extract_name(q),
    },
    {
        "pattern": r"(?:关系|关联|连接).*",
        "intent": "find_relations",
        "extract": lambda q: _extract_entity_id(q),
    },
    {
        "pattern": r"(?:统计|数量|多少|总数)",
        "intent": "statistics",
        "extract": lambda q: None,
    },
    {
        "pattern": r"(?:类型|种类|分类)",
        "intent": "list_types",
        "extract": lambda q: None,
    },
]


def _extract_name(query: str) -> Optional[str]:
    """Extract entity name from natural language query."""
    # Look for quoted strings
    match = re.search(r'["\']([^"\']+)["\']', query)
    if match:
        return match.group(1)
    # Look for common patterns like "关于AM600", "叫做X"
    match = re.search(r'(?:关于|叫做|名为|叫)\s*(\S+)', query)
    if match:
        return match.group(1)
    # Look for alphanumeric identifiers (e.g., AM600, H5U)
    # Use lookahead/lookbehind for Chinese char boundaries
    match = re.search(r'([A-Za-z]{2,}\d{1,}[A-Za-z0-9]*)', query)
    if match:
        return match.group(1)
    # Try pure uppercase+digit patterns
    match = re.search(r'([A-Z]+\d+)', query)
    if match:
        return match.group(1)
    return None


def _extract_protocol(query: str) -> Optional[str]:
    """Extract protocol name from query."""
    protocols = ["Modbus", "OPC", "OPC-UA", "EtherCAT", "Profinet", "EtherNet/IP",
                 "CANopen", "MQTT", "HTTP", "TCP", "UDP"]
    for p in protocols:
        if p.lower() in query.lower():
            return p
    return None


def _extract_entity_id(query: str) -> Optional[str]:
    """Extract entity ID from query."""
    # Look for hex IDs
    match = re.search(r'\b([0-9a-f]{32})\b', query)
    if match:
        return match.group(1)
    return None


class HybridQueryEngine:
    """
    Hybrid query engine combining NL->SPARQL with keyword fallback.
    
    Query resolution order:
    1. Pattern matching (rule-based NL -> SPARQL)
    2. SPARQL query (if pattern matched and generated valid SPARQL)
    3. Keyword fallback (search through graph labels/tags)
    
    Usage:
        engine = HybridQueryEngine(reasoner, jsonl_store)
        result = engine.query("查找所有PLC设备")
    """

    def __init__(self, reasoner: Optional[DomainKitReasoner] = None,
                 query_engine: Optional[SPARQLQueryEngine] = None,
                 ns_manager: Optional[NamespaceManager] = None):
        self.ns = ns_manager or NamespaceManager()
        self.reasoner = reasoner
        self.query_engine = query_engine or SPARQLQueryEngine(ns_manager=self.ns)
        self._query_log: List[Dict[str, Any]] = []

    def set_graph(self, graph: Graph) -> None:
        """Update the underlying graph for queries."""
        self.query_engine.set_graph(graph)

    def query(self, natural_language_query: str) -> Dict[str, Any]:
        """
        Process a natural language query.
        
        Args:
            natural_language_query: Query in natural language
            
        Returns:
            Dict with keys: success, method, results, query_used
        """
        # Step 1: Try pattern-based NL -> SPARQL
        intent, extracted = self._classify_intent(natural_language_query)
        
        if intent:
            sparql = self._intent_to_sparql(intent, extracted)
            if sparql:
                result = self.query_engine.execute(sparql)
                if result.success and result.row_count > 0:
                    self._log_query(natural_language_query, "sparql", intent, result)
                    return {
                        "success": True,
                        "method": "sparql",
                        "intent": intent,
                        "results": result.to_dicts(),
                        "query_used": sparql,
                        "execution_time_ms": result.execution_time_ms,
                        "row_count": result.row_count,
                    }

        # Step 2: Keyword fallback
        keyword_results = self._keyword_search(natural_language_query)
        if keyword_results:
            self._log_query(natural_language_query, "keyword", intent, None)
            return {
                "success": True,
                "method": "keyword",
                "intent": intent,
                "results": keyword_results,
                "query_used": natural_language_query,
                "execution_time_ms": 0,
                "row_count": len(keyword_results),
            }

        # Step 3: No results
        self._log_query(natural_language_query, "none", intent, None)
        return {
            "success": False,
            "method": "none",
            "intent": intent,
            "results": [],
            "query_used": natural_language_query,
            "execution_time_ms": 0,
            "row_count": 0,
            "message": "未找到匹配结果",
        }

    def _classify_intent(self, query: str) -> Tuple[Optional[str], Optional[str]]:
        """Classify the query intent using pattern matching."""
        for entry in NL_PATTERNS:
            if re.search(entry["pattern"], query):
                extracted = entry["extract"](query)
                return entry["intent"], extracted
        return None, None

    def _intent_to_sparql(self, intent: str, extracted: Optional[str]) -> Optional[str]:
        """Convert classified intent to SPARQL query."""
        ns = self.ns

        if intent == "find_devices" and extracted:
            return f"""
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX dk-class: <{ns.class_ns}>
                
                SELECT ?entity ?name ?description WHERE {{
                    ?entity rdf:type dk-class:Device .
                    ?entity rdfs:label ?name .
                    OPTIONAL {{ ?entity rdfs:comment ?description }}
                    FILTER(CONTAINS(LCASE(?name), LCASE("{extracted}")))
                }} LIMIT 50
            """
        elif intent == "find_devices":
            return f"""
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX dk-class: <{ns.class_ns}>
                
                SELECT ?entity ?name ?description WHERE {{
                    ?entity rdf:type dk-class:Device .
                    ?entity rdfs:label ?name .
                    OPTIONAL {{ ?entity rdfs:comment ?description }}
                }} LIMIT 50
            """
        elif intent == "find_templates" and extracted:
            return f"""
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX dk-class: <{ns.class_ns}>
                
                SELECT ?entity ?name ?description WHERE {{
                    ?entity rdf:type dk-class:CodeTemplate .
                    ?entity rdfs:label ?name .
                    OPTIONAL {{ ?entity rdfs:comment ?description }}
                    FILTER(CONTAINS(LCASE(?name), LCASE("{extracted}")))
                }} LIMIT 50
            """
        elif intent == "find_templates":
            return f"""
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX dk-class: <{ns.class_ns}>
                
                SELECT ?entity ?name ?description WHERE {{
                    ?entity rdf:type dk-class:CodeTemplate .
                    ?entity rdfs:label ?name .
                    OPTIONAL {{ ?entity rdfs:comment ?description }}
                }} LIMIT 50
            """
        elif intent == "find_constraints" and extracted:
            return f"""
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX dk-class: <{ns.class_ns}>
                
                SELECT ?entity ?name ?description WHERE {{
                    ?entity rdf:type dk-class:Constraint .
                    ?entity rdfs:label ?name .
                    OPTIONAL {{ ?entity rdfs:comment ?description }}
                    FILTER(CONTAINS(LCASE(?name), LCASE("{extracted}")))
                }} LIMIT 50
            """
        elif intent == "statistics":
            return """
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                SELECT (COUNT(DISTINCT ?s) AS ?entities) (COUNT(?s) AS ?triples) WHERE {
                    ?s ?p ?o .
                }
            """
        elif intent == "list_types":
            return """
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                SELECT ?type ?type_name (COUNT(?entity) AS ?count) WHERE {
                    ?entity rdf:type ?type .
                    ?type rdfs:label ?type_name .
                    FILTER(?type != <http://www.w3.org/2002/07/owl#Ontology>)
                    FILTER(?type != <http://www.w3.org/2002/07/owl#Class>)
                } GROUP BY ?type ?type_name ORDER BY DESC(?count)
            """

        return None

    def _keyword_search(self, query: str) -> List[Dict[str, str]]:
        """Fallback keyword search through graph labels and tags."""
        from rdflib.namespace import RDFS, SKOS, RDF
        
        results = []
        query_lower = query.lower()
        # Extract meaningful keywords (skip common words)
        stop_words = {"找", "查", "搜索", "查找", "有哪些", "有什么", "的", "了", "是",
                      "在", "和", "与", "有", "哪些", "什么", "怎么", "如何", "请", "帮"}
        keywords = [w for w in query if w not in stop_words and w.strip()]
        if not keywords:
            keywords = list(query)

        # Search through all labeled resources
        seen = set()
        for s, p, o in self.query_engine.graph.triples((None, RDFS.label, None)):
            label = str(o).lower()
            if any(kw.lower() in label for kw in keywords if len(kw) > 0):
                if str(s) not in seen:
                    seen.add(str(s))
                    # Get type
                    entity_type = ""
                    for _, _, t in self.query_engine.graph.triples((s, RDF.type, None)):
                        if isinstance(t, str) and "class/" in str(t):
                            entity_type = str(t).split("/")[-1]
                        elif hasattr(t, '__str__') and "class/" in str(t):
                            entity_type = str(t).split("/")[-1]
                    results.append({
                        "entity": str(s),
                        "name": str(o),
                        "type": entity_type,
                    })

        # Also search tags
        for s, p, o in self.query_engine.graph.triples((None, SKOS.altLabel, None)):
            tag = str(o).lower()
            if any(kw.lower() in tag for kw in keywords if len(kw) > 0):
                if str(s) not in seen:
                    seen.add(str(s))
                    # Get label
                    name = ""
                    for _, _, l in self.query_engine.graph.triples((s, RDFS.label, None)):
                        name = str(l)
                        break
                    results.append({
                        "entity": str(s),
                        "name": name or tag,
                        "type": "tagged",
                    })

        return results[:50]

    def _log_query(self, query: str, method: str, intent: Optional[str],
                   result: Optional[QueryResult]) -> None:
        """Log query execution."""
        self._query_log.append({
            "query": query,
            "method": method,
            "intent": intent,
            "success": result.success if result else method == "keyword",
            "row_count": result.row_count if result else 0,
        })

    def get_query_log(self) -> List[Dict[str, Any]]:
        """Get the query execution log."""
        return self._query_log

    def get_accuracy_stats(self) -> Dict[str, Any]:
        """Get accuracy statistics from logged queries."""
        if not self._query_log:
            return {"total": 0, "accuracy": 0.0}
        successful = sum(1 for q in self._query_log if q["success"])
        return {
            "total": len(self._query_log),
            "successful": successful,
            "accuracy": successful / len(self._query_log),
            "by_method": {
                "sparql": sum(1 for q in self._query_log if q["method"] == "sparql"),
                "keyword": sum(1 for q in self._query_log if q["method"] == "keyword"),
                "none": sum(1 for q in self._query_log if q["method"] == "none"),
            },
        }
