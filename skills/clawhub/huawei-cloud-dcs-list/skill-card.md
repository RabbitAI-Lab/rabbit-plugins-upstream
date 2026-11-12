## Description:

Lists Huawei Cloud DCS (Redis and Memcached) instances with optional filters and returns names, tables, JSON, or Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this read-only skill to inspect Huawei Cloud DCS inventories, filter instances, and prepare results for reports or downstream tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Combining exact-name searches with tag filters can silently ignore the tag restriction and produce misleading inventory results.

Mitigation: Avoid combining exact-name and tag filters until the filtering bug is corrected; verify the results with separate queries.

Risk: The bundled KooCLI installer source could not be verified.

Mitigation: Install KooCLI by following Huawei's verified instructions rather than using the bundled installer URL.

Risk: Credentials and exported inventories can expose access or infrastructure details.

Mitigation: Use credentials limited to DCS inventory access, configure secrets outside chat, and protect exports containing infrastructure details.

## Reference(s):

- [ClawHub release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-dcs-list)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [KooCLI installation and credential guide](references/cli-installation-guide.md)
- [Least-privilege IAM policy](references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Instance-name list, full-field table, raw JSON array, or ten-column Markdown table; Markdown may also be saved to a file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports server-side filters and automatic paging. Markdown cells escape pipes and flatten line breaks; missing fields display as dashes.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
