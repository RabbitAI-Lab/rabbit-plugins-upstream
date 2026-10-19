## Description:

Analyzes a consented frontal face photo through RageHealth to summarize skin scores, skin type, visible concerns, and illustrative images using one of two scoring strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoguaishou-sc](https://clawhub.ai/user/xiaoguaishou-sc)

### License/Terms of Use:

MIT-0

## Use Case:

Users and their assistants use this skill to review skin appearance in a frontal face photo, including pores, acne, wrinkles, pigmentation, and an overall score. Results are informational and not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face photos and skin-analysis data are sent to RageHealth.

Mitigation: Obtain the user's consent before upload and use the service only when comfortable sharing this sensitive data.

Risk: Face ID detection can create a persistent facial identifier within a user group.

Mitigation: Enable face ID only on the user's explicit request; otherwise leave it disabled.

Risk: Skin scores can be mistaken for a clinical diagnosis.

Mitigation: Present results as informational, flag poor photo quality, and recommend an in-person clinician for concerning symptoms.

Risk: Exposed credentials or changing dependency versions can compromise access or reproducibility.

Mitigation: Keep dedicated SKIN_PRO_AK/SKIN_PRO_SK credentials out of chat and pin dependency versions for reproducible installs.

## Reference(s):

- [skin-pro ClawHub release](https://clawhub.ai/xiaoguaishou-sc/skills/skin-pro)
- [Skin analysis response schema](references/response_schema.md)
- [RageHealth client portal](https://ragehealth.cn/client)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Plain-language Markdown summary; optional JSON analysis response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes skin scores, severity labels, photo-quality caveats, and links to illustrative images where available.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
