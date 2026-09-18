## Description:

BoloForms (boloforms.com). Use this skill for BoloForms requests that read, create, or update workspace data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate BoloForms through an OOMOL-connected account, including listing documents, retrieving form responses, checking signing participants, and sending templates for signature after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run a remote installer script for the oo CLI.

Mitigation: Review the oo CLI installation path and prefer official, versioned installation instructions with verification before running installer commands.

Risk: The send_template_for_signing action changes BoloForms state by initiating signing requests.

Mitigation: Confirm the exact template, recipients, and payload with the user before running the write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-boloforms)
- [BoloForms Homepage](https://www.boloforms.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL BoloForms Connection](https://console.oomol.com/app-connections?provider=boloforms)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
