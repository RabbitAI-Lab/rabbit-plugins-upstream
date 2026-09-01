## Description:

Automatically generates video storyboard packages with shot design, camera movement guidance, copy/script text, and storyboard images through the LinkPix qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and marketing teams use this skill to turn product images and product positioning into a storyboard script and related storyboard images. Agents use it when the user asks for a storyboard, shot script, shooting script, or storyboard images rather than a finished video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires installing and running a Node-based qhkit CLI.

Mitigation: Install the CLI only in environments where Node CLI execution is acceptable, and remove or stop using it when the storyboard workflow is no longer needed.

Risk: Selected product images are uploaded to the LinkPix/qhkit service during generation.

Mitigation: Use only images approved for upload to the provider and confirm the submitted reference images before starting credit-consuming generation.

Risk: The workflow requires a configured API key.

Mitigation: Use a revocable key, avoid exposing it in chat or logs, and remove or rotate the token when it is no longer needed.

Risk: Storyboard script and image generation can consume account credits.

Mitigation: Confirm key parameters and expected credit use with the user before submitting generation actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-storyboard)
- [@iqinghu/qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API Key Console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [LinkPix API Key Guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with CLI commands, JSON parameters, storyboard script text, and generated image delivery guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may call qhkit storyboard script, generate, and status actions; generated image delivery depends on the active agent environment.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
