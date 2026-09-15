## Description:

The Workast skill lets agents read, create, complete, and update Workast tasks and spaces through an OOMOL-connected CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and team operators use this skill to inspect Workast spaces and tasks, create new tasks, update task details, and mark tasks complete. It is intended for agents acting on a connected Workast account with user confirmation before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts that are run directly in a shell.

Mitigation: Review the installer step before use, prefer a trusted versioned release or package manager with verification, and confirm Workast write payloads before allowing the agent to run them.

Risk: Write actions can create, update, or complete Workast tasks in the connected account.

Mitigation: Require user confirmation of the exact payload and intended effect before running any action tagged as write.

## Reference(s):

- [Workast ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-workast)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Workast Homepage](https://www.workast.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Workast connector requests and summarize JSON responses returned by the connected account.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
