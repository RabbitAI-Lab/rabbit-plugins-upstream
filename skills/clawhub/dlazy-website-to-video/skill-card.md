## Description:

Helps turn a website URL into a promotional video, social ad, or product demo using dLazy's website-to-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to request website-based promotional videos, social ads, and product demos through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and website details are sent to dLazy's hosted service.

Mitigation: Avoid including sensitive details unless you intend to share them with dLazy.

Risk: Files supplied with --files are uploaded to dLazy.

Mitigation: Review attachments and exclude sensitive files before uploading.

Risk: The CLI can store an API key locally.

Mitigation: Protect your local configuration and rotate or revoke the key in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown and CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include video project status or links from the hosted service.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
