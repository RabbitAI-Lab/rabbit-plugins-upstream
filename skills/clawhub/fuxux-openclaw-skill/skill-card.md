## Description:

Turn OpenClaw into a Fuxux social media manager for scheduling, publishing, queue review, media handling, drafts, and publishing analytics across connected social platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abogitoff](https://clawhub.ai/user/abogitoff)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an OpenClaw-compatible agent to Fuxux so it can draft, schedule, publish, inspect queues, and review publishing analytics for connected social accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Fuxux API key that can authorize account and posting actions.

Mitigation: Treat FUXUX_API_KEY like a password, keep it out of committed files and chat, and rotate it in Fuxux settings if exposed.

Risk: Immediate or bulk publishing can make content public across connected social accounts.

Mitigation: Use drafts for review when appropriate and confirm before bulk or immediate publishing.

Risk: Publishing may fail or target the wrong platform if account status is expired or requires reconnection.

Mitigation: List connected accounts before publishing and skip expired accounts or accounts with needs_reconnect set.

Risk: Agents following these instructions may read workspace files, including environment files.

Mitigation: Store only necessary secrets in the agent workspace and warn users before workflows that require access to local environment files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/abogitoff/skills/fuxux-openclaw-skill)
- [Server-resolved source repository](https://github.com/abogitoff/fuxux-openclaw-skill)
- [Fuxux OpenClaw guide](https://www.fuxux.com/openclaw)
- [Fuxux API reference](https://www.fuxux.com/reference)
- [Fuxux OpenAPI JSON](https://www.fuxux.com/openapi.json)
- [Fuxux MCP setup](https://www.fuxux.com/mcp/docs)
- [Fuxux MCP endpoint](https://www.fuxux.com/api/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline HTTP, JSON, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MCP configuration guidance and REST request examples for authenticated Fuxux workflows.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
