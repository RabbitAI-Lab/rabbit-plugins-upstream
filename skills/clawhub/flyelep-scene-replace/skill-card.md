## Description:

Helps an agent call the Flyelep AI Tool API to replace an image background scene with a target scene using a reference image and text prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to gather required image URLs, prompt text, and a Flyelep secretKey, then call Flyelep's scene replacement API and return the generated image URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a user-provided Flyelep secretKey for API calls.

Mitigation: Provide the secretKey only at runtime, do not store it in skill files or persistent configuration, and rotate it if it is exposed.

Risk: Uploading local images can create permanent public URLs accessible to anyone with the link.

Mitigation: Avoid confidential, personal, or proprietary images unless that exposure is acceptable; prefer already-public image URLs for sensitive workflows.

Risk: Incorrect inputs can cause failed calls or poor scene replacement results.

Mitigation: Confirm required parameters with the user, keep modelType set to 9, provide exactly one optional reference image, and use a specific textPrompt.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-scene-replace)
- [Flyelep scene replacement API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/sceneReplace)
- [Flyelep file upload API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)
- [Flyelep control board](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with HTTP, JSON, shell, and PowerShell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the scene replacement result as an image URL when the API call succeeds.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
