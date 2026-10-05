## Description:

Analyzes pet feeding videos or video URLs to estimate eating speed, provide a report, and suggest slow-feeding interventions when eating appears too fast, without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers of smart feeders use this skill to review feeding videos, estimate eating speed, and identify when a slow-feeding prompt may be appropriate. It can also retrieve prior analysis reports; results are informational, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-feeding videos or video URLs are sent to an external service for analysis.

Mitigation: Review before installing, obtain consent before sharing footage, and confirm the provider's privacy, retention, and deletion practices.

Risk: Analysis and history reports may be linked to an internal identity, and account tokens may be stored locally.

Mitigation: Use a separate workspace and account, limit access to local files and reports, and review what history the service retains.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/18072937735/skills/smyx-pet-eating-speed-slow-feed-analysis)
- [Pet eating analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Feeding-speed estimates, risk prompts, intervention suggestions, and report links; optional saved report file.]

## Skill Version(s):

1.0.13 (source: ClawHub server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
