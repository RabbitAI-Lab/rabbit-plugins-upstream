## Description:

Publish or schedule social posts, inspect delivery, and manage automatic crossposting through a connected PostOnce MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[niyonx](https://clawhub.ai/user/niyonx)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to draft, publish, schedule, inspect, and manage crossposting for social posts through a configured PostOnce MCP connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured API key can allow an agent to draft, publish, schedule, upload media, or manage crossposting when requested.

Mitigation: Use a dedicated PostOnce API key with the narrowest needed scopes, keep it out of chat and files, and revoke it when it is no longer needed.

Risk: Publishing or crossposting to the wrong account, target, or time can create unintended public social content.

Mitigation: Review target accounts, schedule times, platform requirements, and delivery status before treating an operation as complete.

Risk: Retries after uncertain failures can duplicate drafts, posts, uploads, or workflows.

Mitigation: Use stable idempotency keys for mutating operations and inspect existing returned IDs or statuses before retrying.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/niyonx/skills/postonce)
- [PostOnce OpenClaw Integration](https://postonce.to/integrations/openclaw)
- [PostOnce API Documentation](https://docs.postonce.to)
- [PostOnce Plans](https://postonce.to/pricing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls, Markdown]

**Output Format:** [Markdown with inline shell commands and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post, draft, workflow, account, delivery status, and media upload handling details returned by PostOnce tools.]

## Skill Version(s):

0.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
