## Description: <br>
A WeChat Official Account benchmarking skill that uses RedFox data to recommend peer benchmark accounts and higher-performing aspirational accounts from account names, IDs, or categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
WeChat creators, brand marketers, MCN teams, and content operators use this skill to find comparable public accounts, inspect recent article performance, and identify operational patterns for launch, content planning, advertising, or competitive analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a RedFox API key and may read it from user shell profiles. <br>
Mitigation: Set REDFOX_API_KEY only for the current session or through a secure secret manager, and avoid hard-coding or committing the key. <br>
Risk: Queried account details and submitted WeChat IDs are sent to RedFox services. <br>
Mitigation: Use the skill only when users are comfortable sharing those identifiers with RedFox, and avoid submitting sensitive or unnecessary account data. <br>
Risk: The sync flow can display a success confirmation even if the RedFox sync request fails. <br>
Mitigation: Treat sync confirmations as pending unless the API response is verified, and update the skill before relying on sync status for operational decisions. <br>


## Reference(s): <br>
- [Core workflow](references/core_workflow.md) <br>
- [RedFox Hub](https://redfox.hk/) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-similar-account) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with tables, inline shell commands, and short JSON status output for sync submissions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY and may include account metrics, recommendation reasons, subscription prompts, and enterprise-service guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
