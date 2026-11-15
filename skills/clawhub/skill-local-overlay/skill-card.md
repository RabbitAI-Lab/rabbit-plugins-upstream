## Description:

Local patch layer for marketplace, connector, and built-in skills that get overwritten on platform or plugin upgrades. Use BEFORE modifying any skill that is not agent-created, and AFTER an upgrade that may have wiped local edits. Snapshot before edit, record every change in a patch ledger (补丁台账), replay patches after upstream upgrades. Trigger keywords: 修改内置 skill, marketplace skill 更新覆盖, upgrade overwrote my changes, skill 修改丢失, 升级覆盖本地修改, overlay patch, patch ledger, 补丁台账, connector skill 定制, builtin skill 修改, keep local edits, re-apply patches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers maintaining marketplace-installed, connector, or built-in skills use this skill to preserve local edits across upgrades. It guides them to snapshot originals, record changes in a patch ledger, and replay applicable patches after an upgrade.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review had medium confidence because a local path-like reference could not be resolved, leaving the evidence incomplete.

Mitigation: Review the referenced local path and the skill's proposed changes before installing or applying them.

## Reference(s):

- [Skill Local Overlay on ClawHub](https://clawhub.ai/haiyangchenbj/skills/skill-local-overlay)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files]

**Output Format:** [Markdown workflow guidance, patch ledger entries, snapshots, and applied skill edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
