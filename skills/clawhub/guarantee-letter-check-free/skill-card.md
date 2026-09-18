## Description:

银行保函台账逐项核对，复算保函金额、到期日、保函号唯一性、注销状态自洽性和到期未注销额度占用，并为结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance, credit-management, construction, trade, and manufacturing teams use this skill to check Chinese-language bank guarantee ledgers for amount, maturity, status, duplicate-number, and occupied-credit inconsistencies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill steers users toward a paid add-on that involves an unpinned remote installer and payment authorization.

Mitigation: Do not run the remote payment installer or authorize purchases unless the provider, package, and payment flow have been independently verified.

Risk: The free release omits several advanced checks, so its findings are not a complete guarantee-letter risk review.

Mitigation: Review the reported checks-not-run list before relying on the result for credit-limit, release-schedule, or full exposure decisions.

Risk: The security summary reports an under-disclosed prompt marker.

Mitigation: Review the skill instructions and runtime output before deployment, especially any paid-upgrade or version-choice prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/guarantee-letter-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Chinese-language Markdown or JSON with line-cited ledger findings and missing-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided ledger text; the free release reports checks that were executed and checks that were not run.]

## Skill Version(s):

1.0.1 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
