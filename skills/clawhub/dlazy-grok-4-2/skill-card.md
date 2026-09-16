## Description:

Uses the dLazy CLI to access a hosted Grok 4.2 text model for text generation, dialogue Q&A, and logical reasoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent call dLazy's hosted Grok 4.2 service for prompt-based text generation, chat-style Q&A, and reasoning tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and provided media files may be sent to dLazy endpoints.

Mitigation: Use the skill only when external dLazy processing is intended, avoid sensitive prompts and local file paths, and review payloads before execution.

Risk: API keys may be stored in the local dLazy CLI config or supplied through the environment.

Mitigation: Use a revocable API key or per-run DLAZY_API_KEY where possible, rotate or revoke keys when exposure is suspected, and prefer isolated environments.

Risk: Broad triggers and third-party CLI execution could cause unintended external use.

Mitigation: Invoke this skill only for explicit dLazy Grok 4.2 requests and review commands before running them.

Risk: The artifact describes text generation but shows an image-style output example.

Mitigation: Confirm the expected response shape and model behavior before relying on output in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [JSON response from the dLazy CLI containing generated output or async task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports dry-run mode and async task polling.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
