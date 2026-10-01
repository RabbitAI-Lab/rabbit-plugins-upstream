## Description:

Guides agents to generate videos through dLazy's Seedance 2.5 CLI using text prompts and optional image, video, audio, or frame references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide video generation from prompts and optional media references through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media files explicitly supplied to the CLI may be uploaded to dLazy's hosted service.

Mitigation: Submit only prompts and media you are authorized to share with that service.

Risk: CLI login saves an API key in local configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable when local key storage is unsuitable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI repository (listed in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance and shell commands; the CLI returns JSON containing media URLs or task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets can be downloaded locally; asynchronous jobs can return a task ID for later polling.]

## Skill Version(s):

1.2.19 (source: ClawHub release evidence; artifact frontmatter and CLI install specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
