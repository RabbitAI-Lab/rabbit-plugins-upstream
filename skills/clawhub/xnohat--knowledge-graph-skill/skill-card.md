## Description:

Embedded knowledge graph for AI agents that stores structured knowledge as entities and relationships, supports local search and traversal, and produces compact session context summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xnohat](https://clawhub.ai/user/xnohat)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to maintain persistent personal or project knowledge across sessions, query known entities and relationships, extract structured knowledge from longer materials, and generate compact KGML summaries for agent context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently changes agent instructions to automatically collect broad personal, project, infrastructure, preference, location, habit, and credential-related information.

Mitigation: Review or remove the injected KG-AUTONOMOUS instruction block after installation, and limit collection categories to information the user explicitly wants retained.

Risk: Vault commands can expose secrets when plaintext values are passed as shell arguments.

Mitigation: Avoid passing secrets directly on the command line; review command history and stored vault keys before relying on the vault for sensitive credentials.

Risk: Memory import can scan and persist information from local files that the user has not reviewed.

Mitigation: Run memory import in dry-run mode first and review the exact files and categories before applying imports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xnohat/skills/knowledge-graph-skill)
- [README](artifact/README.md)
- [Design document](artifact/DESIGN.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, plus CLI-generated JSON graph data, KGML Markdown summaries, and self-contained HTML visualizations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js 18 or newer and stores persistent graph, summary, configuration, visualization, and vault files under the skill data directory.]

## Skill Version(s):

1.1.1 (source: package.json and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
