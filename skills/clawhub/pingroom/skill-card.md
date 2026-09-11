## Description:

Reach a human through PingRoom from an OpenClaw agent using the `pingroom` CLI to send notifications, files, links, locations, acknowledgement requests, questions, approvals, handoffs, live progress, incoming-ping streams, and promotional-code redemption requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pingroom](https://clawhub.ai/user/pingroom)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw agents use this skill when a workflow needs to notify a human, ask a question, require approval, hand off a decision, stream progress, receive pings, or redeem a PingRoom code through the PingRoom CLI. It is intended for human-in-the-loop operational workflows where messages, attachments, links, locations, or room content are shared only with user consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages, attachments, links, locations, and room content may be sent to the PingRoom service and delivered to a paired human's phone.

Mitigation: Confirm user consent before sharing private files, locations, room content, or ambiguous content off-platform, and send only the minimum information required for the task.

Risk: PingRoom tokens, credentials.json, webhook URLs, attachments, and promotional codes are sensitive.

Mitigation: Keep credentials and codes out of public messages and logs, restrict credential file access, inspect attachment URLs before allowing downloads, and use the pinned local runtime described by the artifact.

## Reference(s):

- [PingRoom OpenClaw command reference](https://pingroom.io/connect-openclaw.md)
- [ClawHub skill page](https://clawhub.ai/pingroom/skills/pingroom)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes CLI setup steps, command examples, exit-code handling, configuration guidance, and privacy cautions for PingRoom operations.]

## Skill Version(s):

1.1.1 (source: frontmatter, package.json, package-lock.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
