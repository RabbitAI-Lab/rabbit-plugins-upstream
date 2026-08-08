## Description:

Analyzes child face video from classroom, desk, or online-learning settings to estimate visual fatigue indicators such as PERCLOS, eye-closure duration, nodding, and a 0-100 fatigue score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as teachers, parents, and education-support agents use this skill to analyze uploaded or URL-based child learning videos for drowsiness indicators, fatigue level, rest reminders, report links, and historical fatigue reports. Outputs are visual fatigue assessments only and are not medical or sleep-disorder diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child media and identity-linked report data are sent to cloud services.

Mitigation: Verify backend privacy terms, retention and deletion controls, and guardian consent before installing or using the skill.

Risk: The skill silently creates or reuses local identities and tokens for analysis and history lookup.

Mitigation: Confirm local token storage, identity reuse behavior, and automatic history access are acceptable for the deployment environment.

Risk: Fatigue results could be mistaken for medical conclusions.

Mitigation: Present outputs as visual fatigue assessments and rest guidance only, not as medical or sleep-disorder diagnoses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Child fatigue detection API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, JSON, files, shell commands, guidance]

**Output Format:** [Markdown text or JSON analysis with optional saved output file and report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud history and return Markdown tables for prior reports.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
