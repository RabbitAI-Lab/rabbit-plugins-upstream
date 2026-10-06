## Description:

Helps agents generate videos from text prompts or reference images using Kling V3 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-video or image-to-video generation and retrieve the resulting media through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied for generation are uploaded to the dLazy cloud service.

Mitigation: Use only content approved for upload to dLazy and avoid supplying sensitive local files.

Risk: Generation may consume account credits.

Mitigation: Check the cost estimate with --dry-run before submitting a generation request.

Risk: Authentication may store an API key locally, and global CLI installation persists on the system.

Mitigation: Protect the local key and use the pinned npx invocation if a persistent global install is not wanted.

Risk: Generic video requests could trigger unintended dLazy generation.

Mitigation: Invoke this skill explicitly for Kling/dLazy video generation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [CLI commands and JSON responses with media URLs or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media may be saved locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.25 (source: ClawHub release evidence; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
