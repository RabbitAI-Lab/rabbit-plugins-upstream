## Description:

Memory Bank Update Workflow - v6.12 compliant with project-repo awareness for agents invoked with $mem-update or asked to run this workflow by name.

This skill is ready for commercial/non-commercial use.

## Publisher:

[space-cadet](https://clawhub.ai/user/space-cadet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to maintain OpenClaw memory-bank records for project or workspace work. It helps identify the correct memory-bank location, scan existing tasks and session records, update scoped markdown files, and prepare a compliant commit message.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may read memory-bank notes across multiple project repositories.

Mitigation: Use it only in workspaces where the agent is allowed to inspect the relevant project and workspace memory-bank files.

Risk: The workflow may modify task, session, registry, and history markdown files in the selected memory bank.

Mitigation: Confirm the target memory-bank location and review proposed file diffs before committing changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/mem-update)
- [Skill source: SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, files, shell commands]

**Output Format:** [Markdown and concise text with file edits and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Updates scoped memory-bank records and generates a commit message when appropriate.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
