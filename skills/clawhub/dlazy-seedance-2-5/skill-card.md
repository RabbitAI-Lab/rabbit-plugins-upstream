## Description:

Guides agents in generating short videos with Seedance 2.5 through dLazy, using text prompts, optional media references, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short-form videos for storytelling and advertising, with optional image, video, audio, or frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media may be sent to dLazy's hosted service.

Mitigation: Review prompts and media for sensitive content before submitting them.

Risk: Generation may consume account credits.

Mitigation: Check available credits and use the documented dry-run cost estimate before generating.

Risk: The dLazy API key may be stored locally by the CLI.

Mitigation: Use the per-invocation DLAZY_API_KEY option when persistent storage is unsuitable; rotate or revoke exposed keys.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy service](https://dlazy.com)
- [dLazy CLI package listed in skill metadata](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository listed in skill metadata (not verified release provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Video result URLs]

**Output Format:** [Markdown instructions and CLI JSON responses with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs; the embedded installation instructions pin dLazy CLI 1.2.3.]

## Skill Version(s):

1.2.23 (source: server-resolved ClawHub release; embedded frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
