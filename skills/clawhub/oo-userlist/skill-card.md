## Description:

Userlist (userlist.com). Use this skill for ANY Userlist request - reading, creating, and updating data. Whenever a task involves Userlist, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Userlist connector schemas and run OOMOL-connected Userlist actions for reading, creating, and updating users, companies, relationships, events, and transactional messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or update Userlist records or send transactional messages with an incorrect target or payload.

Mitigation: Inspect the live action schema first and obtain explicit user confirmation for write targets and payloads before running the action.

Risk: The first-time setup section includes pipe-to-shell installer commands that may be unsafe if run without verification.

Mitigation: Prefer a verified OOMOL installation guide, pinned release, checksum, signature, or package manager before installing the oo CLI.

Risk: The connected OOMOL account may have inappropriate service permissions or billing state for the requested Userlist operation.

Mitigation: Use an OOMOL account with appropriate connected services and permissions, and resolve authentication, connection, scope, or billing errors before retrying.

## Reference(s):

- [Userlist homepage](https://userlist.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-userlist)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces oo CLI schema and run commands; write actions require confirmation of the target and payload.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
