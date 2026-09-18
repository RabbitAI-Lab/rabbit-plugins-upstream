## Description:

Enables agents to handle NetSuite requests, including reading, creating, and updating data, through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and operations teams use this skill to read, create, update, list, and query NetSuite records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands that can execute changing code on the user's machine.

Mitigation: Prefer official, versioned, integrity-verified oo CLI installation steps and avoid blindly running pipe-to-shell commands.

Risk: NetSuite write actions can change business records.

Mitigation: Review the exact record type, record ID, and payload with the user before approving create or update actions.

## Reference(s):

- [NetSuite homepage](https://www.netsuite.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL NetSuite connection](https://console.oomol.com/app-connections?provider=netsuite)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-netsuite)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to inspect live connector schemas before constructing NetSuite action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
