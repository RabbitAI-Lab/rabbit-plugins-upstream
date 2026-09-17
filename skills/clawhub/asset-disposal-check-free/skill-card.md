## Description:

对固定资产处置表执行逐行复算、合计勾稽、重复与空缺检测，并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during month-end close, reconciliation, asset inventory, or disposal review to check whether fixed-asset disposal rows and totals are internally consistent. The free version covers the checker-declared free checks and reports missing input instead of fabricating conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill text includes an unpinned external `npx ... @latest` install path and purchase flow that could cause an agent to install changing code or proceed toward payment.

Mitigation: Use only the local free checker unless a human manually verifies the package source and version, and keep wallet authorization, payment confirmation, and any follow-on installation under direct user control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/asset-disposal-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Plain text findings by default, with optional JSON output from the local Node.js checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include line-level evidence when checks run; insufficient input returns missing-field guidance and no conclusion.]

## Skill Version(s):

1.0.7 (source: evidence.release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
