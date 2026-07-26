## Description: <br>
Alibaba Cloud OPC Advisor helps non-technical solo founders choose a standard Alibaba Cloud OPC package with pricing, purchase guidance, and a plain-language launch or migration path. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to triage one-person-company cloud hosting needs, distinguish first launches from migrations, and recommend an appropriate Alibaba Cloud OPC SKU before any deployment action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SKU recommendations can influence cloud spend and production architecture decisions. <br>
Mitigation: Confirm the SKU, region, monthly price, billing impact, and account eligibility before purchase or provisioning. <br>
Risk: Migration guidance may lead to DNS, data, or availability changes if another agent executes it. <br>
Mitigation: Require backups, a rollback plan, and explicit user approval before any deployment, DNS, or data-migration step. <br>
Risk: The skill is recommendation-oriented but discusses assisted purchasing and deployment flows. <br>
Mitigation: Keep this skill in advisory mode until a separate, authorized execution workflow is invoked. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-opc-advisor) <br>
- [A1 Branch Output Template: Zero-Start Five-Section Format](references/a1-zero-start.md) <br>
- [A2 Branch Output Template: Migration Five-Section Format](references/a2-migration.md) <br>
- [OPC SKU Matrix](references/skus.md) <br>
- [SKU Sizing Questionnaire - Pre-Engagement Scale Assessment](references/sku-sizing-questionnaire.md) <br>
- [Concurrent Users Triage & SKU Mapping Guide](references/concurrency-to-sku.md) <br>
- [Purchase / Console Entry-Point Canonical Registry](references/purchase-url-canonical.md) <br>
- [Domain & ICP Filing Appendix](references/domain-and-icp.md) <br>
- [UGC Application Hardening - Public UGC Site Security Checklist](references/ugc-application-hardening.md) <br>
- [Alibaba Cloud OPC Package Page](https://opc.aliyun.com/products) <br>
- [Alibaba Cloud Domain Registration](https://wanwang.aliyun.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration] <br>
**Output Format:** [Chinese Markdown prescription with optional structured YAML for deployment handoff] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only recommendation output; the skill does not deploy resources by itself.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
