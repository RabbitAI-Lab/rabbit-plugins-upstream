## Description:

Analyzes livestock and poultry barn footage for fighting, biting, chasing, and butting, and reports behavior type, intensity, and alert level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and livestock-monitoring teams use the skill to screen barn footage for aggressive interactions, review alerts, and retrieve historical analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn footage and report queries are sent to external lifeemergence.com services.

Mitigation: Confirm data-sharing approval and retention terms before submitting sensitive footage or business records.

Risk: The skill silently creates or reuses a local identity database and stores authentication tokens.

Mitigation: Review account linking, local token storage, access controls, and data retention before installation.

Risk: Automated behavior alerts may be mistaken for definitive animal-welfare assessments.

Mitigation: Review footage and follow farm and veterinary procedures before taking action.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-aggressive-behavior-detection-analysis)
- [Aggressive behavior analysis API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured analysis text and Markdown report tables with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior and intensity labels, alert levels, and report links; results are advisory.]

## Skill Version(s):

1.0.13 (source: server release metadata; bundled frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
