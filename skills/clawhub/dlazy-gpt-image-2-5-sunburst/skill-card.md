## Description:

Generates and edits detailed images from prompts, with optional reference images and controls for aspect ratio and quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images where fine detail, text rendering, and composition matter. It requires a dLazy account and API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service.

Mitigation: Only submit prompts and files you are comfortable sharing with dLazy.

Risk: The third-party CLI may be installed globally and login saves an API key locally.

Mitigation: Review the CLI before installing; use the pinned npx invocation and per-invocation DLAZY_API_KEY if you prefer not to retain a global install or saved key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI repository (declared in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image files]

**Output Format:** [JSON with hosted image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to five reference images; asynchronous requests can return a task ID instead of an image.]

## Skill Version(s):

1.2.18 (source: ClawHub release metadata; skill frontmatter and CLI install specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
