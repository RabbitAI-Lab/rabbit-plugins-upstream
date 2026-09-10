## Description:

A ClawHub skill that invokes dLazy's hosted Qwen 3.8 Max model for text generation, complex reasoning, code engineering, long-context analysis, and image-grounded prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send prompts and optional images to dLazy's hosted Qwen model through the dLazy CLI and receive generated text or JSON-formatted results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media files supplied to the skill are sent to dLazy's hosted API and media storage.

Mitigation: Review data sensitivity before use and avoid sending content that should not leave the local environment.

Risk: Authentication stores a dLazy API key in local CLI configuration unless a per-invocation environment variable is used.

Mitigation: Use the documented login or auth flow, protect the local config file, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global CLI install persists the dLazy command on the system.

Mitigation: Use the pinned npx invocation when a temporary, non-global CLI execution is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return JSON outputs or asynchronous task identifiers; optional local media paths may be uploaded by the CLI for model input.]

## Skill Version(s):

1.2.12 (source: server release metadata; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
