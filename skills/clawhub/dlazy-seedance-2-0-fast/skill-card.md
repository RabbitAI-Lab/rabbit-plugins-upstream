## Description:

Helps agents generate videos from text prompts and optional image, video, audio, or first-and-last-frame references using dLazy's Seedance 2.0 Fast service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from text and optional media references, including first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local images, videos, and audio are uploaded to dLazy's hosted service.

Mitigation: Avoid sending private media unless you are comfortable sharing it with dLazy.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Prefer a per-invocation environment variable when appropriate, and rotate or revoke the key if access is no longer trusted.

Risk: Using the skill requires a third-party npm CLI and hosted service.

Mitigation: Review the CLI before installation and use the pinned npx invocation if a global install is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Video URLs]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted media URLs or an asynchronous task ID; a requested result can be saved locally.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
