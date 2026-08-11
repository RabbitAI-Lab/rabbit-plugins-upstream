## Description:

Replaces the product in a source image with a specified product image through the Flyelep AI Tool API while preserving the original background, lighting, and scene.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to replace a visible product in an image by collecting required image URLs, prompt constraints, and a Flyelep API key, then calling the Flyelep product replacement endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime use sends image URLs, prompts, and a Flyelep API key to Flyelep.

Mitigation: Confirm the user is comfortable sharing those inputs, treat product images and prompts as potentially sensitive, and request the API key only at runtime.

Risk: Real API keys could be exposed if written into skill files, examples, repositories, or persistent configuration.

Mitigation: Keep the Flyelep secretKey in request headers only for the active call and avoid storing it in files or long-lived configuration.

Risk: Temporary payload files used for Windows or PowerShell requests may retain sensitive image URLs, prompts, or credentials after execution.

Mitigation: Use UTF-8 no-BOM temporary payload files only when needed and delete them immediately after the API response.

Risk: Documentation is inconsistent about whether replaceImageUrl accepts one image or multiple comma-separated image URLs.

Mitigation: Prefer a single replaceImageUrl unless the user confirms multi-image behavior against Flyelep's current API documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-product-replace)
- [Flyelep product replacement API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/productReplace)
- [Flyelep controlboard](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, text]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns or presents the product-replaced image URL from the Flyelep API response.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
