## Description: <br>
Subscribes to Douyin accounts, fetches recent work metrics on a daily schedule, and produces Markdown summaries and HTML reports for account monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operators, short-video creators, brands, MCNs, and analysts use this skill to subscribe to Douyin IDs, monitor account updates, and generate daily Markdown and HTML reports for competitor or niche tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a RedFox API key and sends subscribed Douyin IDs to redfox.hk. <br>
Mitigation: Install only when that data sharing is acceptable; keep REDFOX_API_KEY scoped, revocable, and out of prompts, logs, and output files. <br>
Risk: The skill can create or modify recurring daily automation with account IDs embedded in automation commands. <br>
Mitigation: Review recurring automation after subscription changes, remove accounts that are no longer needed, and avoid embedding sensitive monitoring lists. <br>
Risk: The skill writes local reports and failure-state files and may auto-open generated HTML reports. <br>
Mitigation: Review generated reports before sharing and remove local artifacts when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/redfox-data/skills/douyin-subscribe) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [Douyin data API endpoint](https://redfox.hk/story/api/dy/data/listWorkByAccount) <br>
- [API test parameters](references/test_api_params.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration] <br>
**Output Format:** [Markdown tables, local HTML report files, and command/configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses REDFOX_API_KEY, sends subscribed Douyin IDs to redfox.hk, and may create recurring daily automation plus local report and failure-state files.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
