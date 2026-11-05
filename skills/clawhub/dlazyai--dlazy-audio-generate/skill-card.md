## Description:

Automatically selects a suitable dLazy CLI audio or text-to-speech model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate speech, dialogue, music, and sound effects from prompts by choosing a suitable dLazy audio model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's cloud service for generation.

Mitigation: Only submit content you are comfortable uploading.

Risk: The CLI saves an organization API key in local configuration.

Mitigation: Protect the saved key and rotate or revoke it from the organization dashboard if needed.

## Reference(s):

- [dLazy CLI project page (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, Text, JSON]

**Output Format:** [Generated audio hosted at a URL, with JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts and selected media are sent to the dLazy cloud service; generated media is hosted by dLazy.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
