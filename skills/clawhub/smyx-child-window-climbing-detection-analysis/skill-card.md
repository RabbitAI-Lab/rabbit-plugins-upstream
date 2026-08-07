## Description:

Analyzes fixed-camera home or childcare video for child window or balcony climbing behaviors and returns structured warning results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to analyze video or video URLs from window and balcony areas for child climbing, leaning, railing-crossing, and related high-fall risk behaviors. It can also query cloud-stored historical warning reports for the same scenario.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child or home video, video URLs, generated reports, and report history may be processed by external lifeemergence.com services.

Mitigation: Use only with informed guardian consent, avoid unnecessary sensitive footage, and confirm retention, deletion, and access controls before deployment.

Risk: The skill may silently create or reuse a local identity and store authentication tokens in the workspace.

Mitigation: Run in a controlled workspace, restrict access to local data files, and prefer a version with explicit controls to reset or disable account-linked history.

Risk: Warnings are an auxiliary monitoring signal and may be incomplete or incorrect.

Mitigation: Do not use as a replacement for adult supervision; require human review and operational fallback for safety-critical alerts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Child Window/Balcony Detection API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with structured JSON report content, warning results, historical report lists, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the displayed result to a user-specified output file.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
