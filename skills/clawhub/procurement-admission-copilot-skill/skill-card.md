## Description:

Shadow-mode copilot for B2B procurement admission. Given a supplier's raw qualification inputs, it checks material-package completeness and internal consistency; given a set of approval cases, it tracks status, stalls, and gaps. It never drafts contract terms or makes the admission decision — only structures and flags for a human to decide.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and human reviewers use this skill to check B2B supplier admission packages for completeness and consistency or to track approval-case status, stalls, and gaps. It structures findings for review and leaves all approval decisions to people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplier materials and generated reports may contain sensitive business information.

Mitigation: Provide only supplier materials authorized for sharing with the agent, and protect generated reports.

Risk: Readiness findings depend on the completeness of the supplied manifest and checklist.

Mitigation: Verify checklist completeness and review findings before making decisions; leave approval decisions to human reviewers.

## Reference(s):

- [Procurement Admission Qualification Checklist](references/qualification-checklist.md)
- [ClawHub release page](https://clawhub.ai/haiyangchenbj/skills/procurement-admission-copilot-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown reports and dashboards; JSON readiness checks and normalized case data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review-only findings; does not modify supplier documents or make admission decisions.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
