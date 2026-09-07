## Description:

Image super-resolution tool that enhances image clarity and details and returns an enhanced image URL for low-resolution asset restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to upscale low-resolution images through the dLazy CLI and receive a hosted enhanced image URL or saved result file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images passed to the CLI may be uploaded to dLazy-hosted storage for processing.

Mitigation: Do not submit private or sensitive images unless the user accepts that upload and hosted processing.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use a sandboxed account or per-invocation environment variable where appropriate, and rotate or revoke the key if exposure is suspected.

Risk: Global installation of the third-party CLI can persist executable code on the system.

Mitigation: Prefer pinned npx use or review the CLI source and npm package before installing globally in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted image URLs, asynchronous task identifiers, or save the enhanced image to a local path when requested.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
