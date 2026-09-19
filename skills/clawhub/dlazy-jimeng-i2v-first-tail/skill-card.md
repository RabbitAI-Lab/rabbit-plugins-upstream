## Description:

Generate coherent transition videos using Jimeng's first and tail frame models from a prompt plus first-frame and last-frame images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Jimeng first/tail-frame image-to-video workflow from an agent or shell. It is intended for generating transition videos from user-supplied prompts and media inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and selected media files to dLazy cloud services for video generation.

Mitigation: Use only media and prompts that are acceptable to upload to dLazy, and review dLazy service terms before use.

Risk: Authentication can persist a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY or npx for less persistent local state when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: The documentation has inconsistent examples for firstFrame and lastFrame flags versus generic image flags.

Mitigation: Check `dlazy jimeng-i2v-first-tail -h` before execution and verify that first and last frame arguments are mapped correctly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, files, guidance]

**Output Format:** [CLI commands and JSON responses containing generated asset URLs or asynchronous task IDs; optional saved media files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and uploads selected prompts, parameters, and media files to dLazy cloud endpoints.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
