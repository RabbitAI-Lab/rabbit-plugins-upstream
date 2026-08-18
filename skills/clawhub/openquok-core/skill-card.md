## Description:

Schedule and manage social posts with the openquok CLI: authenticate, upload media, create drafts and scheduled posts, configure internal plugs, and read channel analytics for integrations in an OpenQuok workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratimon](https://clawhub.ai/user/ratimon)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and social media teams use this skill to have an agent operate the OpenQuok CLI for authenticated social channel setup, media upload, post drafting, scheduling, analytics, and supported engagement automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to perform real actions on connected social accounts, including creating, scheduling, updating, or deleting posts and plug rules.

Mitigation: Use drafts or a test workspace first, and review commands before execution in production workspaces.

Risk: Incorrect integration IDs, schedule values, media references, or acting plug accounts can publish to the wrong channel or at the wrong time.

Mitigation: Verify integration IDs, scheduledAt/status values, uploaded media IDs and paths, and acting accounts before create, upsert, or delete commands.

Risk: OpenQuok credentials and scheduled automations may persist outside the skill after the agent session ends.

Mitigation: Confirm authentication state, use scoped programmatic tokens where appropriate, and log out or rotate credentials when access should end.

## Reference(s):

- [OpenQuok CLI package](https://www.npmjs.com/package/@openquok/auto-cli)
- [OpenQuok website](https://www.openquok.com/)
- [Command reference](resources/command-reference.md)
- [Provider settings](resources/provider-settings.md)
- [Workflow recipes](resources/patterns.md)
- [Plugs](resources/plugs.md)
- [Threads publish behavior](resources/threads-publish.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the global openquok CLI on PATH and authenticated OpenQuok credentials for API actions.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
