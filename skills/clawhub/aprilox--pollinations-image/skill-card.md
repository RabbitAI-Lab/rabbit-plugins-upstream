## Description:

Generate detailed images from text prompts using Pollinations.ai models with optional configuration, model selection, and advanced settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aprilox](https://clawhub.ai/user/aprilox)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users can use this skill to generate image files from text prompts through Pollinations.ai, compare available models, set persistent defaults, and tune generation options such as size, seed, watermark removal, and prompt enhancement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shell script has unsafe code-execution risk when loading configuration or handling generated commands.

Mitigation: Review the shell script before installation, avoid untrusted arguments or configuration files, and run it with least-privilege local permissions.

Risk: The configuration command can disclose whether an API key is configured and may expose secret-handling weaknesses.

Mitigation: Do not run the configuration command with a real API key until the key-printing issue is fixed, and avoid storing sensitive secrets in shared logs or terminals.

Risk: Text prompts are sent to the Pollinations image generation service.

Mitigation: Avoid sensitive, confidential, or regulated prompts unless the service terms and the user's environment approve that use.

## Reference(s):

- [Pollinations.ai](https://pollinations.ai)
- [Pollinations API Key Portal](https://enter.pollinations.ai)
- [ClawHub Skill Page](https://clawhub.ai/aprilox/skills/pollinations-image)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files]

**Output Format:** [Terminal text with generated image files saved to disk]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation output includes the selected model, image dimensions, prompt, file name, file size, and local output path.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
