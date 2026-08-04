## Description: <br>
Retrieves translated patent description or specification text from the Zhihuiya data service in Chinese, English, or Japanese using patent IDs or publication numbers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and patent professionals use this skill to retrieve translated patent description text for a known patent ID or publication number. It supports batch lookup, language selection, and optional family-member substitution when the original description is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent query results, which may include full translated descriptions, are written to local LinkFox folders and cached. <br>
Mitigation: Use the skill in a dedicated workspace when handling sensitive patent material, review saved JSON files after use, and clear local cache or session files when retention is not desired. <br>
Risk: The skill includes feedback-reporting behavior and external onboarding or install instructions. <br>
Mitigation: Require explicit user approval before sending feedback or downloading additional skills, and review any onboarding source before installation. <br>
Risk: Patent lookups consume LinkFox credits and batch requests can multiply cost. <br>
Mitigation: Confirm cost-sensitive or repeated queries with the user before proceeding, especially for batch lookups or retries after empty results. <br>


## Reference(s): <br>
- [智慧芽-说明书翻译 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-description-data-translated) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, files] <br>
**Output Format:** [Markdown guidance with JSON API responses and locally saved JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script saves full responses under a local linkfox session directory, caches matching requests for 24 hours, prints small responses inline, and summarizes larger responses unless --inline is used.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
