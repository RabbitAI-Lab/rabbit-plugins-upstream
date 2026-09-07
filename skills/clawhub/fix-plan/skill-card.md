## Description:

fix-plan manages fix_plan.md and checklist.md tracker schemas, lifecycle states, priority triage, sync, claims, issue drafts, model triage, and completion cleanup for agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to keep long-lived fix plans and checklists structured, deduplicated, prioritized, synchronized with external issue state, and ready for safe handoff across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify persistent tracker, archive, draft, and state files.

Mitigation: Review target files before invocation, prefer dry-run paths where available, and keep tracker changes under version control.

Risk: The skill can sync or index content through external systems such as GitHub, Plane, RAG, or Qdrant when those paths are configured.

Mitigation: Require explicit confirmation for external sync or indexing, and pin or remove the uvx/Qdrant import path before installation.

Risk: The security review flags broad local Python automation and cross-package code execution as requiring careful review.

Mitigation: Narrow allowed tools to the behavior needed in the target environment and avoid the unverified sibling plane_sync import for local-only claims.

Risk: Cleanup and archive workflows can remove or relocate active tracker content if misapplied.

Mitigation: Run documented dry-run or verification checks before cleanup and require confirmation for destructive cleanup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix-plan)
- [Skill overview](SKILL.md)
- [Changelog](CHANGELOG.md)
- [Format](format.md)
- [Priority](priority.md)
- [Sync](sync.md)
- [Claim](claim.md)
- [Move](move.md)
- [Add](add.md)
- [Update](update.md)
- [Upsert](upsert.md)
- [Verify](verify.md)
- [Completion criteria](completion-criteria.md)
- [Flowchart](flowchart.md)
- [Draft](draft.md)
- [Issue drafts](issue-drafts.md)
- [Model triage](model-triage.md)
- [Sync automation](sync-automation.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets and local file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update tracker, archive, issue-draft, state, and configuration-adjacent files when invoked.]

## Skill Version(s):

0.12.0 (source: server release metadata and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
