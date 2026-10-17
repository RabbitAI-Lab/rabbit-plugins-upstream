## Description:

Generates detailed vector illustrations and production-ready SVG assets from text prompts through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to generate vector artwork and detailed illustrations from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to the hosted dLazy service.

Mitigation: Avoid submitting sensitive prompts or files unless sharing them with dLazy is acceptable.

Risk: Login can store an API key on the local device.

Mitigation: Use DLAZY_API_KEY for per-run authentication when a saved key is not wanted.

Risk: The skill depends on an external npm CLI.

Mitigation: Review the pinned npm package before installation if supply-chain provenance matters.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Text or Markdown with commands and generated asset links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include a hosted asset URL or a locally saved file.]

## Skill Version(s):

1.3.29 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
