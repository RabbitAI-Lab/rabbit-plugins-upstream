## Description:

Runs a session-end cleanup workflow that reviews automation, preserves useful knowledge, updates work records, and recommends next-session actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Cleanup at session end to preserve progress, review hook or skill behavior, store reusable findings, and prepare follow-up work for the next session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically initiate high-impact session-end actions, including workflow control through guard scripts.

Mitigation: Install only in trusted workspaces, review bundled hook scripts before enabling them, and disable automatic Stop-triggered cleanup when explicit user confirmation is required.

Risk: Session content and artifact details may be persisted to a RAG system or local pending queue.

Mitigation: Require consent before RAG import for sensitive work, scrub confidential content before persistence, and verify the configured receiver and retention policy.

Risk: The cleanup workflow can invoke other skills and keep local pending queues, which may affect follow-up task state.

Mitigation: Review cleanup reports, pending queues, and generated follow-up tasks before treating the session as fully closed.

## Reference(s):

- [Cleanup Skill](https://clawhub.ai/drumrobot/skills/cleanup)
- [Run](run.md)
- [RAG Store](rag-store.md)
- [Hook Error Review](hook-review.md)
- [Config](config.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger skill calls, local file updates, RAG persistence, and guard-script checks depending on the agent environment and cleanup configuration.]

## Skill Version(s):

0.5.1 (source: server release metadata and CHANGELOG, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
