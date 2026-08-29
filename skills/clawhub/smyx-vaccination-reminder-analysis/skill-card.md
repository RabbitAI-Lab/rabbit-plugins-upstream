## Description:

Analyzes pet face images or video URLs to identify a registered pet, compare its vaccination record with the current date, and return due or overdue vaccination reminders without providing veterinary medical advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet hospitals, boarding centers, and insurance reviewers use this skill to check pet vaccination due status from a submitted face image or video and associated vaccination records. It returns database-comparison reminders, history listings, and report links rather than medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, URLs, and vaccination-record-linked data are sent to third-party cloud services for analysis and history retrieval.

Mitigation: Use the skill only where the lifeemergence.com backend is approved for this data, and confirm user consent, data-retention rules, and processing terms before deployment.

Risk: The skill silently creates or reuses a local identity and persists session tokens for cloud API access.

Mitigation: Review whether silent account creation and local token storage are acceptable, run the skill in an isolated workspace, and remove or rotate stored credentials when access is no longer needed.

Risk: History queries can return identity-linked vaccination reminder records and report links.

Mitigation: Restrict history-list usage to authorized operators and avoid exposing generated report links outside approved workflows.

## Reference(s):

- [Skill API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)

## Skill Output:

**Output Type(s):** [text, markdown, json]

**Output Format:** [Markdown or JSON structured analysis report, with optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include due or overdue status, recognized pet record details, history-list tables, and report links depending on the cloud API response.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter declares 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
