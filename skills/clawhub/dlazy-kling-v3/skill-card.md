## Description:

Helps agents generate Kling V3 videos from text prompts or reference images through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short text-to-video or image-to-video generations, adjust generation settings, and retrieve resulting media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media are sent to dLazy's hosted services.

Mitigation: Share only prompts and files approved for upload; review sensitive content before submitting.

Risk: The CLI stores an API key locally and installation runs a third-party npm package.

Mitigation: Review the pinned package before installation, use on-demand npx if preferred, and rotate or revoke the key when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI homepage (declared in metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (declared in metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Video URLs]

**Output Format:** [CLI commands and JSON responses with media URLs or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated media locally when requested.]

## Skill Version(s):

1.3.28 (source: ClawHub release evidence; artifact frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
