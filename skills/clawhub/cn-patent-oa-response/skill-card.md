## Description:

Analyzes CNIPA office actions, cited references, and claim differences to produce issue breakdowns, amendment support, and draft response materials for patent-professional review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent professionals and agents use this skill to analyze CNIPA office actions, map examiner objections to claims and cited references, identify amendment bases, and prepare draft OA response materials. Outputs are drafts that require review by a qualified Chinese patent attorney or patent agent before CNIPA submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanned or image-based patent documents may be sent to the configured PatSnap AI60 cloud OCR service when OCR is needed.

Mitigation: Use OCR only for documents and API credentials the user is authorized to process, and avoid exposing credentials in prompts or generated materials.

Risk: Generated CNIPA response materials may contain incomplete legal or technical analysis if source documents, cited references, or amendment history are missing.

Mitigation: Require qualified patent-professional review before CNIPA filing and treat generated materials as drafts only.

## Reference(s):

- [Source Map - Patent OA Response](references/source-map.md)
- [PatSnap AI60 OCR Service Endpoint](https://connect.zhihuiya.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown draft response materials with cited analysis, amendment tables, source appendices, and risk notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OCR-assisted extraction notes and requires human patent-professional review before filing.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
