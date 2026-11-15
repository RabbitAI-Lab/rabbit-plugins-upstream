## Description:

Analyzes videos for emotional and behavioral patterns and returns structured mental-health analysis reports with suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing user-provided video can request a structured summary of apparent emotional or behavioral patterns, possible common mental-health concerns, and suggestions; the skill can also retrieve prior reports. Treat its output as informational, not as a diagnosis or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports credential handling that may send credentials to arbitrary URLs, along with automatic account creation.

Mitigation: Review and verify the configured service destination and credential handling before use; avoid providing credentials until they are understood.

Risk: Video uploads may expose personal information, and the security review reports privacy and consent gaps.

Mitigation: Upload only video you are authorized to share, obtain appropriate consent, and avoid sensitive footage when privacy protections are unclear.

Risk: The security review says export-only mode may still analyze supplied input, and the scan was partial because a referenced local path was missing.

Mitigation: Do not rely on export-only mode to prevent processing; review the complete release and its data handling before using sensitive inputs.

Risk: Mental-health indicators inferred from video may be misleading and are not a clinical diagnosis.

Mitigation: Use results only as informational guidance and refer mental-health concerns to a qualified professional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis)
- [API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured analysis report with suggestions and report links; history results may be returned as JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotional or behavioral observations, possible concern indicators, and links to reports.]

## Skill Version(s):

1.0.25 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
