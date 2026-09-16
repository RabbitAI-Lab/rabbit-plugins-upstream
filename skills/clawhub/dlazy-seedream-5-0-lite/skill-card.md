## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or transform images through the dLazy CLI using Doubao Seedream 5.0 Lite. It supports prompt-based generation, image references, resolution and aspect-ratio controls, asynchronous task polling, and optional local saving of generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party cloud API and uploads prompts, parameters, and selected media to dLazy endpoints.

Mitigation: Do not submit sensitive prompts or media unless dLazy's terms and your data-handling requirements allow it; use dry-run mode when you need to inspect the request payload before calling the API.

Risk: Authentication requires a dLazy API key that may be stored locally or supplied through an environment variable.

Mitigation: Avoid placing API keys in chat logs, store credentials through the CLI or per-invocation environment variables, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Global installation persists the dLazy CLI on the user's system.

Mitigation: Use the pinned npx invocation for on-demand execution if a persistent global CLI is not desired, and review the referenced package or source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON, Files]

**Output Format:** [Markdown guidance with CLI commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns generated image URLs, or a task identifier for asynchronous requests, and can save generated assets to a local path.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
