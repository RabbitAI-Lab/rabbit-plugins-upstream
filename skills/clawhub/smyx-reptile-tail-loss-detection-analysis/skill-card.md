## Description:

Analyzes gecko and lizard tail images or videos to detect abnormal shortening, tail-tip wounds, scabs, regenerated-tail baselines, and tail-loss events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External keepers, breeders, and developers use this skill to review reptile enclosure images or videos, flag likely tail-loss events, and retrieve structured historical reports. It is intended to support monitoring workflows, not to replace professional veterinary assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded reptile images, videos, or URLs are sent to a configured backend for analysis.

Mitigation: Deploy only after confirming user consent, backend ownership, retention limits, and the expected media upload flow.

Risk: The skill can silently create or reuse an internal identity and store backend tokens in a local workspace database.

Mitigation: Review identity handling and token lifecycle before deployment, including local storage location, expiry, rotation, and deletion procedures.

Risk: The reviewed package includes private HTTP development endpoints.

Mitigation: Republish or configure the skill with production HTTPS endpoints before normal release use.

Risk: Visual tail-loss analysis may be unreliable when images are blurry, incomplete, poorly lit, below 1080p, or missing SVL/reference context.

Mitigation: Treat low-quality inputs as unreliable and request clearer side-view or top-view images that fully show the tail from cloaca to tip.

## Reference(s):

- [Reptile Tail Loss API Documentation](references/api_doc.md)
- [ClawHub Skill Listing](https://clawhub.ai/18072937735/skills/smyx-reptile-tail-loss-detection-analysis)
- [Skill Usage Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON analysis report, with Markdown tables for history queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the analysis result to a user-specified output file.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact SKILL.md frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
