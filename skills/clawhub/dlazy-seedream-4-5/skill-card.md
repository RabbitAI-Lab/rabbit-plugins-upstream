## Description:

Helps agents generate images from text prompts or reference images using Doubao Seedream 4.5 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users generate images from prompts or supplied images, then retrieve hosted results or save them locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and chosen local images are sent to dLazy, and generated images are hosted by dLazy.

Mitigation: Use only inputs and outputs appropriate for a hosted service; invoke this provider explicitly.

Risk: The login flow can persist an API key in local CLI configuration.

Mitigation: Use npx to avoid a persistent global CLI install and DLAZY_API_KEY for per-invocation authentication when less local persistence is desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI source (CLI reference; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs and can optionally be saved as local files; asynchronous requests can return a task ID.]

## Skill Version(s):

1.3.31 (source: ClawHub release evidence; supplied skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
