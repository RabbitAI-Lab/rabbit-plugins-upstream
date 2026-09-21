## Description:

Elasticsearch (elastic.co). Use this skill for ANY Elasticsearch request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Elasticsearch schemas and run index, document, search, cluster-health, alias, shard, and task actions through an OOMOL-connected Elasticsearch account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive Elasticsearch actions can change, overwrite, or permanently delete data.

Mitigation: Require explicit user approval for write or destructive actions, including confirmation of the exact target and payload before execution.

Risk: Setup commands install or invoke the OOMOL oo CLI before accessing the connected Elasticsearch account.

Mitigation: Review the CLI installer source or use official manual installation guidance before running setup commands.

Risk: Connector calls can fail or behave unexpectedly if the live action schema is not checked first.

Mitigation: Inspect the action schema with oo connector schema before constructing and running each connector payload.

## Reference(s):

- [Elasticsearch homepage](https://www.elastic.co/elasticsearch)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-elasticsearch)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and PowerShell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects returned by the oo CLI when actions are executed.]

## Skill Version(s):

1.0.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
