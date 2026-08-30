## Description:

Operate Webex through an OOMOL-connected account to read, create, update, and delete meetings, messages, rooms, memberships, people, recordings, transcripts, and teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent perform Webex meeting, messaging, space, people, recording, transcript, and team workflows through OOMOL's Webex connector. It is suited to account-scoped Webex automation where the user can review write and destructive actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read actions may expose Webex messages, meeting details, recordings, transcripts, people, rooms, and team data visible to the connected account.

Mitigation: Install and use the skill only when OOMOL's Webex connector is acceptable for the account, and request only the Webex data needed for the task.

Risk: Write and destructive actions can change or delete Webex meetings, messages, rooms, memberships, and teams.

Mitigation: Confirm the exact action, target, and JSON payload with the user before any write action, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Webex Skill Page](https://clawhub.ai/oomol/skills/oo-webex)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Webex](https://www.webex.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect each live connector schema before building a request payload and to return connector responses as JSON when running actions.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
