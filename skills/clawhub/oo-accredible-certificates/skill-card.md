## Description:

Accredible Certificates (accredible.com). Use this skill for Accredible Certificates requests involving credential and group reads, creation, search, listing, and deletion through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Accredible Certificates records from an OOMOL-connected account, including credential lifecycle actions and credential group discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands for the oo CLI.

Mitigation: Use an official, verified installation path and review any installer script before execution.

Risk: The skill can expose certificate, group, and recipient records through the OOMOL connector.

Mitigation: Install only when this data exposure is acceptable for the deployment and account context.

Risk: Create and delete actions can change Accredible Certificates state.

Mitigation: Require explicit user confirmation of the payload, target, and intended effect before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-accredible-certificates)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Accredible Certificates homepage](https://www.accredible.com/)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing Accredible credential, group, recipient, and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
