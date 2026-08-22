## Description:

Reduce duplicate storage by replacing safe redundant copies with symlinks. Identify the canonical copy first, verify consumers tolerate symlinks, preserve rollback, detect already-shared storage, guard against state drift, prefer atomic replacement, and prove the referenced path still works before reclaiming redundant data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pinguy](https://clawhub.ai/user/pinguy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan and verify symlink-based deduplication for large files or directories while preserving rollback and application compatibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Filesystem changes can remove or redirect data before compatibility is proven.

Mitigation: Review the proposed decision receipt before allowing changes, preserve rollback until acceptance, and verify the real consumer works through the symlink.

Risk: Directory, privileged path, cache, active state, or hard-to-restore deduplication can create fragile dependencies.

Mitigation: Require explicit review for these cases and avoid proceeding when identity, lifecycle ownership, rollback, or consumer symlink support is uncertain.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/pinguy/Skills/tree/main/skills/symlink-space-saver)
- [ClawHub skill page](https://clawhub.ai/pinguy/skills/symlink-space-saver)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and decision receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill emphasizes inspect-only planning before filesystem mutation and records verification receipts for identity, storage savings, rollback, and consumer acceptance.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
