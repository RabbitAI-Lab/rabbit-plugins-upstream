## Description:

Analyzes adult face images or short videos for visible fatigue-related features and provides a 0–100 fatigue/stress index with practical suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Adults and workplace wellness teams use this skill to review facial indicators of fatigue and view current or historical wellness reports. Its visual score is not a medical diagnosis or clinical stress assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images, videos, or URLs and related wellness data are sent to remote LifeEmergence services.

Mitigation: Obtain the subject's consent before use and review the provider's retention and deletion practices before sharing sensitive media.

Risk: Reports may be linked to an automatically created or reused identity, with user and token records stored locally.

Mitigation: Review account-linkage practices and protect or remove local user and token records according to your organization's policy.

## Reference(s):

- [Facial fatigue analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [JSON analysis report or Markdown history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a 0–100 index, level, contributing facial features, suggestions, and report links where available.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
