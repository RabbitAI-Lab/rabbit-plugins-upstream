## Description:

Generates 1MP raster images from text prompts for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers use this skill to generate raster images from text prompts for everyday creative work and rapid iteration via dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input files are sent to dLazy's hosted service.

Mitigation: Review prompts and files for sensitive content before submitting them.

Risk: Authentication may save a dLazy API key in local user configuration.

Mitigation: Protect the key; use DLAZY_API_KEY for per-invocation credentials if preferred.

Risk: Image generation may consume paid credits.

Mitigation: Check the cost estimate with --dry-run before submitting a request.

## Reference(s):

- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results include JSON with generated image URLs; images can optionally be saved locally.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; bundled skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
