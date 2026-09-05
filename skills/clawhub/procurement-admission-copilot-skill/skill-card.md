## Description:

Shadow-mode copilot for B2B procurement admission that checks supplier material-package completeness and consistency, tracks approval-case status and gaps, and keeps admission decisions with a human reviewer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, vendor-management, and supplier-onboarding teams use this skill to review supplier qualification packages and approval-case queues before human admission review. It produces structured readiness findings, status dashboards, and recommended human follow-up without drafting contract terms or making admission decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplier financial, compliance, and identity materials can contain sensitive business data.

Mitigation: Use the skill only in workspaces approved for that data and limit access to the procurement reviewers who need the outputs.

Risk: Readiness flags or a 'ready' status could be mistaken for an admission or sourcing decision.

Mitigation: Treat P0/P1/P2 findings as triage signals and keep final admission decisions with an accountable human reviewer or committee.

Risk: Malformed manifests, missing dates, or inconsistent source documents can lead to incomplete or misleading findings.

Mitigation: Review the deterministic check output and require human confirmation of P0/P1 disposition before acting on the report.

## Reference(s):

- [Procurement Admission Qualification Checklist](references/qualification-checklist.md)
- [Procurement Admission Copilot on ClawHub](https://clawhub.ai/haiyangchenbj/skills/procurement-admission-copilot-skill)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [JSON readiness checks and Markdown material packages, readiness reports, and case dashboards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review-only outputs with P0/P1/P2 flags and human confirmation steps; no contract terms or admission decisions.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
