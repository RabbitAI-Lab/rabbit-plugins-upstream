## Description:

Provides a free deterministic local check of 材料成本差异分摊核对表, with source-cited findings for row arithmetic, totals, duplicate rows, blanks or placeholders, and negative plan-cost amounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during month-end close, reconciliation, or inventory checks to validate material-cost variance allocation tables. It helps agents run a local Node.js checker, interpret source-cited findings, and avoid conclusions when required table evidence is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free release intentionally omits several checks that are listed as not included, so a clean result is limited to the executed checks.

Mitigation: Treat findings as coverage for the listed free checks only, and run separate accounting review or the complete tool for omitted checks when those controls matter.

Risk: Security guidance notes that the help text mentions anonymous usage statistics, while the scan found no implemented network calls or persistence.

Mitigation: Review the installed release notes and run in an offline or sandboxed environment if telemetry statements affect deployment policy.

Risk: The tool is a deterministic table checker and does not decide the accounting policy or allocation basis.

Mitigation: Have qualified accounting staff confirm the policy basis and use the tool only for table arithmetic, totals, duplicates, blanks, and stated in-scope checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/material-cost-variance-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON result report from a local Node.js checker, with human-facing guidance and example shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads a user-specified local JSON or text input file, supports a bundled sample, and withholds conclusions when required columns or rows are insufficient.]

## Skill Version(s):

1.0.52 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
