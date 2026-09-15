## Description:

Todoist helps an agent read, create, update, and complete Todoist tasks, projects, sections, labels, and comments through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Todoist content through OOMOL's Todoist connector, including listing, creating, updating, and completing tasks and related project structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run remote installer scripts on the user's machine.

Mitigation: Review the installer path before use and prefer a verifiable, versioned installation method for the oo CLI.

Risk: Write actions can change Todoist tasks, comments, projects, or sections.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-todoist)
- [Todoist Homepage](https://www.todoist.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before Todoist actions and returns connector responses as JSON when commands are run.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
