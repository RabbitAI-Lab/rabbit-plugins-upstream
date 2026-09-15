## Description:

Checks Chinese bill discount interest worksheets by recalculating line items, totals, duplicate bill numbers, and blanks while citing source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill before bill discounting to check whether a copied worksheet's interest, net proceeds, day counts, totals, duplicate bill numbers, and blanks match the stated 360-day basis. It reports missing material rather than drawing conclusions from incomplete inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes an optional paid upgrade flow that asks the agent to run an unpinned remote `npx ... @latest` command.

Mitigation: Do not run the upgrade command or authorize purchase/install through an agent unless the source and package version have been independently verified; prefer a sandboxed environment.

Risk: The free checker does not cover all validation cases, including rate range, inverted dates, non-positive face amounts, invalid net amounts, or day counts over 365.

Mitigation: Treat results as scoped worksheet checks only and review the listed non-executed checks before relying on the output.

Risk: Incomplete or unrecognized input material can lead to unsupported conclusions if handled outside the tool's stated behavior.

Mitigation: Use the tool's insufficient-input output as a stop condition and provide the required worksheet fields before making any conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/discount-interest-check-free)
- [SkillPay upgrade shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay install guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient inputs return missing-field guidance instead of a pass or fail conclusion.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
