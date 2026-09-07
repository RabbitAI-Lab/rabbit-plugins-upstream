## Description:

Use Helena, Enrich Labs' AI marketing agent, to research, plan, create, schedule, publish, and analyze marketing for a connected brand.

This skill is ready for commercial/non-commercial use.

## Publisher:

[enrichlabs](https://clawhub.ai/user/enrichlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and external users use this skill to connect OpenClaw to Helena for brand-aware marketing research, planning, drafting, scheduling, publishing, and analysis through their Enrich Labs account and connected marketing platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helena can publish content, contact people, spend money, change live campaigns, or delete data when the user authorizes those actions.

Mitigation: Clarify ambiguous live actions and request them only after explicit user approval.

Risk: The skill connects OpenClaw to an Enrich Labs account and connected marketing platforms through OAuth.

Mitigation: Use the browser OAuth flow or safe headless fallback, and never request passwords, OAuth codes, access tokens, or refresh tokens in chat.

Risk: Delegated marketing tasks may involve brand, audience, campaign, or account context.

Mitigation: Send only the information needed for the task and avoid unrelated secrets or private conversation history.

## Reference(s):

- [Helena Skill Page](https://clawhub.ai/enrichlabs/skills/helena)
- [Enrich Labs MCP](https://enrichlabs.ai/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and delegated MCP responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links and image assets returned by Helena; live publishing, spending, deletion, or campaign changes require explicit user authorization.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
