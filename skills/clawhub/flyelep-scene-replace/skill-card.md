## Description:

Calls the Flyelep AI scene replacement API to replace an image background with a target scene guided by a reference image and text prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect required public image URLs, prompt text, and a Flyelep API key, then call Flyelep to generate a scene-replaced image URL while preserving the subject.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs, prompt text, and the Flyelep secretKey are shared with Flyelep during API calls.

Mitigation: Use the skill only when that sharing is approved, and avoid sensitive or private image links.

Risk: Temporary payload files may contain request data when the Windows/PowerShell workflow is used.

Mitigation: Delete the temporary payload file after the API call completes.

Risk: Non-public, expired, or non-direct image URLs can cause API failures or unintended access exposure.

Mitigation: Provide only approved, publicly reachable direct image URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-scene-replace)
- [Flyelep scene replacement API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/sceneReplace)
- [Flyelep open platform](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and curl commands; API response data is a generated image URL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided public image URLs, a text prompt, and a Flyelep secretKey; temporary payload files should be removed after use.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
