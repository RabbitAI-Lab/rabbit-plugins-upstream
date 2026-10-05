## Description:

Generates text, answers questions, and supports reasoning through the dLazy-hosted Grok 4.2 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill for text generation, conversational questions, and reasoning through a hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad chat and text-generation triggers may cause unintended external API use.

Mitigation: Prefer explicit invocations and confirm before sending requests to dLazy.

Risk: Prompts, parameters, and referenced media files may be sent to dLazy.

Mitigation: Review inputs and avoid sending sensitive content without authorization.

Risk: Authentication can store an API key locally; installing the CLI runs third-party software.

Mitigation: Use a per-invocation environment variable if local key storage is undesirable, and review the pinned CLI before installation.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Text in a JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before the result is ready.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
