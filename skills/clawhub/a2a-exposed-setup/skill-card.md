## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to deploy and configure a public A2A endpoint, set up wake delivery or polling, and verify that an agent can receive and handle a real message.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious with medium confidence due to unpinned CLI package recommendations and flagged destructive and out-of-scope operations; this verdict does not establish harmful intent.

Mitigation: Review CLI and teardown or automation steps before use, pin a reviewed CLI version where practical, and require human confirmation before destructive changes.

Risk: The security scan is incomplete because four local references were unresolved.

Mitigation: Review the unresolved references and complete the security scan before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed-setup)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted setup overview](https://a2a.exposed/hosted)
- [Getting started guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Hosted MCP endpoint](https://a2a.exposed/mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, Guidance]

**Output Format:** [Markdown guidance with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stepwise setup and verification instructions; secrets are handled through protected storage.]

## Skill Version(s):

0.8.70 (source: server-resolved release metadata, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
