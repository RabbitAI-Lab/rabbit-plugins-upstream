## Description:

通义万相 2.7 视频模型，支持文生视频、首尾帧生视频以及参考图/视频生视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to ask an agent to run dLazy's Wan 2.7 video-generation CLI for text-to-video, first/last-frame video, and reference media workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a third-party dLazy cloud service and may send prompts, parameters, and referenced media to that service.

Mitigation: Use it only with prompts and media intended for dLazy processing; review dLazy service terms and organization policy before use.

Risk: Local API-key storage can expose credentials if the user's machine or config directory is compromised.

Mitigation: Keep the CLI config user-restricted, use per-invocation DLAZY_API_KEY in sensitive environments, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global npm install persists the dLazy CLI on the system.

Mitigation: Use the pinned npx invocation when a persistent global CLI install is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are hosted on files.dlazy.com; --no-wait returns an async task id and --save can download output assets.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
