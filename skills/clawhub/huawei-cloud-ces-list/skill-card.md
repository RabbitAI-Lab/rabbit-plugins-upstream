## Description:

Queries Huawei Cloud CES metric lists and metric data through read-only ListMetrics and ShowMetricData operations, returning JSON while using AK/SK credentials from environment variables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to inspect Huawei Cloud CES monitoring metrics, retrieve metric datapoints, support resource health checks, investigate alert thresholds, and assist capacity planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud AK/SK credentials are required for execution and could be over-privileged if reused from a broad production account.

Mitigation: Use a dedicated IAM user with only CES metric list and get permissions, and provide credentials through environment variables only for the execution session.

Risk: The hcloud CLI installer is fetched from an external Huawei Cloud URL before the skill can run.

Mitigation: Verify the installer source and integrity according to the organization's software supply-chain controls before installing KooCLI.

Risk: Returned metric metadata and datapoints may reveal cloud resource identifiers, namespaces, dimensions, and operational usage patterns.

Mitigation: Limit where command output is stored or shared, and treat exported JSON as potentially sensitive operational data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/huawei-cloud-ces-list)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud CES API reference](https://support.huaweicloud.com/api-ces/ces_03_0057.html)
- [IAM permissions policy](artifact/iam-policies.md)
- [CLI installation guide](artifact/cli-installation-guide.md)
- [Verification method](artifact/verification-method.md)
- [Dataflow diagram](artifact/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands, plus JSON command output from the skill script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The list command returns count, total, marker, and metrics; the show command returns metric_name and datapoints; errors are JSON on stderr with non-zero exit codes.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
