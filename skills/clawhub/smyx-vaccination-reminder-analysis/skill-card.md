## Description:

Analyzes a pet face image or video to identify the pet, compare linked vaccination records with the current date, and return a due or overdue vaccination reminder without providing medical advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet hospital, boarding center, and pet insurance workflows can use this skill to check whether a recognized pet appears due or overdue for vaccination based on linked records. It is intended for record comparison and reminders, not veterinary diagnosis or medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, and report queries are sent to configured cloud services.

Mitigation: Use only when that data transfer is approved, and review the provider's documented authorization, retention, and access controls before operational use.

Risk: The skill silently reuses or creates a local account identity and may store tokens or identity data in the workspace data directory.

Mitigation: Run it in a controlled workspace, avoid shared work directories, and clear or rotate stored identity data when switching users or environments.

Risk: The security summary notes that the code is broader and less specific than the vaccination-reminder purpose implies.

Mitigation: Review the installed artifact before deployment and do not treat outputs as verified vaccination records unless the publisher documents the backend data source and report-history access controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown or JSON analysis results, with optional Markdown table output for history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include due or overdue reminder status, pet type, report links, and saved text output when an output path is provided.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
