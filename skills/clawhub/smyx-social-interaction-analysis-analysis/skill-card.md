## Description:

Analyzes multi-pet household images or videos to classify social interactions such as sniffing, chasing, biting, fleeing, hiding, and playing, then produces a structured social-behavior report with duration, frequency, initiator, and receiver observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet-care operators use this skill to analyze multi-pet interactions from fixed-camera footage, quantify friendly, neutral, and conflict behaviors, and review structured social-behavior reports. It is intended for visual behavior observation, not medical, veterinary, or training advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Household pet images or video may be uploaded to LifeEmergence-hosted APIs.

Mitigation: Use only with informed consent and acceptable data-handling terms; confirm retention, deletion, and access controls before deployment.

Risk: The skill can create or reuse an internal identity and store authentication tokens locally.

Mitigation: Review local credential storage and token lifecycle before installation, and prefer a deployment that documents identity and token handling clearly.

Risk: Certain phrases can trigger automatic cloud report history lookup.

Mitigation: Require explicit user confirmation before cloud history queries or deploy a version that makes report lookup opt-in.

## Reference(s):

- [Skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-social-interaction-analysis-analysis)
- [API documentation](references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis results, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include analysis progress, behavior classifications, conflict-level observations, recommendations, and cloud report links.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter states 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
