## Description:

Reviews talking-head scripts before publication with per-sentence density scoring, an eleven-question audience audit, red-line checks, and separate machine-signal guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and reviewers use this skill to decide whether a short-form talking-head script is ready to publish, needs targeted edits, or should be rewritten. It is tailored to solo knowledge creators who need a concise pre-publication review rather than a full rewrite.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the skill can write review feedback and recurring writing issues into persistent local vault or skill-memory files without clear opt-in or deletion controls.

Mitigation: Use it only with drafts that may be retained, require an explicit no-memory or opt-in workflow before running, and review or delete any generated memory files after use.

Risk: The skill issues publication-readiness and platform-signal judgments that could be mistaken for final compliance approval.

Mitigation: Treat the report as editorial guidance and confirm final scripts against current platform, legal, and brand requirements before publishing.

Risk: Artifact behavior allows local vault reference files to override bundled criteria, which can change review outcomes across environments.

Mitigation: Record which reference files were available during a review and prefer pinned or reviewed criteria for repeatable release workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-review)
- [规则卡](references/规则卡.md)
- [评分锚点](references/评分锚点.md)
- [Evaluation samples](evals/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review report with scoring tables, pass/fail findings, and rewrite guidance for flagged issues]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnose-only by default; may provide targeted replacement wording for red-line findings.]

## Skill Version(s):

0.2.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
