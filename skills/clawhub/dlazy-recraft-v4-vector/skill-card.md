## Description:

Helps agents generate vector-style logos, icons, and other scalable design assets from text prompts through dLazy's Recraft V4 Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other users can ask an agent to create logos, icons, and scalable design assets from text prompts using the dLazy image-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected input files, and generated outputs are handled by dLazy's hosted service.

Mitigation: Review data-sharing requirements before sending sensitive prompts or files.

Risk: Using the skill requires installing a third-party CLI and authenticating with an API key.

Mitigation: Review the pinned CLI before installation; protect the key and rotate or revoke it if needed.

Risk: The documented output format is inconsistent: SVG is described, but the example response is PNG.

Mitigation: Check the returned MIME type and file format before using the asset as a vector graphic.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns generated asset URLs or downloaded files; documentation describes SVG output, but its example shows a PNG result.]

## Skill Version(s):

1.3.23 (source: server release metadata; artifact frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
