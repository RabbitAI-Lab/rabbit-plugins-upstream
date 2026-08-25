## Description:

Analyzes elder-care monitoring images or videos to identify bed exits, prolonged wandering, and extended immobility, then returns structured monitoring results, risk guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, nursing-home operators, and developers use this skill to analyze night-monitoring videos or image inputs for bed-exit, wandering, and immobility events. It supports structured result review, report-link follow-up, and cloud report-list retrieval for elder-care monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive elder-care media, video URLs, report queries, and identity values may be sent to the configured remote service.

Mitigation: Verify endpoint configuration before use and process only media and identity data the user is authorized to share with that service.

Risk: The skill can create and reuse local account identity or token state.

Mitigation: Run in an isolated workspace and clear the workspace data database when account or token state should not persist.

Risk: Monitoring output is safety guidance and can miss or misclassify real-world events.

Mitigation: Treat alerts and reports as caregiver decision support and confirm abnormal events through timely human review.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [Analysis API Interface Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown text with optional JSON details, report links, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [History-report lists are formatted as Markdown tables; detailed output defaults to JSON.]

## Skill Version(s):

1.0.15 (source: server release evidence; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
