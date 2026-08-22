## Description:

ElevenLabs eleven_v3 text-to-speech with curated multilingual voices and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's ElevenLabs TTS wrapper for dubbing, audiobooks, and character dialogue generation from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied files are processed by dLazy's hosted service.

Mitigation: Review prompts and file inputs for confidential or regulated data before invoking the skill.

Risk: Generated outputs are hosted on files.dlazy.com.

Mitigation: Treat generated URLs as externally hosted artifacts and avoid sharing sensitive output through this workflow unless the deployment policy allows it.

Risk: The dLazy CLI may persist an API key in local user configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, json, files]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses that reference generated media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated outputs are hosted on files.dlazy.com.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
