## Description:

Generate and edit images with Alibaba Qwen Image 3.0 and 2.1 (Pro, Turbo, LoRA) via the PopNow API: strong Chinese and English text rendering, multi-image batches and precise edits. Exact USD quotes first. Use when the user asks for Qwen Image, bilingual text in images or batch image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyuminjo](https://clawhub.ai/user/kyuminjo)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users can ask an agent to generate or edit images with Qwen Image through PopNow, including bilingual text, batches, and targeted edits. The agent checks the current model schema and quoted price, then proceeds only after the user approves the exact maximum charge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image generation uses a paid API balance, so requests can incur charges.

Mitigation: Use a dedicated key with spending limits and approve each exact quoted maximum charge before generation.

Risk: Prompts and reference-media URLs are shared with PopNow and its generation provider; command arguments may remain in host logs.

Mitigation: Avoid sending sensitive material, keep the API key in secret settings, and review the provider's privacy terms.

## Reference(s):

- [Qwen Image model page](https://popnow.ai/models/qwen-image-2-1-pro)
- [PopNow task API documentation](https://popnow.ai/docs/tasks)

## Skill Output:

**Output Type(s):** [Images, Guidance]

**Output Format:** [Generated image links with concise status and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image count and detail depend on the selected model and request.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
