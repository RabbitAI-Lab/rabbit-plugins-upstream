## Description: <br>
Searches Douyin for viral content by keyword and optional date range, then presents engagement data in structured result tables. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, MCN and brand operators, growth teams, and marketing teams use this skill to find high-engagement Douyin works, compare content performance, and monitor keyword trends. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends a RedFox API key and Douyin search terms to redfox.hk. <br>
Mitigation: Confirm the key scope, retention policy, and reset or revocation process before use; keep the key in environment configuration rather than prompts, logs, or source files. <br>
Risk: The subscription feature can create persistent daily scheduled tasks. <br>
Mitigation: Before enabling daily pushes, confirm where the task will be created, how to pause or delete it, and what keyword and date data will be retained. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/douyin-search-redfox) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk) <br>
- [RedFoxHub enterprise service](https://redfox.hk/dashboard/enterprise) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown tables and text, with helper-script JSON used as the source data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search output includes clickable Douyin work links, engagement counts, publication time, hot recommendations, and optional subscription guidance.] <br>

## Skill Version(s): <br>
1.0.4 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
