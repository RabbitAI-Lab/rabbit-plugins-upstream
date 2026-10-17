## Description:

Helps agents request Suno music generation in inspiration or custom mode, with vocals or as instrumental music.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and other users can ask an agent to generate music from a prompt, supply custom lyrics and style, or request instrumental output through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external CLI and using the hosted service requires trusting the package and provider.

Mitigation: Review and verify the pinned @dlazy/cli package and dLazy service before use.

Risk: Prompts and explicitly supplied file paths may be sent to dLazy, and authentication stores an API key locally.

Mitigation: Avoid submitting sensitive prompts or files; protect the local API key and rotate or revoke it when necessary.

Risk: The example response shows an image output for a music-generation skill.

Mitigation: Treat that example as a documentation bug; check actual results before relying on its output type.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and guidance for obtaining generated music]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return a hosted result URL or an asynchronous task ID; the documented image-output example appears incorrect.]

## Skill Version(s):

1.3.29 (source: ClawHub release; skill file lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
