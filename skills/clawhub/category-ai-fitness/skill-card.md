## Description: <br>
输入三级类目表，自动抓取 Amazon/Walmart TOP 商品主图，用 Claude 多模态分析并输出类目级决策表，覆盖 AI 改图适配度、侵权风险、经济性和竞争度。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liwenzhen1108-png](https://clawhub.ai/user/liwenzhen1108-png) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Merchandising, ecommerce, and operations users can analyze category lists or marketplace category URLs to decide whether product images are suitable for AI image adaptation, direct reuse, cautious review, or rejection. The skill supports both a Streamlit UI and CLI workflow for producing category-level reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Result summaries may be sent to a hardcoded Feishu webhook. <br>
Mitigation: Review or remove the Feishu webhook behavior before installation or execution. <br>
Risk: Credentials and sensitive configuration are handled broadly, including a bundled config.env credential. <br>
Mitigation: Remove bundled credentials, rotate exposed secrets, and provide required API keys only through a controlled local environment. <br>
Risk: Category lists, product strategy, downloaded images, and generated recommendations may leave the local machine through external services. <br>
Mitigation: Run only with data approved for LinkFox, Anthropic or the configured Anthropic-compatible endpoint, Walmart/image hosts, and any enabled notification endpoint. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liwenzhen1108-png/category-ai-fitness) <br>
- [Publisher profile](https://clawhub.ai/user/liwenzhen1108-png) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Release metadata](artifact/_meta.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Streamlit UI output and Excel reports, with CLI text logs and generated spreadsheet files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3, LINKFOXAGENT_API_KEY, and ANTHROPIC_API_KEY or compatible Anthropic authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact/_meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
