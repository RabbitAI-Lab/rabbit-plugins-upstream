## Description:

Generate high-quality images with Vidu Q2, supporting text-to-image and image-to-image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Vidu Q2 image-generation CLI from an agent, using prompts and optional reference images to produce hosted image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs the external @dlazy/cli package and sends prompts plus selected local image files to dLazy hosted endpoints.

Mitigation: Review the package before use, prefer npx or a scoped local install, and only provide prompts or image files that are appropriate to upload to the service.

Risk: The CLI can store a dLazy API key in the local user configuration.

Mitigation: Use a revocable key, rotate it when needed, or pass DLAZY_API_KEY per invocation to avoid persistent credential storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent can request synchronous image results, asynchronous task IDs, or saved files through the dLazy CLI.]

## Skill Version(s):

1.3.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
