## Description:

7shifts (7shifts.com). Use this skill for ANY 7shifts request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to retrieve 7shifts company, department, location, role, user, and identity data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to execute remote installer scripts for the oo CLI.

Mitigation: Review the installer path before installation and prefer a manually inspected, version-pinned, checksum- or signature-verified installer from the vendor.

Risk: The skill operates through a connected 7shifts account, so excessive account scopes could expose more data than needed.

Mitigation: Connect only the 7shifts scopes needed for read access and re-check authorization if scope or credential errors occur.

## Reference(s):

- [7shifts ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-7-shifts)
- [7shifts Homepage](https://www.7shifts.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running 7shifts actions and returns connector JSON responses when actions execute.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
