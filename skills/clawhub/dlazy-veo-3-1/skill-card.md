## Description:

Generate high-quality cinematic effects videos with Google Veo 3.1, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to invoke the dLazy CLI for Google Veo 3.1 video generation, including prompt-only generation, reference-image generation, and video extension. It is intended for cloud-hosted generation workflows where selected prompts and media are sent to dLazy services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs the external dLazy npm CLI.

Mitigation: Use the pinned npx invocation when avoiding a persistent global install, and review the referenced source or package before use.

Risk: Prompts and selected image, video, or audio files are sent to dLazy API and file services.

Mitigation: Avoid sending sensitive media or prompts unless approved for the target workflow and account.

Risk: The workflow requires a dLazy API key stored in local configuration or supplied by environment variable.

Mitigation: Use revocable organization-scoped API keys and rotate or revoke keys when no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result objects containing generated media URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated media to a local path when the CLI is invoked with --save; asynchronous runs can return a generateId for later polling.]

## Skill Version(s):

1.3.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
