## Description:

Use this skill for Resend (resend.com) requests that read, create, or update email data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Resend schemas, read sent and received email records, retrieve attachment metadata, and perform confirmed send or scheduled-email management actions through an OOMOL-connected Resend account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read email contents, headers, delivery state, attachment metadata, and temporary attachment links from the connected Resend account.

Mitigation: Install it only when the agent should access the OOMOL-connected Resend account, and limit prompts to the specific email data needed for the task.

Risk: Write actions can send email, send batch email, cancel scheduled email, or update scheduled delivery times.

Mitigation: Confirm the exact action, recipient, payload, and expected effect before allowing any send, batch send, cancel, or update command.

## Reference(s):

- [Resend homepage](https://resend.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-resend)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and execution metadata; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
