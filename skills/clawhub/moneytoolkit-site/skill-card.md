## Description: <br>
小O的赚钱工具箱 provides a dashboard for monitoring UUMit digital assets, ClawHub paid skills, wallet balance, pricing, and task progress. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cx75227-ops](https://clawhub.ai/user/cx75227-ops) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can use this skill as an informational site to monitor UUMit assets, ClawHub paid-skill status, wallet balances, pricing, and monetization workflow progress. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The frontend contacts api.uumit.com and displays live account or asset information. <br>
Mitigation: Review the network call and avoid using the skill with private account data unless the API behavior and browser credential handling are understood. <br>
Risk: The skill references use of the logged-in @cx75227-ops ClawHub account context. <br>
Mitigation: Confirm the installed environment and account context before relying on displayed ClawHub status or monetization data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cx75227-ops/skills/moneytoolkit-site) <br>
- [Publisher profile](https://clawhub.ai/user/cx75227-ops) <br>
- [UUMit digital assets API](https://api.uumit.com/api/v1/digital-assets) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions and static HTML site files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a frontend dashboard that fetches live UUMit asset data and displays ClawHub account status.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
