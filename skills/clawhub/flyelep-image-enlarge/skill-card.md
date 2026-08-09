## Description:

Uses the Flyelep AI Tool API to enlarge and enhance one or more public image URLs, returning the processed image URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call Flyelep's image enlargement API for single-image or batch enhancement workflows. It is suited for improving clarity, upscaling image dimensions, and enhancing product images when users provide public image URLs, a scaling ratio, and a Flyelep API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided image URLs and a Flyelep secretKey to Flyelep for processing.

Mitigation: Use the skill only when Flyelep's terms and data handling are acceptable, avoid private or sensitive image URLs, and provide the secretKey only at runtime.

Risk: Credentials or request details may be exposed if copied into shared files, repositories, or logs.

Mitigation: Do not persist real secretKey values in skill files, examples, repositories, or shared logs; remove temporary payload files after use.

## Reference(s):

- [Flyelep Image Enlarge API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/enlarge)
- [Flyelep Open Platform console](https://www.flyelep.cn/controlboard)
- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-image-enlarge)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns Flyelep response JSON containing comma-separated processed image URLs; requires user-provided image URLs, scalingRatio, and secretKey at runtime.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
