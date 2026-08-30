## Description:

Audit 8D reports, SCARs, and customer corrective-action reports against VDA and IATF 16949 standards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sam-zhang01](https://clawhub.ai/user/sam-zhang01)

### License/Terms of Use:

MIT-0

## Use Case:

Quality engineers, supplier quality engineers, and automotive corrective-action reviewers use this skill to audit 8D, SCAR, and customer complaint reports for VDA and IATF 16949 alignment before submission or closure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded 8D, SCAR, and corrective-action reports may contain confidential customer, supplier, production, or personnel details.

Mitigation: Redact unnecessary sensitive details before sharing reports with the agent and limit uploads to the sections needed for review.

Risk: Broad report-review trigger phrases may activate the skill outside a precise 8D, SCAR, VDA, or corrective-action context.

Mitigation: Invoke the skill with explicit report type, standard, and review objective so findings are scoped to the intended quality workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sam-zhang01/skills/8d-report-auditor)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured markdown-style audit report with conclusion, D1-D8 findings, gap analysis, and training recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects report content or uploaded Word, PDF, or text documents and returns a fixed four-section review format.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
