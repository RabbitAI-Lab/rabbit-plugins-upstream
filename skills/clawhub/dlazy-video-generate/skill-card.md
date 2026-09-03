## Description:

Video generation skill that helps an agent select and run an appropriate dLazy CLI video model for text-to-video, image-to-video, first/last-frame video, digital human, lip-sync, and related media workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to choose a suitable dLazy CLI video model, inspect its parameters, and execute video-generation or media-processing commands. It supports workflows such as text-to-video, image animation, first/last-frame generation, digital human video, lip sync, segmentation, and command chaining.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and media files passed to the CLI are sent to the dLazy cloud API and media storage.

Mitigation: Use only content appropriate for processing by dLazy, and review provider terms and data-handling expectations before use.

Risk: Authentication stores or uses a dLazy API key on the local system.

Mitigation: Protect the local CLI configuration, prefer scoped keys where available, and rotate or revoke keys from the dLazy dashboard when access should change.

Risk: The skill installs or runs a pinned third-party npm CLI.

Mitigation: Review the pinned npm package or source before installation and use it only in environments approved for third-party command-line tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with inline bash commands and dLazy CLI JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The executed CLI may return hosted media URLs in a JSON envelope.]

## Skill Version(s):

1.4.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
