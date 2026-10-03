## Description:

Generates a short Jimeng video from a first-frame image and a text prompt through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a supplied first-frame image and prompt into a short generated video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be uploaded to dLazy, and generated outputs are hosted there.

Mitigation: Avoid submitting sensitive material without reviewing dLazy's service terms and data-handling practices.

Risk: Logging in can store an API key on the local machine.

Mitigation: Protect access to the user account and rotate or revoke the key if exposed.

Risk: Installing the third-party CLI globally leaves a persistent executable on the system.

Mitigation: Review the CLI source before installation; use the pinned on-demand npx command if a persistent installation is unnecessary.

## Reference(s):

- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown instructions with CLI examples and JSON result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned by URL; optional local download or asynchronous task tracking.]

## Skill Version(s):

1.3.24 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
