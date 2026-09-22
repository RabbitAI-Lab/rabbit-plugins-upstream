## Description:

Analyzes a pet facial image or video, matches the pet to vaccination records, and returns a due or overdue vaccination reminder based on configured intervals without providing medical advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet hospitals, boarding centers, and pet insurance workflows can use this skill to identify a pet from facial media, retrieve linked vaccination records, and determine whether a vaccination reminder is due. The output is a database-comparison reminder, not veterinary medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, and vaccination-record requests may be sent to remote services.

Mitigation: Use only approved HTTPS production endpoints and require explicit user or administrator consent before processing pet media or clinic-linked records.

Risk: The skill automatically creates or reuses account identity for analysis and history lookup.

Mitigation: Confirm the account-registration behavior, tenant mapping, and authorization model before enabling the skill for customer-facing workflows.

Risk: History report retrieval can expose customer-linked vaccination reminders.

Mitigation: Restrict report-list access to authorized users and verify that each request is scoped to the correct identity and tenant.

Risk: Returned tokens may be stored in plaintext.

Mitigation: Store tokens in a secure secret store, rotate exposed credentials, and avoid production use until token handling is reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown report or JSON-style structured output with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links and a Markdown history table when listing prior reports.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
