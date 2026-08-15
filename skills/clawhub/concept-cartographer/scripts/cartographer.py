#!/usr/bin/env python3
"""
Concept Cartographer — prerequisite mapping for learning any topic.

Subcommands:
  map        — show the full prerequisite map for a topic
  path       — generate a personalized learning path given known concepts
  audit      — identify knowledge gaps for a target topic
  visualize  — export concept map as Mermaid or text tree
  topics     — list all topics in the knowledge base

Usage:
  python cartographer.py map "machine learning"
  python cartographer.py path "machine learning" --known "python,statistics"
  python cartographer.py audit "deep learning" --known "python,linear-algebra"
  python cartographer.py visualize "machine learning" --format mermaid
  python cartographer.py topics
"""

import argparse
import json
import os
import sys
from collections import defaultdict, deque

# ---------------------------------------------------------------------------
# Built-in knowledge base (concept prerequisite DAG)
# ---------------------------------------------------------------------------

KNOWLEDGE_BASE = {
    # --- Programming ---
    "programming-basics": {
        "name": "Programming Basics",
        "description": "Variables, loops, conditionals, functions — the fundamentals of coding",
        "difficulty": "beginner",
        "hours": 20,
        "category": "Programming",
        "prerequisites": [],
    },
    "python": {
        "name": "Python",
        "description": "Python syntax, data types, standard library — the most popular language for ML and data",
        "difficulty": "beginner",
        "hours": 40,
        "category": "Programming",
        "prerequisites": ["programming-basics"],
    },
    "javascript": {
        "name": "JavaScript",
        "description": "Web's programming language — front-end interactivity and Node.js backends",
        "difficulty": "beginner",
        "hours": 40,
        "category": "Programming",
        "prerequisites": ["programming-basics"],
    },
    "data-structures": {
        "name": "Data Structures",
        "description": "Arrays, linked lists, trees, graphs, hash maps — organizing data efficiently",
        "difficulty": "intermediate",
        "hours": 30,
        "category": "Programming",
        "prerequisites": ["programming-basics"],
    },
    "algorithms": {
        "name": "Algorithms",
        "description": "Sorting, searching, dynamic programming, complexity analysis",
        "difficulty": "intermediate",
        "hours": 40,
        "category": "Programming",
        "prerequisites": ["data-structures"],
    },
    "sql": {
        "name": "SQL & Databases",
        "description": "Relational database queries, schema design, normalization",
        "difficulty": "beginner",
        "hours": 20,
        "category": "Programming",
        "prerequisites": ["programming-basics"],
    },

    # --- Math ---
    "basic-math": {
        "name": "Basic Mathematics",
        "description": "Arithmetic, fractions, exponents, basic algebra",
        "difficulty": "beginner",
        "hours": 15,
        "category": "Math",
        "prerequisites": [],
    },
    "algebra": {
        "name": "Algebra",
        "description": "Equations, polynomials, functions, graphs",
        "difficulty": "beginner",
        "hours": 30,
        "category": "Math",
        "prerequisites": ["basic-math"],
    },
    "calculus": {
        "name": "Calculus",
        "description": "Limits, derivatives, integrals — essential for understanding optimization and rates of change",
        "difficulty": "intermediate",
        "hours": 50,
        "category": "Math",
        "prerequisites": ["algebra"],
    },
    "linear-algebra": {
        "name": "Linear Algebra",
        "description": "Vectors, matrices, eigenvalues — the mathematical foundation of ML and graphics",
        "difficulty": "intermediate",
        "hours": 40,
        "category": "Math",
        "prerequisites": ["algebra"],
    },
    "discrete-math": {
        "name": "Discrete Mathematics",
        "description": "Logic, sets, combinatorics, graph theory — foundations for CS",
        "difficulty": "intermediate",
        "hours": 35,
        "category": "Math",
        "prerequisites": ["basic-math"],
    },
    "probability": {
        "name": "Probability Theory",
        "description": "Random variables, distributions, Bayes' theorem — uncertainty modeling",
        "difficulty": "intermediate",
        "hours": 35,
        "category": "Math",
        "prerequisites": ["calculus", "discrete-math"],
    },
    "statistics": {
        "name": "Statistics",
        "description": "Hypothesis testing, regression, Bayesian inference",
        "difficulty": "intermediate",
        "hours": 40,
        "category": "Math",
        "prerequisites": ["probability"],
    },

    # --- Machine Learning / AI ---
    "machine-learning": {
        "name": "Machine Learning",
        "description": "Supervised/unsupervised learning, model evaluation, feature engineering",
        "difficulty": "intermediate",
        "hours": 60,
        "category": "AI/ML",
        "prerequisites": ["python", "statistics", "linear-algebra"],
    },
    "neural-networks": {
        "name": "Neural Networks",
        "description": "Backpropagation, activation functions, training techniques",
        "difficulty": "advanced",
        "hours": 40,
        "category": "AI/ML",
        "prerequisites": ["machine-learning", "calculus"],
    },
    "deep-learning": {
        "name": "Deep Learning",
        "description": "CNNs, RNNs, transformers — state-of-the-art AI architectures",
        "difficulty": "advanced",
        "hours": 80,
        "category": "AI/ML",
        "prerequisites": ["neural-networks"],
    },
    "nlp": {
        "name": "Natural Language Processing",
        "description": "Text processing, embeddings, language models, transformers for text",
        "difficulty": "advanced",
        "hours": 50,
        "category": "AI/ML",
        "prerequisites": ["deep-learning"],
    },
    "computer-vision": {
        "name": "Computer Vision",
        "description": "Image processing, object detection, image segmentation",
        "difficulty": "advanced",
        "hours": 50,
        "category": "AI/ML",
        "prerequisites": ["deep-learning"],
    },

    # --- Web Development ---
    "html-css": {
        "name": "HTML & CSS",
        "description": "Web page structure and styling — the foundation of front-end web development",
        "difficulty": "beginner",
        "hours": 25,
        "category": "Web",
        "prerequisites": [],
    },
    "react": {
        "name": "React",
        "description": "Component-based front-end framework for building UIs",
        "difficulty": "intermediate",
        "hours": 40,
        "category": "Web",
        "prerequisites": ["html-css", "javascript"],
    },
    "nodejs": {
        "name": "Node.js",
        "description": "Server-side JavaScript runtime for building backends and APIs",
        "difficulty": "intermediate",
        "hours": 35,
        "category": "Web",
        "prerequisites": ["javascript"],
    },

    # --- Science ---
    "physics": {
        "name": "Physics (Classical)",
        "description": "Mechanics, electricity, magnetism — the physical laws of nature",
        "difficulty": "intermediate",
        "hours": 60,
        "category": "Science",
        "prerequisites": ["calculus"],
    },
    "quantum-mechanics": {
        "name": "Quantum Mechanics",
        "description": "Wave functions, Schrödinger equation, quantum states",
        "difficulty": "advanced",
        "hours": 80,
        "category": "Science",
        "prerequisites": ["physics", "linear-algebra", "probability"],
    },
    "quantum-computing": {
        "name": "Quantum Computing",
        "description": "Qubits, quantum gates, quantum algorithms (Shor's, Grover's)",
        "difficulty": "advanced",
        "hours": 60,
        "category": "Science",
        "prerequisites": ["quantum-mechanics", "algorithms"],
    },

    # --- Business ---
    "economics": {
        "name": "Economics",
        "description": "Micro/macroeconomics, supply and demand, market structures",
        "difficulty": "beginner",
        "hours": 30,
        "category": "Business",
        "prerequisites": ["basic-math"],
    },
    "finance": {
        "name": "Finance",
        "description": "Time value of money, valuation, portfolio theory",
        "difficulty": "intermediate",
        "hours": 40,
        "category": "Business",
        "prerequisites": ["economics", "statistics"],
    },
    "accounting": {
        "name": "Accounting",
        "description": "Financial statements, bookkeeping, managerial accounting",
        "difficulty": "beginner",
        "hours": 30,
        "category": "Business",
        "prerequisites": ["basic-math"],
    },
}


# ---------------------------------------------------------------------------
# Graph operations
# ---------------------------------------------------------------------------

class ConceptGraph:
    def __init__(self, concepts):
        self.concepts = concepts
        self._validate()

    def _validate(self):
        """Check that all prerequisites exist and no cycles."""
        for key, info in self.concepts.items():
            for prereq in info.get("prerequisites", []):
                if prereq not in self.concepts:
                    raise ValueError(f"Unknown prerequisite '{prereq}' for '{key}'")
        if self._has_cycle():
            raise ValueError("Concept graph has a cycle — prerequisites must form a DAG")

    def _has_cycle(self):
        """DFS-based cycle detection."""
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {k: WHITE for k in self.concepts}

        def dfs(node):
            color[node] = GRAY
            for neighbor in self.concepts[node].get("prerequisites", []):
                if color[neighbor] == GRAY:
                    return True
                if color[neighbor] == WHITE and dfs(neighbor):
                    return True
            color[node] = BLACK
            return False

        return any(color[k] == WHITE and dfs(k) for k in self.concepts)

    def get_all_prerequisites(self, target):
        """Recursively get all prerequisites for a concept (transitive closure)."""
        result = set()
        queue = deque(self.concepts.get(target, {}).get("prerequisites", []))
        while queue:
            prereq = queue.popleft()
            if prereq not in result:
                result.add(prereq)
                queue.extend(self.concepts.get(prereq, {}).get("prerequisites", []))
        return result

    def topological_sort(self, target=None):
        """Kahn's algorithm for topological sort."""
        # Build adjacency: prereq -> [dependents]
        in_degree = {k: 0 for k in self.concepts}
        adj = defaultdict(list)
        for key, info in self.concepts.items():
            for prereq in info.get("prerequisites", []):
                adj[prereq].append(key)
                in_degree[key] += 1

        # If target specified, only include relevant concepts
        relevant = self.get_all_prerequisites(target) | {target} if target else set(self.concepts.keys())
        relevant_in_degree = {k: in_degree[k] for k in relevant}

        queue = deque([k for k in relevant if relevant_in_degree[k] == 0])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for dependent in adj[node]:
                if dependent in relevant:
                    relevant_in_degree[dependent] -= 1
                    if relevant_in_degree[dependent] == 0:
                        queue.append(dependent)
        return result

    def critical_path(self, target):
        """Find the longest prerequisite chain to the target."""
        def dfs_longest(node, memo):
            if node in memo:
                return memo[node]
            prereqs = self.concepts.get(node, {}).get("prerequisites", [])
            if not prereqs:
                memo[node] = [node]
                return [node]
            best = []
            for prereq in prereqs:
                path = dfs_longest(prereq, memo)
                if len(path) > len(best):
                    best = path
            memo[node] = best + [node]
            return memo[node]
        return dfs_longest(target, {})

    def learning_path(self, target, known):
        """Shortest learning path from known concepts to target."""
        all_prereqs = self.get_all_prerequisites(target)
        unknown = all_prereqs - set(known)
        if not unknown:
            return [target]

        # Topological sort of unknown + target, respecting order
        relevant = unknown | {target}
        topo = self.topological_sort(target)
        path = [c for c in topo if c in relevant]
        return path


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def resolve_topic(query, graph):
    """Match a human-readable query to a concept key."""
    query_lower = query.lower().strip()
    # Exact key match
    if query_lower in graph.concepts:
        return query_lower
    # Match by name
    for key, info in graph.concepts.items():
        if info["name"].lower() == query_lower:
            return key
        if query_lower in info["name"].lower():
            return key
        if query_lower in key:
            return key
    # Partial match
    for key, info in graph.concepts.items():
        words = info["name"].lower().split()
        if any(w in query_lower for w in words):
            return key
    return None


def load_graph(args):
    """Load built-in KB or custom graph file."""
    if args.graph:
        with open(args.graph) as f:
            data = json.load(f)
        return ConceptGraph(data["concepts"])
    return ConceptGraph(KNOWLEDGE_BASE)


def cmd_map(args):
    graph = load_graph(args)
    target = resolve_topic(args.topic, graph)
    if not target:
        print(f"Topic '{args.topic}' not found. Use 'topics' command to list all.")
        sys.exit(1)

    info = graph.concepts[target]
    all_prereqs = graph.get_all_prerequisites(target)
    critical = graph.critical_path(target)

    print("=" * 65)
    print(f"  📋 PREREQUISITE MAP: {info['name']}")
    print(f"  Difficulty: {info['difficulty']} | Est. hours: {info['hours']}h")
    print(f"  {info['description']}")
    print("=" * 65)

    if not all_prereqs:
        print("\n  No prerequisites! You can start here directly.\n")
    else:
        print(f"\n  📊 Total prerequisites: {len(all_prereqs)}")
        print(f"  🛤️  Critical path length: {len(critical)} steps")
        print(f"\n  CRITICAL PATH (longest prerequisite chain):")
        for i, step in enumerate(critical):
            marker = "🎯" if step == target else f"{i+1}."
            name = graph.concepts[step]["name"]
            print(f"    {marker} {name}")

        print(f"\n  ALL PREREQUISITES (grouped by category):")
        cats = defaultdict(list)
        for p in sorted(all_prereqs):
            cats[graph.concepts[p]["category"]].append(p)
        for cat in sorted(cats):
            print(f"\n    [{cat}]")
            for key in cats[cat]:
                p = graph.concepts[key]
                print(f"      • {p['name']} ({p['difficulty']}, {p['hours']}h)")
                print(f"        ↳ {p['description']}")
    print()


def cmd_path(args):
    graph = load_graph(args)
    target = resolve_topic(args.topic, graph)
    if not target:
        print(f"Topic '{args.topic}' not found.")
        sys.exit(1)

    known = set()
    if args.known:
        for k in args.known.split(","):
            k = k.strip().lower()
            resolved = resolve_topic(k, graph)
            known.add(resolved or k)

    path = graph.learning_path(target, known)
    critical = graph.critical_path(target)
    all_prereqs = graph.get_all_prerequisites(target)
    new_concepts = [c for c in path if c != target]
    total_hours = sum(graph.concepts[c]["hours"] for c in new_concepts)

    print("=" * 65)
    print(f"  🎯 TARGET: {graph.concepts[target]['name']}")
    print(f"  📊 Current knowledge: {len(known & all_prereqs)} of {len(all_prereqs)} prerequisites")
    print(f"  ⏱️  New concepts to learn: {len(new_concepts)}")
    print(f"  ⏰ Estimated time: {total_hours}h ({total_hours // 10}–{total_hours // 8} weeks at 10h/week)")
    print("=" * 65)
    print()
    print("  LEARNING PATH:")
    for i, step in enumerate(path, 1):
        info = graph.concepts[step]
        is_target = step == target
        prereqs = info.get("prerequisites", [])
        prereq_status = []
        for p in prereqs:
            if p in known:
                prereq_status.append(f"✓ {graph.concepts[p]['name']}")
            elif p in path[:i-1]:
                prereq_status.append(f"☐ {graph.concepts[p]['name']}")
            else:
                prereq_status.append(f"? {graph.concepts[p]['name']}")
        status_str = ", ".join(prereq_status) if prereq_status else "✓ (none needed)"
        marker = "🎯" if is_target else f"{i:>2}."
        print(f"  {marker} ☐ {info['name']} [{info['difficulty']}, {info['hours']}h]")
        print(f"       Prerequisites: {status_str}")
        print(f"       Why: {info['description']}")
        if is_target:
            print(f"       └── 🎯 TARGET REACHED")
        print()

    if args.output:
        output_data = {
            "target": target,
            "known": sorted(known),
            "path": path,
            "estimated_hours": total_hours,
            "critical_path": critical,
        }
        with open(args.output, 'w') as f:
            json.dump(output_data, f, indent=2)
        print(f"  ✓ Path saved to {args.output}")


def cmd_audit(args):
    graph = load_graph(args)
    target = resolve_topic(args.topic, graph)
    if not target:
        print(f"Topic '{args.topic}' not found.")
        sys.exit(1)

    known = set()
    if args.known:
        for k in args.known.split(","):
            k = k.strip().lower()
            resolved = resolve_topic(k, graph)
            known.add(resolved or k)

    all_prereqs = graph.get_all_prerequisites(target)
    print("=" * 65)
    print(f"  🔍 KNOWLEDGE AUDIT: {graph.concepts[target]['name']}")
    print("=" * 65)
    print()
    print(f"  {'Concept':<30} {'Status':<8} {'Difficulty':<15} {'Gap?'}")
    print(f"  {'-'*30} {'-'*8} {'-'*15} {'-'*5}")
    gaps = []
    for p in sorted(all_prereqs, key=lambda x: graph.concepts[x]["difficulty"]):
        info = graph.concepts[p]
        status = "✓ Known" if p in known else "✗ Missing"
        gap = "" if p in known else "⚠️"
        print(f"  {info['name']:<30} {status:<8} {info['difficulty']:<15} {gap}")
        if p not in known:
            gaps.append(p)

    print(f"\n  📊 SUMMARY: {len(known & all_prereqs)}/{len(all_prereqs)} prerequisites known")
    if gaps:
        print(f"  ⚠️  {len(gaps)} GAPS to fill before starting {graph.concepts[target]['name']}")
        print(f"  Suggested order: {', '.join(graph.concepts[g]['name'] for g in gaps[:5])}")
    else:
        print(f"  ✅ You're ready to learn {graph.concepts[target]['name']}!")
    print()


def cmd_visualize(args):
    graph = load_graph(args)
    target = resolve_topic(args.topic, graph)
    if not target:
        print(f"Topic '{args.topic}' not found.")
        sys.exit(1)

    all_prereqs = graph.get_all_prerequisites(target) | {target}

    if args.format == "mermaid":
        lines = ["graph TD"]
        for key in all_prereqs:
            name = graph.concepts[key]["name"]
            lines.append(f'    {key}["{name}"]')
        lines.append("")
        for key in all_prereqs:
            for prereq in graph.concepts[key].get("prerequisites", []):
                if prereq in all_prereqs:
                    lines.append(f"    {prereq} --> {key}")
        lines.append("")
        # Style target
        lines.append(f'    classDef target fill:#e74c3c,color:#fff')
        lines.append(f'    class {target} target')
        output = "\n".join(lines)
    elif args.format == "tree":
        output_lines = [f"📁 {graph.concepts[target]['name']}"]
        def build_tree(node, prefix=""):
            prereqs = graph.concepts[node].get("prerequisites", [])
            for i, prereq in enumerate(sorted(prereqs)):
                is_last = i == len(prereqs) - 1
                connector = "└── " if is_last else "├── "
                name = graph.concepts[prereq]["name"]
                output_lines.append(f"{prefix}{connector}{name}")
                extension = "    " if is_last else "│   "
                build_tree(prereq, prefix + extension)
        build_tree(target)
        output = "\n".join(output_lines)
    else:
        print(f"Unknown format: {args.format}")
        sys.exit(1)

    print(output)
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output + "\n")
        print(f"\n✓ Saved to {args.output}")


def cmd_topics(args):
    graph = load_graph(args)
    cats = defaultdict(list)
    for key, info in graph.concepts.items():
        cats[info["category"]].append((key, info))

    print("=" * 50)
    print(f"  KNOWLEDGE BASE — {len(graph.concepts)} topics")
    print("=" * 50)
    for cat in sorted(cats):
        print(f"\n  [{cat}]")
        for key, info in sorted(cats[cat], key=lambda x: x[1]["difficulty"]):
            print(f"    • {info['name']:<25} ({info['difficulty']}, {info['hours']}h)")
    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Concept Cartographer — prerequisite mapping for learning.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command")

    p_map = sub.add_parser("map", help="Show prerequisite map for a topic")
    p_map.add_argument("topic", help="Target topic to map")
    p_map.add_argument("--graph", help="Custom graph JSON file")

    p_path = sub.add_parser("path", help="Generate learning path from known concepts")
    p_path.add_argument("topic", help="Target topic")
    p_path.add_argument("--known", help="Comma-separated known concepts")
    p_path.add_argument("--output", help="Save path JSON to file")
    p_path.add_argument("--graph", help="Custom graph JSON file")

    p_audit = sub.add_parser("audit", help="Audit knowledge gaps")
    p_audit.add_argument("topic", help="Target topic")
    p_audit.add_argument("--known", help="Comma-separated known concepts")
    p_audit.add_argument("--graph", help="Custom graph JSON file")

    p_viz = sub.add_parser("visualize", help="Export concept map")
    p_viz.add_argument("topic", help="Target topic")
    p_viz.add_argument("--format", choices=["mermaid", "tree"], default="tree")
    p_viz.add_argument("--output", help="Save to file")
    p_viz.add_argument("--graph", help="Custom graph JSON file")

    p_topics = sub.add_parser("topics", help="List all topics in knowledge base")
    p_topics.add_argument("--graph", help="Custom graph JSON file")

    args = parser.parse_args()

    if args.command == "map":
        cmd_map(args)
    elif args.command == "path":
        cmd_path(args)
    elif args.command == "audit":
        cmd_audit(args)
    elif args.command == "visualize":
        cmd_visualize(args)
    elif args.command == "topics":
        cmd_topics(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
