## Description:

AI销售线索雷达 helps government and enterprise sales, business development, and channel teams find, rank, and track sales leads from proposed projects, purchase intentions, and expiring contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales and business development users use this skill to turn an industry, product, and region into a prioritized sales-opportunity list with recommended next actions. It supports one-time scans, follow-up on a specific opportunity, and recurring morning-report style monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor receives lead-search query terms and related scan criteria.

Mitigation: Use only queries you are comfortable sending to the vendor API, and avoid including confidential customer or strategy details in search terms.

Risk: Auto-registration can collect device-deduplication data and store an API key in ~/.zlbx/config.json.

Mitigation: Prefer configuring ZLBX_API_KEY manually; if auto-registration is used, review and remove ~/.zlbx/config.json later if the stored key is no longer wanted.

Risk: Generated reports may contain direct-access sk links.

Mitigation: Avoid sharing generated reports unless those links are safe for the intended recipients.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/ai-sales-lead-radar)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Workflow reference](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Zhiliaobiaoxun lead platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown lead list in chat, with an optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritized opportunities include ranking rationale, data gaps, next actions, source links, and scan-cost notes.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
