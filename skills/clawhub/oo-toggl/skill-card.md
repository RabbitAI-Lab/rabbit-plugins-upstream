## Description:

Toggl Track lets an agent read, create, update, stop, and delete Toggl Track data through OOMOL's oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Toggl Track from an agent-connected OOMOL account, including listing workspace data, managing projects, tasks, tags, and time entries, and stopping running entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include one-line remote installer commands that can execute code on a user's machine.

Mitigation: Avoid running the remote installer commands unless the OOMOL installer endpoint and delivery chain are trusted; prefer a signed or package-manager install path, or download and verify the installer before execution.

Risk: Write and destructive Toggl Track actions can change or delete user data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-toggl)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Toggl Track homepage](https://toggl.com/track/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Toggl Track connection setup](https://console.oomol.com/app-connections?provider=toggl)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should inspect the live connector schema before payload construction and confirm write or destructive operations before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
