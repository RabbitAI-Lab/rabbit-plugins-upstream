## Description:

Generates vector-style design assets from text prompts for logos, icons, and scalable graphics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other users can generate logos, icons, and scalable design assets from text prompts through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any referenced local media are sent to the dLazy service.

Mitigation: Review what will be sent before submitting sensitive prompts or local files.

Risk: Installing the CLI or saving an API key creates local software and credential exposure.

Mitigation: Review the CLI source and package before installation; prefer on-demand execution and a per-invocation API key if persistent installation or credential storage is undesirable.

Risk: The returned image may not be SVG despite the skill description.

Mitigation: Verify the returned MIME type before using the asset as an SVG.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI source (listed in release metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Generated asset links]

**Output Format:** [JSON result with hosted asset URLs and MIME types]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Check the returned MIME type before treating an asset as SVG; asynchronous requests return a task ID until completion.]

## Skill Version(s):

1.3.29 (source: ClawHub release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
