## Description:

SureContact helps agents read, create, update, delete, and organize SureContact contacts, lists, and tags through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage SureContact account data from an agent, including contact lookup, list and tag management, and confirmed state-changing contact workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Prefer a verified or package-manager install path for the oo CLI before using this skill.

Risk: Some SureContact attach and detach operations can change account state without being clearly tagged as write or destructive actions.

Mitigation: Require explicit user confirmation for every SureContact state change, including attach and detach operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-surecontact)
- [SureContact Homepage](https://surecontact.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
