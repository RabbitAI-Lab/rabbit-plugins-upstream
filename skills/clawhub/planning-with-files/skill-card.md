## Description:

Provides persistent file-based planning for AI coding agents by storing task plans, findings, and progress in project markdown files so multi-step work can survive context loss or /clear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI coding agents use this skill to organize multi-step engineering, research, and build tasks with persistent plans, findings, progress logs, session recovery, and optional attestation or gated modes for long-running work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recovery workflow can surface prior local agent-session snippets without per-run confirmation.

Mitigation: Avoid use in workspaces containing secrets or sensitive chats unless the catchup workflow is reviewed or disabled.

Risk: Planning files are read back into agent context, so untrusted or tampered plan content can influence future turns.

Mitigation: Keep planning files under user control, treat injected plan content as data, and use attestation for long-running or gated plans.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/planning-with-files)
- [Examples: Planning with Files in Action](examples.md)
- [Reference: Manus Context Engineering Principles](reference.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown planning files with inline shell and PowerShell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates project-local planning files such as task_plan.md, findings.md, progress.md, and optional .planning state.]

## Skill Version(s):

3.10.2 (source: frontmatter metadata and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
