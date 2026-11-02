## Description:

Email and calendar for your OpenClaw agent through the GigaMail MCP server — read, search, draft, reply, schedule — with every destructive action (send, delete, calendar write) held for out-of-band human approval that the agent cannot grant itself.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adecubed](https://clawhub.ai/user/adecubed)

### License/Terms of Use:

MIT-0

## Use Case:

People using OpenClaw can use this skill to read and search connected email, review calendar availability, draft replies, and work with calendar or Drive content. Actions such as sending, deleting, or changing calendar data require approval outside the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email and knowledge-file content may enter the model provider’s context.

Mitigation: Connect only accounts and files that you want the agent to read.

Risk: Sending, deleting, or changing calendar data affects real accounts.

Mitigation: Review each action preview and verify the installed server’s out-of-band approval behavior before approving.

Risk: Automatic reply rules can send messages within configured limits.

Mitigation: Enable automatic replies only with suitable limits.

## Reference(s):

- [GigaMail](https://gigamail.ai)
- [GigaMail on ClawHub](https://clawhub.ai/adecubed/skills/gigamail)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural language responses and email or calendar drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include summaries, search results, proposed times, and approval previews.]

## Skill Version(s):

0.4.0 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
