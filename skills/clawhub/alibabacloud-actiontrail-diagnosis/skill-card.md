## Description:

Provides read-only diagnosis of Alibaba Cloud ActionTrail audit events so an agent can identify who performed an operation, when it happened, from which source IP, and on which resource.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and incident responders use this skill to query Alibaba Cloud audit history, investigate resource changes or suspicious operations, and produce either a readable event summary or machine-readable results for follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit logs and JSON output can expose sensitive account activity and operational history.

Mitigation: Treat generated results as sensitive data, use the minimum read-only RAM permissions, and avoid sharing raw output outside the investigation context.

Risk: Automatic dependency installation can conflict with controlled runtime environments.

Mitigation: Leave ACTIONTRAIL_AUTO_INSTALL disabled in managed environments and preinstall or approve dependencies through the normal change process.

Risk: Overly broad ActionTrail queries can return account-wide activity and make findings hard to interpret.

Mitigation: Confirm region, time window, and product or event filters before execution, and narrow the query before treating results as complete.

## Reference(s):

- [LookupEvents API Reference](references/api-reference.md)
- [LookupAttribute Parameter Guide](references/lookup-attribute.md)
- [Full ActionTrail Event Catalog for Network Products](references/network-events-catalog.md)
- [RAM Permissions (Minimum Read-Only Policy)](references/ram-policies.md)
- [ActionTrail ServiceName Mapping for Network Products](references/service-mapping.md)
- [Alibaba Cloud LookupEvents API Explorer](https://api.aliyun.com/api/Actiontrail/2020-07-06/LookupEvents)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown table and summary, or JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on actual API returns; credential values are not printed, and audit identifiers are masked except for the effective account UID.]

## Skill Version(s):

0.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
