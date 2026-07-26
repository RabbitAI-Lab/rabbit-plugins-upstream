## Description: <br>
This Chinese-language skill helps security monitoring and intelligent-building bidders evaluate target tenders, compare buyer history and competitors, estimate pricing, and produce a bid-decision report from public bidding data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bid teams and intelligent-building contractors use this skill to decide whether to pursue a specific security monitoring, weak-current, cabling, machine-room, access-control, or building-automation tender. It produces a decision-oriented report covering buyer history, incumbent supplier signals, likely competitors, comparable awards, pricing guidance, qualification thresholds, and no-bid risks. <br>

### Deployment Geography for Use: <br>
Global; analysis is focused on Chinese public bidding data and vendor services. <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports that the skill contacts vendor services, can create an account after consent, and stores an API key under the user's home directory. <br>
Mitigation: Install only when those vendor-service and credential-storage behaviors are acceptable; prefer a user-provided ZLBX_API_KEY when available and avoid sharing credentials in chat. <br>
Risk: Generated reports can contain signed vendor links and bid-analysis details that may be confidential. <br>
Mitigation: Treat generated reports and links as confidential, review recipients before sharing, and avoid publishing report files in public locations. <br>
Risk: The security summary flags the release as suspicious because persistent credential/account flows and shareable report exports are not fully contained. <br>
Mitigation: Review the skill's behavior before deployment, keep generated files in controlled directories, and use it only in environments where the vendor API and local report writing are permitted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/intelligent-building-bid-decision) <br>
- [ZhiLiaoBiaoXun API endpoint pattern](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool}) <br>
- [Manual account setup](https://ai.zhiliaobiaoxun.com/?ch=s81) <br>
- [ZhiLiao business intelligence portal](https://agent.zhiliaobiaoxun.com) <br>
- [Biaoshu proposal-writing service](https://biaoshu.zhiliaobiaoxun.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown report in chat, with optional local HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a ZLBX_API_KEY credential or consent-based account setup; complete reports typically consume 12-25 vendor query credits and quick checks consume about 5-8 credits.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
