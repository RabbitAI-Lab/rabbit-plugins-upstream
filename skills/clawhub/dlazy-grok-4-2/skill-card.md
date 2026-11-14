## Description:

Efficient text generation, dialogue QA, and logical reasoning using Grok 4.2 text model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can request text generation, question answering, and logical reasoning through the dLazy hosted service using Grok 4.2.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanners flag broad trigger phrases that could cause the skill to be selected without a clear request for this provider.

Mitigation: Invoke it only when the user explicitly requests Grok 4.2 through dLazy.

Risk: The security review reports a mismatch between the advertised Grok 4.2 text features and the visible CLI login and external package commands; package behavior and some referenced material were not fully assessed.

Mitigation: Avoid installation until the publisher clarifies the mismatch and narrows the triggers; review the CLI and package before authenticating or using them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy website](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Generated text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are generated through the hosted dLazy service.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
