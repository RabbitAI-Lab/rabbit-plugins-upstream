## Description:

Procurement Admission Copilot helps human procurement reviewers check supplier admission material packages and approval-case queues for completeness, consistency, stalls, and gaps without drafting contract terms or making admission decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement employees, supplier onboarding teams, and approval committees use this skill to review supplier qualification materials and admission case queues before a human decision. It produces readiness findings, status dashboards, and recommended reviewer actions while keeping admission responsibility with the buyer or committee.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reviewed artifact references deterministic scripts and report templates that were not included in the inspected files.

Mitigation: Manually verify readiness checks, status findings, and generated reports before relying on them in a procurement workflow.

Risk: Supplier qualification materials and approval cases may contain sensitive business, financial, compliance, or identity information.

Mitigation: Provide only materials intended for review and handle outputs according to the buyer's procurement data policies.

Risk: The skill can flag blocking issues but must not decide supplier admission or draft contract terms.

Mitigation: Keep final admission, sourcing, and contract decisions with the procurement reviewer, buyer, or committee.

## Reference(s):

- [Procurement Admission Qualification Checklist](references/qualification-checklist.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Guidance]

**Output Format:** [Structured JSON and Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include readiness checks, supplier material packages, readiness reports, normalized case data, and case dashboards; the skill is review-only and does not emit approval or rejection decisions.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
