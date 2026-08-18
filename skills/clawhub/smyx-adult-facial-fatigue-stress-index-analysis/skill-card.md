## Description:

Analyzes adult face images or short videos to estimate visual fatigue and stress indicators, then returns a 0-100 fatigue/stress index with a level, contributing features, suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, workplace wellness teams, and developers use this skill to analyze consenting adults' face images or short videos for visual fatigue/stress indicators and trendable reports. It is intended for personal or workplace health reference, not diagnosis or clinical stress assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive face images or videos may be uploaded for remote processing, and prior reports may be retrieved from cloud history.

Mitigation: Use only with informed user consent for remote face-media processing and history lookup; avoid use where biometric privacy requirements cannot be met.

Risk: The skill may create or reuse persistent account-linked identity records and tokens without enough user control.

Mitigation: Review identity and token handling before installation, protect the local data directory and SQLite database, and prefer a version that requires explicit confirmation before uploads, history lookup, and account creation.

Risk: The fatigue/stress index is based on visual facial features and is not a medical diagnosis or clinical stress assessment.

Mitigation: Present outputs as informational guidance only and direct users to professional evaluation for persistent high scores or physical symptoms.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-adult-facial-fatigue-stress-index-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [JSON or Markdown report text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; history queries return cloud report records when available.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter declares 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
