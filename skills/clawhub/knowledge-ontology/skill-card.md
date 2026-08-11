## Description:

知识本体 helps agents model local knowledge as typed entities and relationships with constraint validation, schema evolution, and graph traversal planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators can use this skill when they need an agent to create, query, validate, and evolve a local ontology or knowledge graph for project memory, dependency analysis, and impact analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags inconsistent API credential guidance without a clear external integration boundary.

Mitigation: Use the skill only for explicit knowledge-graph or ontology tasks, and do not provide API keys unless the publisher clarifies a specific external integration.

Risk: The skill requests exec and write capabilities that can mutate local graph files.

Mitigation: Review planned file and command actions before execution, restrict work to the intended ontology directory, and keep recoverable backups or append-only history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/knowledge-ontology)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe local ontology file changes, validation results, migrations, traversal plans, and command-line steps.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
