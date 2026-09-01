## Description:

Compares recorded Amazon product-page price snapshots for a main ASIN and authorized competitors to explain relative price position, timestamp, and evidence gaps without claiming realtime prices or supporting sales, profit, inventory, order, or repricing decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to compare a main ASIN with authorized competitor product-page snapshots, understand price positioning at a point in time, and identify evidence gaps before making business decisions.

### Deployment Geography for Use:

Global, limited to supported Amazon marketplaces documented by the skill: US, UK, Germany, Japan, Canada, France, Spain, and Italy.

## Known Risks and Mitigations:

Risk: The packaged ARI tool exposes broader account capabilities than the narrow price-positioning description suggests.

Mitigation: Install only when broad ARI account access is acceptable, and limit the agent to commands needed for the requested workflow.

Risk: Paid actions can consume ARI credits, and interrupted streams may already have completed server-side.

Mitigation: Require a quote and explicit confirmation before any paid command, and check existing reports or operation status before retrying a confirmed action.

Risk: Schedules and watches can continue collecting data after the immediate analysis is complete.

Mitigation: Require explicit approval before creating, resuming, or changing monitoring, and review active schedules or watches after use.

Risk: An ARI API key provides access to the user's ARI account.

Mitigation: Keep the key out of prompts, reports, examples, and screenshots, and revoke it when the integration is no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/competitor-price)
- [Operation workflow](artifact/references/operation-workflow.md)
- [ARI command reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and command-oriented guidance, with ARI CLI output summarized for the user.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid actions or monitoring changes.]

## Skill Version(s):

1.4.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
