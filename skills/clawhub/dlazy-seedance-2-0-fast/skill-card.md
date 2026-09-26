## Description:

Fast version of ByteDance's Seedance 2.0 that generates videos faster with support for multi-modal references, first and last frames, and text-to-video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call the dLazy Seedance 2.0 Fast hosted video-generation service from an agent workflow, generating video from text prompts and optional image, video, audio, first-frame, or last-frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI can store an API key in the user's local configuration.

Mitigation: Use OS-user-restricted config permissions, prefer per-invocation DLAZY_API_KEY for temporary use, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Prompts and media paths supplied to the skill are sent to dLazy-hosted endpoints for generation.

Mitigation: Review prompts and referenced media before invocation, avoid sensitive inputs unless approved for the service, and use dry-run behavior to inspect payloads before calling the API.

Risk: The skill depends on a third-party CLI package and hosted service.

Mitigation: Confirm trust in the dLazy CLI package and service before installing or invoking it, and use the pinned @dlazy/cli@1.2.3 package declared by the artifact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, files, guidance]

**Output Format:** [Markdown instructions with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted file URLs, async task IDs, and optionally save generated assets to a local path.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
