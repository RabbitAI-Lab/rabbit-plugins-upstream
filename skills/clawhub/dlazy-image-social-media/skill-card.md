## Description:

Guides agents through planning and creating platform-tailored social-media visuals, captions, and image-generation requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan social-media images, thumbnails, and carousels for specific platforms, then generate visuals and separate caption copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media supplied for generation may be sent to dLazy's cloud service.

Mitigation: Only provide content and media you are comfortable sending to dLazy.

Risk: Signing in stores a dLazy API key locally.

Mitigation: Protect the local key and rotate or revoke it in your dLazy account if needed.

Risk: A global CLI installation remains on the user's system.

Mitigation: Use the documented npx invocation for temporary use if a global install is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Image URLs]

**Output Format:** [Markdown with design plans, caption copy, CLI commands, and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps in-image text separate from captions and checks platform dimensions and safe areas.]

## Skill Version(s):

1.3.25 (source: ClawHub release evidence; artifact frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
