## Description:

L2S lets agents read, create, and update shortened URL records through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve L2S URL details, create shortened URLs, and update existing shortened URL records from an OOMOL-connected account. Write actions require confirming the exact payload and intended effect before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path asks users to execute a remote installer script for the oo CLI.

Mitigation: Review the installer source and prefer a verified installation method before using the skill.

Risk: Shortening or updating URLs changes state in the connected L2S account.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [L2S homepage](https://www.l2s.is)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-l2s)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
