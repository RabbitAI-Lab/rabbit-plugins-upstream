## Description:

Anthropic's latest Sonnet model for reasoning, code generation, long-horizon agentic work, and text generation with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to call dLazy's hosted Claude Sonnet 5 wrapper for text generation, coding help, reasoning, and multimodal prompt workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided image, video, or audio file paths are sent to dLazy's hosted service for processing.

Mitigation: Avoid sending sensitive data unless the service terms and data-handling posture are acceptable for the use case.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or npx when less persistent setup is preferred, and rotate or revoke keys when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [JSON response containing generated outputs, commonly consumed as text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt input plus user-selected image and video inputs; asynchronous calls may return a task identifier instead of immediate outputs.]

## Skill Version(s):

1.2.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
