## Description:

Operate Capsule CRM through the OOMOL-connected oo CLI to read, create, update, and delete CRM records without handling raw credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external CRM operators use this skill to inspect Capsule CRM action schemas and run read, search, create, update, and delete operations through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include downloaded installer commands that could execute remote code if run without verification.

Mitigation: Use a verified oo CLI package or inspect and verify the installer before execution.

Risk: The skill can create, update, and delete Capsule CRM records.

Mitigation: Require explicit user confirmation for write and destructive actions, including the target record and exact payload.

## Reference(s):

- [Capsule CRM](https://capsulecrm.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-capsule-crm)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI command results with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
