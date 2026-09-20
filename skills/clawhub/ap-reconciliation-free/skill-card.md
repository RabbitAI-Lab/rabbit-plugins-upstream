## Description:

A free local supplier accounts-payable reconciliation checker that validates line arithmetic, totals, duplicate suppliers, and blank fields while citing source lines for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounts payable, treasury, and warehouse staff use this skill during month-end or periodic supplier reconciliation to check supplier payable tables for arithmetic consistency, mismatches, duplicates, and missing values. It is intended as a deterministic reconciliation aid, not as payment, audit, tax, or legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplier payable reconciliation tables can contain sensitive business information.

Mitigation: Run the skill only on files the agent is intended to read and handle both inputs and outputs as sensitive finance material.

Risk: Users may over-rely on arithmetic findings as payment, audit, tax, or legal conclusions.

Mitigation: Treat results as deterministic arithmetic checks and require finance review before payment decisions or formal audit, tax, or legal use.

Risk: The free edition does not execute the documented withheld checks, including payment-direction anomalies and difference-rate threshold checks.

Mitigation: Review the reported checks not run and use a broader reconciliation process when those checks are required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ap-reconciliation-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, analysis, shell commands, guidance]

**Output Format:** [Plain text or JSON reconciliation results with findings, summaries, cited source lines, checks executed, and checks not run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries; reads user-provided table text or JSON and does not use network access or persistence according to server security evidence.]

## Skill Version(s):

1.0.60 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
