## Description: <br>
Generate Huawei Cloud pre-order price estimates, safely provision allowlisted resources via hcloud, and guide unsubscribe requests to the console only. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agenticweb4](https://clawhub.ai/user/agenticweb4) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and FinOps users use this skill to quote Huawei Cloud resources, prepare guarded hcloud provisioning commands for allowlisted create operations, and receive console-only unsubscribe guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use a local Huawei Cloud CLI profile and can reach account-scoped pricing or provisioning APIs. <br>
Mitigation: Install only for agents that should use the local Huawei Cloud profile, keep credentials out of chat, and review the active hcloud configuration before use. <br>
Risk: Approved create operations may change cloud account state or incur charges. <br>
Mitigation: Require the documented allowlist check, runtime help lookup, fee review or unknown-cost disclosure, successful --dryrun, and explicit confirmation before any create command is run. <br>
Risk: Unsubscribe or delete-like workflows can affect refunds, data retention, or service continuity. <br>
Mitigation: Keep unsubscribe guidance console-only, remind users to back up data, and have users verify resource identity, associated resources, fees, and refund destination in the Huawei Cloud console. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/agenticweb4/skills/huawei-cloud-cost-estimation) <br>
- [KooCLI Installation Guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html) <br>
- [Huawei Cloud Unsubscription Rules](https://support.huaweicloud.com/usermanual-billing/unsubscription_topic_2000010.html) <br>
- [Huawei Cloud Period Pricing API](https://support.huaweicloud.com/api-bpconsole/bcloud_01002.html) <br>
- [Huawei Cloud On-Demand Pricing API](https://support.huaweicloud.com/api-bpconsole/bcloud_01001.html) <br>
- [Huawei Cloud Resource Specs API](https://support.huaweicloud.com/api-oce/qct_00008.html) <br>
- [Pricing Command Contracts](references/pricing/commands.md) <br>
- [Lifecycle Execution Concepts](references/lifecycle/concepts.md) <br>
- [Lifecycle Create Command Allowlist](references/lifecycle/commands.md) <br>
- [RFQ Semantic Catalog](references/pricing/semantic/catalog.yml) <br>
- [Pricing IAM Policies](references/pricing/iam-policies.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration instructions, Markdown] <br>
**Output Format:** [Markdown with hcloud command examples and concise pricing or lifecycle guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or run hcloud commands when credentials are already configured locally; create operations require dry run, fee review, and explicit confirmation.] <br>

## Skill Version(s): <br>
3.2.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
