## Description:

Ambivo lets an agent read, create, update, and delete Ambivo CRM data through the OOMOL oo CLI connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Ambivo CRM records through an OOMOL-connected account, including contacts, leads, and tasks. It is suitable for CRM read workflows and for controlled write or delete actions after confirming payloads and targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Install or update the oo CLI only after independently trusting and verifying the installer source.

Risk: Write and destructive actions can modify or delete Ambivo CRM data.

Mitigation: Confirm each create, update, or delete payload with the user, and obtain explicit approval before deleting a task.

Risk: Connector schemas can change over time.

Mitigation: Fetch the live action schema before constructing payloads for Ambivo actions.

Risk: Ambivo access is mediated by OOMOL.

Mitigation: Use the skill only when the user is comfortable with OOMOL managing Ambivo access and credentials.

## Reference(s):

- [Ambivo homepage](https://www.ambivo.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ambivo)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
