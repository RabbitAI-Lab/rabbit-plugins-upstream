## Description:

Talenox helps agents inspect schemas and run read-only OOMOL connector actions for Talenox branches, employees, company settings, working days, and working hours.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Talenox through an OOMOL-connected account, inspect live action schemas, and retrieve HR and company configuration data through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions execute a remote OOMOL CLI installer directly.

Mitigation: Review the installer path before installation and prefer a pinned, verified, or manually inspected installer.

Risk: Connecting Talenox gives the OOMOL connector access to sensitive employee and company data visible to the Talenox credential.

Mitigation: Use an appropriate Talenox credential, review connection scope, and limit use to data the requester is authorized to access.

## Reference(s):

- [ClawHub Talenox Skill Listing](https://clawhub.ai/oomol/skills/oo-talenox)
- [Talenox Homepage](https://www.talenox.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action requests; read actions return structured JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
