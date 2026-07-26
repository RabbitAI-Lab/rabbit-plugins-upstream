## Description: <br>
Helps agents produce traceable company due-diligence reports from bidding and award records, including bid history, performance evidence, partner and customer context, competitor landscape, and public-risk notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business users, procurement teams, supplier-review teams, and agents use this skill to investigate a company's bidding history, performance evidence, fulfillment signals, partners, competitors, and public-risk context. It supports single-company reports and two-company comparisons with source links back to public announcements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a credentialed API and may create or persist a local trial account credential. <br>
Mitigation: Prefer a user-provided ZLBX_API_KEY, require explicit consent before auto-registration, and never expose API keys in conversation or reports. <br>
Risk: Generated reports may include signed no-login links, local HTML files, or business contact data. <br>
Mitigation: Treat generated reports and signed links as sensitive, share them only with intended recipients, and use contact data only for legitimate and lawful business purposes. <br>
Risk: Queries consume account credits and company-intelligence conclusions can be incomplete if public bidding data is missing or delayed. <br>
Mitigation: Disclose estimated credit use before running, preserve source links and data-boundary notes, and review conclusions before relying on them for business decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-winner-company-profile) <br>
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun) <br>
- [API quick reference](references/api-quick.md) <br>
- [Workflow guide](references/workflow.md) <br>
- [Report template](references/report-template.md) <br>
- [Auto-registration guide](references/auto-register.md) <br>
- [知了商机大师](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown reports in chat, with optional generated HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY; reports should include source links, data boundaries, and absolute paths for generated HTML files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
