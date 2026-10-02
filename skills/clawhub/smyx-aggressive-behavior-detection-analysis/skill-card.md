## Description:

Analyzes barn images and videos for aggressive livestock and poultry interactions, reporting behavior type, intensity, and alert level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock keepers and farm staff use the skill to screen barn footage for fighting, biting, chasing, and butting, then review alerts and historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn media or supplied URLs are sent to an external cloud service for analysis.

Mitigation: Confirm data handling and retention expectations before submitting sensitive footage or URLs.

Risk: The skill creates or reuses cloud identity state and stores tokens in the workspace data directory.

Mitigation: Review identity and deletion practices and limit access to the workspace data directory.

Risk: Detection results may not reliably determine when an animal needs intervention.

Mitigation: Treat alerts as screening signals and follow farm procedures and veterinary guidance for decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-aggressive-behavior-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured analysis report or Markdown table of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include incident details, alert levels, and report links.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
