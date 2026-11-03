## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to clone a voice from reference audio and generate spoken audio for supplied text through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference audio and text are sent to dLazy's hosted service, and requests may incur usage charges.

Mitigation: Submit only audio and text you trust dLazy to process, review the dry-run cost estimate before generation, and use the documented login flow to store credentials locally instead of sharing API keys in chat.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio, JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON response containing generated audio URLs and task status, with shell command usage instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio is hosted by dLazy; asynchronous runs may return a task ID before outputs are ready.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
