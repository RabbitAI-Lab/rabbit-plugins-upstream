## Description:

Generates images from text prompts with Jimeng through the dLazy service, with optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or local files; review what is sent before generation.

Risk: The external CLI requires an API key and may be installed globally.

Mitigation: Use the on-demand npx option if preferred, and rotate or revoke the API key through the dLazy dashboard when necessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response with image URLs; optionally saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before an image is available.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
