## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent call dLazy's Doubao TTS wrapper, converting supplied text into generated speech with selectable Chinese or English voices and speed settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and API-key authenticated requests are handled by dLazy's hosted API.

Mitigation: Avoid sending sensitive text, use scoped keys where possible, and rotate the dLazy API key if exposure is suspected.

Risk: The skill depends on a third-party npm CLI.

Mitigation: Prefer npx @dlazy/cli@1.2.3 or an isolated user environment, and review the upstream package/source before use.

Risk: Generated result URLs are hosted by dLazy media storage.

Mitigation: Treat returned URLs and saved audio files according to the user's data handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration]

**Output Format:** [JSON results with generated audio URLs or task status, plus optional downloaded audio files when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and parameters are sent to dLazy hosted API endpoints.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
