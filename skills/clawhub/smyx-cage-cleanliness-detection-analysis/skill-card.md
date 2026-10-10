## Description:

Analyzes kennel images or videos for waste coverage and cleanliness, returning reports and cleaning alerts when a configured threshold is exceeded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Boarding facilities, pet shops, animal hospitals, and breeders use this skill to assess kennel floor cleanliness from images or video, request cleaning alerts, and retrieve past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kennel media or URLs may expose private customer, staff, or facility information when sent to a cloud service.

Mitigation: Review media for sensitive content and obtain authorization before cloud processing.

Risk: Account identity may be created or reused automatically, with tokens and database records persisted locally.

Mitigation: Review automatic account association and protect or remove local credentials and records as appropriate.

Risk: Cloud history retrieval is tied to the current or generated identity.

Mitigation: Confirm the associated identity and access permissions before retrieving or sharing historical reports.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cage-cleanliness-detection-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [JSON analysis results or Markdown report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cleaning recommendations and links to cloud-hosted reports; results can optionally be saved to a file.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
