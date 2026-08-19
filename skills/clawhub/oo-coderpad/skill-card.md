## Description:

Enables an agent to operate CoderPad through an OOMOL-connected account, including reading organization, pad, question, and event data and creating interview pads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiting teams, and operations staff use this skill to inspect CoderPad organization and interview resources, review pad or question details, and create interview pads through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read potentially sensitive organization, interview pad, event, and question data through an OOMOL-connected CoderPad account.

Mitigation: Install only for users who need CoderPad access, and treat retrieved CoderPad data as sensitive workspace information.

Risk: The create-pad action changes CoderPad state.

Mitigation: Confirm the exact payload and intended effect with the user before approving any create-pad action.

Risk: Setup, login, and connector recovery steps can alter account connection state or require billing remediation.

Mitigation: Run setup or login commands only after an auth, connection, scope, expiry, app readiness, or billing error indicates they are needed.

## Reference(s):

- [CoderPad homepage](https://coderpad.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
