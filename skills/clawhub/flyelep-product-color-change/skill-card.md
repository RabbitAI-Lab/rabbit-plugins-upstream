## Description:

Uses the Flyelep AI Tool API to identify products in images and generate recolored product image results when users want the same product shown in a different color.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to collect product image URLs, target color instructions, and a user-provided Flyelep API key, then call Flyelep endpoints to return a recolored product image URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a user-provided Flyelep API key at runtime.

Mitigation: Ask the user for the key only when needed and avoid storing it in skill files, examples, repositories, or persistent configuration.

Risk: Local images uploaded through the helper path may become permanently accessible through a public provider URL.

Mitigation: Use the upload path only for images appropriate for Flyelep processing and avoid uploading sensitive or restricted content.

Risk: Color-change results can vary when prompts are vague or product boundaries are unclear.

Mitigation: Collect a clear target color, preservation constraints, and a clean source product image before calling the API.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-product-color-change)
- [Flyelep controlboard](https://www.flyelep.cn/controlboard)
- [Flyelep product color change API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/productColorChange)
- [Flyelep file upload API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples and curl commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns or displays the resulting product image URL without reading image contents back to the user.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
