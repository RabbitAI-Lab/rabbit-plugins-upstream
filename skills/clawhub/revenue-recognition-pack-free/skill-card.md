## Description:

A local checker for revenue recognition and settlement worksheets that runs 7 built-in checks per project directory and prints one conclusion line per project with source file and line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue accountants and project finance teams at software, content, and service companies use this skill before monthly or quarterly revenue recognition and settlement reviews to run local consistency checks over exported text or JSON materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat worksheet consistency findings as accounting, audit, tax, contract-validity, or system-of-record conclusions.

Mitigation: Use the output as a local consistency screen and verify accounting conclusions against company policy and qualified reviewers.

Risk: Incomplete, stale, or incorrectly exported text/JSON materials can lead to missing checks, non-execution, or misleading findings.

Mitigation: Provide complete current materials for each project and review the source file and line citations attached to each finding.

Risk: The free edition omits cross-project summary tables, risk ranking, common-issue grouping, and ledger exports.

Mitigation: Perform separate aggregation and management review when cross-project reporting or prioritization is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/revenue-recognition-pack-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON summaries with per-project conclusions, issue counts, and source file line citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally over provided project directories or text/JSON inputs; results are printed to stdout and do not write files.]

## Skill Version(s):

1.0.17 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
