## Description:

Lets agents read Tally forms and submissions through an OOMOL-connected Tally account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to retrieve Tally forms and submissions through the OOMOL oo CLI connector without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup documents remote shell installer commands for the oo CLI.

Mitigation: Review the installer path and prefer a package manager, signed release, checksum-verified download, or locally inspected installer before installation.

Risk: Tally form submissions may include sensitive personal or business information.

Mitigation: Use the skill only for intended Tally data access and handle returned form and submission data according to the user's privacy and retention requirements.

## Reference(s):

- [Tally homepage](https://tally.so)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused Tally connector actions return form and submission data with execution metadata.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
