## Description:

Turns a webpage URL into a promotional, social ad, or product demo video with branding, storyboard, and voiceover.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn website links into promotional videos, social ads, or product demos through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments may be sent to dLazy's hosted service.

Mitigation: Only submit prompts and files you intend to share with dLazy.

Risk: Login saves a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key if compromised.

Risk: Installing a third-party CLI introduces software supply-chain exposure.

Mitigation: Review the linked CLI source and package before installing; use the pinned npx option if a persistent global installation is undesirable.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Video]

**Output Format:** [Text responses and generated video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the website-to-video workflow; a dLazy account and API key are required.]

## Skill Version(s):

1.0.21 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
