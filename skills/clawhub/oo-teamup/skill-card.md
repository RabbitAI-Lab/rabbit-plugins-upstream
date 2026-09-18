## Description:

Teamup Calendar helps agents read, create, update, and delete Teamup Calendar data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Teamup Calendar from an agent session, including listing calendars and events, retrieving event details, and creating, updating, or deleting events after confirming write or destructive payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote shell and PowerShell installer commands for the oo CLI.

Mitigation: Prefer a versioned, verifiable oo CLI package or official release instructions, and review installer contents before execution.

Risk: Create, update, and delete actions can change or remove Teamup Calendar data.

Mitigation: Confirm the exact action target, payload, and expected effect with the user before running write or destructive commands.

## Reference(s):

- [Teamup Calendar homepage](https://www.teamup.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
