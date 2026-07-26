## Description: <br>
Queries FastMoss data for TikTok Shop top-selling product rankings across supported global markets by day, week, or month, with optional category and sorting filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, e-commerce sellers, and analysts use this skill to retrieve TikTok Shop ranking data for product scouting, trend analysis, and competitive intelligence. It returns ranking data for supported markets and time windows rather than providing subjective business advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends ranking requests and API credentials to LinkFox services as part of a paid FastMoss workflow. <br>
Mitigation: Use dedicated LinkFox API credentials, limit who can run the skill, and confirm the user accepts the credit cost before repeated calls. <br>
Risk: Full API responses are saved locally and may include business query context or retrieved ranking data. <br>
Mitigation: Run the skill only in approved workspaces, review the linkfox output directory, and avoid sensitive business queries when local retention is not acceptable. <br>
Risk: Error handling can direct the agent toward installing a separate onboarding skill or sending feedback content. <br>
Mitigation: Require explicit user approval before installing additional skills, downloading onboarding assets, or sending feedback to LinkFox. <br>


## Reference(s): <br>
- [FastMoss-TikTok热销榜 ClawHub listing](https://clawhub.ai/linkfox-ai/skills/linkfox-fastmoss-product-rank-top-selling) <br>
- [FastMoss top-selling API reference](references/api.md) <br>
- [LinkFox tool gateway endpoint](https://tool-gateway.linkfox.com/fastmoss/productRankTopSelling) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API parameters, shell command examples, saved JSON data files, and concise tabular result summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials from environment variables. The script uses a 24-hour local cache, writes full API responses under a linkfox session data directory, and may summarize large responses unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
