## Description:

Versatile video generation with Kling v3 Omni; supports multi-modal inputs such as prompts and images to generate dynamic videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to invoke the dLazy CLI for Kling v3 Omni video generation from text prompts and optional image or video references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced media are sent to dLazy cloud services for generation.

Mitigation: Avoid submitting private or sensitive prompts and media unless the dLazy service terms and cloud workflow are acceptable for the use case.

Risk: The skill relies on API credentials for a third-party service.

Mitigation: Use scoped dLazy API keys, rotate or revoke them through the dLazy dashboard when needed, and prefer DLAZY_API_KEY or npx when avoiding persistent global configuration.

Risk: Installing a pinned third-party CLI introduces dependency and supply-chain exposure.

Mitigation: Review the pinned @dlazy/cli package and source before installation, or run the pinned package with npx for on-demand use.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI may return hosted media URLs, asynchronous task identifiers, or save generated assets to a local path when requested.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
