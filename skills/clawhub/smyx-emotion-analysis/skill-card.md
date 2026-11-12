## Description:

Analyzes facial expressions in supplied images or videos and returns structured emotion reports and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing facial media can request expression and emotion summaries, follow visible expression changes in a video, and retrieve prior reports. Treat results as tentative visual cues rather than evidence of a person's inner state or a substitute for psychological assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags account and token handling, shared reports, and external video processing beyond the advertised analysis; the scan is partial because a referenced local path was missing.

Mitigation: Review the complete package and its account, token, report-sharing, and video-processing behavior before use. Avoid sending sensitive or identifiable media until those behaviors are understood; do not rely on export-only mode to prevent video processing.

## Reference(s):

- [Skill release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-emotion-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured emotion analysis report, as JSON or Markdown, with report links where available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include expression cues, emotion labels, suggestions, and historical report links; accuracy depends on input quality.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
