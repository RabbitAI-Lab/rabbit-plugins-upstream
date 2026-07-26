## Description: <br>
Audits and maintains machine-facing entity identity facts, including Knowledge Graph, Wikidata, schema.org, sameAs, disambiguation, and AI-recognition evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers, marketers, and knowledge graph operators use this skill to audit, reconcile, and update canonical entity identity records for machine-readable discovery and disambiguation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect proposal acceptance or registry writes could make misleading entity facts canonical. <br>
Mitigation: Review proposed persistent writes before approval, require explicit authorization, and report accepted event IDs, offsets, and revisions. <br>
Risk: Wikidata, profile, or entity-identity changes can publish unsupported or inaccurate facts. <br>
Mitigation: Use verified primary and third-party sources, preserve unresolved conflicts, and review external changes before publication. <br>
Risk: Natural-person records can create privacy and compliance exposure. <br>
Mitigation: Confirm an applicable lawful basis, minimize stored fields, use pseudonymous aggregate IDs, and honor erasure or tombstone state unless explicitly reauthorized. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/entity-optimizer) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Entity Signal Checklist](references/entity-signal-checklist.md) <br>
- [Entity Type Reference](references/entity-type-reference.md) <br>
- [Knowledge Graph Guide](references/knowledge-graph-guide.md) <br>
- [Knowledge Panel and Wikidata Guide](references/knowledge-panel-wikidata-guide.md) <br>
- [Example Entity Audit Report](references/example-audit-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with optional shell commands and structured registry-event request details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose persistent registry changes only after user authorization and host capability checks.] <br>

## Skill Version(s): <br>
17.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
