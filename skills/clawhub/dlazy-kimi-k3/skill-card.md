## Description:

Moonshot AI thinking model with text, image, and video understanding, suited to complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call the dLazy Kimi K3 CLI for text generation, multimodal understanding, complex analysis, coding, and writing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and parameters are sent to the hosted dLazy API endpoint for inference.

Mitigation: Use the skill only with data approved for processing by the dLazy hosted service.

Risk: Local image, video, or audio paths provided to the CLI may be uploaded to dLazy media storage.

Mitigation: Pass only media files that are approved for upload to dLazy; use dry-run or path review before submitting sensitive files.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local key storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party npm CLI package and hosted service.

Mitigation: Review trust in the external dLazy CLI package and service before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON response from the dLazy CLI, with generated content nested in outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async calls may return a generateId and status instead of immediate outputs; saved assets may be downloaded when requested.]

## Skill Version(s):

1.2.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
