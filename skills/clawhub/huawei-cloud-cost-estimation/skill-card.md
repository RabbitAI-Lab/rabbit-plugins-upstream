## Description:

This skill helps agents estimate Huawei Cloud costs, prepare allowlisted hcloud provisioning commands behind dry-run and confirmation gates, and route unsubscribe requests to console-only guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, cloud operators, and agents use this skill to request Huawei Cloud quotes, compare budget options, and prepare controlled provisioning workflows without accepting credentials in chat. It is intended for Huawei Cloud and hcloud KooCLI workflows only.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create billable Huawei Cloud resources after approval.

Mitigation: Use least-privilege IAM credentials and approve execution only after reviewing the dry-run command, target project, region, resource, quantity, and billing terms.

Risk: Cloud access keys or tokens could be exposed if pasted into chat.

Mitigation: Configure credentials locally through hcloud or environment variables and refuse plaintext AK/SK or token values in conversation.

Risk: Cloud quotes may be misleading if based on stale assumptions or mismatched parameters.

Mitigation: Use only current hcloud pricing responses, confirm region, resource type, specification, quantity, and billing period, and present quoted amounts as non-final bills.

Risk: Automated unsubscribe or deletion actions could remove resources or alter billing unexpectedly.

Mitigation: Provide console-only unsubscribe guidance and require the user to review account, resource, linked resources, refund amount, fees, and refund destination before submitting in Huawei Cloud.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/agenticweb4/skills/huawei-cloud-cost-estimation)
- [KooCLI installation guide](references/cli-installation.md)
- [IAM least-privilege policy notes](references/iam-policies.md)
- [Lifecycle execution concepts](references/lifecycle/concepts.md)
- [Lifecycle command allowlist](references/lifecycle/commands.md)
- [Pricing command contracts](references/pricing/commands.md)
- [Pricing semantic catalog](references/pricing/semantic/catalog.yml)
- [Huawei Cloud period pricing API](https://support.huaweicloud.com/api-bpconsole/bcloud_01002.html)
- [Huawei Cloud on-demand pricing API](https://support.huaweicloud.com/api-bpconsole/bcloud_01001.html)
- [Huawei Cloud resource specs API](https://support.huaweicloud.com/api-oce/qct_00008.html)
- [Huawei Cloud unsubscribe rules](https://support.huaweicloud.com/usermanual-billing/unsubscription_topic_2000010.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise plain-text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include hcloud dry-run commands, quoted costs from current responses, confirmation summaries, and console-only unsubscribe guidance.]

## Skill Version(s):

3.2.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
