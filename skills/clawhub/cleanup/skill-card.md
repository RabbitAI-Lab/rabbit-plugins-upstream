## Description:

Runs an opinionated end-of-session cleanup workflow that reviews hook issues, preserves session state, stores relevant knowledge, updates checklist records, and recommends next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to run a structured wrap-up sequence at the end of a session, including hook review, knowledge persistence, checklist maintenance, and next-work capture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session or artifact data may be persisted to configured RAG stores or local queues during cleanup.

Mitigation: Use the config controls to disable persistence for sensitive sessions unless the receiver, retention policy, and hook environment are trusted.

Risk: The workflow can enforce broad session-end actions such as hook inspection, task creation or deletion, and commit-oriented cleanup.

Mitigation: Review the generated cleanup report and proposed actions before allowing changes that affect tasks, hooks, commits, or stored records.

## Reference(s):

- [ClawHub cleanup skill page](https://clawhub.ai/drumrobot/skills/cleanup)
- [SKILL.md](SKILL.md)
- [run.md](run.md)
- [rag-store.md](rag-store.md)
- [hook-review.md](hook-review.md)
- [config.md](config.md)
- [CHANGELOG.md](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline command examples, status tables, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local session records, checklist entries, RAG-store entries, and follow-up task recommendations when the referenced tools are available.]

## Skill Version(s):

0.6.0 (source: server release metadata and CHANGELOG, released 2026-09-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
