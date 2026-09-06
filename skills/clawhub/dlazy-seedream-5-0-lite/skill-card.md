## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Seedream 5.0 Lite image generation service from an agent workflow. It supports prompt-only generation and image-guided generation, with optional local saving of generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image paths may be sent to dLazy's hosted API, and referenced media may be uploaded to files.dlazy.com.

Mitigation: Use the skill only with content suitable for dLazy's hosted service, and avoid passing sensitive prompts or local files unless that data transfer is acceptable.

Risk: Authentication can store a dLazy API key in ~/.dlazy/config.json.

Mitigation: Use per-invocation DLAZY_API_KEY when persistent local key storage is not desired, and rotate or revoke organization keys from the dLazy dashboard when needed.

Risk: Successful image generation calls may consume dLazy credits.

Mitigation: Use dry-run or cost-estimation behavior where appropriate and confirm the organization has sufficient credits before running large jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned through dLazy-hosted result URLs, and asynchronous runs may return a task identifier for polling.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
