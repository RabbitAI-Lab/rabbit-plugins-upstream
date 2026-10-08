## Description:

Generates detailed images from text prompts and optional reference images for commercial visuals and brand materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and creative teams use this skill to generate brand visuals and other high-detail images from prompts, with optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected private media are sent to dLazy's hosted service, which also hosts results.

Mitigation: Avoid supplying sensitive prompts or media unless upload and hosting are acceptable.

Risk: Login saves an API key locally, and use requires a paid cloud account.

Mitigation: Protect the local key and check account costs before generating images.

Risk: A global CLI install persists on the user's system.

Mitigation: Use the documented pinned npx command when a persistent install is not wanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image URLs, Image files, Text]

**Output Format:** [JSON response with hosted image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task ID instead of an image.]

## Skill Version(s):

1.2.22 (source: ClawHub release; bundled skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
