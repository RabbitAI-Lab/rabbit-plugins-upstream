## Description:

This skill lets agents operate Deepgram through an OOMOL-connected account for Deepgram requests including searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Deepgram through an OOMOL-connected account, inspect live action schemas, and retrieve projects, models, balances, and API-key information without handling raw Deepgram tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer execution.

Mitigation: Review the setup path before installation and prefer installing the oo CLI from a verified, versioned source.

Risk: Project API-key listings are sensitive even when exposed as read actions.

Mitigation: Request API-key listings only when needed and avoid sharing the returned key information broadly.

## Reference(s):

- [Deepgram homepage](https://deepgram.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-deepgram)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Deepgram action data and execution metadata returned by the OOMOL connector.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
