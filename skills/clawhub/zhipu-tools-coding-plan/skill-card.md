## Description: <br>
智谱 Coding Plan 免费工具：网络搜索、网页读取、GitHub 仓库文档搜索、文件解析、视觉理解(GLM-4.6V)、额度查询。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wnzzer](https://clawhub.ai/user/wnzzer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search the web, read webpages, inspect GitHub repository documentation, parse local documents, analyze images or videos, and check Zhipu Coding Plan usage from a command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send searches, URLs, GitHub repository names, selected local documents, screenshots, images, or videos to Zhipu/Z.AI services. <br>
Mitigation: Use it only for data the user intends to share with Zhipu/Z.AI, and avoid confidential files or media unless explicit upload is acceptable. <br>
Risk: Some documented paths can use Legacy account-billed APIs or have inconsistent fallback and cost disclosures. <br>
Mitigation: Keep MCP mode enabled for normal use, require explicit approval before setting ZHIPU_USE_MCP=false, and warn users when a command may use account balance. <br>
Risk: The skill requires a ZHIPU_API_KEY that can authorize remote service calls. <br>
Mitigation: Store the key outside source control, scope or rotate it where possible, and avoid exposing it in logs or shared configuration. <br>
Risk: Quota and balance reporting relies on a documented skill behavior that may change if Zhipu adjusts API responses or billing rules. <br>
Mitigation: Treat quota output as operational guidance and re-check provider billing or account dashboards before making high-impact usage decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wnzzer/skills/zhipu-tools-coding-plan) <br>
- [Z.AI Open Platform](https://open.bigmodel.cn/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text summaries with optional JSON for raw quota output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include search results, webpage text, repository file content, document parsing results, visual analysis, and quota details.] <br>

## Skill Version(s): <br>
3.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
