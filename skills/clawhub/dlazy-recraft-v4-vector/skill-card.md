## Description:

Generates design assets from text prompts using dLazy's hosted Recraft V4 Vector tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to create logos, icons, and other design assets from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media may be sent to dLazy, and generated assets are hosted there.

Mitigation: Avoid submitting sensitive content without reviewing the dLazy service terms and data flow.

Risk: Login stores an API key locally, and the skill installs or runs an external npm CLI.

Mitigation: Review the CLI before installation and protect the locally stored API key.

Risk: The skill promises SVG, while its sample response shows a PNG image.

Mitigation: Check the returned MIME type and asset format before relying on vector output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI source (skill metadata link; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image files]

**Output Format:** [CLI JSON response with generated asset URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [SVG is advertised, but the documented response example is PNG; verify the delivered format.]

## Skill Version(s):

1.3.25 (source: server-resolved release; skill frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
