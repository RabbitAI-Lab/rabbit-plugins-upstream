## Description:

Analyzes emergency-shelter video for observable acute stress behaviors and provides psychological-crisis alerts for review by on-site responders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized emergency-response teams use shelter video to identify observable signs of distress, prioritize human review, and guide on-site psychological support; the output is not a clinical diagnosis.

### Deployment Geography for Use:

Global, subject to local emergency-response authorization

## Known Risks and Mitigations:

Risk: Emergency video and cloud reports may expose sensitive information about affected people.

Mitigation: Use only in an authorized response environment with explicit governance for video upload, cloud processing, report retention, and access to historical reports.

Risk: The skill can create or reuse persistent identities and store access tokens locally.

Mitigation: Verify where identities, tokens, and reports are stored, who can access them, and how they are deleted before use.

Risk: Broad automatic triggers may retrieve sensitive historical psychological-crisis reports unexpectedly.

Mitigation: Require operator confirmation before every history lookup and restrict who may query past reports.

Risk: Behavioral alerts may be mistaken for clinical conclusions or drive inappropriate dispatch.

Mitigation: Keep outputs at the observation level and require qualified responder review before escalating high-risk alerts.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis reports, crisis alerts, recommendations, and report links in JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports historical report listings and optional saved output.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
