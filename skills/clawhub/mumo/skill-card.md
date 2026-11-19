## Description:

Runs multi-model deliberations that provide independent responses and cross-model reactions to support architecture, design, and other consequential decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericatmumo](https://clawhub.ai/user/ericatmumo)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use mumo to review architecture choices, plans, designs, and other high-regret decisions through independent model perspectives and typed reactions. It is most useful when the cost of a mistaken decision outweighs the time and cost of deliberation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided problem context may be sent to an external multi-model service without a clear warning or sensitive-data check.

Mitigation: Avoid submitting confidential or personal information unless you have confirmed it is appropriate to share.

Risk: The security scan was partial because two local references in SKILL.md could not be resolved, leaving the evidence incomplete.

Mitigation: Resolve the referenced files and review the security assessment again before relying on it.

## Reference(s):

- [mumo on ClawHub](https://clawhub.ai/ericatmumo/skills/mumo)
- [mumo MCP documentation](https://mumo.chat/docs/mcp)
- [mumo API documentation](https://mumo.chat/docs/api)
- [OpenClaw installation guide](https://mumo.chat/install/openclaw)
- [OpenClaw documentation](https://docs.openclaw.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Model responses with typed cross-model reactions, claim maps, and optional round takeaways, presented as text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a mumo API key and sends user-provided prompts to an external multi-model service.]

## Skill Version(s):

0.7.0 (source: release metadata and CHANGELOG, released 2026-11-19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
