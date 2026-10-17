## Description:

Helps agents generate videos with Tongyi Wanxiang 2.7 from text prompts, first and last frames, or reference media through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating short videos from prompts, images, video references, or frame images via dLazy's video-generation CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media supplied to the hosted service may be uploaded to dLazy.

Mitigation: Avoid sending sensitive prompts or media unless sharing them with dLazy is acceptable.

Risk: Signing in may save an API key locally, and installing the CLI adds a third-party package.

Mitigation: Protect the local key and review the @dlazy/cli package before installing; use the documented pinned npx invocation to avoid a persistent global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Media URLs]

**Output Format:** [Markdown guidance and CLI commands; JSON responses with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be saved locally; asynchronous requests return a task ID for status checks.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release; bundled frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
