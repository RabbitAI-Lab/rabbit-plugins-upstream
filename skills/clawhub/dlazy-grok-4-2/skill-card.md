## Description:

Uses dLazy's hosted Grok 4.2 text model for text generation, dialogue question answering, and logical reasoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call dLazy's hosted Grok 4.2 model through the dLazy CLI for prompt-based text generation, chat-style QA, and reasoning tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly referenced local media files may be sent to dLazy hosted endpoints.

Mitigation: Use explicit invocation, avoid sensitive prompts or local files, and review what inputs will be sent before running the CLI.

Risk: The security summary flags broad triggers and remote file or media handling that could route prompts or files to dLazy unexpectedly.

Mitigation: Prefer explicit command use, use dry-run when practical, and confirm referenced files before invoking the hosted service.

Risk: Use requires installing or running @dlazy/cli and storing or passing a dLazy API key.

Mitigation: Use the pinned @dlazy/cli version from the artifact, review the package before global installation, and rely on revocable API keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON API response or Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the dLazy CLI, npm or npx, and a dLazy API key; supports dry-run, asynchronous task IDs, and timeout controls.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
