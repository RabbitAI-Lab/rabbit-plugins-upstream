## Description:

Reviews Chinese talking-head scripts before publication by scoring information density, checking red-line issues, and separating platform machine-signal risks from content problems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and reviewers use this skill to audit Chinese short-form video scripts before publishing. It helps identify weak hooks, low-information sentences, red-line compliance issues, conversion-language risks, and machine-signal concerns while keeping diagnosis separate from rewriting by default.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feedback write-back or memory entries may save private plans, client details, or unpublished claims.

Mitigation: Use the skill only in a vault you control, and require confirmation or disable write-back before private material is saved.

Risk: Mutable vault files can override the reviewed bundled criteria.

Mitigation: Review local vault rules before use and make the report state whether local vault criteria or bundled artifact criteria were applied.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-review)
- [规则卡](references/规则卡.md)
- [评分锚点](references/评分锚点.md)
- [Evaluation sample README](evals/README.md)
- [Evaluation result sample 01](evals/results/sample-01-v0.3.0.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown review report with scoring tables, red-line findings, machine-signal notes, and concise rewrite options when issues are found.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnose-only by default; may ask for clarification when the target audience or source script is incomplete.]

## Skill Version(s):

0.2.9 (source: ClawHub release evidence; artifact frontmatter says 0.3.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
