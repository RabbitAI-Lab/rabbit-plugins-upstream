## Description:

Helps Amazon sellers compare an ASIN's category star-rating and negative-review-rate position, with optional paid category leaderboards for recent popularity, negative-review rate, and average rating.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators and ecommerce analysts use this skill to benchmark a product's review position within a category, inspect category rankings, and decide where product or positioning changes may be needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some ARI workflows can spend credits automatically under server-side auto-confirm rules.

Mitigation: Before use, ask the agent to set confirmations to always ask, or use phrases such as "only quote, do not execute" when comparing products or requesting reports.

Risk: The skill exposes broader ARI account and analytics workflows than its benchmark-focused label suggests.

Mitigation: Review requested actions before execution and keep use scoped to the intended Amazon benchmark, leaderboard, and related review-analysis tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/industry-benchmark)
- [ARI API reference](artifact/references/reference.md)
- [Usage guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Text and Markdown, with shell commands when setup or troubleshooting is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report links, data range, sample-size notes, credit usage, and confirmation prompts for paid actions.]

## Skill Version(s):

1.4.7 (source: server release, frontmatter, changelog, CLI VERSION, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
