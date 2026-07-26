## Description: <br>
A free news-fetching agent skill that uses a public news API to retrieve daily news lists, hot-topic rankings, article details, and category-filtered results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to ask an agent for daily news summaries, historical daily news by date, hot news rankings, and article details from a news API. It is intended for personal news browsing and quick information retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation and unrelated data-analysis or reporting language could cause the skill to run outside explicit news-fetching requests. <br>
Mitigation: Enable the skill only for clear news-list, news-detail, date-based news, hot-news, or category-filtering requests. <br>
Risk: The skill asks the agent to use shell commands for API calls and includes examples that write summaries or cache files to the user's home directory. <br>
Mitigation: Review commands before execution, use trusted news API endpoints, and limit file writes to expected summary or cache paths. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-news-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call an external news API and may write optional news summaries or cache files under the user's home directory when the agent follows the provided examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
