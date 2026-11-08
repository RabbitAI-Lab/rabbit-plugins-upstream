## Description:

Conducts open-ended Q&A on image content based on computer vision and large language models, supporting natural-language responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users can provide an image and a question to get a natural-language visual analysis, or request a cloud-based list of prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags remote processing, implicit account creation, local identity and token storage, and history retrieval as capabilities to consider beyond image question answering.

Mitigation: Review these behaviors before use, send only images approved for remote processing, and confirm identity storage and report-history access are acceptable.

Risk: Model-generated visual answers may be inaccurate.

Mitigation: Verify important claims against the source image or another trusted source.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-visual-qa-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Natural-language answers, structured JSON results, and Markdown tables for report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers are model-generated and should be checked before relying on important information.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
