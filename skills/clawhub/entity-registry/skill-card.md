## Description: <br>
Entity Registry helps agents audit and maintain canonical machine-facing entity identity, sameAs, schema, disambiguation, Wikidata, and AI-recognition evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and operators use this skill to audit, reconcile, and update canonical entity identity for Knowledge Graph, Wikidata, schema.org, sameAs, and AI-system disambiguation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Entity records can become inaccurate if weak, stale, or ambiguous evidence is accepted as canonical. <br>
Mitigation: Confirm the target entity, require source-backed observations and verified cross-links for merges, keep Unknown distinct from failure, and preserve conflicts instead of silently choosing one fact. <br>
Risk: Natural-person records can create privacy or authorization concerns when persisted. <br>
Mitigation: Confirm an applicable lawful basis before persistence, minimize fields, avoid raw contact details and credentials, and respect prior erasure or tombstone state unless the user explicitly authorizes a new lawful record. <br>
Risk: Unauthorized writes could change canonical entity state. <br>
Mitigation: Ask before the first persistent write and only append canonical changes through the authorized registry runtime with the required host capability, schema, catalog, and revision checks. <br>


## Reference(s): <br>
- [Entity Signal Checklist](artifact/references/entity-signal-checklist.md) <br>
- [Entity Type Reference](artifact/references/entity-type-reference.md) <br>
- [Example Entity Optimization Report](artifact/references/example-audit-report.md) <br>
- [Knowledge Graph Guide](artifact/references/knowledge-graph-guide.md) <br>
- [Knowledge Panel and Wikidata Optimization Guide](artifact/references/knowledge-panel-wikidata-guide.md) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/entity-registry) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown reports, JSON event requests, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Persistent registry writes require user authorization, host capability, and verified runtime/schema/catalog support.] <br>

## Skill Version(s): <br>
19.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
