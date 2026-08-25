## Description:

Schedule and manage social posts with the OpenQuok CLI, including authentication, media uploads, drafts, scheduled posts, internal plugs, and channel analytics for an OpenQuok workspace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratimon](https://clawhub.ai/user/ratimon)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and social media teams use this skill to have an agent prepare OpenQuok CLI commands and JSON payloads for publishing, scheduling, drafting, and analyzing social posts across connected channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to run OpenQuok version and authentication status commands automatically at the start of a session.

Mitigation: Confirm which OpenQuok workspace and stored credentials are active before using the skill for posting or account management.

Risk: OpenQuok post creation, deletion, connection, and plug commands can publish content or change behavior on connected social accounts.

Mitigation: Review every posts:create, posts:delete, posts:connect, and plugs:* command before execution, including integration IDs, schedule times, media identifiers, and JSON settings.

Risk: Persistent cross-account plug automation can act from one connected account in response to activity on another account.

Mitigation: Configure cross-account plugs only for accounts whose owners explicitly approved the automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ratimon/skills/openquok-core)
- [OpenQuok CLI package](https://www.npmjs.com/package/@openquok/auto-cli)
- [OpenQuok website](https://www.openquok.com/)
- [Command reference](resources/command-reference.md)
- [Provider settings](resources/provider-settings.md)
- [JSON post examples](resources/examples/EXAMPLES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with OpenQuok CLI commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the global openquok CLI on PATH; examples use social-channel integration UUIDs and uploaded media identifiers.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
