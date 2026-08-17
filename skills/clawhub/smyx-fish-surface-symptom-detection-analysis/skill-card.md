## Description:

Analyzes aquarium or underwater fish images and videos to classify visible body-surface symptoms such as white spots, hyperemia, and fin rot, returning symptom locations, confidence, severity, alerts, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarium keepers, aquaculture operators, and developers use this skill to submit fish images or videos for visual symptom screening and receive structured health reports with alert guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish images, videos, or URLs may be sent to external cloud services for analysis.

Mitigation: Use only authorized aquarium media, avoid private or internal URLs, and confirm endpoint, authentication, and retention expectations before deployment.

Risk: The skill may query cloud report history and create or reuse local identity/token state.

Mitigation: Run it in an isolated workspace, limit access to shared environments, and review or clear local identity/token state according to the operator's credential policy.

Risk: Visual symptom classifications may be mistaken for a veterinary diagnosis or treatment plan.

Mitigation: Present results as screening guidance only, avoid medication names or dosing instructions, and direct final diagnosis and treatment decisions to a qualified aquatic veterinarian or aquarium professional.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-surface-symptom-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON report text with symptom classifications, confidence scores, alert level, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external cloud services for media analysis and report history, and may create or reuse local identity/token state.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
