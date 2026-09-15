## Description:

CommPeak enables agents to read, create, and update CommPeak account data, including TextPeak streams, messages, domains, senders, and SMS sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected CommPeak account through the OOMOL oo CLI, including listing TextPeak resources and sending SMS after confirming the payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can direct users to execute unverified remote installer scripts.

Mitigation: Review the installer path before installation and prefer a versioned, verifiable oo CLI installation method.

Risk: The send_sms action changes CommPeak account state and can send one or more SMS messages.

Mitigation: Confirm the exact send_sms payload, recipients, and expected effect with the user before allowing execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-commpeak)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [CommPeak Homepage](https://www.commpeak.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON; write actions require payload and effect confirmation before execution.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
