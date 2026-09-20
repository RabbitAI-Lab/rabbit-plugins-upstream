## Description:

Evenium (corp.evenium.com) supports searching and reading event and guest data through the OOMOL-connected Evenium connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and agents use this skill to read Evenium event and guest information through an OOMOL-connected account, including event lookup, guest lookup, RSVP status, attendance status, filtered event lists, and filtered guest lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can lead an agent to install a remote oo CLI script automatically if the CLI is missing.

Mitigation: Confirm trust in OOMOL and its oo CLI distribution path, and install the CLI through a verified method rather than allowing automatic curl-to-bash or PowerShell execution.

Risk: The connected OOMOL account may expose Evenium event and guest data to the agent.

Mitigation: Review the connected account, scopes, and Evenium data access before using the skill.

## Reference(s):

- [ClawHub Evenium skill page](https://clawhub.ai/oomol/skills/oo-evenium)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Evenium homepage](https://corp.evenium.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector actions and returns Evenium read results as JSON when executed.]

## Skill Version(s):

1.0.4 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
