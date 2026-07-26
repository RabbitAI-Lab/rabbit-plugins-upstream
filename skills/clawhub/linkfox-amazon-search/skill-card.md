## Description: <br>
Simulates Amazon storefront searches and returns real-time search results data such as product positions, prices, ratings, review counts, brands, delivery details, and sponsored status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, e-commerce analysts, and agent users use this skill to inspect live Amazon search result pages for keyword ranking, competitor discovery, price comparison, sponsored product analysis, and new product monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flagged that the skill sends Amazon search terms, marketplace settings, delivery ZIPs, API credentials, and session-related headers to LinkFox. <br>
Mitigation: Use only approved LinkFox credentials, avoid sensitive business queries unless necessary, and confirm the user is comfortable sharing the requested search context before calling the API. <br>
Risk: Raw search responses are saved on disk and may contain query details, product data, delivery simulation settings, and session metadata. <br>
Mitigation: Run the skill in a dedicated workspace, inspect generated linkfox files before sharing them, and delete saved response files when they are no longer needed. <br>
Risk: Each Amazon search consumes LinkFox credits, and repeated retries, pagination, or parameter changes can increase cost. <br>
Mitigation: Explain additional credit usage before follow-up searches and avoid automatic retries, keyword changes, page turns, or delivery ZIP changes without user confirmation. <br>
Risk: The artifact includes onboarding-download and feedback-reporting flows that may contact LinkFox services beyond the search API. <br>
Mitigation: Ask for explicit user consent before downloading onboarding materials or sending feedback, and skip those flows when they are not needed for the task. <br>


## Reference(s): <br>
- [亚马逊前端搜索模拟 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON files, guidance] <br>
**Output Format:** [Markdown summaries and tables with optional shell commands and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full responses are saved under a local linkfox session data directory; large responses are summarized unless inline output is explicitly requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
