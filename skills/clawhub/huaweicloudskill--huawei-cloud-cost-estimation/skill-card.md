## Description:

Helps users obtain current Huawei Cloud price quotes, provision allowlisted resources after review and confirmation, and find console-only unsubscribe guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Huawei Cloud users and engineers use this skill to compare current pre-order prices and, with explicit approval, create supported cloud resources. It also guides users to the console for unsubscriptions without automating them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provisioning may create paid resources or use an unexpected configuration.

Mitigation: Review the resource, region, configuration and price; require a successful dry run and explicit confirmation before creation.

Risk: Cloud credentials could be exposed if shared in conversation.

Mitigation: Keep credentials in a local hcloud profile; never paste access keys, secret keys or tokens into chat.

Risk: Unavailable live pricing may leave costs unknown.

Mitigation: Do not invent a quote; disclose that pricing is unavailable and require additional approval before any potentially chargeable creation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cost-estimation)
- [Huawei Cloud CLI documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud price inquiry API](https://support.huaweicloud.com/api-bpconsole/bcloud_01002.html)
- [Huawei Cloud unsubscription guidance](https://support.huaweicloud.com/usermanual-billing/unsubscription_topic_2000010.html)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with price summaries and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quotes depend on current account pricing responses; provisioning requires a successful dry run and explicit confirmation.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
