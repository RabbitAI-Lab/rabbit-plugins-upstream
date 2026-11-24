## Description:

Runs a multi-model deliberation across models from different labs via mumo's MCP server, returning full responses plus typed cross-model reactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericatmumo](https://clawhub.ai/user/ericatmumo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and OpenClaw developers use mumo to gather independent perspectives on architecture, product, design, and security-sensitive decisions before committing to a course of action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may send user context to external model providers without a sensitivity check or warning; the security scan was partial, so its evidence is incomplete.

Mitigation: Avoid submitting confidential information unless external processing is permitted, and review the unresolved references before relying on the scan.

## Reference(s):

- [Mumo MCP documentation](https://mumo.chat/docs/mcp)
- [Mumo API documentation](https://mumo.chat/docs/api)
- [OpenClaw installation guide](https://mumo.chat/install/openclaw)
- [Mumo ClawHub listing](https://clawhub.ai/ericatmumo/skills/mumo)
- [Model selection](artifact/references/model-selection.md)
- [Synthesis guidance](artifact/references/synthesis.md)
- [Reading reactions](artifact/references/reading-reactions.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown text containing model responses and typed cross-model reactions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full model responses with cross-model reactions; available perspectives depend on the models selected and successfully responding.]

## Skill Version(s):

0.9.0 (source: release evidence and CHANGELOG, released 2026-11-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
