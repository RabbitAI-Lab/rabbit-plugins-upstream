## Description: <br>
Searches X/Twitter by keyword across Top, Latest, Media, People, and Lists modes and returns structured post, engagement, media, and author information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations, marketing, brand, and content teams use this skill to search X/Twitter posts, users, and lists by keyword for trend tracking, competitor analysis, brand monitoring, and content research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: X/Twitter search terms and pagination data are sent to redfox.hk using the user's RedFox API key. <br>
Mitigation: Avoid sensitive searches when third-party processing is not acceptable, and configure the API key only through the documented environment, config file, or command-line mechanisms. <br>
Risk: Search results may include public author profile details, locations, engagement metrics, and media URLs. <br>
Mitigation: Treat returned social data as third-party public content and review it before reuse, publication, or downstream analysis. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/redfox-data/redfox-community/tree/main/skills/twitter-work-search) <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/twitter-work-search) <br>
- [Core workflow](references/core_workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown tables and short explanatory text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns up to 20 results per page and may include pagination prompts when additional results are available.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
