## Description:

进口税费计算表逐项核对（逐行算术复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External importers, freight forwarders, customs operations teams, and finance reviewers use this skill before payment to recheck copied import-duty worksheet arithmetic and line-level totals. It reports missing inputs instead of producing a conclusion when the worksheet lacks required columns or rows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes optional paid-upgrade instructions that direct users to an unpinned external installer and payment flow.

Mitigation: Independently verify the Alipay/SkillPay source, package name, exact version, and payment details; run any installer in a constrained environment and personally approve wallet or payment steps.

Risk: Users may overread arithmetic findings as tax, customs, or legal advice.

Mitigation: Treat output only as worksheet arithmetic checking and confirm customs classifications, rates, valuation, and payment decisions with qualified review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/import-duty-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands; the local checker can emit human-readable text or JSON findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers and the checker declares withheld and out-of-scope checks.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
