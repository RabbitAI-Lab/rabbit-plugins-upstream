## Description:

Pre-publish review for talking-head scripts that checks audience fit, sentence-level information density, red-line issues, and machine-review signals while diagnosing by default rather than rewriting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and editorial reviewers use this skill to review talking-head scripts before publication, with checks for whether viewers will click, stay, remember, and act. It produces a concise diagnostic report with scoring, red-line findings, machine-signal notes, and targeted revision options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store user feedback or review memory automatically, which can expose confidential strategy, client information, unpublished business plans, or sensitive editorial patterns.

Mitigation: Review the skill before installing, and disable or gate local vault and memory write-back behavior when drafts contain confidential or sensitive information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-review)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [规则卡](references/规则卡.md)
- [评分锚点](references/评分锚点.md)
- [Evaluation samples](evals/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown diagnostic report with scoring tables, red-line findings, machine-signal notes, and revision options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnose-only by default; rewriting is gated on explicit user request.]

## Skill Version(s):

0.4.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
