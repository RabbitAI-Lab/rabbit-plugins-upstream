## Description:

Extracts Xiaohongshu note text, per-image OCR and descriptions, engagement details, and video transcripts from shared links, with optional translation and consumer insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People working with public Xiaohongshu links can use the skill to retrieve note text, image text, video transcripts, and engagement details. It can also provide translated output or optional summaries and consumer insights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports capabilities beyond the stated Xiaohongshu purpose and an optional integration that runs an unpinned package; the scan was partial because a local path-like reference could not be resolved.

Mitigation: Review the optional integration before use, and treat the unresolved reference as unevaluated. Skip installation unless the extra platform and analysis features are needed and the receiving service is trusted.

Risk: Submitted links are sent to LinkDigest, and results for public links may be cached and made available to others requesting the same link.

Mitigation: Do not submit private note links; review the LinkDigest privacy policy before sending links.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs?ref=skill-xiaohongshu-note-to-text)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content for one link, with optional transcript, translation, summary, and consumer insight sections.]

## Skill Version(s):

1.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
