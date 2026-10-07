## Description:

Generates images from text prompts and edits or combines images provided as references through the dLazy image-generation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create images from prompts or edit images using up to five reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to the dLazy service.

Mitigation: Confirm that the service is trusted before sharing prompts or local images.

Risk: Signing in can save an API key locally, and installing the CLI introduces a dependency on third-party software.

Mitigation: Use the pinned npx command if a global installation is unwanted; rotate or revoke the dLazy API key if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI repository (skill metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Image URLs, JSON responses]

**Output Format:** [JSON with hosted image URLs; optionally downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports JPEG, PNG and WebP output; asynchronous requests return a task ID for later polling.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; supplied skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
