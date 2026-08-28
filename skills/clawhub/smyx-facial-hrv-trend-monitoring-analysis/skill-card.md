## Description:

Analyzes 30-60 second adult facial videos with remote photoplethysmography (rPPG) to estimate HRV metrics such as SDNN and RMSSD, trend changes, stress or fatigue hints, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, care teams, wellness operators, and developers use this skill to process adult seated face videos or URLs for HRV trend monitoring and history lookup. It is intended for personal wellness trend reference, stress or fatigue prompts, and report generation rather than medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial videos and HRV results may be sent to a remote backend and linked to an automatically created or reused identity.

Mitigation: Require explicit user consent before analysis or history lookup, and review or replace backend configuration before deployment.

Risk: Account tokens and identity data may be persisted locally while processing sensitive facial health data.

Mitigation: Run the skill in an isolated environment, restrict local filesystem access, and remove or rotate stored credentials after use.

Risk: rPPG-derived HRV can be affected by video quality, lighting, motion, posture, caffeine, emotions, and other conditions, and should not be treated as a diagnosis.

Mitigation: Use clear 30-60 second front-facing videos at 25 FPS or higher under stable lighting, compare trends under consistent conditions, and present results only as wellness trend references.

## Reference(s):

- [Adult Facial HRV API Documentation](references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-facial-hrv-trend-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or JSON-style structured text with HRV metrics, trend summaries, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the rendered analysis output to a user-specified file.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact/SKILL.md frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
