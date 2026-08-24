## Description:

Combines TCM facial feature recognition with physiological indicators to screen face images or videos for stroke risk signals, return structured reports, and provide lifestyle and medical guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit face images or videos, optionally with blood pressure, blood sugar, or blood lipid values, and receive a structured stroke risk screening report. The skill can also query the user's cloud report history and return report records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive face images, videos, physiological indicators, and report queries are sent to configured LifeEmergence services.

Mitigation: Use the skill only with informed user consent, approved public endpoints, and confirmed privacy, retention, deletion, and authorization practices.

Risk: The skill silently creates or reuses a persistent user identity and can retrieve cloud report history.

Mitigation: Limit access to trusted agents and workspaces, review identity handling before deployment, and verify that report history access matches the user's authorization.

Risk: Stroke risk screening output could be mistaken for diagnosis or emergency medical advice.

Mitigation: Present results as screening guidance only and direct high-risk or symptomatic users to professional medical care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](artifact/references/api_doc.md)
- [SMYX analysis API reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON reports, with optional report links and history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a requested output file and may include cloud report export URLs.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
