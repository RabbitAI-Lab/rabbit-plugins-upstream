## Description:

Detects delivery packages in a target surveillance area for inventory checks and unattended alerts at community stations, residential entrances, and office building lobbies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, operations teams, and developers use this skill to analyze surveillance images or videos for package presence, counts, locations, overdue pickup reminders, and report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images, videos, and report-history queries may be sent to configured remote services.

Mitigation: Use only with appropriate privacy notice and permission, and confirm that the configured API endpoint is approved before submitting media or retrieving history.

Risk: The skill may automatically create and reuse local identity state and store tokens in the workspace data directory.

Mitigation: Review local identity and token storage behavior before installation, restrict workspace access, and clear stored state when rotating users or environments.

Risk: Published configuration includes development or private HTTP endpoints.

Mitigation: Remove or override non-production endpoints before deployment and document the intended production service endpoints.

Risk: Payment prompts or account-provisioning flows may occur during use.

Mitigation: Require explicit user confirmation before account provisioning, history retrieval, or any paid action.

## Reference(s):

- [Package Detection API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown or JSON structured analysis report, with optional saved file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include package detection status, counts, locations, overdue pickup reminders, recommendations, and report links returned by the configured remote API.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
