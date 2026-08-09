## Description: <br>
Queries Huawei Cloud monitoring and enterprise project resources across CES and EPS, including alarm rules, alarm histories, alarm templates, dashboards, notification masks, resource groups, one-click alarms, and enterprise project details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and support engineers use this skill to inspect Huawei Cloud CES monitoring resources and EPS enterprise project inventory using read-only query scripts. It helps verify alarm status, dashboards, resource groups, enterprise project metadata, quotas, bound resources, migration records, and reusable cloud resource identifiers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence reports that the skill disables HTTPS verification while using Huawei Cloud credentials. <br>
Mitigation: Review before installing, enable TLS verification or a trusted CA path before use, and run only with least-privilege Huawei Cloud credentials. <br>
Risk: The release evidence reports that the environment setup can fetch and run installer code. <br>
Mitigation: Remove the get-pip download-and-execute fallback or verify it strongly, and prefer preinstalled or pinned dependencies from a trusted package source. <br>
Risk: The skill performs authenticated IAM, CES, and EPS read queries that may expose cloud inventory, alarm, and enterprise project metadata in outputs. <br>
Mitigation: Use narrow query filters, avoid printing or storing secrets, cache large outputs only where appropriate, and restrict credentials to the minimum read permissions needed. <br>
Risk: Dependencies are specified with lower-bound version constraints. <br>
Mitigation: Pin dependency versions and hashes for repeatable installation before production deployment. <br>


## Reference(s): <br>
- [CES Python Script Usage Guide](references/ces/guide.md) <br>
- [Enterprise Project EPS Python Script Usage Guide](references/eps/guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-monitoring-query) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON or tabular query results from local Python scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Huawei Cloud query output depends on selected CES or EPS script, region, project scope, credentials, and pagination filters.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
