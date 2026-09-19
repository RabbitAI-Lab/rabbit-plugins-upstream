## Description:

Use this skill to search and read Rippling data through an OOMOL-connected account instead of calling the Rippling API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to retrieve Rippling worker, company, and department information from a connected Rippling account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer scripts are documented as setup options without verification.

Mitigation: Prefer a verified, signed, or package-manager installation method for the oo CLI before using the skill.

Risk: Rippling access is mediated through OOMOL and depends on connected account scopes.

Mitigation: Install only if that intermediary model is acceptable, and confirm the Rippling account scopes before running queries.

## Reference(s):

- [Rippling homepage](https://www.rippling.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action requests.]

## Skill Version(s):

1.0.3 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
