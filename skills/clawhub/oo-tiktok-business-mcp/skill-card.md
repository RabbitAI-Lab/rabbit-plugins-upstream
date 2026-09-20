## Description:

Operates TikTok for Business through OOMOL's tiktok_business_mcp connector so agents can inspect available tools and run account actions through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to discover TikTok for Business MCP tools and invoke read or account-changing actions through an OOMOL-connected TikTok for Business account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected TikTok for Business tools may change budgets, ads, delivery, access, or advertising assets.

Mitigation: Require explicit user confirmation of the exact payload, target, and expected effect before write or destructive actions.

Risk: The skill includes remote installer commands for the oo CLI.

Mitigation: Prefer a verifiable package or reviewed installer before installing the CLI.

Risk: The connected account can give OOMOL broad operational reach into TikTok for Business workflows.

Mitigation: Install only when the publisher is trusted and the connected account scopes match the intended task.

## Reference(s):

- [TikTok for Business](https://business.tiktok.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-tiktok-business-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs may return JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
