## Description: <br>
Seerfar-Ozon市场关键词搜索 helps agents query LinkFox's Seerfar Ozon keyword database and return market metrics for Ozon and Wildberries keyword research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace researchers, e-commerce operators, and agent workflows use this skill to discover and rank Ozon market keywords by search volume, growth, competition, seller counts, price, sales, and related market indicators. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LinkFox receives Ozon keyword queries, session/app identifiers, and the API credential needed for billing. <br>
Mitigation: Use only approved LinkFox credentials and avoid submitting sensitive keyword research or identifiers unless that data sharing is authorized. <br>
Risk: Full market research responses and cache files are saved under generated linkfox directories. <br>
Mitigation: Review local output locations and periodically delete saved files when the market research data is sensitive. <br>
Risk: The skill includes automatic external feedback reporting behavior. <br>
Mitigation: Review the feedback-reporting instruction before use and avoid including confidential details in any feedback content. <br>
Risk: Repeated API calls consume LinkFox credits. <br>
Mitigation: Confirm expected credit use before high-frequency searches or repeated pagination. <br>


## Reference(s): <br>
- [Seerfar Ozon 市场热词搜索 API 参考](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-market-keyword-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries and tables, shell commands, and JSON API responses saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are persisted under linkfox session data directories; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
