## Description:

Shadow-mode copilot for B2B procurement admission that checks supplier material-package completeness and consistency, tracks approval-case status and gaps, and leaves admission decisions to human reviewers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, vendor-management, and supplier-onboarding teams use this skill to review supplier qualification packages before submission and to monitor admission approval cases for stalls, missing documents, inconsistent decisions, and other gaps. It produces review artifacts for human decision-makers rather than contract terms, rankings, or admission decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes supplier materials and approval-case files that may contain sensitive procurement, identity, financial, or compliance information.

Mitigation: Run it in a designated work directory with only the files needed for the review, and avoid exposing materials the agent does not need.

Risk: Generated flags and recommended actions could be mistaken for admission, sourcing, or contract decisions.

Mitigation: Treat outputs as review artifacts only; require a human reviewer or procurement committee to confirm P0/P1 disposition and make all admission decisions.

Risk: The workflow uses Chinese-leaning templates and procurement terms that may not match every organization's jurisdiction or process.

Mitigation: Review the generated package, report, and dashboard against the organization's procurement policy before acting.

## Reference(s):

- [Procurement Admission Qualification Checklist](references/qualification-checklist.md)
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/procurement-admission-copilot-skill)

## Skill Output:

**Output Type(s):** [Analysis, Files, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [JSON readiness checks and Markdown supplier packages, readiness reports, and case dashboards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review-only outputs; generated findings and recommended actions should cite supplied materials and require human confirmation before procurement action.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
