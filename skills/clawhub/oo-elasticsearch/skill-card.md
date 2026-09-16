## Description:

Elasticsearch (elastic.co). Use this skill for ANY Elasticsearch request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Elasticsearch action schemas and run search, document, index, alias, shard, node, task, and cluster-health operations through the OOMOL-connected oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends remote installer scripts that are executed directly in a shell.

Mitigation: Review installer contents or use an official signed or checksummed install path before installing the oo CLI.

Risk: The skill can perform write and destructive Elasticsearch actions.

Mitigation: Require explicit confirmation of the target, payload, and expected effect before running write or destructive actions.

Risk: Access to Elasticsearch is mediated through the oo CLI and OOMOL-connected credentials.

Mitigation: Install only when the publisher is trusted and the user is comfortable with OOMOL mediating access to the connected Elasticsearch account.

## Reference(s):

- [Elasticsearch skill on ClawHub](https://clawhub.ai/oomol/skills/oo-elasticsearch)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Elasticsearch homepage](https://www.elastic.co/elasticsearch)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose oo CLI connector commands and JSON request payloads; write and destructive Elasticsearch actions require explicit user confirmation.]

## Skill Version(s):

1.0.5 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
