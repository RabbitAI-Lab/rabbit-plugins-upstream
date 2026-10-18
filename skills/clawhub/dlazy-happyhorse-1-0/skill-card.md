## Description:

Guides agents in using dLazy's Happy Horse 1.0 CLI for text-to-video, first-frame-to-video, reference-to-video, and video editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent through generating or editing videos with the dLazy Happy Horse 1.0 service from text prompts, images, or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service.

Mitigation: Review prompts and media for sensitive content before submission.

Risk: Logging in can save a dLazy API key locally.

Mitigation: Protect the local CLI configuration and rotate or revoke the key if exposed.

Risk: Using the CLI installs or runs a third-party npm package.

Mitigation: Review the pinned @dlazy/cli package and source before use; choose npx to avoid a global installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses can include generated media URLs or asynchronous task IDs; an optional save path downloads the result.]

## Skill Version(s):

1.3.30 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
