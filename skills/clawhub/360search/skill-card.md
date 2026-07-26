## Description: <br>
360 Web Search lets an agent query 360 Search APIs for real-time Chinese web, news, AI search, and image search results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tonylwj](https://clawhub.ai/user/tonylwj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs current Chinese web, news, market, policy, product, or image-search information from 360 Search APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms, UUID session IDs, and selected image-search inputs are sent to api.360.cn using the configured 360 API key. <br>
Mitigation: Do not use the skill for secrets, private personal data, or proprietary prompts unless that external disclosure is acceptable. <br>
Risk: Broad activation wording may cause agents to use third-party search for many current-information requests. <br>
Mitigation: Narrow activation triggers or require confirmation before search when tighter control over external requests is needed. <br>


## Reference(s): <br>
- [360 AI Open Platform](https://ai.360.com/platform) <br>
- [ClawHub skill page](https://clawhub.ai/tonylwj/skills/360search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown search results and setup guidance with inline shell commands when credentials are missing] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SEARCH_360_API_KEY and outbound HTTPS access to api.360.cn; search responses may include returned source URLs.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata, SKILL.md frontmatter, README version history) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
