## Description:

Estimate Huawei Cloud pre-order costs, provision allowlisted resources through hcloud, and guide unsubscribe requests through the console. Use for Huawei Cloud pricing, budgets, resource creation, unsubscribe guidance, or hcloud readiness checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud users and engineers use this skill to estimate Huawei Cloud costs, check hcloud readiness, and prepare allowlisted resource provisioning requests with cost and confirmation checks. It also guides users through console-based unsubscribe requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating paid cloud resources can incur ongoing charges.

Mitigation: Check and present the complete configuration and cost, then obtain explicit confirmation before making a real create call.

Risk: Cloud credentials could be exposed or granted broader access than needed.

Mitigation: Use a least-privilege local profile and never ask users to paste credentials into chat.

Risk: An unresolved ELB capacity or billing unit can make a quoted amount misleading.

Mitigation: Verify the product capacity and unit before including the line in a verified subtotal; otherwise mark it unverified and exclude it from that subtotal.

## Reference(s):

- [Declared project homepage (skill metadata)](https://github.com/concept-git/cloud-concept-skills/tree/main/skills/en/huawei-cloud-cost-estimation)
- [KooCLI installation guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [KooCLI installation and readiness](references/cli-installation.md)
- [Pricing workflow](references/pricing/commands.md)
- [Provisioning checks and failure handling](references/lifecycle/concepts.md)
- [Provisioning operation allowlist](references/lifecycle/commands.md)
- [IAM least privilege](references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Text and Markdown with itemized cost estimates, explanations, and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A single response may include pricing estimates and provisioning guidance; estimates are not final bills.]

## Skill Version(s):

3.2.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
