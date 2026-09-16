## Description:

Video generation skill that selects an appropriate dLazy CLI video model for text-to-video, image-to-video, frame-constrained video, digital-human, lip-sync, and related video generation requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent choose and run the right dLazy video-generation command for prompts, images, videos, audio, first/last frames, digital-human clips, lip-sync tasks, and segmentation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the npm-distributed dLazy CLI and depends on third-party hosted API endpoints.

Mitigation: Use the pinned install or on-demand npx command, and review the linked CLI source before installing when supply-chain risk matters.

Risk: Authentication can store a dLazy API key in the local user configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY for temporary use, and rotate or revoke saved keys when access is no longer needed.

Risk: Prompts and user-provided image, video, or audio files are uploaded to dLazy-hosted services for generation.

Mitigation: Avoid sending sensitive media or prompts unless the user accepts dLazy's service handling for the request.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash commands and JSON result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the npm-distributed dLazy CLI and may return hosted media URLs in JSON envelopes.]

## Skill Version(s):

1.4.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
