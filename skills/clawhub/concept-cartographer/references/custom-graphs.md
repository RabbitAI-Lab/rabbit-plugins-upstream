# Custom Concept Graphs

## Defining Your Own Knowledge Maps

While Concept Cartographer ships with a built-in knowledge base, you can define custom concept graphs for any domain.

## Graph File Format

Custom graphs are JSON files with the following structure:

```json
{
  "domain": "My Custom Domain",
  "concepts": {
    "concept-a": {
      "name": "Concept A",
      "description": "What this concept is about",
      "difficulty": "beginner",
      "estimated_hours": 10,
      "prerequisites": []
    },
    "concept-b": {
      "name": "Concept B",
      "description": "Builds on A",
      "difficulty": "intermediate",
      "estimated_hours": 20,
      "prerequisites": ["concept-a"]
    },
    "concept-c": {
      "name": "Concept C (Target)",
      "description": "The final goal",
      "difficulty": "advanced",
      "estimated_hours": 40,
      "prerequisites": ["concept-a", "concept-b"]
    }
  }
}
```

## Using Custom Graphs

```bash
# Use a custom graph file
python scripts/cartographer.py map "concept-c" --graph custom_graph.json

# Path through a custom graph
python scripts/cartographer.py path "concept-c" --known "concept-a" --graph custom_graph.json
```

## Example: Music Theory Learning Map

```json
{
  "domain": "Music Theory",
  "concepts": {
    "basic-notation": {
      "name": "Basic Notation",
      "description": "Reading sheet music: clefs, notes, rhythms",
      "difficulty": "beginner",
      "estimated_hours": 10,
      "prerequisites": []
    },
    "scales-keys": {
      "name": "Scales and Keys",
      "description": "Major/minor scales, key signatures, circle of fifths",
      "difficulty": "beginner",
      "estimated_hours": 15,
      "prerequisites": ["basic-notation"]
    },
    "intervals": {
      "name": "Intervals",
      "description": "Distance between pitches, consonance/dissonance",
      "difficulty": "beginner",
      "estimated_hours": 10,
      "prerequisites": ["basic-notation"]
    },
    "chords": {
      "name": "Chords and Harmony",
      "description": "Triads, seventh chords, chord progressions",
      "difficulty": "intermediate",
      "estimated_hours": 25,
      "prerequisites": ["scales-keys", "intervals"]
    },
    "counterpoint": {
      "name": "Counterpoint",
      "description": "Independent melodic lines, species counterpoint",
      "difficulty": "advanced",
      "estimated_hours": 40,
      "prerequisites": ["chords"]
    },
    "composition": {
      "name": "Composition",
      "description": "Writing original music: form, orchestration, analysis",
      "difficulty": "advanced",
      "estimated_hours": 100,
      "prerequisites": ["chords", "counterpoint"]
    }
  }
}
```

## Design Principles for Good Graphs

1. **Atomic concepts**: Each node should be a single, learnable unit. "Mathematics" is too broad; "Linear Algebra" is right-sized.

2. **Minimal edges**: Only add a prerequisite edge if knowledge of A is truly necessary before B. Optional but helpful knowledge shouldn't create a dependency.

3. **Honest difficulty**: Estimate hours realistically. A concept that takes 2 hours to understand is very different from one that takes 40.

4. **No cycles**: The graph must be a DAG (directed acyclic graph). If A requires B and B requires A, you've over-complicated — break them into smaller pieces.

5. **Clear descriptions**: Each concept's description should explain *why* it matters for the target, not just *what* it is.

## Graph Validation

Concept Cartographer validates custom graphs:
- Checks for cycles (which would make topological sort impossible)
- Warns about orphan nodes (concepts with no path to any other)
- Reports the maximum depth (longest prerequisite chain)

## Sharing Graphs

Custom graphs are plain JSON — share them via GitHub, Gist, or any file-sharing method. A community-maintained collection of learning graphs could become a powerful open educational resource.
