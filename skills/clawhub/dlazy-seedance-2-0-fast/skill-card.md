## Description:

Fast version of ByteDance's Seedance 2.0 that helps agents generate videos with text prompts, multi-modal references, first or last frames, and optional generated audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to ask an agent to run dLazy's Seedance 2.0 Fast video-generation workflow from prompts and optional image, video, or audio references. It is suited for cloud-hosted text-to-video, reference-guided video generation, and first-frame or last-frame video generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and selected local image, video, or audio files to dLazy's hosted API and media storage.

Mitigation: Avoid passing sensitive prompts or media unless sharing them with the dLazy service is acceptable for the user's use case.

Risk: The skill requires a dLazy API key that may be stored in the local CLI configuration or supplied through an environment variable.

Mitigation: Use normal secret-handling practices, avoid exposing the key in shared logs or prompts, and rotate or revoke the key if exposure is suspected.

Risk: Running the pinned dLazy npm CLI executes third-party tooling on the user's system.

Mitigation: Prefer the pinned npx invocation when a persistent global binary is not needed, and review the package source before installation in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result payloads that include generated media URLs or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can save generated media to a local path when requested, or return hosted output URLs from files.dlazy.com.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
