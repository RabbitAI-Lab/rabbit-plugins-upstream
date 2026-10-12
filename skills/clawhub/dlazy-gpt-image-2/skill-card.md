## Description:

Helps agents generate images from text prompts and edit images using reference inputs through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users generate images from prompts or edit and combine images using reference files through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to dLazy's hosted service, and generated files may be hosted there.

Mitigation: Only submit prompts and files approved for external processing; review hosted results before sharing.

Risk: Authentication may store an API key in the local CLI configuration.

Mitigation: Protect and rotate the key as needed, or use the per-invocation environment variable instead of saving it.

Risk: A global CLI installation persists on the user's system.

Mitigation: Use the pinned npx command when a persistent global installation is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI homepage (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and generated-image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns image URLs or an asynchronous task ID; images can optionally be saved locally.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
