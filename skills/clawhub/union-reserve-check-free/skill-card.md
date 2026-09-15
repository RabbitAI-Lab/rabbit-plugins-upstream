## Description:

Runs a free local checker for 工会经费与残保金计提 tables, recalculating rows and totals while flagging duplicate periods, blanks, and source-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during monthly close, reconciliation, or review to check union fund and disability employment security fund accrual tables for arithmetic, totals, duplicate periods, blanks, and cited source lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional paid-upgrade instructions ask an agent to run an unpinned third-party installer and then follow newly installed external skill instructions.

Mitigation: Verify the SkillPay package source and exact version, avoid @latest where possible, review the downloaded skill before letting an agent follow it, and keep wallet authorization or payment confirmation manual.

Risk: The free checker intentionally omits several complete-version checks and does not return conclusions when required table material is missing.

Mitigation: Review the listed withheld checks and missing-input messages before relying on results, and provide complete source tables with headers for any accounting review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/union-reserve-check-free)
- [Sample input template](templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON from a local Node.js checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally according to artifact evidence; no API key or network is required for the free checker.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
