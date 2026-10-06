## Description:

Helps agents generate vocal or instrumental music using inspiration or custom-lyrics modes through the dLazy Suno music service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request Suno music with automatically generated or supplied lyrics, including instrumental tracks, through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media files may be sent to dLazy's hosted service.

Mitigation: Avoid sending sensitive prompts or media and review the service terms before use.

Risk: Using the external CLI requires trusting its package and may save an API key locally.

Mitigation: Review the CLI package and source before installation and protect the locally stored key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON results]

**Output Format:** [Markdown instructions and CLI commands; generated results returned as JSON with asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs and optional local asset download.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
