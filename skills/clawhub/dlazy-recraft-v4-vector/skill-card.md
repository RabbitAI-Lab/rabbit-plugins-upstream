## Description:

Guides an agent to generate logos, icons, and other design assets from text prompts using dLazy's Recraft V4 Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other users can ask an agent to generate logos, icons, and scalable design assets from text prompts through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media files explicitly provided to the CLI are sent to dLazy's hosted service.

Mitigation: Review inputs before submission and avoid sharing sensitive prompts or files.

Risk: The third-party CLI can be installed globally, and login saves the API key in a local configuration file.

Mitigation: Use the pinned npx invocation to avoid a global install and pass DLAZY_API_KEY per invocation if local key storage is unwanted.

Risk: The skill describes SVG/vector output, but its example response identifies a PNG image.

Mitigation: Check the returned MIME type and asset format before relying on a scalable vector file.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [CLI commands and JSON responses with generated asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save a generated asset locally; the documented sample returns PNG despite the SVG description.]

## Skill Version(s):

1.3.26 (source: ClawHub release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
