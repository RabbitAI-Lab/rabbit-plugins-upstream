## Description:

Generates ElevenLabs-style multi-voice dialogue audio through the pinned dLazy CLI, letting agents assign voices to dialogue lines and request a complete conversation render.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to generate character dialogue, podcast segments, and short skit audio by passing dialogue lines, voice assignments, and generation settings to the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue prompts, generation parameters, and local media files supplied to the CLI may be sent to dLazy cloud endpoints.

Mitigation: Avoid submitting sensitive content unless the user accepts that cloud processing path, and prefer dry runs when checking payloads or cost.

Risk: Logging in with the CLI may persist a dLazy API key in the local user configuration.

Mitigation: Use npx with DLAZY_API_KEY for less persistent setup, and rotate or revoke organization API keys when access should end.

Risk: The skill depends on a third-party hosted service and a pinned third-party CLI package.

Mitigation: Review the pinned CLI source and npm package before installation when the release will handle sensitive or production content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI command guidance and JSON responses containing hosted generated output URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return asynchronous task identifiers when --no-wait is used.]

## Skill Version(s):

1.3.8 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
