## Description:

Schedule and manage social posts with the openquok CLI, including authentication, media uploads, drafts, scheduled posts, internal plugs, and channel analytics for integrations in an OpenQuok workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratimon](https://clawhub.ai/user/ratimon)

### License/Terms of Use:

MIT-0

## Use Case:

External users, social media operators, and developers use this skill to prepare, schedule, publish, and review social content through connected OpenQuok integrations. It helps agents choose the right CLI commands, provider settings, media workflow, and authentication flow for supported social channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run a new-session check that reports OpenQuok authentication status and workspace name before the user asks for a specific OpenQuok action.

Mitigation: Install it only where that always-available behavior is desired, and use it in workspaces where revealing auth state and workspace name is acceptable.

Risk: The guided CLI workflows can schedule posts, create drafts, publish comments, configure automated engagement, and act from connected social accounts.

Mitigation: Review workspace, integration IDs, post IDs, privacy settings, acting accounts, captions, media, schedules, and plug settings before approving commands.

Risk: Incorrect authentication flow or stale CLI versions can leave the agent unable to complete device login or publish reliably.

Mitigation: Use the documented two-step device flow on messaging hosts, confirm credentials with auth status, and compare the installed CLI with the package page when version issues appear.

## Reference(s):

- [OpenQuok CLI package](https://www.npmjs.com/package/@openquok/auto-cli)
- [OpenQuok website](https://www.openquok.com/)
- [OpenQuok command reference](artifact/resources/command-reference.md)
- [Provider settings](artifact/resources/provider-settings.md)
- [OpenQuok plugs](artifact/resources/plugs.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide terminal-backed OpenQuok CLI actions that authenticate, upload media, schedule or draft posts, configure engagement plugs, and read analytics.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
