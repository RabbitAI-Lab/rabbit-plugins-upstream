## Description:

Analyzes rehabilitation training video, with optional audio, to detect patient frustration or giving-up behaviors and produce structured motivation guidance, escalation signals, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and care-support teams use this skill to analyze rehabilitation session media for frustration, training interruption, low engagement, and lack-of-progress signals, then generate structured encouragement and escalation guidance. It is intended to support motivation workflows, not to diagnose medical or psychological conditions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive rehabilitation video, optional audio, and history records may be processed by cloud services.

Mitigation: Use only with explicit patient or guardian and institution authorization, and confirm endpoint, retention, and access-control policies before processing real patient media.

Risk: The skill links analysis to patient identity-like open IDs and may store tokens or default user records in the workspace data directory.

Mitigation: Run in a controlled workspace, restrict access to the data directory, and review or clear local identity and token storage according to the deployment policy.

Risk: Motivation or escalation output could be misread as medical or psychological diagnosis.

Mitigation: Present results as behavioral support signals only, require clinician review for care decisions, and avoid diagnostic labels or unauthorized training-plan changes.

Risk: Encouragement actions or progress comparisons could pressure patients or rely on inaccurate history data.

Mitigation: Use only verified historical progress data, keep encouragement specific and non-comparative, and require human oversight for escalation to caregivers or family.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-rehab-motivation-encouragement-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON structured analysis report with report links; Markdown table output for history listings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call cloud APIs, upload local media or pass media URLs, poll for results, and optionally write output to a file.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
