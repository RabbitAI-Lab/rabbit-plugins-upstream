## Description:

Uses the Flyelep AI Tool API to identify a product in an image and generate a new image URL with the product color changed while preserving the product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to collect a product image URL, color-change prompt, and Flyelep API key, call Flyelep's product color-change endpoint, and return the resulting image URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product image URLs, prompts, and the Flyelep API key are sent to a third-party Flyelep service.

Mitigation: Install and use the skill only after confirming that this data sharing is acceptable for the intended products, prompts, and account.

Risk: The Flyelep secretKey may be exposed if stored in skill files, persistent configuration, temporary payloads, or shell history.

Mitigation: Provide the key only at runtime through secure secret handling where available, avoid committing or saving real keys, and remove any temporary payload file after the API call.

Risk: Color-change output can be inaccurate when the prompt is vague or the source image does not clearly show the product and target area.

Mitigation: Use a clear public image URL and a specific prompt that names the target color, preserved materials, background, brand marks, lighting, and any product parts that should not change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-product-color-change)
- [Flyelep product color-change API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/productColorChange)
- [Flyelep open platform controlboard](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON request bodies, shell command examples, and a returned image URL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided public source image URL, color-change prompt, modelType 0, and Flyelep secretKey at runtime.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
