## Description:

Helps agents generate cinematic videos from text prompts and images using Veo 3.1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide text-to-video, image-guided video generation, and video extension with dLazy's hosted Veo 3.1 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-supplied media may be sent to dLazy and generated results hosted there.

Mitigation: Avoid submitting private prompts or media unless approved for the service.

Risk: Authentication can store an API key in local CLI configuration.

Mitigation: Protect local credentials or use per-invocation environment authentication.

Risk: Broad video-generation triggers can consume paid API credits.

Mitigation: Confirm the request and cost before generating; use dry-run when appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return hosted video links or save generated media locally.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release metadata; source frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
