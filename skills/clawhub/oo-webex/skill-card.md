## Description:

Webex helps an agent operate a connected Webex account to manage meetings, rooms, teams, memberships, messages, people, recordings, transcripts, and meeting summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and agents use this skill to read and manage Webex collaboration data through an OOMOL-connected account. It supports meeting administration, messaging, room and team management, participant lookup, recordings, transcripts, and AI-generated meeting summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute changing code from the internet.

Mitigation: Review the OOMOL CLI installation process outside the agent flow, prefer a signed or checksummed installer, and avoid running pipe-to-shell commands directly.

Risk: Webex write and destructive actions can create, update, or delete meetings, messages, rooms, teams, and memberships.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before running write or destructive actions.

Risk: Connected Webex credentials may have broader scopes than needed for a task.

Mitigation: Connect only the Webex scopes intended for use and resolve missing or expired scopes through the OOMOL connection flow before retrying.

## Reference(s):

- [ClawHub Webex skill page](https://clawhub.ai/oomol/skills/oo-webex)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Webex homepage](https://www.webex.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Webex action schemas and JSON payloads; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
