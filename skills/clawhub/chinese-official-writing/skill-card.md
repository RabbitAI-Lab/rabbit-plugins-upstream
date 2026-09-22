## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩、润色、审校、文种核对、去口语化、降 AI 味及 Word 格式处理，适用于机关、企事业单位、学校和新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and document reviewers use this skill to draft, revise, compress, proofread, and format Chinese official documents, work materials, and news-style materials. It is especially suited to formal correspondence, reports, notices, summaries, meeting materials, procurement documents, feasibility materials, and review comments where facts, responsibilities, dates, and policy references need careful checking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential government, enterprise, procurement, personnel, or budget details may be exposed if the agent uses web search with unredacted draft content.

Mitigation: Keep processing local where possible; when web research is necessary, instruct the agent to avoid browsing with confidential details or to search only with redacted terms.

Risk: Generated official-document drafts may contain incorrect facts, numbers, policy references, responsibilities, or commitments.

Mitigation: Review factual claims, dates, figures, source references, obligations, and approval status before formal use.

## Reference(s):

- [README](artifact/README.md)
- [Reference Index](artifact/references/reference-index.md)
- [Genre Routing](artifact/references/genre-routing.md)
- [Writing Rules](artifact/references/writing-rules.md)
- [Review Checklist](artifact/references/review-checklist.md)
- [GB/T 9704 Formatting](artifact/references/format-gbt9704.md)
- [External Research Guidance](artifact/references/external-research.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Plain text or Markdown, with document files when host tooling is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include final drafts, revised drafts, review comments, post-draft notes, or formatted Word-ready content depending on the user request.]

## Skill Version(s):

2.0.10 (source: ClawHub release metadata and README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
