## Description:

Estimates a child's apparent emotional state from a provided video and optional audio, and returns a structured analysis with soothing suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and early-education staff can use it to review child-monitoring footage and receive a structured estimate of visible emotional cues with soothing prompts. The results are informational and do not provide a psychological diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review raises concerns about credential handling and account registration behavior.

Mitigation: Review how credentials and account registration are handled and where data is sent before installing or running the skill.

Risk: The skill processes child video and optional audio, and the security review says its upload behavior needs clarification.

Mitigation: Confirm the media destination and handling practices, obtain guardian consent, and protect recordings before submitting child media.

Risk: The security guidance says the export-only behavior needs correction or verification.

Mitigation: Verify that export-only mode does not execute analysis or transmit data before relying on it.

## Reference(s):

- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured emotion analysis report with soothing suggestions; JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotion category, intensity, duration, alerts, and a report link; results are not a clinical assessment.]

## Skill Version(s):

1.0.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
