## Description:

Gov Disclosure Check helps agents run a zero-dependency local checker for government or public information disclosure text, verifying required fields such as decision basis, responsible department, time limit, remedy channel, and data source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance reviewers, and agent users use this skill to run a local disclosure completeness check for government or public-information workflows and get a deterministic pass/fail result with missing fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented one-command install path uses an unpinned global installer that can execute mutable third-party code.

Mitigation: Review the skill before installing; prefer a pinned release, specific commit, checksum-verified archive, or manual inspection of the cloned repository.

Risk: Disclosure checks are keyword-based and may miss legal or factual issues in the underlying public-information content.

Mitigation: Use the checker as a structured self-check and confirm consequential decisions against current official requirements and qualified professional review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/gov-disclosure-check)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON from a local CLI checker, with guidance in Markdown skill instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit codes indicate complete disclosure, missing required fields, or usage/environment errors.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
