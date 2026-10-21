## Description:

Helps users generate logos, icons, and other design assets from text prompts through dLazy's Recraft V4 Vector CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to request generated logo, icon, and other design assets using text prompts and an aspect ratio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied files may be sent to dLazy's hosted service.

Mitigation: Avoid submitting confidential prompts or files unless sharing them with dLazy is approved.

Risk: Using the CLI requires trusting the installed third-party package.

Mitigation: Verify the pinned @dlazy/cli@1.2.3 package before installation.

Risk: The skill describes SVG output, but its sample result is a PNG image.

Mitigation: Confirm the actual output format before relying on vector or SVG properties.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Links]

**Output Format:** [Markdown with shell commands and generated asset links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can save the generated asset locally with --save.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
