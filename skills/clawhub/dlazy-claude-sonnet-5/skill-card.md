## Description:

Uses the dLazy CLI to generate text with Claude Sonnet 5 from prompts and optional image or video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users invoke a hosted text-generation model for reasoning, coding, and writing tasks, optionally providing images or videos as context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI may introduce supply-chain exposure.

Mitigation: Review the package and source before installation, especially under strict supply-chain controls; use the documented pinned version.

Risk: Logging in saves a dLazy API key on the local device.

Mitigation: Use the per-invocation DLAZY_API_KEY option if you do not want a saved key, and rotate or revoke credentials when needed.

Risk: Prompts and selected local media files are sent to dLazy-hosted services.

Mitigation: Send only prompts and files you are comfortable sharing with the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Text or structured JSON, depending on the request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task ID or save a generated result to a file.]

## Skill Version(s):

1.2.34 (source: ClawHub release; artifact frontmatter lists 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
