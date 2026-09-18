## Description:

Databox (databox.com). Use this skill for ANY Databox request: reading, creating, updating, and deleting data through the OOMOL-connected Databox connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Databox accounts, ingestion data sources, datasets, and dataset records through the OOMOL `oo` CLI. It supports reading account and ingestion status, creating resources, pushing JSON records, and deleting Databox resources after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path uses remote installer commands that can execute changing code on the user's machine.

Mitigation: Review setup before installation and prefer official OOMOL installation documentation or a verified, pinned installer.

Risk: Write and delete actions can change or remove Databox resources.

Mitigation: Require explicit approval with the exact target and payload before running state-changing or destructive Databox actions.

## Reference(s):

- [Databox homepage](https://databox.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-databox)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run OOMOL `oo connector` commands; state-changing Databox actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
