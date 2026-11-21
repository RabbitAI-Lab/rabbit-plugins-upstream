## Description:

Runs single-model or multi-model deliberations through mumo and returns model responses with typed reactions to support decision-making, reviews, and pressure tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericatmumo](https://clawhub.ai/user/ericatmumo)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to gather independent model perspectives on architecture choices, design reviews, launch risks, and decisions where hidden assumptions or costly mistakes matter. It summarizes the panel's responses and reactions to help users assess tradeoffs; the panel is advisory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marks the workflow suspicious because user context may be sent to external services without a clear privacy warning; scan evidence is partial.

Mitigation: Review prompt contents before use, and omit confidential code or operational details unless sharing them with the external services is approved.

## Reference(s):

- [Mumo product](https://mumo.chat)
- [Mumo MCP documentation](https://mumo.chat/docs/mcp)
- [Mumo API documentation](https://mumo.chat/docs/api)
- [OpenClaw install guide](https://mumo.chat/install/openclaw)
- [Reading reactions](references/reading-reactions.md)
- [Writing reactions](references/writing-reactions.md)
- [Synthesis guidance](references/synthesis.md)
- [Model selection](references/model-selection.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Decision-support guidance]

**Output Format:** [Markdown summary with model responses and typed cross-model reactions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory; using the mumo service requires a configured platform API key.]

## Skill Version(s):

0.8.0 (source: server-resolved release, CHANGELOG.md, released 2026-11-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
