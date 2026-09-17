## Description:

HelloLeads helps agents read, create, and update HelloLeads data through an OOMOL-connected HelloLeads account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect HelloLeads web form definitions and submit supported lead data through a connected HelloLeads account. It is useful when an agent needs to work with HelloLeads through the OOMOL oo CLI instead of direct API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that run downloaded scripts directly.

Mitigation: Review the installer instructions first, prefer an official versioned, signed, or checksum-verified oo CLI installation method, and avoid elevated privileges unless OOMOL documents why they are required.

Risk: The submit_web_form action can create a lead in HelloLeads.

Mitigation: Confirm the exact submission payload and expected effect with the user before allowing the write action.

## Reference(s):

- [HelloLeads ClawHub skill page](https://clawhub.ai/oomol/skills/oo-helloleads)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [HelloLeads homepage](https://www.helloleads.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run oo CLI connector schema and connector run commands; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
