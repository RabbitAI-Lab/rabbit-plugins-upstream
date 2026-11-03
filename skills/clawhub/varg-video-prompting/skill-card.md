## Description:

Guides creators through choosing varg image, video, voice, and music models, writing reference-aware prompts, and checking generated shots before production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Video creators and production teams use this skill to choose models and prepare prompts for consistent image-to-video, video-to-video, still, voice, and music generation. It also provides a staged workflow for reviewing stills, estimating credit costs, and checking generated audio and frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded footage, photos, or recordings may contain confidential material, and upload results can include public-link fields.

Mitigation: Use only media authorized for sharing with varg and its model providers; confirm access controls and retention before uploading confidential material.

Risk: Generation retries and media-analysis steps can consume credits.

Mitigation: Set a credit ceiling, estimate the cost of a real request, and review one pilot before running a larger batch.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/varg-video-prompting)
- [varg](https://varg.ai)
- [Model catalog](https://varg.ai/models/llms.txt)
- [MCP tools guide](artifact/references/mcp-tools.md)
- [Model guidance](artifact/references/models.md)
- [Prompt templates](artifact/references/prompt-templates.md)
- [Examples and lessons learned](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [Guidance, Text prompts, Configuration]

**Output Format:** [Markdown guidance and prompt text, with JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes model-selection advice, staged review gates, and frame and audio QA checklists.]

## Skill Version(s):

1.0.0 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
