## Description:

Efficient text generation, dialogue QA, and logical reasoning using Grok 4.2 text model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's hosted Grok 4.2 API for text generation, dialogue question answering, chat, and logical reasoning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and parameters are sent to the dLazy hosted API, so sensitive content could leave the local environment.

Mitigation: Use explicit invocations, avoid sensitive prompts, and confirm hosted SaaS processing is acceptable for the use case.

Risk: The artifact describes media-file upload behavior even though the release is positioned as a text generation skill.

Mitigation: Avoid passing local file paths unless file upload is intentional, and review commands before execution.

Risk: A stored dLazy API key may be exposed through local configuration or environment handling.

Mitigation: Prefer isolated or npx execution where appropriate and rotate the dLazy API key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI source code](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [CLI response, typically text or JSON returned by the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; asynchronous calls may return a task identifier before final output.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
