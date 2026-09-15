## Description:

Phonely helps an agent read Phonely data through an OOMOL-connected account, including accessible agents, call lists, call details, summaries, and transcripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Phonely read workflows through the oo CLI after their OOMOL account is connected. It is intended for retrieving Phonely agents, calls, call summaries, and transcripts without exposing raw credentials to the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands, which can be high impact if run automatically or without verification.

Mitigation: Do not let an agent run installer one-liners automatically; install the oo CLI only from a trusted source, preferably with pinned versioning and verification.

Risk: The workflow depends on an OOMOL account connection and may involve account scopes, credential expiry, or billing state.

Mitigation: Use connector commands only after the user understands the OOMOL account connection, scopes, and billing implications.

## Reference(s):

- [Phonely homepage](https://www.phonely.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Phonely Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-phonely)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON from the oo CLI when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
