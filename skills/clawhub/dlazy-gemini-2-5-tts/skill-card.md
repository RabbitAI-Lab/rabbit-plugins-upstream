## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to authenticate with dLazy and invoke the pinned dLazy CLI for Gemini 2.5 text-to-speech generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected parameters are sent to dLazy's hosted API, and generated results are hosted by dLazy.

Mitigation: Use the skill only when hosted processing is acceptable for the data, and avoid submitting sensitive content unless the user's policy allows it.

Risk: Authentication can store a dLazy API key in the local user configuration.

Mitigation: Prefer per-invocation credentials or npx when persistence is undesirable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact includes an inaccurate image/png output example for a text-to-speech skill.

Mitigation: Treat the example as documentation quality noise and validate actual CLI responses for audio output URLs or asynchronous task status.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [CLI command guidance and JSON responses containing hosted generated audio outputs or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and selected parameters are sent to dLazy's hosted API.]

## Skill Version(s):

1.3.17 (source: server release evidence; artifact frontmatter lists 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
