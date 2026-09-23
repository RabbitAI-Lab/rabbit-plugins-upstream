## Description:

Happy Horse 1.0 is a dLazy video-generation skill for text-to-video, first-frame-to-video, reference-to-video, and video editing, routing each mode to the matching sub-model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Happy Horse 1.0 model from an agent workflow and generate or edit video from prompts, images, or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, video, or audio files may be sent to dLazy's hosted service for generation.

Mitigation: Review inputs for sensitive content before use and apply the organization's cloud-service data handling policy.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation environment variables when appropriate, keep local config permissions restricted, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: A global CLI install persists a third-party executable on the user's system.

Mitigation: Use the pinned npx invocation when a temporary execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown command guidance with JSON CLI responses and optional downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns hosted output URLs by default; --save can download the generated asset locally, and --no-wait returns an asynchronous task identifier.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
