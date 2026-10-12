## Description:

Helps agents turn a website URL into a promotional video, social ad, or product demo through dLazy's website-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn a website or landing page into a promotional video, social ad, or product demo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to the external dLazy service.

Mitigation: Do not include confidential information unless the service is approved for it.

Risk: Files attached to a request are uploaded to dLazy media storage.

Mitigation: Review and explicitly approve attachments before sending them.

Risk: The workflow requires a dLazy API key and installation of the pinned CLI package.

Mitigation: Keep the key private and review the pinned package before installation.

## Reference(s):

- [dLazy CLI source and installation guidance](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Terminal text or Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports follow-up turns in a saved project.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
