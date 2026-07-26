## Description: <br>
A Guandata BI agent skill that routes standard BI work to the official Guandata CLI family and guides ETL governance, custom dashboard and chart workflows, v7 publishing, SuperApp reverse-engineering, AI-native ADS design, and restaurant BI formulas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maojiebc](https://clawhub.ai/user/maojiebc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, BI administrators, and analytics engineers use this skill to handle Guandata BI workflows that need operational judgment beyond standard CLI routing, including ETL governance, custom chart injection, dashboard publishing, SuperApp integration, and business metric formula work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated publish, overwrite, delete, batch upload, and reverse-engineered API workflows can affect live Guandata BI assets. <br>
Mitigation: Use a least-privileged BI account, test in non-production first, export or back up pages, ETLs, and datasets before write operations, and require explicit human confirmation before destructive or publishing actions. <br>
Risk: The skill is intended for administrators of the target Guandata BI environment and may be unsafe for users without appropriate BI permissions or operational context. <br>
Mitigation: Install and run it only when administering the target BI environment, and review planned CLI/API actions before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/guanyuan-majia) <br>
- [Project homepage](https://github.com/maojiebc/majia-guanyuan) <br>
- [README](README.en.md) <br>
- [Security policy](SECURITY.md) <br>
- [Part B-17 full-chain rewrite methodology](references/part-b17-fullchain-rewrite.md) <br>
- [Part C HTML dashboard workflow](references/part-c-html-dashboard.md) <br>
- [V7 page/card publish pipeline](references/v7-page-card-publish-pipeline.md) <br>
- [SuperApp pipeline](references/part-e-superapp-pipeline.md) <br>
- [AI-native ADS design](references/ai-native-ads-design.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON payload examples, and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured Guandata BI account and the official @guandata/guanskill CLI family for live operations.] <br>

## Skill Version(s): <br>
3.1.8 (source: SKILL.md frontmatter, package.json, manifest.json, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
