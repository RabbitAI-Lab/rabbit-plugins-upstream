## Description:

Backlog provides unified backlog lifecycle management and task tracking across session TODOs, markdown checklists, and issue trackers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to capture, triage, prioritize, synchronize, and prune backlog items across session TODOs, workspace checklist files, and issue trackers such as Plane or GitHub.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use Plane API keys and mutate Plane issues, comments, pages, and local tracker files.

Mitigation: Install only for trusted publishers, use scoped credentials, verify the active workspace configuration, and run dry-run modes before applying changes.

Risk: Automatic K3s or SSH-backed Django shell fallbacks can execute privileged changes against a Plane deployment.

Mitigation: Disable or remove K3s and SSH fallback paths unless explicitly required, and require an operator-approved kubectl or SSH context when they remain enabled.

Risk: Hard-coded private Plane endpoint behavior can target unintended services or workspaces.

Mitigation: Replace private defaults with explicit workspace-specific configuration and confirm PLANE_HOST, PLANE_WORKSPACE, and PLANE_PROJECT before use.

Risk: Prune workflows can remove issue-tracked P2/P3 entries from local active sections.

Mitigation: Use dry-run and anomaly checks first, keep tracker files under version control, and review the resulting diff before committing changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/backlog)
- [Skill Definition](artifact/SKILL.md)
- [Create Plane Issues and Intake Items](artifact/create.md)
- [Post Plane Issue Comments](artifact/comment.md)
- [Prune P2/P3 Backlog Items](artifact/prune.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON result schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce tracker mutations, local file edits, and JSON summaries when the bundled scripts are invoked.]

## Skill Version(s):

0.3.0 (source: server release metadata and changelog, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
