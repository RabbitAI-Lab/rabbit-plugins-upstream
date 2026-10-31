## Description:

Video generation skill that automatically selects the best dlazy CLI video model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to choose a dLazy hosted video model and generate or transform video from text prompts and media inputs, including image animation, reference-based generation, editing, and lip synchronization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local image, video, or audio inputs are uploaded to dLazy media storage for processing.

Mitigation: Submit only media you are comfortable sharing with dLazy.

Risk: The CLI stores the API key in its local configuration by default.

Mitigation: Use the documented DLAZY_API_KEY environment-variable option when preferred, and rotate or revoke keys through the dLazy dashboard as needed.

Risk: Video generation may consume account credits.

Mitigation: Consider generation charges and available credits before submitting a request.

Risk: The skill depends on the external dLazy CLI.

Mitigation: Review the CLI source before installation and use the version-pinned install command or npx package shown in the skill.

## Reference(s):

- [dLazy service information](https://dlazy.com)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON, Guidance]

**Output Format:** [Generated media URLs and a JSON response envelope, with model-selection and command guidance]

**Output Parameters:** [Variable by model and request; may include prompt, media inputs, duration, resolution, aspect ratio, and audio options]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; some workflows return video, audio, or mask-video URLs.]

## Skill Version(s):

1.4.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
