## Description:

Replaces the product in an image with a specified product image through the Flyelep AI Tool API while preserving the original background, lighting, and scene composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to replace a product subject in an existing image with one or more target product images while retaining the original scene context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Flyelep secretKey at runtime.

Mitigation: Request the secretKey only from the user at execution time and avoid storing it in skill files, repositories, logs, or persistent configuration.

Risk: Source and replacement product images are sent to Flyelep for processing.

Mitigation: Use only images whose privacy and data-handling requirements are compatible with Flyelep processing, and avoid private or sensitive images unless that transfer is acceptable.

Risk: Local image files may need to be uploaded to obtain public image URLs before product replacement.

Mitigation: Confirm that the user wants local files uploaded and reuse the returned public URL only for the current task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-product-replace)
- [Flyelep product replacement API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/productReplace)
- [Flyelep file upload API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)
- [Flyelep control board](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON payloads and curl commands; successful API calls return a product-replaced image URL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided secretKey and source/replacement product images; modelType is fixed to 9; replaceImageUrl accepts up to 3 comma-separated images.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
