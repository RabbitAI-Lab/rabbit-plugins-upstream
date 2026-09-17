## Description:

Elasticsearch (elastic.co) connector skill for Elasticsearch requests that read, create, update, or delete data through the OOMOL-connected Elasticsearch connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and operators use this skill to inspect Elasticsearch schemas and run search, count, document, index, alias, shard, task, node, and cluster actions through the OOMOL `oo` CLI. It supports read workflows, controlled write workflows, and explicitly confirmed destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documentation recommends running remote installer scripts directly in a shell.

Mitigation: Prefer an official signed or checksummed installation path, review installer contents before execution, and avoid elevated privileges unless required.

Risk: The skill can issue write and destructive Elasticsearch actions that alter or remove data.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before write or destructive actions.

Risk: Connector operation depends on OOMOL-managed authentication for the user's Elasticsearch account.

Mitigation: Install only when the user accepts OOMOL's connector managing account access and verify connection scope before use.

## Reference(s):

- [Elasticsearch homepage](https://www.elastic.co/elasticsearch)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-elasticsearch)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include Elasticsearch action names, schema-inspection commands, connector run commands, JSON request payloads, and safety confirmations for write or destructive actions.]

## Skill Version(s):

1.0.5 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
