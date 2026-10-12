## Description:

Generates and edits images from text prompts and optional reference images using the dLazy-hosted GPT Image 2.5 Flare service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from prompts and up to five reference images, with selectable aspect ratio and quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to the external dLazy service.

Mitigation: Avoid submitting sensitive prompts or media; review what you select before generating.

Risk: The external CLI requires a dLazy API key, and login stores it locally.

Mitigation: Use the on-demand npx option if preferred, protect the local key, and rotate or revoke it from the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Image URLs, JSON metadata]

**Output Format:** [Image URL in a JSON result; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task ID instead of an image.]

## Skill Version(s):

1.2.17 (source: ClawHub release metadata; bundled skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
