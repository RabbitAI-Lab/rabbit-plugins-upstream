## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's Gemini 2.5 TTS CLI for multilingual speech generation from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends text prompts and generation parameters to dLazy's hosted API.

Mitigation: Avoid sending sensitive text unless use of the hosted service is appropriate.

Risk: Use requires running the dLazy npm CLI locally.

Mitigation: Prefer the pinned npx/on-demand path when a persistent global binary is not desired.

Risk: The skill depends on a dLazy API key stored locally or supplied through the environment.

Mitigation: Rotate or revoke the API key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and npm or npx; generated media URLs are hosted by dLazy.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter reports 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
