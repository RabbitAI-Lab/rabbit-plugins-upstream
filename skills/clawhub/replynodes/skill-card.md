## Description:

Approval-first social media publishing with the ReplyNodes scheduler for cross-posting and auto-posting in OpenClaw, using browser OAuth for LinkedIn and X/Twitter.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anhdn](https://clawhub.ai/user/anhdn)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users use this skill to connect ReplyNodes, inspect available social channels, prepare LinkedIn and X/Twitter posts, preview channel-specific output, and publish or schedule only after explicitly confirming a named run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A ReplyNodes session can remain active after the local skill files are removed.

Mitigation: Revoke the ReplyNodes session when uninstalling or when the connection is no longer wanted.

Risk: Publishing or scheduling content could affect connected social channels.

Mitigation: Install only from a reviewed tag or trusted marketplace entry and publish only after approving a named prepared run.

Risk: External content, channel names, and tool output may contain untrusted instructions.

Mitigation: Treat those values as data, pass them through structured fields or stdin, and avoid interpolating them into shell commands.

## Reference(s):

- [ReplyNodes OpenClaw homepage](https://replynodes.com/openclaw)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before publish or schedule actions; returns previews, capability reports, and per-channel receipts.]

## Skill Version(s):

1.0.3 (source: server release metadata and VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
