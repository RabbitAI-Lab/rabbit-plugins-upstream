## Description:

Drata lets an agent search and read Drata company, control, personnel, vendor, and workspace data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, compliance operators, and agents use this skill to retrieve Drata compliance workspace information, including company metadata, controls, personnel, vendors, and available workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Drata compliance records through OOMOL server-side credentials.

Mitigation: Use a least-privilege, read-only Drata connection and confirm that the organization allows OOMOL to process Drata records.

Risk: The setup flow includes pipe-to-shell installer commands.

Mitigation: Avoid pipe-to-shell installation unless the installer source and integrity are verified through a trusted channel.

Risk: Connector requests depend on live schemas and connected-account scopes.

Mitigation: Inspect the live action schema before each request and verify that requested records match the intended Drata workspace and scope.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-drata)
- [Drata Homepage](https://drata.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON connector responses from Drata actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
