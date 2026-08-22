## Description:

Generates and edits images from prompts and optional reference images for product photos, background changes, style transfer, compositing, and model swapping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request AI image generation or image editing through LinkFox, including product photography, reference-guided edits, background replacement, style transfer, and product compositing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, reference images, and selected local images may be sent to LinkFox services or uploaded as publicly accessible image URLs.

Mitigation: Use the skill only when the user trusts LinkFox with the content, and require explicit confirmation before uploading local files publicly.

Risk: Image generation and onboarding flows can consume account credits or create payment orders.

Mitigation: Confirm expected credit or payment impact with the user before running paid generation or billing actions.

Risk: The skill handles API keys, phone/SMS authentication data, and feedback content.

Mitigation: Avoid exposing credentials unnecessarily, require confirmation before displaying or storing API keys, and confirm before sending feedback content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-generate-image)
- [AI drawing API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown image output, JSON API responses, and saved JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image responses may be displayed inline; complete API responses are saved under linkfox/ session data and cached for repeat requests.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
