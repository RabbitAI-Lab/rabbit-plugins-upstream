## Description:

CoderPad enables agents to read CoderPad data and create interview pads through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and recruiting teams use this skill to operate CoderPad interview pads, questions, organization data, and usage statistics from an authenticated OOMOL/CoderPad account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read actions can expose organization, pad, question, and event data from CoderPad.

Mitigation: Install the skill only when the agent should access CoderPad through the OOMOL-connected account, and review requested reads against the user's intent.

Risk: The create_pad action can change CoderPad state.

Mitigation: Confirm the exact create_pad payload and expected effect before approving execution.

Risk: Connector access can fail when authentication, connection scope, credentials, or billing are missing or expired.

Mitigation: Use the documented setup and recovery steps only after a command returns the matching error.

## Reference(s):

- [ClawHub CoderPad skill page](https://clawhub.ai/oomol/skills/oo-coderpad)
- [CoderPad homepage](https://coderpad.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command results are returned as JSON when the agent executes the documented oo CLI commands.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
