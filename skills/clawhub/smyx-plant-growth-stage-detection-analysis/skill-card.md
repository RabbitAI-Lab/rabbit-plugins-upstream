## Description:

AI-powered plant growth stage detection from plant images or videos that identifies phenological features, classifies the current growth stage, and returns confidence, general care direction, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, greenhouse operators, and developers use this skill to analyze plant images or videos from smart pots, home grow boxes, greenhouses, or plant factories and determine the current growth stage. The output supports growth-stage monitoring and general cultivation guidance, but the skill documentation states that results are reference-only and not a specific agricultural operation plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media and network media URLs are uploaded to lifeemergence.com services for analysis.

Mitigation: Use approved, non-sensitive media and avoid images or videos that expose people, private spaces, location details, or confidential cultivation operations.

Risk: The skill can silently create or reuse an internal identity and store session tokens in a workspace SQLite database.

Mitigation: Run it only in trusted workspaces, restrict access to the workspace data directory, and remove local identity or token storage when the skill is no longer needed.

Risk: History lookup retrieves cloud-linked report records with limited user control.

Mitigation: Confirm that cloud history access is expected before using history commands, and prefer a release that asks before account creation or history lookup when stronger user control is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write analysis output to a user-specified file; history queries return cloud-linked report records.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
