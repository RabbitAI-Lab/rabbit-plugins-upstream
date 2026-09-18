## Description:

Checks property-fee and late-fee calculation sheets by recalculating line items, totals, duplicates, and blanks, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External property managers and business-operations teams use this skill to check monthly property-fee and late-fee tables before billing or collection follow-up. It helps surface arithmetic mismatches, total-row errors, duplicate customer rows, and missing required fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation and normal output steer users or agents toward installing an unpinned external payment package and buying another skill.

Mitigation: Use the local free checker only; do not run the external payment/onboarding command or delegate purchases unless the package and newly installed instructions are independently reviewed and each install or payment step is explicitly approved.

Risk: The free package omits several range and reasonableness checks, so passing output could be mistaken for a complete audit.

Mitigation: Treat results as arithmetic checks for the listed free scope only, and manually review withheld checks such as rate, days, month range, nonpositive area, and excessive late-fee conditions before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/property-fee-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [Purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Console text or JSON containing findings, summaries, executed checks, withheld checks, and source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; accepts a JSON file or pasted tabular text and can emit JSON with --json.]

## Skill Version(s):

1.0.6 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
