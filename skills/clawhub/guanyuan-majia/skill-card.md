## Description:

为观远 BI 用户提供实战指导，涵盖 ETL 治理、受限取数、看板验收、自定义图表与 SuperApp 兼容问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

供观远 BI 用户和开发者处理标准 CLI 覆盖之外的 ETL 治理、受限取数与结果验收、看板定制和发布兼容问题。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Archive cleanup instructions may delete unrelated archives.

Mitigation: Fix the cleanup behavior before relying on it; until then, delete only explicitly identified generated archives.

Risk: The uninstaller deletes a legacy credential backup it says it preserves.

Mitigation: Fix the uninstall behavior and keep any legacy credential backup outside the skill directory before uninstalling.

Risk: Customer attributes or production evidence may be exposed during BI or model-assisted workflows.

Mitigation: Keep production evidence private, select the intended agent and BI profile, and approve the model service before sending customer attributes.

Risk: External CLI packages and the OTA helper were not verified.

Mitigation: Verify these external components before relying on them.

## Reference(s):

- [Project homepage](https://github.com/maojiebc/majia-guanyuan)
- [ClawHub release page](https://clawhub.ai/maojiebc/skills/guanyuan-majia)
- [Security policy](https://github.com/maojiebc/majia-guanyuan/blob/main/SECURITY.md)
- [Restricted query playbook](https://github.com/maojiebc/majia-guanyuan/blob/main/references/restricted-query-playbook.md)
- [Dashboard evidence guide](https://github.com/maojiebc/majia-guanyuan/blob/main/references/dashboard-evidence.md)
- [Restaurant BI formulas](https://github.com/maojiebc/majia-huiyuan/tree/main/%E5%85%AC%E5%BC%8F%E5%BA%93)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, SQL, Code, Configuration, Markdown, HTML]

**Output Format:** [Markdown guidance, shell commands, SQL, Python and JavaScript examples, JSON configuration, and HTML/CSS dashboard templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples may use synthetic or offline data; live BI work depends on the user's configured Guandata environment.]

## Skill Version(s):

3.5.1 (source: release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
