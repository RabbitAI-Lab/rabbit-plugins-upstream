## Description:

Checks inventory scrap and approval ledgers line by line for arithmetic, totals, duplicates, blanks, and negative values, with findings tied to source evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

Finance, cashier, inventory, and operations staff use this skill during monthly closing, reconciliation, or stocktaking to check inventory scrap and approval ledgers before downstream accounting or review work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documentation steers users toward an external unpinned installer, another skill's instructions, and a paid purchase workflow for the full version.

Mitigation: Use the free local checker independently unless the user separately trusts SkillPay, the Alipay package, the merchant product, and the newly installed skill instructions; treat installation, wallet authorization, and payment as separate explicit approval decisions.

Risk: The workflow and outputs are primarily Chinese-language, which can make review harder for users who cannot comfortably read the materials.

Mitigation: Deploy only where reviewers can understand the Chinese-language workflow and can independently verify the source ledger rows and cited findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/inventory-scrap-approval-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown-style text or JSON containing local ledger check results, missing-input notices, and executed-check summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with the bundled Node.js engine; insufficient material returns missing fields rather than a pass/fail conclusion.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
