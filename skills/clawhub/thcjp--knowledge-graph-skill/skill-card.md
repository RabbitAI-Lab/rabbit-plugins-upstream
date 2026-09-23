## Description:

Provides an embedded knowledge graph workflow that stores structured knowledge in JSON and supports KGML summaries, querying, merging, visualization, and configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to maintain persistent structured knowledge, query and merge entities, create KGML session summaries, and generate offline knowledge graph visualizations. It is intended for workflow automation and knowledge management rather than tasks requiring independent creative judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says this local CLI skill can modify assistant instruction files.

Mitigation: Review installation behavior before use, confirm exactly which files are changed, and keep an undo path for any instruction-file patches.

Risk: The security evidence says the skill handles encrypted secrets and the plaintext example and secret-display behavior need clarification.

Mitigation: Do not store real credentials in the vault until secret handling is reviewed and confirmed; keep credentials out of chat, logs, and version control.

Risk: The authoritative security verdict is suspicious because the skill lacks enough guardrails around secrets and instruction-file patching.

Mitigation: Review and scan the skill before deployment, and limit use to environments where local execution and file modification are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/knowledge-graph-skill)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, KGML text, JSON data, and offline HTML visualization outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local JSON storage for graph data and may create configuration, summary, vault, export, and visualization files in the workspace.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
