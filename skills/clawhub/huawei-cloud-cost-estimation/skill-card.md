## Description: <br>
Generate Huawei Cloud pre-order price estimates, safely provision allowlisted resources via hcloud, and guide unsubscribe requests to the console only. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agenticweb4](https://clawhub.ai/user/agenticweb4) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and finance-aware engineering teams use this skill to quote Huawei Cloud resources, prepare controlled provisioning commands, and route unsubscribe requests to the Huawei Cloud console. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create billable Huawei Cloud resources after user approval. <br>
Mitigation: Use least-privilege IAM credentials, review quoted costs, require a successful hcloud --dryrun, and obtain explicit confirmation before running provisioning commands. <br>
Risk: Huawei Cloud AK/SK keys or tokens could be exposed if pasted into chat. <br>
Mitigation: Do not accept credentials in chat; direct users to configure hcloud locally and verify with non-secret configuration checks. <br>
Risk: Partner delegated-token workflows can query customer account scope. <br>
Mitigation: Avoid delegated-token workflows unless the operator has explicit customer authorization and understands the account scope being queried. <br>
Risk: Automated unsubscribe or delete actions can cause data loss or incorrect refunds. <br>
Mitigation: Do not run or emit unsubscribe CLI/API commands; guide users to the Huawei Cloud console and remind them to back up data and review account, resource, refund, and related-resource details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/huawei-cloud-cost-estimation) <br>
- [Publisher profile](https://clawhub.ai/user/agenticweb4) <br>
- [KooCLI installation guide](references/cli-installation.md) <br>
- [Pricing command contract](references/pricing/commands.md) <br>
- [Pricing IAM policies](references/pricing/iam-policies.md) <br>
- [Pricing semantic catalog](references/pricing/semantic/catalog.yml) <br>
- [Lifecycle concepts](references/lifecycle/concepts.md) <br>
- [Lifecycle command allowlist](references/lifecycle/commands.md) <br>
- [Huawei Cloud unsubscribe rules](https://support.huaweicloud.com/usermanual-billing/unsubscription_topic_2000010.html) <br>
- [Huawei Cloud KooCLI quick install](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html) <br>
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/overview) <br>
- [Huawei Cloud IAM best practices](https://support.huaweicloud.com/bestpractice-iam/iam_0426.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with quoted prices, command proposals, confirmation prompts, and console guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires hcloud and locally configured Huawei Cloud credentials; provisioning commands require runtime help, cost review, dry-run, and explicit user confirmation.] <br>

## Skill Version(s): <br>
3.2.3 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
