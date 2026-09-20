## Description:

预付账款核销台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文，并仅执行本免费版引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

Finance and accounting users use this skill during monthly close, reconciliation, or inventory review to check prepayment offset ledgers for arithmetic mismatches, totals inconsistencies, duplicate supplier-contract rows, and missing required fields. It is intended for local review of supplied ledger text and does not make broader accounting judgments beyond the declared checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is a Chinese-language local ledger checker, which may be unsuitable for users who cannot review Chinese accounting output.

Mitigation: Install only when reviewers can understand the Chinese-language checks, findings, and limitations.

Risk: Documentation mentions anonymous statistics, while the authoritative security evidence reports no observed network transmission and flags this as stale wording.

Mitigation: Treat the statistics language as a documentation inconsistency and rely on current security evidence when assessing network behavior.

Risk: The free version intentionally omits some checks, including long-aging and selected overage or negative-amount checks.

Mitigation: Review the reported omitted checks before relying on the result, and use additional review for items outside the free version's scope.

Risk: If required ledger columns or usable rows are missing, the skill does not produce a reconciliation conclusion.

Mitigation: Provide a ledger with recognizable headers and supplier detail rows; treat insufficient-input output as no conclusion rather than a clean result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/prepayment-offset-check-free)

## Skill Output:

**Output Type(s):** [analysis, json, text, shell commands, guidance]

**Output Format:** [Human-readable text or JSON results with cited ledger lines, executed checks, omitted checks, findings, and insufficient-input messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs against user-supplied ledger text; sample input is provided as JSON.]

## Skill Version(s):

1.0.51 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
