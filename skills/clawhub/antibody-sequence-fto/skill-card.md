## Description:

开展抗体及生物序列专利检索和FTO风险初筛，用于相似序列检索、专利族识别和权利要求相关性初筛。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, patent analysts, and R&D teams use this skill to run early antibody or biosequence patent/FTO screens from HC/LC protein sequences, including sequence similarity review, patent-family identification, risk grading, and HTML reporting before formal legal review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive antibody sequences or target details may be sent to patent or sequence search tools.

Mitigation: Review data-sharing permissions before use and submit confidential sequences only through approved connected tools.

Risk: Initial FTO screening output may be mistaken for formal legal advice.

Mitigation: Treat the report as a technical screen and require patent counsel to review claims before legal or commercial decisions.

Risk: Users who cannot read Chinese may miss workflow constraints and cautions in the skill instructions.

Mitigation: Review a reliable translation of the skill instructions before relying on the workflow.

Risk: Unsupported sequence identity, patent, or claim conclusions could mislead users.

Mitigation: Report only tool-returned facts with traceable source markers and state clearly when no supporting result is available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/antibody-sequence-fto)

## Skill Output:

**Output Type(s):** [text, HTML, guidance]

**Output Format:** [Source-linked HTML report with narrative findings and risk tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should use only returned tool data, source markers, and explicit no-result statements when evidence is unavailable.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
