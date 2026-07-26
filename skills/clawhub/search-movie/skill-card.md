## Description: <br>
一个基于 Model Context Protocol (MCP) 构建的智能电影和电视剧资源搜索工具，支持多源搜索和链接验证。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search for movie or TV resources, then validate candidate playback links before presenting results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and reuses a service API key from a plain local .env file. <br>
Mitigation: Use a dedicated XiaoBenYang key, avoid shared or version-controlled workspaces, and check whether an existing .env already contains XBY_APIKEY before running the skill. <br>
Risk: The security summary notes confusing leftover configuration from another skill. <br>
Mitigation: Review the configuration values and outputs before use to confirm they match the movie-search workflow and expected XiaoBenYang service account. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/search-movie) <br>
- [XiaoBenYang API key service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, API calls] <br>
**Output Format:** [JSON API results summarized as human-facing text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key before search or validation calls can run.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
