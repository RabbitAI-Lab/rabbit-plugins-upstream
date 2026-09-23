## Description:

Generates production-grade vector-style assets and detailed illustrations from text prompts through the dLazy Recraft V4 Pro Vector cloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and content teams use this skill to ask an agent to run the dLazy CLI, generate vector/image assets from prompts, optionally save results locally, and handle asynchronous generation status or common authentication and balance errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and any local files passed to media fields may be sent to the third-party dLazy cloud service.

Mitigation: Only provide content appropriate for upload to dLazy and avoid passing sensitive files unless the user has approved that cloud processing.

Risk: Authentication can store a dLazy API key in a local CLI configuration file.

Mitigation: Use per-invocation DLAZY_API_KEY or npx execution when less local persistence is preferred, and rotate or revoke organization keys when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON responses containing generated image URLs or asynchronous task identifiers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets may be saved locally with --save; otherwise result URLs are hosted by files.dlazy.com. Async mode returns a generateId for later polling.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
