## Description:

持续监控多个 Amazon ASIN 的评论、评分趋势和差评主题，并在负面反馈集中爆发时帮助运营人员对比竞品、生成 VOC 与改进建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and brand operators use this skill to monitor ASIN review sentiment, detect negative-review alerts, compare competitors, generate VOC and operations reports, and manage ongoing review monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores or reads an ARI API key and sends Amazon review data to ARI services.

Mitigation: Install only if the user trusts ARI/funewa with that data, keep the API key out of reports and examples, and revoke or rotate the key if access is no longer intended.

Risk: Paid analysis and collection actions can consume ARI credits, including paths where service-side autoconfirm may run small paid actions before a separate prompt.

Mitigation: Check the account autoconfirm setting before paid use and set it to ask every time when strict per-action approval is required.

Risk: Schedule, watch, and competitor-monitoring commands can create ongoing monitoring relationships and future credit use.

Mitigation: Confirm monitoring intent, review estimated monthly cost where provided, and use schedule or watch management commands to pause, delete, or return products to manual collection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/brand-monitor)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [README](artifact/README.md)
- [CLI and API reference](artifact/references/reference.md)
- [User guide](artifact/使用说明.md)
- [ARI API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown reports and concise operational guidance, with shell commands and optional CSV, HTML, or Markdown exports from the CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid operations can consume ARI credits and monitoring commands can create future recurring review collection.]

## Skill Version(s):

1.4.5 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
