## Description:

Uses the OOMOL-connected oo CLI to inspect schemas and read Rippling workers, companies, and departments without calling the Rippling API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to retrieve Rippling worker, company, and department data through an OOMOL-connected account while relying on the live connector schema for request payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may lead an agent to execute a remote oo CLI installer directly in the shell.

Mitigation: Install the oo CLI through a separately verified official package or reviewed installer before using the skill.

Risk: The skill can retrieve HR-related Rippling data through the connected account.

Mitigation: Use only in environments where OOMOL and Rippling access is approved and scoped for the requested data.

## Reference(s):

- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Rippling homepage](https://www.rippling.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live action schemas before constructing connector requests; available documented actions are read-only.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
