## Description:

This skill helps agents use the dLazy CLI to generate Kling v3 Omni videos from prompts and optional media inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run dLazy's hosted Kling v3 Omni video generation workflow from text prompts and optional image or video references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media paths provided to the skill may be uploaded to dLazy's hosted service.

Mitigation: Use the skill only with content approved for processing by dLazy, and avoid sending confidential media unless that service is approved for the data.

Risk: Authentication stores a dLazy API key in local CLI configuration when using the login flow.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill runs an external pinned CLI package through npm or npx.

Mitigation: Install or execute only the pinned package version declared by the skill and review the package source before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted file URLs, saved local assets, or asynchronous task identifiers from the dLazy CLI.]

## Skill Version(s):

1.3.10 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
