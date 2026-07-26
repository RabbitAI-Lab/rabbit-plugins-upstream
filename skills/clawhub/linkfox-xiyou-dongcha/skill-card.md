## Description: <br>
Provides Amazon ASIN and keyword analytics via Xiyou Insights through the LinkFox gateway, covering traffic scores, reverse ASIN keyword lookup, ranking and traffic trends, BSR, ABA weekly trends, keyword competition, and suggested CPC across supported Amazon marketplaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and ecommerce analysts use this skill to query Xiyou Amazon marketplace data for ASIN research, keyword discovery, traffic and rank trend review, and competitive keyword analysis. It requires LinkFox and Xiyou credentials before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ASINs, keywords, Xiyou credentials, and analytics requests are sent through an external LinkFox gateway to the Xiyou service. <br>
Mitigation: Use only in environments where this data sharing is acceptable, and configure credentials through environment variables rather than prompts, files, or chat messages. <br>
Risk: Full analytics responses are saved locally as plaintext JSON and may contain commercially sensitive product research. <br>
Mitigation: Run the skill in a controlled workspace, restrict access to generated linkfox output directories, and clean saved responses when they are no longer needed. <br>
Risk: The security review notes that feedback can be sent to an external endpoint without clear user confirmation. <br>
Mitigation: Do not submit feedback automatically when the content is confidential or not safe to share with the provider. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-xiyou-dongcha) <br>
- [西柚找词 API 参考](references/api.md) <br>
- [Xiyou Insights OpenAPI console](https://www.xydc.com/openapi?xiyou-insights-web=%2Fopenapi) <br>
- [Xiyou OpenAPI](https://openapi.xiyouzhaoci.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved locally as JSON; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
0.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
