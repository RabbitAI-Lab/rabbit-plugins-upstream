## Description:

Operate Capsule CRM through the OOMOL-connected oo CLI to read, create, update, delete, search, and list CRM records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and agents use this skill to operate Capsule CRM records through an OOMOL-connected account without handling raw credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include unverified remote installer commands that can execute code on the user's machine.

Mitigation: Use a reviewed, version-pinned, checksum-verified oo CLI installation path and do not allow an agent to run the installer automatically.

Risk: Write and destructive Capsule CRM actions can create, update, or delete business records.

Mitigation: Confirm exact targets, payloads, and intended effects before running create, update, or delete actions.

## Reference(s):

- [Capsule CRM homepage](https://capsulecrm.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-capsule-crm)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data and an executionId under meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
