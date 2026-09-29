## Description:

Provides supplier-name matching guidance and a local reconciliation report for comparing vendor aliases and canonical names.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and finance staff use this skill to generate supplier-name matching guidance and a local match report. Review the results against actual supplier records before relying on a match.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Matching reports may reflect generic rules or bundled sample names instead of actual supplier records.

Mitigation: Supply the intended structured supplier data and check results against registration details before accepting a match.

Risk: The downstream operation writes a local match report to the selected output directory.

Mitigation: Choose a writable directory appropriate for the data and review its contents before sharing or reuse.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/supplier-reconciliation-studio)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Files]

**Output Format:** [JSON results and a local match report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream operation writes a report under the caller-selected output directory; it does not confirm an external business action.]

## Skill Version(s):

3.0.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
