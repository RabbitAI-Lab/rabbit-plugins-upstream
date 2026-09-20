## Description:

A Chinese-language local checker for store sales report tables that recalculates row totals, compares reported revenue against channel totals, detects duplicates and blanks, and cites source line numbers for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Store operations and finance teams use this skill to check Chinese store sales report tables before escalation or review. It helps identify arithmetic inconsistencies, duplicate store-date rows, missing required cells, and cases where available inputs are insufficient for a conclusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users could treat table consistency findings as an audit opinion or proof that all revenue was captured.

Mitigation: Use the output as arithmetic and completeness checking only, and review the underlying POS, platform, and accounting records before making audit or financial decisions.

Risk: The release documentation contains conflicting statements about no-network behavior and anonymous usage statistics.

Mitigation: Rely on the inspected version's security evidence for deployment review, and ask the publisher to clarify telemetry wording before broad rollout.

Risk: The free edition omits checks such as negative amounts, threshold-based differences, zero channel totals with nonzero reported revenue, and difference-rate checks.

Mitigation: Review the listed checks not run, and do not assume omitted conditions were evaluated.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/store-sales-report-check-free)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown instructions and local Node command output, with optional JSON findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers and distinguish executed checks from checks not included in the free edition.]

## Skill Version(s):

1.0.28 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
