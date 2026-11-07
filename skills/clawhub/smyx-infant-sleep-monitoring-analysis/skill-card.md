## Description:

Analyzes infant sleep monitoring footage to classify sleep states and produce daily sleep reports and routine analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use the skill to review infant sleep footage and understand sleep patterns through state summaries and daily reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload private nursery footage to LifeEmergence, create cloud accounts, and store access tokens; the security evidence also says the export-only option does not prevent this behavior.

Mitigation: Wait until the export-only behavior and ignored server override are fixed before using private footage. Confirm processing, account creation, charges, and retention/deletion terms; use an isolated workspace and protect its credential database.

Risk: Sleep analysis could be mistaken for medical advice.

Mitigation: Treat results as parenting reference and consult a pediatric clinician about sleep or health concerns.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-sleep-monitoring-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured sleep analysis and report text, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sleep-state classifications, sleep-time and awakening summaries, routine analysis, and suggestions. For parenting reference only; not a substitute for professional medical advice.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
