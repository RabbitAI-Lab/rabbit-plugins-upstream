## Description:

费用预算执行差异核对（免费）逐项核对预算执行表，执行逐行复算、合计勾稽、重复与空缺检测，并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill during monthly close, reconciliation, or inventory checks to validate budget execution tables for arithmetic consistency, totals, duplicate items, and missing required fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security verdict is suspicious because the free local checker also presents a paid-upgrade path.

Mitigation: Use the bundled free checker locally unless the paid upgrade is independently reviewed as a separate trust decision.

Risk: The artifact asks an agent to run an unpinned npx install command and initiate purchase and installation steps for the paid upgrade.

Mitigation: Do not run the npx command or authorize purchase/install steps until the package source, version, and payment flow are independently verified.

Risk: Budget execution tables can contain sensitive financial information.

Mitigation: Keep checks local and avoid sending source materials to external services unless the data owner has approved that workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/budget-variance-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay upgrade shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay purchase guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON report, with Markdown usage guidance and shell command examples in the skill instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard-library code; input is JSON or pasted budget-table text with headers; insufficient input returns no conclusion.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
