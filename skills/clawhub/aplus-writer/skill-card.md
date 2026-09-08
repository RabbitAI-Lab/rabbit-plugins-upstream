## Description:

Plans Amazon A+ content modules, information hierarchy, and buyer-question responses from Amazon product details and review evidence; it does not create ads, images, or directly publish pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to plan A+ content from product-detail and review evidence. It helps structure modules, prioritize buyer concerns, and produce evidence-based listing guidance while preserving cost-confirmation and data-coverage boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access broad ARI account operations beyond narrow A+ planning.

Mitigation: Install it only when that account-level ARI access is intended, and review the requested operation before execution.

Risk: Paid ARI operations may run through account auto-confirm rules.

Mitigation: Review or disable auto-confirm spending rules, and use 'only quote, do not execute' when checking prices.

Risk: Recurring collection or monitoring settings can create ongoing costs.

Mitigation: Enable recurring collection or monitoring only after confirming the schedule, account limits, and expected cost.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/aplus-writer)
- [Amazon A+ operation workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional inline shell commands and links to generated reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may use paid ARI operations only after the applicable confirmation flow.]

## Skill Version(s):

1.4.8 (source: server release evidence, artifact frontmatter, and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
