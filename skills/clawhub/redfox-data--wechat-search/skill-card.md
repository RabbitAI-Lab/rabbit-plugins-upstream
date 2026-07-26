## Description: <br>
Searches recent high-read WeChat Official Account articles by keyword and returns ranked trend results for content planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, WeChat operators, brands, and self-media teams use this skill to find viral WeChat article examples, track niche trends, and set up recurring keyword checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports a hardcoded secret-looking API key in a reference file. <br>
Mitigation: Configure your own REDFOX_API_KEY, do not rely on or redistribute the bundled example key, and rotate any exposed key before use. <br>
Risk: Search keywords are sent to RedFox when the skill queries article trends. <br>
Mitigation: Avoid sensitive or confidential search terms and only use the skill when sharing query text with RedFox is acceptable. <br>
Risk: The skill can create recurring calendar-based subscription prompts for future article checks. <br>
Mitigation: Review the subscription prompt and schedule before allowing calendar creation, and keep only subscriptions that match the intended keyword and cadence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-search) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [gzh_trend_data_format.md](references/gzh_trend_data_format.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, HTML files, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown tables and prompts for users, JSON from the helper script, and optional HTML report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a REDFOX_API_KEY and sends search keywords to RedFox; results cover recent indexed WeChat articles with 5,000+ reads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
