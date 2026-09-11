## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Chinese or English speech from text prompts through the dLazy CLI and hosted text-to-speech service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts and any files explicitly passed to the command are sent to dLazy's hosted service.

Mitigation: Use the skill only for content suitable for that service and review dLazy's terms before sending sensitive material.

Risk: The skill installs or runs a third-party npm CLI.

Mitigation: Prefer the pinned npx command when a persistent global binary is not desired, review the linked package and source, and avoid running npm with elevated privileges.

Risk: The dLazy API key grants access to the user's organization.

Mitigation: Store the key using the CLI or environment variable as appropriate, and rotate or revoke it when the service is no longer used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON result from the dLazy CLI with generated audio output URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and npm or npx; generated output URLs are hosted by files.dlazy.com.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
