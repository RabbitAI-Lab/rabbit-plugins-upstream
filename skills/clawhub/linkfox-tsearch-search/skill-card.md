## Description: <br>
Tsearch-网页实时搜索 lets agents search the live web and retrieve extracted page content for current news, facts, Reddit and community discussions, product research, trends, and online references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs current online information, source pages, market or product research, recent news, community discussion, or other live web context. It is suited to summarizing retrieved web results with source titles and URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, retrieved content, and feedback details may be sent to LinkFox services. <br>
Mitigation: Avoid sensitive personal, financial, medical, credential, or proprietary searches unless LinkFox data handling and retention are acceptable. <br>
Risk: The skill uses LinkFox credits and may incur user-visible cost. <br>
Mitigation: Warn users before high-frequency use or when credit consumption may exceed expectations. <br>
Risk: Full search responses may be stored on disk by the helper script. <br>
Mitigation: Review the generated local response files and remove them when results contain sensitive or unnecessary retained content. <br>
Risk: The skill may direct agents to install the LinkFox onboarding skill when credentials or credits are missing. <br>
Mitigation: Review the onboarding download step and obtain user authorization before installing additional skills. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tsearch-search) <br>
- [Publisher profile](https://clawhub.ai/user/linkfox-ai) <br>
- [API reference](references/api.md) <br>
- [LinkFox skill guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown summaries with source titles and URLs, plus JSON search responses or compact response summaries from the helper script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key, consumes LinkFox credits, can call LinkFox feedback, and may persist full search responses to local files.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
