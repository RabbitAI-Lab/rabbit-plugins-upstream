## Description: <br>
Searches Douyin viral works by keyword and optional date range, then returns structured engagement data and links for content research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content creators, MCN and brand operators, growth teams, and marketers use this skill to research Douyin content trends, compare engagement for keyword-based categories, and optionally set up daily keyword tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search keywords and date filters are sent to redfox.hk when the skill runs. <br>
Mitigation: Use the skill only when that data sharing is acceptable for the user's task and organization. <br>
Risk: The skill requires REDFOX_API_KEY, which could grant access to a RedFox account or service quota. <br>
Mitigation: Store the key in the environment or approved local configuration, treat it as sensitive, and avoid committing or logging it. <br>
Risk: Daily subscription tasks may continue running after the initial search. <br>
Mitigation: Review the proposed schedule before creation and remove the task when ongoing monitoring is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/douyin-search-redfox) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables with inline links and optional shell commands; script output is JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include title, author, engagement counts, work URL, publish time, pagination fields, and optional daily subscription guidance.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
