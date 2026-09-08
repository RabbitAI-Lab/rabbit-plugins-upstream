## Description:

PingRoom lets an OpenClaw agent contact a paired human through the `pingroom` CLI for phone notifications, questions, approvals, handoffs, live progress updates, attachments, links, locations, and incoming ping streams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pingroom](https://clawhub.ai/user/pingroom)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an agent needs to notify a person, request an answer, gate an action on approval, or send task context to a paired phone via PingRoom. It is suited to workflows where a real human decision or acknowledgement is required instead of agent inference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages, files, links, locations, room activity, and approval prompts are shared with the PingRoom service and delivered off-platform.

Mitigation: Send only the minimum task context the user has agreed to share, and ask first before including files, locations, or ambiguous sensitive content.

Risk: Pairing tokens, gift codes, and webhook URLs can grant access or reveal private workflow details if posted in public rooms or logs.

Mitigation: Keep these values out of public room messages and logs; use private pairing flows, managed credentials, or secret-backed environment configuration.

Risk: Approval and question workflows may be denied, cancelled, or expire without a human answer.

Mitigation: Treat exit codes distinctly and do not report a timeout as approval or as an answered question.

## Reference(s):

- [PingRoom OpenClaw command reference](https://pingroom.io/connect-openclaw.md)
- [ClawHub PingRoom skill page](https://clawhub.ai/pingroom/skills/pingroom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include blocking CLI commands whose exit codes represent human responses such as approval, denial, timeout, or cancellation.]

## Skill Version(s):

1.0.3 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
