## Description:

Searches 1688 by product image to find visually similar or matching supplier listings with core sourcing data such as title, price, minimum order quantity, monthly sales, repurchase rate, trade score, and seller badges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, sourcing teams, and agent users use this skill to locate visually similar 1688 wholesale products from a public image URL, uploaded local image, image ID, or raw Base64 image. It helps compare supplier listings by price, sales volume, order quantity, service score, repurchase rate, delivery details, and seller badges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs, uploaded local images, search parameters, API keys, onboarding data, account actions, billing requests, and feedback content may be sent to LinkFox services.

Mitigation: Use the skill only with images and account data approved for third-party processing, avoid confidential product imagery, and review authentication, feedback, and billing flows before installation.

Risk: Local image files can be uploaded to a public URL for 24 hours before search.

Mitigation: Prefer already public image URLs when appropriate, and upload local files only after confirming the image can be publicly accessible for the validity window.

Risk: The skill persists full API responses and cache data under a local linkfox session directory.

Mitigation: Review generated response files for sensitive sourcing data, manage local retention, and clear the linkfox cache/session data when no longer needed.

Risk: Search calls consume LinkFox credits and onboarding can initiate payment flows.

Mitigation: Confirm expected credit usage with the user before repeated searches, validate plan and payment choices, and avoid automatic retries that increase cost.

## Reference(s):

- [1688-以图搜图 ClawHub page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-search-by-image)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files]

**Output Format:** [Markdown summaries and tables, shell command snippets, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under a local linkfox session directory, may print compact summaries for large responses, and can emit public image URLs after upload.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
