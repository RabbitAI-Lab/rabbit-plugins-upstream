## Description:

Create videos with MiniMax H3 Standard or Turbo (text-to-video, image-to-video, and reference-to-video) through Phosor AI, then use the same skill for images, speech, LoRA workflows, and e-commerce product or model photography. Use when the user wants to create H3 video from text, images, or references, compare Standard and Turbo, use the Phosor API, generate images or speech, use a custom LoRA, create e-commerce photography, or manage generation jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jasonstarlight](https://clawhub.ai/user/jasonstarlight)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to submit and manage media-generation jobs through the Phosor AI API, including video, image, speech, LoRA, and e-commerce photography workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flawed connection safeguards may expose the API key or selected uploads.

Mitigation: Prefer a corrected release before supplying a valuable key; validate exact hostnames, protect credentials across redirects, and disclose saved-key reuse.

Risk: Prompts and selected media are sent to Phosor, generation spends credits, and local tracking retains short text snippets; hosted-service behavior and retention were not verified.

Mitigation: Review prompts and media before submission, monitor credit use, and avoid including sensitive details in tracked text.

## Reference(s):

- [Phosor AI API documentation](https://docs.phosor.ai)
- [H3 prompt guide](https://phosor.ai/docs/minimax-h3-prompt-guide)
- [API reference (bundled)](artifact/references/api.md)
- [H3 prompt guide (bundled)](artifact/references/h3-prompt-guide.md)
- [ClawHub skill page](https://clawhub.ai/jasonstarlight/skills/phosor-ai-skills)
- [Phosor AI](https://phosor.ai)

## Skill Output:

**Output Type(s):** [Video, image, and audio media, JSON job, status, and result data, Shell commands, Configuration instructions, Markdown guidance]

**Output Format:** [Generated media and JSON API responses, with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media depends on the selected model and supplied prompt or reference assets.]

## Skill Version(s):

1.3.8 (source: frontmatter, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
