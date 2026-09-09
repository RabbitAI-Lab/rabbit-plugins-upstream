# IA deliverables and semantic model

Read this reference after the IA direction is stable enough to communicate or when the user requests a reusable artifact.

## Layered delivery

Do not use every section by default. Select the smallest useful combination.

### Decision layer

- purpose, scope, audience, and evidence status;
- recommendation and why it fits;
- consequential unknowns and decisions;
- next action.

### Working architecture layer

- users, content, and context;
- important objects/content and relationships;
- organization and taxonomy;
- labels and controlled vocabulary;
- navigation, search, entry, orientation, and recovery;
- roles, permissions, ownership, lifecycle, and governance;
- meaningful alternatives and trade-offs.

### Assurance layer

- evidence ledger and limitations;
- validation plan and decision rules;
- decision log and review triggers;
- machine-readable semantic model when it will be reused.

For a focused request, include only its essential prerequisites. Do not pad it into a complete report.

## Canonical structure before presentation

Every deliverable must represent one canonical semantic IA model. Do not independently invent a text hierarchy, diagram, HTML artifact, and role table that disagree with one another.

The canonical model should capture, where relevant:

- users, roles, contexts, and priority information needs;
- information domains, concepts, objects, and content types;
- parent-child hierarchy and ordering;
- typed cross-relationships that hierarchy cannot express;
- organization schemes, taxonomy, labels, metadata, and classification rules;
- navigation, search, entry, orientation, and recovery;
- visibility, permissions, ownership, lifecycle, and governance;
- evidence, consequential assumptions, unknowns, decisions, and validation.

Renderers select views of this model. They do not become the model.

## Audience adaptation

- **Product or leadership:** lead with decisions, risks, scope, and consequences.
- **Cross-functional team:** add object relationships, vocabulary, ownership, and retrieval behavior.
- **Design or research:** emphasize audience language, organization hypotheses, findability, and validation.
- **Engineering or data:** add stable identifiers, relationships, cardinality, states, permissions, and lifecycle rules.
- **Content or operations:** emphasize ownership, vocabulary, metadata, publishing or service lifecycle, retrieval, and governance.

When no audience is specified and it does not affect the decision, use a cross-functional professional baseline.

Translate the same canonical model for each audience. Do not create separate architecture truths for leadership, design, engineering, or operations.

## Format selection

In a conversation-capable environment, use chat text by default. Produce a file or heavy artifact only when the current conversation requests it or the user accepts a concrete format after the IA is ready enough. Persistent memory or a preference from another chat is not deliverable authorization. Prompt-to-app builders are downstream renderers: prepare their handoff only after the canonical IA is stable enough for the intended decision.

Offer only formats supported by the current environment and distinguish:

- editable source;
- rendered output;
- copy-ready content when file creation is unavailable.

Do not generate every format. Produce the one the user selects.

## Interactive connected IA blueprint

When the user requests an interactive visual artifact, it should help a mixed team understand and challenge the IA without requiring IA expertise.

### Primary view

Start with a connected hierarchy of information domains, concepts, objects, and content types. Make containment, classification, and important cross-domain relationships legible. The viewer should understand the product's information universe and major connections before opening any specialist detail.

This is not a sitemap: its nodes are semantic information structures rather than pages or destinations. It is not a user flow: edges express structural or semantic relationships rather than a sequence of actions.

### Progressive detail

Reveal relevant detail through selection, expansion, filtering, or focused subviews:

- purpose, attributes, states, and lifecycle;
- taxonomy, labels, metadata, and classification rules;
- navigation, search, entry, orientation, and recovery;
- role visibility, permissions, ownership, and governance;
- decisions, consequential assumptions, unknowns, evidence, risks, and validation.

Do not make a collection of tabs, tables, or cards the primary IA. Use them only to explain the structure. Avoid rendering internal evidence labels as unexplained badges on every node.

The blueprint is a review view of the architecture. It is not the product interface, wireframe, prototype, sitemap, user flow, API, or database schema. Prefer visible domain containers, clear hierarchy, labeled connections, progressive disclosure, accessibility, and the user's language and writing direction over decorative UI.

## Semantic IA JSON

Use this portable shape only when structured reuse, validation, rendering, or handoff justifies it:

```json
{
  "meta": {
    "title": "Example IA",
    "model_version": "2.0",
    "status": "proposed",
    "language": "en",
    "direction": "ltr",
    "scope": "Product area",
    "problem_shape": "hybrid",
    "locale_context": {
      "country": null,
      "operating_model": null,
      "evidence_status": "Unknown"
    },
    "handoff": {
      "purpose": "review",
      "readiness": "provisional"
    }
  },
  "contexts": [],
  "audiences": [],
  "tasks": [],
  "information_needs": [],
  "domains": [],
  "items": [],
  "relationships": [],
  "roles": [],
  "organization_schemes": [],
  "taxonomy": {},
  "labels": [],
  "metadata_model": [],
  "navigation_systems": [],
  "search": {},
  "permissions": [],
  "lifecycles": [],
  "governance": {},
  "evidence_ledger": [],
  "assumptions": [],
  "unknowns": [],
  "conflicts": [],
  "decisions": [],
  "validation": []
}
```

Keep IDs stable across revisions. Relationships must reference existing IDs. Use the response language for human labels. Technical IDs may be English when interoperability benefits. Use `direction: rtl` for an RTL rendered artifact unless the selected renderer is clearer with English technical labels and a different flow direction.

Use `parent_id` only for real hierarchy, containment, or classification. Represent associative, dependency, reference, ownership, lifecycle, and visibility relationships explicitly in `relationships` with a type, direction, and human-readable meaning.

## Architecture alternative card

```markdown
### Option name
- Organizing principle:
- Best-supported needs:
- Trade-offs and failure risks:
- Retrieval dependency:
- Governance cost:
- Supporting evidence:
- Validation needed:
```

## Decision log entry

```markdown
- Decision:
- Status: Confirmed | Proposed
- Rationale and evidence:
- Alternatives considered:
- Consequences:
- Owner:
- Review trigger:
```
