## Description:

Provides ElevenLabs eleven_v3 text-to-speech through the dLazy CLI with curated multilingual voices and stability, similarity, and style controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate speech audio for dubbing, audiobooks, and character dialogue by sending text prompts and voice parameters to dLazy's hosted text-to-speech service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected inputs, and generated outputs are processed through a third-party cloud service.

Mitigation: Avoid sending confidential or regulated content unless the deployment has approved dLazy's service terms and data handling.

Risk: The skill depends on a third-party npm CLI and local API key configuration.

Mitigation: Review the pinned CLI package before installation, restrict access to the local config file, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: The service may require paid credits and can fail when credits are insufficient.

Mitigation: Use dry-run or cost-estimate flows where appropriate and handle insufficient-balance errors before retrying generation.

Risk: The artifact's output example describes an image result even though the skill is for text-to-speech.

Mitigation: Verify the returned media type and saved file before relying on generated output in downstream workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration instructions]

**Output Format:** [CLI JSON response with hosted result URLs and optional local audio files saved through --save.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may use paid credits; asynchronous runs can return a generateId for later polling.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
