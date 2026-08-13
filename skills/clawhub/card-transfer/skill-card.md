## Description:

Return transfer partners, transfer ratios, timing notes, and restrictions for one major-US credit card.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiahongc](https://clawhub.ai/user/jiahongc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer redemption-transfer questions for one exact major U.S. credit-card variant, including transfer partners, ratios, timing notes, restrictions, caveats, and confidence notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Current public issuer and secondary-source pages may change or disagree about transfer ratios, timing, bonuses, or restrictions.

Mitigation: Fetch the issuer page first, use an approved secondary source only when needed, and include confidence notes when details are uncertain.

Risk: An ambiguous card name can lead to transfer details for the wrong card variant.

Mitigation: Resolve the exact card variant first and stop for a numbered user choice list when the card is ambiguous.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with transfer-program sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visible output includes transfer program, transfer partners, transfer caveats, and confidence notes.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
