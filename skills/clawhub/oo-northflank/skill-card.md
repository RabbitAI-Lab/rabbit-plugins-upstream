## Description:

Northflank helps agents list and retrieve Northflank project and service data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Northflank projects and services from an authenticated OOMOL-connected Northflank account without calling the Northflank API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute scripts directly.

Mitigation: Install the oo CLI from a verified, versioned source or inspect the installer before execution.

Risk: Read-only Northflank actions can expose project and service infrastructure details from the connected account.

Mitigation: Use the skill only with authorized OOMOL and Northflank accounts, and treat returned infrastructure data as sensitive.

Risk: Future or live connector actions may include write or destructive behavior even though the documented actions are read-only.

Mitigation: Fetch the live action schema before constructing payloads and get explicit user confirmation before running write or destructive actions.

## Reference(s):

- [Northflank Homepage](https://northflank.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-northflank)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action payloads should be built from the live schema returned by the oo CLI, and command results may include Northflank infrastructure details.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
