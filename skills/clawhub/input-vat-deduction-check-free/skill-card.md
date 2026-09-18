## Description:

逐项核对进项税额认证与抵扣对照表，执行逐行复算、合计勾稽、重复月份和空白/占位符检测，并引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and bookkeeping users use this skill during monthly close, reconciliation, or review to check whether input VAT certification, transfer-out, and declared deduction figures reconcile. It reports missing materials instead of producing a conclusion when the provided table is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes paid-upgrade instructions that ask an agent to run an unpinned remote `npx ... @latest` install command outside the reviewed package.

Mitigation: Do not run the external purchase or install command unless the user independently verifies the SkillPay source, package identity, and payment flow.

Risk: The free local checker covers only the free-tier checks and withholds several additional tax consistency checks.

Mitigation: Review `checks_not_run` and the out-of-scope list before relying on results, and do not treat a clean result as tax advice or a complete VAT compliance review.

Risk: The security verdict is suspicious because the skill combines self-contained local code with external paid-install steering.

Mitigation: Use the bundled local Node.js checker only, scan the package before deployment, and keep payment or wallet authorization steps under direct human control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/input-vat-deduction-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [Purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON findings from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, source line, summary counts, executed checks, checks not run, and insufficiency messages when input cannot be checked.]

## Skill Version(s):

1.0.7 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
