## Description:

一次把多家投标文件的报价算术全部核一遍，不需要付款，也不需要注册。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and bid-review teams use this skill to run local batch arithmetic checks across bidder quote line items and identify bidders or rows that need closer review. It is a helper for quote math review, not a bid evaluation decision or legal determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the free checker points users or agents toward an unpinned third-party install-and-purchase flow for an upgraded skill.

Mitigation: Do not let an agent run the paid-edition install or purchase flow automatically; review the payment tooling source, pin or inspect the exact package version, and require explicit human approval for install, wallet, and payment steps.

Risk: The artifact positions outputs as AI arithmetic checks, which could be mistaken for bid evaluation findings.

Mitigation: Use the results as review aids only; keep human review responsible for bid evaluation, qualification, and legal determinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bidcheckup-batch-compliance-free)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance and optional JSON result output from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports checks performed, checks withheld, per-bidder verdicts, findings, missing-input guidance, and a disclaimer that results are arithmetic checks rather than bid decisions.]

## Skill Version(s):

1.0.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
