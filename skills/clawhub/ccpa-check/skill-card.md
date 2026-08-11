## Description:

CCPA/CPRA Compliance Check covers 12 core compliance checks for businesses subject to California privacy law, with offline preview and optional cloud scoring through compliancehub.cn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Compliance and privacy teams use this skill to preview CCPA/CPRA checklist items offline and, when they choose to provide an API key, generate a scored compliance report from their yes/no answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scored run sends checklist answers and an API key to compliancehub.cn.

Mitigation: Use the non-interactive preview for offline review, run scored checks only after confirming the destination, and prefer COMPLIANCEHUB_API_KEY on shared machines.

Risk: The generated report is compliance guidance and may not reflect a formal legal opinion.

Mitigation: Treat the report as a self-assessment aid and have qualified counsel review material CCPA/CPRA decisions.

## Reference(s):

- [CCPA Check Skill Page](https://clawhub.ai/wwumit/skills/ccpa-check)
- [Publisher Profile](https://clawhub.ai/user/wwumit)
- [API Key Reference](references/api_key.md)
- [ComplianceHub Account Page](https://compliancehub.cn/account.html?skill=ccpa-check)
- [ComplianceHub Service Endpoint](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Console text, JSON, or HTML report output with setup guidance and command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The offline preview lists bundled check items without network access; scored reports require COMPLIANCEHUB_API_KEY and send checklist answers to compliancehub.cn.]

## Skill Version(s):

2.2.0 (source: server release evidence, package.json, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
