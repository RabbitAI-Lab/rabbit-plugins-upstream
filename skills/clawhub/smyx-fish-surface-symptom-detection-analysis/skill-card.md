## Description:

Detects visible fish body-surface symptom signals, including white spots, hyperemia, and fin rot, from aquarium or underwater camera images and videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium hobbyists, public aquarium staff, ornamental fish farms, and developers use this skill to analyze fish images or videos for visible body-surface symptom signals and generate structured health reports for follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package silently creates or reuses an identity and persists backend tokens.

Mitigation: Deploy only where identity use, local state, token storage, and deletion controls are documented and acceptable to reviewers and users.

Risk: The package ships with plaintext development HTTP endpoints for media and authenticated traffic.

Mitigation: Require HTTPS production endpoints before installation or execution, and block development endpoints in production configuration.

Risk: Fish-health outputs could be mistaken for a diagnosis or treatment plan.

Mitigation: Keep outputs framed as visual symptom classification only, avoid specific medication or dosing instructions, and route diagnosis and treatment decisions to qualified aquatic veterinary professionals.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-surface-symptom-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured JSON-style report content and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include confidence scores, symptom locations, severity labels, report export links, recommended non-medication actions, and disclaimers.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
