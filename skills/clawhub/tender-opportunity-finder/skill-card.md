## Description: <br>
招标商机发现助手，可根据行业、产品和地区扫描拟建项目、采购意向、临期续约和项目进展线索，并按价值排序输出商机清单。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sales, business development, and market teams use this skill to find early tender opportunities from a requested industry, product, region, or budget threshold. It produces ranked opportunity lists with next-step guidance for follow-up before or near procurement events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts Zhiliaobiaoxun services and requires a ZLBX API account or user-approved trial registration. <br>
Mitigation: Install only if this service dependency is acceptable, and prefer setting your own ZLBX_API_KEY before use. <br>
Risk: Trial registration can collect a hashed device identifier and store an API key locally. <br>
Mitigation: Use preconfigured credentials to skip registration, approve registration only when comfortable with the device-derived signal, and avoid shared machines when local credential storage is not acceptable. <br>
Risk: Generated reports may contain signed direct-access links returned by the service. <br>
Mitigation: Review generated reports before sharing and remove links or files that should not be distributed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/tender-opportunity-finder) <br>
- [Workflow guide](artifact/references/workflow.md) <br>
- [API quick reference](artifact/references/api-quick.md) <br>
- [Report template](artifact/references/report-template.md) <br>
- [Auto-registration flow](artifact/references/auto-register.md) <br>
- [Zhiliaobiaoxun opportunity platform](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown opportunity list with optional HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved trial registration; reports may include signed direct-access links returned by the service.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
