## Description:

Chat with the dLazy sandbox agent as a project-scoped assistant for multi-turn work that can discover skills and projects with dlazy skills list and dlazy projects list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to start or continue project-scoped conversations with the dLazy hosted sandbox agent, including selecting a skill or template, attaching files, and managing chat sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected options, and chat context are sent to dLazy's hosted service.

Mitigation: Use the skill only when the user or organization is comfortable sharing that content with dLazy's service.

Risk: Files attached with --files are uploaded to dLazy media storage.

Mitigation: Attach only intended files and avoid uploading sensitive files unless service use has been approved.

Risk: The skill requires a dLazy API key that may be stored in the local CLI configuration.

Mitigation: Protect the local config file, use per-invocation environment variables when preferred, and rotate or revoke the key when it is no longer needed.

Risk: Installing the CLI globally persists a local binary.

Mitigation: Review the pinned @dlazy/cli package before installation or use the npx command for on-demand execution.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or terminal text with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream responses from the hosted dLazy service and may reference uploaded files when the user attaches local files.]

## Skill Version(s):

1.2.22 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
