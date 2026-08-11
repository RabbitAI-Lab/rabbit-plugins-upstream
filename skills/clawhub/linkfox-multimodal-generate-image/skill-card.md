## Description:

AI-powered image generation and editing skill for product images, text-to-image, image-to-image, background replacement, style transfer, object replacement, scene compositing, and model swapping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit commercial product visuals from prompts and optional reference images through LinkFox image services. It supports product compositing, background changes, style transfer, and model swapping when public reference image URLs are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image prompts, reference images, uploaded local images, and generated outputs are handled by LinkFox services.

Mitigation: Use the skill only for content you are comfortable sharing with LinkFox, and avoid submitting sensitive or private images.

Risk: Local image uploads create publicly accessible image URLs.

Mitigation: Upload only images intended for public URL access, and avoid using the upload flow for confidential files.

Risk: The onboarding flow can request SMS codes, issue API keys, and access account credentials.

Mitigation: Provide SMS codes or account details only when you explicitly intend to link a LinkFox account, and store API keys securely.

Risk: Billing and package flows can create payment orders.

Mitigation: Do not initiate purchases unless the user has explicitly approved the plan and payment method.

Risk: Custom gateway environment variables can redirect requests.

Mitigation: Set custom LinkFox gateway variables only to trusted LinkFox endpoints.

Risk: API responses are cached and retained in local LinkFox session directories.

Mitigation: Review and clear retained local data when outputs or prompts contain sensitive material.

## Reference(s):

- [AI drawing API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-generate-image)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [API Calls, Markdown, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown image output, JSON API responses, saved JSON data files, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated responses may be cached for 24 hours and full API responses are retained in a local LinkFox session data directory.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
