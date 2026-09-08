## Description:

Generate dynamic videos from a first-frame image and prompt using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Jimeng image-to-video CLI, providing a prompt and first-frame image to generate a hosted video result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys are required for use and may be exposed through local configuration or the execution environment.

Mitigation: Use the documented dLazy authentication flow or per-run DLAZY_API_KEY handling, restrict local config access, and rotate the key if compromise is suspected.

Risk: Input media files provided to the CLI are uploaded to dLazy-hosted services for processing.

Mitigation: Provide only media files intended for upload and review the dLazy service terms before processing sensitive content.

Risk: The executable component is installed or run through the @dlazy/cli npm package.

Mitigation: Review the linked source or npm package before installation, and prefer npx or a sandbox for one-off use.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash examples and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task IDs when --no-wait is used; --save can download generated media to a local path.]

## Skill Version(s):

1.3.14 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
