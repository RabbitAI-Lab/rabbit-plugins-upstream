## Description:

Analyzes home-monitoring images or videos for prolonged periods without visits or interaction and provides care reports and alerts for families of older adults living alone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Families, caregivers, and community care teams use monitoring media to check for prolonged isolation, review analysis reports, and follow up on care alerts. Users can also request historical monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home-monitoring images or videos, media URLs, identity context, and report queries are sent to configured cloud services.

Mitigation: Confirm consent from the monitored person and caregivers, and use the skill only if you trust the publisher and the configured services.

Risk: The skill silently creates or reuses a persistent local identity and caches authentication tokens.

Mitigation: Restrict access to the local workspace data directory and treat its identity records and cached tokens as sensitive.

## Reference(s):

- [Unattended monitoring API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis reports or Markdown tables, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save a JSON report to a user-selected file.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
