## Description:

Generates 2K, 3K, or 4K images from prompts and optional reference images for posters, key visuals, and large-format prints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers use this skill to generate high-resolution images from text prompts or reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or files as reference images.

Risk: Authentication may store a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key through the dLazy dashboard if needed.

Risk: Using the skill requires an external npm CLI.

Mitigation: Review the CLI before installation; use its on-demand npx option to avoid a global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0)
- [dLazy CLI repository (skill metadata link; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image URLs, JSON results]

**Output Format:** [JSON with generated image URLs; optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [2K, 3K, or 4K resolution; asynchronous jobs may return a task ID instead of an image URL.]

## Skill Version(s):

1.2.22 (source: ClawHub release; artifact frontmatter: 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
