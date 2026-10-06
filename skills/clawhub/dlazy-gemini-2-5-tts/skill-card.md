## Description:

Helps agents generate multilingual speech from text with Gemini 2.5 TTS through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn text prompts into multilingual speech with selectable voices via dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the external dLazy CLI exposes the environment to third-party software.

Mitigation: Confirm the package is trusted before installation; use the pinned on-demand npx option instead of a global install when appropriate.

Risk: Prompts and supplied media may be sent to dLazy's cloud service.

Mitigation: Send only content approved for external processing, and rotate or revoke the dLazy API key when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text and shell commands; CLI results are JSON with hosted output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; asynchronous requests may return a task ID pending completion.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; bundled skill frontmatter lists 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
