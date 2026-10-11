## Description:

Generates images from text prompts or reference images using Seedream 4.5 through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-image or image-to-image generation and retrieve hosted image links or saved image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to dLazy for processing, and generated images are hosted by dLazy.

Mitigation: Review inputs for sensitive content and confirm the service is appropriate before uploading them.

Risk: Login can save an API key to local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials if persistent storage is undesirable.

Risk: Installing the third-party npm CLI executes third-party software.

Mitigation: Review the package and source before installing; use the pinned npx invocation to avoid a persistent global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown guidance with shell commands and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be hosted by dLazy or saved to a local path.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
