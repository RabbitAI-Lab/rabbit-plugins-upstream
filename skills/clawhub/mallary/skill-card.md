## Description:

Use this skill only when the user explicitly asks to inspect, set up, or act through Mallary, the Mallary CLI, the Mallary API, Mallary MCP, or an existing Mallary workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sammydigits](https://clawhub.ai/user/sammydigits)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, CI maintainers, and AI agents use this skill to inspect Mallary state, set up authentication, and carry out explicit user-requested Mallary workflows such as publishing, scheduling, media upload for a post, replies, and account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth or an API key grants broad Mallary access and can authorize publishing, engagement, and account-management actions.

Mitigation: Use browser OAuth only for explicit setup requests, keep API keys in a secret manager or masked environment, and never request or print credentials in chat or logs.

Risk: A clear request to publish, schedule, upload media for a post, or send a reply can create public or scheduled social content without a second confirmation.

Mitigation: Resolve the exact profile, destination, content, files, and timing before acting, keep the action within the request, run it once, and verify with a read-only command.

Risk: Read-only Mallary discovery can expose sensitive profile IDs, account labels, post content, analytics, settings, webhook destinations, and provider metadata.

Mitigation: Request only the data needed for the user's Mallary task and redact sensitive operational identifiers and metadata before sharing output.

Risk: Deletion, platform disconnection, webhook changes, and settings updates can affect remote data, public behavior, or account access.

Mitigation: Use read-only discovery to identify the target and confirm target and effect when the current request does not already clearly identify both and ask to execute now.

## Reference(s):

- [ClawHub Mallary Skill Page](https://clawhub.ai/sammydigits/skills/mallary)
- [Mallary Website](https://mallary.ai/)
- [Mallary Docs](https://docs.mallary.ai)
- [Mallary CLI npm Package](https://www.npmjs.com/package/@mallary/cli)
- [Mallary Agent Repository](https://github.com/mallarylabs/mallary-agent)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may guide read-only discovery and user-authorized Mallary CLI actions; executable write syntax is intentionally limited in the artifact.]

## Skill Version(s):

1.1.2 (source: server release metadata; artifact frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
