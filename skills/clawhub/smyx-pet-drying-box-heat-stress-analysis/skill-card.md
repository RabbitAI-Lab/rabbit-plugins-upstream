## Description:

Analyzes pet drying-box video files or URLs for heat-stress signs and returns risk levels and intervention guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, groomers, and veterinary staff use the skill to review drying-box footage for panting, tongue-color changes, and movement patterns, then receive heat-stress risk guidance. It does not provide a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet footage or video URLs are sent to lifeemergence.com services for analysis.

Mitigation: Avoid sensitive footage until the publisher clarifies consent, retention, and deletion controls.

Risk: The skill silently creates or reuses a cloud identity, links report history to it, and stores account tokens locally.

Mitigation: Review the account behavior before installation and protect access to the workspace data directory.

Risk: Heat-stress guidance is not a veterinary diagnosis and may not be sufficient during an emergency.

Mitigation: Treat suspected heat stress as urgent; stop drying and seek veterinary advice rather than relying only on the report.

## Reference(s):

- [Pet drying-box analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or JSON; historical report list in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk levels, observations, intervention suggestions, and report links when available.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
