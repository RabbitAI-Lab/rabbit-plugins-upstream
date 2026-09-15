## Description:

Runs a free local pre-check of bidding materials for bidder-level price arithmetic mismatches and leftover template placeholders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Bid preparers, procurement reviewers, and their agents use this skill before submission to check structured bidder line items for arithmetic mismatches and bidder document text for unfilled template placeholders. It supports a low-cost first pass and does not replace legal, procurement, or evaluation committee review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional upgrade path asks the agent to run an unpinned external installer and then follow newly installed skill instructions.

Mitigation: Treat the upgrade as a separate trust decision; verify the SkillPay source, package name, resolved version, installed contents, and any payment authorization before proceeding.

Risk: Procurement findings can be mistaken for a final compliance, legal, or bid evaluation decision.

Mitigation: Use the output as a mechanical pre-check only and require qualified human review before submission or evaluation decisions.

Risk: Incomplete bidder input can lead to skipped checks or unverifiable rows.

Mitigation: Provide a bidders array with each bidder's structured line items and/or document text, and treat insufficient-input or NOT_CHECKED results as missing evidence rather than clean results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tenderaudit-full-compliance-free)
- [Optional full-version SkillPay shelf referenced by the skill](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON containing executed checks, withheld checks, per-bidder findings, severity counts, and an overall verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with user-provided bidder input; reports insufficient input instead of producing a clean result from missing materials.]

## Skill Version(s):

1.1.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
