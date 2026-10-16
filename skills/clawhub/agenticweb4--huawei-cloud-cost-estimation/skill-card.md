## Description:

Generates Huawei Cloud pre-order estimates, provisions allowlisted resources through hcloud, and routes unsubscribe requests to console guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud engineers, and cost operators use this skill to estimate Huawei Cloud pre-order costs, prepare allowlisted hcloud provisioning commands, and route unsubscribe requests to console-only guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provisioning commands can create billable Huawei Cloud resources or change account state.

Mitigation: Use a least-privilege IAM user and approve execution only after the account, region, resource, billing mode, price or unknown-price warning, dry run, and command batch are clear.

Risk: Manual hcloud installation can place unverified binaries or scripts in PATH.

Mitigation: Verify installers and binaries through Huawei's official channels before installation and keep the agent limited to version and configuration checks.

Risk: Huawei Cloud AK/SK credentials are sensitive long-lived account credentials.

Mitigation: Use local profiles or environment configuration, avoid sharing secrets in chat or logs, and rotate or scope credentials according to IAM least-privilege practice.

Risk: Unsubscribe, delete, or refund workflows can cause data loss, service interruption, or unexpected fee handling.

Mitigation: Keep unsubscribe actions console-only, require backup or migration first, and have the user verify resource identity, related resources, fees, refunds, and refund destination in the Huawei Cloud Console.

## Reference(s):

- [Project homepage from Clawdis metadata](https://github.com/concept-git/cloud-concept-skills/tree/main/skills/en/huawei-cloud-cost-estimation)
- [Pricing command contract](references/pricing/commands.md)
- [Pricing semantic catalog](references/pricing/semantic/catalog.yml)
- [Lifecycle execution concepts](references/lifecycle/concepts.md)
- [Lifecycle command allowlist](references/lifecycle/commands.md)
- [IAM least-privilege guidance](references/iam-policies.md)
- [KooCLI installation guide](references/cli-installation.md)
- [Huawei Cloud unsubscribe rules](https://support.huaweicloud.com/usermanual-billing/unsubscription_topic_2000010.html)
- [Huawei Cloud KooCLI quick installation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/overview)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline hcloud command blocks and concise bullet lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pricing responses are based on current hcloud results; provisioning output must preserve dry-run, fee review, and explicit confirmation gates.]

## Skill Version(s):

3.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
