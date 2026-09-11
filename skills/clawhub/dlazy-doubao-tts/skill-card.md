## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to synthesize Chinese or English text into natural speech through the dLazy Doubao TTS CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and selected local media paths to dLazy's hosted service.

Mitigation: Avoid sending sensitive text or files unless cloud processing is intended.

Risk: The skill depends on an npm-distributed CLI and API credentials.

Mitigation: Prefer npx or an isolated install, review the CLI package provenance, and rotate or revoke the dLazy API key when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI GitHub Project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated speech assets are returned as hosted URLs and can be saved locally with --save.]

## Skill Version(s):

1.3.14 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
