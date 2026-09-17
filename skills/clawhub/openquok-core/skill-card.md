## Description:

Schedule and manage social posts with the openquok CLI: authenticate, upload media, create drafts and scheduled posts, configure internal plugs, and read channel analytics for integrations in an OpenQuok workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratimon](https://clawhub.ai/user/ratimon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and social media teams use this skill to guide agents through OpenQuok CLI workflows for creating, scheduling, rescheduling, publishing, and analyzing posts across connected social channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Always-on session bootstrap can run OpenQuok version, auth, and workspace checks before the user has asked for an OpenQuok task, potentially disclosing workspace metadata.

Mitigation: Review before installing and prefer a version that gates bootstrap and workspace-discovery commands behind explicit user intent.

Risk: The skill can create, reschedule, delete, publish, and automate engagement on connected social accounts.

Mitigation: Use authenticated accounts with appropriate permissions, review generated commands before execution, and keep destructive or publishing actions subject to explicit user confirmation.

Risk: Uploaded media may need to be exposed through public URLs so social platforms can fetch it.

Mitigation: Avoid uploading sensitive media and verify that only intended assets are published or made publicly reachable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ratimon/skills/openquok-core)
- [OpenQuok CLI package](https://www.npmjs.com/package/@openquok/auto-cli)
- [OpenQuok website](https://www.openquok.com/)
- [Command reference](resources/command-reference.md)
- [Provider settings](resources/provider-settings.md)
- [Posting patterns](resources/patterns.md)
- [Plugs](resources/plugs.md)
- [Threads publish behavior](resources/threads-publish.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the global openquok CLI on PATH and valid OpenQuok credentials for API-backed commands.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
