## Description: <br>
Provisions Alibaba Cloud resource bundles for one-person company deployments after a supported SKU is selected, with Chinese step-by-step status and explicit confirmations before paid actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to provision predefined Alibaba Cloud SKUs for small-company web, app, and growth deployments. It guides account checks, CLI setup, resource creation, verification, manual fallbacks, and teardown-aware state handling. <br>

### Deployment Geography for Use: <br>
Alibaba Cloud regions, with the provided SKU parameters defaulting to cn-beijing. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create billable Alibaba Cloud resources and perform account-wide cloud actions. <br>
Mitigation: Require an itemized resource and price confirmation before any paid action, use quota limits, and review ESA PurchaseRatePlan and other broad actions before execution. <br>
Risk: Broad or mishandled cloud credentials could expose the user's Alibaba Cloud account. <br>
Mitigation: Use the dedicated RamRoleArn setup, avoid broad administrator credentials, never paste or echo AK/SK values, and review files written under state/, ~/.aliyun, ~/.local/bin, ~/.opc, and ~/.ssh. <br>
Risk: Provisioned resources may expose public web ports or leave SSH reachable if networking steps are skipped. <br>
Mitigation: Confirm public 80/443 exposure with the payment prompt and restrict SSH to the user's current IP as part of the security group flow. <br>
Risk: Some Alibaba Cloud products require partial or manual console steps that may be missed during automation. <br>
Mitigation: Use the CLI capability matrix before deployment, stop for console-only or partial products, and wait for user confirmation before continuing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-opc-deploy) <br>
- [Iron rules and credential safety](references/iron-rules.md) <br>
- [Execution phases](references/execution-phases.md) <br>
- [RAM least-privilege policy](references/ram-policies.md) <br>
- [CLI capability matrix](references/cli_capability_matrix.md) <br>
- [SKU parameter format](references/sku-params-format.md) <br>
- [Alibaba Cloud CLI documentation](https://help.aliyun.com/zh/cli/) <br>
- [Alibaba Cloud CLI install and update documentation](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli) <br>
- [Alibaba Cloud ECS RunInstances API](https://help.aliyun.com/zh/ecs/developer-reference/api-ecs-2014-05-26-runinstances) <br>
- [Alibaba Cloud SWAS API overview](https://help.aliyun.com/zh/simple-application-server/developer-reference/api-swas-open-2020-06-01-overview) <br>
- [Alibaba Cloud ESA PurchaseRatePlan API](https://help.aliyun.com/zh/edge-security-acceleration/esa/api-esa-2024-09-10-purchaserateplan) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese Markdown with step-by-step confirmations, status summaries, CLI command execution guidance, and resource tables.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit SKU selection and explicit confirmation before cost-incurring actions; writes deployment state and references Alibaba Cloud CLI configuration.] <br>

## Skill Version(s): <br>
0.0.1 (source: evidence.json release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
