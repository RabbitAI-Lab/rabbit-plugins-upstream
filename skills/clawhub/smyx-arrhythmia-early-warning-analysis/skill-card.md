## Description:

Analyzes facial video to identify arrhythmia warning signals such as premature beats, atrial fibrillation, tachycardia, and bradycardia for early heart-health risk screening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents use this skill to submit a face video or video URL for early arrhythmia warning analysis and to retrieve historical cloud reports. Results are screening-oriented and should not be treated as a professional medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive facial videos and health-related results are sent to a configured cloud service.

Mitigation: Obtain explicit user consent before analysis, minimize submitted media, and document retention, deletion, and account-linkage controls.

Risk: The skill can create or reuse a persistent internal identity and retrieve historical reports.

Mitigation: Limit history lookups to the intended user context, avoid exposing identity values, and audit access to report history.

Risk: Screening output could be mistaken for a clinical diagnosis.

Mitigation: Present results as early warning information only and advise professional medical evaluation for high-risk findings.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-arrhythmia-early-warning-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON text with shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can optionally write analysis output to a caller-supplied file path.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
