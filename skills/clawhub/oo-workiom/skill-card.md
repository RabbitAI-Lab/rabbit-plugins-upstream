## Description:

Workiom lets an agent read, create, and update Workiom data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Workiom apps, lists, metadata, and records, and to create records through a connected Workiom account after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can run a remote oo CLI installer without verification.

Mitigation: Install the oo CLI only through a trusted, verifiable method and do not let an agent run the remote installer automatically.

Risk: The create_record action changes Workiom data.

Mitigation: Confirm the exact target list, payload, and effect with the user before executing write actions.

## Reference(s):

- [Workiom homepage](https://workiom.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-workiom)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Workiom connector read actions and confirmed write actions through the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
