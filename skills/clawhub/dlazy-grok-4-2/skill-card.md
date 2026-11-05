## Description:

Efficient text generation, dialogue QA, and logical reasoning using Grok 4.2 text model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to generate text, answer questions, and perform logical reasoning with the Grok 4.2 model through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and submitted media are sent to dLazy's hosted services, and use may incur charges.

Mitigation: Invoke the skill when you intend to use paid dLazy processing, and submit only content you approve for external processing.

Risk: The API key persists in local CLI configuration; the published executable and hosted service were not audited.

Mitigation: Review the pinned CLI before installation, protect the local configuration, and rotate or revoke the key if exposed.

## Reference(s):

- [dLazy CLI source code](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Generated model output in the CLI's JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task identifier.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
