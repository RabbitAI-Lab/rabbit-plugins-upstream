## Description:

Schedule and manage social posts with the openquok CLI: authenticate, upload media, create drafts and scheduled posts, configure internal plugs, and read channel analytics for integrations in an OpenQuok workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratimon](https://clawhub.ai/user/ratimon)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate the OpenQuok CLI for connected social channels: authentication, integration discovery, media upload, post drafting or scheduling, plug configuration, and analytics review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OpenQuok commands can publish, delete, schedule, or automate content on connected social accounts.

Mitigation: Review generated commands before execution, use drafts for human review when appropriate, and require confirmation before publishing, deleting, or enabling auto-reply or repost plugs.

Risk: The skill depends on OpenQuok credentials or tokens that affect real workspaces.

Mitigation: Use the documented device flow or programmatic tokens carefully, avoid exposing secrets, and revoke tokens when access is no longer needed.

## Reference(s):

- [OpenQuok Core on ClawHub](https://clawhub.ai/ratimon/skills/openquok-core)
- [OpenQuok CLI package](https://www.npmjs.com/package/@openquok/auto-cli)
- [OpenQuok](https://www.openquok.com/)
- [Command reference](resources/command-reference.md)
- [Provider settings](resources/provider-settings.md)
- [Post examples](resources/examples/EXAMPLES.md)
- [Plugs](resources/plugs.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the openquok CLI on PATH and valid OpenQuok workspace credentials for API operations.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
