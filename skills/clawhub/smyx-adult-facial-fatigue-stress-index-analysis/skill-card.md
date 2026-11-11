## Description:

Analyzes adult facial images or short videos for visual signs associated with fatigue or stress and returns a 0–100 index with directional suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and workplace wellness teams use the skill to review adult facial images or short clips and receive a fatigue or stress score with directional suggestions. The score is a visual reference, not a medical assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial media may be uploaded even when export-only mode is selected.

Mitigation: Obtain the subject's consent, confirm upload controls and the provider's retention and deletion practices, and defer use until export-only behavior is reliable.

Risk: A real API secret may be recorded as identity data through the current credential path.

Mitigation: Keep API secrets separate from identity fields and rotate any secret that may have passed through this path.

Risk: Scoring accuracy and remote privacy controls have not been verified.

Mitigation: Treat scores as non-diagnostic guidance and seek professional assessment for persistent health concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-adult-facial-fatigue-stress-index-analysis)
- [API reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Text]

**Output Format:** [Structured analysis report with a fatigue or stress score, visual feature metrics, suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual reference only; not a medical diagnosis]

## Skill Version(s):

1.0.13 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
