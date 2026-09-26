## Description:

Analyzes resting pet videos to estimate respiratory rate, flag readings outside species-specific ranges, and provide a report for follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, veterinary teams, and boarding staff can analyze resting pet videos for respiratory-rate alerts and review past reports. Results are health indicators, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or submitted URLs are sent to a cloud analysis provider.

Mitigation: Use only media you are comfortable sharing; confirm the provider's retention and access controls before sending sensitive videos.

Risk: The integration creates or reuses a persistent local identity and stores service tokens in the workspace data database.

Mitigation: Review the identity and token-storage behavior before installing or running the skill; restrict access to workspace data.

Risk: The skill can automatically query cloud report history.

Mitigation: Limit access to report history and review which reports and links are shared.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON analysis results; Markdown links for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include respiratory-rate alerts and links to cloud-hosted reports; results are not diagnoses.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
