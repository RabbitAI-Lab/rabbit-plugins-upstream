## Description:

Generates logo, icon, and other design imagery from text prompts using the dLazy Recraft V4 Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to request logos, icons, and other design assets from text prompts through dLazy's hosted image-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the third-party dLazy CLI executes external software.

Mitigation: Review the CLI and the pinned package version before installing or running it.

Risk: API keys stored locally or supplied through the environment could be exposed.

Mitigation: Protect local credentials and avoid sharing API keys in prompts or logs.

Risk: Prompts and any supplied files are sent to dLazy's cloud service.

Mitigation: Only submit content approved for the service.

Risk: The documented example returns PNG despite claims of SVG/vector output.

Mitigation: Check the returned MIME type and file contents before using the asset as a vector graphic.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI source (tooling, not skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON result with a generated asset URL; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation describes SVG/vector output, but its example reports a PNG image; verify the returned file type before treating it as a vector asset.]

## Skill Version(s):

1.3.20 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
