## Description:

Searches Pixabay Music through the dLazy CLI and returns royalty-free audio track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to find royalty-free background music candidates, usually with short English style keywords and optional duration limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party cloud CLI and service that may receive user queries, parameters, and local paths passed to it.

Mitigation: Use the skill only with trusted dLazy credentials and avoid passing local paths or save destinations unless the user explicitly wants that behavior.

Risk: The CLI stores an API key locally when authenticated.

Mitigation: Prefer per-invocation credentials or isolated execution when possible, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: The security summary notes contradictory parameters and broader cloud-generation behavior in the instructions.

Mitigation: Use the documented `dlazy search_audio --query` workflow and review command arguments before execution.

Risk: A global npm install increases persistence and trust requirements for the dLazy CLI.

Mitigation: Prefer the pinned `npx @dlazy/cli@1.2.3` invocation or an isolated container-style run over a privileged global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing search result metadata and track URLs; asynchronous calls can return a generateId for later status polling.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
