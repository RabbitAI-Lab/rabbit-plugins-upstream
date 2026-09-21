## Description:

Databox connector skill for reading, creating, updating, and deleting Databox data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage Databox accounts, ingestion data sources, datasets, and dataset records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, modify, and delete Databox resources through connector actions.

Mitigation: Review Databox write and delete payloads with the user before approval, and confirm destructive targets explicitly.

Risk: The skill depends on an external oo CLI installation source.

Mitigation: Confirm trust in OOMOL and use verified oo CLI installer instructions before installing or running the connector.

## Reference(s):

- [Databox homepage](https://databox.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Databox skill page](https://clawhub.ai/oomol/skills/oo-databox)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before running actions; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
