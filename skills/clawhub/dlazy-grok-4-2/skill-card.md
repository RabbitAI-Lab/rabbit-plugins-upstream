## Description:

Uses Grok 4.2 for text generation, dialogue question answering, and logical reasoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can submit prompts to generate text, answer questions, and receive logical reasoning through Grok 4.2.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media provided to the CLI may be sent to dLazy services, and broad triggers may route unrelated requests to the service.

Mitigation: Use the skill only when dLazy processing is intended, and avoid sending sensitive prompts or media until the service's data handling is understood.

Risk: ClawScan reports a suspicious purpose-to-command mismatch and limited visibility into the CLI implementation; the partial scan does not establish malicious intent.

Mitigation: Review the CLI release and its behavior before installation, and proceed only if it matches the intended text-generation use.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Generated text returned through the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task identifier for later status checks.]

## Skill Version(s):

1.3.43 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
