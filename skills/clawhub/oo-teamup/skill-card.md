## Description:

Teamup Calendar helps an agent read, create, update, and delete Teamup calendar data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Teamup Calendar from an agent session, including listing events and subcalendars, retrieving event details, and creating, updating, or deleting events after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can execute remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI from a verified official release or trusted package manager, and inspect any installer before running it.

Risk: Create, update, and delete actions can change or remove Teamup Calendar data.

Mitigation: Confirm the exact target, payload, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Teamup Calendar skill page](https://clawhub.ai/oomol/skills/oo-teamup)
- [Teamup Calendar homepage](https://www.teamup.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when actions run.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
