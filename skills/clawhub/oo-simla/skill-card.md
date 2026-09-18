## Description:

Simla.com guides agents through reading, creating, and updating Simla.com customer and order data through the OOMOL simla connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Simla.com customer and order workflows through an OOMOL-connected account, including listing, retrieving, creating, and editing records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback can execute remote oo CLI installer scripts without integrity verification.

Mitigation: Review the installer path before installing, prefer a signed or checksum-verifiable oo CLI release, and install only from trusted OOMOL sources.

Risk: Customer and order actions can create or edit live Simla.com records.

Mitigation: Inspect the live action schema and confirm the exact payload and intended account impact before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-simla)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Simla.com Homepage](https://www.simla.com/en)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should inspect the live connector schema before constructing payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
