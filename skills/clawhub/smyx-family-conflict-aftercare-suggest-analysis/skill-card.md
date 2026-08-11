## Description:

Analyzes fixed-camera household audio/video from public family areas to detect conflict signals, determine when a calm window has been reached, and produce neutral aftercare suggestions or safety-resource escalation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External smart-home developers and integrators use this skill to process household public-area media for conflict-event reports, calm-window status, aftercare action suggestions, and historical report lookup. It is intended for non-clinical aftercare prompts and safety-resource routing, not relationship scoring or therapy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive household audio/video may be sent to cloud APIs and linked to persistent identity or token data.

Mitigation: Deploy only with informed consent from affected household members, confirm account linkage and deletion controls, and review retention behavior before use.

Risk: In-home monitoring can overreach into private spaces or retain intimate conversation data.

Mitigation: Limit deployment to public household areas, avoid bedrooms, bathrooms, and children's private rooms, and minimize retained raw media in favor of event metrics and short-lived clips.

Risk: Aftercare prompts during active or violent conflicts could increase harm.

Mitigation: Trigger prompts only after the calm-window criteria are met, route redline events to safety resources, and keep all wording neutral and non-accusatory.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-family-conflict-aftercare-suggest-analysis)
- [API Interface Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include conflict levels, observed audio/video signals, calm-window status, aftercare recommendations, safety resources, and report links.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
