## Description:

Identifies bird species in images and videos and returns analysis reports for birdwatching and ecological observation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Birdwatchers and ecological observers use the skill to identify birds in images or videos and review cloud-based analysis and historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, or their URLs are sent to the lifeemergence.com cloud service for analysis.

Mitigation: Use only media approved for cloud processing; avoid sensitive images, private locations, and personal imagery unless the publisher's data handling is acceptable.

Risk: The skill can silently create or reuse a local account identity, store tokens locally, and retrieve cloud report history under broad triggers.

Mitigation: Review account and token behavior before installation, protect local credentials, and confirm intent before retrieving historical reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-bird-recognition-analysis)
- [Bird recognition API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; Markdown tables for historical report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and recognition results.]

## Skill Version(s):

1.0.23 (source: ClawHub release metadata; skill frontmatter states 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
