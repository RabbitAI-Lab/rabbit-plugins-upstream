## Description:

Helps turn raster images into scalable vector artwork through the dLazy vectorization service and returns a result URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to request vector-style versions of logos, icons, and flat illustrations from PNG or JPG images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image files are uploaded to the third-party dLazy service.

Mitigation: Review dLazy's retention and access practices before sending private, proprietary, personal, or regulated media.

Risk: The CLI uses a dLazy API key and may save it in local configuration.

Mitigation: Treat the key as a secret and prefer DLAZY_API_KEY on shared or automated systems.

Risk: The skill advertises SVG vectorization, but its example result is PNG.

Mitigation: Check the returned file type and confirm SVG availability before relying on vector output.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with a result URL or JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the returned asset locally; example response is PNG, so SVG output needs verification.]

## Skill Version(s):

1.2.25 (source: server-resolved ClawHub release; artifact frontmatter says 1.2.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
