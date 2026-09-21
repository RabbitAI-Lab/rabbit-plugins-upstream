## Description:

Manage and diagnose Huawei Cloud WAF and AAD protections with the hcloud CLI, including read-only inventory and diagnostics plus confirmed WAF rule creation or deletion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud security operators, developers, and site reliability engineers use this skill to inspect Huawei Cloud WAF and AAD coverage, diagnose CNAME/rule-order/protection gaps, and safely prepare WAF rule changes through preview and confirmation flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or delete Huawei Cloud WAF rules, which may disrupt production traffic or weaken firewall protection if used incorrectly.

Mitigation: Use least-privilege read-only credentials by default, grant WAF rule create/delete permissions only to trusted operators, preview every change, start rule changes in report mode, and require explicit confirmation for production changes.

Risk: Automatic quality reporting may send sensitive WAF domains, IP addresses, policy details, command outputs, or error information.

Mitigation: Disable or constrain quality reporting for sensitive environments, and avoid sending detailed outputs or errors unless they have been reviewed.

Risk: The artifact documents a curl-to-bash KooCLI installer path, which can introduce supply-chain risk if run without verification.

Mitigation: Verify the installer independently or install KooCLI through an approved internal software channel before using the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-waf-aad-rule-management)
- [KooCLI Installation and Configuration Guide](references/cli-installation-guide.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [IAM Policies for huawei-cloud-waf-aad-rule-management](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Related Commands and Context](references/related-commands.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline hcloud commands and structured JSON-style results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostics may run automatically; WAF rule creation requires preview and confirmation, and deletion requires explicit confirmation.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
