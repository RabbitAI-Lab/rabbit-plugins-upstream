## Description: <br>
Searches Weibo posts through the RedFox API by keyword, with support for sort modes, verification filters, pagination, empty-result keyword expansion, and daily keyword subscriptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operators, creators, brand teams, and PR users use this skill to find current Weibo posts for topic research, trend discovery, creator screening, and mention monitoring. It returns filtered post results and can help set up daily keyword checks when the user confirms a subscription. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Daily keyword subscriptions may create persistent scheduled automation without enough visible scoping or cancellation controls. <br>
Mitigation: Before confirming a subscription, verify where the schedule is stored, what timezone it uses, how to disable it, and whether the query scope is appropriate. <br>
Risk: The skill depends on a RedFox API key for live Weibo searches. <br>
Mitigation: Store REDFOX_API_KEY only in environment or approved local configuration, avoid exposing it in prompts or logs, and rotate or revoke it if it may have been disclosed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/weibo-realtime-search-redfox) <br>
- [RedFoxHub API Keys](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown search summaries and tables, plus JSON output from the helper script when invoked directly] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a REDFOX_API_KEY environment variable. Search results include post text, author, engagement counts, links, page state, and filter labels.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
