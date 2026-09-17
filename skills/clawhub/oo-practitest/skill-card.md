## Description:

PractiTest helps agents read, create, update, and delete PractiTest projects and tests through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and developers use this skill to operate PractiTest projects and tests from an agent workflow. It supports listing and retrieving records, creating and updating tests, and deleting tests after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer execution for the OOMOL CLI.

Mitigation: Review the installer path before use and prefer an official package manager or a downloaded, versioned installer with checksum or signature verification.

Risk: Create, update, and delete actions can change or remove PractiTest data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before allowing write or destructive commands.

## Reference(s):

- [PractiTest homepage](https://www.practitest.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-practitest)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector commands can return JSON data from PractiTest actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
