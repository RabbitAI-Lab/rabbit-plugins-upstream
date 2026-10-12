## Description:

Synthesizes Chinese or English text into speech using Doubao TTS through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and other users can turn text into spoken audio with selectable Chinese or English voices and speech speed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to the dLazy hosted API and may contain sensitive text.

Mitigation: Avoid sensitive prompts unless comfortable with the provider handling them; review the CLI package before installation.

Risk: Logging in saves an API key to local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-run authentication if a saved key is undesirable.

Risk: The documented output example shows an image rather than speech audio.

Mitigation: Treat the example as a documentation error and verify the actual output before relying on its format.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and references to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service returns an output URL; optional --save downloads the result, and --no-wait returns an asynchronous task ID.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
