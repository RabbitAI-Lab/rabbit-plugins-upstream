## Description:

Diagnoses whether Alibaba Cloud cloud-native products can reach the public internet or use a fixed public egress IP by resolving their VPC/vSwitch and checking NAT gateway SNAT egress in a read-only report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and support engineers use this skill to diagnose outbound public internet access and fixed public egress IP behavior for one user-confirmed Alibaba Cloud MSE gateway, cloud-native API gateway, AI gateway, SAE application, or FC function.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the current aliyun CLI session to read the named cloud resource, VPC/vSwitch, NAT/SNAT configuration, and caller identity metadata.

Mitigation: Confirm the product, region, and instance ID before use, and grant only the documented read-only RAM actions needed for the diagnosis.

Risk: Caller identity metadata may be cached locally in scripts/.sts_cache.json.

Mitigation: Treat the cache as account metadata, rely on its 0600 file permissions, and remove it after use if local policy requires no retained identity metadata.

Risk: A gw- prefixed identifier can refer to different Alibaba Cloud gateway products with different APIs.

Mitigation: Confirm whether the target is an MSE gateway, cloud-native API gateway, or AI gateway before running diagnostics.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-cloud-native-internet-diagnostics)
- [Instance Lookup](references/module1_instance_lookup.md)
- [vSwitch Egress Determination](references/module2_vswitch_egress.md)
- [RAM Policies](references/ram-policies.md)
- [Diagnosis Report Template](references/report-template.md)
- [aliyun CLI releases](https://github.com/aliyun/aliyun-cli/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON plus a human-readable diagnosis report with summary, conclusion, warnings, and next steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports on a single user-confirmed cloud resource and preserves degraded permission or lookup warnings when present.]

## Skill Version(s):

0.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
