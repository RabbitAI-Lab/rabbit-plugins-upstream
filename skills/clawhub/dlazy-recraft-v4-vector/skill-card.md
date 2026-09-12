## Description:

Text-to-vector model that outputs SVG results for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and external users use this skill to call the dLazy Recraft V4 Vector workflow from an agent and generate vector-style image assets from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supported file inputs may be sent to dLazy's hosted API and media storage.

Mitigation: Only submit prompts and files that are appropriate for the dLazy service and the user's organization policy.

Risk: The skill uses a dLazy API key for authentication.

Mitigation: Treat the API key as a credential and rotate or revoke it from the dLazy dashboard if exposure is suspected.

Risk: The workflow depends on installing or running the third-party @dlazy/cli package.

Mitigation: Review the linked CLI package or source before use in sensitive environments and prefer npx when a persistent global install is unnecessary.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted result URLs, save generated assets to a local path, or return an async task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
