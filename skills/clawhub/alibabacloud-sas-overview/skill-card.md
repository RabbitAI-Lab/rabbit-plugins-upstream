## Description:

Retrieves Alibaba Cloud Security Center (SAS) overview data including security score, asset status, risk governance, asset risk trends, WAF blocks, and billing information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud security operators use this skill to query Alibaba Cloud SAS overview metrics and billing or subscription status through Aliyun CLI commands, scoped to the requested data item, module, or full dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup steps can persistently change the local Aliyun CLI environment and install or update plugins.

Mitigation: Use a separately verified Aliyun CLI and explicitly approved plugin versions; avoid mutable latest installers and curl-piped shell installation.

Risk: Cloud credentials or tokens could be exposed if placed in commands or agent chat.

Mitigation: Configure credentials outside the agent session, do not print access keys, and only verify credential status with safe profile listing commands.

Risk: The skill queries SAS, WAF, and billing data from an Alibaba Cloud account.

Mitigation: Use a dedicated least-privilege, read-only RAM profile for SAS, WAF, and billing overview queries.

## Reference(s):

- [Related APIs](references/related-apis.md)
- [RAM Policies](references/ram-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Aliyun CLI Installation Guide](references/cli-installation-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-sas-overview)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance]

**Output Format:** [Markdown with Aliyun CLI command blocks and concise result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries are scoped to the requested SAS overview module or data item; no cloud resources are created.]

## Skill Version(s):

0.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
