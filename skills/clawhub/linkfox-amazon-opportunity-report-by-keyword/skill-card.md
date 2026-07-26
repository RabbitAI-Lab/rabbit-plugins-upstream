## Description: <br>
Generates AI-powered Amazon US keyword opportunity reports covering market potential, product characteristics, reviews, customer profiles, search trends, and pricing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers and e-commerce researchers use this skill to generate keyword-level market opportunity reports for US marketplace product research and selection decisions. <br>

### Deployment Geography for Use: <br>
United States marketplace data; usable globally where LinkFox and Amazon US market research are appropriate. <br>

## Known Risks and Mitigations: <br>
Risk: Paid LinkFox API calls may consume credits. <br>
Mitigation: Confirm the user wants to continue before running report generation, especially when retrying after failures or empty results. <br>
Risk: Full report JSON and session-linked metadata are saved locally. <br>
Mitigation: Use the skill only for non-confidential product research unless local retention of report data is acceptable. <br>
Risk: Feedback reporting can send broad user intent or result-quality details to LinkFox. <br>
Mitigation: Review feedback content before reporting and avoid including confidential product, account, or strategy details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-opportunity-report-by-keyword) <br>
- [API reference](references/api.md) <br>
- [LinkFox skills](https://skill.linkfox.com/) <br>
- [LinkFox API key guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>
- [LinkFox account portal](https://os.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown report from the API, with full JSON response saved locally and summarized on stdout for large responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key, supports the Amazon US marketplace only, uses a 24-hour local cache for repeated parameter combinations, and may consume paid LinkFox credits.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
