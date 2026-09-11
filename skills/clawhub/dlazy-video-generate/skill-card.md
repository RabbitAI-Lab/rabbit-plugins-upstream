## Description:

Video generation skill that automatically selects the best dLazy CLI video model for text-to-video, image-to-video, frame-guided video, digital human, and lip-sync requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route video generation prompts and selected media inputs to the appropriate dLazy CLI model, including text-to-video, image animation, reference-guided generation, digital human video, and lip-sync workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, video, or audio files are sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only with content appropriate for dLazy's hosted service and avoid submitting sensitive media unless that processing is approved.

Risk: The skill depends on a pinned third-party npm CLI and API-key based authentication.

Mitigation: Use revocable API keys, prefer per-invocation credentials or npx for one-off use, and review the CLI source before installing in sensitive environments.

Risk: Generated media may fail because of authorization, account balance, server errors, missing local files, or service safety policy checks.

Mitigation: Check returned error codes, rotate or revoke credentials through the dLazy dashboard when needed, and verify local file paths before invocation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill selects dLazy CLI subcommands and may produce hosted video result URLs through the dLazy service.]

## Skill Version(s):

1.4.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
