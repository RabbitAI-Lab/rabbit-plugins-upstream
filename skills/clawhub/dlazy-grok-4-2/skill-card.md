## Description:

Efficient text generation, dialogue QA, and logical reasoning using Grok 4.2 text model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can use this skill to generate text, answer questions, and reason through prompts with Grok 4.2 through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports broad activation triggers and a mismatch between the stated text-generation purpose and the CLI login/setup behavior it inspected. The external package's behavior remains unverified, and local references are missing; the suspicious verdict is not a finding of malicious intent.

Mitigation: Before use, review the activation triggers and inspect the CLI installation, login, setup, and package behavior; obtain the missing references and treat the verdict as a review signal.

## Reference(s):

- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Generated text returned by the CLI, with results in a JSON envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts are sent to dLazy's hosted API; use requires a dLazy API key.]

## Skill Version(s):

1.3.38 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
