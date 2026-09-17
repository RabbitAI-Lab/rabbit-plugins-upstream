## Description:

Altoviz operates Altoviz customer data through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read and update Altoviz customer records through an OOMOL-connected account, including customer creation, lookup, retrieval, and paginated listing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions run remote installer scripts directly.

Mitigation: Review the oo CLI installation path before use; prefer a pinned, signed, or checksum-verified installer from OOMOL, and do not let an agent run remote install commands automatically.

Risk: Altoviz write actions can change customer data.

Mitigation: Confirm the exact payload and expected customer data change with the user before running write actions.

## Reference(s):

- [Altoviz homepage](https://altoviz.com/en/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Altoviz connection setup](https://console.oomol.com/app-connections?provider=altoviz)
- [ClawHub Altoviz skill page](https://clawhub.ai/oomol/skills/oo-altoviz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
