## Description:

Create and edit videos with Kuaishou Kling 4.0 and Kling O3 through the PopNow API: up to 30-second 1080p clips, keyframes, image-to-video, reference-to-video, extensions and video edits, with an exact USD quote before rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyuminjo](https://clawhub.ai/user/kyuminjo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and users can create or edit short videos with Kling models through PopNow, including text, image, and reference generation, keyframes, extensions, and prompt-based edits. The workflow confirms model inputs and obtains an exact maximum price quote before submitting a render.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference URLs are shared with PopNow and the generation provider, and command logs may retain inputs.

Mitigation: Avoid sensitive personal data, use only material you have rights to share, and consider provider and host-log retention before submitting prompts or references.

Risk: Video generation uses a paid API balance, and exposed or over-permissioned API keys can enable unwanted spending.

Mitigation: Keep the key in secret settings, restrict its models and spending, and review and explicitly approve the exact maximum quote before each render.

## Reference(s):

- [Kling model page](https://popnow.ai/models/kling-4-0)
- [PopNow API task documentation](https://popnow.ai/docs/tasks)
- [PopNow privacy policy](https://popnow.ai/privacy)

## Skill Output:

**Output Type(s):** [Video, API Calls, Guidance]

**Output Format:** [Video output links with JSON quote and task-status data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Kling 4.0 supports clips up to 30 seconds at 1080p; generation may queue, and the helper returns links without downloading files.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
