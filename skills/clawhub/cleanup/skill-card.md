## Description:

Cleanup runs a configurable session-end loop that reviews pending work, analyzes mistakes and hook errors, persists useful knowledge, prunes failed-attempt records, and records next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Cleanup at session end to preserve state, record lessons, clean local tracking records, and prepare next-session work. It is intended for wrap-up workflows where memory, RAG storage, checklist hygiene, and self-improvement steps should run consistently.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist raw session content, artifacts, and local findings to a configured RAG store or pending queue.

Mitigation: Disable memory and RAG-related tasks before sensitive sessions, review the configured receiver, and avoid installing it where private code, credentials, customer data, or regulated context may be captured.

Risk: The session-end workflow may commit changes and update or delete local task, checklist, failed-attempts, and improvement records.

Mitigation: Review proposed changes before approval, keep source control available for recovery, and use the configuration guide to disable tasks that are too aggressive for the workspace.

Risk: Hook review, helper scripts, and external coordination can affect local automation behavior during wrap-up.

Mitigation: Inspect bundled scripts and hook procedures before enabling the skill, run it only in trusted workspaces, and keep direct hook modifications behind explicit review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/cleanup)
- [Publisher Profile](https://clawhub.ai/user/drumrobot)
- [Cleanup Skill Definition](SKILL.md)
- [Run Workflow](run.md)
- [RAG Store Procedure](rag-store.md)
- [Retrospect Procedure](retrospect.md)
- [Failed-Attempts Prune Procedure](fa-prune.md)
- [Hook Review Procedure](hook-review.md)
- [Configuration Guide](config.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline commands, configuration snippets, and local-file update guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update commits, task/checklist records, memory entries, RAG store items, queue files, and improvement notes depending on enabled topics, available tools, and user approvals.]

## Skill Version(s):

0.2.0 (source: server release metadata and CHANGELOG, released 2026-08-29; SKILL.md metadata lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
