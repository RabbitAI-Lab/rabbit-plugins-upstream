## Description:

Luckin Coffee lets an agent search stores and products, preview orders, inspect order details, and create or cancel orders through an OOMOL-connected Luckin Coffee account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to work with a connected Luckin Coffee account, including store discovery, product search, order preview, order detail lookup, and confirmed order creation or cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can preview, create, and cancel real Luckin Coffee orders through a connected account.

Mitigation: Require explicit user confirmation for createOrder and cancelOrder, including the exact order or payload and expected effect.

Risk: First-time setup includes remote installer commands that could be unsafe if run blindly.

Mitigation: Prefer a verified, pinned, official installation path and only run setup commands after an auth or connection failure requires them.

Risk: Security review marked the release suspicious because real ordering and cancellation power is mixed with read-only wording.

Mitigation: Review before installing and treat createOrder and cancelOrder as sensitive actions even when not tagged in the skill text.

## Reference(s):

- [Luckin Coffee MCP homepage](https://open.lkcoffee.com/mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-luckin-coffee)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and JSON responses from the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
