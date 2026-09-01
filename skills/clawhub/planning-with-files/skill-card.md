## Description:

Persistent file-based planning for multi-step AI-agent work, using task_plan.md, findings.md, and progress.md with lifecycle hooks that inject selected project planning context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to keep multi-step work organized across long sessions by storing plans, findings, progress, decisions, and recovery notes in project files. It is most useful for research, implementation, debugging, and other tasks that require repeated tool use or resumable state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Planning files can contain untrusted or instruction-like content that may be injected into agent context by hooks.

Mitigation: Treat injected planning content as structured data, keep external research in findings.md rather than task_plan.md, and use plan attestation before relying on automatic injection.

Risk: Explicit session replay can expose prior local session excerpts, commands, or paths from the same project.

Mitigation: Use session-catchup.py --metadata before --replay, request replay only when needed, and avoid replay in repositories where prior local session records may contain sensitive information.

Risk: Hook-based reminders and optional gated mode may affect the agent's stopping or planning behavior.

Mitigation: Install only when persistent planning hooks are desired, review active plan status regularly, and use gated mode only on hosts that support the required stop-hook behavior.

## Reference(s):

- [Planning with files ClawHub release](https://clawhub.ai/othmanadi/skills/planning-with-files)
- [Reference: Manus Context Engineering Principles](reference.md)
- [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [Examples: Planning with Files in Action](examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown planning files with inline shell or PowerShell commands and structured progress notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates project-local planning files; hook output is advisory planning context, and optional session replay emits bounded excerpts only when explicitly requested.]

## Skill Version(s):

3.12.0 (source: server release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
