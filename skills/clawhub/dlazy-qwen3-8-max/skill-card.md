## Description:

Uses dLazy's hosted Qwen 3.8 Max model for reasoning, code assistance, and analysis of text and images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users use this skill to generate answers, work through complex reasoning and coding tasks, and analyze text or images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to a third-party cloud service.

Mitigation: Review prompts and selected files for sensitive data before sending them to dLazy.

Risk: Authentication stores an API key in local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key in the dLazy dashboard when access should be removed.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [JSON response containing generated content; content format depends on the prompt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous task ID or saved result asset.]

## Skill Version(s):

1.2.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
