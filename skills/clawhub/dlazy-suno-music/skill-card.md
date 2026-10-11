## Description:

Helps agents generate vocal or instrumental music with Suno through dLazy, using automatic or user-provided lyrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request vocal or instrumental music from prompts, with automatic lyrics or custom lyrics and style settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the third-party CLI executes external package code.

Mitigation: Review the pinned package before use; run it on demand with npx instead of installing globally if preferred.

Risk: Prompts, selected media files, and generated outputs pass through dLazy's hosted service.

Mitigation: Only submit content approved for that service and review its terms before use.

Risk: The CLI can store an API key in local configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation access if local key storage is unsuitable.

## Reference(s):

- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns hosted output URLs or can save generated assets locally.]

## Skill Version(s):

1.3.26 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
