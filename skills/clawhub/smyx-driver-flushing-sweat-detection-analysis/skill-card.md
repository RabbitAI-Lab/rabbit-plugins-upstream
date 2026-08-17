## Description:

Using an in-cabin DMS camera, this skill analyzes driver facial video to flag visual signs of facial flushing or abnormal sweating and produce structured health-risk reminders without making a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, fleet operators, and developers use this skill to analyze driver-facing DMS video or images for visual flushing and sweating signals, then return structured alerts, suggested safety actions, and report links. It is intended as an assistive driver-health reminder and does not replace medical instruments or clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive driver facial video and inferred health-risk reports are sent to configured backend services.

Mitigation: Use only with clear driver or employee consent, appropriate retention controls, and a reviewed backend configuration.

Risk: The skill silently creates or reuses a persistent local identity and stores authentication tokens.

Mitigation: Confirm this identity model is acceptable for the deployment environment and isolate or rotate credentials as needed.

Risk: Visual flushing and sweating signals can be affected by lighting, tinted windows, RGB channel quality, occlusion, and individual skin differences.

Mitigation: Treat outputs as assistive reminders, validate input quality, and avoid using the result as a medical diagnosis.

## Reference(s):

- [Driver flushing and sweat detection API documentation](references/api_doc.md)
- [Shared health analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text containing structured JSON analysis results, warnings, suggested actions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the rendered result to a local file when an output path is supplied; history queries return report records from the configured backend.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
