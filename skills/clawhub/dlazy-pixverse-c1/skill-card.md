## Description:

Helps agents generate PixVerse C1 videos from text prompts, images, first and last frames, or reference images through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to instruct an agent to generate short videos from prompts and optional image inputs, and to retrieve the resulting media links or files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media may be sent to dLazy's cloud service, and generated assets may be hosted there.

Mitigation: Confirm cloud processing is appropriate and share only media and prompts approved for upload.

Risk: An API key may be saved in local CLI configuration.

Mitigation: Protect the local configuration or provide the key per invocation, and rotate or revoke it if exposed.

Risk: Generation may consume paid credits and installing the CLI globally persists a local executable.

Mitigation: Check the cost estimate with dry-run before generation and use the pinned npx invocation if a persistent installation is unwanted.

## Reference(s):

- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Text with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses can include hosted video asset URLs or an asynchronous task ID; results can be saved locally.]

## Skill Version(s):

1.2.29 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
