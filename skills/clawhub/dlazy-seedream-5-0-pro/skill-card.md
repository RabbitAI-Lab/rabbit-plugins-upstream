## Description:

Generates detailed images from text prompts and optional reference images for commercial visuals and brand assets using Seedream 5.0 Pro.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, designers, and developers use this skill to generate commercial key visuals and brand assets from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and parameters are sent to a third-party cloud service, and provided local media may be uploaded.

Mitigation: Avoid supplying sensitive prompts or files unless their transfer to dLazy is approved.

Risk: Login may store an API key locally, and installation uses a third-party npm CLI.

Mitigation: Use the pinned npx command or a per-invocation DLAZY_API_KEY to reduce persistent installation or credential storage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs; an optional save command downloads them locally.]

## Skill Version(s):

1.2.20 (source: ClawHub release; bundled skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
