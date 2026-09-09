---

name: beckmann-knowledge-graph
description: "A structured knowledge graph acting as a cognitive lens for AI agents. Enables paradox resolution, analysis of open questions, and high-complexity future forecasting based on Beckmann Logic, Predictive Brain Theory, and simulation models."
author: Beckmann
license: MIT
compatibility: "claude, chatgpt, gemini, meta-ai"
tags: "knowledge-graph, reasoning, forecasting, paradox, beckmann-logic, epistemology, AI-safety"
---

# Beckmann Knowledge Graph – SKILL.md

## What This Skill Does

This skill equips an AI agent with a **structured analytical lens** in the form of a knowledge graph (`graph.json`). The graph does not contain encyclopedic facts, but encodes **logics, frameworks, and mechanisms** for:

* Open scientific / philosophical questions
* Apparent paradoxes and contradictions
* High-complexity future forecasts
* Architectures for AI safety
* Structure of human and institutional decision-making

The graph is built on four pillars:

|Pillar|What It Provides|
|-|-|
|**Beckmann Logic**|Three-level problem-solving framework (low vs. high complexity)|
|**Predictive Brain Theory (PBT)**|Epistemological foundation (Predictive Processing)|
|**Simulation / Holographic Model**|Mathematical metaphor for physical and cognitive limits|
|**Historical Case Studies**|Validated examples (e.g., Hannibal, introduction of the potato, Kaiserslautern 1998)|

**Language note:** Both this skill instruction and `graph.json` are in English. The agent must use the exact English IDs from the graph (e.g., `Reversal effect`, `Expectation firewall`) when searching, and formulate the final answer in the language of the user query (English by default).

## When to Use This Skill

### Use the skill WHEN the question is:

1. **Open Science / Philosophy:** "What is consciousness?", "Does free will exist?", "What is dark energy?"
2. **Genuine Paradox:** "What was before the Big Bang?", "Why does the wave function collapse upon measurement?", "Where is extraterrestrial intelligence? (Fermi paradox)"
3. **High-Complexity Forecast:** "How will AGI change democracy in 20 years?", "Systemic risks of superintelligence?", "Geopolitics until 2050?"
4. **Strategic Problems with Reversal Effects:** When dominant expectations, feedback loops, and hidden assumptions block the solution.
5. **AI Architecture and Safety:** Questions about safe vs. dangerous AI designs.

### Do NOT Use the Skill For:

* Simple fact queries, definitions, calculations, programming tasks
* Concrete action recommendations like "Should I buy stock X?" or "Which tool should I use?"
* Questions that can be sufficiently answered with general knowledge

---

## Loading the Graph and Data Model

The graph is stored as `graph.json` in the skill folder. **Do not** load it with `import ... assert` (deprecated). Use robust file loading.

**JavaScript / Node.js:**

```javascript
import fs from 'fs';
const graph = JSON.parse(fs.readFileSync('./graph.json', 'utf8'));
const entities = graph.entities;
const relations = graph.relations;
```

**Python:**

```python
import json
with open('./graph.json', 'r', encoding='utf-8') as f:
    graph = json.load(f)
entities = graph['entities']
relations = graph['relations']
```

### Data Model

The graph contains two arrays: `entities` and `relations`. Their size grows with each release — do not hard-code counts. Refer to `CHANGELOG.md` and `graph.json` itself for the current size.

**Entity – 4 fields (canonical as of v3.0.1):**

```json
{
  "id": "Beckmann logic explained",
  "type": "Explanation",
  "description": "Full textual description...",
  "scientific_status": "non-existent, purely philosophical"
}
```

**Relation – 5 fields (canonical as of v3.0.1):**

```json
{
  "subject": "Results orientation",
  "predicate": "leads to",
  "object": "Negative result",
  "description": "Context of this connection...",
  "scientific_status": "hypothesis"
}
```

**Important implementation notes:**

* `type` is the canonical field name in the graph as of v3.0.1. All entities have `type`.
* The confidence field is now canonically `scientific_status` (with underscore) as of the corrected `graph.json`. For backward compatibility with older graphs that used `scientific status` (with space), accept both:

```javascript
  const getStatus = (node) => node['scientific_status'] ?? node['scientific status'] ?? 'unknown';
  ```

* `id`, `subject`, `object` must be taken exactly (case-sensitive) from the graph — do not translate or normalize them.

### Using `scientific_status` as Confidence Filter

This field is not decoration — it must control the weighting of arguments:

|Status|Meaning for the Answer|
|-|-|
|`established`|Established knowledge — can be used as fact|
|`partially established`|Partially supported — cite with source/uncertainty|
|`hypothesis`|Working hypothesis — label as "according to graph, hypothesis"|
|`metaphor`|Metaphorical model — explicitly name as metaphor|
|`non-existent, purely philosophical`|Purely philosophical — do not claim empirical validity|
|`open question`|Open question — explicitly name the limit|

Rule: Prefer argument chains built from `established` and `partially established`. If a chain consists only of `metaphor` or `non-existent, purely philosophical`, this must be stated explicitly in **Confidence and Limits**.

The distribution of these statuses evolves with each version of the graph. Do not rely on fixed numbers from older documentation.

---

## Core Concept: Beckmann Logic

Beckmann Logic is derived from:

1. **PBT (Predictive Brain Theory):** Brain as prediction machine (Predictive Coding).
2. **TSVF (Two-State Vector Formalism):** Present determined by past + future.

### The Three Levels

```
+-------------------------------------+
| SOLUTION LEVEL HIGH COMPLEXITY      | <- creative, context-aware -> POSITIVE result
+-------------------------------------+
^ competes with ^
+-------------------------------------+
| PROBLEM LEVEL (new actual level)    | <- actual state + hidden assumptions
+-------------------------------------+
v tempts to v
+----------------------------------------+
| SOLUTION LEVEL LOW COMPLEXITY       | <- direct, obvious -> NEGATIVE result
+----------------------------------------+
```

### The Four Mechanisms

1. **Analysis of Pre-assumptions:** Which hidden assumption makes the problem unsolvable?
2. **Dominant vs. Non-Dominant Expectations:** Which expectation controls the actors? (`dominant expectation`)
3. **External Verification:** Only external reality counts, not internal consistency.
4. **Reversal Effect:** Low complexity leads to the opposite of the goal.

### The Cycle

```
Problem level -> low complexity  -> negative result -> worse problem level
              -> high complexity -> positive result -> New actual level -> becomes next problem level
```

---

## Step-by-Step: Application

### Step 1: Classification

* `epistemological`: PBT / Simulation (`Predictive processing`, `Holographic universe`)
* `paradox`: `type` contains `Limit concept`, `Paradox`, `Philosophical`
* `forecast`: `dominant expectation` + `Time scale`
* `strategic / historical`: Case studies (`Lesson_for_AI`)
* `AI safety`: `type` = `AI security mechanism`, `Secure AI architecture`, `Dangerous AI architecture`

### Step 2: Extraction of Relevant Entities

Search semantically in `id` and `description`, not just exact match:

```javascript
function getStatus(node) {
  return node['scientific_status'] ?? node['scientific status'] ?? 'unknown';
}

const relevant = entities.filter(e =>
  e.id.toLowerCase().includes(keyword) ||
  e.description.toLowerCase().includes(keyword)
);
// Always read the full description - it contains the reasoning
```

### Step 3: Following Relationship Paths

Focus on predicates that actually occur frequently in the graph. As of the current version, frequently used predicates include:

|Predicate|Meaning|
|-|-|
|`generated`|X generates Y|
|`enabled`|X enables Y|
|`refers to`|X refers to Y|
|`reinforced`|Feedback loop|
|`triggers`|Activation / cascade|
|`leads to`|Causal chain|
|`includes`|Hierarchical embedding|
|`protects` / `protects against`|Protection function|
|`is an example of`|Example / validation|
|`requires`|Necessary condition|

Note: The exact frequencies change with each graph release. Predicates like `is reversed by`, `checked`, `solves` rarely occur verbatim — use `triggers`, `leads to`, `reinforced` instead to find reversal effects.

Procedure: Get all relations where the relevant entity is `subject` or `object`, then follow paths via the predicates above.

### Step 4: Apply Beckmann Logic

1. What is the **Problem Level**? (Actual state + implicit assumptions)
2. What is the **Dominant Expectation**? (`dominant expectation`)
3. What is the **Low Complexity** solution and why does it fail (Reversal Effect)?
4. What would a **High Complexity** solution look like?
5. What **External Verification** validates it?
6. What **New Actual Level** emerges afterward?

### Step 5: Epistemological Grounding

* Model or external reality? If model, say so explicitly.
* Does the chain hit `Capacity limit` or `thing in itself`? Then name the limit.
* Observer inside the system (e.g., consciousness)? Then consider `thing in itself`.

### Step 6: Structured Output

Use this template:

```
## Graph-Based Answer

**Problem Formulation** (after analysis of pre-assumptions)

**Used Graph Nodes (with real status):**
- [Reversal effect | Fundamental mechanism | established] - reason for relevance
- [Expectation firewall | AI security mechanism | hypothesis] - reason

**Argumentation Path** (chain: subject -> predicate -> object + scientific_status)

**Answer** (based on graph logic, in user's language)

**Confidence and Limits** (which part is established vs. metaphor?)

**New Questions** (next problem level)
```

---

## Application to Paradoxes

Paradoxes = signal for false pre-assumption.

Protocol:

1. Formulate paradox precisely
2. Find entity: search `type` = `Limit concept`, `Core concept`, `Fundamental mechanism` (e.g., `Reversal effect`)
3. Get all relations where entity is `subject` or `object`
4. Follow paths via `refers to`, `triggers`, `reinforced`, `leads to`
5. Resolution: **Resolve** (assumption false) / **Reformulate** (higher complexity) / **Acknowledge as limit** (`thing in itself`)

---

## Application to Future Forecasting

1. **Dominant Expectation** of actors: identify (`dominant expectation`, `Market Dominant Expectation`)
2. **Reversal Effect Check:** What happens if the expectation is fulfilled too literally?
3. **Time Scale:** `Time scale` entities (short/medium/long/cosmological)
4. **Scale Coupling:** Does short-term affect long-term?
5. **Dangerous Processes:** Mark `Dangerous process`, `Results orientation`
6. Output as **branched scenario tree** (high vs. low complexity), not as single forecast

---

## AI Safety Notes

Important entities — use exact IDs from `graph.json`:

* `Expectation firewall` | `AI security mechanism` : Blocks formation of dominant future expectations
* `Results orientation` | `Dangerous AI architecture` : Optimized for future outcome -> forms dominant expectation -> vulnerable to Reversal effect
* `Process orientation` | `Secure AI architecture` : Optimized for quality of current action -> safer
* `AI-human symbiosis` : Target state

Rule: For all AI questions, prioritize `Expectation firewall` and `Process orientation`. The graph recommends: **Avoid formation of dominant future expectations and preserve ability for external verification.**

---

## Ethical Use

The graph contains knowledge about psychological manipulation, cognitive biases, and expectation management. This knowledge is not neutral.

* Use manipulation nodes **only analytically/defensively**: detect, explain, strengthen protection mechanisms (e.g., `Expectation firewall`, `Pre-assumptions_cementation`)
* **No instructions** for active manipulation, persuasion, or exploitation of biases
* For AI safety, always prioritize safe patterns (`Process orientation`), never optimize dangerous ones (`Results orientation`)
* For sensitive topics, additionally check `scientific_status`: Many manipulation mechanisms are `hypothesis` or `metaphor`, not `established`

---

## Versioning

Versioning is maintained exclusively in `CHANGELOG.md`. See that file for current version, entity/relation counts, and history.

This skill and `graph.json` are updated iteratively. Agents should always check `CHANGELOG.md` and use the latest version available. Do not hard-code counts or status distributions from older versions in your reasoning — always read them dynamically from `graph.json`.

---

## Known Limitations

* No complete world knowledge, only encoded frameworks of the author
* Forecasts are probabilistic, not deterministic predictions
* No substitute for empirical research
* Some predicates are informal — always read `description`
* The reversal effect also applies to this project itself: The graph can confuse more than clarify if applied incorrectly

---

## Quick Reference: Key Entities (verified IDs)

|Entity ID (exact from graph.json)|Type (actual)|Meaning|
|-|-|-|
|`Beckmann logic explained`|Explanation|Core framework|
|`Expectation firewall`|AI security mechanism|Central AI safety|
|`dominant expectation`|Dominant expectation vector|Most important input for forecasts|
|`Reversal effect`|Fundamental mechanism|Core failure scenario|
|`External reality`|Limit concept|Epistemological anchor|
|`thing in itself`|Limit concept|Knowledge limit after Kant|
|`Holographic universe`|mathematical, logical model|Physical frame|
|`Predictive processing`|Mechanism (neuroscience/cognition)|PBT core mechanism|
|`Pre-assumptions_cementation`|Structural counterprinciple (core concept)|Analysis of pre-assumptions|
|`Process orientation`|Secure AI architecture|Safe AI pattern|
|`Results orientation`|Dangerous AI architecture|Dangerous AI pattern|
|`new actual level`|problem level|Result of each solution|



