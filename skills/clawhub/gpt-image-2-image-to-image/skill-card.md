## Description:

GPT Image 2 图生图 helps agents generate new images from one or more authorized reference images while preserving specified subjects, layouts, identity facts, or commercial details and changing style, scene, material, finish, or aspect ratio through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, product teams, and developers use this skill to guide image-to-image transformations from authorized reference images while keeping important identity, layout, product, and scene constraints explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected reference images and prompts are sent to AI Hive for generation.

Mitigation: Use only images you have rights to upload and avoid sending sensitive reference material unless AI Hive handling is acceptable for the task.

Risk: An AI Hive API key may be stored locally for repeated use.

Mitigation: Use the disclosed local config path with 0600 permissions or provide the key through the CLI or environment for stricter session control.

Risk: Generated outputs are downloaded to the user's machine and may need review before publication.

Mitigation: Review generated files against the transformation contract, especially identity, layout, logo, text, and commercial-fact constraints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-image-to-image)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash commands and CLI status text; generated image files are downloaded to a local directory.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least one user-selected reference image and an AI Hive API key supplied by CLI, environment variable, or local config.]

## Skill Version(s):

1.0.1 (source: server evidence release.version and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
