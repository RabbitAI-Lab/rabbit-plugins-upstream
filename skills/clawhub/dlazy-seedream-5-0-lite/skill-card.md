## Description:

Generates images from text prompts or reference images using Doubao Seedream 5.0 Lite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts and optionally transform reference images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image files are sent to dLazy's hosted service, and generated files are hosted there.

Mitigation: Submit only content approved for external processing and sharing.

Risk: Login may save an API key locally.

Mitigation: Use a per-command DLAZY_API_KEY if persistent storage is not desired.

Risk: A global CLI installation persists on the machine.

Mitigation: Use the pinned npx invocation if a global install is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image URLs or optional saved image files; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.30 (source: ClawHub release; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
