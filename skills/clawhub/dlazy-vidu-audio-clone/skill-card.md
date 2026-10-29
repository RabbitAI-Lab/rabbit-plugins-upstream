## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate spoken audio for supplied text in a Vidu voice, using a reference audio clip when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference audio and text are sent to dLazy hosted services, and local reference audio may be uploaded to its media storage.

Mitigation: Submit only audio and text approved for cloud processing, and follow your organization’s data-handling policies.

Risk: The dLazy organization API key is stored in the local CLI configuration.

Mitigation: Protect the local key; rotate or revoke it if it may have been exposed.

Risk: Voice cloning may use a person’s voice without permission.

Mitigation: Use reference voices only with the voice owner’s permission.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio returned as a hosted URL in a JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when run without waiting.]

## Skill Version(s):

1.3.35 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
