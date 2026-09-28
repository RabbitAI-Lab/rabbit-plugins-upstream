## Description:

Through fixed enclosure cameras, the skill analyzes gecko and lizard tail images or videos to detect abnormal tail shortening, visible wounds, scabs, regenerated-tail baselines, and possible tail-loss events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External keepers, breeders, and developers use this skill to analyze reptile enclosure media for tail autotomy signals, generate structured event reports, and review account-linked historical reports. It is intended to support monitoring decisions, not to replace professional reptile veterinary judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media and URLs may be sent to the configured cloud analysis service.

Mitigation: Install only when the publisher and configured service are trusted, and avoid submitting sensitive media unless cloud processing is acceptable.

Risk: The skill resolves an internal identity, queries account-linked report history, and may persist account tokens locally.

Mitigation: Require authorization review before using real account-linked reports, do not pass arbitrary open-id values, and inspect local token storage practices before deployment.

Risk: Visual tail-loss results can be misleading when images are blurry, incomplete, poorly lit, below the required resolution, or missing SVL/reference data.

Mitigation: Treat unreliable inputs as inconclusive, request clearer media, and keep professional reptile veterinary review in the loop for wound or infection concerns.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-reptile-tail-loss-detection-analysis)
- [API Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Structured text or JSON reports with alert levels, measurements, recommended actions, disclaimers, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return cloud-service analysis results and historical report records associated with the resolved internal identity.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
