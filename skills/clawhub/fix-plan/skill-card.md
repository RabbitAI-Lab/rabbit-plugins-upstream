## Description:

Manages fix_plan.md and checklist.md schemas, lifecycle steps, priority and blocker triage, sync, archival, and completion criteria for agent work trackers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to keep fix_plan.md and checklist.md trackers structurally consistent, synchronized with external issue state, and cleanly archived as work completes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can edit and archive tracker files automatically.

Mitigation: Review target tracker paths before running mutation topics, use documented dry-run or backup paths where available, and inspect archive output before relying on cleanup results.

Risk: The skill may query GitHub or Plane and can expose issue or task metadata through those integrations.

Mitigation: Run sync only in workspaces where those external trackers are approved, and verify the relevant credentials and tracker URLs before use.

Risk: Configured RAG or vector routing may send detailed task bodies outside the active tracker.

Mitigation: Enable RAG dispatch only with an approved receiver and avoid it for sensitive markdown artifacts unless the destination is authorized.

Risk: Credential-output helper paths and workspace profile JSON can surface sensitive environment-derived details.

Mitigation: Avoid running workspace_profile.py --json in sensitive environments and keep Plane tokens out of shared logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix-plan)
- [CHANGELOG.md](artifact/CHANGELOG.md)
- [format.md](artifact/format.md)
- [priority.md](artifact/priority.md)
- [sync.md](artifact/sync.md)
- [move.md](artifact/move.md)
- [completion-criteria.md](artifact/completion-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands and optional file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit tracker files, archive completed entries, and report synchronized issue state when invoked with the relevant topic.]

## Skill Version(s):

0.6.2 (source: server release metadata and changelog, released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
