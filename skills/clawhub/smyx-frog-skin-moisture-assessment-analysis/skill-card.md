## Description:

Assesses frog skin moisture from dorsal or side-view images and videos and provides dehydration-risk reports and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Frog keepers, animal-care professionals, and developers use images or videos from vivariums to assess skin moisture, review dehydration-risk alerts, and retrieve historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Frog images, videos, or URLs and report requests are sent to the LifeEmergence cloud service.

Mitigation: Use only media suitable for cloud processing and confirm the service's retention and account controls before submitting sensitive content.

Risk: The skill silently creates or reuses a persistent local identity and caches authentication tokens.

Mitigation: Review the workspace data directory after use, protect cached tokens, and remove them when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-frog-skin-moisture-assessment-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured JSON results or Markdown reports and history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dehydration-risk alerts, suggested actions, and cloud report links.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
