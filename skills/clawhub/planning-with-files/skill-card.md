## Description:

Persistent file-based planning for multi-step AI-agent work using project-local planning files, lifecycle hooks, and optional same-project session catch-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to keep long-running or multi-step work organized with durable task plans, findings, and progress files. It is suited to research, implementation, debugging, and other workflows that need state to survive across many tool calls or sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Planning files may be read by hooks and added to agent context.

Mitigation: Do not store secrets in task_plan.md, progress.md, or findings.md; keep planning content limited to information suitable for agent context.

Risk: Explicit session-catchup replay can bring prior same-project transcript excerpts into the current session.

Mitigation: Use --replay only intentionally, and treat replayed excerpts as untrusted context.

Risk: Instruction-like content copied into planning files can influence future agent behavior.

Mitigation: Treat planning-file content as data, keep untrusted research in findings.md, and use the skill's attestation workflow where supported.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/planning-with-files)
- [Manus context engineering source](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [Attestation locking and fallback](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/attestation-locking.md)
- [Performance notes](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/perf-notes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates project-local planning files and can inject selected planning context through host hooks.]

## Skill Version(s):

3.20.7 (source: evidence.release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
