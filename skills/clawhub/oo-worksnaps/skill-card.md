## Description:

Enables agents to search and read Worksnaps users, projects, tasks, assignments, time entries, and time reports through the OOMOL Worksnaps connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to retrieve Worksnaps account, project, task, assignment, time-entry, or time-report data from an OOMOL-connected Worksnaps account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup recommends executing remote installer scripts without verification.

Mitigation: Use a verified official installer, pinned release, or checksum/signature-verified installation before using the oo CLI.

Risk: The skill accesses Worksnaps data through OOMOL as an intermediary.

Mitigation: Install only when OOMOL-mediated access to Worksnaps data matches the user's data handling requirements.

## Reference(s):

- [ClawHub Worksnaps Skill](https://clawhub.ai/oomol/skills/oo-worksnaps)
- [Worksnaps Homepage](https://www.worksnaps.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector action schemas before constructing request payloads; Worksnaps credentials are handled server-side by OOMOL.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
