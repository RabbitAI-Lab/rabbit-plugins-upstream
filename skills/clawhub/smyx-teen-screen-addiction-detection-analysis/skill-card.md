## Description:

Analyzes video of adolescents using phones or games to estimate screen-looking posture and duration, then produces structured summaries and threshold-based reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Guardians and educators can review summaries of adolescents' observed phone or game screen-looking behavior, duration, and threshold reminders. The results are visual behavior estimates, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential handling, network destinations, account registration, and report export behavior are not sufficiently clarified in the security evidence.

Mitigation: Before use, confirm which credentials are accessed, restrict destinations to the expected service, and review account registration and export behavior.

Risk: Camera footage and behavior reports concern minors and may expose sensitive personal information.

Mitigation: Obtain the guardian's and adolescent's informed consent; avoid retaining source video or sharing reports beyond the intended caregivers.

Risk: Visual posture and duration summaries could be mistaken for a medical diagnosis.

Mitigation: Present results only as behavior estimates and reminders; do not use them to diagnose addiction or other health conditions.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis results; JSON by default, with Markdown tables for history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Posture categories, screen-looking duration summaries, threshold reminders, suggestions, and report links]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata; artifact frontmatter lists 1.0.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
