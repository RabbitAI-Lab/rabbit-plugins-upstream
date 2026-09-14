## Description:

一次把多家投标文件的报价算术全部核一遍，不需要付款，也不需要注册；本免费版执行逐家报价算术校验。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, bid review, and project teams use this skill to run a local mechanical arithmetic check across multiple bidders' quote line items. It helps identify mismatches between quantity, unit price, and amount before human review, but it does not make procurement, scoring, qualification, or legal determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat mechanical arithmetic results as a procurement, scoring, legal, or bid-validity decision.

Mitigation: Present the output as a calculation aid only and require qualified human review before any procurement action.

Risk: Incomplete or malformed bidder data can produce NOT_CHECKED or insufficient-input results that do not cover all bidders or line items.

Mitigation: Review checks_given, checks_withheld, NOT_CHECKED bidders, and insufficiency messages; provide structured bidders with item name, quantity, unit price, and amount where possible.

Risk: The free release intentionally omits checks such as qualification review, substantive response review, collusion signals, and price dispersion analysis.

Mitigation: Use the result only for 逐家报价算术校验 and keep separate review processes for all withheld compliance checks.

Risk: Bid materials can contain sensitive commercial information.

Mitigation: Run the local checker only with bid data intended for this arithmetic check and avoid adding unrelated sensitive material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bidcheckup-batch-compliance-free)
- [Free web checker](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable terminal text or structured JSON containing executed checks, withheld checks, per-bidder verdicts, findings, summaries, and insufficiency guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally under Node.js; returns exit code 0 for completed checks, 3 for insufficient input, and no conclusion when no verifiable quote rows are available.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
