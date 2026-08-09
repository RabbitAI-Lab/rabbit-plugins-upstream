## Description:

Extracts structured visual attributes and prompt-style descriptions from e-commerce product images using LinkFox multimodal analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and analysts use this skill to analyze product main images and optional additional images, extracting visual attributes such as color, material, shape, style, and image-prompt descriptions into structured product rows and attribute groupings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends product images, upstream product data, userInput, and API credentials to LinkFox-controlled services.

Mitigation: Install and run it only when LinkFox is trusted with those inputs, and keep API keys in the documented environment variables rather than pasting them into prompts.

Risk: Image analysis consumes paid credits and may create a large charge when many images or dimensions are analyzed.

Mitigation: Ask for explicit user confirmation before paid analysis, explain that credits will be consumed, and avoid automatic retries or expanded searches after failures.

Risk: The onboarding flow can collect phone-based login details and create payment orders.

Mitigation: Use onboarding only for authentication or billing errors, require explicit confirmation before SMS login or order creation, and do not poll payment status without user direction.

Risk: Configurable LinkFox endpoint environment variables can redirect traffic away from the expected service.

Mitigation: Use endpoint override variables only when they point to verified LinkFox hosts.

Risk: The skill stores full API responses and cache data in the workspace.

Mitigation: Review saved JSON files for sensitive product or user data and remove them when they are no longer needed.

Risk: The skill can automatically submit feedback about user satisfaction or skill behavior.

Mitigation: Require explicit confirmation before feedback submission when it may include user intent, result details, or other sensitive context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-extract-attributes)
- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance, files]

**Output Format:** [Markdown summaries and tables, JSON API responses, stdout summaries, and saved JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved under the current workspace linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
