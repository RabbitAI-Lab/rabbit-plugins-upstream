## Description:

Helps agents generate images from text prompts or reference images using Doubao Seedream 4.5 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-image and image-to-image generation through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected reference files may be sent to dLazy, and generated images are hosted by dLazy.

Mitigation: Send only content you are comfortable sharing with the hosted service and review selected files before upload.

Risk: Logging in can save an API key locally, and global CLI installation persists on the machine.

Mitigation: Use per-invocation DLAZY_API_KEY and the npx option when less local persistence is preferred.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return hosted image URLs or save generated images locally; asynchronous calls return a task ID.]

## Skill Version(s):

1.3.30 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
