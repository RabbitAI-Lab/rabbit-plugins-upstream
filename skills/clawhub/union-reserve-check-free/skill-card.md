## Description:

工会经费与残保金计提表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during month-end closing, reconciliation, or review to check union fund and disability fund accrual tables for arithmetic, totals, duplicate periods, blanks, and source-cited discrepancies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker itself runs locally, but its documentation and normal text output steer users toward installing an unpinned external payment package and buying another skill.

Mitigation: Use the free checker only for local table review and do not run the payment-package installation or purchase flow unless the package, merchant, and payment flow have been independently trusted.

Risk: The free version withholds five checks, so users may mistake a clean free run for complete validation.

Mitigation: Review the listed included and withheld checks before relying on results, and do not treat a free-version pass as full coverage of all union fund and disability fund checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/union-reserve-check-free)

## Skill Output:

**Output Type(s):** [text, json, guidance, shell commands]

**Output Format:** [Human-readable text or JSON results with source-cited findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against provided table text; insufficient input returns missing fields instead of a conclusion.]

## Skill Version(s):

1.0.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
