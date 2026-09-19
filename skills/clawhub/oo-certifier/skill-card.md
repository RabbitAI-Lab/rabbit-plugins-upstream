## Description:

Certifier (certifier.io) helps agents read, create, and update Certifier data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Certifier connector schemas, list or search Certifier records, and create, issue, or send credentials from an OOMOL-connected account after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may ask users to run internet installer scripts directly in a shell.

Mitigation: Review the setup path first, prefer a verified or pinned oo CLI installer, inspect downloaded scripts before execution, and avoid elevated shells.

Risk: Certifier write actions can create, issue, and send credentials to recipients.

Mitigation: Inspect the live action schema and confirm the exact recipient, group, and credential payload before allowing the action.

## Reference(s):

- [ClawHub Certifier Skill](https://clawhub.ai/oomol/skills/oo-certifier)
- [Certifier Homepage](https://certifier.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before forming payloads; write actions require confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
