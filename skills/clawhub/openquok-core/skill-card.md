## Description:

Schedule and manage social posts with the openquok CLI: authenticate, upload media, create drafts and scheduled posts, configure internal plugs, and read channel analytics for integrations in an OpenQuok workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratimon](https://clawhub.ai/user/ratimon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and social media teams use this skill to guide an agent through authenticated OpenQuok CLI workflows for publishing, scheduling, draft review, media upload, plug automation, and analytics across connected social integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically run OpenQuok version, authentication, and workspace checks at the start of a new session.

Mitigation: Review the session-opening behavior before installation and ensure the host policy allows these checks before user-visible interaction.

Risk: The skill can guide commands that publish, schedule, upload media, or configure cross-account and global plug automation for live social accounts.

Mitigation: Confirm integration IDs, schedules, media assets, plug rules, and draft status before running openquok commands; use drafts and review notes when the final post needs human approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ratimon/skills/openquok-core)
- [OpenQuok CLI package](https://www.npmjs.com/package/@openquok/auto-cli)
- [OpenQuok web app](https://www.openquok.com/)
- [OpenQuok CLI command reference](resources/command-reference.md)
- [Provider settings](resources/provider-settings.md)
- [Workflow recipes](resources/patterns.md)
- [Plugs reference](resources/plugs.md)
- [JSON post examples](resources/examples/EXAMPLES.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with openquok CLI commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate authenticated OpenQuok CLI checks and guide live social posting, scheduling, uploads, plugs, and analytics workflows.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
