## Description:

Efficient text generation, dialogue QA, and logical reasoning using the Grok 4.2 text model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to generate text, answer questions, and perform logical reasoning with Grok 4.2 through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad chat triggers could send routine prompts to dLazy and consume credits without a clear provider choice.

Mitigation: Enable the skill only for explicit Grok or dLazy requests; confirm before sending sensitive prompts or incurring paid API use.

Risk: Logging in stores an API key in the local CLI configuration.

Mitigation: Use a trusted device and account, and rotate or revoke the key if it may have been exposed.

Risk: The text-generation description conflicts with an example showing image output.

Mitigation: Resolve the output-type discrepancy before relying on the skill for a specific media type.

## Reference(s):

- [CLI project link from skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON response envelope containing generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The supplied example shows an image output despite the text-generation description; confirm supported output types before relying on them.]

## Skill Version(s):

1.3.35 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
