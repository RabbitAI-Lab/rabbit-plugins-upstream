## Description:

This skill helps agents use dLazy's ElevenLabs Dialogue wrapper to generate multi-voice dialogue audio from per-line voice and text inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to route dialogue lines through a dLazy CLI command for ElevenLabs multi-voice audio generation, including character dialogue, podcasts, and short skits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the dLazy CLI through npm or npx executes third-party code locally.

Mitigation: Review the dLazy CLI package before installation and prefer npx or an isolated environment when a persistent global binary is not needed.

Risk: The skill requires a dLazy API key and stores or accepts credentials through local configuration or environment variables.

Mitigation: Keep the API key revocable, rotate it when needed, and avoid sharing local configuration files or command histories that may expose credentials.

Risk: The evidence notes documentation copy-paste errors around output type and command examples.

Mitigation: Check `dlazy elevenlabs-dialogue -h` before use and verify generated command flags against the CLI help output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked third-party CLI/API returns hosted audio result URLs or async task identifiers; local file saving is optional through the CLI.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
