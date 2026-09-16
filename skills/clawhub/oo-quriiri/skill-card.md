## Description:

Quriiri (quriiri.fi). Use this skill for ANY Quriiri request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Quriiri SMS workflows through an OOMOL-connected account, including sending SMS messages and checking delivery status. It is useful when an agent needs Quriiri data access without calling the Quriiri API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review installer commands before use and prefer installing the oo CLI through a verified package or documented manual process.

Risk: The send_sms action changes external state by sending an SMS message.

Mitigation: Confirm the exact SMS payload and intended effect with the user before allowing the write action.

## Reference(s):

- [Quriiri homepage](https://quriiri.fi/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Quriiri ClawHub release](https://clawhub.ai/oomol/skills/oo-quriiri)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that read Quriiri SMS data or, after explicit user confirmation, send SMS messages.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
