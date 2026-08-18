## Description:

Fix Plan manages fix_plan.md and checklist.md schemas, lifecycle states, priority triage, sync workflows, issue drafts, model triage, and completion criteria for agent task trackers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to maintain task trackers, move completed work into summaries, triage blockers, and synchronize tracker state with GitHub or Plane-backed workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled helper scripts can mutate external Plane state or synchronize tracker state through Plane credentials.

Mitigation: Install only in workspaces where Plane access is intended, keep Plane tokens scoped and unset by default, and prefer dry-run or review-only execution before allowing writes.

Risk: Helper behavior can upload markdown content to a vector store such as Qdrant.

Mitigation: Disable or remove Qdrant-related helpers unless indexing is expected, and review tracker and markdown contents for sensitive information before ingestion.

Risk: Some helper paths can use high-privilege Kubernetes or Django fallback commands.

Mitigation: Run the skill in a least-privilege environment and block Kubernetes or Django fallback execution unless the operator explicitly approves that workflow.

Risk: Plane token details may be exposed through JSON output.

Mitigation: Treat command output as sensitive, avoid logging token-bearing JSON, and verify that downstream tools redact or omit credentials before sharing reports.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/fix-plan)
- [SKILL.md](SKILL.md)
- [format.md](format.md)
- [sync.md](sync.md)
- [priority.md](priority.md)
- [move.md](move.md)
- [CHANGELOG.md](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured checklist edits, inline shell commands, and script-generated status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit tracker files and invoke GitHub or Plane sync helpers when those workflows are selected.]

## Skill Version(s):

0.8.0 (source: release metadata and CHANGELOG, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
