## Description:

Shop Savvy helps users compare products, search for coupons and discounts, summarize reviews, analyze value, and decide whether to buy now or wait.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill before purchases to compare products, search for coupons and discounts, summarize reviews, evaluate value, and decide whether to buy now or wait.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner workflow can keep local usage history and preferences.

Mitigation: Avoid recording sensitive shopping notes, periodically inspect or delete learned_patterns.json, or disable the learner workflow before use.

Risk: The artifact describes automatic edits to SKILL.md after repeated errors or use.

Mitigation: Review any proposed or automatic changes to SKILL.md before relying on the modified skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/shop-savvy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text shopping advice, comparison tables, review summaries, coupon search summaries, and optional learner shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist local usage history and preferences in learned_patterns.json when the learner workflow is used.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
