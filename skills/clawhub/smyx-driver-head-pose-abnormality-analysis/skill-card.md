## Description:

Processes in-cabin driver images or videos to report head-pose estimates and possible head-down or side-view distraction events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and fleet safety teams can submit in-cabin driver video for structured head-pose and possible distraction reports, or review previously generated reports. Treat results as assistive review and do not rely on this skill for live driving warnings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may mix between users in shared workspaces or when private footage is used.

Mitigation: Require caller-isolation fixes before using private footage or a shared workspace.

Risk: The no-analysis option may be ignored, and credential handling needs review.

Mitigation: Require fixes for the ignored option and credential handling before use; confirm the selected operation and credentials are handled as intended.

Risk: Live driving alerts exceed the capabilities established by the bundled skill.

Mitigation: Do not rely on this package for live driving warnings; establish clear account-enrollment, pricing, retention, and deletion terms before using private footage.

## Reference(s):

- [API interface and input requirements](artifact/references/api_doc.md)
- [API response and error-code notes](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured analysis reports and Markdown report lists, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include head-pose estimates and possible distraction events; results depend on clear driver visibility and suitable video quality.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
