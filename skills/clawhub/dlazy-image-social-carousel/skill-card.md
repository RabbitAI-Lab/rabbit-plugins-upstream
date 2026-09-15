## Description:

A structured workflow skill dedicated to social-media carousel design, using a single-confirmation and cover-first two-phase flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and design agents use this skill to plan and generate social-media carousel image sets through a staged workflow that confirms direction, generates a cover first, and then creates matching remaining slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded media, and generated result URLs are processed by dLazy cloud services.

Mitigation: Review the dLazy trust boundary before use, avoid sensitive media unless approved, and prefer the DLAZY_API_KEY environment variable when a persistent saved key is not desired.

Risk: The executable dLazy CLI is installed from npm and is not vendored in the skill artifact.

Mitigation: Review the CLI source or npm package before installation and use the documented pinned @dlazy/cli version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with confirmation tables, concise generation guidance, shell command examples, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses staged user confirmation before generation; generated media is returned through dLazy-hosted URLs.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
