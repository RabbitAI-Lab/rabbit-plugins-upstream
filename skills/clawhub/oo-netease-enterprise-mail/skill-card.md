## Description:

Operates NetEase Enterprise Mail through an OOMOL-connected account for reading, searching, sending, replying, forwarding, moving, deleting, and downloading email content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees or agents with an OOMOL-connected NetEase Enterprise Mail account use this skill to inspect folders, search and read messages, download attachments, and manage or send email after confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup includes remote installer commands for the OOMOL CLI.

Mitigation: Review or verify the CLI installer through a trusted channel and do not allow an agent to run remote install commands automatically.

Risk: Sending, replying, forwarding, moving, deleting, or marking email changes NetEase Enterprise Mail account state.

Mitigation: Require explicit confirmation of the exact target, payload, and expected effect before running write or destructive actions.

Risk: Authentication, connection, and billing setup steps can affect account access or paid service usage.

Mitigation: Run setup or billing steps only after the matching command failure and with user approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-netease-enterprise-mail)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [NetEase Enterprise Mail homepage](https://qiye.163.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples; connector action results are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-injected credentials through the oo CLI; write and destructive mail actions require explicit confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
