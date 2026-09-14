## Description:

Generates a 10-item AI vendor due diligence checklist and scores vendor responses against a configurable threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Procurement, security, legal, and governance reviewers use this skill to request structured AI vendor answers, score a vendor response, and identify items that need human follow-up before contracting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill provides governance and vendor due-diligence support, not binding legal or regulatory advice.

Mitigation: Use its checklist and score as review inputs, then have qualified legal, security, or compliance owners confirm final contracting decisions.

Risk: Unpinned install instructions can allow a different skill version to be installed than the reviewed release.

Mitigation: Install only a reviewed version by pinning the skills CLI version or repository commit, avoiding sudo/admin shells, and reviewing the copied skill before enabling it.

Risk: The skill is mainly Chinese-language, which may cause misunderstanding for teams that do not review Chinese text directly.

Mitigation: Have bilingual reviewers or approved translations confirm checklist wording before using it in procurement workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-vendor-checklist)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown checklist templates, plain text score summaries, and optional JSON score reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled CLI exits with rc=0 for passing scores, rc=1 for scores below threshold, and rc=2 for usage or environment errors.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
