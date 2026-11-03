## Description:

Analyzes classroom video to estimate group engagement, summarize emotion and participation trends, and provide seat-level teaching prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and classroom administrators use the skill to review aggregate engagement trends from classroom video and get prompts for adjusting lesson flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports defects in configuration-only mode and credential handling, while the skill uploads classroom recordings.

Mitigation: Wait for fixes before using sensitive recordings.

Risk: Classroom recordings involve students, and anonymous report outputs do not mean the original videos remain local.

Mitigation: Obtain school and guardian consent, confirm the provider's retention and deletion practices, and isolate users' accounts and workspaces.

## Reference(s):

- [Classroom engagement analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Structured engagement report with aggregate estimates, seat-level alerts, recommendations, and report links; text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Historical report lists can be returned as Markdown; reports may include heatmap links.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
