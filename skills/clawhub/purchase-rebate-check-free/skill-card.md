## Description:

Checks supplier purchase-rebate statements by recalculating earned rebates and differences, verifying totals, detecting duplicate or missing entries, and citing the source line for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Business operations and finance users can run this local checker against copied purchase-rebate tables to identify arithmetic mismatches, total-row errors, duplicate suppliers, and blank or placeholder fields before following up with suppliers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker instructions include an upgrade path that asks an agent to install payment software and start a paid SkillPay purchase workflow.

Mitigation: Run only the local free checker unless a human separately confirms intent to install payment tooling or purchase another skill after independent review.

Risk: The checker covers a limited free subset and does not decide contract reasonableness, tax treatment, cumulative rebate methods, quarterly rebates, or Excel parsing.

Mitigation: Use the reported executed and non-executed checks to bound conclusions, and have business or tax reviewers assess out-of-scope rebate terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/purchase-rebate-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON result objects with findings, summaries, executed checks, and non-executed checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each finding cites a source line when checks execute; insufficient input returns missing fields and advice rather than a pass/fail conclusion.]

## Skill Version(s):

1.0.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
