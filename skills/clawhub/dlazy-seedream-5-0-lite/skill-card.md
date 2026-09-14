## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or transform images through dLazy's hosted Doubao Seedream 5.0 Lite CLI/API, optionally saving generated image files locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image inputs are sent to dLazy's hosted service for inference and media handling.

Mitigation: Only pass prompts and files that are appropriate to upload to dLazy's service, and use revocable organization-scoped API keys.

Risk: Using the global install persists a third-party CLI on the local system.

Mitigation: Prefer npx or another isolated execution method when practical, and review the referenced @dlazy/cli package before global installation.

Risk: The skill depends on dLazy account credentials, service availability, and account credits.

Mitigation: Confirm authentication and credits before use, and use dry-run or async polling modes where appropriate for the workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated image URLs, plus optional downloaded image files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and referenced local files are sent to dLazy cloud endpoints; async runs can return a generateId for polling.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
