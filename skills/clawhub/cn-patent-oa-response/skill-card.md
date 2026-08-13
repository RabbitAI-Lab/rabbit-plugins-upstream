## Description:

Analyzes CNIPA office actions, cited documents, and claim differences to prepare issue breakdowns, amendment bases, and draft response materials for professional review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent practitioners and agents use this skill to analyze CNIPA office actions, map examiner objections to claims and prior-art evidence, identify amendment support, and draft response materials. Outputs are drafts and require review by a qualified Chinese patent attorney or patent agent before filing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanned patent or office-action documents may be sent to a cloud OCR service when OCR is required.

Mitigation: Use OCR only for scanned or image-based inputs, confirm credential handling locally, and review OCR uncertainty before legal or technical analysis.

Risk: Draft office-action responses may contain incorrect legal strategy, amendment scope, citations, or technical conclusions if source documents or tool outputs are incomplete or misread.

Mitigation: Require qualified Chinese patent attorney or patent-agent review before any CNIPA filing and keep every substantive statement tied to cited evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/cn-patent-oa-response)
- [Source Map - Patent OA Response](references/source-map.md)
- [AI60 cloud OCR service](https://connect.zhihuiya.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown draft response analysis with cited issue tables, amendment notes, source appendix, and risk notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OCR-derived text and tool-assisted patent analysis; substantive statements must cite user documents, public patent data, or tool outputs.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
