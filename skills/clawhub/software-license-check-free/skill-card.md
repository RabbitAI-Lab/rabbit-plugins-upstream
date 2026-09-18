## Description:

Checks software license and cloud resource ledgers locally for cost math, term-month consistency, over-installation, duplicate rows, totals, missing fields, negative values, and inverted dates, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

IT asset managers, finance teams, and agents supporting them use this skill to check software license and cloud resource ledgers before budget reviews, renewals, or audits. It reports deterministic table consistency findings with source line references and states when input is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paid-upgrade path includes an unpinned external installer and prewritten purchase authorization text.

Mitigation: Verify the SkillPay/Alipay source, merchant, product identifiers, and package version independently before running installer commands or proceeding with payment.

Risk: The skill writes a temp marker file to avoid repeated upsell prompts.

Mitigation: Expect this local marker behavior and review or remove the temp marker if prompt state needs to be reset.

Risk: The checker reports deterministic table relationships and does not evaluate software vendor contract terms, actual usage logs, cloud list prices, legal compliance, or spreadsheet files directly.

Mitigation: Use its findings as ledger consistency checks only, export spreadsheets to text or JSON first, and have responsible staff validate contract, pricing, and compliance conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/software-license-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON, often summarized by the agent in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields rather than a clean result.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
