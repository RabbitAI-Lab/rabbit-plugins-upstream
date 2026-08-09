## Description:

Groups existing product lists by main-image similarity to help identify visual clusters, duplicates, and cross-brand lookalikes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agents use this skill after product discovery to compare product images, group visually similar items, and highlight cross-brand similarity or image-based duplicates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product data, image URLs, user prompts, API keys, session metadata, and optional feedback content may be sent to LinkFox services.

Mitigation: Use the skill only with data you are allowed to share with LinkFox and avoid custom endpoint environment variables unless the destination is trusted.

Risk: The onboarding helper can request a phone number and SMS code, generate an API key, list paid plans, create payment orders, and render payment QR codes.

Mitigation: Use onboarding and billing flows only when the user intentionally wants to create or recover a LinkFox account or buy credits.

Risk: Full API responses and cached responses are written to local linkfox directories and may contain product or session data.

Mitigation: Review the output location, remove cached or saved response files when no longer needed, and avoid running the skill in directories where persisted outputs are inappropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-product-similarity)
- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with JSON API responses and saved JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full responses under a local linkfox session directory, prints small responses inline, summarizes large responses by default, and supports a 24-hour cache for repeated parameter combinations.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
