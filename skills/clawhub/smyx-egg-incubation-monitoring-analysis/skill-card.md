## Description:

Analyzes turtle and snake egg images or videos for visible incubation signals and produces developmental reports with access to cloud-based history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile breeders and incubator operators use egg images or videos to review visible development signals, receive incubation reports, and look up prior reports by egg.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Egg images and videos are uploaded to a cloud service, rather than analyzed solely on the user's device.

Mitigation: Confirm that upload is acceptable before use and ask the publisher to document data retention and deletion.

Risk: The skill silently creates or reuses identity records and stores authentication tokens locally.

Mitigation: Review remote account creation and local token storage with the publisher before installing.

Risk: History queries can access identity-linked cloud reports without a separate user confirmation.

Mitigation: Require confirmation before history queries and limit access to authorized reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-egg-incubation-monitoring-analysis)
- [Egg incubation monitoring API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured JSON reports or Markdown report summaries and history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links or save results to a file.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; bundled SKILL.md says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
