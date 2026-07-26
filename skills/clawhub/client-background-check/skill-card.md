## Description: <br>
客户背景调查助手，帮助销售和 business development users use public bidding data to investigate a target organization's procurement history, supplier landscape, budget level, procurement activity, major projects, public risk signals, and optional side-by-side company comparisons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales and business development users use this skill before client visits, bids, and commercial outreach to understand a company's procurement behavior, historical spend signals, incumbent suppliers, competitive landscape, and public risk signals. The skill can produce a single-company intelligence report or a two-company comparison based on bidding-data queries and public web research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts external Zhiliaobiaoxun services and sends query terms such as company names, regions, and procurement keywords. <br>
Mitigation: Use it only for queries appropriate for that service, and review the external-service dependency and data handling expectations before installation. <br>
Risk: The skill can create or store credentials locally in ~/.zlbx/config.json and can auto-register a trial account after user consent. <br>
Mitigation: Require explicit user opt-in before registration, prefer a preconfigured ZLBX_API_KEY where possible, and review or remove locally stored credentials when no longer needed. <br>
Risk: Generated reports are written to disk and may include business-sensitive analysis, contact data, and signed platform links. <br>
Mitigation: Store reports in an appropriate location, avoid sharing report files or access-bearing links broadly, and delete exported reports when they are no longer needed. <br>
Risk: Contact results and public-risk sections can affect real organizations or individuals if over-interpreted. <br>
Mitigation: Keep contacts masked unless the backend returns them otherwise, do not attempt to reconstruct masked contact details, cite sources for public-risk statements, and treat conclusions as data-supported signals rather than definitive judgments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/client-background-check) <br>
- [Workflow guide](artifact/references/workflow.md) <br>
- [API quick reference](artifact/references/api-quick.md) <br>
- [Report template](artifact/references/report-template.md) <br>
- [Auto-registration guide](artifact/references/auto-register.md) <br>
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool}) <br>
- [Zhiliaobiaoxun registration and recharge](https://ai.zhiliaobiaoxun.com/?ch=s127) <br>
- [Zhiliaobiaoxun business intelligence portal](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report in conversation, optional self-contained HTML report file, and operational guidance for API-backed company research workflows.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based registration; may write reports to ~/zlbx-company-intel-files/ and credentials to ~/.zlbx/config.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
