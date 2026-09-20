## Description:

Helps agents operate LangSmith through the OOMOL-connected oo CLI for reading, creating, and updating datasets, examples, tracing projects, and workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect LangSmith connector schemas, run read actions, and create LangSmith datasets, examples, and tracing projects through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that should be reviewed before installation.

Mitigation: Prefer a pinned, verifiable oo CLI release or an official package manager flow before enabling the skill.

Risk: Write actions can create LangSmith datasets, examples, and tracing projects.

Mitigation: Confirm the exact LangSmith payload and expected effect with the user before running state-changing actions.

## Reference(s):

- [ClawHub LangSmith Skill](https://clawhub.ai/oomol/skills/oo-langsmith)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [LangSmith Homepage](https://www.langchain.com/langsmith)
- [OOMOL LangSmith Connection Setup](https://console.oomol.com/app-connections?provider=langsmith)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
