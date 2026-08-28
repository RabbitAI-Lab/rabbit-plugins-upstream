## Description:

Generate high-quality Vidu Q2 images from text prompts or image inputs using the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to generate or edit images with Vidu Q2 through dLazy's CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local image paths may be sent or uploaded to dLazy hosted endpoints.

Mitigation: Review prompts and file inputs before execution, and avoid submitting sensitive or regulated content unless dLazy's service terms and controls are acceptable.

Risk: The dlazy login flow stores an API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation when persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global npm install persists the dLazy CLI binary on the host.

Mitigation: Use the pinned npx invocation path when a non-persistent CLI execution is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results containing generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated image assets to a local path when the --save option is used.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
