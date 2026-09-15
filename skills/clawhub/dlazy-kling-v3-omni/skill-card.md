## Description:

Generates dynamic videos with Kling v3 Omni from multimodal inputs such as prompts and images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy CLI for Kling v3 Omni video generation from text prompts and media references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced media are sent to dLazy hosted services for generation.

Mitigation: Only submit prompts and media that are appropriate to share with dLazy and the configured organization.

Risk: Installing or running @dlazy/cli introduces ordinary third-party npm supply-chain risk.

Mitigation: Use the pinned package version, prefer npx for non-persistent use in sensitive environments, and review the linked package or source before installation.

Risk: The dLazy API key is a service credential stored locally or supplied through DLAZY_API_KEY.

Mitigation: Protect the key as a secret and rotate or revoke it from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown with shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, asynchronous task identifiers, or saved local media files when requested.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
