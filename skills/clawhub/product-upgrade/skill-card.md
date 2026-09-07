## Description:

Combines Amazon product detail and review evidence to plan product upgrade directions and validation questions, without forecasting sales, placing purchases, or automatically changing listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT

## Use Case:

External Amazon operators and product teams use this skill to turn product details and review evidence into prioritized upgrade opportunities, validation questions, and concise operating recommendations. It is intended for review-grounded product planning, not automated listing changes or purchasing decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to an ARI API key and can interact with the user's ARI account.

Mitigation: Install only when the user is comfortable granting that account access, and avoid sharing or embedding the API key in reports, prompts, or command examples.

Risk: Paid analysis may spend ARI credits, and some flows may execute under account auto-confirm rules.

Mitigation: Use quote-only requests when comparing costs, set auto-confirm to always ask when per-report approval is needed, and confirm paid runs only after reviewing the quoted cost.

Risk: Schedule, watch, and competitor commands can create ongoing monitoring or future collection costs.

Mitigation: Explain the monitoring scope and expected cost before enabling these commands, and require explicit user agreement for ongoing changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/product-upgrade)
- [README](README.md)
- [Operation workflow](references/operation-workflow.md)
- [ARI CLI and API reference](references/reference.md)
- [Usage guide](使用说明.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise conversational guidance with occasional shell command invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and product ASIN/site context; paid analysis and ongoing monitoring must follow ARI quote and confirmation rules.]

## Skill Version(s):

1.4.7 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
