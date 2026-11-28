## Description:

Builds an evidence-grounded content strategy covering audience, pillars, sequencing, distribution, measurement, assumptions, and owner approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

Content strategists, marketers, SEO teams, and business owners use this skill to turn intake, content inventory, keyword, competitor, trust, and AI-visibility evidence into a prioritized content strategy. The output is a proposal until the owner explicitly approves it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to execute an unbundled validator from the active skills root, which could run unexpected code if that root is not trusted.

Mitigation: Install only in a trusted Groundcrew skills root and verify the groundcrew-doctor.py file before execution.

Risk: Connected mode may read SEO, analytics, or TrustGrowth data through configured connectors and API keys.

Mitigation: Use scoped API keys, avoid printing secrets, verify live connector documentation, and require approval before paid batches or TrustGrowth actions.

Risk: A generated strategy could be mistaken for an approved publishing decision.

Mitigation: Keep assumptions and unknowns visible, treat the strategy as a proposal, and require explicit owner approval before publishing or irreversible changes.

## Reference(s):

- [Connectors and categories](artifact/references/connectors.md)
- [Reporting contract](artifact/references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown strategy plan with evidence references, assumptions, unknowns, and approval status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector recommendations, qualitative priorities, and validation commands; does not produce a prioritized keyword list.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
