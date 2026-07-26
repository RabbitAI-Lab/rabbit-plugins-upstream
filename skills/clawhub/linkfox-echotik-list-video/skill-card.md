## Description: <br>
Searches and analyzes TikTok video data across supported TikTok Shop marketplaces with filters for region, creator, product, category, engagement, duration, publish time, ads, AI content, and selling-video status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketers, and analysts use this skill to find TikTok videos, compare content performance, and inspect estimated engagement, sales, and GMV metrics before making content or campaign decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends API requests to LinkFox services and may report feedback to a LinkFox feedback endpoint. <br>
Mitigation: Install only when LinkFox API use is acceptable, constrain LINKFOX_TOOL_GATEWAY to the intended host, and review or disable feedback behavior before use in sensitive workflows. <br>
Risk: The script saves full analytics responses and request caches locally, which may expose marketplace research data in shared or synced workspaces. <br>
Mitigation: Run it from an appropriate workspace, review the linkfox output directory before sharing a project, and delete saved responses or caches when they are no longer needed. <br>
Risk: Calls consume LinkFox credits, and repeated pagination or exploratory queries can increase cost. <br>
Mitigation: Use narrow filters and pagination deliberately, rely on the 24-hour cache for repeated parameters, and confirm with the user before high-frequency calls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-video) <br>
- [EchoTik TikTok video list API reference](references/api.md) <br>
- [LinkFox API key guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables and summaries, shell command examples, and saved JSON response files with optional full JSON stdout.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a region parameter, uses LinkFox API credentials, caches matching requests for 24 hours, and saves full responses locally for later inspection.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
