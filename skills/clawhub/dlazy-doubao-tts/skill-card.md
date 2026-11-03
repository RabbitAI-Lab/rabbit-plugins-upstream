## Description:

Synthesize text into natural and fluent speech using Doubao TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn supplied text into Chinese or English speech with Doubao TTS through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text and generation parameters are sent to the dLazy hosted API; API credentials are stored in the local CLI configuration unless supplied per invocation.

Mitigation: Submit only approved text, protect the local configuration file, and rotate or revoke exposed organization keys.

Risk: The skill relies on an external CLI package that was not audited in the security review.

Mitigation: Review the pinned @dlazy/cli 1.2.3 package before installation; use the documented on-demand npx invocation when appropriate.

## Reference(s):

- [dLazy CLI repository (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON metadata]

**Output Format:** [Generated speech audio, with output URLs and generation status in a JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports synchronous results or an asynchronous task identifier.]

## Skill Version(s):

1.3.36 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
