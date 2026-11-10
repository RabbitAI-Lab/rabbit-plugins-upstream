## Description:

Text-to-image with one API key across Nano Banana, GPT Image, Seedream, FLUX, Qwen Image, Krea, Ideogram and more via PopNow: the agent picks a model for the job, shows the exact USD price and generates after approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyuminjo](https://clawhub.ai/user/kyuminjo)

### License/Terms of Use:

MIT No Attribution

## Use Case:

People using an AI agent can create images for illustrations, logos, posters, thumbnails, photos, and other visual requests. The agent selects a suitable model, presents an exact price quote, and submits the generation only after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference media URLs are sent to PopNow and the generation provider, and host logs may retain command parameters.

Mitigation: Avoid sensitive material, send only content the user has rights to use, and keep the API key in secret settings rather than prompts or command arguments.

Risk: Image generation spends prepaid API funds, and approval depends on the agent following the quote workflow.

Mitigation: Show the exact maximum USD charge and obtain explicit approval before each generation; use a dedicated key with model and spending limits.

Risk: Provider billing enforcement and data retention were not independently tested.

Mitigation: Review PopNow's current billing and privacy terms and configure conservative key limits before use.

## Reference(s):

- [PopNow image models](https://popnow.ai/image)
- [PopNow API task documentation](https://popnow.ai/docs/tasks)
- [ClawHub skill release](https://clawhub.ai/kyuminjo/skills/ai-image-generator)

## Skill Output:

**Output Type(s):** [Images, Text, API Calls]

**Output Format:** [Generated image output links with text guidance, model details, and USD price quotes]

**Output Parameters:** [Variable (prompt, model, and image settings)]

**Other Properties Related to Output:** [Generation is a paid external service action and requires approval of the quoted maximum charge.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
