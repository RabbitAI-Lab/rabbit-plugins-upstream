## Description:

Ahrefs (ahrefs.com). Use this skill for ANY Ahrefs request - searching and reading data. Whenever a task involves Ahrefs, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Ahrefs keyword, subscription usage, and Site Explorer metrics through an OOMOL-connected Ahrefs account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ahrefs request and response data is routed through OOMOL.

Mitigation: Use the skill only when the user is comfortable sharing Ahrefs query data with OOMOL and the connected account is appropriate for the task.

Risk: First-time setup references internet installer commands for the oo CLI.

Mitigation: Avoid running installer commands until the CLI source and installation path have been reviewed.

## Reference(s):

- [Ahrefs homepage](https://ahrefs.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ahrefs)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Ahrefs connector actions return JSON data and metadata through the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
