## Description:

Helps agents generate graphics with Recraft V4 Vector through dLazy, although the documented result is PNG rather than editable SVG.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to request logos, icons, and other graphics from dLazy's hosted generation service. Check the delivered format before relying on an editable vector asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill advertises SVG/vector output, but its example result is PNG.

Mitigation: Check the actual output format before using the asset where editable or scalable SVG is required.

Risk: Using the service requires a dLazy API key and sends prompts and explicitly supplied local media to dLazy.

Mitigation: Only submit prompts and files you are comfortable sharing with dLazy, and protect your API key.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with CLI examples and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented generated asset is hosted as image/png; editable SVG output is not established.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
