## Description:

This skill analyzes classroom, home desk, or online class face video to estimate child drowsiness from visual fatigue indicators such as PERCLOS, head nodding, eye-region changes, and a 0-100 fatigue score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, parents, and education technology operators use this skill to assess visible signs of child fatigue from learning-area video, generate structured fatigue reports, and retrieve prior reports from the publisher's cloud service. The output is for learning support and rest reminders, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's face videos or video URLs are sent to the publisher's cloud service.

Mitigation: Use only with guardian consent, submit only necessary media, and confirm the publisher's data handling practices before use.

Risk: Historical reports are queried from the publisher's service and local identity or token records may be created or reused.

Mitigation: Run in an isolated workspace with appropriate access controls, and avoid shared environments unless identity and report access are clearly separated per user.

Risk: Visual fatigue scores and reminder text could be mistaken for medical or sleep-disorder diagnosis.

Mitigation: Present outputs as observational learning support only, and route persistent or severe drowsiness concerns to qualified care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and JSON-structured analysis results, with optional saved output files and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include fatigue metrics, fatigue level, drowsiness events, reminder text, and cloud report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; skill frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
