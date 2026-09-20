## Description:

Checks property maintenance fund collection and per-household apportionment tables with six deterministic local checks, citing source lines and figures for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Property managers, finance staff, and homeowners committee finance reviewers use this skill before public maintenance-fund disclosure or after fund use to reconcile collection ledgers, use ledgers, apportionment details, voting ratios, and balances. It provides arithmetic and format checks, not legal, audit, engineering-cost, or banking verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inputs may contain sensitive property, owner, and financial records.

Mitigation: Use redacted input where possible, keep the skill running locally, and avoid sharing generated findings outside the intended review process.

Risk: The findings are arithmetic and table-format checks, not legal, audit, engineering-cost, or banking verification.

Mitigation: Have qualified reviewers confirm legal eligibility, voting procedure, bank records, and audit conclusions before acting on the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/property-maintenance-fund-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON findings with source line numbers, figures, summaries, checks executed, and checks not run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard-library code; material that lacks required headers or rows returns insufficient-input guidance rather than a conclusion.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
