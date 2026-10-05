## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents maintaining a GitLab profile use this skill to collect contribution statistics and update profile charts and a public proof file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The update routine can commit and push changes to a GitLab profile repository.

Mitigation: Use a least-privilege GitLab token and verify the counts and changed assets before publishing.

Risk: A recurring agent job may run updates unexpectedly.

Mitigation: Review or disable the scheduled job before enabling it.

Risk: Broad project discovery or environment-directed file paths can include unintended projects or write to unintended locations.

Mitigation: Set an explicit project list and output paths under assets/.

Risk: WebP conversion may invoke an undeclared npm package fallback.

Mitigation: Provide a pinned local WebP conversion tool or Python dependencies instead of relying on the npm fallback.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and SVG, WebP, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Charts summarize completed months; the proof file lists public records and aggregates private activity.]

## Skill Version(s):

1.98.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
