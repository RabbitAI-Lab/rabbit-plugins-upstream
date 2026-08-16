## Description:

Amilia helps agents search and read Amilia program and activity data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to retrieve Amilia activities and programs from an organization connected through OOMOL. It supports read workflows such as getting individual records and listing programs or program activities with filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Amilia program and activity data through an OOMOL-connected account.

Mitigation: Install it only when that account-level read access is intended, and keep use limited to the disclosed get and list actions.

Risk: Connector use depends on OOMOL CLI authentication, the Amilia app connection, and billing state.

Mitigation: Use the documented setup or recovery steps only after matching command failures, and avoid repeatedly initiating login or connection flows.

Risk: Future connector actions tagged as write or destructive could change Amilia data.

Mitigation: Confirm the exact payload and effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Amilia Skill](https://clawhub.ai/oomol/skills/oo-amilia)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Amilia Homepage](https://www.amilia.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL CLI commands and server-side credentials for listed read actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
