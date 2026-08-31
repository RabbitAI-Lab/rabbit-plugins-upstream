## Description:

Video generation skill that automatically selects the best dLazy CLI video model for text-to-video, image-to-video, first/last-frame video, digital human, and lip-sync requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to select and run dLazy-hosted video generation models for prompts, images, video, and audio inputs. It supports creative video generation workflows including text-to-video, image animation, reference-guided video, digital human generation, lip sync, and segmentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media paths supplied by the user may be sent to dLazy cloud services for generation.

Mitigation: Review inputs before execution and avoid submitting sensitive media or prompts unless the user accepts dLazy cloud processing.

Risk: Local image, video, or audio files passed to generation commands may be uploaded to dLazy media storage.

Mitigation: Confirm intended files before running commands and use least-sensitive source assets for cloud generation workflows.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use account-scoped keys, prefer revocable credentials, and rotate or revoke keys from the dLazy dashboard when access is no longer needed.

Risk: The skill installs or invokes a pinned third-party npm CLI package.

Mitigation: Review the pinned package and source links before installation when supply-chain assurance is required.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs dLazy CLI commands that return JSON envelopes with generated media URLs hosted by files.dlazy.com.]

## Skill Version(s):

1.4.11 (source: ClawHub release evidence; artifact frontmatter reports 1.4.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
