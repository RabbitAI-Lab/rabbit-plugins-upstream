## Description:

Synthesize text into natural-sounding speech with Doubao TTS through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate spoken audio from text for voiceovers and spoken responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text submitted for speech synthesis is sent to dLazy's external API, and generated assets are hosted by dLazy.

Mitigation: Only submit text you are comfortable sharing with dLazy; review the service terms before use.

Risk: The external CLI requires a dLazy API key and can store it locally.

Mitigation: Protect the local API key, rotate or revoke it through the dLazy dashboard when needed, and use the on-demand npx option if a global install is undesirable.

## Reference(s):

- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return a hosted speech asset URL or save generated audio locally.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
