## Description: <br>
Looks up known TikTok Shop products by ID or URL and returns batch product performance metrics, including sales, GMV, livestream, video, influencer, price, rating, commission, and status data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and analysts use this skill to compare known TikTok Shop products side by side using multi-period sales, GMV, live commerce, video, influencer, price, review, commission, and product status metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TikTok product IDs, product URLs, and analytics requests are sent to LinkFox. <br>
Mitigation: Use the skill only for product research data you are comfortable sharing with LinkFox. <br>
Risk: Full API responses are stored locally and may include sensitive product research results. <br>
Mitigation: Run the skill in a dedicated workspace and clean the generated linkfox data and cache directories when results are no longer needed. <br>
Risk: The skill may submit feedback to LinkFox and may guide installation of a separate onboarding skill for account or credit issues. <br>
Mitigation: Review feedback behavior and approve any onboarding skill installation only when you trust the source. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-batch-product-detail) <br>
- [EchoTik-TikTok商品批量详情 API 参考](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, files, guidance] <br>
**Output Format:** [Markdown guidance, shell command examples, stdout JSON or summaries, and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes full responses under a local linkfox session data directory, uses a 24-hour local cache by default, and can print full responses with --inline.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
