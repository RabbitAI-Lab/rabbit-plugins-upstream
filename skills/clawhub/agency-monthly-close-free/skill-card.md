## Description:

Batch monthly-close self-check for bookkeeping agencies that runs seven industry check packs across client folders, emits one result line per client, and cites source files and lines for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Bookkeeping agency staff and supervisors use this skill before monthly client delivery to run local arithmetic and reconciliation checks across all client folders, identify missing materials, and review findings with source file and line references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads the client folders supplied to it, which may contain sensitive bookkeeping material.

Mitigation: Run it only on intended client directories and exclude unrelated or unnecessary files before execution.

Risk: Monthly-close findings are advisory checks and may be mistaken for accounting, legal, tax, or audit assurance.

Mitigation: Have qualified staff review the cited source lines and use the output as reconciliation support, not as a final professional opinion.

Risk: Missing or malformed client materials can produce not-run statuses that may be misread as clean results.

Mitigation: Review missing-material and not-run statuses for each client before treating a monthly close as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/agency-monthly-close-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON summaries with per-client results, finding counts, missing-material status, and source file and line citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are advisory monthly-close checks printed to stdout; the skill does not provide accounting, legal, tax, or audit assurance.]

## Skill Version(s):

1.0.27 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
