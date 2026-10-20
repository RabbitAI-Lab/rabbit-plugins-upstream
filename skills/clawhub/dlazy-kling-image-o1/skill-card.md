## Description:

Generates images from text prompts or reference images using Kling Image O1 through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from prompts and optional reference images through dLazy's Kling Image O1 integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local images may be sent to the third-party dLazy service, which also hosts generated assets.

Mitigation: Avoid using private prompts or files unless you intend to share them with dLazy.

Risk: Login can store an API key locally, and installing the CLI runs third-party software.

Mitigation: Protect local credentials and review the pinned CLI before installation; use the pinned npx option to avoid a persistent global installation.

## Reference(s):

- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response with generated image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID before images are ready.]

## Skill Version(s):

1.3.31 (source: server-resolved release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
