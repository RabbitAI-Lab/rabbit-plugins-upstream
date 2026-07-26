# Routing Schema Specification

Complete YAML schema for skill routing declarations.

## File Locations

A skill's routing config can live in two places (checked in this order):

```
my-skill/
├── routing.yaml    <- Standalone routing config (preferred)
└── SKILL.md        <- Or embedded in frontmatter under metadata.routing
```

## Full Schema

```yaml
# routing.yaml — Complete field reference

name: my-skill                    # Skill identifier (must match directory name)
description: "What this skill does"  # Human-readable description

routing:
  # --- Trigger Rules ---

  keywords:                       # Substring match (case-insensitive)
    - "keyword1"
    - "keyword phrase"
    type: array[string]
    required: false
    notes: |
      Matched via case-insensitive substring search in the query.
      Each keyword is checked independently.
      keyword_score = matched_count / total_count

  patterns:                       # Regex patterns (Python re syntax)
    - "(verb1|verb2).{0,6}(noun1|noun2)"
    type: array[string]
    required: false
    notes: |
      Evaluated with re.search(pattern, query, re.IGNORECASE).
      Any single match sets pattern_score = 1.0.
      Invalid regex is silently skipped.

  intents:                        # Semantic intent tags (dot-separated)
    - "domain.action.target"
    type: array[string]
    required: false
    notes: |
      Tags are split on "." and "_" into keywords.
      Matched against query via substring search.
      intent_score = matched_parts / total_parts

  anti_patterns:                  # Hard exclusion rules
    - "should not trigger phrase"
    type: array[string]
    required: false
    notes: |
      Checked BEFORE scoring. Any match = immediate exclusion.
      Can be regex or plain text (falls back to substring if regex is invalid).
      Use for disambiguation: prevents this skill from stealing queries
      meant for other skills.

  anti_keywords:                  # Soft penalty words
    - "penalty word"
    type: array[string]
    required: false
    notes: |
      Each hit subtracts 0.15 from total score (max -0.5).
      Softer than anti_patterns — reduces score without hard exclusion.

  # --- Scoring Controls ---

  priority: 50                    # 0-100, base importance weight
    type: integer
    default: 50
    notes: |
      Contributes to score as: priority_weight * (priority / 100)
      Higher = more likely to be recalled when signals are weak.
      Guidelines:
        - General utility skills (e.g. "search") -> 60-80
        - Domain-specific skills (e.g. "HIPAA compliance audit") -> 30-50
        - High-frequency daily skills (e.g. "code review") -> 70-90

  mode: any                       # Keyword matching mode
    type: enum[any, all, threshold]
    default: any
    notes: |
      - any: score = hit_count / total (default, most flexible)
      - all: score = 1.0 only if ALL keywords match, else 0.0
      - threshold: score = 1.0 if hit_ratio >= threshold_ratio

  threshold_ratio: 0.5            # For mode=threshold
    type: float
    default: 0.5

  weight_overrides:               # Per-skill weight customization
    keyword: 0.40                 # Override global keyword weight
    pattern: 0.30
    type: dict[string, float]
    required: false
    notes: |
      Overrides global weights for this skill only.
      Useful when a skill relies heavily on one signal type.

  # --- Context Signals ---

  context:
    file_types:                   # Bonus when user has these file types open
      - ".pdf"
      - ".docx"
      type: array[string]
    workspace_hints:              # Bonus when workspace matches these tags
      - "legal"
      - "compliance"
      type: array[string]
    notes: |
      Context signals are optional bonus points.
      Only evaluated if the agent passes context info to the router.
      context_score = matched_conditions / total_conditions

  # --- Advanced ---

  exclusive_with:                 # Mutual exclusion groups
    - "other-skill-name"
    type: array[string]
    required: false
    notes: |
      If both this skill and the named skill score above threshold,
      only the higher-scoring one is recalled.

  requires_skills:                # Dependency declaration
    - "prerequisite-skill"
    type: array[string]
    required: false
    notes: |
      If this skill is recalled, the named skills are also loaded
      regardless of their individual scores.
```

## Writing Effective Patterns

### Pattern Design Principles

1. **Capture verb-object structure** with flexible gaps
2. **Cover multiple phrasings** (synonyms, abbreviations)
3. **Avoid over-broad patterns** that match unintended queries
4. **Avoid over-strict patterns** that only match one exact sentence

### Examples

```yaml
patterns:
  # GOOD: captures core verb-object structure with flexible gap
  - "(review|check|audit).{0,4}(contract|agreement|terms)"

  # GOOD: covers multiple English phrasings
  - "(review|check|audit|examine).{0,8}(contract|agreement|NDA|terms)"

  # BAD: too broad — matches "draft a contract"
  - ".*contract.*"

  # BAD: too strict — only matches this exact sentence
  - "^please review my contract$"
```

### Gap Sizing Guide

| Gap | Use Case |
|-----|----------|
| `.{0,2}` | Direct adjacency (e.g., "code review") |
| `.{0,4}` | One connecting word (e.g., "review the code") |
| `.{0,8}` | Natural sentence gap (e.g., "review my latest code changes") |
| `.{0,12}` | Long-distance relation (use sparingly, high false-positive risk) |

## System-Level Configuration

```yaml
# routing-config.yaml — System administrator settings

router:
  threshold_strategy: gap        # fixed | top-k | gap | pattern-gate
  threshold_params:
    theta: 0.30                  # Score threshold for fixed/gap strategies
    k: 3                         # Number of results for top-k
    delta: 0.15                  # Gap size for gap strategy
  weights:                       # Global weights (can be overridden per-skill)
    keyword: 0.30
    pattern: 0.25
    intent: 0.15
    anti: 1.0
    context: 0.15
    priority: 0.15
  fallback: embedding            # Fallback when all scores < theta
```
