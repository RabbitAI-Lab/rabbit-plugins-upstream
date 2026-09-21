## Description:

Toggl Track enables agents to read, create, update, and delete Toggl Track data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Toggl Track workspaces, projects, tasks, tags, and time entries through an OOMOL-connected account. It supports both read-only lookups and state-changing Toggl Track actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends remote installer commands that pipe downloaded scripts to a shell.

Mitigation: Review the installer step before use and prefer an OOMOL installation method that supports inspection or verification.

Risk: Write and destructive Toggl Track actions can create, update, stop, or delete account data.

Mitigation: Approve write or delete actions only after checking the exact workspace, object IDs, and payload.

## Reference(s):

- [Toggl Track skill page](https://clawhub.ai/oomol/skills/oo-toggl)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Toggl Track homepage](https://toggl.com/track/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
