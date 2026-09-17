## Description:

Operates Customer.io through an OOMOL-connected account for reading, creating, updating, and deleting customer data, tracking events, and managing suppression or profile merges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Customer.io from an agent through the OOMOL-connected Customer.io connector. It supports customer profile changes, event tracking, suppression management, profile merges, and customer deletion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or delete Customer.io customer data without consistently requiring the confirmation its safety text claims.

Mitigation: Require explicit user confirmation for every create, update, event tracking, suppression, merge, or delete action, including actions that are not tagged as write or destructive.

Risk: Installer and authentication steps rely on remote OOMOL commands and account permissions.

Mitigation: Review installer commands before running them and use the skill only with trusted OOMOL and Customer.io account permissions.

## Reference(s):

- [Customer.io homepage](https://customer.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from Customer.io actions through the OOMOL connector.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
