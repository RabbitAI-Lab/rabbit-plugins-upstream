## Description: <br>
Uses multimodal AI to analyze product main images and extract structured visual attributes, groupings, and image prompts for e-commerce product records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, analysts, and agent developers use this skill to turn product image URLs and product records into structured visual attributes such as color, material, shape, style, and prompt-like descriptions. It is suited for product image analysis, visual grouping, and factual attribute summaries when upstream product data is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product image URLs, prompts, product records, and feedback content may be sent to LinkFox services. <br>
Mitigation: Install and run only when that data sharing is acceptable; avoid submitting sensitive product or business data unless authorized. <br>
Risk: Generated response and cache files may retain product or business data locally. <br>
Mitigation: Review the generated LinkFox output and cache files after use, and delete them when retention is not appropriate. <br>
Risk: API keys and gateway settings control access to LinkFox services. <br>
Mitigation: Keep LINKFOX_AGENT_API_KEY, LINKFOXAGENT_API_KEY, and LINKFOX_TOOL_GATEWAY restricted to trusted environments. <br>
Risk: The skill can report feedback automatically based on user reactions or perceived mismatches. <br>
Mitigation: Review feedback behavior before deployment and avoid including sensitive user or product details in feedback content. <br>
Risk: Image analysis consumes LinkFox credits and can become costly for large batches or additional images. <br>
Mitigation: Warn users before running credit-consuming analysis and confirm scope before repeated or expanded calls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-extract-attributes) <br>
- [分析商品主图 API 参考](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables and summaries with JSON response files and optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires product records with accessible image URLs; may persist full LinkFox API responses and cache files locally while printing summaries for large responses.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
