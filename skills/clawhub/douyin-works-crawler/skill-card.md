## Description: <br>
Retrieves Douyin account profile details and up to 50 recent works through RedFox data APIs, returning engagement metrics, direct links, and account-level highlights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Brands, MCN operators, Douyin creators, and data analysts use this skill to inspect a Douyin account's recent works, engagement metrics, and content patterns. It can also guide account indexing when RedFox has not yet collected the requested account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that the script prints part of the RedFox API key in output, which could expose credential material in shared logs or CI systems. <br>
Mitigation: Use a revocable RedFox API key, avoid running the skill in shared logs or CI until the partial key print is removed, and rotate the key if logs may have been exposed. <br>
Risk: The security review notes that Douyin account identifiers are sent to RedFox for lookup or indexing. <br>
Mitigation: Only submit Douyin account IDs that the user is comfortable sending to RedFox, and clarify consent before using the indexing flow for accounts that are not already collected. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/redfox-data/skills/douyin-works-crawler) <br>
- [Core workflow reference](artifact/references/core_workflow.md) <br>
- [RedFoxHub API keys](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown report by default, with optional JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; outputs are limited to RedFox-returned data and recent works, typically up to 50 items.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
