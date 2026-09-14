## Description:

Manage and diagnose Huawei Cloud WAF and AAD protection through hcloud CLI workflows for read-only inspection, WAF rule creation and deletion with confirmation, CNAME onboarding checks, rule-order review, and AAD EIP coverage guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and security engineers use this skill to inspect Huawei Cloud WAF and AAD posture, diagnose CNAME and DDoS coverage issues, and safely preview confirmed WAF rule changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quality reporting may transmit execution inputs, outputs, stack traces, protected domain names, IP addresses, WAF rule details, or cloud token authority.

Mitigation: Review telemetry behavior before installation and set SKILL_QUALITY_DISABLE=1 unless quality reporting is explicitly required.

Risk: Quality reporting can be redirected to an untrusted endpoint or run without TLS certificate verification if unsafe environment variables are set.

Mitigation: Keep SKILL_QUALITY_ENDPOINT trusted and do not set SKILL_QUALITY_INSECURE=1.

Risk: WAF rule creation or deletion can affect production traffic if confirmed with the wrong policy, rule, or action.

Mitigation: Use least-privilege Huawei Cloud credentials, preview exact commands, require confirmation for write actions, and start new blocking rules in log/report mode where possible.

Risk: AAD instance purchase and unsubscribe are console-only flows, so fabricated CLI commands would mislead operators.

Mitigation: Return console guidance for AAD lifecycle actions and verify package or protection state with supported hcloud list commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-waf-aad-rule-management)
- [KooCLI installation guide](references/cli-installation-guide.md)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [Related commands](references/related-commands.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured JSON summaries with inline hcloud CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions are previewed and require user confirmation; AAD purchase and unsubscribe actions return console guidance because no hcloud CLI operation is supported.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
