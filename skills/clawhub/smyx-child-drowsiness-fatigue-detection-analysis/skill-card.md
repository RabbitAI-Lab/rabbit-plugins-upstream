## Description:

Analyzes child classroom or desk video for visual fatigue indicators such as PERCLOS, head nodding, and eye-region glossiness to produce a 0-100 fatigue index and rest-oriented reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External educators, parents, and developers use this skill to analyze child learning-area images or videos, surface visual fatigue indicators, and retrieve associated cloud report history. Results should be treated as learning-support signals, not medical or sleep-disorder diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child images or videos may be sent to a configured cloud service, linked to an automatically resolved identity, and associated with cloud report history.

Mitigation: Use only with clear guardian consent, documented retention and deletion terms, and a visible option to avoid account-linked history or remote processing.

Risk: Stored account tokens and cloud report history can associate analysis results with a user over time.

Mitigation: Review token storage and access controls before deployment, restrict use to approved environments, and rotate or revoke credentials according to policy.

Risk: Visual fatigue scores can be affected by video quality and are not medical or sleep-disorder diagnoses.

Mitigation: Present outputs as classroom or learning-support signals, require adult review, and enforce clear video capture requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis)
- [API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown text with embedded structured JSON and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an optional output file when requested; cloud report history can be listed as structured Markdown or JSON.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
